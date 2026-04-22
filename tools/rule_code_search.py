from __future__ import annotations

import argparse
import csv
import fnmatch
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


DATABASE_ROOT = Path(r"C:\wujiangliang\app\xiangshan\database_beginner")
PAPER_CATALOG_FILE = DATABASE_ROOT / "paper_catalog.tsv"
RULE_CATALOG_FILE = DATABASE_ROOT / "rule_catalog.tsv"

OUTPUT_BASE = Path(r"C:\wujiangliang\app\search")
OUTPUT_DIR: Path = OUTPUT_BASE

BINARY_EXTS = {
    ".so", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".ico",
    ".ttf", ".otf", ".woff", ".woff2",
    ".dex", ".arsc",
    ".mp3", ".mp4", ".wav", ".amr", ".aac", ".ogg", ".m4a", ".flac",
    ".zip", ".jar", ".apk", ".aab",
    ".pdf", ".class",
    ".pyc",
}

MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024

MAX_HITS_PER_RULE_DEFAULT = 80

MAX_HITS_PER_RULE_TIGHT = 40
HIGH_FREQ_RULES = {
    "BR001", "BR002", "BR003", "BR004", "BR005",
    "BR013", "BR026", "BR027", "BR047", "BR080",
    "BR061", "BR062", "BR063", "BR066",
    "BR018", "BR019", "BR020", "BR025",
    "BR091", "BR092", "BR093", "BR094",
}

MAX_MATCHED_TEXT_LEN = 300


FALLBACK_STOP_WORDS = {
    "the", "and", "for", "with", "from", "that", "this", "these", "those",
    "where", "which", "when", "been", "have", "having", "should", "would",
    "could", "about", "into", "onto", "over", "under", "between", "because",
    "their", "there", "other", "some", "such", "than", "them", "then", "they",
    "also", "does", "done", "only", "very", "into", "include", "includes",
    "including", "using", "used", "uses", "apps", "app", "android", "code",
    "file", "files", "data", "test", "tests", "testing", "rule", "rules",
    "paper", "check", "checking", "checked", "signal", "signals", "evidence",
    "static", "dynamic", "network", "cloud", "policy", "resource", "resources",
    "minimum", "primary", "validation", "name", "where", "check",
}
FALLBACK_MIN_LEN = 5
FALLBACK_MAX_KEYWORDS = 12
FALLBACK_MULTI_REQUIRED = 2  

FALLBACK_FIELDS = [
    "risk_name",
    "where_to_check",
    "primary_static_or_code_signal",
    "app_data_resource_policy_signal",
    "dynamic_validation_signal",
    "cloud_network_signal",
    "minimum_evidence",
]



JAVA_KT = ["*.java", "*.kt", "*.smali"]
JAVA_KT_XML = JAVA_KT + ["*.xml"]
CODE_RES = JAVA_KT + ["*.xml", "*.json", "*.properties", "*.txt", "*.html", "*.js"]

SENS_HEALTH = [
    r"heart", r"blood", r"spo2?", r"sleep", r"step", r"temperature", r"temp",
    r"ecg", r"bpm", r"pressure", r"oxygen", r"calorie", r"weight", r"height",
]
SENS_IDENT = [
    r"token", r"password", r"Authorization", r"mac", r"bluetooth", r"bssid",
    r"imei", r"android_?id", r"device_?id", r"devid", r"user_?id", r"userid",
    r"account", r"profile", r"phone", r"email", r"address",
]
SENS_NET = [
    r"upload", r"sync", r"login", r"register", r"save", r"report",
    r"post", r"put", r"delete",
]
SENS_LOC = [r"lat", r"lon", r"latitude", r"longitude", r"gps", r"location"]


RULE_SEARCH_SPECS: Dict[str, dict] = {

    # ---- 1. Manifest / permissions / component exposure -------------------

    "BR001": {  # dangerous permission catalog (SMS/call/contacts etc.)
        "file_globs": ["AndroidManifest.xml", "*.xml"],
        "path_any": [r"AndroidManifest", r"manifest"],
        "line_any": [
            r"uses-permission",
        ],
        "near_any": [
            r"READ_SMS", r"RECEIVE_SMS", r"SEND_SMS", r"READ_CALL_LOG",
            r"WRITE_CALL_LOG", r"READ_CONTACTS", r"WRITE_CONTACTS",
            r"READ_PHONE_STATE", r"CALL_PHONE", r"ANSWER_PHONE_CALLS",
            r"CAMERA", r"RECORD_AUDIO", r"READ_CALENDAR", r"WRITE_CALENDAR",
        ],
        "near_window": 1,
    },
    "BR002": {  # location permissions
        "file_globs": ["AndroidManifest.xml", "*.xml"],
        "line_any": [r"uses-permission"],
        "near_any": [
            r"ACCESS_FINE_LOCATION", r"ACCESS_COARSE_LOCATION",
            r"ACCESS_BACKGROUND_LOCATION",
        ],
        "near_window": 1,
    },
    "BR003": {  # bluetooth permissions
        "file_globs": ["AndroidManifest.xml", "*.xml"],
        "line_any": [r"uses-permission"],
        "near_any": [
            r"BLUETOOTH(?:_SCAN|_CONNECT|_ADVERTISE|_ADMIN)?\b",
        ],
        "near_window": 1,
    },
    "BR004": {  # storage permissions
        "file_globs": ["AndroidManifest.xml", "*.xml"],
        "line_any": [r"uses-permission"],
        "near_any": [
            r"WRITE_EXTERNAL_STORAGE", r"READ_EXTERNAL_STORAGE",
            r"MANAGE_EXTERNAL_STORAGE", r"READ_MEDIA_IMAGES",
            r"READ_MEDIA_VIDEO", r"READ_MEDIA_AUDIO",
        ],
        "near_window": 1,
    },
    "BR005": {  # ad_id / AdServices
        "file_globs": ["AndroidManifest.xml", "*.xml"],
        "line_any": [r"uses-permission"],
        "near_any": [
            r"AD_ID", r"ACCESS_ADSERVICES_AD_ID",
            r"ACCESS_ADSERVICES_ATTRIBUTION",
            r"ACCESS_ADSERVICES_TOPICS",
        ],
        "near_window": 1,
    },
    "BR029": {  # exported activities
        "file_globs": ["AndroidManifest.xml", "*.xml"],
        "line_any": [r'android:exported\s*=\s*"true"'],
        "near_any": [r"<activity", r"<activity-alias"],
        "near_window": 4,
    },
    "BR030": {  # exported services
        "file_globs": ["AndroidManifest.xml", "*.xml"],
        "line_any": [r'android:exported\s*=\s*"true"'],
        "near_any": [r"<service"],
        "near_window": 4,
    },
    "BR031": {  # exported receivers
        "file_globs": ["AndroidManifest.xml", "*.xml"],
        "line_any": [r'android:exported\s*=\s*"true"'],
        "near_any": [r"<receiver"],
        "near_window": 4,
    },
    "BR059": {  # intent-filter exposure
        "file_globs": ["AndroidManifest.xml", "*.xml"],
        "line_any": [r"<intent-filter"],
        "near_any": [
            r"android\.intent\.action\.VIEW",
            r"android\.intent\.action\.SEND",
            r"android\.intent\.category\.BROWSABLE",
        ],
        "near_window": 6,
    },
    "BR071": {  # manifest package / application debuggable / allowBackup
        "file_globs": ["AndroidManifest.xml", "*.xml"],
        "line_any": [
            r'android:debuggable\s*=\s*"true"',
            r'android:allowBackup\s*=\s*"true"',
            r'android:testOnly\s*=\s*"true"',
        ],
        "near_window": 0,
    },

    # ---- 2. cleartext / TLS / network security config ---------------------

    "BR006": {  # usesCleartextTraffic=true
        "file_globs": ["*.xml"],
        "line_any": [r'usesCleartextTraffic\s*=\s*"true"'],
        "near_window": 0,
    },
    "BR007": {  # networkSecurityConfig / cleartextTrafficPermitted
        "file_globs": ["*.xml"],
        "line_any": [
            r"networkSecurityConfig",
            r'cleartextTrafficPermitted\s*=\s*"true"',
            r"<base-config", r"<domain-config",
        ],
        "near_window": 0,
    },
    "BR008": {  # trust-anchors user/debug/system
        "file_globs": ["*.xml"],
        "line_any": [r"<trust-anchors", r"<certificates"],
        "near_any": [r'src\s*=\s*"user"', r'src\s*=\s*"debug"', r'src\s*=\s*"system"'],
        "near_window": 4,
    },
    "BR009": {  # X509TrustManager empty implementations
        "file_globs": JAVA_KT,
        "line_any": [r"X509TrustManager", r"checkServerTrusted", r"checkClientTrusted"],
        "file_any": [r"TrustManager", r"SSLContext"],
        "near_window": 0,
    },
    "BR010": {  # HostnameVerifier return true
        "file_globs": JAVA_KT,
        "line_any": [r"HostnameVerifier", r"\bverify\s*\("],
        "near_any": [r"return\s+true", r"ALLOW_ALL"],
        "near_window": 6,
    },
    "BR011": {  # TLS error fallback to http
        "file_globs": JAVA_KT,
        "line_any": [
            r"SSLException", r"CertificateException", r"SSLHandshakeException",
        ],
        "near_any": [
            r"http://", r"fallback", r"retry", r"downgrade",
        ],
        "near_window": 10,
    },
    "BR012": {  # pinning presence or lack thereof
        "file_globs": JAVA_KT + ["*.xml"],
        "line_any": [
            r"CertificatePinner", r"\bpinCertificates\b", r"<pin-set",
            r"sha256/", r"PinningTrustManager",
        ],
        "near_window": 0,
    },
    "BR013": {  # http:// or ws:// with sensitive semantics nearby
        "file_globs": CODE_RES,
        "line_any": [r"http://", r"ws://"],
        "near_any": SENS_NET + SENS_IDENT + SENS_HEALTH + [r"device", r"mac"],
        "near_window": 5,
    },
    "BR077": {  # SSL/TLS config flags
        "file_globs": JAVA_KT,
        "line_any": [
            r"SSLSocketFactory", r"HttpsURLConnection", r"\bSSLContext\b",
            r"TLSv1(?:\.0|\.1)?",
        ],
        "near_any": [r"setHostnameVerifier", r"setSSLSocketFactory", r"init\s*\("],
        "near_window": 6,
    },
    "BR078": {  # OkHttp trust-all / bypass
        "file_globs": JAVA_KT,
        "line_any": [r"OkHttpClient", r"okhttp3", r"hostnameVerifier"],
        "near_any": [r"return\s+true", r"trustAllCerts", r"TrustManager"],
        "near_window": 6,
    },
    "BR079": {  # WebView mixed content / insecure settings
        "file_globs": JAVA_KT,
        "line_any": [
            r"setMixedContentMode", r"MIXED_CONTENT_ALWAYS_ALLOW",
            r"setAllowFileAccess", r"setAllowUniversalAccessFromFileURLs",
            r"setJavaScriptEnabled",
        ],
        "near_any": [r"WebView", r"WebSettings", r"return\s+true"],
        "near_window": 6,
    },
    "BR095": {  # cleartext uploads of sensitive data
        "file_globs": CODE_RES,
        "line_any": [r"http://"],
        "near_any": SENS_HEALTH + SENS_IDENT + [r"upload", r"sync", r"device"],
        "near_window": 6,
    },

    # ---- 3. URL / API / upload / cloud fields -----------------------------

    "BR091": {  # Retrofit / endpoint + upload/save/sync
        "file_globs": JAVA_KT,
        "line_any": [
            r"@POST\b", r"@GET\b", r"@PUT\b", r"@DELETE\b", r"@PATCH\b",
            r"@Multipart", r"@FormUrlEncoded",
        ],
        "near_any": [
            r"upload", r"save", r"sync", r"login", r"register", r"report",
            r"profile", r"user", r"device", r"heart", r"blood", r"sleep",
            r"spo", r"step", r"health",
        ],
        "near_window": 6,
    },
    "BR092": {  # health data upload
        "file_globs": JAVA_KT,
        "line_any": [
            r"upload", r"sync", r"report", r"save", r"postHealth",
            r"submit", r"reportHealth",
        ],
        "near_any": SENS_HEALTH,
        "near_window": 5,
    },
    "BR093": {  # device-info upload
        "file_globs": JAVA_KT,
        "line_any": [r"upload", r"sync", r"report", r"save", r"submit", r"post"],
        "near_any": [
            r"deviceId", r"devId", r"\bmac\b", r"phoneModel", r"osVersion",
            r"userId", r"uuid", r"imei", r"android_?id",
        ],
        "near_window": 5,
    },
    "BR094": {  # location upload
        "file_globs": JAVA_KT,
        "line_any": [r"upload", r"sync", r"report", r"save", r"submit", r"post"],
        "near_any": SENS_LOC,
        "near_window": 5,
    },
    "BR096": {  # cloud URL / host indicators
        "file_globs": CODE_RES,
        "line_any": [
            r"https?://[a-z0-9\-.]+\.(?:cn|com|net|io|co|org|top|xyz)",
        ],
        "near_any": SENS_NET + [r"api", r"cloud", r"server", r"base_?url", r"host"],
        "near_window": 3,
    },
    "BR097": {  # WebSocket / MQTT endpoints
        "file_globs": CODE_RES,
        "line_any": [r"\bwss?://", r"mqtt://", r"tcp://"],
        "near_any": SENS_NET + SENS_HEALTH + SENS_IDENT + [r"device", r"connect"],
        "near_window": 5,
    },
    "BR098": {  # Retrofit / OkHttp base url config
        "file_globs": JAVA_KT,
        "line_any": [r"baseUrl\s*\(", r"Retrofit\.Builder", r"OkHttpClient\.Builder"],
        "near_any": [r"https?://", r"addInterceptor", r"addConverterFactory"],
        "near_window": 6,
    },

    # ---- 4. Hardcoded secret / identifier / crypto ------------------------

    "BR014": {  # device identifier APIs
        "file_globs": JAVA_KT,
        "line_any": [
            r"TelephonyManager", r"getDeviceId", r"getImei", r"getMeid",
            r"getSubscriberId", r"getSimSerialNumber",
            r"AdvertisingIdClient", r"getAdvertisingIdInfo",
            r"Settings\.Secure\.ANDROID_ID",
        ],
        "near_window": 0,
    },
    "BR015": {  # Build/Locale/TimeZone + device info upload
        "file_globs": JAVA_KT,
        "line_any": [
            r"Build\.MODEL", r"Build\.BRAND", r"Build\.MANUFACTURER",
            r"Build\.SERIAL", r"Build\.DEVICE", r"Build\.PRODUCT",
            r"Locale\.getDefault", r"TimeZone\.getDefault",
        ],
        "near_any": [
            r"upload", r"sync", r"report", r"post", r"json", r"param",
            r"device", r"header", r"user_?agent", r"userAgent",
        ],
        "near_window": 6,
    },
    "BR016": {  # hardcoded tokens / secrets
        "file_globs": CODE_RES,
        "line_any": [
            r"Bearer\s+[A-Za-z0-9_\-.]{6,}",
            r"api_?key", r"app_?key", r"\bsecret\b", r"client_secret",
            r"access_?token", r"refresh_?token",
        ],
        "near_any": [
            r"static\s+final", r"Authorization", r"Header", r"const\s+val",
            r"\"[A-Za-z0-9_\-.]{16,}\"", r"=\s*\"[A-Za-z0-9_\-]{16,}\"",
        ],
        "near_window": 3,
    },
    "BR017": {  # crypto with hardcoded keys
        "file_globs": JAVA_KT,
        "line_any": [
            r"SecretKeySpec", r"IvParameterSpec",
            r"Cipher\.getInstance", r"\bAES\b", r"\bDES\b", r"\bRSA\b",
            r"Hmac(?:SHA|MD5)", r"MessageDigest",
        ],
        "near_any": [
            r"static\s+final", r"new\s+byte\s*\[", r"getBytes\s*\(",
            r"\"[A-Fa-f0-9]{16,}\"", r"\"[A-Za-z0-9+/=]{16,}\"",
        ],
        "near_window": 6,
    },
    "BR060": {  # ECB mode / weak cipher mode
        "file_globs": JAVA_KT,
        "line_any": [
            r"AES/ECB", r"DES/ECB", r"/ECB/", r"\"ECB\"",
            r"AES/CBC/PKCS5Padding",
        ],
        "near_window": 0,
    },

    # ---- 5. Health fields / local storage ---------------------------------

    "BR018": {  # health fields in model/dao/api/ble/parser
        "file_globs": JAVA_KT,
        "path_any": [
            r"(?:^|/)(?:model|bean|entity|dao|api|ble|parser|protocol)(?:/|$)",
        ],
        "line_any": SENS_HEALTH,
        "near_window": 0,
    },
    "BR019": {  # health field serialization
        "file_globs": JAVA_KT,
        "line_any": [
            r"@SerializedName", r"@JsonProperty", r"@JSONField", r"JSONObject",
            r"\.put\s*\(", r"toJson", r"fromJson",
        ],
        "near_any": SENS_HEALTH,
        "near_window": 3,
    },
    "BR020": {  # health data persisted to DB
        "file_globs": JAVA_KT,
        "line_any": [
            r"@Entity", r"@Table", r"@ColumnInfo", r"@Dao", r"Cursor",
            r"execSQL", r"CREATE\s+TABLE", r"INSERT\s+INTO", r"UPDATE\s+",
        ],
        "near_any": SENS_HEALTH,
        "near_window": 5,
    },
    "BR025": {  # local DB with health / profile / session / location
        "file_globs": JAVA_KT,
        "line_any": [
            r"SQLiteOpenHelper", r"SQLiteDatabase", r"RoomDatabase",
            r"openOrCreateDatabase", r"getWritableDatabase",
            r"getReadableDatabase",
        ],
        "near_any": SENS_HEALTH + [r"profile", r"session", r"user", r"location", r"heart", r"sleep"],
        "near_window": 8,
    },
    "BR026": {  # SharedPreferences / MMKV / DataStore with sensitive key
        "file_globs": JAVA_KT,
        "line_any": [
            r"SharedPreferences", r"getSharedPreferences",
            r"\bMMKV\b", r"mmkvWithID",
            r"DataStore", r"preferencesDataStore", r"PreferenceManager",
        ],
        "near_any": [
            r"token", r"mac", r"bluetooth", r"user", r"device",
            r"heart", r"blood", r"spo", r"sleep", r"step", r"height", r"weight",
            r"password", r"session", r"profile",
        ],
        "near_window": 6,
    },
    "BR027": {  # external storage API with sensitive content
        "file_globs": JAVA_KT,
        "line_any": [
            r"getExternalStorage(?:Directory|PublicDirectory)?",
            r"Environment\.getExternal", r"getExternalFilesDir",
            r"getExternalCacheDir", r"MediaStore",
            r"new\s+File\s*\(",
        ],
        "near_any": [
            r"health", r"log", r"export", r"voice", r"audio",
            r"report", r"db", r"database", r"dump", r"backup",
            r"heart", r"blood", r"sleep",
        ],
        "near_window": 6,
    },
    "BR028": {  # allowBackup / dataExtractionRules
        "file_globs": ["*.xml"],
        "line_any": [
            r'android:allowBackup\s*=\s*"true"',
            r"android:dataExtractionRules",
            r"android:fullBackupContent",
            r"<include\s+domain", r"<exclude\s+domain",
        ],
        "near_window": 0,
    },
    "BR081": {  # KeyStore / secure storage usage
        "file_globs": JAVA_KT,
        "line_any": [
            r"AndroidKeyStore", r"KeyStore\.getInstance",
            r"EncryptedSharedPreferences", r"MasterKey",
            r"KeyGenParameterSpec",
        ],
        "near_window": 0,
    },

    # ---- 6. Logs ----------------------------------------------------------

    "BR047": {  # log leakage
        "file_globs": JAVA_KT,
        "line_any": [
            r"Log\.[vdiwe]\s*\(", r"System\.out\.println",
            r"saveLog", r"writeLog", r"Timber\.[vdiwe]",
            r"println\s*\(",
        ],
        "near_any": [
            r"token", r"password", r"Authorization", r"mac", r"bluetooth",
            r"heart", r"blood", r"spo", r"sleep", r"step", r"temp",
            r"ecg", r"lat", r"lon", r"message", r"payload", r"bytes", r"hex",
            r"response", r"request", r"user",
        ],
        "near_window": 3,
    },
    "BR080": {  # verbose debug logging with health / identifiers
        "file_globs": JAVA_KT,
        "line_any": [r"Log\.d\s*\(", r"Log\.v\s*\(", r"BuildConfig\.DEBUG"],
        "near_any": SENS_HEALTH + SENS_IDENT + [r"payload", r"hex", r"bytes"],
        "near_window": 4,
    },

    # ---- 7. ContentProvider / FileProvider --------------------------------

    "BR021": {  # exported provider in manifest
        "file_globs": ["AndroidManifest.xml", "*.xml"],
        "line_any": [r"<provider"],
        "near_any": [
            r'android:exported\s*=\s*"true"',
            r"android:authorities",
            r"android:grantUriPermissions",
        ],
        "near_window": 6,
    },
    "BR022": {  # FileProvider paths
        "file_globs": ["*.xml"],
        "line_any": [
            r"external-path", r"external-files-path", r"external-cache-path",
            r"files-path", r"cache-path", r"root-path",
        ],
        "near_window": 0,
    },
    "BR023": {  # custom ContentProvider implementation
        "file_globs": JAVA_KT,
        "line_any": [r"extends\s+ContentProvider", r":\s*ContentProvider\b"],
        "near_any": [r"query\s*\(", r"insert\s*\(", r"update\s*\(", r"delete\s*\(", r"openFile\s*\("],
        "near_window": 60,
    },
    "BR024": {  # grantUriPermissions usage
        "file_globs": JAVA_KT,
        "line_any": [
            r"grantUriPermissions", r"FLAG_GRANT_READ_URI_PERMISSION",
            r"FLAG_GRANT_WRITE_URI_PERMISSION",
        ],
        "near_window": 0,
    },
    "BR082": {  # FileProvider usage in code
        "file_globs": JAVA_KT,
        "line_any": [r"FileProvider\.getUriForFile", r"androidx\.core\.content\.FileProvider"],
        "near_window": 0,
    },

    # ---- 8. Deep link / external intent -----------------------------------

    "BR032": {  # VIEW + BROWSABLE + scheme
        "file_globs": ["AndroidManifest.xml", "*.xml"],
        "line_any": [r"android\.intent\.action\.VIEW"],
        "near_any": [
            r"android\.intent\.category\.BROWSABLE",
            r"android:scheme", r"android:host", r"android:pathPrefix",
        ],
        "near_window": 6,
    },
    "BR033": {  # getIntent / getData handling
        "file_globs": JAVA_KT,
        "line_any": [r"getIntent\s*\(\s*\)\s*\.\s*getData", r"Uri\.parse\s*\("],
        "near_any": [
            r"login", r"user", r"device", r"health", r"pay",
            r"upload", r"startActivity", r"startService",
        ],
        "near_window": 6,
    },
    "BR034": {  # implicit Intent to startActivity/startService
        "file_globs": JAVA_KT,
        "line_any": [r"startActivity\s*\(", r"startService\s*\(", r"sendBroadcast\s*\("],
        "near_any": [
            r"Intent\s*\(\s*Intent\.ACTION", r"setAction\s*\(",
            r"setData\s*\(",
        ],
        "near_window": 4,
    },
    "BR035": {  # webview loadUrl with external / javascript bridge
        "file_globs": JAVA_KT,
        "line_any": [
            r"\.loadUrl\s*\(", r"addJavascriptInterface",
        ],
        "near_any": [r"https?://", r"javascript:", r"WebView"],
        "near_window": 6,
    },
    "BR083": {  # app link / associated domain
        "file_globs": ["AndroidManifest.xml", "*.xml", "*.json"],
        "line_any": [
            r"android:autoVerify\s*=\s*\"true\"",
            r"assetlinks\.json",
            r"android_app_links",
        ],
        "near_window": 0,
    },
    "BR084": {  # PendingIntent mutability
        "file_globs": JAVA_KT,
        "line_any": [r"PendingIntent\.getActivity", r"PendingIntent\.getBroadcast", r"PendingIntent\.getService"],
        "near_any": [r"FLAG_MUTABLE", r"FLAG_IMMUTABLE", r"FLAG_UPDATE_CURRENT"],
        "near_window": 4,
    },

    # ---- 9. Third-party SDK / ads / wireless scanning --------------------

    "BR040": {  # ad SDK
        "file_globs": CODE_RES,
        "line_any": [
            r"com\.google\.android\.gms\.ads",
            r"com\.facebook\.ads",
            r"com\.applovin",
            r"com\.bytedance\.sdk",
            r"com\.qq\.e\.ads",
            r"com\.kwad",
            r"MobileAds\.initialize",
            r"AdRequest",
        ],
        "near_window": 0,
    },
    "BR041": {  # analytics SDK
        "file_globs": CODE_RES,
        "line_any": [
            r"com\.google\.firebase\.analytics",
            r"com\.google\.android\.gms\.analytics",
            r"com\.umeng", r"UMConfigure",
            r"com\.flurry", r"com\.amplitude",
            r"MobClickAgent",
        ],
        "near_window": 0,
    },
    "BR042": {  # AD_ID / AdvertisingIdClient combined
        "file_globs": CODE_RES,
        "line_any": [
            r"AdvertisingIdClient", r"getAdvertisingIdInfo",
            r"AD_ID", r"ACCESS_ADSERVICES_AD_ID",
        ],
        "near_any": [
            r"ads", r"analytics", r"firebase", r"gms", r"facebook",
            r"umeng", r"flurry", r"adjust", r"appsflyer",
        ],
        "near_window": 20,
    },
    "BR043": {  # BluetoothLeScanner / startScan / ScanResult
        "file_globs": JAVA_KT,
        "line_any": [
            r"BluetoothLeScanner", r"startScan\s*\(", r"ScanResult",
            r"startLeScan\s*\(",
        ],
        "near_window": 0,
    },
    "BR044": {  # WifiManager.getScanResults
        "file_globs": JAVA_KT,
        "line_any": [r"WifiManager", r"getScanResults", r"getConfiguredNetworks"],
        "near_window": 0,
    },
    "BR072": {  # 3rd-party SDK namespaces (push/im/crash)
        "file_globs": CODE_RES,
        "line_any": [
            r"com\.tencent\.mm\.opensdk",
            r"com\.tencent\.mobileqq",
            r"com\.sina\.weibo\.sdk",
            r"cn\.jpush", r"com\.mob", r"com\.xiaomi\.mipush",
            r"com\.huawei\.hms",
            r"com\.tencent\.bugly", r"io\.sentry",
            r"com\.taobao\.accs",
        ],
        "near_window": 0,
    },

    # ---- 10. BLE ----------------------------------------------------------

    "BR061": {  # BLE write / protocol build
        "file_globs": JAVA_KT,
        "line_any": [
            r"writeCharacteristic", r"writeDescriptor",
            r"setValue\s*\(", r"sendCommand", r"\bSendData\b",
            r"getProtocol", r"buildPacket", r"buildPayload",
        ],
        "near_any": [
            r"payload", r"opcode", r"byte", r"cmd", r"protocol",
            r"heart", r"blood", r"sleep", r"step", r"pay", r"sync",
        ],
        "near_window": 6,
    },
    "BR062": {  # onCharacteristicChanged / notify parsing
        "file_globs": JAVA_KT,
        "line_any": [
            r"onCharacteristicChanged", r"onNotificationReceived",
            r"onCharacteristicRead",
            r"setCharacteristicNotification",
        ],
        "near_any": [
            r"heart", r"blood", r"spo", r"sleep", r"temp", r"ecg",
            r"parser", r"parse", r"save", r"upload", r"decode",
        ],
        "near_window": 20,
    },
    "BR063": {  # byte array / opcode / command
        "file_globs": JAVA_KT,
        "line_any": [
            r"new\s+byte\s*\[", r"byte\[\]\s+\w+\s*=",
            r"opcode", r"\bcmd\b", r"\bcommand\b",
        ],
        "near_any": [
            r"reset", r"pair", r"bind", r"pay", r"weather",
            r"heart", r"step", r"sleep", r"calibrate", r"factory",
        ],
        "near_window": 6,
    },
    "BR064": {  # deviceName / MAC / getAddress identity handling
        "file_globs": JAVA_KT,
        "line_any": [
            r"getAddress\s*\(\s*\)", r"getName\s*\(\s*\)",
            r"deviceName", r"deviceAddress", r"\bMAC\b", r"\bmac\b",
        ],
        "near_any": [
            r"identity", r"device", r"user", r"cache", r"upload",
            r"save", r"register", r"session",
        ],
        "near_window": 6,
    },
    "BR065": {  # onServicesDiscovered
        "file_globs": JAVA_KT,
        "line_any": [r"onServicesDiscovered"],
        "near_any": [
            r"read", r"write", r"pair", r"bind", r"user",
            r"step", r"deviceInfo", r"profile",
        ],
        "near_window": 30,
    },
    "BR066": {  # UUID.fromString for BLE services
        "file_globs": JAVA_KT,
        "line_any": [r"UUID\.fromString", r"serviceUUID", r"characteristicUUID"],
        "near_any": [
            r"BluetoothGatt", r"Characteristic", r"Service",
            r"writeCharacteristic", r"notify", r"notification",
        ],
        "near_window": 6,
    },
    "BR067": {  # pairing / bonding flows
        "file_globs": JAVA_KT,
        "line_any": [
            r"createBond", r"removeBond", r"setPin", r"setPairingConfirmation",
            r"ACTION_BOND_STATE_CHANGED",
        ],
        "near_any": [r"BLE", r"bluetooth", r"gatt", r"device"],
        "near_window": 8,
    },
    "BR068": {  # BLE session / token / key
        "file_globs": JAVA_KT,
        "line_any": [r"sessionKey", r"pairKey", r"authKey", r"bindKey", r"challenge"],
        "near_any": [r"BLE", r"bluetooth", r"gatt", r"encrypt", r"decrypt", r"sign"],
        "near_window": 8,
    },
    "BR069": {  # MAC address persistence
        "file_globs": JAVA_KT,
        "line_any": [r"getAddress\s*\(\s*\)", r"\bMAC\b", r"BluetoothDevice"],
        "near_any": [
            r"SharedPreferences", r"MMKV", r"DataStore", r"write\s*\(",
            r"save", r"cache", r"putString", r"commit\s*\(", r"apply\s*\(",
        ],
        "near_window": 8,
    },
    "BR070": {  # BLE connection caching
        "file_globs": JAVA_KT,
        "line_any": [r"connectGatt", r"autoConnect", r"reconnect"],
        "near_any": [r"cache", r"history", r"lastDevice", r"reload"],
        "near_window": 8,
    },
    "BR073": {  # measurement parser
        "file_globs": JAVA_KT,
        "line_any": [r"parser", r"parse", r"decode", r"unpack"],
        "near_any": SENS_HEALTH + [r"payload", r"byte", r"opcode"],
        "near_window": 6,
    },
    "BR074": {  # health upload (parser → upload path)
        "file_globs": JAVA_KT,
        "line_any": [r"upload", r"report", r"sync", r"save", r"submit"],
        "near_any": SENS_HEALTH + [r"measurement", r"record", r"result"],
        "near_window": 6,
    },
    "BR075": {  # control commands (pay / reset / calibrate)
        "file_globs": JAVA_KT,
        "line_any": [r"reset", r"calibrate", r"factoryReset", r"pay", r"alipay", r"wxpay"],
        "near_any": [r"BLE", r"bluetooth", r"gatt", r"command", r"opcode", r"writeCharacteristic"],
        "near_window": 10,
    },
    "BR086": {  # BLE + crypto usage
        "file_globs": JAVA_KT,
        "line_any": [r"AES", r"HMAC", r"SHA", r"sign\s*\(", r"nonce", r"encrypt", r"decrypt"],
        "near_any": [r"BLE", r"bluetooth", r"gatt", r"characteristic", r"payload", r"opcode"],
        "near_window": 10,
    },
    "BR088": {  # OTA / firmware
        "file_globs": JAVA_KT,
        "line_any": [
            r"\bOTA\b", r"firmware", r"FirmwareUpdate", r"dfu",
            r"nordicsemi\.android\.dfu",
        ],
        "near_any": [
            r"upload", r"download", r"https?://", r"verify", r"signature",
            r"crc", r"checksum",
        ],
        "near_window": 10,
    },


    "BR050": {  # privacy policy URL present in resources
        "file_globs": ["*.xml", "*.html", "*.txt", "*.md", "*.json"],
        "line_any": [r"privacy", r"policy"],
        "near_any": [r"https?://", r"url", r"agreement"],
        "near_window": 4,
    },
    "BR051": {  # third-party SDK disclosed in privacy
        "file_globs": ["*.xml", "*.html", "*.txt", "*.md", "*.json"],
        "line_any": [r"privacy", r"policy"],
        "near_any": [
            r"third-party", r"SDK", r"analytics", r"advertising",
            r"statistic", r"bugly", r"umeng", r"firebase", r"jpush",
        ],
        "near_window": 6,
    },
    "BR052": {  # data types disclosed in privacy
        "file_globs": ["*.xml", "*.html", "*.txt", "*.md", "*.json"],
        "line_any": [r"privacy", r"policy"],
        "near_any": [
            r"health", r"device", r"location", r"bluetooth", r"sms",
            r"contact", r"call",
        ],
        "near_window": 6,
    },

    "BR055": {  # around security-relevant code
        "file_globs": JAVA_KT,
        "line_any": [r"\bTODO\b", r"\bFIXME\b", r"\bXXX\b"],
        "near_any": [
            r"token", r"password", r"encrypt", r"decrypt", r"sign",
            r"security", r"insecure", r"fix",
        ],
        "near_window": 3,
    },
    "BR058": {  # first-party / third-party annotation (debug residue)
        "file_globs": JAVA_KT + ["*.txt", "*.md"],
        "line_any": [r"third-party", r"first-party"],
        "near_window": 0,
    },
    "BR090": {  # hypothesis / evidence strings (debug residue)
        "file_globs": JAVA_KT + ["*.txt", "*.md"],
        "line_any": [r"\bhypothesis\b", r"\bevidence\b", r"\bconfirmed\b"],
        "near_window": 0,
    },
}


# ---------------------------------------------------------------------------

def load_tsv(path: Path) -> List[Dict[str, str]]:
    """Load a TSV into a list of dicts. Tolerates UTF-8 BOM."""
    rows: List[Dict[str, str]] = []
    if not path.exists():
        raise FileNotFoundError(f"TSV not found: {path}")
    # Try utf-8-sig first to strip BOM, then utf-8 fallback.
    for enc in ("utf-8-sig", "utf-8", "gbk", "latin-1"):
        try:
            with path.open("r", encoding=enc, newline="") as fh:
                reader = csv.DictReader(fh, delimiter="\t")
                rows = [dict(r) for r in reader]
            return rows
        except UnicodeDecodeError:
            continue
    raise RuntimeError(f"Could not decode TSV: {path}")


def read_text_file(path: Path) -> Optional[str]:
    """Read a file as text, trying multiple encodings. Skip on failure / size."""
    try:
        st = path.stat()
    except OSError:
        return None
    if st.st_size > MAX_FILE_SIZE_BYTES:
        return None
    for enc in ("utf-8", "utf-8-sig", "gbk", "latin-1"):
        try:
            with path.open("r", encoding=enc, errors="strict") as fh:
                return fh.read()
        except (UnicodeDecodeError, OSError):
            continue
    return None


def is_probably_binary(path: Path) -> bool:
    return path.suffix.lower() in BINARY_EXTS


# ---------------------------------------------------------------------------

@dataclass
class Rule:
    rule_id: str
    paper_id: str
    raw: Dict[str, str] = field(default_factory=dict)


@dataclass
class Hit:
    rule_id: str
    paper_id: str
    paper_title: str
    file_path: str
    line_number: int
    matched_text: str

# ---------------------------------------------------------------------------

def compile_regex_list(patterns: Iterable[str]) -> List[re.Pattern]:
    return [re.compile(p, re.IGNORECASE) for p in patterns]


def compile_spec(spec: dict) -> dict:
    compiled = {
        "file_globs": list(spec.get("file_globs") or ["*"]),
        "path_any": compile_regex_list(spec.get("path_any") or []),
        "line_any": compile_regex_list(spec.get("line_any") or []),
        "line_all": compile_regex_list(spec.get("line_all") or []),
        "near_any": compile_regex_list(spec.get("near_any") or []),
        "near_all": compile_regex_list(spec.get("near_all") or []),
        "file_any": compile_regex_list(spec.get("file_any") or []),
        "file_all": compile_regex_list(spec.get("file_all") or []),
        "near_window": int(spec.get("near_window", 3)),
        "fallback_multi": int(spec.get("fallback_multi", 0)),  # if >0, require N distinct line_any matches in file
    }
    return compiled


def tokenize_fallback(texts: Iterable[str]) -> List[str]:
    """Extract fallback keywords from catalog fields."""
    seen: List[str] = []
    seen_set = set()
    for text in texts:
        if not text:
            continue
        # Split on non-word chars
        for tok in re.split(r"[^A-Za-z0-9_]+", text):
            if not tok:
                continue
            low = tok.lower()
            if low in seen_set:
                continue
            if len(low) < FALLBACK_MIN_LEN:
                continue
            if low in FALLBACK_STOP_WORDS:
                continue
            if low.isdigit():
                continue
            seen_set.add(low)
            seen.append(low)
            if len(seen) >= FALLBACK_MAX_KEYWORDS:
                return seen
    return seen


def build_fallback_spec(rule: Rule) -> Optional[dict]:
    """Build a fallback search spec from rule_catalog fields."""
    texts = [rule.raw.get(f, "") for f in FALLBACK_FIELDS]
    keywords = tokenize_fallback(texts)
    if not keywords:
        return None
    # Use word-boundary regex for keywords
    patterns = [rf"\b{re.escape(k)}\b" for k in keywords]
    spec = {
        "file_globs": JAVA_KT_XML + ["*.json", "*.properties", "*.txt"],
        "line_any": patterns,
        "near_window": 0,
    }
    if len(keywords) > 3:
        # Require at least 2 distinct keywords in the same file
        spec["fallback_multi"] = FALLBACK_MULTI_REQUIRED
    return spec


# ---------------------------------------------------------------------------

def file_matches_globs(path_rel: str, globs: List[str]) -> bool:
    name = Path(path_rel).name
    for g in globs:
        # glob may target full name or path
        if "/" in g or "\\" in g:
            if fnmatch.fnmatch(path_rel.replace("\\", "/"), g.replace("\\", "/")):
                return True
        else:
            if fnmatch.fnmatch(name, g):
                return True
    return False


def any_regex(patterns: List[re.Pattern], text: str) -> bool:
    return any(p.search(text) for p in patterns)


def all_regex(patterns: List[re.Pattern], text: str) -> bool:
    return all(p.search(text) for p in patterns)


def window_text(lines: List[str], idx: int, window: int) -> str:
    if window <= 0:
        return lines[idx]
    lo = max(0, idx - window)
    hi = min(len(lines), idx + window + 1)
    return "\n".join(lines[lo:hi])


def apply_spec_to_file(
    spec: dict,
    rel_path: str,
    text: str,
    lines: List[str],
) -> List[Tuple[int, str]]:
    """Return list of (line_number_1based, matched_text) hits."""
    # path_any
    if spec["path_any"]:
        if not any_regex(spec["path_any"], rel_path):
            return []
    # file_any / file_all
    if spec["file_any"] and not any_regex(spec["file_any"], text):
        return []
    if spec["file_all"] and not all_regex(spec["file_all"], text):
        return []

    # fallback multi-keyword: require N distinct line_any patterns present in whole file
    if spec.get("fallback_multi", 0) > 0 and spec["line_any"]:
        distinct = sum(1 for p in spec["line_any"] if p.search(text))
        if distinct < spec["fallback_multi"]:
            return []

    hits: List[Tuple[int, str]] = []
    window = spec["near_window"]
    has_line_any = bool(spec["line_any"])
    has_line_all = bool(spec["line_all"])
    has_near_any = bool(spec["near_any"])
    has_near_all = bool(spec["near_all"])

    if not (has_line_any or has_line_all):
        # Nothing line-anchored; report line 1 of file if file-level predicates
        # are present and passed.
        if spec["file_any"] or spec["file_all"] or spec["path_any"]:
            return [(1, lines[0] if lines else "")]
        return []

    for idx, line in enumerate(lines):
        if has_line_any and not any_regex(spec["line_any"], line):
            continue
        if has_line_all and not all_regex(spec["line_all"], line):
            continue
        if has_near_any or has_near_all:
            win = window_text(lines, idx, window)
            if has_near_any and not any_regex(spec["near_any"], win):
                continue
            if has_near_all and not all_regex(spec["near_all"], win):
                continue
        hits.append((idx + 1, line))
    return hits



def load_catalogs() -> Tuple[Dict[str, str], List[Rule]]:
    paper_rows = load_tsv(PAPER_CATALOG_FILE)
    rule_rows = load_tsv(RULE_CATALOG_FILE)

    paper_titles: Dict[str, str] = {}
    for r in paper_rows:
        pid = (r.get("paper_id") or r.get("id") or "").strip()
        title = (r.get("paper_title") or r.get("title") or "").strip()
        if pid:
            paper_titles[pid] = title

    rules: List[Rule] = []
    for r in rule_rows:
        rid = (r.get("rule_id") or r.get("id") or "").strip()
        if not rid:
            continue
        pid = (r.get("paper_id") or "").strip()
        rules.append(Rule(rule_id=rid, paper_id=pid, raw={k: (v or "") for k, v in r.items()}))
    return paper_titles, rules


def build_specs_for_rules(rules: List[Rule]) -> Dict[str, dict]:
    compiled: Dict[str, dict] = {}
    for rule in rules:
        rid = rule.rule_id
        raw_spec = RULE_SEARCH_SPECS.get(rid)
        if raw_spec is None:
            raw_spec = build_fallback_spec(rule)
            if raw_spec is None:
                continue
        compiled[rid] = compile_spec(raw_spec)
    return compiled


def walk_app_files(app_root: Path) -> Iterable[Path]:
    for p in app_root.rglob("*"):
        if not p.is_file():
            continue
        if is_probably_binary(p):
            continue
        yield p


def short_matched_text(s: str) -> str:
    s = s.strip()
    if len(s) > MAX_MATCHED_TEXT_LEN:
        s = s[:MAX_MATCHED_TEXT_LEN] + "..."
    return s


def scan_app(
    app_root: Path,
    rules: List[Rule],
    paper_titles: Dict[str, str],
    specs: Dict[str, dict],
) -> Tuple[Dict[str, List[Hit]], int]:
    """Scan every file once, evaluating all applicable specs. Return (hits_by_rule, files_scanned)."""
    hits_by_rule: Dict[str, List[Hit]] = {r.rule_id: [] for r in rules}
    seen_keys: Dict[str, set] = {r.rule_id: set() for r in rules}
    rule_paper: Dict[str, Tuple[str, str]] = {
        r.rule_id: (r.paper_id, paper_titles.get(r.paper_id, "")) for r in rules
    }

    files_scanned = 0

    active_rules = [(rid, specs[rid]) for rid in specs]

    for path in walk_app_files(app_root):
        try:
            rel_path = str(path.relative_to(app_root))
        except ValueError:
            rel_path = str(path)
        rel_path_posix = rel_path.replace("\\", "/")

        # Decide which specs might apply by file_globs before even reading
        applicable: List[Tuple[str, dict]] = []
        for rid, spec in active_rules:
            if file_matches_globs(rel_path_posix, spec["file_globs"]):
                applicable.append((rid, spec))
        if not applicable:
            continue

        text = read_text_file(path)
        if text is None:
            continue
        lines = text.splitlines()
        files_scanned += 1

        for rid, spec in applicable:
            cap = MAX_HITS_PER_RULE_TIGHT if rid in HIGH_FREQ_RULES else MAX_HITS_PER_RULE_DEFAULT
            if len(hits_by_rule[rid]) >= cap:
                continue
            raw_hits = apply_spec_to_file(spec, rel_path_posix, text, lines)
            if not raw_hits:
                continue
            pid, ptitle = rule_paper[rid]
            for (lineno, raw_text) in raw_hits:
                if len(hits_by_rule[rid]) >= cap:
                    break
                key = (rel_path_posix, lineno)
                if key in seen_keys[rid]:
                    continue
                seen_keys[rid].add(key)
                hits_by_rule[rid].append(Hit(
                    rule_id=rid,
                    paper_id=pid,
                    paper_title=ptitle,
                    file_path=rel_path_posix,
                    line_number=lineno,
                    matched_text=short_matched_text(raw_text),
                ))
    return hits_by_rule, files_scanned



def write_tsv(out_path: Path, rules: List[Rule], hits_by_rule: Dict[str, List[Hit]]) -> int:
    total = 0
    with out_path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["rule_id", "paper_id", "paper_title", "file_path", "line_number", "matched_text"])
        for r in rules:
            for h in hits_by_rule.get(r.rule_id, []):
                w.writerow([h.rule_id, h.paper_id, h.paper_title, h.file_path, h.line_number, h.matched_text])
                total += 1
    return total


def write_md(out_path: Path, rules: List[Rule], hits_by_rule: Dict[str, List[Hit]], paper_titles: Dict[str, str]) -> None:
    lines_out: List[str] = ["# Rule Search Hits", ""]
    for r in rules:
        hits = hits_by_rule.get(r.rule_id, [])
        if not hits:
            continue
        lines_out.append(f"## {r.rule_id}")
        lines_out.append("")
        lines_out.append(f"paper_id: {r.paper_id}")
        title = paper_titles.get(r.paper_id, "")
        lines_out.append(f"paper_title: {title}")
        lines_out.append("")
        for h in hits:
            lines_out.append(f"- `{h.file_path}:{h.line_number}`")
            # matched_text shown verbatim inside code fence-style backticks
            safe = h.matched_text.replace("`", "'")
            lines_out.append(f"  `{safe}`")
        lines_out.append("")
    out_path.write_text("\n".join(lines_out), encoding="utf-8")


def write_no_hit(out_path: Path, rules: List[Rule], hits_by_rule: Dict[str, List[Hit]]) -> int:
    no_hits = [r.rule_id for r in rules if not hits_by_rule.get(r.rule_id)]
    with out_path.open("w", encoding="utf-8", newline="") as fh:
        for rid in no_hits:
            fh.write(rid + "\n")
    return len(no_hits)



def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Rule-based static code search for decompiled Android apps.",
    )
    parser.add_argument("--app-root", required=True, help="Path to the decompiled Android app root directory.")
    args = parser.parse_args(argv)

    app_root = Path(args.app_root).expanduser()
    if not app_root.exists() or not app_root.is_dir():
        print(f"[error] --app-root does not exist or is not a directory: {app_root}", file=sys.stderr)
        return 2

    global OUTPUT_DIR
    app_dir_name = app_root.resolve().name or "app"
    OUTPUT_DIR = OUTPUT_BASE / app_dir_name

    paper_titles, rules = load_catalogs()
    if not rules:
        print("[error] No rules loaded from rule_catalog.tsv", file=sys.stderr)
        return 3

    specs = build_specs_for_rules(rules)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    hits_by_rule, files_scanned = scan_app(app_root, rules, paper_titles, specs)

    tsv_path = OUTPUT_DIR / "rule_hits.tsv"
    md_path = OUTPUT_DIR / "rule_hits.md"
    nohit_path = OUTPUT_DIR / "no_hit_rules.txt"

    total_hits = write_tsv(tsv_path, rules, hits_by_rule)
    write_md(md_path, rules, hits_by_rule, paper_titles)
    no_hit_count = write_no_hit(nohit_path, rules, hits_by_rule)
    rules_with_hits = sum(1 for r in rules if hits_by_rule.get(r.rule_id))

    print(f"scanned files: {files_scanned}")
    print(f"total hits: {total_hits}")
    print(f"rules with hits: {rules_with_hits}")
    print(f"rules without hits: {no_hit_count}")
    print(f"output dir: {OUTPUT_DIR.resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
