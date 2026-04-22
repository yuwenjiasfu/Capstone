# Rule Search Hits

## BR001

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/AndroidManifest.xml:87`
  `<uses-permission android:name="android.permission.BLUETOOTH_ADMIN"/>`
- `resources/AndroidManifest.xml:88`
  `<uses-permission android:name="android.permission.CAMERA"/>`
- `resources/AndroidManifest.xml:89`
  `<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>`
- `resources/AndroidManifest.xml:99`
  `<uses-permission android:name="android.permission.USE_FINGERPRINT"/>`
- `resources/AndroidManifest.xml:100`
  `<uses-permission android:name="android.permission.RECORD_AUDIO"/>`
- `resources/AndroidManifest.xml:101`
  `<uses-permission android:name="android.permission.RECORD_VIDEO"/>`
- `resources/AndroidManifest.xml:102`
  `<uses-permission android:name="android.permission.READ_CALENDAR"/>`
- `resources/AndroidManifest.xml:103`
  `<uses-permission android:name="android.permission.WRITE_CALENDAR"/>`
- `resources/AndroidManifest.xml:104`
  `<uses-permission android:name="android.permission.VIBRATE"/>`
- `resources/AndroidManifest.xml:108`
  `<uses-permission android:name="android.permission.FOREGROUND_SERVICE_MICROPHONE"/>`
- `resources/AndroidManifest.xml:114`
  `<uses-permission android:name="android.hardware.location"/>`
- `resources/AndroidManifest.xml:115`
  `<uses-permission android:name="android.permission.CALL_PHONE"/>`
- `resources/AndroidManifest.xml:122`
  `<uses-permission android:name="android.permission.READ_PHONE_STATE"/>`

## BR002

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/AndroidManifest.xml:56`
  `<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>`
- `resources/AndroidManifest.xml:57`
  `<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION"/>`
- `resources/AndroidManifest.xml:58`
  `<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>`
- `resources/AndroidManifest.xml:59`
  `<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>`
- `resources/AndroidManifest.xml:60`
  `<uses-permission android:name="android.permission.FOREGROUND_SERVICE"/>`

## BR003

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/AndroidManifest.xml:67`
  `<uses-permission android:name="android.permission.health.READ_HEART_RATE"/>`
- `resources/AndroidManifest.xml:68`
  `<uses-permission android:name="android.permission.BLUETOOTH_SCAN"/>`
- `resources/AndroidManifest.xml:69`
  `<uses-permission android:name="android.permission.BLUETOOTH_CONNECT"/>`
- `resources/AndroidManifest.xml:70`
  `<uses-permission android:name="android.permission.health.READ_WEIGHT"/>`
- `resources/AndroidManifest.xml:86`
  `<uses-permission android:name="android.permission.BLUETOOTH"/>`
- `resources/AndroidManifest.xml:87`
  `<uses-permission android:name="android.permission.BLUETOOTH_ADMIN"/>`
- `resources/AndroidManifest.xml:88`
  `<uses-permission android:name="android.permission.CAMERA"/>`
- `resources/AndroidManifest.xml:128`
  `<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>`
- `resources/AndroidManifest.xml:129`
  `<uses-permission android:name="android.android.permission.BLUETOOTH_SCAN"/>`
- `resources/AndroidManifest.xml:130`
  `<uses-permission android:name="android.permission.USE_BIOMETRIC"/>`

## BR004

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/AndroidManifest.xml:55`
  `<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>`
- `resources/AndroidManifest.xml:56`
  `<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>`
- `resources/AndroidManifest.xml:88`
  `<uses-permission android:name="android.permission.CAMERA"/>`
- `resources/AndroidManifest.xml:89`
  `<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>`
- `resources/AndroidManifest.xml:90`
  `<uses-permission android:name="android.permission.INTERNET"/>`

## BR005

paper_id: B021
paper_title: Metadata-Based Privacy Assessment for Mobile mHealth

- `resources/AndroidManifest.xml:127`
  `<uses-permission android:name="com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE"/>`
- `resources/AndroidManifest.xml:128`
  `<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>`
- `resources/AndroidManifest.xml:129`
  `<uses-permission android:name="android.android.permission.BLUETOOTH_SCAN"/>`
- `resources/AndroidManifest.xml:130`
  `<uses-permission android:name="android.permission.USE_BIOMETRIC"/>`
- `resources/AndroidManifest.xml:131`
  `<uses-permission android:name="android.permission.ACCESS_ADSERVICES_ATTRIBUTION"/>`
- `resources/AndroidManifest.xml:132`
  `<uses-permission android:name="android.permission.ACCESS_ADSERVICES_AD_ID"/>`

## BR006

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/res/xml/config.xml:181`
  `<application android:usesCleartextTraffic="true"/>`

## BR007

paper_id: B025
paper_title: Why Eve and Mallory Still Love Android: Revisiting TLS (In)Security in Android Applications

- `resources/AndroidManifest.xml:165`
  `android:networkSecurityConfig="@xml/network_security_config"`
- `resources/res/xml/network_security_config.xml:3`
  `<base-config cleartextTrafficPermitted="false">`
- `resources/res/xml/network_security_config.xml:8`
  `<domain-config cleartextTrafficPermitted="false">`

## BR008

paper_id: B025
paper_title: Why Eve and Mallory Still Love Android: Revisiting TLS (In)Security in Android Applications

- `resources/res/xml/network_security_config.xml:4`
  `<trust-anchors>`
- `resources/res/xml/network_security_config.xml:5`
  `<certificates src="system"/>`

## BR009

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/egnc/moh/base/net/EvydSSLClient.java:14`
  `import javax.net.ssl.X509TrustManager;`
- `sources/egnc/moh/base/net/EvydSSLClient.java:22`
  `@Metadata(d1 = {"\u0000:\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0011\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\bÆ\u000...`
- `sources/egnc/moh/base/net/EvydSSLClient.java:43`
  `private static final X509TrustManager newX505TrustManager() {`
- `sources/egnc/moh/base/net/EvydSSLClient.java:45`
  `return new X509TrustManager() { // from class: egnc.moh.base.net.EvydSSLClient.newX505TrustManager.1`
- `sources/egnc/moh/base/net/EvydSSLClient.java:46`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/egnc/moh/base/net/EvydSSLClient.java:47`
  `public void checkClientTrusted(X509Certificate[] chain, String authType) throws CertificateException {`
- `sources/egnc/moh/base/net/EvydSSLClient.java:52`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/egnc/moh/base/net/EvydSSLClient.java:53`
  `public void checkServerTrusted(X509Certificate[] chain, String authType) throws CertificateException {`
- `sources/egnc/moh/base/net/EvydSSLClient.java:58`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/egnc/moh/base/net/SSLSocketClient.java:12`
  `import javax.net.ssl.X509TrustManager;`
- `sources/egnc/moh/base/net/SSLSocketClient.java:26`
  `public static X509TrustManager newX505TrustManager() {`
- `sources/egnc/moh/base/net/SSLSocketClient.java:27`
  `return new X509TrustManager() { // from class: egnc.moh.base.net.SSLSocketClient.1`
- `sources/egnc/moh/base/net/SSLSocketClient.java:28`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/egnc/moh/base/net/SSLSocketClient.java:29`
  `public void checkClientTrusted(X509Certificate[] chain, String authType) throws CertificateException {`
- `sources/egnc/moh/base/net/SSLSocketClient.java:32`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/egnc/moh/base/net/SSLSocketClient.java:33`
  `public void checkServerTrusted(X509Certificate[] chain, String authType) throws CertificateException {`
- `sources/egnc/moh/base/net/SSLSocketClient.java:36`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/egnc/moh/base/net/SSLSocketClient.java:44`
  `return new TrustManager[]{new X509TrustManager() { // from class: egnc.moh.base.net.SSLSocketClient.2`
- `sources/egnc/moh/base/net/SSLSocketClient.java:45`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/egnc/moh/base/net/SSLSocketClient.java:46`
  `public void checkClientTrusted(X509Certificate[] chain, String authType) {`
- `sources/egnc/moh/base/net/SSLSocketClient.java:49`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/egnc/moh/base/net/SSLSocketClient.java:50`
  `public void checkServerTrusted(X509Certificate[] chain, String authType) {`
- `sources/egnc/moh/base/net/SSLSocketClient.java:53`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:12`
  `import javax.net.ssl.X509TrustManager;`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:26`
  `public static X509TrustManager newX505TrustManager() {`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:27`
  `return new X509TrustManager() { // from class: egnc.moh.base.web.manager.health.SSLSocketClient.1`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:28`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:29`
  `public void checkClientTrusted(X509Certificate[] chain, String authType) throws CertificateException {`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:32`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:33`
  `public void checkServerTrusted(X509Certificate[] chain, String authType) throws CertificateException {`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:36`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:44`
  `return new TrustManager[]{new X509TrustManager() { // from class: egnc.moh.base.web.manager.health.SSLSocketClient.2`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:45`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:46`
  `public void checkClientTrusted(X509Certificate[] chain, String authType) {`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:49`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:50`
  `public void checkServerTrusted(X509Certificate[] chain, String authType) {`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:53`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/okhttp3/OkHttpClient.java:21`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/OkHttpClient.java:46`
  `@Metadata(d1 = {"\u0000î\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u001a\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u00...`
- `sources/okhttp3/OkHttpClient.java:77`
  `private final X509TrustManager x509TrustManager;`
- `sources/okhttp3/OkHttpClient.java:128`
  `this.x509TrustManager = null;`
- `sources/okhttp3/OkHttpClient.java:139`
  `X509TrustManager x509TrustManagerOrNull = builder.getX509TrustManagerOrNull();`
- `sources/okhttp3/OkHttpClient.java:140`
  `Intrinsics.checkNotNull(x509TrustManagerOrNull);`
- `sources/okhttp3/OkHttpClient.java:141`
  `this.x509TrustManager = x509TrustManagerOrNull;`
- `sources/okhttp3/OkHttpClient.java:146`
  `X509TrustManager x509TrustManagerPlatformTrustManager = Platform.INSTANCE.get().platformTrustManager();`
- `sources/okhttp3/OkHttpClient.java:147`
  `this.x509TrustManager = x509TrustManagerPlatformTrustManager;`
- `sources/okhttp3/OkHttpClient.java:149`
  `Intrinsics.checkNotNull(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/OkHttpClient.java:150`
  `this.sslSocketFactoryOrNull = platform.newSslSocketFactory(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/OkHttpClient.java:152`
  `Intrinsics.checkNotNull(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/OkHttpClient.java:153`
  `CertificateChainCleaner certificateChainCleaner2 = companion.get(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/OkHttpClient.java:163`
  `this.x509TrustManager = null;`
- `sources/okhttp3/OkHttpClient.java:245`
  `/* JADX INFO: renamed from: x509TrustManager, reason: from getter */`
- `sources/okhttp3/OkHttpClient.java:246`
  `public final X509TrustManager getX509TrustManager() {`
- `sources/okhttp3/OkHttpClient.java:247`
  `return this.x509TrustManager;`
- `sources/okhttp3/OkHttpClient.java:322`
  `if (this.x509TrustManager == null) {`
- `sources/okhttp3/OkHttpClient.java:323`
  `throw new IllegalStateException("x509TrustManager == null".toString());`
- `sources/okhttp3/OkHttpClient.java:335`
  `if (this.x509TrustManager != null) {`
- `sources/okhttp3/OkHttpClient.java:519`
  `@Metadata(d1 = {"\u0000ø\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0018...`
- `sources/okhttp3/OkHttpClient.java:550`
  `private X509TrustManager x509TrustManagerOrNull;`
- `sources/okhttp3/OkHttpClient.java:729`
  `/* JADX INFO: renamed from: getX509TrustManagerOrNull$okhttp, reason: from getter */`
- `sources/okhttp3/OkHttpClient.java:730`
  `public final X509TrustManager getX509TrustManagerOrNull() {`
- `sources/okhttp3/OkHttpClient.java:731`
  `return this.x509TrustManagerOrNull;`
- `sources/okhttp3/OkHttpClient.java:734`
  `public final void setX509TrustManagerOrNull$okhttp(X509TrustManager x509TrustManager) {`
- `sources/okhttp3/OkHttpClient.java:735`
  `this.x509TrustManagerOrNull = x509TrustManager;`
- `sources/okhttp3/OkHttpClient.java:869`
  `this.x509TrustManagerOrNull = okHttpClient.getX509TrustManager();`
- `sources/okhttp3/OkHttpClient.java:1031`
  `@Deprecated(level = DeprecationLevel.ERROR, message = "Use the sslSocketFactory overload that accepts a X509TrustManager.")`
- `sources/okhttp3/OkHttpClient.java:1038`
  `X509TrustManager x509TrustManagerTrustManager = Platform.INSTANCE.get().trustManager(sslSocketFactory);`
- `sources/okhttp3/OkHttpClient.java:1039`
  `if (x509TrustManagerTrustManager == null) {`
- `sources/okhttp3/OkHttpClient.java:1042`
  `setX509TrustManagerOrNull$okhttp(x509TrustManagerTrustManager);`
- `sources/okhttp3/OkHttpClient.java:1044`
  `X509TrustManager x509TrustManagerOrNull = getX509TrustManagerOrNull();`
- `sources/okhttp3/OkHttpClient.java:1045`
  `Intrinsics.checkNotNull(x509TrustManagerOrNull);`
- `sources/okhttp3/OkHttpClient.java:1046`
  `setCertificateChainCleaner$okhttp(platform.buildCertificateChainCleaner(x509TrustManagerOrNull));`
- `sources/okhttp3/OkHttpClient.java:1050`
  `public final Builder sslSocketFactory(SSLSocketFactory sslSocketFactory, X509TrustManager trustManager) {`
- `sources/okhttp3/OkHttpClient.java:1053`
  `if (!Intrinsics.areEqual(sslSocketFactory, getSslSocketFactoryOrNull()) || !Intrinsics.areEqual(trustManager, getX509TrustManagerOrNull())) {`
- `sources/okhttp3/OkHttpClient.java:1058`
  `setX509TrustManagerOrNull$okhttp(trustManager);`
- `sources/okhttp3/internal/platform/Android10Platform.java:10`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/platform/Android10Platform.java:27`
  `@Metadata(d1 = {"\u0000J\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\...`
- `sources/okhttp3/internal/platform/Android10Platform.java:47`
  `public X509TrustManager trustManager(SSLSocketFactory sslSocketFactory) {`
- `sources/okhttp3/internal/platform/Android10Platform.java:121`
  `public CertificateChainCleaner buildCertificateChainCleaner(X509TrustManager trustManager) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:19`
  `import javax.net.ssl.X509TrustManager;`

## BR010

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/egnc/moh/base/net/SSLSocketClient.java:60`
  `public static HostnameVerifier getHostnameVerifier() {`
- `sources/egnc/moh/base/net/SSLSocketClient.java:61`
  `return new HostnameVerifier() { // from class: egnc.moh.base.net.SSLSocketClient.3`
- `sources/egnc/moh/base/net/SSLSocketClient.java:62`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/egnc/moh/base/net/SSLSocketClient.java:63`
  `public boolean verify(String s, SSLSession sslSession) {`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:60`
  `public static HostnameVerifier getHostnameVerifier() {`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:61`
  `return new HostnameVerifier() { // from class: egnc.moh.base.web.manager.health.SSLSocketClient.3`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:62`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:63`
  `public boolean verify(String s, SSLSession sslSession) {`
- `sources/okhttp3/internal/connection/RealConnection.java:620`
  `if (this.http2Connection == null || routes == null || !routeMatchesAny(routes) || address.hostnameVerifier() != OkHostnameVerifier.INSTANCE || !supportsUrl(address.url())) {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:82`
  `@Metadata(d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\u0011\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\bÀ\u0002\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002J3\u0...`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:83`
  `public static final class DisabledHostnameVerifier implements ConscryptHostnameVerifier {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:84`
  `public static final DisabledHostnameVerifier INSTANCE = new DisabledHostnameVerifier();`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:86`
  `public final boolean verify(String hostname, SSLSession session) {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:90`
  `public boolean verify(X509Certificate[] certs, String hostname, SSLSession session) {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:94`
  `private DisabledHostnameVerifier() {`
- `sources/okhttp3/internal/tls/BasicCertificateChainCleaner.java:78`
  `toVerify.verify(signingCert.getPublicKey());`

## BR011

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/com/tencent/liteav/base/http/HttpClientAndroid.java:54`
  `import javax.net.ssl.SSLException;`
- `sources/okhttp3/internal/connection/ConnectionSpecSelector.java:10`
  `import javax.net.ssl.SSLException;`
- `sources/okhttp3/internal/connection/ConnectionSpecSelector.java:11`
  `import javax.net.ssl.SSLHandshakeException;`
- `sources/okhttp3/internal/connection/ConnectionSpecSelector.java:71`
  `return (!this.isFallbackPossible || (e instanceof ProtocolException) || (e instanceof InterruptedIOException) || ((e instanceof SSLHandshakeException) && (e.getCause() instanceof CertificateException)) || (e instanceof SSLPeerUnverifiedException) || !(e instanceof SSLException)) ? false : true;`

## BR012

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/okhttp3/Address.java:21`
  `@Metadata(d1 = {"\u0000h\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002...`
- `sources/okhttp3/Address.java:23`
  `private final CertificatePinner certificatePinner;`
- `sources/okhttp3/Address.java:35`
  `public Address(String uriHost, int i, Dns dns, SocketFactory socketFactory, SSLSocketFactory sSLSocketFactory, HostnameVerifier hostnameVerifier, CertificatePinner certificatePinner, Authenticator proxyAuthenticator, Proxy proxy, List<? extends Protocol> protocols, List<ConnectionSpec> connectionSpe...`
- `sources/okhttp3/Address.java:47`
  `this.certificatePinner = certificatePinner;`
- `sources/okhttp3/Address.java:72`
  `public final CertificatePinner certificatePinner() {`
- `sources/okhttp3/Address.java:73`
  `return this.certificatePinner;`
- `sources/okhttp3/Address.java:160`
  `@Deprecated(level = DeprecationLevel.ERROR, message = "moved to val", replaceWith = @ReplaceWith(expression = "certificatePinner", imports = {}))`
- `sources/okhttp3/Address.java:161`
  `/* JADX INFO: renamed from: -deprecated_certificatePinner, reason: not valid java name and from getter */`
- `sources/okhttp3/Address.java:162`
  `public final CertificatePinner getCertificatePinner() {`
- `sources/okhttp3/Address.java:163`
  `return this.certificatePinner;`
- `sources/okhttp3/Address.java:177`
  `return ((((((((((((((((((527 + this.url.hashCode()) * 31) + this.dns.hashCode()) * 31) + this.proxyAuthenticator.hashCode()) * 31) + this.protocols.hashCode()) * 31) + this.connectionSpecs.hashCode()) * 31) + this.proxySelector.hashCode()) * 31) + Objects.hashCode(this.proxy)) * 31) + Objects.hashCo...`
- `sources/okhttp3/Address.java:182`
  `return Intrinsics.areEqual(this.dns, that.dns) && Intrinsics.areEqual(this.proxyAuthenticator, that.proxyAuthenticator) && Intrinsics.areEqual(this.protocols, that.protocols) && Intrinsics.areEqual(this.connectionSpecs, that.connectionSpecs) && Intrinsics.areEqual(this.proxySelector, that.proxySelec...`
- `sources/okhttp3/CertificatePinner.java:26`
  `/* JADX INFO: compiled from: CertificatePinner.kt */`
- `sources/okhttp3/CertificatePinner.java:28`
  `@Metadata(d1 = {"\u0000T\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\"\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0010\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u0011\...`
- `sources/okhttp3/CertificatePinner.java:29`
  `public final class CertificatePinner {`
- `sources/okhttp3/CertificatePinner.java:33`
  `public static final CertificatePinner DEFAULT = new Builder().build();`
- `sources/okhttp3/CertificatePinner.java:52`
  `public CertificatePinner(Set<Pin> pins, CertificateChainCleaner certificateChainCleaner) {`
- `sources/okhttp3/CertificatePinner.java:58`
  `public /* synthetic */ CertificatePinner(Set set, CertificateChainCleaner certificateChainCleaner, int i, DefaultConstructorMarker defaultConstructorMarker) {`
- `sources/okhttp3/CertificatePinner.java:74`
  `check$okhttp(hostname, new Function0<List<? extends X509Certificate>>() { // from class: okhttp3.CertificatePinner.check.1`
- `sources/okhttp3/CertificatePinner.java:83`
  `CertificateChainCleaner certificateChainCleaner = CertificatePinner.this.getCertificateChainCleaner();`
- `sources/okhttp3/CertificatePinner.java:172`
  `public final CertificatePinner withCertificateChainCleaner$okhttp(CertificateChainCleaner certificateChainCleaner) {`
- `sources/okhttp3/CertificatePinner.java:174`
  `return Intrinsics.areEqual(this.certificateChainCleaner, certificateChainCleaner) ? this : new CertificatePinner(this.pins, certificateChainCleaner);`
- `sources/okhttp3/CertificatePinner.java:178`
  `if (other instanceof CertificatePinner) {`
- `sources/okhttp3/CertificatePinner.java:179`
  `CertificatePinner certificatePinner = (CertificatePinner) other;`
- `sources/okhttp3/CertificatePinner.java:180`
  `if (Intrinsics.areEqual(certificatePinner.pins, this.pins) && Intrinsics.areEqual(certificatePinner.certificateChainCleaner, this.certificateChainCleaner)) {`
- `sources/okhttp3/CertificatePinner.java:193`
  `/* JADX INFO: compiled from: CertificatePinner.kt */`
- `sources/okhttp3/CertificatePinner.java:194`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0007\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0004\u0018\u00002\u00020\u0001B\u0015\u0012\u0006\u0010\...`
- `sources/okhttp3/CertificatePinner.java:221`
  `if (StringsKt.startsWith$default(pin, "sha256/", false, 2, (Object) null)) {`
- `sources/okhttp3/CertificatePinner.java:233`
  `throw new IllegalArgumentException(Intrinsics.stringPlus("pins must start with 'sha256/' or 'sha1/': ", pin));`
- `sources/okhttp3/CertificatePinner.java:277`
  `return Intrinsics.areEqual(this.hash, CertificatePinner.INSTANCE.sha256Hash(certificate));`
- `sources/okhttp3/CertificatePinner.java:280`
  `return Intrinsics.areEqual(this.hash, CertificatePinner.INSTANCE.sha1Hash(certificate));`
- `sources/okhttp3/CertificatePinner.java:305`
  `/* JADX INFO: compiled from: CertificatePinner.kt */`
- `sources/okhttp3/CertificatePinner.java:306`
  `@Metadata(d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010!\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010\u000e\n\u0002\u0010\u0011\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\u0018\u00002\u00020\u0001B\u0005¢\u0006\u0002\u0010\u0002J'\u0010\b\u001a\u00020\u00...`
- `sources/okhttp3/CertificatePinner.java:327`
  `public final CertificatePinner build() {`
- `sources/okhttp3/CertificatePinner.java:328`
  `return new CertificatePinner(CollectionsKt.toSet(this.pins), null, 2, 0 == true ? 1 : 0);`
- `sources/okhttp3/CertificatePinner.java:332`
  `/* JADX INFO: compiled from: CertificatePinner.kt */`
- `sources/okhttp3/CertificatePinner.java:333`
  `@Metadata(d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\b\u0086\u0003\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002...`
- `sources/okhttp3/CertificatePinner.java:366`
  `return Intrinsics.stringPlus("sha256/", sha256Hash((X509Certificate) certificate).base64());`
- `sources/okhttp3/OkHttpClient.java:46`
  `@Metadata(d1 = {"\u0000î\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u001a\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u00...`
- `sources/okhttp3/OkHttpClient.java:52`
  `private final CertificatePinner certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:129`
  `this.certificatePinner = CertificatePinner.DEFAULT;`
- `sources/okhttp3/OkHttpClient.java:142`
  `CertificatePinner certificatePinner = builder.getCertificatePinner();`
- `sources/okhttp3/OkHttpClient.java:144`
  `this.certificatePinner = certificatePinner.withCertificateChainCleaner$okhttp(certificateChainCleaner);`
- `sources/okhttp3/OkHttpClient.java:155`
  `CertificatePinner certificatePinner2 = builder.getCertificatePinner();`
- `sources/okhttp3/OkHttpClient.java:157`
  `this.certificatePinner = certificatePinner2.withCertificateChainCleaner$okhttp(certificateChainCleaner2);`
- `sources/okhttp3/OkHttpClient.java:164`
  `this.certificatePinner = CertificatePinner.DEFAULT;`
- `sources/okhttp3/OkHttpClient.java:262`
  `public final CertificatePinner certificatePinner() {`
- `sources/okhttp3/OkHttpClient.java:263`
  `return this.certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:338`
  `if (!Intrinsics.areEqual(this.certificatePinner, CertificatePinner.DEFAULT)) {`
- `sources/okhttp3/OkHttpClient.java:482`
  `@Deprecated(level = DeprecationLevel.ERROR, message = "moved to val", replaceWith = @ReplaceWith(expression = "certificatePinner", imports = {}))`
- `sources/okhttp3/OkHttpClient.java:483`
  `/* JADX INFO: renamed from: -deprecated_certificatePinner, reason: not valid java name and from getter */`
- `sources/okhttp3/OkHttpClient.java:484`
  `public final CertificatePinner getCertificatePinner() {`
- `sources/okhttp3/OkHttpClient.java:485`
  `return this.certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:519`
  `@Metadata(d1 = {"\u0000ø\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0018...`
- `sources/okhttp3/OkHttpClient.java:525`
  `private CertificatePinner certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:571`
  `this.certificatePinner = CertificatePinner.DEFAULT;`
- `sources/okhttp3/OkHttpClient.java:766`
  `/* JADX INFO: renamed from: getCertificatePinner$okhttp, reason: from getter */`
- `sources/okhttp3/OkHttpClient.java:767`
  `public final CertificatePinner getCertificatePinner() {`
- `sources/okhttp3/OkHttpClient.java:768`
  `return this.certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:771`
  `public final void setCertificatePinner$okhttp(CertificatePinner certificatePinner) {`
- `sources/okhttp3/OkHttpClient.java:772`
  `Intrinsics.checkNotNullParameter(certificatePinner, "<set-?>");`
- `sources/okhttp3/OkHttpClient.java:773`
  `this.certificatePinner = certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:873`
  `this.certificatePinner = okHttpClient.certificatePinner();`
- `sources/okhttp3/OkHttpClient.java:1105`
  `public final Builder certificatePinner(CertificatePinner certificatePinner) {`
- `sources/okhttp3/OkHttpClient.java:1106`
  `Intrinsics.checkNotNullParameter(certificatePinner, "certificatePinner");`
- `sources/okhttp3/OkHttpClient.java:1107`
  `if (!Intrinsics.areEqual(certificatePinner, getCertificatePinner())) {`
- `sources/okhttp3/OkHttpClient.java:1110`
  `setCertificatePinner$okhttp(certificatePinner);`
- `sources/okhttp3/internal/connection/RealCall.java:29`
  `import okhttp3.CertificatePinner;`
- `sources/okhttp3/internal/connection/RealCall.java:414`
  `CertificatePinner certificatePinner;`
- `sources/okhttp3/internal/connection/RealCall.java:418`
  `certificatePinner = this.client.certificatePinner();`
- `sources/okhttp3/internal/connection/RealCall.java:422`
  `certificatePinner = null;`
- `sources/okhttp3/internal/connection/RealCall.java:424`
  `return new Address(url.host(), url.port(), this.client.dns(), this.client.socketFactory(), sslSocketFactory, hostnameVerifier, certificatePinner, this.client.proxyAuthenticator(), this.client.proxy(), this.client.protocols(), this.client.connectionSpecs(), this.client.proxySelector());`
- `sources/okhttp3/internal/connection/RealConnection.java:35`
  `import okhttp3.CertificatePinner;`
- `sources/okhttp3/internal/connection/RealConnection.java:310`
  `final CertificatePinner certificatePinner = address.certificatePinner();`
- `sources/okhttp3/internal/connection/RealConnection.java:311`
  `Intrinsics.checkNotNull(certificatePinner);`
- `sources/okhttp3/internal/connection/RealConnection.java:320`
  `CertificateChainCleaner certificateChainCleaner$okhttp = certificatePinner.getCertificateChainCleaner();`
- `sources/okhttp3/internal/connection/RealConnection.java:325`
  `certificatePinner.check$okhttp(address.url().host(), new Function0<List<? extends X509Certificate>>() { // from class: okhttp3.internal.connection.RealConnection.connectTls.2`
- `sources/okhttp3/internal/connection/RealConnection.java:358`
  `throw new SSLPeerUnverifiedException(StringsKt.trimMargin$default("\n              |Hostname " + address.url().host() + " not verified:\n              |    certificate: " + CertificatePinner.INSTANCE.pin(x509Certificate) + "\n              |    DN: " + ((Object) x509Certificate.getSubjectDN().getNam...`
- `sources/okhttp3/internal/connection/RealConnection.java:624`
  `CertificatePinner certificatePinner = address.certificatePinner();`
- `sources/okhttp3/internal/connection/RealConnection.java:625`
  `Intrinsics.checkNotNull(certificatePinner);`

## BR013

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `resources/assets/mobile.v2.22.1.html:877`
  `// Reference: http://es5.github.io/#x15.4.4.14`
- `resources/assets/html/bruhealth_disclaimer.html:2`
  `<!-- saved from url=(0082)http://test.k8s.bruneihealth.yiducloud.cn/covid19/bruhealth/term_of_use_2.0.0.html -->`
- `resources/assets/html-de/sharing.html:12`
  `<p>Um QR-Codes auf Ihrem Computer zu erzeugen, testen Sie den ZXing QR Code Generator, er basiert auf dem selben Quelltext wie dieses Programm: <a href="http://zxing.appspot.com/generator/">http://zxing.appspot.com/generator/</a></p>`
- `resources/assets/html-en/index.html:10`
  `<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>`
- `resources/assets/html-en/sharing.html:12`
  `<p>To generate QR Codes from your computer, try the ZXing QR Code Generator: <a href="http://zxing.appspot.com/generator/">http://zxing.appspot.com/generator/</a></p>`
- `resources/assets/html-es/index.html:10`
  `<a href="http://github.com/zxing/zxing"> http://github.com/zxing/zxing </a></p>`
- `resources/assets/html-es/license.html:34`
  `<p> Este proyecto se basa en la <a class="notranslate" href="http://github.com/zxing/zxing">ZXing</a> código de barras`
- `resources/assets/html-es/license.html:36`
  `<a class="notranslate" href="http://www.apache.org/licenses/LICENSE-2.0.html">Apache License 2.0</a> : </p>`
- `resources/assets/html-es/sharing.html:12`
  `<p> Para generar códigos QR desde su computadora, pruebe el generador ZXing Código QR: <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-fr/index.html:10`
  `<a href="http://github.com/zxing/zxing"> http://github.com/zxing/zxing </a></p>`
- `resources/assets/html-fr/sharing.html:12`
  `<p> Pour générer les codes QR à partir de votre ordinateur, essayez le générateur de code QR ZXing: <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-it/sharing.html:12`
  `<p> Per generare i codici QR dal tuo computer, provare il generatore di ZXing QR Code: <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-ja/sharing.html:12`
  `<p>パソコンからQRコードを生成するには、ZXing QR Code Generator (<a href="http://zxing.appspot.com/generator/">http://zxing.appspot.com/generator/</a>)をご利用ください。</p>`
- `resources/assets/html-ko/sharing.html:12`
  `<p> 컴퓨터에서 QR 코드를 생성하려면 ZXing QR 코드 생성기를 사용해 : <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-nl/sharing.html:12`
  `<p> Om QR Codes van uw computer te genereren, probeer dan de ZXing QR Code Generator: <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-pt/sharing.html:12`
  `<p> Para gerar QR Codes do seu computador, experimente a Gerador de código QR ZXing: <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-ru/sharing.html:12`
  `<p> Для создания QR-коды с компьютера, попробуйте ZXing QR Генератор кода: <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-uk/sharing.html:12`
  `<p> Для створення QR-кода з комп'ютеру, спробуйте ZXing QR Генератор: <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-zh-rCN/sharing.html:12`
  `<p> 在电脑上可以使用 ZXing 二维码生成器： <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-zh-rHK/sharing.html:12`
  `<p>要從您的電腦產生 QR Code，請試用 ZXing QR Code 產生器（英文）：<a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-zh-rTW/sharing.html:12`
  `<p>要從您的電腦產生 QR Code，請試用 ZXing QR Code 產生器（英文）：<a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/www/index.html:1`
  `<!DOCTYPE html><html lang=en><head><meta charset=utf-8><meta http-equiv=X-UA-Compatible content="IE=edge"><meta name=viewport content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=0,viewport-fit=cover"><meta http-equiv=Content-Security-Policy content="default-src 'self' data: gap...`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:26`
  `var i=Object.freeze({}),r=Array.isArray;function o(t){return void 0===t||null===t}function a(t){return void 0!==t&&null!==t}function s(t){return!0===t}function l(t){return!1===t}function u(t){return"string"===typeof t||"number"===typeof t||"symbol"===typeof t||"boolean"===typeof t}function c(t){retu...`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:32`
  `* Based on Underscore.js 1.8.3 <http://underscorejs.org/LICENSE>`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:47`
  `var i=n("b639"),r=i.Buffer;function o(t,e){for(var n in t)e[n]=t[n]}function a(t,e,n){return r(t,e,n)}r.from&&r.alloc&&r.allocUnsafe&&r.allocUnsafeSlow?t.exports=i:(o(i,e),e.Buffer=a),a.prototype=Object.create(r.prototype),o(r,a),a.from=function(t,e,n){if("number"===typeof t)throw new TypeError("Arg...`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:73`
  `License at http://www.apache.org/licenses/LICENSE-2.0`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:83`
  `/*! http://mths.be/fromcodepoint v0.2.1 by @mathias */`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:84`
  `String.fromCodePoint||function(){var t=function(){try{var t={},e=Object.defineProperty,n=e(t,t,t)&&e}catch(i){}return n}(),e=String.fromCharCode,n=Math.floor,i=function(t){var i,r,o=16384,a=[],s=-1,l=arguments.length;if(!l)return"";var u="";while(++s<l){var c=Number(arguments[s]);if(!isFinite(c)||c<...`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:107`
  `* @author   Feross Aboukhadijeh <http://feross.org>`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:113`
  `᠎";t.exports=function(t){return r((function(){return!!o[t]()||a[t]()!==a||i&&o[t].name!==t}))}},c8ef:function(t,e,n){var i=n("6d8b"),r=n("a15a"),o=r.createSymbol,a=n("2306"),s=a.Group,l=n("3842"),u=l.parsePercent,c=n("1418"),h=3;function f(t){return i.isArray(t)||(t=[+t,+t]),t}function d(t,e){var n=...`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:117`
  `* @author   Feross Aboukhadijeh <feross@feross.org> <http://feross.org>`
- `resources/assets/www/plugins/cordova-plugin-camera/www/Camera.js:106`
  `* - Save the data locally ('LocalStorage', [Lawnchair](http://brianleroux.github.com/lawnchair/), etc.)`
- `resources/assets/www/plugins/cordova-plugin-file-transfer/www/FileTransfer.js:51`
  `// Proof: http://social.msdn.microsoft.com/Forums/windowsapps/en-US/a327cf3c-f033-4a54-8b7f-03c56ba3203f/windows-foundation-uri-security-problem`
- `resources/assets/www/plugins/cordova-plugin-globalization/www/globalization.js:159`
  `*                                    http://unicode.org/reports/tr35/tr35-4.html`
- `resources/assets/www/plugins/cordova-plugin-globalization/www/globalization.js:329`
  `*                                    http://unicode.org/reports/tr35/tr35-4.html`
- `resources/assets/www/plugins/cordova-plugin-globalization/www/globalization.js:364`
  `*                                    http://unicode.org/reports/tr35/tr35-4.html`
- `resources/res/color/design_box_stroke_color.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/color/m3_textfield_input_text_color.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/abc_ic_ab_back_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_arrow_drop_right_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`

## BR014

paper_id: B022
paper_title: A Study of Android Application Security

- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1499`
  `panelFeatureState.qwertyMode = KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1;`
- `sources/androidx/appcompat/app/ToolbarActionBar.java:436`
  `menu.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);`
- `sources/androidx/appcompat/app/WindowDecorActionBar.java:1278`
  `menu.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);`
- `sources/androidx/camera/core/impl/CameraValidator.java:22`
  `if (Build.VERSION.SDK_INT >= 34 && Api34Impl.getDeviceId(context) != 0) {`
- `sources/androidx/camera/core/impl/CameraValidator.java:27`
  `Logger.d(TAG, "Virtual device with ID: " + Api34Impl.getDeviceId(context) + " has " + cameras.size() + " cameras. Skipping validation.");`
- `sources/androidx/camera/core/impl/CameraValidator.java:94`
  `static int getDeviceId(Context context) {`
- `sources/androidx/camera/core/impl/CameraValidator.java:95`
  `return context.getDeviceId();`
- `sources/androidx/camera/core/impl/utils/ContextUtil.java:14`
  `if (Build.VERSION.SDK_INT >= 34 && (deviceId = Api34Impl.getDeviceId(context)) != Api34Impl.getDeviceId(applicationContext)) {`
- `sources/androidx/camera/core/impl/utils/ContextUtil.java:57`
  `static int getDeviceId(Context context) {`
- `sources/androidx/camera/core/impl/utils/ContextUtil.java:58`
  `return context.getDeviceId();`
- `sources/androidx/compose/ui/platform/AndroidComposeView.java:1642`
  `MotionEvent event = MotionEvent.obtain(motionEvent.getDownTime() == motionEvent.getEventTime() ? eventTime : motionEvent.getDownTime(), eventTime, action, pointerCount, pointerPropertiesArr, pointerCoordsArr, motionEvent.getMetaState(), forceHover ? 0 : motionEvent.getButtonState(), motionEvent.getX...`
- `sources/androidx/core/content/ContextCompat.java:59`
  `import android.telephony.TelephonyManager;`
- `sources/androidx/core/content/ContextCompat.java:355`
  `map.put(TelephonyManager.class, HintConstants.AUTOFILL_HINT_PHONE);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:4`
  `import android.telephony.TelephonyManager;`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:9`
  `public class TelephonyManagerCompat {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:10`
  `private static Method sGetDeviceIdMethod;`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:13`
  `public static String getImei(TelephonyManager telephonyManager) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:15`
  `return Api26Impl.getImei(telephonyManager);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:17`
  `int subscriptionId = getSubscriptionId(telephonyManager);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:21`
  `return Api23Impl.getDeviceId(telephonyManager, slotIndex);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:24`
  `if (sGetDeviceIdMethod == null) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:25`
  `Method declaredMethod = TelephonyManager.class.getDeclaredMethod("getDeviceId", Integer.TYPE);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:26`
  `sGetDeviceIdMethod = declaredMethod;`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:29`
  `return (String) sGetDeviceIdMethod.invoke(telephonyManager, Integer.valueOf(slotIndex));`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:34`
  `return telephonyManager.getDeviceId();`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:37`
  `public static int getSubscriptionId(TelephonyManager telephonyManager) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:39`
  `return Api30Impl.getSubscriptionId(telephonyManager);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:43`
  `Method declaredMethod = TelephonyManager.class.getDeclaredMethod("getSubId", new Class[0]);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:47`
  `Integer num = (Integer) sGetSubIdMethod.invoke(telephonyManager, new Object[0]);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:57`
  `private TelephonyManagerCompat() {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:64`
  `static int getSubscriptionId(TelephonyManager telephonyManager) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:65`
  `return telephonyManager.getSubscriptionId();`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:73`
  `static String getImei(TelephonyManager telephonyManager) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:74`
  `return telephonyManager.getImei();`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:82`
  `static String getDeviceId(TelephonyManager telephonyManager, int i) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:83`
  `return telephonyManager.getDeviceId(i);`
- `sources/androidx/core/view/DifferentialMotionFlingController.java:81`
  `int deviceId = motionEvent.getDeviceId();`
- `sources/androidx/core/view/DifferentialMotionFlingController.java:95`
  `iArr[0] = ViewConfigurationCompat.getScaledMinimumFlingVelocity(context, viewConfiguration, motionEvent.getDeviceId(), i, motionEvent.getSource());`
- `sources/androidx/core/view/DifferentialMotionFlingController.java:96`
  `iArr[1] = ViewConfigurationCompat.getScaledMaximumFlingVelocity(context, viewConfiguration, motionEvent.getDeviceId(), i, motionEvent.getSource());`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:10`
  `import android.telephony.TelephonyManager;`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:227`
  `TelephonyManager telephonyManager = (TelephonyManager) Utils.getApp().getSystemService(HintConstants.AUTOFILL_HINT_PHONE);`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:228`
  `if (telephonyManager == null || (networkOperatorName = telephonyManager.getNetworkOperatorName()) == null) {`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:12`
  `import android.telephony.TelephonyManager;`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:140`
  `TelephonyManager telephonyManager;`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:142`
  `telephonyManager = (TelephonyManager) Utils.getApp().getSystemService(HintConstants.AUTOFILL_HINT_PHONE);`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:146`
  `if (telephonyManager == null) {`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:150`
  `return telephonyManager.isDataEnabled();`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:152`
  `Method declaredMethod = telephonyManager.getClass().getDeclaredMethod("getDataEnabled", new Class[0]);`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:154`
  `return ((Boolean) declaredMethod.invoke(telephonyManager, new Object[0])).booleanValue();`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:213`
  `TelephonyManager telephonyManager = (TelephonyManager) Utils.getApp().getSystemService(HintConstants.AUTOFILL_HINT_PHONE);`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:214`
  `if (telephonyManager == null) {`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:217`
  `return telephonyManager.getNetworkOperatorName();`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:4`
  `import android.telephony.TelephonyManager;`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:15`
  `return getTelephonyManager().getPhoneType() != 0;`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:18`
  `public static String getDeviceId() {`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:22`
  `TelephonyManager telephonyManager = getTelephonyManager();`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:23`
  `String deviceId = telephonyManager.getDeviceId();`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:30`
  `String imei = telephonyManager.getImei();`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:34`
  `String meid = telephonyManager.getMeid();`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:50`
  `public static String getIMEI() {`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:51`
  `return getImeiOrMeid(true);`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:54`
  `public static String getMEID() {`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:55`
  `return getImeiOrMeid(false);`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:64`
  `public static java.lang.String getImeiOrMeid(boolean r10) {`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:72`
  `android.telephony.TelephonyManager r0 = getTelephonyManager()`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:111`
  `java.lang.String r1 = r0.getDeviceId()`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:113`
  `java.lang.String r7 = "getDeviceId"`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:171`
  `throw new UnsupportedOperationException("Method not decompiled: com.blankj.utilcode.util.PhoneUtils.getImeiOrMeid(boolean):java.lang.String");`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:195`
  `getTelephonyManager().getSubscriberId();`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:201`
  `return getTelephonyManager().getSubscriberId();`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:205`
  `return getTelephonyManager().getPhoneType();`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:209`
  `return getTelephonyManager().getSimState() == 5;`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:213`
  `return getTelephonyManager().getSimOperatorName();`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:217`
  `String simOperator = getTelephonyManager().getSimOperator();`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:253`
  `private static TelephonyManager getTelephonyManager() {`
- `sources/com/blankj/utilcode/util/PhoneUtils.java:254`
  `return (TelephonyManager) Utils.getApp().getSystemService(HintConstants.AUTOFILL_HINT_PHONE);`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:8`
  `import android.telephony.TelephonyManager;`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:117`
  `private static TelephonyManager getTelephonyManager(Context context) {`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:118`
  `return (TelephonyManager) context.getSystemService(HintConstants.AUTOFILL_HINT_PHONE);`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:122`
  `String simOperator = getTelephonyManager(context).getSimOperator();`

## BR015

paper_id: B022
paper_title: A Study of Android Application Security

- `sources/androidx/biometric/BiometricFragment.java:258`
  `if (!DeviceUtils.shouldHideFingerprintDialog(applicationContext, Build.MODEL)) {`
- `sources/androidx/biometric/BiometricFragment.java:353`
  `if (context == null || !DeviceUtils.shouldDelayShowingPrompt(context, Build.MODEL)) {`
- `sources/androidx/biometric/BiometricFragment.java:562`
  `return (activity == null || this.mViewModel.getCryptoObject() == null || !DeviceUtils.shouldUseFingerprintForCrypto(activity, Build.MANUFACTURER, Build.MODEL)) ? false : true;`
- `sources/androidx/biometric/BiometricFragment.java:576`
  `return (context == null || !DeviceUtils.shouldHideFingerprintDialog(context, Build.MODEL)) ? 2000 : 0;`
- `sources/androidx/biometric/BiometricManager.java:79`
  `return DeviceUtils.canAssumeStrongBiometrics(this.mContext, Build.MODEL);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:23`
  `return "OnePlus".equalsIgnoreCase(Build.BRAND) && "OnePlus6".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:27`
  `return "OnePlus".equalsIgnoreCase(Build.BRAND) && "OnePlus6T".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:31`
  `return "HUAWEI".equalsIgnoreCase(Build.BRAND) && "HWANE".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:35`
  `return "SAMSUNG".equalsIgnoreCase(Build.BRAND) && "ON7XELTE".equalsIgnoreCase(Build.DEVICE) && Build.VERSION.SDK_INT >= 27;`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:39`
  `return "SAMSUNG".equalsIgnoreCase(Build.BRAND) && "J7XELTE".equalsIgnoreCase(Build.DEVICE) && Build.VERSION.SDK_INT >= 27;`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:43`
  `return "REDMI".equalsIgnoreCase(Build.BRAND) && "joyeuse".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExtraSupportedSurfaceCombinationsQuirk.java:30`
  `return "heroqltevzw".equalsIgnoreCase(Build.DEVICE) || "heroqltetmo".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExtraSupportedSurfaceCombinationsQuirk.java:34`
  `if (!"google".equalsIgnoreCase(Build.BRAND)) {`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExtraSupportedSurfaceCombinationsQuirk.java:37`
  `return SUPPORT_EXTRA_LEVEL_3_CONFIGURATIONS_GOOGLE_MODELS.contains(Build.MODEL.toUpperCase(Locale.US));`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExtraSupportedSurfaceCombinationsQuirk.java:41`
  `if (!"samsung".equalsIgnoreCase(Build.BRAND)) {`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExtraSupportedSurfaceCombinationsQuirk.java:44`
  `String upperCase = Build.MODEL.toUpperCase(Locale.US);`
- `sources/androidx/camera/camera2/internal/compat/quirk/FlashAvailabilityBufferUnderflowQuirk.java:24`
  `return KNOWN_AFFECTED_MODELS.contains(new Pair(Build.MANUFACTURER.toLowerCase(Locale.US), Build.MODEL.toLowerCase(Locale.US)));`
- `sources/androidx/camera/camera2/internal/compat/quirk/ImageCaptureFailedForVideoSnapshotQuirk.java:19`
  `return PROBLEMATIC_UNI_SOC_MODELS.contains(Build.MODEL.toLowerCase(Locale.US)) || (Build.VERSION.SDK_INT >= 31 && "Spreadtrum".equalsIgnoreCase(Build.SOC_MANUFACTURER)) || Build.HARDWARE.toLowerCase(Locale.US).startsWith("ums") || ("itel".equalsIgnoreCase(Build.BRAND) && Build.HARDWARE.toLowerCase(L...`
- `sources/androidx/camera/camera2/internal/compat/quirk/ImageCaptureFailedForVideoSnapshotQuirk.java:23`
  `return "HUAWEI".equalsIgnoreCase(Build.BRAND) && "FIG-LX1".equalsIgnoreCase(Build.MODEL);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ImageCaptureFailedWhenVideoCaptureIsBoundQuirk.java:33`
  `return "motorola".equalsIgnoreCase(Build.BRAND) && "moto e13".equalsIgnoreCase(Build.MODEL);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ImageCaptureFailedWhenVideoCaptureIsBoundQuirk.java:37`
  `return "samsung".equalsIgnoreCase(Build.BRAND) && ("gta8".equalsIgnoreCase(Build.DEVICE) || "gta8wifi".equalsIgnoreCase(Build.DEVICE));`
- `sources/androidx/camera/camera2/internal/compat/quirk/InvalidVideoProfilesQuirk.java:20`
  `return "samsung".equalsIgnoreCase(Build.BRAND) && isTp1aBuild();`
- `sources/androidx/camera/camera2/internal/compat/quirk/InvalidVideoProfilesQuirk.java:36`
  `return ("redmi".equalsIgnoreCase(Build.BRAND) || "xiaomi".equalsIgnoreCase(Build.BRAND)) && (isTkq1Build() || isTp1aBuild());`
- `sources/androidx/camera/camera2/internal/compat/quirk/InvalidVideoProfilesQuirk.java:40`
  `return AFFECTED_PIXEL_MODELS.contains(Build.MODEL.toLowerCase(Locale.ROOT));`
- `sources/androidx/camera/camera2/internal/compat/quirk/JpegCaptureDownsizingQuirk.java:17`
  `return KNOWN_AFFECTED_FRONT_CAMERA_DEVICES.contains(Build.MODEL.toLowerCase(Locale.US)) && ((Integer) cameraCharacteristicsCompat.get(CameraCharacteristics.LENS_FACING)).intValue() == 0;`
- `sources/androidx/camera/camera2/internal/compat/quirk/JpegHalCorruptImageQuirk.java:16`
  `return KNOWN_AFFECTED_DEVICES.contains(Build.DEVICE.toLowerCase(Locale.US));`
- `sources/androidx/camera/camera2/internal/compat/quirk/Nexus4AndroidLTargetAspectRatioQuirk.java:18`
  `return "GOOGLE".equalsIgnoreCase(Build.BRAND) && Build.VERSION.SDK_INT < 23 && DEVICE_MODELS.contains(Build.MODEL.toUpperCase(Locale.US));`
- `sources/androidx/camera/camera2/internal/compat/quirk/PreviewPixelHDRnetQuirk.java:14`
  `return "Google".equals(Build.MANUFACTURER) && SUPPORTED_DEVICES.contains(Build.DEVICE.toLowerCase(Locale.getDefault()));`
- `sources/androidx/camera/camera2/internal/compat/quirk/ZslDisablerQuirk.java:20`
  `return "samsung".equalsIgnoreCase(Build.BRAND) && isAffectedModel(AFFECTED_SAMSUNG_MODEL);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ZslDisablerQuirk.java:24`
  `return "xiaomi".equalsIgnoreCase(Build.BRAND) && isAffectedModel(AFFECTED_XIAOMI_MODEL);`
- `sources/androidx/camera/camera2/internal/compat/workaround/FlashAvailabilityChecker.java:24`
  `Logger.d(TAG, String.format("Device is known to throw an exception while checking flash availability. Flash is not available. [Manufacturer: %s, Model: %s, API Level: %d].", Build.MANUFACTURER, Build.MODEL, Integer.valueOf(Build.VERSION.SDK_INT)));`
- `sources/androidx/camera/camera2/internal/compat/workaround/FlashAvailabilityChecker.java:26`
  `Logger.e(TAG, String.format("Exception thrown while checking for flash availability on device not known to throw exceptions during this check. Please file an issue at https://issuetracker.google.com/issues/new?component=618491&template=1257717 with this error message [Manufacturer: %s, Model: %s, AP...`
- `sources/androidx/camera/core/impl/CameraValidator.java:44`
  `Logger.d(TAG, "Verifying camera lens facing on " + Build.DEVICE + ", lensFacingInteger: " + lensFacing);`
- `sources/androidx/camera/core/impl/DeviceProperties.java:14`
  `return create(Build.MANUFACTURER, Build.MODEL, Build.VERSION.SDK_INT);`
- `sources/androidx/camera/core/impl/utils/ExifData.java:136`
  `return new Builder(ByteOrder.BIG_ENDIAN).setAttribute(ExifInterface.TAG_ORIENTATION, String.valueOf(1)).setAttribute(ExifInterface.TAG_X_RESOLUTION, "72/1").setAttribute(ExifInterface.TAG_Y_RESOLUTION, "72/1").setAttribute(ExifInterface.TAG_RESOLUTION_UNIT, String.valueOf(2)).setAttribute(ExifInterf...`
- `sources/androidx/camera/core/internal/compat/quirk/ImageCaptureRotationOptionQuirk.java:28`
  `return Build.FINGERPRINT.startsWith("generic") || Build.FINGERPRINT.startsWith("unknown") || Build.MODEL.contains("google_sdk") || Build.MODEL.contains("Emulator") || Build.MODEL.contains("Cuttlefish") || Build.MODEL.contains("Android SDK built for x86") || Build.MANUFACTURER.contains("Genymotion") ...`
- `sources/androidx/camera/core/internal/compat/quirk/IncorrectJpegMetadataQuirk.java:21`
  `return "Samsung".equalsIgnoreCase(Build.BRAND) && SAMSUNG_DEVICES.contains(Build.DEVICE.toUpperCase(Locale.US));`
- `sources/androidx/camera/core/internal/compat/quirk/LargeJpegImageQuirk.java:21`
  `return "Samsung".equalsIgnoreCase(Build.BRAND) && SAMSUNG_DEVICE_MODELS.contains(Build.MODEL.toUpperCase(Locale.US));`
- `sources/androidx/camera/core/internal/compat/quirk/LargeJpegImageQuirk.java:25`
  `return "Samsung".equalsIgnoreCase(Build.BRAND);`
- `sources/androidx/camera/core/internal/compat/quirk/LargeJpegImageQuirk.java:29`
  `return "Vivo".equalsIgnoreCase(Build.BRAND) && VIVO_DEVICE_MODELS.contains(Build.MODEL.toUpperCase(Locale.US));`
- `sources/androidx/camera/core/internal/compat/quirk/LowMemoryQuirk.java:15`
  `return DEVICE_MODELS.contains(Build.MODEL.toUpperCase(Locale.US));`
- `sources/androidx/camera/extensions/internal/compat/quirk/ExtensionDisabledQuirk.java:25`
  `return "google".equalsIgnoreCase(Build.BRAND) && "redfin".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/extensions/internal/compat/quirk/ExtensionDisabledQuirk.java:29`
  `return "motorola".equalsIgnoreCase(Build.BRAND);`
- `sources/androidx/camera/video/internal/compat/quirk/AudioTimestampFramePositionIncorrectQuirk.java:18`
  `return "oppo".equalsIgnoreCase(Build.BRAND) && AFFECTED_OPPO_MODELS.contains(Build.MODEL.toLowerCase(Locale.ROOT));`
- `sources/androidx/camera/video/internal/compat/quirk/AudioTimestampFramePositionIncorrectQuirk.java:22`
  `return "lge".equalsIgnoreCase(Build.BRAND) && "lg-m250".equalsIgnoreCase(Build.MODEL);`
- `sources/androidx/camera/video/internal/compat/quirk/CameraUseInconsistentTimebaseQuirk.java:24`
  `return "SAMSUNG".equalsIgnoreCase(Build.BRAND) && BUILD_HARDWARE_SET.contains(Build.HARDWARE.toLowerCase());`
- `sources/androidx/camera/video/internal/compat/quirk/CameraUseInconsistentTimebaseQuirk.java:28`
  `return BUILD_MODEL_SET.contains(Build.MODEL.toLowerCase());`
- `sources/androidx/camera/video/internal/compat/quirk/EncoderNotUsePersistentInputSurfaceQuirk.java:13`
  `return Build.VERSION.SDK_INT <= 22 || DEVICE_MODELS.contains(Build.MODEL.toUpperCase());`
- `sources/androidx/camera/video/internal/compat/quirk/MediaCodecInfoReportIncorrectInfoQuirk.java:23`
  `return "Nokia".equalsIgnoreCase(Build.BRAND) && "Nokia 1".equalsIgnoreCase(Build.MODEL);`
- `sources/androidx/camera/video/internal/compat/quirk/MediaCodecInfoReportIncorrectInfoQuirk.java:66`
  `return INCORRECT_FHD_PROFILE_MODEL_LIST.contains(Build.MODEL.toLowerCase(Locale.US));`
- `sources/androidx/camera/video/internal/compat/quirk/ReportedVideoQualityNotSupportedQuirk.java:17`
  `return "Huawei".equalsIgnoreCase(Build.BRAND) && "HMA-L29".equalsIgnoreCase(Build.MODEL);`
- `sources/androidx/camera/video/internal/workaround/VideoTimebaseConverter.java:80`
  `Logger.e(TAG, String.format("Detected camera timebase inconsistent. Please file an issue at https://issuetracker.google.com/issues/new?component=618491&template=1257717 with this error message [Manufacturer: %s, Model: %s, Hardware: %s, API Level: %d%s].\nCamera timebase is inconsistent. The timebas...`
- `sources/androidx/camera/view/internal/compat/quirk/SurfaceViewStretchedQuirk.java:21`
  `return SAMSUNG.equalsIgnoreCase(Build.MANUFACTURER) && (GALAXY_Z_FOLD_2.equalsIgnoreCase(Build.DEVICE) || GALAXY_Z_FOLD_3.equalsIgnoreCase(Build.DEVICE));`
- `sources/androidx/camera/view/internal/compat/quirk/SurfaceViewStretchedQuirk.java:25`
  `return OPPO.equalsIgnoreCase(Build.MANUFACTURER) && OPPO_FIND_N.equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/view/internal/compat/quirk/SurfaceViewStretchedQuirk.java:29`
  `return LENOVO.equalsIgnoreCase(Build.MANUFACTURER) && LENOVO_TAB_P12_PRO.equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/compose/material3/CalendarDate.java:110`
  `locale = Locale.getDefault();`
- `sources/androidx/compose/material3/CalendarMonth.java:131`
  `locale = Locale.getDefault();`
- `sources/androidx/compose/material3/LegacyCalendarModelImpl.java:135`
  `TimeZone timeZone = TimeZone.getDefault();`
- `sources/androidx/compose/ui/text/android/animation/SegmentBreaker.java:128`
  `BreakIterator characterInstance = BreakIterator.getCharacterInstance(Locale.getDefault());`
- `sources/androidx/compose/ui/text/android/animation/SegmentBreaker.java:129`
  `Intrinsics.checkNotNullExpressionValue(characterInstance, "getCharacterInstance(Locale.getDefault())");`
- `sources/com/alibaba/android/arouter/core/LogisticsCenter.java:154`
  `ARouter.logger.debug("ARouter::", String.format(Locale.getDefault(), "The group [%s] starts loading, trigger by [%s]", postcard.getGroup(), postcard.getPath()));`
- `sources/com/alibaba/android/arouter/core/LogisticsCenter.java:159`
  `ARouter.logger.debug("ARouter::", String.format(Locale.getDefault(), "The group [%s] has already been loaded, trigger by [%s]", postcard.getGroup(), postcard.getPath()));`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:224`
  `if (Build.FINGERPRINT.startsWith("generic") || Build.FINGERPRINT.toLowerCase().contains("vbox") || Build.FINGERPRINT.toLowerCase().contains("test-keys") || Build.MODEL.contains("google_sdk") || Build.MODEL.contains("Emulator") || Build.MODEL.contains("Android SDK built for x86") || Build.MANUFACTURE...`
- `sources/com/blankj/utilcode/util/UtilsBridge.java:555`
  `sb.append(Build.MANUFACTURER);`
- `sources/com/blankj/utilcode/util/UtilsBridge.java:557`
  `sb.append(Build.MODEL);`
- `sources/com/bruhealth/glucometer/util/ZTimeTool.java:32`
  `private SimpleDateFormat DEFAULT_SDF = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.getDefault());`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:221`
  `java.lang.String r1 = android.os.Build.DEVICE`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:224`
  `java.lang.String r1 = android.os.Build.DEVICE`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:138`
  `return eventInternal.toBuilder().addMetadata(KEY_SDK_VERSION, Build.VERSION.SDK_INT).addMetadata(KEY_MODEL, Build.MODEL).addMetadata(KEY_HARDWARE, Build.HARDWARE).addMetadata(KEY_DEVICE, Build.DEVICE).addMetadata(KEY_PRODUCT, Build.PRODUCT).addMetadata(KEY_OS_BUILD, Build.ID).addMetadata(KEY_MANUFAC...`
- `sources/com/google/android/exoplayer2/util/Util.java:301`
  `String str = Build.DEVICE;`
- `sources/com/google/android/exoplayer2/util/Util.java:303`
  `String str2 = Build.MANUFACTURER;`
- `sources/com/google/android/exoplayer2/util/Util.java:305`
  `String str3 = Build.MODEL;`
- `sources/com/google/android/gms/fitness/data/Device.java:35`
  `return new Device(Build.MANUFACTURER, Build.MODEL, zzo.zzb(context), iZza, 2);`
- `sources/com/google/android/gms/fitness/data/zzo.java:34`
  `int i3 = (TextUtils.isEmpty(Build.PRODUCT) || !Build.PRODUCT.startsWith("glass_")) ? 1 : 6;`
- `sources/com/google/android/material/color/DynamicColors.java:210`
  `DeviceSupportCondition deviceSupportCondition = DYNAMIC_COLOR_SUPPORTED_MANUFACTURERS.get(Build.MANUFACTURER.toLowerCase(Locale.ROOT));`
- `sources/com/google/android/material/color/DynamicColors.java:212`
  `deviceSupportCondition = DYNAMIC_COLOR_SUPPORTED_BRANDS.get(Build.BRAND.toLowerCase(Locale.ROOT));`
- `sources/com/google/android/material/datepicker/DaysOfWeekAdapter.java:65`
  `textView.setContentDescription(String.format(viewGroup.getContext().getString(R.string.mtrl_picker_day_of_week_column_header), this.calendar.getDisplayName(7, 2, Locale.getDefault())));`
- `sources/com/google/android/material/internal/ManufacturerUtils.java:32`
  `String str = Build.MANUFACTURER;`
- `sources/com/google/firebase/FirebaseCommonRegistrar.java:35`
  `arrayList.add(LibraryVersionComponent.create(DEVICE_NAME, safeValue(Build.PRODUCT)));`
- `sources/com/google/firebase/FirebaseCommonRegistrar.java:36`
  `arrayList.add(LibraryVersionComponent.create(DEVICE_MODEL, safeValue(Build.DEVICE)));`

## BR016

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/AndroidManifest.xml:335`
  `android:name="com.google.android.geo.API_KEY"`
- `resources/assets/www/js/chunk-242b1d3c.e1ab5c24.js:1`
  `(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-242b1d3c"],{"49ab":function(e,t,r){},9836:function(e,t,r){"use strict";r("49ab")},b5db:function(e,t,r){"use strict";r.r(t);r("b0c0");var i=function(){var e=this,t=e._self._c;return t("div",{staticClass:"member-wrapper"},[e.fullscreen?...`
- `resources/assets/www/js/chunk-7695d904.24ff9ac9.js:1`
  `(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-7695d904"],{1163:function(e,t,i){},"1aec":function(e,t,i){},"2a94":function(e,t,i){"use strict";i("1163")},"2ea6":function(e,t,i){},"674d":function(e,t,i){"use strict";i("1aec")},"6f54":function(e,t,i){"use strict";i.r(t);var a=functi...`
- `resources/assets/www/js/chunk-c9dcfac2.d61de690.js:1`
  `(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-c9dcfac2"],{2972:function(e,t,n){"use strict";n("fefa")},4127:function(e,t,n){"use strict";n.r(t);var i=function(){var e=this,t=e._self._c;return t("div",{staticClass:"account-setting"},[e.fullscreen?t("div",{staticClass:"global-fulls...`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:45`
  `*/var i=Object.getOwnPropertySymbols,r=Object.prototype.hasOwnProperty,o=Object.prototype.propertyIsEnumerable;function a(t){if(null===t||void 0===t)throw new TypeError("Object.assign cannot be called with null or undefined");return Object(t)}function s(){try{if(!Object.assign)return!1;var t=new Str...`
- `resources/assets/www/js/ihospital-appointment3.02af1573.js:1`
  `(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["ihospital-appointment3","chunk-242b1d3c","chunk-7596e42f"],{"31e2":function(e,t,r){"use strict";r("6559")},"49ab":function(e,t,r){},6559:function(e,t,r){},9836:function(e,t,r){"use strict";r("49ab")},a2ef:function(e,t,r){"use strict";r.r(t)...`
- `resources/assets/www/js/ihospital-appointment5.78f05133.js:1`
  `(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["ihospital-appointment5","activity-apply~cms~ihospital-appointment15~ihospital-appointment20~ihospital-appointment6~ihospital-~faa2c3e0","chunk-d171f720","chunk-1ce9121e","chunk-17599c4c","chunk-7695d904"],{"028f":function(t,e,a){},"0778":fu...`
- `resources/res/values/public.xml:5373`
  `<public type="string" name="google_api_key" id="0x7f13011c" />`
- `resources/res/values/public.xml:5375`
  `<public type="string" name="google_crash_reporting_api_key" id="0x7f13011e" />`
- `resources/res/values/strings.xml:287`
  `<string name="google_api_key">AIzaSyB2E-3-r3a9W6pw1evqo_2o_NSiUqXO-ac</string>`
- `resources/res/values/strings.xml:289`
  `<string name="google_crash_reporting_api_key">AIzaSyB2E-3-r3a9W6pw1evqo_2o_NSiUqXO-ac</string>`
- `sources/com/google/android/datatransport/cct/CCTDestination.java:14`
  `private static final String DEFAULT_API_KEY;`
- `sources/com/google/android/datatransport/cct/CCTDestination.java:23`
  `private final String apiKey;`
- `sources/com/google/android/datatransport/cct/CCTDestination.java:32`
  `DEFAULT_API_KEY = strMergeStrings3;`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:63`
  `static final String API_KEY_HEADER_KEY = "X-Goog-Api-Key";`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:233`
  `if (httpRequest.apiKey != null) {`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:234`
  `httpURLConnection.setRequestProperty(API_KEY_HEADER_KEY, httpRequest.apiKey);`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:384`
  `final String apiKey;`
- `sources/com/google/android/gms/auth/api/signin/GoogleSignInOptions.java:208`
  `return new GoogleSignInOptions(3, new ArrayList(hashSet), !TextUtils.isEmpty(strOptString) ? new Account(strOptString, "com.google") : null, jSONObject.getBoolean("idTokenRequested"), jSONObject.getBoolean("serverAuthRequested"), jSONObject.getBoolean("forceCodeForRefreshToken"), jSONObject.has("ser...`
- `sources/com/google/android/gms/auth/api/signin/GoogleSignInOptions.java:390`
  `jSONObject.put("forceCodeForRefreshToken", this.zal);`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:65`
  `public static final Task zai(HasApiKey hasApiKey, HasApiKey... hasApiKeyArr) {`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:66`
  `Preconditions.checkNotNull(hasApiKey, "Requested API must not be null.");`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:67`
  `for (HasApiKey hasApiKey2 : hasApiKeyArr) {`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:68`
  `Preconditions.checkNotNull(hasApiKey2, "Requested API must not be null.");`
- `sources/com/google/android/gms/common/api/internal/zaae.java:22`
  `public static void zad(Activity activity, GoogleApiManager googleApiManager, ApiKey apiKey) {`
- `sources/com/google/android/gms/location/FusedLocationProviderClient.java:14`
  `public interface FusedLocationProviderClient extends HasApiKey<Api.ApiOptions.NoOptions> {`
- `sources/com/google/android/gms/signin/internal/SignInClientImpl.java:50`
  `bundle.putBoolean("com.google.android.gms.signin.internal.forceCodeForRefreshToken", false);`
- `sources/com/google/android/gms/signin/internal/SignInClientImpl.java:53`
  `bundle.putBoolean("com.google.android.gms.signin.internal.waitForAccessTokenRefresh", false);`
- `sources/com/google/firebase/FirebaseError.java:11`
  `public static final int ERROR_INVALID_API_KEY = 17023;`
- `sources/com/google/firebase/FirebaseOptions.java:12`
  `private static final String API_KEY_RESOURCE_NAME = "google_api_key";`
- `sources/com/google/firebase/FirebaseOptions.java:19`
  `private final String apiKey;`
- `sources/com/google/firebase/FirebaseOptions.java:28`
  `private String apiKey;`
- `sources/com/google/firebase/crashlytics/internal/send/DataTransportCrashlyticsReportSender.java:24`
  `private static final String CRASHLYTICS_API_KEY = mergeStrings("AzSBpY4F0rHiHFdinTvM", "IayrSTFL9eJ69YeSUO2");`
- `sources/com/google/firebase/iid/FirebaseInstanceId.java:53`
  `private static final Pattern API_KEY_FORMAT = Pattern.compile("\\AA[\\w-]{38}\\z");`
- `sources/com/google/firebase/iid/FirebaseInstanceId.java:158`
  `static boolean isValidApiKeyFormat(@Nonnull String str) {`
- `sources/com/google/firebase/installations/FirebaseInstallations.java:35`
  `private static final String API_KEY_VALIDATION_MSG = "Please set a valid API key. A Firebase API key is required to communicate with Firebase server APIs: It authenticates your project with Google.Please refer to https://firebase.google.com/support/privacy/init-options.";`
- `sources/com/google/firebase/installations/Utils.java:16`
  `private static final Pattern API_KEY_FORMAT = Pattern.compile("\\AA[\\w-]{38}\\z");`
- `sources/com/google/firebase/installations/local/PersistedInstallation.java:19`
  `private static final String REFRESH_TOKEN_KEY = "RefreshToken";`
- `sources/com/google/firebase/installations/remote/AutoValue_InstallationResponse.java:102`
  `private String refreshToken;`
- `sources/com/google/firebase/installations/remote/FirebaseInstallationServiceClient.java:40`
  `private static final String API_KEY_HEADER = "x-goog-api-key";`
- `sources/com/google/firebase/installations/remote/FirebaseInstallationServiceClient.java:300`
  `httpURLConnection.addRequestProperty(API_KEY_HEADER, str);`
- `sources/com/google/firebase/remoteconfig/RemoteConfigComponent.java:146`
  `}, this.executor, DEFAULT_CLOCK, DEFAULT_RANDOM, configCacheClient, getFrcBackendApiClient(this.firebaseApp.getOptions().getApiKey(), str, configMetadataClient), configMetadataClient, this.customHeaders);`
- `sources/com/google/firebase/remoteconfig/internal/ConfigFetchHttpClient.java:43`
  `private static final String API_KEY_HEADER = "X-Goog-Api-Key";`
- `sources/com/google/firebase/remoteconfig/internal/ConfigFetchHttpClient.java:52`
  `private final String apiKey;`
- `sources/com/google/firebase/remoteconfig/internal/ConfigFetchHttpClient.java:141`
  `httpURLConnection.setRequestProperty(API_KEY_HEADER, this.apiKey);`
- `sources/com/google/firebase/remoteconfig/internal/ConfigRealtimeHttpClient.java:46`
  `private static final String API_KEY_HEADER = "X-Goog-Api-Key";`
- `sources/com/google/firebase/remoteconfig/internal/ConfigRealtimeHttpClient.java:113`
  `httpURLConnection.setRequestProperty(API_KEY_HEADER, this.firebaseApp.getOptions().getApiKey());`
- `sources/egnc/moh/bruhealth/R.java:13070`
  `public static final int google_api_key = 0x7f13011c;`
- `sources/egnc/moh/bruhealth/R.java:13076`
  `public static final int google_crash_reporting_api_key = 0x7f13011e;`

## BR017

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `sources/androidx/biometric/CryptoObjectUtils.java:129`
  `KeyGenerator keyGenerator = KeyGenerator.getInstance("AES", "AndroidKeyStore");`
- `sources/androidx/biometric/CryptoObjectUtils.java:133`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS7Padding");`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:112`
  `java.security.MessageDigest r4 = java.security.MessageDigest.getInstance(r4)     // Catch: java.io.IOException -> L2f java.security.NoSuchAlgorithmException -> L31 java.lang.Throwable -> L47`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:120`
  `java.security.MessageDigest r4 = r2.getMessageDigest()     // Catch: java.io.IOException -> L2f java.security.NoSuchAlgorithmException -> L31 java.lang.Throwable -> L47`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:259`
  `public static String encryptHmacMD5ToString(String str, String str2) {`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:263`
  `return encryptHmacMD5ToString(str.getBytes(), str2.getBytes());`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:266`
  `public static String encryptHmacMD5ToString(byte[] bArr, byte[] bArr2) {`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:267`
  `return UtilsBridge.bytes2HexString(encryptHmacMD5(bArr, bArr2));`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:274`
  `public static String encryptHmacSHA1ToString(String str, String str2) {`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:278`
  `return encryptHmacSHA1ToString(str.getBytes(), str2.getBytes());`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:281`
  `public static String encryptHmacSHA1ToString(byte[] bArr, byte[] bArr2) {`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:282`
  `return UtilsBridge.bytes2HexString(encryptHmacSHA1(bArr, bArr2));`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:289`
  `public static String encryptHmacSHA224ToString(String str, String str2) {`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:293`
  `return encryptHmacSHA224ToString(str.getBytes(), str2.getBytes());`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:296`
  `public static String encryptHmacSHA224ToString(byte[] bArr, byte[] bArr2) {`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:297`
  `return UtilsBridge.bytes2HexString(encryptHmacSHA224(bArr, bArr2));`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:304`
  `public static String encryptHmacSHA256ToString(String str, String str2) {`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:308`
  `return encryptHmacSHA256ToString(str.getBytes(), str2.getBytes());`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:311`
  `public static String encryptHmacSHA256ToString(byte[] bArr, byte[] bArr2) {`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:312`
  `return UtilsBridge.bytes2HexString(encryptHmacSHA256(bArr, bArr2));`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:319`
  `public static String encryptHmacSHA384ToString(String str, String str2) {`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:323`
  `return encryptHmacSHA384ToString(str.getBytes(), str2.getBytes());`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:326`
  `public static String encryptHmacSHA384ToString(byte[] bArr, byte[] bArr2) {`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:327`
  `return UtilsBridge.bytes2HexString(encryptHmacSHA384(bArr, bArr2));`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:334`
  `public static String encryptHmacSHA512ToString(String str, String str2) {`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:338`
  `return encryptHmacSHA512ToString(str.getBytes(), str2.getBytes());`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:341`
  `public static String encryptHmacSHA512ToString(byte[] bArr, byte[] bArr2) {`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:342`
  `return UtilsBridge.bytes2HexString(encryptHmacSHA512(bArr, bArr2));`
- `sources/com/blankj/utilcode/util/FileUtils.java:877`
  `java.security.MessageDigest r3 = java.security.MessageDigest.getInstance(r3)     // Catch: java.lang.Throwable -> L33 java.io.IOException -> L35 java.security.NoSuchAlgorithmException -> L37`
- `sources/com/blankj/utilcode/util/FileUtils.java:885`
  `java.security.MessageDigest r3 = r2.getMessageDigest()     // Catch: java.io.IOException -> L2f java.security.NoSuchAlgorithmException -> L31 java.lang.Throwable -> L47`
- `sources/com/bumptech/glide/load/Key.java:4`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/Key.java:15`
  `void updateDiskCacheKey(MessageDigest messageDigest);`
- `sources/com/bumptech/glide/load/Option.java:4`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/Option.java:10`
  `public void update(byte[] bArr, Object obj, MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/Option.java:48`
  `public void update(T t, MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/Option.java:49`
  `this.cacheKeyUpdater.update(getKeyBytes(), t, messageDigest);`
- `sources/com/bumptech/glide/load/engine/ResourceCacheKey.java:11`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/engine/cache/SafeKeyGenerator.java:46`
  `return Util.sha256BytesToHex(poolableDigestContainer.messageDigest.digest());`
- `sources/com/bumptech/glide/load/engine/cache/SafeKeyGenerator.java:53`
  `final MessageDigest messageDigest;`
- `sources/com/bumptech/glide/load/engine/cache/SafeKeyGenerator.java:56`
  `PoolableDigestContainer(MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/engine/cache/SafeKeyGenerator.java:57`
  `this.messageDigest = messageDigest;`
- `sources/com/bumptech/glide/load/engine/prefill/BitmapPreFillRunner.java:103`
  `public void updateDiskCacheKey(MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/model/GlideUrl.java:9`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/model/GlideUrl.java:83`
  `public void updateDiskCacheKey(MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/model/GlideUrl.java:84`
  `messageDigest.update(getCacheKeyBytes());`
- `sources/com/bumptech/glide/load/resource/UnitTransformation.java:6`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/CenterCrop.java:5`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/CenterInside.java:5`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/CircleCrop.java:5`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/FitCenter.java:5`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/GranularRoundedCorners.java:7`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/Rotate.java:7`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/RoundedCorners.java:8`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:38`
  `public void update(byte[] bArr, Long l, MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:39`
  `messageDigest.update(bArr);`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:42`
  `messageDigest.update(this.buffer.putLong(l.longValue()).array());`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:50`
  `public void update(byte[] bArr, Integer num, MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:57`
  `messageDigest.update(this.buffer.putInt(num.intValue()).array());`
- `sources/com/bumptech/glide/signature/EmptySignature.java:4`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/signature/EmptySignature.java:11`
  `public void updateDiskCacheKey(MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/signature/MediaStoreSignature.java:39`
  `public void updateDiskCacheKey(MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/signature/MediaStoreSignature.java:40`
  `messageDigest.update(ByteBuffer.allocate(12).putLong(this.dateModified).putInt(this.orientation).array());`
- `sources/com/bumptech/glide/signature/MediaStoreSignature.java:41`
  `messageDigest.update(this.mimeType.getBytes(CHARSET));`
- `sources/com/bumptech/glide/signature/ObjectKey.java:34`
  `public void updateDiskCacheKey(MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/signature/ObjectKey.java:35`
  `messageDigest.update(this.object.toString().getBytes(CHARSET));`
- `sources/com/evyd/core/multipicker/selectpic/util/FileUtils.java:175`
  `java.security.MessageDigest r3 = java.security.MessageDigest.getInstance(r3)     // Catch: java.lang.Throwable -> L31 java.lang.Exception -> L33`
- `sources/com/evyd/core/multipicker/selectpic/util/Utils.java:93`
  `MessageDigest messageDigest = MessageDigest.getInstance("MD5");`
- `sources/com/evyd/core/multipicker/selectpic/util/Utils.java:94`
  `messageDigest.update(str.getBytes());`
- `sources/com/evyd/core/multipicker/selectpic/util/Utils.java:95`
  `byte[] bArrDigest = messageDigest.digest();`
- `sources/com/google/android/exoplayer2/source/hls/Aes128DataSource.java:87`
  `return Cipher.getInstance("AES/CBC/PKCS7Padding");`
- `sources/com/google/android/exoplayer2/source/hls/playlist/HlsPlaylistParser.java:47`
  `private static final String METHOD_AES_128 = "AES-128";`
- `sources/com/google/android/exoplayer2/source/hls/playlist/HlsPlaylistParser.java:49`
  `private static final String METHOD_SAMPLE_AES = "SAMPLE-AES";`
- `sources/com/google/android/exoplayer2/source/hls/playlist/HlsPlaylistParser.java:50`
  `private static final String METHOD_SAMPLE_AES_CENC = "SAMPLE-AES-CENC";`
- `sources/com/google/android/exoplayer2/source/hls/playlist/HlsPlaylistParser.java:51`
  `private static final String METHOD_SAMPLE_AES_CTR = "SAMPLE-AES-CTR";`
- `sources/com/google/android/exoplayer2/source/hls/playlist/HlsPlaylistParser.java:120`
  `private static final Pattern REGEX_METHOD = Pattern.compile("METHOD=(NONE|AES-128|SAMPLE-AES|SAMPLE-AES-CENC|SAMPLE-AES-CTR)\\s*(?:,|$)");`
- `sources/com/google/android/exoplayer2/upstream/cache/CachedContentIndex.java:43`
  `import javax.crypto.spec.IvParameterSpec;`
- `sources/com/google/android/exoplayer2/upstream/cache/CachedContentIndex.java:44`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/google/android/exoplayer2/upstream/cache/CachedContentIndex.java:210`
  `return Cipher.getInstance("AES/CBC/PKCS5PADDING", "BC");`
- `sources/com/google/android/exoplayer2/upstream/cache/CachedContentIndex.java:214`
  `return Cipher.getInstance("AES/CBC/PKCS5PADDING");`
- `sources/com/google/android/exoplayer2/upstream/cache/CachedContentIndex.java:367`
  `this.cipher.init(2, (Key) Util.castNonNull(this.secretKeySpec), new IvParameterSpec(bArr));`

## BR018

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/com/bumptech/glide/load/model/GlideUrl.java:39`
  `this.stringUrl = Preconditions.checkNotEmpty(str);`
- `sources/com/bumptech/glide/load/model/ModelCache.java:43`
  `private int height;`
- `sources/com/bumptech/glide/load/model/ModelCache.java:66`
  `this.height = i2;`
- `sources/com/bumptech/glide/load/model/ModelCache.java:81`
  `return this.width == modelKey.width && this.height == modelKey.height && this.model.equals(modelKey.model);`
- `sources/com/bumptech/glide/load/model/ModelCache.java:85`
  `return (((this.height * 31) + this.width) * 31) + this.model.hashCode();`
- `sources/com/bumptech/glide/load/model/ModelLoaderRegistry.java:59`
  `List<ModelLoader<A, ?>> listEmptyList = Collections.emptyList();`
- `sources/com/bumptech/glide/load/model/ModelLoaderRegistry.java:65`
  `listEmptyList = new ArrayList<>(size - i);`
- `sources/com/bumptech/glide/load/model/ModelLoaderRegistry.java:68`
  `listEmptyList.add(modelLoader);`
- `sources/com/bumptech/glide/load/model/ModelLoaderRegistry.java:71`
  `if (listEmptyList.isEmpty()) {`
- `sources/com/bumptech/glide/load/model/ModelLoaderRegistry.java:74`
  `return listEmptyList;`
- `sources/com/bumptech/glide/load/model/MultiModelLoader.java:73`
  `Preconditions.checkNotEmpty(list);`
- `sources/com/bumptech/glide/load/model/stream/QMediaStoreUriLoader.java:54`
  `private final int height;`
- `sources/com/bumptech/glide/load/model/stream/QMediaStoreUriLoader.java:67`
  `this.height = i2;`
- `sources/com/bumptech/glide/load/model/stream/QMediaStoreUriLoader.java:101`
  `return this.fileDelegate.buildLoadData(queryForFilePath(this.uri), this.width, this.height, this.options);`
- `sources/com/bumptech/glide/load/model/stream/QMediaStoreUriLoader.java:104`
  `return this.uriDelegate.buildLoadData(this.uri, this.width, this.height, this.options);`
- `sources/com/bumptech/glide/load/model/stream/QMediaStoreUriLoader.java:106`
  `return this.uriDelegate.buildLoadData(isAccessMediaLocationGranted() ? MediaStore.setRequireOriginal(this.uri) : this.uri, this.width, this.height, this.options);`
- `sources/com/causahealth/mobile/route/bean/ActivityLifeState.java:11`
  `@Metadata(d1 = {"\u00000\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\t\n\u0002\b\f\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u0002\n\u0002\b\u0003\u0018\u00002\u00020\u0001B\u001b\b\u0016\u0012\b\u0010\u0002\u0...`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:13`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\t\n\u0002\b\u0006\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b \n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u000e\n\u0000\b\u0087\b\u0018\u00002\u00020\u0001BM\u0012\u0006\u0010\u0002...`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:20`
  `@SerializedName(Field.NUTRIENT_CALORIES)`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:21`
  `private Long calories;`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:29`
  `@SerializedName("heartRate")`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:30`
  `private Long heartRate;`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:35`
  `@SerializedName("steps")`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:36`
  `private Long steps;`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:49`
  `public final Long getSteps() {`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:50`
  `return this.steps;`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:59`
  `public final Long getCalories() {`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:60`
  `return this.calories;`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:64`
  `public final Long getHeartRate() {`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:65`
  `return this.heartRate;`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:72`
  `public final ActivityData copy(long startTs, long endTs, Long steps, Long distance, Long calories, Long heartRate, List<ActivityTrack> activities) {`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:73`
  `return new ActivityData(startTs, endTs, steps, distance, calories, heartRate, activities);`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:84`
  `return this.startTs == activityData.startTs && this.endTs == activityData.endTs && Intrinsics.areEqual(this.steps, activityData.steps) && Intrinsics.areEqual(this.distance, activityData.distance) && Intrinsics.areEqual(this.calories, activityData.calories) && Intrinsics.areEqual(this.heartRate, acti...`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:89`
  `Long l = this.steps;`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:93`
  `Long l3 = this.calories;`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:95`
  `Long l4 = this.heartRate;`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:102`
  `return "ActivityData(startTs=" + this.startTs + ", endTs=" + this.endTs + ", steps=" + this.steps + ", distance=" + this.distance + ", calories=" + this.calories + ", heartRate=" + this.heartRate + ", activities=" + this.activities + SqlExpression.SqlEnclosureClosingBrace;`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:108`
  `this.steps = l;`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:110`
  `this.calories = l3;`
- `sources/com/evyd/core/mobile/android/health/model/ActivityData.java:111`
  `this.heartRate = l4;`

## BR019

paper_id: B011
paper_title: Locking it down: The privacy and security of mobile medication apps

- `sources/androidx/appcompat/widget/ActivityChooserModel.java:387`
  `map.put(new ComponentName(activityResolveInfo.resolveInfo.activityInfo.packageName, activityResolveInfo.resolveInfo.activityInfo.name), activityResolveInfo);`
- `sources/androidx/camera/core/internal/ViewPorts.java:40`
  `map2.put(entry.getKey(), matrix);`
- `sources/androidx/camera/extensions/internal/sessionprocessor/SessionProcessorBase.java:137`
  `map.put(Integer.valueOf(camera2OutputConfig.getId()), imageReaderNewInstance);`
- `sources/androidx/camera/video/CapabilitiesByQuality.java:37`
  `this.mAreaSortedSizeToQualityMap.put(new Size(defaultVideoProfile.getWidth(), defaultVideoProfile.getHeight()), quality);`
- `sources/androidx/camera/video/CapabilitiesByQuality.java:38`
  `this.mSupportedProfilesMap.put(quality, validatedProfiles);`
- `sources/androidx/camera/video/QualityRatioToResolutionsTable.java:27`
  `map.put(Quality.UHD, Range.create(2160, 4319));`
- `sources/androidx/camera/video/QualityRatioToResolutionsTable.java:28`
  `map.put(Quality.FHD, Range.create(1080, 1439));`
- `sources/androidx/camera/video/QualityRatioToResolutionsTable.java:29`
  `map.put(Quality.HD, Range.create(720, 1079));`
- `sources/androidx/camera/video/QualityRatioToResolutionsTable.java:30`
  `map.put(Quality.SD, Range.create(241, Integer.valueOf(AdaptiveTrackSelection.DEFAULT_MAX_HEIGHT_TO_DISCARD)));`
- `sources/androidx/camera/video/QualityRatioToResolutionsTable.java:33`
  `map2.put(0, AspectRatioUtil.ASPECT_RATIO_4_3);`
- `sources/androidx/camera/video/internal/QualityExploredEncoderProfilesProvider.java:97`
  `treeMap.put(new Size(defaultVideoProfile.getWidth(), defaultVideoProfile.getHeight()), videoValidatedEncoderProfilesProxyFindNearestHigherSupportedEncoderProfilesFor);`
- `sources/androidx/camera/video/internal/compat/quirk/ExtraSupportedQualityQuirk.java:48`
  `map.put(4, immutableEncoderProfilesProxyCreate);`
- `sources/androidx/camera/video/internal/compat/quirk/ExtraSupportedQualityQuirk.java:50`
  `map.put(1, immutableEncoderProfilesProxyCreate);`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridState.java:709`
  `this.currentItemPrefetchHandles.put(Integer.valueOf(index), this.prefetchState.m991schedulePrefetch0kLqBqw(index, jM5637fixedHeightOenEA2s));`
- `sources/androidx/compose/foundation/text/modifiers/TextStringSimpleNode.java:228`
  `linkedHashMap.put(AlignmentLineKt.getLastBaseline(), Integer.valueOf(MathKt.roundToInt(paragraph.getLastBaseline())));`
- `sources/androidx/compose/material/ripple/CommonRippleIndicationInstance.java:78`
  `this.ripples.put(interaction, rippleAnimation);`
- `sources/androidx/compose/ui/input/pointer/PointerInputChangeEventProducer.java:39`
  `linkedHashMap.put(PointerId.m4475boximpl(pointerInputEventData.m4508getIdJ3iCeTQ()), new PointerInputChange(pointerInputEventData.m4508getIdJ3iCeTQ(), pointerInputEventData.getUptime(), pointerInputEventData.m4509getPositionF1C5BW0(), pointerInputEventData.getDown(), pointerInputEventData.getPressur...`
- `sources/androidx/compose/ui/input/pointer/PointerInputChangeEventProducer.java:41`
  `this.previousPointerInputData.put(PointerId.m4475boximpl(pointerInputEventData.m4508getIdJ3iCeTQ()), new PointerInputData(pointerInputEventData.getUptime(), pointerInputEventData.m4510getPositionOnScreenF1C5BW0(), pointerInputEventData.getDown(), pointerInputEventData.m4512getTypeT8wyACA(), null));`
- `sources/androidx/constraintlayout/compose/ConstraintSetParserKt.java:624`
  `layoutVariables.put(elementName, f, f2, 1.0f, str, stringOrNull2);`
- `sources/androidx/constraintlayout/compose/ConstraintSetParserKt.java:633`
  `layoutVariables.put(elementName, f3, f4);`
- `sources/androidx/constraintlayout/compose/LayoutVariables.java:29`
  `this.generators.put(elementName, new Generator(start, incrementBy));`
- `sources/androidx/constraintlayout/compose/LayoutVariables.java:40`
  `this.generators.put(elementName, finiteGenerator);`
- `sources/androidx/constraintlayout/compose/LayoutVariables.java:41`
  `this.arrayIds.put(elementName, finiteGenerator.array());`
- `sources/androidx/constraintlayout/compose/Measurer.java:251`
  `getPlaceables().put(companionWidget, placeableMo4614measureBRTryo0);`
- `sources/androidx/constraintlayout/compose/Measurer.java:501`
  `getPlaceables().put(companionWidget2, ((Measurable) companionWidget2).mo4614measureBRTryo0(Constraints.INSTANCE.m5636fixedJhjzzOo(constraintWidget2.getWidth(), constraintWidget2.getHeight())));`
- `sources/androidx/constraintlayout/compose/ToolingUtilsKt.java:30`
  `@Metadata(d1 = {"\u0000h\n\u0000\n\u0002\u0010\b\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\b\t\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010!\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u001...`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:648`
  `this.mTempMapIdToWidget.put(0, this.mLayoutWidget);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:649`
  `this.mTempMapIdToWidget.put(getId(), this.mLayoutWidget);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:652`
  `this.mTempMapIdToWidget.put(childAt4.getId(), getViewWidget(childAt4));`
- `sources/androidx/coordinatorlayout/widget/DirectedAcyclicGraph.java:34`
  `this.mGraph.put(t, emptyList);`
- `sources/androidx/core/graphics/TypefaceCompatApi24Impl.java:102`
  `simpleArrayMap.put(uri, byteBufferMmap);`
- `sources/androidx/core/location/LocationManagerCompat.java:124`
  `WeakReference<LocationListenerTransport> weakReferencePut = sLocationListeners.put(locationListenerTransport.getKey(), new WeakReference<>(locationListenerTransport));`
- `sources/androidx/core/location/LocationManagerCompat.java:224`
  `GnssListenersHolder.sGnssMeasurementListeners.put(gnssMeasurementsEvent$Callback, gnssMeasurementsTransport);`
- `sources/androidx/core/location/LocationManagerCompat.java:965`
  `GnssListenersHolder.sGnssStatusListeners.put(callback, gnssStatusTransport);`
- `sources/androidx/core/location/LocationManagerCompat.java:1068`
  `GnssListenersHolder.sGnssStatusListeners.put(callback, preRGnssStatusTransport);`
- `sources/androidx/health/connect/client/impl/platform/records/ResponseConvertersKt.java:256`
  `mapCreateMapBuilder.put(metricKey$connect_client_release2, Double.valueOf(companion.calories(PrintHelper$$ExternalSyntheticApiModelOutline0.m6435m(value).getInCalories()).getKilocalories()));`
- `sources/androidx/health/connect/client/units/BloodGlucose.java:113`
  `linkedHashMap.put(type, new BloodGlucose(0.0d, type));`
- `sources/androidx/heifwriter/EglRectBlt.java:76`
  `this.mTexCoordArray.put(this.mTexCoords);`
- `sources/androidx/transition/ChangeBounds.java:154`
  `transitionValues.values.put(PROPNAME_BOUNDS, new Rect(view.getLeft(), view.getTop(), view.getRight(), view.getBottom()));`
- `sources/androidx/transition/ChangeBounds.java:155`
  `transitionValues.values.put(PROPNAME_PARENT, transitionValues.view.getParent());`

## BR020

paper_id: B012
paper_title: Reviewing the data security and privacy policies of mobile apps for depression

- `sources/androidx/appcompat/widget/SearchView.java:93`
  `CursorAdapter mSuggestionsAdapter;`
- `sources/androidx/camera/core/UseCase.java:353`
  `throw new UnsupportedOperationException("Attempt to update the implementation options for a use case without attached stream specifications.");`
- `sources/androidx/camera/video/Recorder.java:2182`
  `throw new AssertionError("Attempted to update event listener with event from incorrect recording [Recording: " + videoRecordEvent.getOutputOptions() + ", Expected: " + getOutputOptions() + "]");`
- `sources/androidx/compose/foundation/text/AndroidCursorHandle_androidKt.java:37`
  `/* JADX INFO: compiled from: AndroidCursorHandle.android.kt */`
- `sources/androidx/compose/foundation/text/AndroidCursorHandle_androidKt.java:39`
  `@Metadata(d1 = {"\u0000.\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0010\u0007\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0006\u001a:\u0010\t\u001a\u00020\n2\u0006\u0010\u000b\u001a\u00020\f...`
- `sources/androidx/compose/foundation/text/AndroidCursorHandle_androidKt.java:40`
  `public final class AndroidCursorHandle_androidKt {`
- `sources/androidx/compose/foundation/text/AndroidCursorHandle_androidKt.java:41`
  `private static final float CursorHandleHeight;`
- `sources/androidx/compose/foundation/text/AndroidCursorHandle_androidKt.java:42`
  `private static final float CursorHandleWidth;`
- `sources/androidx/compose/foundation/text/AndroidCursorHandle_androidKt.java:45`
  `public static final float getCursorHandleHeight() {`
- `sources/androidx/compose/foundation/text/AndroidCursorHandle_androidKt.java:46`
  `return CursorHandleHeight;`
- `sources/androidx/compose/foundation/text/AndroidCursorHandle_androidKt.java:49`
  `public static final float getCursorHandleWidth() {`
- `sources/androidx/compose/foundation/text/AndroidCursorHandle_androidKt.java:50`
  `return CursorHandleWidth;`
- `sources/androidx/compose/foundation/text/AndroidCursorHandle_androidKt.java:154`
  `ComposerKt.traceEventStart(694251107, i, -1, "androidx.compose.foundation.text.DefaultCursorHandle (AndroidCursorHandle.android.kt:57)");`
- `sources/androidx/compose/foundation/text/AndroidCursorHandle_androidKt.java:156`
  `SpacerKt.Spacer(drawCursorHandle(SizeKt.m873sizeVpY3zN4(modifier, CursorHandleWidth, CursorHandleHeight)), composerStartRestartGroup, 0);`
- `sources/androidx/compose/foundation/text/AndroidCursorHandle_androidKt.java:212`
  `objRememberedValue = (Function1) new Function1<CacheDrawScope, DrawResult>() { // from class: androidx.compose.foundation.text.AndroidCursorHandle_androidKt$drawCursorHandle$1$1$1`
- `sources/androidx/compose/foundation/text/AndroidCursorHandle_androidKt.java:272`
  `CursorHandleHeight = fM5684constructorimpl;`
- `sources/androidx/compose/foundation/text/AndroidCursorHandle_androidKt.java:273`
  `CursorHandleWidth = Dp.m5684constructorimpl(Dp.m5684constructorimpl(fM5684constructorimpl * 2.0f) / 2.4142137f);`
- `sources/androidx/compose/foundation/text/CoreTextFieldKt.java:70`
  `@Metadata(d1 = {"\u0000\u009a\u0001\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0...`
- `sources/androidx/compose/foundation/text/CoreTextFieldKt.java:394`
  `if (state != null && state.getShowCursorHandle()) {`
- `sources/androidx/compose/foundation/text/CoreTextFieldKt.java:400`
  `objRememberedValue = manager.cursorDragObserver$foundation_release();`
- `sources/androidx/compose/foundation/text/CoreTextFieldKt.java:411`
  `Offset offsetM3068boximpl = Offset.m3068boximpl(jM1309getCursorPositiontuRUvjQ$foundation_release);`
- `sources/androidx/compose/foundation/text/CoreTextFieldKt.java:417`
  `objRememberedValue2 = (Function1) new Function1<SemanticsPropertyReceiver, Unit>() { // from class: androidx.compose.foundation.text.CoreTextFieldKt$TextFieldCursorHandle$2$1`
- `sources/androidx/compose/foundation/text/HorizontalScrollLayoutModifier.java:108`
  `return (((((this.scrollerPosition.hashCode() * 31) + this.cursorOffset) * 31) + this.transformedText.hashCode()) * 31) + this.textLayoutResultProvider.hashCode();`
- `sources/androidx/compose/foundation/text/TextFieldCursorKt.java:45`
  `/* JADX INFO: compiled from: TextFieldCursor.kt */`
- `sources/androidx/compose/foundation/text/TextFieldCursorKt.java:47`
  `@Metadata(d1 = {"\u00008\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\u0010\u0007\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000b\n\u0000\u001a4\u0010\b\...`
- `sources/androidx/compose/foundation/text/TextFieldCursorKt.java:48`
  `public final class TextFieldCursorKt {`
- `sources/androidx/compose/foundation/text/TextFieldCursorKt.java:49`
  `private static final AnimationSpec<Float> cursorAnimationSpec = AnimationSpecKt.m428infiniteRepeatable9IiC70o$default(AnimationSpecKt.keyframes(new Function1<KeyframesSpec.KeyframesSpecConfig<Float>, Unit>() { // from class: androidx.compose.foundation.text.TextFieldCursorKt$cursorAnimationSpec$1`
- `sources/androidx/compose/foundation/text/TextFieldCursorKt.java:93`
  `ComposerKt.traceEventStart(1634330012, i, -1, "androidx.compose.foundation.text.cursor.<anonymous> (TextFieldCursor.kt:44)");`
- `sources/androidx/compose/foundation/text/TextFieldState.java:29`
  `@Metadata(d1 = {"\u0000ª\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0007\n\u0002\u0010\u000b\n\u0002\b\u0007\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n...`
- `sources/androidx/compose/foundation/text/TextFieldState.java:76`
  `this.showCursorHandle = SnapshotStateKt__SnapshotStateKt.mutableStateOf$default(false, null, 2, null);`
- `sources/androidx/compose/foundation/text/VerticalScrollLayoutModifier.java:107`
  `return (((((this.scrollerPosition.hashCode() * 31) + this.cursorOffset) * 31) + this.transformedText.hashCode()) * 31) + this.textLayoutResultProvider.hashCode();`
- `sources/androidx/compose/foundation/text/VerticalScrollLayoutModifier.java:188`
  `int cursorOffset = this.getCursorOffset();`
- `sources/androidx/compose/foundation/text/VerticalScrollLayoutModifier.java:191`
  `this.getScrollerPosition().update(Orientation.Vertical, TextFieldScrollKt.getCursorRectInScroller(measureScope, cursorOffset, transformedText, textLayoutResultProxyInvoke != null ? textLayoutResultProxyInvoke.getValue() : null, false, placeableMo4614measureBRTryo0.getWidth()), iMin, placeableMo4614m...`
- `sources/androidx/compose/foundation/text/selection/BaseTextPreparedSelection.java:26`
  `@Metadata(d1 = {"\u0000T\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0015\n\u0002\u0010\u000e\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\b\u0003\n\u...`
- `sources/androidx/compose/foundation/text/selection/TextFieldPreparedSelection.java:20`
  `@Metadata(d1 = {"\u0000B\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u001...`
- `sources/androidx/compose/foundation/text/selection/TextFieldPreparedSelection.java:111`
  `androidx.compose.ui.geometry.Rect r0 = r1.getCursorRect(r0)`
- `sources/androidx/compose/foundation/text/selection/TextFieldSelectionManager.java:45`
  `@Metadata(d1 = {"\u0000¸\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0010\b\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0010\u000b\n\u0002\b\u0007\n\u0002\u0018...`
- `sources/androidx/compose/material/TextFieldDefaults.java:29`
  `@Metadata(d1 = {"\u0000p\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u0007\n\u0000\n\u0002\u0018\u0002\n\u0002\b\t\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0010\u0002\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0007...`
- `sources/androidx/compose/material3/OutlinedTextFieldDefaults.java:20`
  `@Metadata(d1 = {"\u0000j\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\n\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0010\u000e\n\u...`
- `sources/androidx/compose/material3/SearchBarDefaults.java:21`
  `@Metadata(d1 = {"\u0000B\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0007\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u00...`

## BR021

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `resources/AndroidManifest.xml:437`
  `<provider`
- `resources/AndroidManifest.xml:446`
  `<provider`
- `resources/AndroidManifest.xml:467`
  `<provider`
- `resources/AndroidManifest.xml:491`
  `<provider`
- `resources/AndroidManifest.xml:561`
  `<provider`
- `resources/AndroidManifest.xml:570`
  `<provider`
- `resources/AndroidManifest.xml:583`
  `<provider`
- `resources/AndroidManifest.xml:733`
  `<provider`
- `resources/AndroidManifest.xml:791`
  `<provider`
- `resources/AndroidManifest.xml:827`
  `<provider`
- `resources/AndroidManifest.xml:842`
  `<provider`

## BR022

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `resources/res/xml/camera_provider_paths.xml:3`
  `<external-files-path`
- `resources/res/xml/file_paths_select_pic_public.xml:3`
  `<external-path`
- `resources/res/xml/image_share_filepaths.xml:3`
  `<files-path`
- `resources/res/xml/localnotification_provider_paths.xml:3`
  `<external-path`
- `resources/res/xml/share_file_provider_paths.xml:3`
  `<cache-path`
- `resources/res/xml/share_file_provider_paths.xml:6`
  `<cache-path`
- `resources/res/xml/util_code_provider_paths.xml:3`
  `<root-path`
- `resources/res/xml/util_code_provider_paths.xml:6`
  `<files-path`
- `resources/res/xml/util_code_provider_paths.xml:9`
  `<cache-path`
- `resources/res/xml/util_code_provider_paths.xml:12`
  `<external-path`
- `resources/res/xml/util_code_provider_paths.xml:15`
  `<external-files-path`
- `resources/res/xml/util_code_provider_paths.xml:18`
  `<external-cache-path`

## BR023

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `sources/androidx/startup/InitializationProvider.java:10`
  `public class InitializationProvider extends ContentProvider {`
- `sources/com/google/android/gms/measurement/AppMeasurementContentProvider.java:15`
  `public class AppMeasurementContentProvider extends ContentProvider {`
- `sources/com/google/firebase/provider/FirebaseInitProvider.java:16`
  `public class FirebaseInitProvider extends ContentProvider {`
- `sources/com/google/mlkit/common/internal/MlKitInitProvider.java:15`
  `public class MlKitInitProvider extends ContentProvider {`
- `sources/com/marianhello/bgloc/data/provider/LocationContentProvider.java:19`
  `public class LocationContentProvider extends ContentProvider {`
- `sources/com/squareup/picasso/PicassoProvider.java:10`
  `public final class PicassoProvider extends ContentProvider {`

## BR024

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `sources/androidx/core/content/FileProvider.java:71`
  `if (!providerInfo.grantUriPermissions) {`
- `sources/androidx/core/content/IntentSanitizer.java:122`
  `consumer.accept("Allowing Extra Stream requires also allowing at least  FLAG_GRANT_READ_URI_PERMISSION Flag.");`
- `sources/androidx/core/content/IntentSanitizer.java:124`
  `consumer.accept("Allowing Extra Output requires also allowing FLAG_GRANT_READ_URI_PERMISSION and FLAG_GRANT_WRITE_URI_PERMISSION Flags.");`

## BR025

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:173`
  `Api17Impl.setTextLocale(this.mView, Api21Impl.forLanguageTag(string2.split(SQLiteOpenHelper.COMMA_SEP)[0]));`
- `sources/androidx/compose/ui/platform/AndroidComposeViewAccessibilityDelegateCompat.java:1401`
  `accessibilityEventCreateEvent$ui_release.setContentDescription(TempListUtilsKt.fastJoinToString$default(contentDescription, SQLiteOpenHelper.COMMA_SEP, null, null, 0, null, null, 62, null));`
- `sources/androidx/compose/ui/platform/AndroidComposeViewAccessibilityDelegateCompat.java:2205`
  `return TempListUtilsKt.fastJoinToString$default((List) node.getUnmergedConfig().get(SemanticsProperties.INSTANCE.getContentDescription()), SQLiteOpenHelper.COMMA_SEP, null, null, 0, null, null, 62, null);`
- `sources/androidx/constraintlayout/core/motion/utils/SplineSet.java:209`
  `this.mAttributeName = str.split(SQLiteOpenHelper.COMMA_SEP)[1];`
- `sources/androidx/constraintlayout/core/motion/utils/SplineSet.java:272`
  `this.mAttributeName = str.split(SQLiteOpenHelper.COMMA_SEP)[1];`
- `sources/androidx/constraintlayout/core/motion/utils/TimeCycleSplineSet.java:95`
  `this.mAttributeName = str.split(SQLiteOpenHelper.COMMA_SEP)[1];`
- `sources/androidx/constraintlayout/core/motion/utils/TimeCycleSplineSet.java:320`
  `this.mAttributeName = str.split(SQLiteOpenHelper.COMMA_SEP)[1];`
- `sources/androidx/constraintlayout/motion/widget/SplineSet.java:376`
  `this.mAttributeName = str.split(SQLiteOpenHelper.COMMA_SEP)[1];`
- `sources/androidx/constraintlayout/motion/widget/TimeCycleSplineSet.java:395`
  `this.mAttributeName = str.split(SQLiteOpenHelper.COMMA_SEP)[1];`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1152`
  `String[] strArrSplit = ((String) tag).split(SQLiteOpenHelper.COMMA_SEP);`
- `sources/androidx/core/os/LocaleListCompat.java:72`
  `String[] strArrSplit = str.split(SQLiteOpenHelper.COMMA_SEP, -1);`
- `sources/androidx/room/AutoCloser.java:65`
  `public void init(SupportSQLiteOpenHelper supportSQLiteOpenHelper) {`
- `sources/androidx/room/AutoCloser.java:69`
  `this.mDelegateOpenHelper = supportSQLiteOpenHelper;`
- `sources/androidx/room/AutoCloser.java:73`
  `public <V> V executeRefCountingFunction(Function<SupportSQLiteDatabase, V> function) {`
- `sources/androidx/room/AutoCloser.java:81`
  `public SupportSQLiteDatabase incrementCountAndEnsureDbIsOpen() {`
- `sources/androidx/room/AutoCloser.java:88`
  `SupportSQLiteDatabase supportSQLiteDatabase = this.mDelegateDatabase;`
- `sources/androidx/room/AutoCloser.java:89`
  `if (supportSQLiteDatabase != null && supportSQLiteDatabase.isOpen()) {`
- `sources/androidx/room/AutoCloser.java:92`
  `SupportSQLiteOpenHelper supportSQLiteOpenHelper = this.mDelegateOpenHelper;`
- `sources/androidx/room/AutoCloser.java:93`
  `if (supportSQLiteOpenHelper != null) {`
- `sources/androidx/room/AutoCloser.java:94`
  `SupportSQLiteDatabase writableDatabase = supportSQLiteOpenHelper.getWritableDatabase();`
- `sources/androidx/room/InvalidationTracker.java:180`
  `void internalInit(SupportSQLiteDatabase supportSQLiteDatabase) {`
- `sources/androidx/room/InvalidationTracker.java:186`
  `supportSQLiteDatabase.execSQL("PRAGMA temp_store = MEMORY;");`
- `sources/androidx/room/InvalidationTracker.java:187`
  `supportSQLiteDatabase.execSQL("PRAGMA recursive_triggers='ON';");`
- `sources/androidx/room/InvalidationTracker.java:188`
  `supportSQLiteDatabase.execSQL(CREATE_TRACKING_TABLE_SQL);`
- `sources/androidx/room/InvalidationTracker.java:189`
  `syncTriggers(supportSQLiteDatabase);`
- `sources/androidx/room/InvalidationTracker.java:190`
  `this.mCleanupStatement = supportSQLiteDatabase.compileStatement(RESET_UPDATED_TABLES_SQL);`
- `sources/androidx/room/InvalidationTracker.java:234`
  `private void startTrackingTable(SupportSQLiteDatabase supportSQLiteDatabase, int i) {`
- `sources/androidx/room/InvalidationTracker.java:235`
  `supportSQLiteDatabase.execSQL("INSERT OR IGNORE INTO room_table_modification_log VALUES(" + i + ", 0)");`
- `sources/androidx/room/RoomDatabase.java:16`
  `import androidx.sqlite.db.SupportSQLiteDatabase;`
- `sources/androidx/room/RoomDatabase.java:17`
  `import androidx.sqlite.db.SupportSQLiteOpenHelper;`
- `sources/androidx/room/RoomDatabase.java:20`
  `import androidx.sqlite.db.framework.FrameworkSQLiteOpenHelperFactory;`
- `sources/androidx/room/SQLiteCopyOpenHelper.java:171`
  `SupportSQLiteDatabase readableDatabase;`
- `sources/com/evyd/core/mobile/android/health/delegate/TrackSportUtil.java:16`
  `import com.marianhello.bgloc.data.sqlite.SQLiteOpenHelper;`
- `sources/com/evyd/core/mobile/android/health/track/TrackLocationManager.java:12`
  `import com.marianhello.bgloc.data.sqlite.SQLiteOpenHelper;`
- `sources/com/evyd/core/mobile/android/health/track/TrackLocationManager.java:221`
  `HealthConfig.INSTANCE.logE(getTag(), "[" + source + "]onLocationChanged(valid:" + z + ") = time(" + formatDate(this.appForegroundTime) + "/" + formatDate$default(this, 0L, 1, null) + ")(" + location.getLatitude() + SQLiteOpenHelper.COMMA_SEP + location.getLongitude() + SqlExpression.SqlEnclosureClos...`
- `sources/com/evyd/core/trtcroom/room/widget/videolayout/TRTCVideoRoomLayoutManager.java:126`
  `sb.append(SQLiteOpenHelper.COMMA_SEP);`
- `sources/com/evyd/core/trtcroom/room/widget/videolayout/TRTCVideoRoomLayoutManager.java:643`
  `sb.append(SQLiteOpenHelper.COMMA_SEP);`
- `sources/com/google/android/datatransport/runtime/backends/MetadataBackendRegistry.java:9`
  `import com.marianhello.bgloc.data.sqlite.SQLiteOpenHelper;`
- `sources/com/google/android/datatransport/runtime/backends/MetadataBackendRegistry.java:101`
  `for (String str2 : ((String) obj).split(SQLiteOpenHelper.COMMA_SEP, -1)) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:4`
  `import android.database.sqlite.SQLiteDatabase;`

## BR026

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/androidx/datastore/core/SingleProcessDataStore$readAndInit$api$1$updateData$1.java:1`
  `package androidx.datastore.core;`
- `sources/androidx/datastore/core/SingleProcessDataStore$readAndInit$api$1$updateData$1.java:10`
  `/* JADX INFO: compiled from: SingleProcessDataStore.kt */`
- `sources/androidx/datastore/core/SingleProcessDataStore$readAndInit$api$1$updateData$1.java:13`
  `@DebugMetadata(c = "androidx.datastore.core.SingleProcessDataStore$readAndInit$api$1", f = "SingleProcessDataStore.kt", i = {0, 0, 1, 2, 2}, l = {TypedValues.PositionType.TYPE_PERCENT_WIDTH, TokenId.SWITCH, TokenId.THIS}, m = "updateData", n = {"transform", "$this$withLock_u24default$iv", "$this$wit...`
- `sources/androidx/datastore/core/SingleProcessDataStore$readAndInit$api$1$updateData$1.java:14`
  `final class SingleProcessDataStore$readAndInit$api$1$updateData$1 extends ContinuationImpl {`
- `sources/androidx/datastore/core/SingleProcessDataStore.java:94`
  `/* JADX INFO: renamed from: androidx.datastore.core.SingleProcessDataStore$readAndInit$1, reason: invalid class name and case insensitive filesystem */`
- `sources/androidx/datastore/core/SingleProcessDataStore.java:95`
  `/* JADX INFO: compiled from: SingleProcessDataStore.kt */`
- `sources/androidx/datastore/core/SingleProcessDataStore.java:97`
  `@DebugMetadata(c = "androidx.datastore.core.SingleProcessDataStore", f = "SingleProcessDataStore.kt", i = {0, 0, 1, 1, 1, 2}, l = {TokenId.IMPORT, 348, TypedValues.PositionType.TYPE_SIZE_PERCENT}, m = "readAndInit", n = {"updateLock", "initData", "updateLock", "initData", "initializationComplete", "...`
- `sources/androidx/datastore/core/SingleProcessDataStore.java:197`
  `/* JADX INFO: renamed from: androidx.datastore.core.SingleProcessDataStore$readDataOrHandleCorruption$1, reason: invalid class name and case insensitive filesystem */`
- `sources/androidx/datastore/core/SingleProcessDataStore.java:198`
  `/* JADX INFO: compiled from: SingleProcessDataStore.kt */`
- `sources/androidx/datastore/core/SingleProcessDataStore.java:200`
  `@DebugMetadata(c = "androidx.datastore.core.SingleProcessDataStore", f = "SingleProcessDataStore.kt", i = {0, 1, 2, 2}, l = {TokenId.GE, TokenId.PLUSPLUS, TokenId.LSHIFT_E}, m = "readDataOrHandleCorruption", n = {"this", "ex", "ex", "newData"}, s = {"L$0", "L$1", "L$0", "L$1"})`
- `sources/androidx/datastore/core/SingleProcessDataStore.java:206`
  `final /* synthetic */ SingleProcessDataStore<T> this$0;`
- `sources/androidx/datastore/core/SingleProcessDataStore.java:222`
  `/* JADX INFO: renamed from: androidx.datastore.core.SingleProcessDataStore$transformAndWrite$1, reason: invalid class name and case insensitive filesystem */`
- `sources/androidx/datastore/core/SingleProcessDataStore.java:223`
  `/* JADX INFO: compiled from: SingleProcessDataStore.kt */`
- `sources/androidx/datastore/core/SingleProcessDataStore.java:225`
  `@DebugMetadata(c = "androidx.datastore.core.SingleProcessDataStore", f = "SingleProcessDataStore.kt", i = {0, 0, 0}, l = {402, TokenId.TRUE}, m = "transformAndWrite", n = {"this", "curDataAndHash", "curData"}, s = {"L$0", "L$1", "L$2"})`
- `sources/androidx/datastore/preferences/core/PreferencesKt.java:1`
  `package androidx.datastore.preferences.core;`
- `sources/androidx/datastore/preferences/core/PreferencesKt.java:3`
  `import androidx.datastore.core.DataStore;`
- `sources/androidx/datastore/preferences/core/PreferencesKt.java:16`
  `@Metadata(d1 = {"\u0000$\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\u001a?\u0010\u0000\u001a\u00020\u0001*\b\u0012\u0004\u0012\u00020\u00010\u00022\"\u0010\u0003\u001a\u00...`
- `sources/androidx/datastore/preferences/core/PreferencesKt.java:19`
  `/* JADX INFO: renamed from: androidx.datastore.preferences.core.PreferencesKt$edit$2, reason: invalid class name */`
- `sources/androidx/datastore/preferences/core/PreferencesKt.java:21`
  `@Metadata(d1 = {"\u0000\b\n\u0000\n\u0002\u0018\u0002\n\u0000\u0010\u0000\u001a\u00020\u00012\u0006\u0010\u0002\u001a\u00020\u0001H\u008a@"}, d2 = {"<anonymous>", "Landroidx/datastore/preferences/core/Preferences;", "it"}, k = 3, mv = {1, 5, 1}, xi = 48)`
- `sources/androidx/datastore/preferences/core/PreferencesKt.java:22`
  `@DebugMetadata(c = "androidx.datastore.preferences.core.PreferencesKt$edit$2", f = "Preferences.kt", i = {}, l = {TokenId.PACKAGE}, m = "invokeSuspend", n = {}, s = {})`
- `sources/androidx/datastore/preferences/protobuf/AbstractProtobufList.java:1`
  `package androidx.datastore.preferences.protobuf;`
- `sources/androidx/datastore/preferences/protobuf/AbstractProtobufList.java:3`
  `import androidx.datastore.preferences.protobuf.Internal;`
- `sources/androidx/datastore/preferences/protobuf/BinaryWriter.java:1`
  `package androidx.datastore.preferences.protobuf;`
- `sources/androidx/datastore/preferences/protobuf/BinaryWriter.java:4`
  `import androidx.datastore.preferences.protobuf.Internal;`
- `sources/androidx/datastore/preferences/protobuf/BinaryWriter.java:5`
  `import androidx.datastore.preferences.protobuf.MapEntryLite;`
- `sources/androidx/datastore/preferences/protobuf/BinaryWriter.java:6`
  `import androidx.datastore.preferences.protobuf.Utf8;`
- `sources/androidx/datastore/preferences/protobuf/BinaryWriter.java:7`
  `import androidx.datastore.preferences.protobuf.WireFormat;`
- `sources/androidx/datastore/preferences/protobuf/BinaryWriter.java:8`
  `import androidx.datastore.preferences.protobuf.Writer;`
- `sources/androidx/datastore/preferences/protobuf/BooleanArrayList.java:1`
  `package androidx.datastore.preferences.protobuf;`
- `sources/androidx/datastore/preferences/protobuf/BooleanArrayList.java:3`
  `import androidx.datastore.preferences.protobuf.Internal;`
- `sources/androidx/datastore/preferences/protobuf/ByteString.java:91`
  `UNSIGNED_LEXICOGRAPHICAL_COMPARATOR = new Comparator<ByteString>() { // from class: androidx.datastore.preferences.protobuf.ByteString.2`
- `sources/androidx/datastore/preferences/protobuf/ByteString.java:92`
  `/* JADX WARN: Type inference failed for: r0v0, types: [androidx.datastore.preferences.protobuf.ByteString$ByteIterator] */`
- `sources/androidx/datastore/preferences/protobuf/ByteString.java:93`
  `/* JADX WARN: Type inference failed for: r1v0, types: [androidx.datastore.preferences.protobuf.ByteString$ByteIterator] */`
- `sources/androidx/datastore/preferences/protobuf/CodedOutputStream.java:783`
  `@Override // androidx.datastore.preferences.protobuf.CodedOutputStream`
- `sources/androidx/datastore/preferences/protobuf/DoubleArrayList.java:1`
  `package androidx.datastore.preferences.protobuf;`
- `sources/androidx/datastore/preferences/protobuf/DoubleArrayList.java:3`
  `import androidx.datastore.preferences.protobuf.Internal;`
- `sources/androidx/datastore/preferences/protobuf/FloatArrayList.java:1`
  `package androidx.datastore.preferences.protobuf;`
- `sources/androidx/datastore/preferences/protobuf/FloatArrayList.java:3`
  `import androidx.datastore.preferences.protobuf.Internal;`
- `sources/androidx/datastore/preferences/protobuf/IntArrayList.java:1`
  `package androidx.datastore.preferences.protobuf;`
- `sources/androidx/datastore/preferences/protobuf/IntArrayList.java:3`
  `import androidx.datastore.preferences.protobuf.Internal;`

## BR027

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/androidx/activity/result/contract/ActivityResultContracts.java:12`
  `import android.provider.MediaStore;`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:120`
  `File file = new File(this.mAppContext.getFilesDir(), BrowserServiceFileProvider.FILE_SUB_DIR);`
- `sources/androidx/camera/video/Recorder.java:2057`
  `if (outputOptions instanceof MediaStoreOutputOptions) {`
- `sources/androidx/camera/video/Recorder.java:2058`
  `final MediaStoreOutputOptions mediaStoreOutputOptions = (MediaStoreOutputOptions) outputOptions;`
- `sources/androidx/camera/video/Recorder.java:2115`
  `String absolutePathFromUri = OutputUtil.getAbsolutePathFromUri(mediaStoreOutputOptions.getContentResolver(), uriInsert, Recorder.MEDIA_COLUMN);`
- `sources/androidx/camera/video/Recorder.java:2119`
  `if (!OutputUtil.createParentFolder(new File(absolutePathFromUri))) {`
- `sources/androidx/camera/video/Recorder.java:2124`
  `ParcelFileDescriptor parcelFileDescriptorOpenFileDescriptor = mediaStoreOutputOptions.getContentResolver().openFileDescriptor(uriInsert, "rw");`
- `sources/androidx/camera/video/internal/compat/quirk/DeviceQuirksLoader.java:39`
  `if (quirkSettings.shouldEnableQuirk(MediaStoreVideoCannotWrite.class, MediaStoreVideoCannotWrite.load())) {`
- `sources/androidx/camera/video/internal/compat/quirk/DeviceQuirksLoader.java:40`
  `arrayList.add(new MediaStoreVideoCannotWrite());`
- `sources/androidx/camera/view/CameraController.java:743`
  `public Recording startRecording(MediaStoreOutputOptions mediaStoreOutputOptions, AudioConfig audioConfig, Executor executor, Consumer<VideoRecordEvent> consumer) {`
- `sources/androidx/camera/view/CameraController.java:744`
  `return startRecordingInternal(mediaStoreOutputOptions, audioConfig, executor, consumer);`
- `sources/androidx/core/graphics/drawable/IconCompat.java:359`
  `return new FileInputStream(new File((String) this.mObj1));`
- `sources/androidx/core/util/AtomicFile.java:19`
  `this.mNewName = new File(file.getPath() + ".new");`
- `sources/androidx/core/util/AtomicFile.java:20`
  `this.mLegacyBackupName = new File(file.getPath() + ".bak");`
- `sources/androidx/datastore/migrations/SharedPreferencesMigration.java:413`
  `return new File(new File(context.getApplicationInfo().dataDir, "shared_prefs"), Intrinsics.stringPlus(name, ".xml"));`
- `sources/androidx/datastore/migrations/SharedPreferencesMigration.java:417`
  `return new File(Intrinsics.stringPlus(prefsFile.getPath(), ".bak"));`
- `sources/androidx/documentfile/provider/RawDocumentFile.java:31`
  `File file = new File(this.mFile, str2);`
- `sources/androidx/multidex/MultiDex.java:56`
  `doInstallation(context, new File(applicationInfo.sourceDir), new File(applicationInfo.dataDir), "secondary-dexes", "", true);`
- `sources/androidx/multidex/MultiDex.java:83`
  `File file = new File(applicationInfo2.dataDir);`
- `sources/androidx/multidex/MultiDex.java:84`
  `doInstallation(context2, new File(applicationInfo.sourceDir), file, str + "secondary-dexes", str, false);`
- `sources/androidx/multidex/MultiDex.java:85`
  `doInstallation(context2, new File(applicationInfo2.sourceDir), file, "secondary-dexes", "", false);`
- `sources/androidx/multidex/MultiDex.java:234`
  `File file = new File(context.getFilesDir(), "secondary-dexes");`
- `sources/androidx/multidex/MultiDex.java:259`
  `File file2 = new File(file, CODE_CACHE_NAME);`
- `sources/androidx/multidex/MultiDexExtractor.java:61`
  `File file3 = new File(file2, LOCK_FILENAME);`
- `sources/androidx/profileinstaller/ProfileInstaller.java:225`
  `String name = new File(applicationInfo.sourceDir).getName();`
- `sources/androidx/sqlite/db/SupportSQLiteOpenHelper.java:89`
  `SupportSQLiteCompat.Api16Impl.deleteDatabase(new File(str));`
- `sources/androidx/sqlite/db/framework/FrameworkSQLiteOpenHelper.java:41`
  `this.mDelegate = new OpenHelper(this.mContext, new File(SupportSQLiteCompat.Api21Impl.getNoBackupFilesDir(this.mContext), this.mName).getAbsolutePath(), frameworkSQLiteDatabaseArr, this.mCallback);`
- `sources/ch/qos/logback/classic/android/SQLiteAppender.java:226`
  `File file = (str == null || str.trim().length() <= 0) ? null : new File(str);`
- `sources/ch/qos/logback/classic/android/SQLiteAppender.java:233`
  `return new File(CommonPathUtil.getDatabaseDirectoryPath(property), DBLogReader.DB_FILENAME);`
- `sources/ch/qos/logback/core/android/CommonPathUtil.java:19`
  `public static String getExternalStorageDirectoryPath() {`
- `sources/ch/qos/logback/core/android/CommonPathUtil.java:21`
  `return Environment.getExternalStorageDirectory().getAbsolutePath();`
- `sources/ch/qos/logback/core/property/FileExistsPropertyDefiner.java:18`
  `return booleanAsStr(new File(this.path).exists());`
- `sources/ch/qos/logback/core/rolling/FixedWindowRollingPolicy.java:80`
  `if (new File(strConvertInt2).exists()) {`
- `sources/ch/qos/logback/core/rolling/RollingFileAppender.java:113`
  `this.currentlyActiveFile = new File(getFile());`
- `sources/ch/qos/logback/core/rolling/helper/SizeAndTimeBasedArchiveRemover.java:16`
  `File parentFile = new File(this.fileNamePattern.convertMultipleArguments(relativeDate, 0)).getAbsoluteFile().getAbsoluteFile().getParentFile();`
- `sources/ch/qos/logback/core/rolling/helper/TimeBasedArchiveRemover.java:14`
  `File file = new File(this.fileNamePattern.convert(this.rc.getRelativeDate(date, i)));`
- `sources/com/alibaba/android/arouter/utils/ClassUtils.java:119`
  `File file = new File(applicationInfo.sourceDir);`
- `sources/com/alibaba/android/arouter/utils/ClassUtils.java:148`
  `File file = new File((String) Class.forName("com.android.tools.fd.runtime.Paths").getMethod("getDexFileDirectory", String.class).invoke(null, applicationInfo.packageName));`
- `sources/com/blankj/utilcode/util/CleanUtils.java:21`
  `return UtilsBridge.deleteAllInDir(new File(Utils.getApp().getFilesDir().getParent(), "databases"));`
- `sources/com/blankj/utilcode/util/CleanUtils.java:29`
  `return UtilsBridge.deleteAllInDir(new File(Utils.getApp().getFilesDir().getParent(), "shared_prefs"));`

## BR029

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:182`
  `android:exported="true"`
- `resources/AndroidManifest.xml:210`
  `android:exported="true"`
- `resources/AndroidManifest.xml:365`
  `android:exported="true">`
- `resources/AndroidManifest.xml:373`
  `android:exported="true"`
- `resources/AndroidManifest.xml:757`
  `android:exported="true"/>`

## BR030

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:718`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:757`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:800`
  `android:exported="true">`

## BR031

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:392`
  `android:exported="true">`
- `resources/AndroidManifest.xml:622`
  `android:exported="true">`
- `resources/AndroidManifest.xml:862`
  `android:exported="true"`

## BR032

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `resources/AndroidManifest.xml:215`
  `<action android:name="android.intent.action.VIEW"/>`

## BR033

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/androidx/browser/browseractions/BrowserActionsIntent.java:179`
  `return context.getPackageManager().queryIntentActivities(new Intent(ACTION_BROWSER_ACTIONS_OPEN, Uri.parse(TEST_URL)), 131072);`
- `sources/androidx/compose/ui/platform/AndroidUriHandler.java:26`
  `this.context.startActivity(new Intent("android.intent.action.VIEW", Uri.parse(uri)));`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:235`
  `intent.setData(Uri.parse("tel:123456"));`
- `sources/com/blankj/utilcode/util/PermissionUtils.java:153`
  `intent.setData(Uri.parse("package:" + Utils.getApp().getPackageName()));`
- `sources/com/blankj/utilcode/util/PermissionUtils.java:177`
  `intent.setData(Uri.parse("package:" + Utils.getApp().getPackageName()));`
- `sources/com/google/zxing/client/android/book/BrowseBookListener.java:30`
  `Intent intent = new Intent("android.intent.action.VIEW", Uri.parse("http://books.google." + LocaleManager.getBookSearchCountryTLD(this.activity) + "/books?id=" + isbn.substring(isbn.indexOf(61) + 1) + "&pg=" + pageId + "&vq=" + query));`
- `sources/com/google/zxing/client/android/encode/EncodeActivity.java:128`
  `intent.putExtra("android.intent.extra.STREAM", Uri.parse(sb.toString()));`
- `sources/com/google/zxing/client/android/history/HistoryActivity.java:107`
  `Intent intent = new Intent("android.intent.action.SEND", Uri.parse(MailTo.MAILTO_SCHEME));`
- `sources/com/marianhello/bgloc/BackgroundGeolocationFacade.java:389`
  `intent.setData(Uri.parse("package:" + context.getPackageName()));`
- `sources/com/netease/nis/captcha/CaptchaWebView.java:111`
  `CaptchaWebView.this.getContext().startActivity(new Intent("android.intent.action.VIEW", Uri.parse(str)));`
- `sources/egnc/moh/base/utils/ExternalUtils.java:25`
  `Uri uri = Uri.parse(url);`
- `sources/egnc/moh/base/view/MapDialog.java:211`
  `Intent intent = new Intent("android.intent.action.VIEW", Uri.parse(str));`
- `sources/egnc/moh/base/web/CommonWebView.java:306`
  `Intent intent = new Intent("android.intent.action.VIEW", Uri.parse(arg0));`
- `sources/egnc/moh/base/web/CommonWebView.java:435`
  `CommonWebView.this.mContext.startActivity(new Intent("android.intent.action.VIEW", Uri.parse(url)));`
- `sources/egnc/moh/base/web/manager/health/HealthConnectManager.java:765`
  `intent.setData(Uri.parse("https://play.google.com/store/apps/details?id=com.google.android.apps.healthdata"));`
- `sources/egnc/moh/bruhealth/nativeLib/activities/AuthenticationEntryActivity.java:117`
  `this.this$0.startActivity(new Intent("android.intent.action.VIEW", Uri.parse(url)));`
- `sources/io/flutter/plugins/urllauncher/UrlLauncher.java:68`
  `this.activity.startActivity(new Intent("android.intent.action.VIEW").setData(Uri.parse(str)).putExtra("com.android.browser.headers", extractBundle(map)));`
- `sources/io/flutter/plugins/urllauncher/UrlLauncher.java:80`
  `if (openCustomTab(this.activity, Uri.parse(str), bundleExtractBundle, browserOptions)) {`
- `sources/mx/ferreyra/callnumber/CFCallNumber.java:61`
  `intent.setData(Uri.parse(strReplaceAll));`
- `sources/org/apache/cordova/CordovaWebViewImpl.java:177`
  `Uri uri = Uri.parse(str);`
- `sources/org/apache/cordova/inappbrowser/InAppBrowser.java:211`
  `intent.setData(Uri.parse(string));`
- `sources/org/apache/cordova/inappbrowser/InAppBrowser.java:1173`
  `intent.setData(Uri.parse(str));`
- `sources/org/apache/cordova/inappbrowser/InAppBrowser.java:1182`
  `intent2.setData(Uri.parse(str));`
- `sources/org/apache/cordova/inappbrowser/InAppBrowser.java:1201`
  `intent3.setData(Uri.parse("sms:" + strSubstring));`

## BR034

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/androidx/browser/customtabs/CustomTabsIntent.java:108`
  `ContextCompat.startActivity(context, this.intent, this.startAnimationBundle);`
- `sources/androidx/browser/customtabs/TrustedWebUtils.java:32`
  `context.startActivity(intent);`
- `sources/com/badrit/Backbutton/BackbuttonPlugin.java:34`
  `this.cordova.getActivity().startActivity(intent2);`
- `sources/com/blankj/utilcode/util/FileUtils.java:1010`
  `Utils.getApp().sendBroadcast(intent);`
- `sources/com/causahealth/mobile/route/plugin/EvydPlatformPlugin.java:460`
  `this.activity.startActivity(Intent.createChooser(intent, null));`
- `sources/com/evyd/core/mobile/android/health/track/TrackLocationCenter.java:58`
  `app2.startService(intent2);`
- `sources/com/evyd/core/multipicker/selectpic/util/Utils.java:41`
  `context.sendBroadcast(intent);`
- `sources/com/evyd/core/trtcroom/util/TRTCPermissionManager.java:208`
  `context.startActivity(intent);`
- `sources/com/google/android/exoplayer2/offline/DownloadService.java:364`
  `private static void startService(Context context, Intent intent, boolean z) {`
- `sources/com/google/android/gms/measurement/internal/zzhj.java:34`
  `this.zza.doStartService(context, className);`
- `sources/com/google/android/gms/measurement/internal/zznv.java:1062`
  `this.zzm.zza().sendBroadcast(intent);`
- `sources/com/google/mlkit/common/sdkinternal/OptionalModuleUtils.java:196`
  `context.sendBroadcast(intent);`
- `sources/com/marianhello/bgloc/BackgroundGeolocationFacade.java:393`
  `context.startActivity(intent);`
- `sources/egnc/moh/base/utils/ExternalUtils.java:29`
  `activity.startActivity(intent);`
- `sources/egnc/moh/base/web/manager/camera/CameraLauncher.java:506`
  `this.mContext.sendBroadcast(intent);`
- `sources/egnc/moh/base/web/manager/health/GoogleFitStepCounter.java:1136`
  `ActivityUtils.getTopActivity().startActivity(intent);`
- `sources/egnc/moh/base/web/manager/health/HealthConnectManager.java:767`
  `ActivityUtils.getTopActivity().startActivity(intent);`
- `sources/egnc/moh/base/web/manager/videoeditor/VideoEditor.java:211`
  `app.sendBroadcast(intent);`
- `sources/egnc/moh/base/web/trtc/TrtcBridge.java:304`
  `context.startActivity(intent);`
- `sources/egnc/moh/bruhealth/channel/GlucometerBridge.java:175`
  `topActivity.startActivity(intent);`
- `sources/egnc/moh/bruhealth/health/SportLocationCenter.java:56`
  `app2.startService(intent2);`
- `sources/io/flutter/plugin/platform/PlatformPlugin.java:465`
  `this.activity.startActivity(Intent.createChooser(intent, null));`
- `sources/io/flutter/plugins/urllauncher/UrlLauncher.java:68`
  `this.activity.startActivity(new Intent("android.intent.action.VIEW").setData(Uri.parse(str)).putExtra("com.android.browser.headers", extractBundle(map)));`
- `sources/it/nexxa/base64ToGallery/Base64ToGallery.java:77`
  `this.cordova.getActivity().sendBroadcast(intent);`
- `sources/mx/ferreyra/callnumber/CFCallNumber.java:65`
  `this.cordova.getActivity().startActivity(intent);`
- `sources/org/apache/cordova/CordovaWebViewImpl.java:183`
  `this.cordova.getActivity().startActivity(intent);`
- `sources/org/apache/cordova/camera/CameraLauncher.java:480`
  `this.cordova.getActivity().sendBroadcast(intent);`
- `sources/org/apache/cordova/inappbrowser/InAppBrowser.java:212`
  `InAppBrowser.this.cordova.getActivity().startActivity(intent);`
- `sources/org/apache/cordova/inappbrowser/InAppBrowser.java:1174`
  `InAppBrowser.this.cordova.getActivity().startActivity(intent);`
- `sources/org/apache/cordova/inappbrowser/InAppBrowser.java:1183`
  `InAppBrowser.this.cordova.getActivity().startActivity(intent2);`
- `sources/org/apache/cordova/inappbrowser/InAppBrowser.java:1204`
  `InAppBrowser.this.cordova.getActivity().startActivity(intent3);`
- `sources/org/apache/cordova/videoeditor/VideoEditor.java:139`
  `applicationContext.sendBroadcast(intent);`

## BR035

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/com/evgenii/jsevaluator/WebViewWrapper.java:22`
  `this.mWebView.addJavascriptInterface(new JavaScriptInterface(callJavaResultInterface), JsEvaluator.JS_NAMESPACE);`
- `sources/com/evgenii/jsevaluator/WebViewWrapper.java:29`
  `this.mWebView.loadUrl("data:text/html;charset=utf-8;base64," + strEncodeToString);`
- `sources/com/evgenii/jsevaluator/WebViewWrapper.java:40`
  `this.mWebView.loadUrl("about:blank");`
- `sources/com/google/zxing/client/android/HelpActivity.java:21`
  `webView.loadUrl(BASE_URL + "index.html");`
- `sources/com/netease/nis/captcha/a.java:532`
  `captchaWebView.loadUrl("about:blank");`
- `sources/de/appplant/cordova/plugin/localnotification/LocalNotification.java:359`
  `cordovaWebView.loadUrl("javascript:" + str);`
- `sources/egnc/moh/base/web/CommonWebView.java:243`
  `this.mWebView.loadUrl(url, new HashMap());`
- `sources/egnc/moh/base/web/CommonWebView.java:446`
  `view.loadUrl(url);`
- `sources/egnc/moh/base/web/WebViewActivity.java:140`
  `this.webview.getWebView().addJavascriptInterface(this.injector, "flutter_inappwebview");`
- `sources/egnc/moh/bruhealth/activity/MyCordovaActivity.java:304`
  `webView.addJavascriptInterface(javaScriptInjector, "flutter_inappwebview");`
- `sources/egnc/moh/bruhealth/nativeLib/activities/PrivacyUserActivity.java:121`
  `webView4.addJavascriptInterface(javaScriptInjector, "flutter_inappwebview");`
- `sources/egnc/moh/bruhealth/nativeLib/activities/PrivacyUserActivity.java:160`
  `webView2.loadUrl("file:android_asset/html/bruhealth_disclaimer.html?full_screen=no");`
- `sources/egnc/moh/bruhealth/nativeLib/cordovahook/CordovaHookUtils.java:20`
  `webView.addJavascriptInterface(new HookExposedJsApi(bridge), "_cordovaNative");`
- `sources/io/flutter/plugins/urllauncher/WebViewActivity.java:43`
  `webView.loadUrl(webResourceRequest.getUrl().toString());`
- `sources/io/flutter/plugins/urllauncher/WebViewActivity.java:58`
  `WebViewActivity.this.webview.loadUrl(webResourceRequest.getUrl().toString());`
- `sources/io/flutter/plugins/urllauncher/WebViewActivity.java:64`
  `WebViewActivity.this.webview.loadUrl(str);`
- `sources/io/flutter/plugins/urllauncher/WebViewActivity.java:86`
  `this.webview.loadUrl(stringExtra, extractHeaders(intent.getBundleExtra("com.android.browser.headers")));`
- `sources/nl/xservices/plugins/LaunchMyApp.java:74`
  `this.webView.loadUrl("javascript:handleOpenURL('" + URLEncoder.encode(stringWriter.toString()) + "');");`
- `sources/org/apache/cordova/CordovaWebViewImpl.java:97`
  `this.engine.loadUrl(str, false);`
- `sources/org/apache/cordova/CordovaWebViewImpl.java:146`
  `CordovaWebViewImpl.this.engine.loadUrl(str, z2);`
- `sources/org/apache/cordova/NativeToJsMessageQueue.java:224`
  `LoadUrlBridgeMode.this.engine.loadUrl("javascript:" + strPopAndEncodeAsJs, false);`
- `sources/org/apache/cordova/engine/SystemWebViewEngine.java:160`
  `webView.addJavascriptInterface(new SystemExposedJsApi(cordovaBridge), "_cordovaNative");`
- `sources/org/apache/cordova/engine/SystemWebViewEngine.java:165`
  `this.webView.loadUrl(str);`
- `sources/org/apache/cordova/inappbrowser/InAppBrowser.java:206`
  `InAppBrowser.this.webView.loadUrl(string);`
- `sources/org/apache/cordova/inappbrowser/InAppBrowser.java:426`
  `webView.loadUrl("about:blank");`
- `sources/org/apache/cordova/inappbrowser/InAppBrowser.java:463`
  `this.inAppWebView.loadUrl("http://" + str);`
- `sources/org/apache/cordova/inappbrowser/InAppBrowser.java:465`
  `this.inAppWebView.loadUrl(str);`
- `sources/org/apache/cordova/inappbrowser/InAppBrowser.java:906`
  `InAppBrowser.this.inAppWebView.addJavascriptInterface(new Object() { // from class: org.apache.cordova.inappbrowser.InAppBrowser.7.1JsObject`
- `sources/org/apache/cordova/inappbrowser/InAppBrowser.java:944`
  `InAppBrowser.this.inAppWebView.loadUrl(this.val$url);`
- `sources/org/apache/cordova/inappbrowser/InAppBrowser.java:1018`
  `InAppBrowser.this.loadUrl(InAppBrowser.this.inAppWebView.getUrl());`
- `sources/org/apache/cordova/inappbrowser/InAppBrowser.java:1383`
  `this.inAppWebView.loadUrl(str);`

## BR040

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `sources/com/bumptech/glide/ListPreloader.java:29`
  `RequestBuilder<?> getPreloadRequestBuilder(U u);`
- `sources/com/bumptech/glide/ListPreloader.java:111`
  `RequestBuilder<?> preloadRequestBuilder;`
- `sources/com/bumptech/glide/ListPreloader.java:112`
  `if (t == null || (preloadSize = this.preloadDimensionProvider.getPreloadSize(t, i, i2)) == null || (preloadRequestBuilder = this.preloadModelProvider.getPreloadRequestBuilder(t)) == null) {`
- `sources/com/bumptech/glide/ListPreloader.java:115`
  `preloadRequestBuilder.into(this.preloadTargetQueue.next(preloadSize[0], preloadSize[1]));`
- `sources/com/bumptech/glide/integration/compose/PreloadDataImpl.java:30`
  `@Metadata(d1 = {"\u0000V\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002...`
- `sources/com/bumptech/glide/integration/compose/PreloaderData.java:17`
  `@Metadata(d1 = {"\u0000R\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0013...`
- `sources/com/bumptech/glide/integration/compose/PreloaderData.java:119`
  `public final RequestBuilder<Drawable> preloadRequests(RequestManager requestManager, DataT item) {`
- `sources/com/bumptech/glide/integration/compose/PreloadKt.java:23`
  `@Metadata(d1 = {"\u0000R\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u00...`
- `sources/com/bumptech/glide/integration/compose/PreloadModelProvider.java:14`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010!\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\b\u0002\u0018\u0000*\b\b\u0000\u0010\u0001*\u00020\u...`
- `sources/com/bumptech/glide/integration/compose/PreloadModelProvider.java:32`
  `public RequestBuilder<?> getPreloadRequestBuilder(DataT item) {`
- `sources/com/bumptech/glide/integration/compose/PreloadModelProvider.java:34`
  `return this.data.preloadRequests(this.requestManager, item);`
- `sources/com/evyd/core/mobile/android/health/sync/google/GoogleDailyDataSync.java:6`
  `import com.google.android.gms.fitness.request.DataReadRequest;`
- `sources/com/evyd/core/mobile/android/health/sync/google/GoogleDailyDataSync.java:16`
  `@Metadata(d1 = {"\u0000.\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\t\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\b\u0007\u0018\u00002\u00020\u0001B\u0005¢\u0006\u0002\u0010\u0002J\...`
- `sources/com/evyd/core/mobile/android/health/sync/google/GoogleDailyDataSync.java:104`
  `public final DataReadRequest getRequest(long startTime, long endTime) {`
- `sources/com/evyd/core/mobile/android/health/sync/google/GoogleDailyDataSync.java:105`
  `DataReadRequest dataReadRequestBuild = new DataReadRequest.Builder().read(DataType.TYPE_CALORIES_EXPENDED).read(DataType.TYPE_STEP_COUNT_DELTA).read(DataType.TYPE_DISTANCE_DELTA).bucketByActivityType(1, TimeUnit.SECONDS).setTimeRange(startTime, endTime, TimeUnit.MILLISECONDS).build();`
- `sources/com/evyd/core/mobile/android/health/sync/google/GoogleDailyDataSync.java:106`
  `Intrinsics.checkNotNullExpressionValue(dataReadRequestBuild, "build(...)");`
- `sources/com/evyd/core/mobile/android/health/sync/google/GoogleDailyDataSync.java:107`
  `return dataReadRequestBuild;`
- `sources/com/google/android/exoplayer2/offline/DefaultDownloaderFactory.java:29`
  `public Downloader createDownloader(DownloadRequest downloadRequest) {`
- `sources/com/google/android/exoplayer2/offline/DefaultDownloaderFactory.java:30`
  `int iInferContentTypeForUriAndMimeType = Util.inferContentTypeForUriAndMimeType(downloadRequest.uri, downloadRequest.mimeType);`
- `sources/com/google/android/exoplayer2/offline/DefaultDownloaderFactory.java:32`
  `return createDownloader(downloadRequest, iInferContentTypeForUriAndMimeType);`
- `sources/com/google/android/exoplayer2/offline/DefaultDownloaderFactory.java:35`
  `return new ProgressiveDownloader(new MediaItem.Builder().setUri(downloadRequest.uri).setCustomCacheKey(downloadRequest.customCacheKey).build(), this.cacheDataSourceFactory, this.executor);`
- `sources/com/google/android/exoplayer2/offline/DefaultDownloaderFactory.java:40`
  `private Downloader createDownloader(DownloadRequest downloadRequest, int i) {`
- `sources/com/google/android/exoplayer2/offline/DefaultDownloaderFactory.java:46`
  `return constructor.newInstance(new MediaItem.Builder().setUri(downloadRequest.uri).setStreamKeys(downloadRequest.streamKeys).setCustomCacheKey(downloadRequest.customCacheKey).build(), this.cacheDataSourceFactory, this.executor);`
- `sources/com/google/android/exoplayer2/offline/DefaultDownloadIndex.java:15`
  `import com.google.android.exoplayer2.offline.DownloadRequest;`
- `sources/com/google/android/exoplayer2/offline/DefaultDownloadIndex.java:312`
  `DownloadRequest.Builder streamKeys = new DownloadRequest.Builder((String) Assertions.checkNotNull(cursor.getString(0)), Uri.parse((String) Assertions.checkNotNull(cursor.getString(2)))).setMimeType(cursor.getString(1)).setStreamKeys(decodeStreamKeys(cursor.getString(3)));`
- `sources/com/google/android/exoplayer2/offline/DefaultDownloadIndex.java:316`
  `DownloadRequest downloadRequestBuild = streamKeys.setKeySetId(blob).setCustomCacheKey(cursor.getString(4)).setData(cursor.getBlob(5)).build();`
- `sources/com/google/android/exoplayer2/offline/DefaultDownloadIndex.java:321`
  `return new Download(downloadRequestBuild, i, cursor.getLong(7), cursor.getLong(8), cursor.getLong(9), cursor.getInt(10), i == 4 ? cursor.getInt(11) : 0, downloadProgress);`
- `sources/com/google/android/exoplayer2/offline/DefaultDownloadIndex.java:325`
  `DownloadRequest downloadRequestBuild = new DownloadRequest.Builder((String) Assertions.checkNotNull(cursor.getString(0)), Uri.parse((String) Assertions.checkNotNull(cursor.getString(2)))).setMimeType(inferMimeType(cursor.getString(1))).setStreamKeys(decodeStreamKeys(cursor.getString(3))).setCustomCa...`
- `sources/com/google/android/exoplayer2/offline/DefaultDownloadIndex.java:330`
  `return new Download(downloadRequestBuild, i, cursor.getLong(7), cursor.getLong(8), cursor.getLong(9), cursor.getInt(10), i == 4 ? cursor.getInt(11) : 0, downloadProgress);`
- `sources/com/google/android/exoplayer2/offline/Download.java:25`
  `public final DownloadRequest request;`
- `sources/com/google/android/exoplayer2/offline/Download.java:43`
  `public Download(DownloadRequest downloadRequest, int i, long j, long j2, long j3, int i2, int i3) {`
- `sources/com/google/android/exoplayer2/offline/Download.java:44`
  `this(downloadRequest, i, j, j2, j3, i2, i3, new DownloadProgress());`
- `sources/com/google/android/exoplayer2/offline/Download.java:47`
  `public Download(DownloadRequest downloadRequest, int i, long j, long j2, long j3, int i2, int i3, DownloadProgress downloadProgress) {`
- `sources/com/google/android/exoplayer2/offline/Download.java:53`
  `this.request = downloadRequest;`
- `sources/com/google/android/exoplayer2/offline/DownloaderFactory.java:5`
  `Downloader createDownloader(DownloadRequest downloadRequest);`
- `sources/com/google/android/exoplayer2/offline/DownloadHelper.java:27`
  `import com.google.android.exoplayer2.offline.DownloadRequest;`
- `sources/com/google/android/exoplayer2/offline/DownloadHelper.java:314`
  `public static MediaSource createMediaSource(DownloadRequest downloadRequest, DataSource.Factory factory) {`
- `sources/com/google/android/exoplayer2/offline/DownloadHelper.java:315`
  `return createMediaSource(downloadRequest, factory, null);`
- `sources/com/google/android/exoplayer2/offline/DownloadHelper.java:318`
  `public static MediaSource createMediaSource(DownloadRequest downloadRequest, DataSource.Factory factory, DrmSessionManager drmSessionManager) {`
- `sources/com/google/android/exoplayer2/offline/DownloadHelper.java:319`
  `return createMediaSourceInternal(downloadRequest.toMediaItem(), factory, drmSessionManager);`
- `sources/com/google/android/exoplayer2/offline/DownloadHelper.java:499`
  `public DownloadRequest getDownloadRequest(byte[] bArr) {`
- `sources/com/google/android/exoplayer2/offline/DownloadHelper.java:500`
  `return getDownloadRequest(this.localConfiguration.uri.toString(), bArr);`
- `sources/com/google/android/exoplayer2/offline/DownloadHelper.java:503`
  `public DownloadRequest getDownloadRequest(String str, byte[] bArr) {`
- `sources/com/google/android/exoplayer2/offline/DownloadHelper.java:504`
  `DownloadRequest.Builder data = new DownloadRequest.Builder(str, this.localConfiguration.uri).setMimeType(this.localConfiguration.mimeType).setKeySetId(this.localConfiguration.drmConfiguration != null ? this.localConfiguration.drmConfiguration.getKeySetId() : null).setCustomCacheKey(this.localConfigu...`
- `sources/com/google/android/exoplayer2/offline/DownloadManager.java:247`
  `public void addDownload(DownloadRequest downloadRequest) {`
- `sources/com/google/android/exoplayer2/offline/DownloadManager.java:248`
  `addDownload(downloadRequest, 0);`
- `sources/com/google/android/exoplayer2/offline/DownloadManager.java:251`
  `public void addDownload(DownloadRequest downloadRequest, int i) {`
- `sources/com/google/android/exoplayer2/offline/DownloadManager.java:253`
  `this.internalHandler.obtainMessage(6, i, 0, downloadRequest).sendToTarget();`
- `sources/com/google/android/exoplayer2/offline/DownloadManager.java:413`
  `static Download mergeRequest(Download download, DownloadRequest downloadRequest, int i, long j) {`
- `sources/com/google/android/exoplayer2/offline/DownloadManager.java:415`
  `return new Download(download.request.copyWithMergedRequest(downloadRequest), (i2 == 5 || i2 == 7) ? 7 : i != 0 ? 1 : 0, (i2 == 5 || download.isTerminalState()) ? j : download.startTimeMs, j, -1L, i, 0);`
- `sources/com/google/android/exoplayer2/offline/DownloadManager.java:483`
  `addDownload((DownloadRequest) message.obj, message.arg1);`
- `sources/com/google/android/exoplayer2/offline/DownloadManager.java:596`
  `private void addDownload(DownloadRequest downloadRequest, int i) {`
- `sources/com/google/android/exoplayer2/offline/DownloadManager.java:597`
  `Download download = getDownload(downloadRequest.id, true);`
- `sources/com/google/android/exoplayer2/offline/DownloadManager.java:600`
  `putDownload(DownloadManager.mergeRequest(download, downloadRequest, i, jCurrentTimeMillis));`
- `sources/com/google/android/exoplayer2/offline/DownloadManager.java:602`
  `putDownload(new Download(downloadRequest, i != 0 ? 1 : 0, jCurrentTimeMillis, jCurrentTimeMillis, -1L, i, 0));`
- `sources/com/google/android/exoplayer2/offline/DownloadManager.java:906`
  `private final DownloadRequest request;`
- `sources/com/google/android/exoplayer2/offline/DownloadManager.java:908`
  `private Task(DownloadRequest downloadRequest, Downloader downloader, DownloadProgress downloadProgress, boolean z, int i, InternalHandler internalHandler) {`
- `sources/com/google/android/exoplayer2/offline/DownloadManager.java:909`
  `this.request = downloadRequest;`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:17`
  `public final class DownloadRequest implements Parcelable {`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:18`
  `public static final Parcelable.Creator<DownloadRequest> CREATOR = new Parcelable.Creator<DownloadRequest>() { // from class: com.google.android.exoplayer2.offline.DownloadRequest.1`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:21`
  `public DownloadRequest createFromParcel(Parcel parcel) {`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:22`
  `return new DownloadRequest(parcel);`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:27`
  `public DownloadRequest[] newArray(int i) {`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:28`
  `return new DownloadRequest[i];`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:86`
  `public DownloadRequest build() {`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:94`
  `return new DownloadRequest(str, uri, str2, listOf, this.keySetId, this.customCacheKey, this.data);`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:98`
  `private DownloadRequest(String str, Uri uri, String str2, List<StreamKey> list, byte[] bArr, String str3, byte[] bArr2) {`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:114`
  `DownloadRequest(Parcel parcel) {`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:129`
  `public DownloadRequest copyWithId(String str) {`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:130`
  `return new DownloadRequest(str, this.uri, this.mimeType, this.streamKeys, this.keySetId, this.customCacheKey, this.data);`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:133`
  `public DownloadRequest copyWithKeySetId(byte[] bArr) {`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:134`
  `return new DownloadRequest(this.id, this.uri, this.mimeType, this.streamKeys, bArr, this.customCacheKey, this.data);`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:137`
  `public DownloadRequest copyWithMergedRequest(DownloadRequest downloadRequest) {`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:139`
  `Assertions.checkArgument(this.id.equals(downloadRequest.id));`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:140`
  `if (this.streamKeys.isEmpty() || downloadRequest.streamKeys.isEmpty()) {`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:144`
  `for (int i = 0; i < downloadRequest.streamKeys.size(); i++) {`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:145`
  `StreamKey streamKey = downloadRequest.streamKeys.get(i);`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:151`
  `return new DownloadRequest(this.id, downloadRequest.uri, downloadRequest.mimeType, listEmptyList, downloadRequest.keySetId, downloadRequest.customCacheKey, downloadRequest.data);`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:163`
  `if (!(obj instanceof DownloadRequest)) {`
- `sources/com/google/android/exoplayer2/offline/DownloadRequest.java:166`
  `DownloadRequest downloadRequest = (DownloadRequest) obj;`

## BR041

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `resources/AndroidManifest.xml:648`
  `android:name="com.google.firebase.components:com.google.firebase.analytics.ktx.FirebaseAnalyticsLegacyRegistrar"`
- `resources/AndroidManifest.xml:681`
  `android:name="com.google.firebase.components:com.google.firebase.analytics.connector.internal.AnalyticsConnectorRegistrar"`
- `sources/androidx/compose/animation/core/Animations.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/animation/core/AnimationVector.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/animation/core/AnimationVector1D.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/animation/core/AnimationVector2D.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/animation/core/AnimationVector3D.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/animation/core/AnimationVector4D.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/TempListUtilsKt.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/layout/FlowResult.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/LazyDslKt$itemsIndexed$$inlined$itemsIndexed$default$1.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/LazyDslKt$itemsIndexed$$inlined$itemsIndexed$default$2.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/LazyDslKt.java:8`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/LazyListAnimateScrollScope.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/LazyListInterval.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/LazyListIntervalContent.java:10`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/LazyListItemInfo.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/LazyListItemProviderImpl.java:12`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/LazyListMeasuredItem.java:11`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/LazyListMeasuredItemProvider.java:9`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/LazyListMeasureKt.java:12`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/LazyListScope.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/LazyListScrollPosition.java:8`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/LazyListState.java:26`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/grid/LazyGridAnimateScrollScope.java:9`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/grid/LazyGridDslKt.java:16`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/grid/LazyGridInterval.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/grid/LazyGridIntervalContent.java:10`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/grid/LazyGridItemInfo.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/grid/LazyGridItemProviderImpl.java:12`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/grid/LazyGridMeasuredItem.java:12`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/grid/LazyGridMeasuredItemProvider.java:8`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/grid/LazyGridMeasuredLine.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/grid/LazyGridMeasuredLineProvider.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/grid/LazyGridScope.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/grid/LazyGridScrollPosition.java:8`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/grid/LazyGridState.java:29`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/layout/DefaultLazyKey.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/layout/IntervalList.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/layout/LazyAnimateScrollKt.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/layout/LazyAnimateScrollScope.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/layout/LazyLayoutIntervalContent.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/layout/LazyLayoutItemContentFactory.java:12`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/layout/LazyLayoutItemContentFactoryKt.java:10`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/layout/LazyLayoutItemProvider.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/layout/LazyLayoutKeyIndexMap.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/layout/LazyLayoutMeasureScope.java:12`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/layout/LazyLayoutMeasureScopeImpl.java:13`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/layout/LazyLayoutPinnableItem.java:11`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/layout/LazyLayoutPinnableItemKt.java:16`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/layout/LazyLayoutPinnedItemList.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/layout/LazyLayoutPrefetcher.java:10`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/layout/LazyLayoutPrefetchState.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/layout/LazyLayoutSemanticState.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/layout/Lazy_androidKt.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/layout/MutableIntervalList.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/layout/NearestRangeKeyIndexMap.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridAnimateScrollScope.java:9`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridDslKt$items$2$1.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridDslKt$items$4$1.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridDslKt$items$7$1.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridDslKt$items$9$1.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridDslKt$itemsIndexed$2$1.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridDslKt$itemsIndexed$4$1.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridDslKt$itemsIndexed$7$1.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridDslKt$itemsIndexed$9$1.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridDslKt.java:16`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridInterval.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridIntervalContent.java:10`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridItemInfo.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridItemProviderImpl.java:12`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridLaneInfo.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridMeasuredItem.java:12`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridMeasureProvider.java:9`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridScope.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridScrollPosition.java:10`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/lazy/staggeredgrid/LazyStaggeredGridState.java:30`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/pager/LazyLayoutPagerKt.java:14`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/pager/MeasuredPage.java:11`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/compose/foundation/pager/PageInfo.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`

## BR042

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `resources/AndroidManifest.xml:128`
  `<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>`
- `resources/AndroidManifest.xml:132`
  `<uses-permission android:name="android.permission.ACCESS_ADSERVICES_AD_ID"/>`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:27`
  `public class AdvertisingIdClient {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:91`
  `Preconditions.checkNotNull(advertisingIdClient.zza);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:92`
  `Preconditions.checkNotNull(advertisingIdClient.zzb);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:93`
  `zZzd = advertisingIdClient.zzb.zzd();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:95`
  `synchronized (advertisingIdClient.zzd) {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:96`
  `zzb zzbVar = advertisingIdClient.zze;`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:98`
  `throw new IOException("AdvertisingIdClient is not connected.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:102`
  `advertisingIdClient.zzb(false);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:103`
  `if (!advertisingIdClient.zzc) {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:104`
  `throw new IOException("AdvertisingIdClient cannot reconnect.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:106`
  `Preconditions.checkNotNull(advertisingIdClient.zza);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:107`
  `Preconditions.checkNotNull(advertisingIdClient.zzb);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:109`
  `zZzd = advertisingIdClient.zzb.zzd();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:111`
  `Log.i("AdvertisingIdClient", "GMS remote exception ", e);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:115`
  `throw new IOException("AdvertisingIdClient cannot reconnect.", e2);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:119`
  `advertisingIdClient.zze();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:122`
  `advertisingIdClient.zza();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:141`
  `throw new IOException("AdvertisingIdClient is not connected.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:147`
  `throw new IOException("AdvertisingIdClient cannot reconnect.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:154`
  `Log.i("AdvertisingIdClient", "GMS remote exception ", e);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:158`
  `throw new IOException("AdvertisingIdClient cannot reconnect.", e2);`
- `sources/com/google/android/gms/ads/identifier/zza.java:11`
  `zza(AdvertisingIdClient advertisingIdClient, Map map) {`
- `sources/com/google/android/gms/ads/identifier/zzb.java:12`
  `private final WeakReference<AdvertisingIdClient> zzc;`
- `sources/com/google/android/gms/ads/identifier/zzb.java:15`
  `public zzb(AdvertisingIdClient advertisingIdClient, long j) {`
- `sources/com/google/android/gms/ads/identifier/zzb.java:16`
  `this.zzc = new WeakReference<>(advertisingIdClient);`
- `sources/com/google/android/gms/ads/identifier/zzb.java:22`
  `AdvertisingIdClient advertisingIdClient = this.zzc.get();`
- `sources/com/google/android/gms/ads/identifier/zzb.java:23`
  `if (advertisingIdClient != null) {`
- `sources/com/google/android/gms/ads/identifier/zzb.java:24`
  `advertisingIdClient.zza();`
- `sources/com/google/android/gms/internal/measurement/zzni.java:345`
  `zza = zzhrVarZza.zza("measurement.ad_id_cache_time", AbstractComponentTracker.LINGERING_TIMEOUT);`
- `sources/com/google/android/gms/internal/measurement/zzni.java:346`
  `zzb = zzhrVarZza.zza("measurement.app_uninstalled_additional_ad_id_cache_time", 3600000L);`
- `sources/com/google/android/gms/internal/measurement/zzof.java:11`
  `zzhrVarZza.zza("measurement.client.ad_id_consent_fix", true);`
- `sources/com/google/android/gms/measurement/internal/zzal.java:33`
  `private static final String[] zzc = {"app_version", "ALTER TABLE apps ADD COLUMN app_version TEXT;", "app_store", "ALTER TABLE apps ADD COLUMN app_store TEXT;", "gmp_version", "ALTER TABLE apps ADD COLUMN gmp_version INTEGER;", "dev_cert_hash", "ALTER TABLE apps ADD COLUMN dev_cert_hash INTEGER;", "...`
- `sources/com/google/android/gms/measurement/internal/zzbh.java:184`
  `zza = zzb("measurement.ad_id_cache_time", lValueOf, new zzfx() { // from class: com.google.android.gms.measurement.internal.zzbj`
- `sources/com/google/android/gms/measurement/internal/zzbh.java:190`
  `zzb = zzb("measurement.app_uninstalled_additional_ad_id_cache_time", 3600000L, new zzfx() { // from class: com.google.android.gms.measurement.internal.zzcz`
- `sources/com/google/android/gms/measurement/internal/zzha.java:9`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/measurement/internal/zzha.java:81`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(true);`
- `sources/com/google/android/gms/measurement/internal/zzha.java:83`
  `AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(zza());`
- `sources/com/google/android/gms/measurement/internal/zzha.java:94`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(false);`
- `sources/com/google/android/gms/measurement/internal/zzmw.java:6`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/measurement/internal/zzmw.java:41`
  `AdvertisingIdClient.Info advertisingIdInfo;`
- `sources/com/google/android/gms/measurement/internal/zzmw.java:48`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(true);`
- `sources/com/google/android/gms/measurement/internal/zzmw.java:52`
  `advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(zza());`
- `sources/com/google/android/gms/measurement/internal/zzmw.java:69`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(false);`
- `sources/com/google/mlkit/common/sdkinternal/model/zzc.java:32`
  `long longExtra = intent.getLongExtra("extra_download_id", -1L);`

## BR043

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/com/bruhealth/glucometer/GlucometerNativeUtils.java:136`
  `public final boolean startScan(Context context, Map<String, ? extends Object> params) {`
- `sources/com/inuker/bluetooth/library/search/le/BluetoothLESearcher.java:39`
  `this.mBluetoothAdapter.startLeScan(this.mLeScanCallback);`
- `sources/egnc/moh/bruhealth/channel/GlucometerBridge.java:197`
  `result.success(Boolean.valueOf(companion.startScan(app, params)));`

## BR044

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/androidx/core/content/ContextCompat.java:43`
  `import android.net.wifi.WifiManager;`
- `sources/androidx/core/content/ContextCompat.java:362`
  `map.put(WifiManager.class, "wifi");`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:7`
  `import android.net.wifi.WifiManager;`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:71`
  `WifiManager wifiManager = (WifiManager) Utils.getApp().getSystemService("wifi");`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:72`
  `if (wifiManager == null) {`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:75`
  `return wifiManager.isWifiEnabled();`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:79`
  `WifiManager wifiManager = (WifiManager) Utils.getApp().getSystemService("wifi");`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:80`
  `if (wifiManager == null || z == wifiManager.isWifiEnabled()) {`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:83`
  `wifiManager.setWifiEnabled(z);`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:120`
  `WifiManager wifiManager = (WifiManager) Utils.getApp().getApplicationContext().getSystemService("wifi");`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:121`
  `if (wifiManager != null && (connectionInfo = wifiManager.getConnectionInfo()) != null) {`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:10`
  `import android.net.wifi.WifiManager;`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:175`
  `WifiManager wifiManager = (WifiManager) Utils.getApp().getSystemService("wifi");`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:176`
  `if (wifiManager == null) {`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:179`
  `return wifiManager.isWifiEnabled();`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:183`
  `WifiManager wifiManager = (WifiManager) Utils.getApp().getSystemService("wifi");`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:184`
  `if (wifiManager == null || z == wifiManager.isWifiEnabled()) {`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:187`
  `wifiManager.setWifiEnabled(z);`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:381`
  `WifiManager wifiManager = (WifiManager) Utils.getApp().getSystemService("wifi");`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:382`
  `if (wifiManager == null) {`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:385`
  `return Formatter.formatIpAddress(wifiManager.getDhcpInfo().ipAddress);`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:389`
  `WifiManager wifiManager = (WifiManager) Utils.getApp().getSystemService("wifi");`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:390`
  `if (wifiManager == null) {`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:393`
  `return Formatter.formatIpAddress(wifiManager.getDhcpInfo().gateway);`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:397`
  `WifiManager wifiManager = (WifiManager) Utils.getApp().getSystemService("wifi");`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:398`
  `if (wifiManager == null) {`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:401`
  `return Formatter.formatIpAddress(wifiManager.getDhcpInfo().netmask);`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:405`
  `WifiManager wifiManager = (WifiManager) Utils.getApp().getSystemService("wifi");`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:406`
  `if (wifiManager == null) {`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:409`
  `return Formatter.formatIpAddress(wifiManager.getDhcpInfo().serverAddress);`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:414`
  `WifiManager wifiManager = (WifiManager) Utils.getApp().getApplicationContext().getSystemService("wifi");`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:415`
  `if (wifiManager == null || (connectionInfo = wifiManager.getConnectionInfo()) == null) {`
- `sources/com/google/android/exoplayer2/WifiLockManager.java:4`
  `import android.net.wifi.WifiManager;`
- `sources/com/google/android/exoplayer2/WifiLockManager.java:13`
  `private WifiManager.WifiLock wifiLock;`
- `sources/com/google/android/exoplayer2/WifiLockManager.java:14`
  `private final WifiManager wifiManager;`
- `sources/com/google/android/exoplayer2/WifiLockManager.java:17`
  `this.wifiManager = (WifiManager) context.getApplicationContext().getSystemService("wifi");`
- `sources/com/google/android/exoplayer2/WifiLockManager.java:22`
  `WifiManager wifiManager = this.wifiManager;`
- `sources/com/google/android/exoplayer2/WifiLockManager.java:23`
  `if (wifiManager == null) {`
- `sources/com/google/android/exoplayer2/WifiLockManager.java:24`
  `Log.w(TAG, "WifiManager is null, therefore not creating the WifiLock.");`
- `sources/com/google/android/exoplayer2/WifiLockManager.java:27`
  `WifiManager.WifiLock wifiLockCreateWifiLock = wifiManager.createWifiLock(3, WIFI_LOCK_TAG);`
- `sources/com/google/android/exoplayer2/WifiLockManager.java:42`
  `WifiManager.WifiLock wifiLock = this.wifiLock;`
- `sources/com/google/zxing/client/android/result/WifiResultHandler.java:4`
  `import android.net.wifi.WifiManager;`
- `sources/com/google/zxing/client/android/result/WifiResultHandler.java:39`
  `WifiManager wifiManager = (WifiManager) getActivity().getSystemService("wifi");`
- `sources/com/google/zxing/client/android/result/WifiResultHandler.java:40`
  `if (wifiManager == null) {`
- `sources/com/google/zxing/client/android/result/WifiResultHandler.java:41`
  `Log.w(TAG, "No WifiManager available from device");`
- `sources/com/google/zxing/client/android/result/WifiResultHandler.java:51`
  `new WifiConfigManager(wifiManager).executeOnExecutor(AsyncTask.THREAD_POOL_EXECUTOR, wifiParsedResult);`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:4`
  `import android.net.wifi.WifiManager;`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:15`
  `private final WifiManager wifiManager;`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:17`
  `public WifiConfigManager(WifiManager wifiManager) {`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:18`
  `this.wifiManager = wifiManager;`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:26`
  `if (!this.wifiManager.isWifiEnabled()) {`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:29`
  `if (this.wifiManager.setWifiEnabled(true)) {`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:31`
  `while (!this.wifiManager.isWifiEnabled()) {`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:52`
  `changeNetworkUnEncrypted(this.wifiManager, wifiParsedResult);`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:57`
  `changeNetworkWEP(this.wifiManager, wifiParsedResult);`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:59`
  `changeNetworkWPA(this.wifiManager, wifiParsedResult);`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:70`
  `private static void updateNetwork(WifiManager wifiManager, WifiConfiguration wifiConfiguration) {`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:71`
  `Integer numFindNetworkInExistingConfig = findNetworkInExistingConfig(wifiManager, wifiConfiguration.SSID);`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:74`
  `wifiManager.removeNetwork(numFindNetworkInExistingConfig.intValue());`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:75`
  `wifiManager.saveConfiguration();`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:77`
  `int iAddNetwork = wifiManager.addNetwork(wifiConfiguration);`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:79`
  `if (wifiManager.enableNetwork(iAddNetwork, true)) {`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:81`
  `wifiManager.saveConfiguration();`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:102`
  `private static void changeNetworkWEP(WifiManager wifiManager, WifiParsedResult wifiParsedResult) {`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:112`
  `updateNetwork(wifiManager, wifiConfigurationChangeNetworkCommon);`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:115`
  `private static void changeNetworkWPA(WifiManager wifiManager, WifiParsedResult wifiParsedResult) {`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:127`
  `updateNetwork(wifiManager, wifiConfigurationChangeNetworkCommon);`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:130`
  `private static void changeNetworkUnEncrypted(WifiManager wifiManager, WifiParsedResult wifiParsedResult) {`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:133`
  `updateNetwork(wifiManager, wifiConfigurationChangeNetworkCommon);`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:136`
  `private static Integer findNetworkInExistingConfig(WifiManager wifiManager, String str) {`
- `sources/com/google/zxing/client/android/wifi/WifiConfigManager.java:137`
  `List<WifiConfiguration> configuredNetworks = wifiManager.getConfiguredNetworks();`
- `sources/com/tencent/liteav/base/system/LiteavSystemInfo.java:6`
  `import android.net.wifi.WifiManager;`
- `sources/com/tencent/liteav/base/system/LiteavSystemInfo.java:271`
  `return ((WifiManager) applicationContext.getSystemService("wifi")).getDhcpInfo().gateway;`

## BR047

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/android/support/v4/media/MediaBrowserCompat.java:657`
  `Log.d(MediaBrowserCompat.TAG, "addSubscription failed with RemoteException parentId=" + parentId);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:751`
  `Log.i(MediaBrowserCompat.TAG, "Remote error sending a custom action: action=" + action + ", extras=" + extras, e);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:767`
  `Log.w(MediaBrowserCompat.TAG, "onConnect from service while mState=" + getStateLabel(this.mState) + "... ignoring");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:889`
  `Log.d(MediaBrowserCompat.TAG, "  mServiceBinderWrapper=" + this.mServiceBinderWrapper);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:890`
  `Log.d(MediaBrowserCompat.TAG, "  mCallbacksMessenger=" + this.mCallbacksMessenger);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:891`
  `Log.d(MediaBrowserCompat.TAG, "  mRootId=" + this.mRootId);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:892`
  `Log.d(MediaBrowserCompat.TAG, "  mMediaSessionToken=" + this.mMediaSessionToken);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1071`
  `Log.i(MediaBrowserCompat.TAG, "Remote error subscribing media item: " + parentId);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1194`
  `Log.i(MediaBrowserCompat.TAG, "The connected service doesn't support sendCustomAction.");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1207`
  `Log.i(MediaBrowserCompat.TAG, "Remote error sending a custom action: action=" + action + ", extras=" + extras, e);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1244`
  `Log.e(MediaBrowserCompat.TAG, "Unexpected IllegalStateException", e);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1404`
  `Log.w(MediaBrowserCompat.TAG, "Unhandled message: " + msg + "\n  Client version: 1\n  Service version: " + msg.arg1);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1598`
  `Log.w(MediaBrowserCompat.TAG, "Unknown result code: " + resultCode + " (extras=" + this.mExtras + ", resultData=" + resultData + SqlExpression.SqlEnclosureClosingBrace);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1186`
  `Log.e(MediaControllerCompat.TAG, "Dead object in setRating.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1240`
  `Log.e(MediaControllerCompat.TAG, "Dead object in sendCustomAction.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1273`
  `Log.e(MediaControllerCompat.TAG, "Dead object in registerCallback.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1294`
  `Log.e(MediaControllerCompat.TAG, "Dead object in unregisterCallback.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1327`
  `Log.e(MediaControllerCompat.TAG, "Dead object in getPlaybackState.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1409`
  `Log.e(MediaControllerCompat.TAG, "Dead object in isCaptioningEnabled.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1422`
  `Log.e(MediaControllerCompat.TAG, "Dead object in getRepeatMode.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1435`
  `Log.e(MediaControllerCompat.TAG, "Dead object in getShuffleMode.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1493`
  `Log.e(MediaControllerCompat.TAG, "Dead object in getSessionInfo.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1523`
  `Log.e(MediaControllerCompat.TAG, "Dead object in registerCallback.", e);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:310`
  `Log.e(TAG, "Found duplicate queue id: " + queueItem.getQueueId(), new IllegalArgumentException("id of each queue item should be unique"));`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:880`
  `Log.e(MediaSessionCompat.TAG, "Could not unparcel the data.");`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:2649`
  `Log.w(MediaSessionCompat.TAG, "Exception happened while accessing MediaSession.mCallback.", e);`
- `sources/androidx/activity/result/ActivityResultRegistry.java:148`
  `Log.w(LOG_TAG, "Dropping pending result for request " + str + ": " + this.mParsedPendingResults.get(str));`
- `sources/androidx/activity/result/ActivityResultRegistry.java:152`
  `Log.w(LOG_TAG, "Dropping pending result for request " + str + ": " + this.mPendingResults.getParcelable(str));`
- `sources/androidx/appcompat/app/ActionBarDrawerToggle.java:217`
  `Log.w("ActionBarDrawerToggle", "DrawerToggle may not show up because NavigationIcon is not visible. You may need to call actionbar.setDisplayHomeAsUpEnabled(true);");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1263`
  `Log.i("AppCompatDelegate", "Failed to instantiate custom view inflater " + string + ". Falling back to default.", th);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1314`
  `Log.i("AppCompatDelegate", "The Activity's LayoutInflater already has a Factory installed so we can not install AppCompat's");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1844`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1850`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR_OVERLAY id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2225`
  `Log.d("AppCompatDelegate", "Exception while getting ActivityInfo", e);`
- `sources/androidx/appcompat/app/ResourcesFlusher.java:170`
  `Log.e(TAG, "Could not retrieve value from ThemedResourceCache#mUnthemedEntries", e3);`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:286`
  `Log.w(SupportMenuInflater.LOG_TAG, "Ignoring attribute 'actionProviderClass'. Action view already specified.");`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:343`
  `Log.w(SupportMenuInflater.LOG_TAG, "Ignoring attribute 'itemActionViewLayout'. Action view already specified.");`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:386`
  `Log.w(SupportMenuInflater.LOG_TAG, "Cannot instantiate class: " + str, e);`
- `sources/androidx/appcompat/view/menu/MenuItemImpl.java:100`
  `Log.e(TAG, "Can't find activity to handle intent; ignoring", e);`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:355`
  `Log.w(TAG, "Failed to invoke TextView#nullLayouts() method", e);`

## BR050

paper_id: B021
paper_title: Metadata-Based Privacy Assessment for Mobile mHealth

- `resources/assets/flutter_assets/AssetManifest.json:1`
  `{"config/country.json":["config/country.json"],"config/floor/explore_floor_config.json":["config/floor/explore_floor_config.json"],"config/floor/explore_floor_config_v2.json":["config/floor/explore_floor_config_v2.json"],"config/floor/home_floor_config.json":["config/floor/home_floor_config.json"],"...`
- `resources/assets/flutter_assets/config/language/en.json:83`
  `"login_agree_policy": "Please agree to our User Agreement and Privacy Policy first.",`
- `resources/assets/html/bruhealth_disclaimer.html:158`
  `The service is provided by NetEase Easy Shield, which will collect, use and protect your personal information in accordance with the NetEase Easy Shield Privacy Policy (https://dun.163.com/clause/privacy/en). The information will be protected using secure processing methods such as encrypted transmi...`
- `resources/assets/html/bruhealth_privacy_policy.html:2`
  `<!-- saved from url=(0072)https://www.healthapp.gov.bn/covid19/bruhealth/privacy_policy_2.0.0.html -->`
- `resources/assets/html/bruhealth_privacy_policy.html:18`
  `<title>Privacy Policy</title>`
- `resources/assets/html/bruhealth_privacy_policy.html:309`
  `accordance with the <a href="https://dun.163.com/clause/privacy/en">NetEase Easy Shield Privacy`
- `resources/assets/html/bruhealth_privacy_policy.html:310`
  `Policy</a>. The information will be protected using secure processing methods such as encrypted`
- `resources/assets/html/bruhealth_terms_of_use.html:2`
  `<!-- saved from url=(0072)https://www.healthapp.gov.bn/covid19/bruhealth/privacy_policy_2.0.0.html -->`
- `resources/assets/html/bruhealth_terms_of_use.html:296`
  `to conflict of law provisions. The Operator may assign or delegate this TOU and/or the Operator’s Privacy`
- `resources/assets/html/bruhealth_terms_of_use.html:305`
  `THESE TERMS OF USE, TOGETHER WITH THE PRIVACY POLICY, REPRESENT THE COMPLETE AND EXCLUSIVE STATEMENT OF THE`
- `resources/assets/www/index.html:1`
  `<!DOCTYPE html><html lang=en><head><meta charset=utf-8><meta http-equiv=X-UA-Compatible content="IE=edge"><meta name=viewport content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=0,viewport-fit=cover"><meta http-equiv=Content-Security-Policy content="default-src 'self' data: gap...`
- `resources/res/drawable/selector_policy.xml:5`
  `android:drawable="@mipmap/policy_checked"/>`
- `resources/res/drawable/selector_policy_dialog.xml:5`
  `android:drawable="@mipmap/privacy_selected"/>`
- `resources/res/values/strings.xml:37`
  `<string name="agree_policy">Please agree to our User Agreement and Privacy Policy first.</string>`
- `resources/res/values-en/strings.xml:9`
  `<string name="agree_policy">Please agree to our User Agreement and Privacy Policy first.</string>`

## BR051

paper_id: B013
paper_title: Availability and quality of mobile health app privacy policies

- `BRUHEALTH_AUDIT_REPORT.md:642`
  `- B005 / mHealth privacy`
- `BRUHEALTH_AUDIT_REPORT.md:647`
  `- B019 / pulse oximeter privacy`
- `BRUHEALTH_SOURCE_PAPER_REVIEW.md:186`
  `- 但论文方法本身提示：第三方共享需要 traffic 和 policy 对照，不能只靠 SDK 包名确认。`
- `resources/assets/html/bruhealth_privacy_policy.html:302`
  `adhere to the Health Connect Permissions Policy, including the Limited User Requirements.</p>`
- `resources/assets/html/bruhealth_privacy_policy.html:309`
  `accordance with the <a href="https://dun.163.com/clause/privacy/en">NetEase Easy Shield Privacy`
- `resources/assets/html/bruhealth_privacy_policy.html:310`
  `Policy</a>. The information will be protected using secure processing methods such as encrypted`
- `resources/assets/html/bruhealth_privacy_policy.html:422`
  `practices by going to www.google.com/policies/privacy/partners/. </p>`
- `resources/assets/html/bruhealth_terms_of_use.html:137`
  `proprietary rights, including privacy, publicity, etc., unless you are the owner of such rights or have the`
- `resources/assets/html/bruhealth_terms_of_use.html:207`
  `offensiveness, opinions, reliability, privacy practices or other policies of or contained in the Third`
- `resources/assets/html-en/license.html:25`
  `separate from and not affiliated with this application, and are not covered by this Privacy Policy.</p>`
- `resources/res/values/public.xml:5079`
  `<public type="mipmap" name="privacy_unselected" id="0x7f100059" />`

## BR052

paper_id: B013
paper_title: Availability and quality of mobile health app privacy policies

- `BRUHEALTH_AUDIT_REPORT.md:122`
  `- B005 'Mobile health and privacy: cross sectional study'`
- `BRUHEALTH_AUDIT_REPORT.md:124`
  `- B016 'Privacy and Security Analysis of COVID-19 Contact Tracing Android Apps'`
- `BRUHEALTH_AUDIT_REPORT.md:342`
  `- BR025 / B005 / 'Mobile health and privacy: cross sectional study'`
- `BRUHEALTH_AUDIT_REPORT.md:380`
  `- BR026 / B002 / 'Unaddressed privacy risks in accredited health and wellness apps'`
- `BRUHEALTH_AUDIT_REPORT.md:488`
  `- BR097 / B019 / Pulse Oximeter App Privacy，关注健康测量数据隐私。`
- `BRUHEALTH_AUDIT_REPORT.md:642`
  `- B005 / mHealth privacy`
- `BRUHEALTH_AUDIT_REPORT.md:647`
  `- B019 / pulse oximeter privacy`
- `BRUHEALTH_SOURCE_PAPER_REVIEW.md:172`
  `论文：'B005-mobile-health-privacy.html'`
- `BRUHEALTH_SOURCE_PAPER_REVIEW.md:176`
  `- 'C:\wujiangliang\app\xiangshan\database_beginner\snapshots\B005-mobile-health-privacy.html'`
- `BRUHEALTH_SOURCE_PAPER_REVIEW.md:186`
  `- 但论文方法本身提示：第三方共享需要 traffic 和 policy 对照，不能只靠 SDK 包名确认。`
- `resources/AndroidManifest.xml:303`
  `android:name="egnc.moh.bruhealth.nativeLib.activities.PrivacyUserActivity"`
- `resources/AndroidManifest.xml:315`
  `android:name="egnc.moh.bruhealth.nativeLib.activities.PwdPolicyActivity"`
- `resources/assets/flutter_assets/AssetManifest.json:1`
  `{"config/country.json":["config/country.json"],"config/floor/explore_floor_config.json":["config/floor/explore_floor_config.json"],"config/floor/explore_floor_config_v2.json":["config/floor/explore_floor_config_v2.json"],"config/floor/home_floor_config.json":["config/floor/home_floor_config.json"],"...`
- `resources/assets/flutter_assets/config/language/en.json:104`
  `"login_privacy": "I have carefully read and agreed to BruHealth Terms of Use and Privacy Policy",`
- `resources/assets/flutter_assets/config/language/en.json:105`
  `"login_privacy_policy": "Privacy Policy",`
- `resources/assets/flutter_assets/config/language/ms.json:80`
  `"login_agree_policy": "Sila bersetuju dengan Syarat Penggunaan dan Dasar Privasi BruHealth",`
- `resources/assets/flutter_assets/config/language/ms.json:101`
  `"login_privacy": "Saya telah membaca dan bersetuju dengan Syarat Penggunaan dan Polisi Privasi BruHealth",`
- `resources/assets/flutter_assets/config/language/ms.json:102`
  `"login_privacy_policy": "Polisi Privasi",`
- `resources/assets/html/bruhealth_disclaimer.html:121`
  `Thank you for your trust in BruHealth. Before you activate this app, please read our Terms of Use and Privacy Policy carefully. After reading the same, by hitting the “I Agree” button, you signify to us that you agree to the Terms of Use and Privacy Policy. We will provide services to you in accorda...`
- `resources/assets/html/bruhealth_disclaimer.html:158`
  `The service is provided by NetEase Easy Shield, which will collect, use and protect your personal information in accordance with the NetEase Easy Shield Privacy Policy (https://dun.163.com/clause/privacy/en). The information will be protected using secure processing methods such as encrypted transmi...`
- `resources/assets/html/bruhealth_disclaimer.html:174`
  `<div class="link" id="privacy">`
- `resources/assets/html/bruhealth_disclaimer.html:186`
  `var privacyBtn = document.getElementById('privacy');`
- `resources/assets/html/bruhealth_disclaimer.html:187`
  `privacyBtn.addEventListener("click", function () {`
- `resources/assets/html/bruhealth_disclaimer.html:188`
  `window.flutter_inappwebview._callHandler("show_privacy_policy","2222","");`
- `resources/assets/html/bruhealth_privacy_policy.html:2`
  `<!-- saved from url=(0072)https://www.healthapp.gov.bn/covid19/bruhealth/privacy_policy_2.0.0.html -->`
- `resources/assets/html/bruhealth_privacy_policy.html:18`
  `<title>Privacy Policy</title>`
- `resources/assets/html/bruhealth_privacy_policy.html:69`
  `<div data-v-98e77254="" class="section-title">Privacy Statement</div>`
- `resources/assets/html/bruhealth_privacy_policy.html:71`
  `<p data-v-98e77254="">The privacy and security of your information is very important to us. Whether you are`
- `resources/assets/html/bruhealth_privacy_policy.html:75`
  `<p data-v-98e77254="">We have prepared this Privacy Statement to explain more about who we are and how we`
- `resources/assets/html/bruhealth_privacy_policy.html:81`
  `<div data-v-98e77254="" class="section-content">This Privacy Statement is issued by The Ministry of Health of`
- `resources/assets/html/bruhealth_privacy_policy.html:83`
  `operator of the APP (collectively referred to as “Operator”, “we”, “us”, or “our” in this Privacy`
- `resources/assets/html/bruhealth_privacy_policy.html:280`
  `track compliance with policy measures. </p>`
- `resources/assets/html/bruhealth_privacy_policy.html:302`
  `adhere to the Health Connect Permissions Policy, including the Limited User Requirements.</p>`
- `resources/assets/html/bruhealth_privacy_policy.html:374`
  `that have been provided to third parties in connection with the services discussed in this Privacy`
- `resources/assets/html/bruhealth_privacy_policy.html:383`
  `online video consultation and public health management discussed in this Privacy Statement.</div>`
- `resources/assets/html/bruhealth_privacy_policy.html:422`
  `practices by going to www.google.com/policies/privacy/partners/. </p>`
- `resources/assets/html/bruhealth_privacy_policy.html:456`
  `or permitted in light of the purpose(s) for which it was obtained and as outlined in this Privacy Policy.`
- `resources/assets/html/bruhealth_privacy_policy.html:465`
  `<p data-v-98e77254="">For any questions or concerns regarding this Privacy Statement or our data privacy`
- `resources/assets/html/bruhealth_privacy_policy.html:473`
  `<div data-v-98e77254="" class="section-title">Changes to this Privacy Policy</div>`
- `resources/assets/html/bruhealth_privacy_policy.html:475`
  `Privacy Policy in order to comply with the evolving regulatory environment or the needs of our public health`
- `resources/assets/html/bruhealth_privacy_policy.html:477`
  `Privacy Policy will be communicated through the APP. However, if there will be changes made to the use of`
- `resources/assets/html/bruhealth_terms_of_use.html:2`
  `<!-- saved from url=(0072)https://www.healthapp.gov.bn/covid19/bruhealth/privacy_policy_2.0.0.html -->`
- `resources/assets/html/bruhealth_terms_of_use.html:137`
  `proprietary rights, including privacy, publicity, etc., unless you are the owner of such rights or have the`
- `resources/assets/html/bruhealth_terms_of_use.html:244`
  `your personal information is collected and used, please refer to the Privacy Policy of the APP.</div>`
- `resources/assets/html-en/license.html:10`
  `<h3>Privacy Policy</h3>`
- `resources/assets/html-nl/license.html:10`
  `<h3> Privacybeleid </h3>`
- `resources/assets/html-nl/license.html:16`
  `<p> Merk ook op dat deze applicatie links naar derden websites en applicaties. Weer geen uitzondering zoektermen informatie wordt doorgegeven als deel van deze verbindingen. Deze sites en applicaties staan los van en niet verbonden met deze toepassing, en vallen niet onder dit privacybeleid. </p>`
- `resources/assets/www/index.html:1`
  `<!DOCTYPE html><html lang=en><head><meta charset=utf-8><meta http-equiv=X-UA-Compatible content="IE=edge"><meta name=viewport content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=0,viewport-fit=cover"><meta http-equiv=Content-Security-Policy content="default-src 'self' data: gap...`
- `resources/res/values/public.xml:4789`
  `<public type="layout" name="dialog_password_policy" id="0x7f0d005f" />`
- `resources/res/values/public.xml:4831`
  `<public type="layout" name="item_policy_switch_member" id="0x7f0d0089" />`
- `resources/res/values/strings.xml:37`
  `<string name="agree_policy">Please agree to our User Agreement and Privacy Policy first.</string>`
- `resources/res/values/strings.xml:44`
  `<string name="app_policy">I have read and agreed to Terms of Use and Privacy Policy.</string>`
- `resources/res/values/strings.xml:678`
  `<string name="privacy_policy">Privacy Policy</string>`
- `resources/res/values/strings.xml:679`
  `<string name="privacy_policy_dialog">Privacy Policy</string>`
- `resources/res/values-en/strings.xml:9`
  `<string name="agree_policy">Please agree to our User Agreement and Privacy Policy first.</string>`
- `resources/res/values-en/strings.xml:14`
  `<string name="app_policy">I have read and agreed to BruHealth Terms of Use and Privacy Policy.</string>`
- `resources/res/values-en/strings.xml:275`
  `<string name="privacy_policy">Privacy Policy</string>`
- `resources/res/values-en/strings.xml:276`
  `<string name="privacy_policy_dialog">Privacy Policy</string>`
- `resources/res/values-ms/strings.xml:36`
  `<string name="agree_policy">Sila setuju dengan Perjanjian Pengguna dan Polisi Privasi kami terlebih dahulu.</string>`
- `resources/res/values-ms/strings.xml:41`
  `<string name="app_policy">Saya telah membaca dan bersetuju dengan Syarat Penggunaan dan Polisi Privasi BruHealth.</string>`
- `resources/res/values-ms/strings.xml:481`
  `<string name="privacy_policy">Polisi Privasi</string>`
- `resources/res/values-ms/strings.xml:482`
  `<string name="privacy_policy_dialog">Polisi Privasi</string>`

## BR055

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `sources/androidx/core/util/PatternsCompat.java:16`
  `static final String IANA_TOP_LEVEL_DOMAINS = "(?:(?:aaa|aarp|abb|abbott|abbvie|abc|able|abogado|abudhabi|academy|accenture|accountant|accountants|aco|actor|ads|adult|aeg|aero|aetna|afl|africa|agakhan|agency|aig|airbus|airforce|airtel|akdn|alibaba|alipay|allfinanz|allstate|ally|alsace|alstom|amazon|a...`
- `sources/androidx/core/util/PatternsCompat.java:26`
  `private static final String STRICT_HOST_NAME = "(?:(?:[a-zA-Z0-9[ -\ud7ff豈-﷏ﷰ-\uffef𐀀-\u1fffd𠀀-\u2fffd𰀀-\u3fffd\u40000-\u4fffd\u50000-\u5fffd\u60000-\u6fffd\u70000-\u7fffd\u80000-\u8fffd\u90000-\u9fffd\ua0000-\uafffd\ub0000-\ubfffd\uc0000-\ucfffd\ud0000-\udfffd\ue1000-\uefffd&&[^ [\u2000-\u200a]\u20...`
- `sources/androidx/core/util/PatternsCompat.java:27`
  `private static final String STRICT_TLD = "(?:(?:(?:aaa|aarp|abb|abbott|abbvie|abc|able|abogado|abudhabi|academy|accenture|accountant|accountants|aco|actor|ads|adult|aeg|aero|aetna|afl|africa|agakhan|agency|aig|airbus|airforce|airtel|akdn|alibaba|alipay|allfinanz|allstate|ally|alsace|alstom|amazon|am...`
- `sources/androidx/core/util/PatternsCompat.java:43`
  `Pattern patternCompile3 = Pattern.compile("(?:(?:(?:[a-zA-Z0-9[ -\ud7ff豈-﷏ﷰ-\uffef𐀀-\u1fffd𠀀-\u2fffd𰀀-\u3fffd\u40000-\u4fffd\u50000-\u5fffd\u60000-\u6fffd\u70000-\u7fffd\u80000-\u8fffd\u90000-\u9fffd\ua0000-\uafffd\ub0000-\ubfffd\uc0000-\ucfffd\ud0000-\udfffd\ue1000-\uefffd&&[^ [\u2000-\u200a]\u2028...`

## BR058

paper_id: B022
paper_title: A Study of Android Application Security

- `BRUHEALTH_EVIDENCE_CHAINS.md:633`
  `- provider 均未见 first-party exported=true + 无权限的敏感 ContentProvider。`
- `BRUHEALTH_EVIDENCE_CHAINS.md:665`
  `## Chain 12: Third-party / supplier code boundary`
- `BRUHEALTH_EVIDENCE_CHAINS.md:697`
  `- 反编译源目录和 Manifest 证据足以建立 third-party library inventory。`
- `BRUHEALTH_SOURCE_PAPER_REVIEW.md:564`
  `- 不能把所有 exported third-party/library 组件统一写成漏洞。`
- `BRUHEALTH_SOURCE_PAPER_REVIEW.md:616`
  `- B001 说明 third-party servers 是 mHealth 重要风险面。`
- `resources/assets/html/apache-license.txt:115`
  `wherever such third-party notices normally appear. The contents`
- `resources/assets/html/apache-license.txt:187`
  `identification within third-party archives.`

## BR059

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/AndroidManifest.xml:213`
  `<intent-filter>`
- `resources/AndroidManifest.xml:375`
  `<intent-filter>`

## BR060

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `sources/com/google/android/exoplayer2/upstream/cache/CachedContentIndex.java:210`
  `return Cipher.getInstance("AES/CBC/PKCS5PADDING", "BC");`
- `sources/com/google/android/exoplayer2/upstream/cache/CachedContentIndex.java:214`
  `return Cipher.getInstance("AES/CBC/PKCS5PADDING");`
- `sources/com/netease/nis/basesdk/EncryptUtil.java:19`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/netease/nis/basesdk/EncryptUtil.java:26`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/netease/nis/basesdk/EncryptUtil.java:34`
  `Cipher cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding");`
- `sources/com/tencent/liteav/sdk/common/LicenseCheckerPlatformAndroid.java:22`
  `private static final String ALGORITHM_AES_CBC_PKCS5PADDING = "AES/CBC/PKCS5Padding";`
- `sources/egnc/moh/base/utils/FieldEncryption.java:11`
  `return Base64.encodeToString(EncryptUtils.encryptRSA(field.getBytes("utf-8"), Base64.decode(Constants.PUBLIC_KEY, 2), 1024, "RSA/ECB/PKCS1Padding"), 2);`
- `sources/egnc/moh/bruhealth/login/activities/PasswordEnterActivity.java:476`
  `linkedHashMap.put("oldPwd", Base64.encodeToString(EncryptUtils.encryptRSA(bytes, Base64.decode(Constants.PUBLIC_KEY, 2), 1024, "RSA/ECB/PKCS1Padding"), 2));`
- `sources/egnc/moh/bruhealth/model/PhoneLogin.java:52`
  `this.loginParams.put("loginParam", Base64.encodeToString(EncryptUtils.encryptRSA(this.param.getBytes("utf-8"), Base64.decode(Constants.PUBLIC_KEY, 2), 1024, "RSA/ECB/PKCS1Padding"), 2));`
- `sources/egnc/moh/bruhealth/nativeLib/utils/EvydEncryptUtil.java:44`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/egnc/moh/bruhealth/nativeLib/utils/EvydEncryptUtil.java:77`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`

## BR061

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/compose/material3/PlainTooltipState.java:26`
  `this.isVisible.setValue(Boolean.valueOf(z));`
- `sources/androidx/compose/material3/RichTooltipState.java:38`
  `this.isPersistent.setValue(Boolean.valueOf(z));`
- `sources/androidx/compose/runtime/Recomposer.java:222`
  `recomposer._state.setValue(Recomposer.State.ShuttingDown);`
- `sources/androidx/compose/runtime/Recomposer.java:1134`
  `this._state.setValue(State.ShuttingDown);`
- `sources/androidx/compose/runtime/SnapshotMutableDoubleStateImpl.java:67`
  `((DoubleStateStateRecord) SnapshotKt.overwritableRecord(doubleStateStateRecord2, this, current, doubleStateStateRecord)).setValue(d);`
- `sources/androidx/compose/runtime/SnapshotMutableFloatStateImpl.java:67`
  `((FloatStateStateRecord) SnapshotKt.overwritableRecord(floatStateStateRecord2, this, current, floatStateStateRecord)).setValue(f);`
- `sources/androidx/compose/runtime/SnapshotMutableIntStateImpl.java:68`
  `((IntStateStateRecord) SnapshotKt.overwritableRecord(intStateStateRecord2, this, current, intStateStateRecord)).setValue(i);`
- `sources/androidx/compose/runtime/SnapshotMutableLongStateImpl.java:65`
  `((LongStateStateRecord) SnapshotKt.overwritableRecord(longStateStateRecord2, this, current, longStateStateRecord)).setValue(j);`
- `sources/androidx/compose/runtime/SnapshotMutableStateImpl.java:55`
  `((StateStateRecord) SnapshotKt.overwritableRecord(stateStateRecord2, this, current, stateStateRecord)).setValue(t);`
- `sources/androidx/constraintlayout/core/state/WidgetFrame.java:415`
  `public boolean setValue(String str, CLElement cLElement) throws CLParsingException {`
- `sources/androidx/constraintlayout/motion/widget/KeyAttributes.java:178`
  `public void setValue(String str, Object obj) {`
- `sources/androidx/constraintlayout/motion/widget/KeyCycle.java:340`
  `public void setValue(String str, Object obj) {`
- `sources/androidx/constraintlayout/motion/widget/KeyTimeCycle.java:165`
  `public void setValue(String str, Object obj) {`
- `sources/androidx/core/view/inputmethod/EditorInfoCompat.java:209`
  `static int getProtocol(EditorInfo editorInfo) {`
- `sources/androidx/core/view/inputmethod/InputConnectionCompat.java:143`
  `int protocol = EditorInfoCompat.getProtocol(editorInfo);`
- `sources/androidx/datastore/core/SingleProcessDataStore.java:309`
  `((SingleProcessDataStore) this.this$0).downstreamFlow.setValue(new Final(th));`
- `sources/androidx/datastore/preferences/protobuf/Any.java:54`
  `public void setValue(ByteString byteString) {`
- `sources/androidx/datastore/preferences/protobuf/Any.java:162`
  `public Builder setValue(ByteString byteString) {`
- `sources/androidx/datastore/preferences/protobuf/Any.java:164`
  `((Any) this.instance).setValue(byteString);`
- `sources/androidx/datastore/preferences/protobuf/BytesValue.java:24`
  `public void setValue(ByteString byteString) {`
- `sources/androidx/datastore/preferences/protobuf/BytesValue.java:104`
  `public Builder setValue(ByteString byteString) {`
- `sources/androidx/datastore/preferences/protobuf/BytesValue.java:106`
  `((BytesValue) this.instance).setValue(byteString);`
- `sources/androidx/datastore/preferences/protobuf/BytesValue.java:200`
  `return newBuilder().setValue(byteString).build();`
- `sources/androidx/datastore/preferences/protobuf/LazyFieldLite.java:80`
  `public MessageLite setValue(MessageLite messageLite) {`
- `sources/androidx/datastore/preferences/protobuf/LazyFieldLite.java:106`
  `setValue(mergeValueAndBytes(lazyFieldLite.value, this.delayedBytes, this.extensionRegistry));`
- `sources/androidx/datastore/preferences/protobuf/LazyFieldLite.java:108`
  `setValue(mergeValueAndBytes(this.value, lazyFieldLite.delayedBytes, lazyFieldLite.extensionRegistry));`
- `sources/androidx/datastore/preferences/protobuf/LazyFieldLite.java:110`
  `setValue(this.value.toBuilder().mergeFrom(lazyFieldLite.value).build());`
- `sources/androidx/datastore/preferences/protobuf/LazyFieldLite.java:127`
  `setValue(this.value.toBuilder().mergeFrom(codedInputStream, extensionRegistryLite).build());`
- `sources/androidx/datastore/preferences/protobuf/StringValue.java:29`
  `public void setValue(String str) {`
- `sources/androidx/datastore/preferences/protobuf/StringValue.java:121`
  `public Builder setValue(String str) {`
- `sources/androidx/datastore/preferences/protobuf/StringValue.java:123`
  `((StringValue) this.instance).setValue(str);`
- `sources/androidx/health/platform/client/proto/Any.java:53`
  `public void setValue(ByteString value) {`
- `sources/androidx/health/platform/client/proto/Any.java:161`
  `public Builder setValue(ByteString value) {`
- `sources/androidx/health/platform/client/proto/Any.java:163`
  `((Any) this.instance).setValue(value);`
- `sources/androidx/health/platform/client/proto/BytesValue.java:24`
  `public void setValue(ByteString value) {`
- `sources/androidx/health/platform/client/proto/BytesValue.java:104`
  `public Builder setValue(ByteString value) {`
- `sources/androidx/health/platform/client/proto/BytesValue.java:106`
  `((BytesValue) this.instance).setValue(value);`
- `sources/androidx/health/platform/client/proto/BytesValue.java:200`
  `return newBuilder().setValue(value).build();`
- `sources/androidx/health/platform/client/proto/LazyFieldLite.java:80`
  `public MessageLite setValue(MessageLite value) {`
- `sources/androidx/health/platform/client/proto/LazyFieldLite.java:106`
  `setValue(mergeValueAndBytes(other.value, this.delayedBytes, this.extensionRegistry));`

## BR062

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/com/inuker/bluetooth/library/connect/BleConnectWorker.java:133`
  `public void onCharacteristicRead(BluetoothGattCharacteristic bluetoothGattCharacteristic, int i, byte[] bArr) {`
- `sources/com/inuker/bluetooth/library/connect/BleConnectWorker.java:135`
  `BluetoothLog.v(String.format("onCharacteristicRead for %s: status = %d, service = 0x%s, character = 0x%s, value = %s", this.mBluetoothDevice.getAddress(), Integer.valueOf(i), bluetoothGattCharacteristic.getService().getUuid(), bluetoothGattCharacteristic.getUuid(), ByteUtils.byteToString(bArr)));`
- `sources/com/inuker/bluetooth/library/connect/BleConnectWorker.java:140`
  `((ReadCharacterListener) gattResponseListener).onCharacteristicRead(bluetoothGattCharacteristic, i, bArr);`
- `sources/com/inuker/bluetooth/library/connect/BleConnectWorker.java:155`
  `public void onCharacteristicChanged(BluetoothGattCharacteristic bluetoothGattCharacteristic, byte[] bArr) {`
- `sources/com/inuker/bluetooth/library/connect/BleConnectWorker.java:157`
  `BluetoothLog.v(String.format("onCharacteristicChanged for %s: value = %s, service = 0x%s, character = 0x%s", this.mBluetoothDevice.getAddress(), ByteUtils.byteToString(bArr), bluetoothGattCharacteristic.getService().getUuid(), bluetoothGattCharacteristic.getUuid()));`
- `sources/com/inuker/bluetooth/library/connect/IBleConnectWorker.java:33`
  `boolean setCharacteristicNotification(UUID uuid, UUID uuid2, boolean z);`
- `sources/com/inuker/bluetooth/library/connect/listener/IBluetoothGattResponse.java:8`
  `void onCharacteristicChanged(BluetoothGattCharacteristic bluetoothGattCharacteristic, byte[] bArr);`
- `sources/com/inuker/bluetooth/library/connect/listener/IBluetoothGattResponse.java:10`
  `void onCharacteristicRead(BluetoothGattCharacteristic bluetoothGattCharacteristic, int i, byte[] bArr);`
- `sources/com/inuker/bluetooth/library/connect/listener/ReadCharacterListener.java:7`
  `void onCharacteristicRead(BluetoothGattCharacteristic bluetoothGattCharacteristic, int i, byte[] bArr);`
- `sources/com/inuker/bluetooth/library/connect/response/BluetoothGattResponse.java:28`
  `public void onCharacteristicRead(BluetoothGatt bluetoothGatt, BluetoothGattCharacteristic bluetoothGattCharacteristic, int i) {`
- `sources/com/inuker/bluetooth/library/connect/response/BluetoothGattResponse.java:29`
  `this.response.onCharacteristicRead(bluetoothGattCharacteristic, i, bluetoothGattCharacteristic.getValue());`
- `sources/com/inuker/bluetooth/library/connect/response/BluetoothGattResponse.java:38`
  `public void onCharacteristicChanged(BluetoothGatt bluetoothGatt, BluetoothGattCharacteristic bluetoothGattCharacteristic) {`
- `sources/com/inuker/bluetooth/library/connect/response/BluetoothGattResponse.java:39`
  `this.response.onCharacteristicChanged(bluetoothGattCharacteristic, bluetoothGattCharacteristic.getValue());`

## BR063

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/android/support/v4/media/session/MediaControllerCompat.java:44`
  `public static final String COMMAND_ADD_QUEUE_ITEM = "android.support.v4.media.session.command.ADD_QUEUE_ITEM";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:45`
  `public static final String COMMAND_ADD_QUEUE_ITEM_AT = "android.support.v4.media.session.command.ADD_QUEUE_ITEM_AT";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:46`
  `public static final String COMMAND_ARGUMENT_INDEX = "android.support.v4.media.session.command.ARGUMENT_INDEX";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:47`
  `public static final String COMMAND_ARGUMENT_MEDIA_DESCRIPTION = "android.support.v4.media.session.command.ARGUMENT_MEDIA_DESCRIPTION";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:48`
  `public static final String COMMAND_GET_EXTRA_BINDER = "android.support.v4.media.session.command.GET_EXTRA_BINDER";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:49`
  `public static final String COMMAND_REMOVE_QUEUE_ITEM = "android.support.v4.media.session.command.REMOVE_QUEUE_ITEM";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:50`
  `public static final String COMMAND_REMOVE_QUEUE_ITEM_AT = "android.support.v4.media.session.command.REMOVE_QUEUE_ITEM_AT";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:990`
  `public void sendCommand(String command, Bundle params, ResultReceiver cb) {`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:992`
  `this.mBinder.sendCommand(command, params, cb == null ? null : new MediaSessionCompat.ResultReceiverWrapper(cb));`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1470`
  `public void sendCommand(String command, Bundle params, ResultReceiver cb) {`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1471`
  `this.mControllerFwk.sendCommand(command, params, cb);`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:259`
  `byte[] bArrJpegImageToJpegByteArray = jpegImageToJpegByteArray(imageProxy);`
- `sources/androidx/datastore/preferences/protobuf/BinaryWriter.java:1350`
  `byte[] bArr4 = this.buffer;`
- `sources/androidx/datastore/preferences/protobuf/CodedInputStream.java:2317`
  `byte[] bArr = this.buffer;`
- `sources/androidx/datastore/preferences/protobuf/CodedOutputStream.java:517`
  `byte[] bytes = str.getBytes(Internal.UTF_8);`
- `sources/androidx/exifinterface/media/ExifInterface.java:1843`
  `byte[] bArr = this.mThumbnailBytes;`
- `sources/androidx/exifinterface/media/ExifInterface.java:2110`
  `byte[] bArr = new byte[5000];`
- `sources/androidx/exifinterface/media/ExifInterface.java:2342`
  `byte[] bArr = IDENTIFIER_EXIF_APP1;`
- `sources/androidx/exifinterface/media/ExifInterface.java:2344`
  `byte[] bArr2 = new byte[bArr.length];`
- `sources/androidx/exifinterface/media/ExifInterface.java:2349`
  `byte[] bArr3 = IDENTIFIER_EXIF_APP1;`
- `sources/androidx/health/platform/client/proto/BinaryWriter.java:1354`
  `byte[] bArr4 = this.buffer;`
- `sources/androidx/health/platform/client/proto/CodedInputStream.java:2350`
  `byte[] bArr = this.buffer;`
- `sources/androidx/health/platform/client/proto/CodedOutputStream.java:517`
  `byte[] bytes = value.getBytes(Internal.UTF_8);`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:204`
  `int iUpdatePositionWithPostponed2 = updatePositionWithPostponed(updateOp.positionStart + (i * i5), updateOp.cmd);`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:205`
  `int i6 = updateOp.cmd;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:207`
  `UpdateOp updateOpObtainUpdateOp = obtainUpdateOp(updateOp.cmd, iUpdatePositionWithPostponed, i4, updateOp.payload);`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:210`
  `if (updateOp.cmd == 4) {`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:222`
  `UpdateOp updateOpObtainUpdateOp2 = obtainUpdateOp(updateOp.cmd, iUpdatePositionWithPostponed, i4, obj);`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:230`
  `int i2 = updateOp.cmd;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:506`
  `int cmd;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:512`
  `this.cmd = i;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:519`
  `int i = this.cmd;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:579`
  `updateOpAcquire.cmd = i;`
- `sources/androidx/room/RoomSQLiteQuery.java:96`
  `this.mBlobBindings = new byte[i2][];`
- `sources/ch/qos/logback/core/net/SyslogOutputStream.java:34`
  `byte[] byteArray = this.baos.toByteArray();`
- `sources/com/blankj/utilcode/util/ImageUtils.java:1298`
  `byte[] byteArray = byteArrayOutputStream.toByteArray();`
- `sources/com/blankj/utilcode/util/ImageUtils.java:1317`
  `byte[] byteArray = byteArrayOutputStream.toByteArray();`
- `sources/com/bumptech/glide/gifdecoder/GifHeaderParser.java:32`
  `private final byte[] block = new byte[256];`
- `sources/com/bumptech/glide/load/resource/bitmap/Downsampler.java:129`
  `byte[] bArr = (byte[]) this.byteArrayPool.get(65536, byte[].class);`
- `sources/com/bumptech/glide/load/resource/bitmap/ImageReader.java:47`
  `byte[] bArr = this.bytes;`

## BR064

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:202`
  `String name = xml.getName();`
- `sources/androidx/biometric/BiometricPrompt.java:20`
  `import javax.crypto.Mac;`
- `sources/androidx/biometric/BiometricPrompt.java:64`
  `private final Mac mMac;`
- `sources/androidx/biometric/BiometricPrompt.java:81`
  `public CryptoObject(Mac mac) {`
- `sources/androidx/biometric/BiometricPrompt.java:84`
  `this.mMac = mac;`
- `sources/androidx/biometric/BiometricPrompt.java:103`
  `public Mac getMac() {`
- `sources/androidx/biometric/CryptoObjectUtils.java:48`
  `Mac mac = Api28Impl.getMac(cryptoObject);`
- `sources/androidx/biometric/CryptoObjectUtils.java:49`
  `if (mac != null) {`
- `sources/androidx/biometric/CryptoObjectUtils.java:50`
  `return new BiometricPrompt.CryptoObject(mac);`
- `sources/androidx/biometric/CryptoObjectUtils.java:71`
  `Mac mac = cryptoObject.getMac();`
- `sources/androidx/biometric/CryptoObjectUtils.java:72`
  `if (mac != null) {`
- `sources/androidx/biometric/CryptoObjectUtils.java:73`
  `return Api28Impl.create(mac);`
- `sources/androidx/biometric/CryptoObjectUtils.java:112`
  `Mac mac = cryptoObject.getMac();`
- `sources/androidx/biometric/CryptoObjectUtils.java:113`
  `if (mac != null) {`
- `sources/androidx/biometric/CryptoObjectUtils.java:114`
  `return new FingerprintManagerCompat.CryptoObject(mac);`
- `sources/androidx/browser/customtabs/PostMessageServiceConnection.java:40`
  `intent.setClassName(str, PostMessageService.class.getName());`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1051`
  `this.mUseCaseAttachState.setUseCaseDetached(this.mMeteringRepeatingSession.getName() + this.mMeteringRepeatingSession.hashCode());`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1052`
  `this.mUseCaseAttachState.setUseCaseInactive(this.mMeteringRepeatingSession.getName() + this.mMeteringRepeatingSession.hashCode());`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1409`
  `return meteringRepeatingSession.getName() + meteringRepeatingSession.hashCode();`
- `sources/androidx/camera/camera2/internal/DynamicRangeResolver.java:103`
  `DynamicRange dynamicRangeResolveDynamicRange = resolveDynamicRange(dynamicRange, set4, set2, set3, useCaseConfig.getTargetName());`
- `sources/androidx/camera/camera2/internal/DynamicRangeResolver.java:108`
  `throw new IllegalArgumentException(String.format("Unable to resolve supported dynamic range. The dynamic range may not be supported on the device or may not be allowed concurrently with other attached use cases.\nUse case:\n  %s\nRequested dynamic range:\n  %s\nSupported dynamic ranges:\n  %s\nConst...`
- `sources/androidx/camera/video/VideoCapture.java:257`
  `return "VideoCapture:" + getName();`
- `sources/androidx/compose/ui/platform/JvmActuals_jvmKt.java:19`
  `str = obj.getClass().getName();`
- `sources/androidx/compose/ui/res/PainterResources_androidKt.java:103`
  `if (!Intrinsics.areEqual(XmlVectorParser_androidKt.seekToStartTag(xml).getName(), "vector")) {`
- `sources/androidx/compose/ui/semantics/SemanticsConfiguration.java:186`
  `sb.append(key.getName());`
- `sources/androidx/compose/ui/text/font/DeviceFontFamilyName.java:61`
  `public final String getName() {`
- `sources/androidx/compose/ui/text/font/PlatformTypefacesApi.java:26`
  `android.graphics.Typeface typefaceM5305loadNamedFromTypefaceCacheOrNullRetOiIg = m5305loadNamedFromTypefaceCacheOrNullRetOiIg(PlatformTypefacesKt.getWeightSuffixForFallbackFamilyName(name.getName(), fontWeight), fontWeight, fontStyle);`
- `sources/androidx/compose/ui/text/font/PlatformTypefacesApi.java:27`
  `return typefaceM5305loadNamedFromTypefaceCacheOrNullRetOiIg == null ? m5303createAndroidTypefaceUsingTypefaceStyleRetOiIg(name.getName(), fontWeight, fontStyle) : typefaceM5305loadNamedFromTypefaceCacheOrNullRetOiIg;`
- `sources/androidx/compose/ui/text/font/PlatformTypefacesApi.java:38`
  `if (Intrinsics.areEqual(familyName, FontFamily.INSTANCE.getSansSerif().getName())) {`
- `sources/androidx/compose/ui/text/font/PlatformTypefacesApi.java:40`
  `} else if (Intrinsics.areEqual(familyName, FontFamily.INSTANCE.getSerif().getName())) {`
- `sources/androidx/compose/ui/text/font/PlatformTypefacesApi.java:42`
  `} else if (Intrinsics.areEqual(familyName, FontFamily.INSTANCE.getMonospace().getName())) {`
- `sources/androidx/compose/ui/text/font/PlatformTypefacesApi.java:45`
  `typefaceMo5301createNamedRetOiIg = Intrinsics.areEqual(familyName, FontFamily.INSTANCE.getCursive().getName()) ? mo5301createNamedRetOiIg(FontFamily.INSTANCE.getCursive(), weight, style) : m5305loadNamedFromTypefaceCacheOrNullRetOiIg(familyName, weight, style);`
- `sources/androidx/compose/ui/text/font/PlatformTypefacesApi28.java:22`
  `if (Intrinsics.areEqual(familyName, FontFamily.INSTANCE.getSansSerif().getName())) {`
- `sources/androidx/compose/ui/text/font/PlatformTypefacesApi28.java:24`
  `} else if (Intrinsics.areEqual(familyName, FontFamily.INSTANCE.getSerif().getName())) {`
- `sources/androidx/compose/ui/text/font/PlatformTypefacesApi28.java:26`
  `} else if (Intrinsics.areEqual(familyName, FontFamily.INSTANCE.getMonospace().getName())) {`
- `sources/androidx/compose/ui/text/font/PlatformTypefacesApi28.java:29`
  `typefaceMo5301createNamedRetOiIg = Intrinsics.areEqual(familyName, FontFamily.INSTANCE.getCursive().getName()) ? mo5301createNamedRetOiIg(FontFamily.INSTANCE.getCursive(), weight, style) : m5308loadNamedFromTypefaceCacheOrNullRetOiIg(familyName, weight, style);`
- `sources/androidx/compose/ui/text/font/PlatformTypefacesApi28.java:46`
  `return m5306createAndroidTypefaceApi28RetOiIg(name.getName(), fontWeight, fontStyle);`
- `sources/androidx/compose/ui/tooling/data/SlotTreeKt.java:335`
  `String name = sourceInformationContextSourceInformationContextOf != null ? sourceInformationContextSourceInformationContextOf.getName() : null;`
- `sources/androidx/compose/ui/tooling/data/SlotTreeKt.java:336`
  `String name2 = sourceInformationContextSourceInformationContextOf != null ? sourceInformationContextSourceInformationContextOf.getName() : null;`
- `sources/androidx/core/app/NotificationCompat.java:1446`
  `if (TextUtils.isEmpty(person.getName())) {`
- `sources/androidx/core/app/NotificationCompat.java:1454`
  `return this.mUser.getName();`
- `sources/androidx/core/app/NotificationCompat.java:1550`
  `messagingStyleCreateMessagingStyle = Api24Impl.createMessagingStyle(this.mUser.getName());`
- `sources/androidx/core/app/NotificationCompat.java:1628`
  `CharSequence name = message.getPerson() == null ? "" : message.getPerson().getName();`
- `sources/androidx/core/app/NotificationCompat.java:1632`
  `name = this.mUser.getName();`
- `sources/androidx/core/app/NotificationCompat.java:1651`
  `bundle.putCharSequence(NotificationCompat.EXTRA_SELF_DISPLAY_NAME, this.mUser.getName());`
- `sources/androidx/core/content/FileProvider.java:215`
  `String name = fileProviderPathsMetaData.getName();`
- `sources/androidx/core/graphics/WeightTypefaceApi14.java:25`
  `Log.e(TAG, e.getClass().getName(), e);`
- `sources/androidx/core/util/DebugUtils.java:14`
  `if ((simpleName == null || simpleName.length() <= 0) && (iLastIndexOf = (simpleName = obj.getClass().getName()).lastIndexOf(46)) > 0) {`
- `sources/androidx/health/connect/client/impl/converters/records/ProtoToRecordConvertersKt.java:86`
  `String name = proto.getDataType().getName();`
- `sources/androidx/lifecycle/viewmodel/compose/SavedStateHandleSaverKt.java:100`
  `final Object objM6425saveable = SavedStateHandleSaverKt.m6425saveable(savedStateHandle, property.getName(), (Saver<Object, ? extends Object>) saver, (Function0<? extends Object>) init);`
- `sources/androidx/lifecycle/viewmodel/compose/SavedStateHandleSaverKt.java:133`
  `final MutableState mutableStateSaveable = SavedStateHandleSaverKt.saveable(savedStateHandle, property.getName(), (Saver) stateSaver, (Function0) init);`
- `sources/androidx/media2/session/MediaSessionImplBase.java:108`
  `Uri uriBuild = new Uri.Builder().scheme(MediaSessionImplBase.class.getName()).appendPath(str).appendPath(String.valueOf(SystemClock.elapsedRealtime())).build();`
- `sources/androidx/media2/session/MediaUtils.java:581`
  `arrayList.add(new MediaSession.CommandButton.Builder().setCommand(new SessionCommand(customAction.getAction(), customAction.getExtras())).setDisplayName(customAction.getName()).setEnabled(true).setIconResId(customAction.getIcon()).build());`
- `sources/androidx/privacysandbox/ads/adservices/customaudience/CustomAudienceManager.java:68`
  `android.adservices.customaudience.LeaveCustomAudienceRequest leaveCustomAudienceRequestBuild = DeletionRequest$$ExternalSyntheticApiModelOutline0.m6467m().setBuyer(convertAdTechIdentifier(request.getBuyer())).setName(request.getName()).build();`
- `sources/androidx/privacysandbox/ads/adservices/customaudience/CustomAudienceManager.java:74`
  `android.adservices.customaudience.CustomAudience customAudienceBuild = DeletionRequest$$ExternalSyntheticApiModelOutline0.m6464m().setActivationTime(request.getActivationTime()).setAds(convertAdData(request.getAds())).setBiddingLogicUri(request.getBiddingLogicUri()).setBuyer(convertAdTechIdentifier(...`
- `sources/androidx/savedstate/SavedStateRegistry.java:118`
  `String name = clazz.getName();`
- `sources/androidx/versionedparcelable/VersionedParcel.java:992`
  `Method method = this.mWriteCache.get(cls.getName());`
- `sources/androidx/versionedparcelable/VersionedParcel.java:999`
  `this.mWriteCache.put(cls.getName(), declaredMethod);`
- `sources/androidx/versionedparcelable/VersionedParcel.java:1004`
  `Class cls2 = this.mParcelizerCache.get(cls.getName());`
- `sources/androidx/versionedparcelable/VersionedParcel.java:1008`
  `Class<?> cls3 = Class.forName(String.format("%s.%sParcelizer", cls.getPackage().getName(), cls.getSimpleName()), false, cls.getClassLoader());`
- `sources/androidx/versionedparcelable/VersionedParcel.java:1009`
  `this.mParcelizerCache.put(cls.getName(), cls3);`
- `sources/ch/qos/logback/core/pattern/parser/Parser.java:26`
  `map.put(Token.BARE_COMPOSITE_KEYWORD_TOKEN.getValue().toString(), IdentityCompositeConverter.class.getName());`
- `sources/ch/qos/logback/core/pattern/parser/Parser.java:27`
  `map.put(REPLACE_CONVERTER_WORD, ReplacingCompositeConverter.class.getName());`
- `sources/com/alibaba/android/arouter/core/AutowiredServiceImpl.java:43`
  `String name = cls.getName();`
- `sources/com/alibaba/android/arouter/core/AutowiredServiceImpl.java:50`
  `iSyringe = (ISyringe) Class.forName(cls.getName() + Consts.SUFFIX_AUTOWIRED).getConstructor(new Class[0]).newInstance(new Object[0]);`
- `sources/com/blankj/utilcode/util/BusUtils.java:121`
  `String name = cls.getName();`
- `sources/com/blankj/utilcode/util/BusUtils.java:200`
  `String name = obj.getClass().getName();`
- `sources/com/blankj/utilcode/util/LogUtils.java:610`
  `String name = file.getName();`
- `sources/com/blankj/utilcode/util/MessengerUtils.java:37`
  `if (UtilsBridge.isServiceRunning(ServerService.class.getName())) {`
- `sources/com/blankj/utilcode/util/MessengerUtils.java:60`
  `if (!UtilsBridge.isServiceRunning(ServerService.class.getName())) {`
- `sources/com/bruhealth/glucometer/GlucometerListener.java:13`
  `@Metadata(d1 = {"\u00004\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\u0007\bf\u0018\u00002\u00020\u0001J\u0018\u001...`
- `sources/com/bruhealth/glucometer/GlucometerListener.java:15`
  `void onConnectFail(String mac, String msg);`
- `sources/com/bruhealth/glucometer/GlucometerListener.java:17`
  `void onConnectSuccess(BleGattProfile data, String mac);`
- `sources/com/bruhealth/glucometer/GlucometerListener.java:21`
  `void onDisConnected(String mac);`
- `sources/com/bruhealth/glucometer/GlucometerListener.java:23`
  `void onGetHistoryData(String mac, List<GlucoseItemModel> list);`
- `sources/com/bruhealth/glucometer/GlucometerListener.java:25`
  `void onGetRealTimeData(String mac, GlucoseItemModel item);`
- `sources/com/bruhealth/glucometer/GlucometerNativeUtils.java:86`
  `String name = device.getName();`
- `sources/com/bruhealth/glucometer/GlucometerNativeUtils.java:89`
  `GlucometerNativeUtils.this.log("onDeviceFounded name:" + device.getName() + " address:" + device.getAddress() + " rssi:" + device.rssi);`
- `sources/com/bruhealth/glucometer/GlucometerNativeUtils.java:90`
  `EVYDScheme.INSTANCE.getInstance().callFlutterEvent("glucometer.scanListener", MapsKt.mapOf(TuplesKt.to("name", device.getName()), TuplesKt.to("mac", device.getAddress()), TuplesKt.to("rssi", Integer.valueOf(device.rssi)), TuplesKt.to(NotificationCompat.CATEGORY_STATUS, "success")), null);`
- `sources/com/bruhealth/glucometer/GlucometerNativeUtils.java:95`
  `public void onDisConnected(String mac) {`

## BR065

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/com/inuker/bluetooth/library/connect/BleConnectWorker.java:117`
  `public void onServicesDiscovered(int i) {`
- `sources/com/inuker/bluetooth/library/connect/BleConnectWorker.java:119`
  `BluetoothLog.v(String.format("onServicesDiscovered for %s: status = %d", this.mBluetoothDevice.getAddress(), Integer.valueOf(i)));`
- `sources/com/inuker/bluetooth/library/connect/BleConnectWorker.java:129`
  `((ServiceDiscoverListener) gattResponseListener).onServicesDiscovered(i, this.mBleGattProfile);`
- `sources/com/inuker/bluetooth/library/connect/listener/IBluetoothGattResponse.java:22`
  `void onServicesDiscovered(int i);`
- `sources/com/inuker/bluetooth/library/connect/listener/ServiceDiscoverListener.java:7`
  `void onServicesDiscovered(int i, BleGattProfile bleGattProfile);`
- `sources/com/inuker/bluetooth/library/connect/request/BleConnectRequest.java:166`
  `public void onServicesDiscovered(int i, BleGattProfile bleGattProfile) {`
- `sources/com/inuker/bluetooth/library/connect/response/BluetoothGattResponse.java:23`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/com/inuker/bluetooth/library/connect/response/BluetoothGattResponse.java:24`
  `this.response.onServicesDiscovered(i);`

## BR066

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/com/bruhealth/glucometer/util/ZBleManager.java:51`
  `@Metadata(d1 = {"\u0000\u0084\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0...`
- `sources/com/bruhealth/glucometer/util/ZBleManager.java:618`
  `private final boolean indicate(String serviceUUID, String characterUUID) {`
- `sources/com/bruhealth/glucometer/util/ZBleManager.java:632`
  `bluetoothClient.notify(this.macAddress, UUID.fromString(serviceUUID), UUID.fromString(characterUUID), this.mIndicateNotifyListener);`
- `sources/com/bruhealth/glucometer/util/ZBleManager.java:636`
  `private final boolean unIndicate(String serviceUUID, String characterUUID) {`
- `sources/com/bruhealth/glucometer/util/ZBleManager.java:650`
  `bluetoothClient.unnotify(this.macAddress, UUID.fromString(serviceUUID), UUID.fromString(characterUUID), new BleUnnotifyResponse() { // from class: com.bruhealth.glucometer.util.ZBleManager$$ExternalSyntheticLambda2`
- `sources/com/bruhealth/glucometer/util/ZBleManager.java:747`
  `bluetoothClient.write(this.macAddress, UUID.fromString(Constant.INSTANCE.getGATT_SERVICE_PRIMARY()), UUID.fromString(Constant.INSTANCE.getCHARACTERISTIC_WRITEABLE()), data, new BleWriteResponse() { // from class: com.bruhealth.glucometer.util.ZBleManager$$ExternalSyntheticLambda3`
- `sources/com/inuker/bluetooth/library/Constants.java:14`
  `public static final UUID CLIENT_CHARACTERISTIC_CONFIG = UUID.fromString("00002902-0000-1000-8000-00805f9b34fb");`
- `sources/com/inuker/bluetooth/library/connect/request/BleIndicateRequest.java:11`
  `private UUID mServiceUUID;`
- `sources/com/inuker/bluetooth/library/connect/request/BleIndicateRequest.java:15`
  `this.mServiceUUID = uuid;`
- `sources/com/inuker/bluetooth/library/connect/request/BleIndicateRequest.java:36`
  `if (!setCharacteristicIndication(this.mServiceUUID, this.mCharacterUUID, true)) {`
- `sources/com/inuker/bluetooth/library/connect/request/BleNotifyRequest.java:11`
  `private UUID mServiceUUID;`
- `sources/com/inuker/bluetooth/library/connect/request/BleNotifyRequest.java:15`
  `this.mServiceUUID = uuid;`
- `sources/com/inuker/bluetooth/library/connect/request/BleNotifyRequest.java:36`
  `if (!setCharacteristicNotification(this.mServiceUUID, this.mCharacterUUID, true)) {`
- `sources/com/inuker/bluetooth/library/connect/request/BleReadDescriptorRequest.java:13`
  `private UUID mServiceUUID;`
- `sources/com/inuker/bluetooth/library/connect/request/BleReadDescriptorRequest.java:17`
  `this.mServiceUUID = uuid;`
- `sources/com/inuker/bluetooth/library/connect/request/BleReadDescriptorRequest.java:39`
  `if (!readDescriptor(this.mServiceUUID, this.mCharacterUUID, this.mDescriptorUUID)) {`
- `sources/com/inuker/bluetooth/library/connect/request/BleReadRequest.java:12`
  `private UUID mServiceUUID;`
- `sources/com/inuker/bluetooth/library/connect/request/BleReadRequest.java:16`
  `this.mServiceUUID = uuid;`
- `sources/com/inuker/bluetooth/library/connect/request/BleReadRequest.java:37`
  `if (!readCharacteristic(this.mServiceUUID, this.mCharacterUUID)) {`
- `sources/com/inuker/bluetooth/library/connect/request/BleUnnotifyRequest.java:11`
  `private UUID mServiceUUID;`
- `sources/com/inuker/bluetooth/library/connect/request/BleUnnotifyRequest.java:15`
  `this.mServiceUUID = uuid;`
- `sources/com/inuker/bluetooth/library/connect/request/BleUnnotifyRequest.java:36`
  `if (!setCharacteristicNotification(this.mServiceUUID, this.mCharacterUUID, false)) {`
- `sources/com/inuker/bluetooth/library/connect/request/BleWriteDescriptorRequest.java:13`
  `private UUID mServiceUUID;`
- `sources/com/inuker/bluetooth/library/connect/request/BleWriteDescriptorRequest.java:17`
  `this.mServiceUUID = uuid;`
- `sources/com/inuker/bluetooth/library/connect/request/BleWriteDescriptorRequest.java:40`
  `if (!writeDescriptor(this.mServiceUUID, this.mCharacterUUID, this.mDescriptorUUID, this.mBytes)) {`
- `sources/com/inuker/bluetooth/library/connect/request/BleWriteNoRspRequest.java:12`
  `private UUID mServiceUUID;`
- `sources/com/inuker/bluetooth/library/connect/request/BleWriteNoRspRequest.java:16`
  `this.mServiceUUID = uuid;`
- `sources/com/inuker/bluetooth/library/connect/request/BleWriteNoRspRequest.java:38`
  `if (!writeCharacteristicWithNoRsp(this.mServiceUUID, this.mCharacterUUID, this.mBytes)) {`
- `sources/com/inuker/bluetooth/library/connect/request/BleWriteRequest.java:12`
  `private UUID mServiceUUID;`
- `sources/com/inuker/bluetooth/library/connect/request/BleWriteRequest.java:16`
  `this.mServiceUUID = uuid;`
- `sources/com/inuker/bluetooth/library/connect/request/BleWriteRequest.java:38`
  `if (!writeCharacteristic(this.mServiceUUID, this.mCharacterUUID, this.mBytes)) {`

## BR067

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/androidx/camera/view/CameraController.java:1005`
  `public void setPinchToZoomEnabled(boolean z) {`
- `sources/androidx/compose/foundation/lazy/layout/LazyLayoutPinnableItem.java:18`
  `@Metadata(d1 = {"\u00000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\t\n\u0002\u0010\b\n\u0002\b\u0018\n\u0002\u0010\u0002\n\u0002\b\u0003\b\u0002\u0018\u00002\u00020\u00012\u00020\u00022\u00020\u00...`
- `sources/androidx/compose/foundation/lazy/layout/LazyLayoutPinnableItem.java:63`
  `private final void setPinsCount(int i) {`
- `sources/androidx/compose/foundation/lazy/layout/LazyLayoutPinnableItem.java:118`
  `setPinsCount(getPinsCount() + 1);`
- `sources/androidx/compose/foundation/lazy/layout/LazyLayoutPinnableItem.java:127`
  `setPinsCount(getPinsCount() - 1);`

## BR068

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/com/google/android/exoplayer2/source/hls/HlsManifest.java:18`
  `this.masterPlaylist = new HlsMasterPlaylist(hlsMultivariantPlaylist.baseUri, hlsMultivariantPlaylist.tags, hlsMultivariantPlaylist.variants, hlsMultivariantPlaylist.videos, hlsMultivariantPlaylist.audios, hlsMultivariantPlaylist.subtitles, hlsMultivariantPlaylist.closedCaptions, hlsMultivariantPlayl...`
- `sources/com/google/android/exoplayer2/source/hls/HlsMediaPeriod.java:61`
  `private final boolean useSessionKeys;`
- `sources/com/google/android/exoplayer2/source/hls/HlsMediaPeriod.java:93`
  `this.useSessionKeys = z2;`
- `sources/com/google/android/exoplayer2/source/hls/HlsMediaSource.java:168`
  `return new HlsMediaSource(mediaItem, hlsDataSourceFactory, hlsExtractorFactory, compositeSequenceableLoaderFactory, drmSessionManager, loadErrorHandlingPolicy, this.playlistTrackerFactory.createTracker(this.hlsDataSourceFactory, loadErrorHandlingPolicy, filteringHlsPlaylistParserFactory), this.elaps...`
- `sources/com/google/android/exoplayer2/source/hls/HlsMediaSource.java:190`
  `this.useSessionKeys = z2;`
- `sources/com/google/android/exoplayer2/source/hls/HlsMediaSource.java:214`
  `return new HlsMediaPeriod(this.extractorFactory, this.playlistTracker, this.dataSourceFactory, this.mediaTransferListener, this.drmSessionManager, createDrmEventDispatcher(mediaPeriodId), this.loadErrorHandlingPolicy, eventDispatcherCreateEventDispatcher, allocator, this.compositeSequenceableLoaderF...`
- `sources/com/google/android/exoplayer2/source/hls/playlist/HlsMultivariantPlaylist.java:24`
  `public final List<DrmInitData> sessionKeyDrmInitData;`
- `sources/com/google/android/exoplayer2/source/hls/playlist/HlsMultivariantPlaylist.java:87`
  `this.sessionKeyDrmInitData = Collections.unmodifiableList(list8);`
- `sources/com/google/android/exoplayer2/source/hls/playlist/HlsMultivariantPlaylist.java:92`
  `return new HlsMultivariantPlaylist(this.baseUri, this.tags, copyStreams(this.variants, 0, list), Collections.emptyList(), copyStreams(this.audios, 1, list), copyStreams(this.subtitles, 2, list), Collections.emptyList(), this.muxedAudioFormat, this.muxedCaptionFormats, this.hasIndependentSegments, th...`
- `sources/com/google/android/gms/auth/api/accounttransfer/AccountTransferStatusCodes.java:7`
  `public static final int CHALLENGE_NOT_ALLOWED = 20503;`
- `sources/com/google/android/gms/auth/api/accounttransfer/AccountTransferStatusCodes.java:21`
  `case CHALLENGE_NOT_ALLOWED /* 20503 */:`
- `sources/com/google/android/gms/auth/api/accounttransfer/AccountTransferStatusCodes.java:22`
  `return "CHALLENGE_NOT_ALLOWED";`
- `sources/com/google/android/gms/auth/api/accounttransfer/DeviceMetaData.java:41`
  `SafeParcelWriter.writeBoolean(parcel, 4, isChallengeAllowed());`
- `sources/com/google/zxing/pdf417/PDF417Common.java:50`
  `1291, 1288, 265, 1302, 1299, 2113, 204, 196, 192, 2042, 1232, 1230, 1224, 214, 1220, 210, 1242, 1239, 1235, 1250, 2077, 2075, 151, 148, 1993, 144, 1990, 1163, 1162, 1160, 1158, 1155, 161, 1152, 157, 1173, 1171, 1168, 1165, 168, 1181, 1178, 2021, 2020, 2018, 2023, 585, 560, 557, 1585, 516, 509, 1562,...`
- `sources/com/tencent/liteav/live/TXLivePlayerJni.java:259`
  `nativeSetConfig(this.mNativeTXLivePlayerJni, tXLivePlayConfig.getCacheTime(), tXLivePlayConfig.getMaxAutoAdjustCacheTime(), tXLivePlayConfig.getMinAutoAdjustCacheTime(), tXLivePlayConfig.getVideoBlockThreshold(), tXLivePlayConfig.getConnectRetryCount(), tXLivePlayConfig.getConnectRetryInterval(), tX...`
- `sources/com/tencent/rtmp/TXLivePlayConfig.java:22`
  `String mFlvSessionKey = "";`
- `sources/com/tencent/rtmp/TXLivePlayConfig.java:74`
  `public String getFlvSessionKey() {`
- `sources/com/tencent/rtmp/TXLivePlayConfig.java:75`
  `return this.mFlvSessionKey;`
- `sources/com/tencent/rtmp/TXLivePlayConfig.java:118`
  `public void setFlvSessionKey(String str) {`
- `sources/com/tencent/rtmp/TXLivePlayConfig.java:119`
  `this.mFlvSessionKey = str;`
- `sources/egnc/moh/base/view/MapDialog.java:172`
  `logReportUtils.addClickLog("choose map", str4, "Challenge", "choose_map", "", map2, map);`
- `sources/egnc/moh/base/web/manager/CallMethodManager.java:1254`
  `LogReportUtils.getInstance().addSkimLog("choose map", "", "choose_map", "Open direction in a map", "Challenge", new HashMap(), mapJsonToMap);`
- `sources/egnc/moh/bruhealth/compose/ExtendsKt.java:43`
  `import egnc.moh.bruhealth.compose.dialog.ChallengeJoinDialogKt;`
- `sources/egnc/moh/bruhealth/compose/ExtendsKt.java:71`
  `@Metadata(d1 = {"\u00002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010$\n\u0000\n\u0002\u0018\u0002\n\u0002\u0010\b\n\u0002\b\b\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\u001a<\u0010\u0000\u001a\u00020\u00012\u0006\u0010\u0002...`
- `sources/egnc/moh/bruhealth/compose/ExtendsKt.java:1711`
  `composeView.setContent(ComposableLambdaKt.composableLambdaInstance(-228158272, true, new Function2<Composer, Integer, Unit>() { // from class: egnc.moh.bruhealth.compose.ExtendsKt$showChallengeRoutines$1$1`
- `sources/egnc/moh/bruhealth/compose/ExtendsKt.java:1727`
  `ComposerKt.traceEventStart(-228158272, i, -1, "egnc.moh.bruhealth.compose.showChallengeRoutines.<anonymous>.<anonymous> (extends.kt:481)");`
- `sources/egnc/moh/bruhealth/compose/ExtendsKt.java:1747`
  `Function0<Unit> function0 = new Function0<Unit>() { // from class: egnc.moh.bruhealth.compose.ExtendsKt$showChallengeRoutines$1$1.1`
- `sources/egnc/moh/bruhealth/compose/ExtendsKt.java:1787`
  `RewardDialogKt.ShowBottomSheet(function0, function12, true, ComposableLambdaKt.composableLambda(composer, 266468841, true, new Function2<Composer, Integer, Unit>() { // from class: egnc.moh.bruhealth.compose.ExtendsKt$showChallengeRoutines$1$1.3`
- `sources/egnc/moh/bruhealth/compose/dialog/ChallengeJoinDialogKt.java:94`
  `public static final void ChallengeRoutinesDialog(java.lang.String r24, java.lang.String r25, java.lang.String r26, java.lang.String r27, java.lang.String r28, kotlin.jvm.functions.Function1<? super java.lang.Boolean, kotlin.Unit> r29, androidx.compose.runtime.Composer r30, final int r31, final int r...`
- `sources/egnc/moh/bruhealth/compose/dialog/ChallengeJoinDialogKt.java:99`
  `throw new UnsupportedOperationException("Method not decompiled: egnc.moh.bruhealth.compose.dialog.ChallengeJoinDialogKt.ChallengeRoutinesDialog(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, kotlin.jvm.functions.Function1, androidx.compose.runtime.Composer,...`
- `sources/egnc/moh/bruhealth/compose/dialog/ChallengeJoinDialogKt.java:124`
  `public static final void ChallengeJoinTop(java.lang.String r62, java.lang.String r63, androidx.compose.runtime.Composer r64, final int r65, final int r66) {`
- `sources/egnc/moh/bruhealth/compose/dialog/ChallengeJoinDialogKt.java:129`
  `throw new UnsupportedOperationException("Method not decompiled: egnc.moh.bruhealth.compose.dialog.ChallengeJoinDialogKt.ChallengeJoinTop(java.lang.String, java.lang.String, androidx.compose.runtime.Composer, int, int):void");`
- `sources/egnc/moh/bruhealth/compose/dialog/ChallengeJoinDialogKt.java:152`
  `ComposerKt.traceEventStart(1939977013, i3, -1, "egnc.moh.bruhealth.compose.dialog.ChallengeJoinDescription (ChallengeJoinDialog.kt:104)");`
- `sources/egnc/moh/bruhealth/compose/dialog/ChallengeJoinDialogKt.java:256`
  `public static final void ChallengeJoinBottom(java.lang.String r98, java.lang.String r99, kotlin.jvm.functions.Function1<? super java.lang.Boolean, kotlin.Unit> r100, androidx.compose.runtime.Composer r101, final int r102, final int r103) {`
- `sources/egnc/moh/bruhealth/compose/dialog/ChallengeJoinDialogKt.java:261`
  `throw new UnsupportedOperationException("Method not decompiled: egnc.moh.bruhealth.compose.dialog.ChallengeJoinDialogKt.ChallengeJoinBottom(java.lang.String, java.lang.String, kotlin.jvm.functions.Function1, androidx.compose.runtime.Composer, int, int):void");`
- `sources/egnc/moh/bruhealth/compose/dialog/ComposableSingletons$ChallengeJoinDialogKt.java:30`
  `/* JADX INFO: compiled from: ChallengeJoinDialog.kt */`
- `sources/egnc/moh/bruhealth/compose/dialog/ComposableSingletons$ChallengeJoinDialogKt.java:33`
  `public final class ComposableSingletons$ChallengeJoinDialogKt {`
- `sources/egnc/moh/bruhealth/compose/dialog/ComposableSingletons$ChallengeJoinDialogKt.java:34`
  `public static final ComposableSingletons$ChallengeJoinDialogKt INSTANCE = new ComposableSingletons$ChallengeJoinDialogKt();`
- `sources/egnc/moh/bruhealth/compose/dialog/ComposableSingletons$ChallengeJoinDialogKt.java:37`
  `public static Function3<GlideSubcompositionScope, Composer, Integer, Unit> f74lambda1 = ComposableLambdaKt.composableLambdaInstance(-1158240447, false, new Function3<GlideSubcompositionScope, Composer, Integer, Unit>() { // from class: egnc.moh.bruhealth.compose.dialog.ComposableSingletons$Challenge...`
- `sources/egnc/moh/bruhealth/compose/dialog/ComposableSingletons$ChallengeJoinDialogKt.java:47`
  `ComposerKt.traceEventStart(-1158240447, i, -1, "egnc.moh.bruhealth.compose.dialog.ComposableSingletons$ChallengeJoinDialogKt.lambda-1.<anonymous> (ChallengeJoinDialog.kt:78)");`
- `sources/okhttp3/Challenge.java:83`
  `public final Challenge withCharset(Charset charset) {`
- `sources/okhttp3/Challenge.java:89`
  `return new Challenge(this.scheme, (Map<String, String>) mutableMap);`
- `sources/okhttp3/Response.java:24`
  `@Metadata(d1 = {"\u0000p\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010\t\n\u0002\b\u...`
- `sources/okhttp3/internal/http/HttpHeaders.java:42`
  `readChallengeHeader(new Buffer().writeUtf8(headers.value(i)), arrayList);`
- `sources/okhttp3/internal/http/HttpHeaders.java:44`
  `Platform.INSTANCE.get().log("Unable to parse challenge", 5, e);`
- `sources/okhttp3/internal/http/HttpHeaders.java:65`
  `private static final void readChallengeHeader(okio.Buffer r7, java.util.List<okhttp3.Challenge> r8) throws java.io.EOFException {`

## BR069

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/com/google/api/BackendRule.java:473`
  `public String getAddress() {`
- `sources/com/google/api/BackendRule.java:474`
  `return ((BackendRule) this.instance).getAddress();`
- `sources/com/inuker/bluetooth/library/connect/BleConnectWorker.java:146`
  `BluetoothLog.v(String.format("onCharacteristicWrite for %s: status = %d, service = 0x%s, character = 0x%s, value = %s", this.mBluetoothDevice.getAddress(), Integer.valueOf(i), bluetoothGattCharacteristic.getService().getUuid(), bluetoothGattCharacteristic.getUuid(), ByteUtils.byteToString(bArr)));`
- `sources/com/inuker/bluetooth/library/connect/BleConnectWorker.java:157`
  `BluetoothLog.v(String.format("onCharacteristicChanged for %s: value = %s, service = 0x%s, character = 0x%s", this.mBluetoothDevice.getAddress(), ByteUtils.byteToString(bArr), bluetoothGattCharacteristic.getService().getUuid(), bluetoothGattCharacteristic.getUuid()));`
- `sources/com/inuker/bluetooth/library/connect/BleConnectWorker.java:175`
  `BluetoothLog.v(String.format("onDescriptorWrite for %s: status = %d, service = 0x%s, character = 0x%s, descriptor = 0x%s", this.mBluetoothDevice.getAddress(), Integer.valueOf(i), bluetoothGattDescriptor.getCharacteristic().getService().getUuid(), bluetoothGattDescriptor.getCharacteristic().getUuid()...`
- `sources/com/inuker/bluetooth/library/connect/BleConnectWorker.java:186`
  `BluetoothLog.v(String.format("onReadRemoteRssi for %s, rssi = %d, status = %d", this.mBluetoothDevice.getAddress(), Integer.valueOf(i), Integer.valueOf(i2)));`
- `sources/com/inuker/bluetooth/library/connect/BleConnectWorker.java:291`
  `BluetoothLog.v(String.format("refreshDeviceCache for %s", getAddress()));`
- `sources/com/inuker/bluetooth/library/connect/BleConnectWorker.java:307`
  `BluetoothLog.v(String.format("readCharacteristic for %s: service = 0x%s, character = 0x%s", this.mBluetoothDevice.getAddress(), uuid, uuid2));`
- `sources/okio/HashingSink.java:100`
  `Intrinsics.checkNotNullExpressionValue(mac, "try {\n      Mac.getInsta…rgumentException(e)\n    }");`
- `sources/okio/HashingSink.java:101`
  `this(sink, mac);`
- `sources/okio/HashingSink.java:120`
  `Mac mac = this.mac;`
- `sources/okio/HashingSink.java:121`
  `Intrinsics.checkNotNull(mac);`
- `sources/okio/HashingSink.java:122`
  `mac.update(segment.data, segment.pos, iMin);`

## BR070

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/com/bumptech/glide/load/data/HttpUrlFetcher.java:143`
  `private HttpURLConnection buildAndConfigureConnection(URL url, Map<String, String> map) throws HttpException {`
- `sources/egnc/moh/base/web/CommonWebView.java:208`
  `onRetryConnectionClickListener.reconnect();`
- `sources/kotlinx/coroutines/flow/FlowKt__MigrationKt.java:376`
  `@Deprecated(level = DeprecationLevel.ERROR, message = "Flow analogue of 'replay(bufferSize)' is 'shareIn' with the specified replay parameter. \nreplay().connect() is the default strategy (no extra call is needed), \nreplay().autoConnect() translates to 'started = SharingStared.Lazily' argument, \nr...`
- `sources/okhttp3/EventListener.java:14`
  `@Metadata(d1 = {"\u0000z\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004...`

## BR073

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:672`
  `public void restoreToolbarHierarchyState(SparseArray<Parcelable> sparseArray) {`
- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:674`
  `this.mDecorToolbar.restoreHierarchyState(sparseArray);`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:463`
  `java.lang.String r5 = r2.getAttributeValue(r6, r5)     // Catch: java.lang.Throwable -> L89 java.io.IOException -> L8b org.xmlpull.v1.XmlPullParserException -> La5`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:465`
  `java.lang.String r7 = r2.getAttributeValue(r6, r7)     // Catch: java.lang.Throwable -> L89 java.io.IOException -> L8b org.xmlpull.v1.XmlPullParserException -> La5`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:466`
  `long r7 = java.lang.Long.parseLong(r7)     // Catch: java.lang.Throwable -> L89 java.io.IOException -> L8b org.xmlpull.v1.XmlPullParserException -> La5`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:468`
  `java.lang.String r6 = r2.getAttributeValue(r6, r9)     // Catch: java.lang.Throwable -> L89 java.io.IOException -> L8b org.xmlpull.v1.XmlPullParserException -> La5`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:469`
  `float r6 = java.lang.Float.parseFloat(r6)     // Catch: java.lang.Throwable -> L89 java.io.IOException -> L8b org.xmlpull.v1.XmlPullParserException -> La5`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:470`
  `androidx.appcompat.widget.ActivityChooserModel$HistoricalRecord r9 = new androidx.appcompat.widget.ActivityChooserModel$HistoricalRecord     // Catch: java.lang.Throwable -> L89 java.io.IOException -> L8b org.xmlpull.v1.XmlPullParserException -> La5`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:471`
  `r9.<init>(r5, r7, r6)     // Catch: java.lang.Throwable -> L89 java.io.IOException -> L8b org.xmlpull.v1.XmlPullParserException -> La5`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:472`
  `r3.add(r9)     // Catch: java.lang.Throwable -> L89 java.io.IOException -> L8b org.xmlpull.v1.XmlPullParserException -> La5`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:205`
  `TextViewCompat.setCompoundDrawableTintMode(this.mView, DrawableUtils.parseTintMode(tintTypedArrayObtainStyledAttributes4.getInt(R.styleable.AppCompatTextView_drawableTintMode, -1), null));`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:420`
  `SparseArray sparseParcelableArray = extras.getSparseParcelableArray(EXTRA_COLOR_SCHEME_PARAMS);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:421`
  `return (sparseParcelableArray == null || (bundle = (Bundle) sparseParcelableArray.get(i)) == null) ? customTabColorSchemeParamsFromBundle : CustomTabColorSchemeParams.fromBundle(bundle).withDefaults(customTabColorSchemeParamsFromBundle);`
- `sources/androidx/browser/trusted/TokenContents.java:42`
  `parseIfNeeded();`
- `sources/androidx/browser/trusted/TokenContents.java:51`
  `parseIfNeeded();`
- `sources/androidx/browser/trusted/TokenContents.java:60`
  `parseIfNeeded();`
- `sources/androidx/browser/trusted/TokenContents.java:130`
  `private void parseIfNeeded() throws IOException {`
- `sources/androidx/camera/camera2/internal/Camera2CaptureOptionUnpacker.java:16`
  `@Override // androidx.camera.core.impl.CaptureConfig.OptionUnpacker`
- `sources/androidx/camera/camera2/internal/Camera2CaptureOptionUnpacker.java:17`
  `public void unpack(UseCaseConfig<?> useCaseConfig, CaptureConfig.Builder builder) {`
- `sources/androidx/camera/camera2/internal/Camera2SessionOptionUnpacker.java:20`
  `@Override // androidx.camera.core.impl.SessionConfig.OptionUnpacker`
- `sources/androidx/camera/camera2/internal/Camera2SessionOptionUnpacker.java:21`
  `public void unpack(Size size, UseCaseConfig<?> useCaseConfig, SessionConfig.Builder builder) {`
- `sources/androidx/camera/camera2/internal/Camera2UseCaseConfigFactory.java:27`
  `mutableOptionsBundleCreate.insertOption(UseCaseConfig.OPTION_SESSION_CONFIG_UNPACKER, Camera2SessionOptionUnpacker.INSTANCE);`
- `sources/androidx/camera/camera2/internal/Camera2UseCaseConfigFactory.java:31`
  `mutableOptionsBundleCreate.insertOption(UseCaseConfig.OPTION_CAPTURE_CONFIG_UNPACKER, captureType == UseCaseConfigFactory.CaptureType.IMAGE_CAPTURE ? ImageCaptureOptionUnpacker.INSTANCE : Camera2CaptureOptionUnpacker.INSTANCE);`
- `sources/androidx/camera/camera2/internal/SupportedSurfaceCombination.java:871`
  `int i = Integer.parseInt(this.mCameraId);`
- `sources/androidx/camera/core/imagecapture/JpegBytes2CroppedBitmap.java:29`
  `return BitmapRegionDecoder.newInstance(bArr, 0, bArr.length, false).decodeRegion(rect, new BitmapFactory.Options());`
- `sources/androidx/camera/core/imagecapture/JpegBytes2CroppedBitmap.java:31`
  `throw new ImageCaptureException(1, "Failed to decode JPEG.", e);`
- `sources/androidx/camera/core/imagecapture/JpegBytes2Disk.java:68`
  `fileOutputStream.write(bArr, 0, new InvalidJpegDataParser().getValidDataLength(bArr));`
- `sources/androidx/camera/core/impl/CaptureConfig.java:31`
  `public interface OptionUnpacker {`
- `sources/androidx/camera/core/impl/CaptureConfig.java:32`
  `void unpack(UseCaseConfig<?> useCaseConfig, Builder builder);`
- `sources/androidx/camera/core/impl/utils/Exif.java:12`
  `import java.text.ParseException;`
- `sources/androidx/camera/core/impl/utils/ExifAttribute.java:163`
  `return Double.parseDouble((String) value);`
- `sources/androidx/camera/core/impl/utils/ExifAttribute.java:200`
  `return Integer.parseInt((String) value);`
- `sources/androidx/camera/core/impl/utils/ExifData.java:390`
  `long j3 = Long.parseLong(str);`
- `sources/androidx/camera/core/internal/compat/quirk/IncorrectJpegMetadataQuirk.java:30`
  `return (canParseSosMarker(bArr) || (iFindSecondFfd8Position = findSecondFfd8Position(bArr)) != -1) ? Arrays.copyOfRange(bArr, iFindSecondFfd8Position, buffer.limit()) : bArr;`
- `sources/androidx/camera/core/internal/compat/quirk/IncorrectJpegMetadataQuirk.java:33`
  `private boolean canParseSosMarker(byte[] bArr) {`
- `sources/androidx/camera/core/internal/compat/workaround/InvalidJpegDataParser.java:7`
  `public class InvalidJpegDataParser {`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:170`
  `BitmapRegionDecoder bitmapRegionDecoderNewInstance = BitmapRegionDecoder.newInstance(bArr, 0, bArr.length, false);`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:171`
  `Bitmap bitmapDecodeRegion = bitmapRegionDecoderNewInstance.decodeRegion(rect, new BitmapFactory.Options());`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:172`
  `bitmapRegionDecoderNewInstance.recycle();`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:173`
  `if (bitmapDecodeRegion == null) {`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:174`
  `throw new CodecFailedException("Decode byte array failed.", CodecFailedException.FailureType.DECODE_FAILED);`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:177`
  `if (!bitmapDecodeRegion.compress(Bitmap.CompressFormat.JPEG, i, byteArrayOutputStream)) {`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:180`
  `bitmapDecodeRegion.recycle();`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:183`
  `throw new CodecFailedException("Decode byte array failed.", CodecFailedException.FailureType.DECODE_FAILED);`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:185`
  `throw new CodecFailedException("Decode byte array failed with illegal argument." + e, CodecFailedException.FailureType.DECODE_FAILED);`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:260`
  `Bitmap bitmapDecodeByteArray = BitmapFactory.decodeByteArray(bArrJpegImageToJpegByteArray, 0, bArrJpegImageToJpegByteArray.length, null);`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:261`
  `if (bitmapDecodeByteArray != null) {`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:262`
  `return bitmapDecodeByteArray;`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:264`
  `throw new UnsupportedOperationException("Decode jpeg byte array failed");`
- `sources/androidx/compose/material3/CalendarModelImpl.java:13`
  `import java.time.format.DateTimeParseException;`
- `sources/androidx/compose/ui/graphics/vector/PathParserKt.java:12`
  `/* JADX INFO: compiled from: PathParser.kt */`
- `sources/androidx/compose/ui/graphics/vector/PathParserKt.java:15`
  `public final class PathParserKt {`
- `sources/androidx/compose/ui/graphics/vector/compat/XmlVectorParser_androidKt.java:29`
  `import org.xmlpull.v1.XmlPullParser;`
- `sources/androidx/compose/ui/graphics/vector/compat/XmlVectorParser_androidKt.java:30`
  `import org.xmlpull.v1.XmlPullParserException;`
- `sources/androidx/compose/ui/graphics/vector/compat/XmlVectorParser_androidKt.java:32`
  `/* JADX INFO: compiled from: XmlVectorParser.android.kt */`
- `sources/androidx/compose/ui/graphics/vector/compat/XmlVectorParser_androidKt.java:34`
  `@Metadata(d1 = {"\u0000\\\n\u0000\n\u0002\u0010\b\n\u0002\b\u0007\n\u0002\u0010\u000e\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\...`
- `sources/androidx/compose/ui/graphics/vector/compat/XmlVectorParser_androidKt.java:158`
  `Intrinsics.checkNotNullParameter(androidVectorParser, "<this>");`
- `sources/androidx/compose/ui/graphics/vector/compat/XmlVectorParser_androidKt.java:161`
  `TypedArray typedArrayObtainAttributes = androidVectorParser.obtainAttributes(res, theme, attrs, AndroidVectorResources.INSTANCE.getSTYLEABLE_VECTOR_DRAWABLE_TYPE_ARRAY());`
- `sources/androidx/compose/ui/graphics/vector/compat/XmlVectorParser_androidKt.java:162`
  `boolean namedBoolean = androidVectorParser.getNamedBoolean(typedArrayObtainAttributes, "autoMirrored", AndroidVectorResources.INSTANCE.getSTYLEABLE_VECTOR_DRAWABLE_AUTO_MIRRORED(), false);`
- `sources/androidx/compose/ui/graphics/vector/compat/XmlVectorParser_androidKt.java:163`
  `float namedFloat = androidVectorParser.getNamedFloat(typedArrayObtainAttributes, "viewportWidth", AndroidVectorResources.INSTANCE.getSTYLEABLE_VECTOR_DRAWABLE_VIEWPORT_WIDTH(), 0.0f);`
- `sources/androidx/compose/ui/graphics/vector/compat/XmlVectorParser_androidKt.java:164`
  `float namedFloat2 = androidVectorParser.getNamedFloat(typedArrayObtainAttributes, "viewportHeight", AndroidVectorResources.INSTANCE.getSTYLEABLE_VECTOR_DRAWABLE_VIEWPORT_HEIGHT(), 0.0f);`
- `sources/androidx/compose/ui/graphics/vector/compat/XmlVectorParser_androidKt.java:166`
  `throw new XmlPullParserException(typedArrayObtainAttributes.getPositionDescription() + "<VectorGraphic> tag requires viewportWidth > 0");`
- `sources/androidx/compose/ui/graphics/vector/compat/XmlVectorParser_androidKt.java:169`
  `throw new XmlPullParserException(typedArrayObtainAttributes.getPositionDescription() + "<VectorGraphic> tag requires viewportHeight > 0");`
- `sources/androidx/compose/ui/graphics/vector/compat/XmlVectorParser_androidKt.java:171`
  `float dimension = androidVectorParser.getDimension(typedArrayObtainAttributes, AndroidVectorResources.INSTANCE.getSTYLEABLE_VECTOR_DRAWABLE_WIDTH(), 0.0f);`
- `sources/androidx/compose/ui/graphics/vector/compat/XmlVectorParser_androidKt.java:172`
  `float dimension2 = androidVectorParser.getDimension(typedArrayObtainAttributes, AndroidVectorResources.INSTANCE.getSTYLEABLE_VECTOR_DRAWABLE_HEIGHT(), 0.0f);`
- `sources/androidx/compose/ui/graphics/vector/compat/XmlVectorParser_androidKt.java:176`
  `if (typedValue.type != 2 && (namedColorStateList = androidVectorParser.getNamedColorStateList(typedArrayObtainAttributes, theme, "tint", AndroidVectorResources.INSTANCE.getSTYLEABLE_VECTOR_DRAWABLE_TINT())) != null) {`
- `sources/androidx/compose/ui/graphics/vector/compat/XmlVectorParser_androidKt.java:268`
  `String string = androidVectorParser.getString(typedArrayObtainAttributes, AndroidVectorResources.INSTANCE.getSTYLEABLE_VECTOR_DRAWABLE_CLIP_PATH_NAME());`
- `sources/androidx/compose/ui/graphics/vector/compat/XmlVectorParser_androidKt.java:272`
  `List<PathNode> listAddPathNodes = VectorKt.addPathNodes(androidVectorParser.getString(typedArrayObtainAttributes, AndroidVectorResources.INSTANCE.getSTYLEABLE_VECTOR_DRAWABLE_CLIP_PATH_PATH_DATA()));`
- `sources/androidx/compose/ui/graphics/vector/compat/XmlVectorParser_androidKt.java:277`
  `public static final void parseGroup(AndroidVectorParser androidVectorParser, Resources res, Resources.Theme theme, AttributeSet attrs, ImageVector.Builder builder) {`
- `sources/androidx/compose/ui/graphics/vector/compat/XmlVectorParser_androidKt.java:278`
  `Intrinsics.checkNotNullParameter(androidVectorParser, "<this>");`
- `sources/androidx/compose/ui/graphics/vector/compat/XmlVectorParser_androidKt.java:289`
  `float namedFloat5 = androidVectorParser.getNamedFloat(typedArrayObtainAttributes, "translateY", AndroidVectorResources.INSTANCE.getSTYLEABLE_VECTOR_DRAWABLE_GROUP_TRANSLATE_Y(), 0.0f);`
- `sources/androidx/compose/ui/graphics/vector/compat/XmlVectorParser_androidKt.java:290`
  `String string = androidVectorParser.getString(typedArrayObtainAttributes, AndroidVectorResources.INSTANCE.getSTYLEABLE_VECTOR_DRAWABLE_GROUP_NAME());`
- `sources/androidx/compose/ui/input/pointer/MotionEventAdapter.java:14`
  `@Metadata(d1 = {"\u0000^\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010\t\n\u0000\n\u0002\u0010!\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\...`
- `sources/androidx/compose/ui/input/pointer/MotionEventAdapter.java:17`
  `private final SparseLongArray motionEventToComposePointerIdMap = new SparseLongArray();`
- `sources/androidx/compose/ui/input/pointer/MotionEventAdapter.java:18`
  `private final SparseBooleanArray canHover = new SparseBooleanArray();`
- `sources/androidx/compose/ui/node/LayoutNode.java:52`
  `@Metadata(d1 = {"\u0000Ì\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u00...`
- `sources/androidx/compose/ui/node/LayoutNodeLayoutDelegate.java:213`
  `@Metadata(d1 = {"\u0000\u0094\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010 \n\u0002\b\u0003\n\u0002\u0010\u000b\n\u0002\b\b\n\u0002\u0018\u0002\n...`
- `sources/androidx/compose/ui/node/LayoutNodeLayoutDelegate.java:986`
  `@Metadata(d1 = {"\u0000\u009e\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010 \n\u0002\b\u0003\n\u0002\u0010\u000b\n\u0002\b\b\n\u0002\u0018\u0002\n...`
- `sources/androidx/compose/ui/node/LookaheadDelegate.java:28`
  `@Metadata(d1 = {"\u0000¢\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010%\n\u0002\u0018\u0002\n\u0002\u0010\b\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u000...`
- `sources/androidx/compose/ui/node/NodeCoordinator.java:53`
  `@Metadata(d1 = {"\u0000\u0094\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0...`

## BR074

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/android/support/v4/media/session/MediaControllerCompat.java:1555`
  `synchronized (mediaControllerImplApi21.mLock) {`
- `sources/android/support/v4/os/ResultReceiver.java:93`
  `synchronized (this) {`
- `sources/androidx/activity/ComponentActivity.java:74`
  `public class ComponentActivity extends androidx.core.app.ComponentActivity implements ContextAware, LifecycleOwner, ViewModelStoreOwner, HasDefaultViewModelProviderFactory, SavedStateRegistryOwner, OnBackPressedDispatcherOwner, ActivityResultRegistryOwner, ActivityResultCaller, OnConfigurationChange...`
- `sources/androidx/activity/ComponentActivity.java:82`
  `final FullyDrawnReporter mFullyDrawnReporter;`
- `sources/androidx/activity/ComponentActivity.java:147`
  `final ActivityResultContract.SynchronousResult<O> synchronousResult = activityResultContract.getSynchronousResult(componentActivity, i2);`
- `sources/androidx/activity/ComponentActivity.java:148`
  `if (synchronousResult != null) {`
- `sources/androidx/activity/ComponentActivity.java:152`
  `dispatchResult(i, synchronousResult.getValue());`
- `sources/androidx/activity/ComponentActivity.java:235`
  `savedStateRegistryControllerCreate.performAttach();`
- `sources/androidx/activity/ComponentActivity.java:236`
  `SavedStateHandleSupport.enableSavedStateHandles(this);`
- `sources/androidx/activity/ComponentActivity.java:240`
  `getSavedStateRegistry().registerSavedStateProvider(ACTIVITY_RESULT_TAG, new SavedStateRegistry.SavedStateProvider() { // from class: androidx.activity.ComponentActivity$$ExternalSyntheticLambda2`
- `sources/androidx/activity/ComponentActivity.java:241`
  `@Override // androidx.savedstate.SavedStateRegistry.SavedStateProvider`
- `sources/androidx/activity/ComponentActivity.java:242`
  `public final Bundle saveState() {`
- `sources/androidx/activity/ComponentActivity.java:257`
  `this.mActivityResultRegistry.onSaveInstanceState(bundle);`
- `sources/androidx/activity/ComponentActivity.java:263`
  `Bundle bundleConsumeRestoredStateForKey = getSavedStateRegistry().consumeRestoredStateForKey(ACTIVITY_RESULT_TAG);`
- `sources/androidx/activity/ComponentActivity.java:501`
  `if (!TextUtils.equals(e.getMessage(), "Can not perform this action after onSaveInstanceState")) {`
- `sources/androidx/activity/ComponentActivity.java:530`
  `public FullyDrawnReporter getFullyDrawnReporter() {`
- `sources/androidx/activity/ComponentActivity.java:531`
  `return this.mFullyDrawnReporter;`
- `sources/androidx/activity/FullyDrawnReporterKt.java:17`
  `/* JADX INFO: compiled from: FullyDrawnReporter.kt */`
- `sources/androidx/activity/FullyDrawnReporterKt.java:19`
  `@DebugMetadata(c = "androidx.activity.FullyDrawnReporterKt", f = "FullyDrawnReporter.kt", i = {0}, l = {185}, m = "reportWhenComplete", n = {"$this$reportWhenComplete"}, s = {"L$0"})`
- `sources/androidx/activity/FullyDrawnReporterKt.java:33`
  `return FullyDrawnReporterKt.reportWhenComplete(null, null, this);`
- `sources/androidx/activity/FullyDrawnReporterKt.java:59`
  `androidx.activity.FullyDrawnReporterKt$reportWhenComplete$1 r0 = new androidx.activity.FullyDrawnReporterKt$reportWhenComplete$1`
- `sources/androidx/activity/FullyDrawnReporterKt.java:69`
  `androidx.activity.FullyDrawnReporter r4 = (androidx.activity.FullyDrawnReporter) r4`
- `sources/androidx/activity/FullyDrawnReporterKt.java:79`
  `r4.addReporter()`
- `sources/androidx/activity/FullyDrawnReporterKt.java:80`
  `boolean r6 = r4.isFullyDrawnReported()`
- `sources/androidx/activity/compose/ActivityResultRegistryKt.java:16`
  `import androidx.compose.runtime.saveable.RememberSaveableKt;`
- `sources/androidx/activity/compose/ActivityResultRegistryKt.java:17`
  `import androidx.compose.runtime.saveable.Saver;`
- `sources/androidx/activity/compose/ActivityResultRegistryKt.java:34`
  `String str = (String) RememberSaveableKt.m2965rememberSaveable(new Object[0], (Saver) null, (String) null, (Function0) new Function0<String>() { // from class: androidx.activity.compose.ActivityResultRegistryKt$rememberLauncherForActivityResult$key$1`
- `sources/androidx/activity/compose/ReportDrawnKt.java:3`
  `import androidx.activity.FullyDrawnReporter;`
- `sources/androidx/activity/compose/ReportDrawnKt.java:4`
  `import androidx.activity.FullyDrawnReporterOwner;`
- `sources/androidx/activity/compose/ReportDrawnKt.java:57`
  `ReportDrawnKt.ReportDrawnWhen(function0, composer2, i | 1);`
- `sources/androidx/activity/compose/ReportDrawnKt.java:62`
  `EffectsKt.DisposableEffect(fullyDrawnReporter, function0, new Function1<DisposableEffectScope, DisposableEffectResult>() { // from class: androidx.activity.compose.ReportDrawnKt.ReportDrawnWhen.1`
- `sources/androidx/activity/compose/ReportDrawnKt.java:70`
  `if (!fullyDrawnReporter.isFullyDrawnReported()) {`
- `sources/androidx/activity/compose/ReportDrawnKt.java:71`
  `final ReportDrawnComposition reportDrawnComposition = new ReportDrawnComposition(fullyDrawnReporter, function0);`
- `sources/androidx/activity/compose/ReportDrawnKt.java:72`
  `return new DisposableEffectResult() { // from class: androidx.activity.compose.ReportDrawnKt$ReportDrawnWhen$1$invoke$$inlined$onDispose$2`
- `sources/androidx/activity/compose/ReportDrawnKt.java:75`
  `reportDrawnComposition.removeReporter();`
- `sources/androidx/activity/compose/ReportDrawnKt.java:79`
  `return new DisposableEffectResult() { // from class: androidx.activity.compose.ReportDrawnKt$ReportDrawnWhen$1$invoke$$inlined$onDispose$1`
- `sources/androidx/activity/compose/ReportDrawnKt.java:230`
  `FullyDrawnReporter fullyDrawnReporter;`
- `sources/androidx/activity/compose/ReportDrawnKt.java:236`
  `FullyDrawnReporter fullyDrawnReporter2 = this.$fullyDrawnReporter;`
- `sources/androidx/activity/compose/ReportDrawnKt.java:238`
  `fullyDrawnReporter2.addReporter();`
- `sources/androidx/activity/compose/ReportDrawnKt.java:239`
  `if (!fullyDrawnReporter2.isFullyDrawnReported()) {`
- `sources/androidx/activity/compose/ReportDrawnKt.java:241`
  `this.L$0 = fullyDrawnReporter2;`
- `sources/androidx/activity/compose/ReportDrawnKt.java:259`
  `fullyDrawnReporter = (FullyDrawnReporter) this.L$0;`
- `sources/androidx/activity/compose/ReportDrawnKt.java:262`
  `fullyDrawnReporter.removeReporter();`
- `sources/androidx/activity/compose/ReportDrawnKt.java:265`
  `fullyDrawnReporter.removeReporter();`
- `sources/androidx/activity/result/ActivityResultRegistry.java:162`
  `public final void onSaveInstanceState(Bundle bundle) {`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:12`
  `@Metadata(d1 = {"\u0000.\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\b\u0004\b&\u0018\u0000*\u0004\b\u0000\u0010\u0001*\u0004\b\u0001\u0010\u00022\u...`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:16`
  `public SynchronousResult<O> getSynchronousResult(Context context, I input) {`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:24`
  `@Metadata(d1 = {"\u0000\u000e\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0000\n\u0002\b\u0006\u0018\u0000*\u0004\b\u0002\u0010\u00012\u00020\u0002B\r\u0012\u0006\u0010\u0003\u001a\u00028\u0002¢\u0006\u0002\u0010\u0004R\u0013\u0010\u0003\u001a\u00028\u0002¢\u0006\n\n\u0002\u0010\u0007\u001a\u0004\b\u...`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:25`
  `public static final class SynchronousResult<T> {`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:28`
  `public SynchronousResult(T t) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:88`
  `@Metadata(d1 = {"\u0000>\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0011\n\u0002\u0010\u000e\n\u0002\u0010$\n\u0002\u0010\u000b\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:123`
  `public ActivityResultContract.SynchronousResult<Map<String, Boolean>> getSynchronousResult(Context context, String[] input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:127`
  `return new ActivityResultContract.SynchronousResult<>(MapsKt.emptyMap());`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:139`
  `return new ActivityResultContract.SynchronousResult<>(linkedHashMap);`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:164`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\u0018\u00002\u000e\u0012\u0004\u0012\u00020\u00...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:199`
  `public ActivityResultContract.SynchronousResult<Boolean> getSynchronousResult(Context context, String input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:203`
  `return new ActivityResultContract.SynchronousResult<>(true);`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:210`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0016\u0018\u00002\u0012\u0012\u0006\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:213`
  `public final ActivityResultContract.SynchronousResult<Bitmap> getSynchronousResult(Context context, Void input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:238`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\b\u0016\u0018\u00002\u000e\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:241`
  `public final ActivityResultContract.SynchronousResult<Boolean> getSynchronousResult(Context context, Uri input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:264`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0017\u0018\u00002\u0010\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:268`
  `public final ActivityResultContract.SynchronousResult<Bitmap> getSynchronousResult(Context context, Uri input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:297`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\b\u0016\u0018\u00002\u000e\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:300`
  `public final ActivityResultContract.SynchronousResult<Boolean> getSynchronousResult(Context context, Uri input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:347`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0016\u0018\u00002\u0010\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:350`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(Context context, String input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:379`
  `@Metadata(d1 = {"\u0000:\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\b\u0017\u001...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:386`
  `public final ActivityResultContract.SynchronousResult<List<Uri>> getSynchronousResult(Context context, String input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:446`
  `@Metadata(d1 = {"\u00006\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0011\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\b\u0002\b\u0017\u0018\u00002\u0016\...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:449`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(Context context, String[] input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:478`
  `@Metadata(d1 = {"\u0000>\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0011\n\u0002\u0010\u000e\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:481`
  `public final ActivityResultContract.SynchronousResult<List<Uri>> getSynchronousResult(Context context, String[] input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:507`
  `@Metadata(d1 = {"\u0000.\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0017\u0018\u00002\u0012\u0012\u0006\u0012\u0004\u0018\u00010\u00...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:510`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(Context context, Uri input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:539`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0017\u0018\u00002\u0010\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:544`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(Context context, String input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:583`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\b\b\u0017\u0018\u0000 \u00102\u0010\u0012\u0004\u0012...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:610`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(Context context, PickVisualMediaRequest input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:796`
  `@Metadata(d1 = {"\u00008\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\b\u0017\u0018\u0000 ...`

## BR075

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/androidx/appcompat/R.java:1205`
  `public static int AppCompatTextView_autoSizePresetSizes = 0x00000003;`
- `sources/androidx/appcompat/R.java:1543`
  `public static int[] AppCompatTextView = {android.R.attr.textAppearance, egnc.moh.bruhealth.R.attr.autoSizeMaxTextSize, egnc.moh.bruhealth.R.attr.autoSizeMinTextSize, egnc.moh.bruhealth.R.attr.autoSizePresetSizes, egnc.moh.bruhealth.R.attr.autoSizeStepGranularity, egnc.moh.bruhealth.R.attr.autoSizeTe...`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:233`
  `resetGroup();`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:236`
  `public void resetGroup() {`
- `sources/androidx/appcompat/view/menu/MenuItemImpl.java:611`
  `actionProvider2.reset();`
- `sources/androidx/appcompat/widget/AppCompatButton.java:187`
  `public void setAutoSizeTextTypeUniformWithPresetSizes(int[] iArr, int i) throws IllegalArgumentException {`
- `sources/androidx/appcompat/widget/AppCompatButton.java:189`
  `super.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatButton.java:194`
  `appCompatTextHelper.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:183`
  `Api26Impl.setAutoSizeTextTypeUniformWithPresetSizes(this.mView, autoSizeTextAvailableSizes, 0);`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:52`
  `void setAutoSizeTextTypeUniformWithPresetSizes(int[] iArr, int i);`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:244`
  `public void setAutoSizeTextTypeUniformWithPresetSizes(int[] iArr, int i) throws IllegalArgumentException {`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:246`
  `getSuperCaller().setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:251`
  `appCompatTextHelper.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:50`
  `private boolean mHasPresetAutoSizeValues = false;`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:112`
  `if (typedArrayObtainStyledAttributes.hasValue(R.styleable.AppCompatTextView_autoSizePresetSizes) && (resourceId = typedArrayObtainStyledAttributes.getResourceId(R.styleable.AppCompatTextView_autoSizePresetSizes, 0)) > 0) {`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:114`
  `setupAutoSizeUniformPresetSizes(typedArrayObtainTypedArray);`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:120`
  `if (!this.mHasPresetAutoSizeValues) {`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:216`
  `private void setupAutoSizeUniformPresetSizes(TypedArray typedArray) {`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:288`
  `this.mAutoSizeTextSizesInPx = cleanupAutoSizePresetSizes(iArr);`
- `sources/androidx/biometric/FingerprintDialogFragment.java:43`
  `final Runnable mResetDialogRunnable = new Runnable() { // from class: androidx.biometric.FingerprintDialogFragment.1`
- `sources/androidx/biometric/FingerprintDialogFragment.java:46`
  `FingerprintDialogFragment.this.resetDialog();`
- `sources/androidx/biometric/FingerprintDialogFragment.java:155`
  `FingerprintDialogFragment.this.mHandler.removeCallbacks(FingerprintDialogFragment.this.mResetDialogRunnable);`
- `sources/androidx/biometric/FingerprintDialogFragment.java:158`
  `FingerprintDialogFragment.this.mHandler.postDelayed(FingerprintDialogFragment.this.mResetDialogRunnable, ExoPlayer.DEFAULT_DETACH_SURFACE_TIMEOUT_MS);`
- `sources/androidx/biometric/FingerprintDialogFragment.java:164`
  `FingerprintDialogFragment.this.mHandler.removeCallbacks(FingerprintDialogFragment.this.mResetDialogRunnable);`
- `sources/androidx/biometric/FingerprintDialogFragment.java:166`
  `FingerprintDialogFragment.this.mHandler.postDelayed(FingerprintDialogFragment.this.mResetDialogRunnable, ExoPlayer.DEFAULT_DETACH_SURFACE_TIMEOUT_MS);`
- `sources/androidx/biometric/R.java:1368`
  `public static int AppCompatTextView_autoSizePresetSizes = 0x00000003;`
- `sources/androidx/biometric/R.java:1752`
  `public static int[] AppCompatTextView = {android.R.attr.textAppearance, egnc.moh.bruhealth.R.attr.autoSizeMaxTextSize, egnc.moh.bruhealth.R.attr.autoSizeMinTextSize, egnc.moh.bruhealth.R.attr.autoSizePresetSizes, egnc.moh.bruhealth.R.attr.autoSizeStepGranularity, egnc.moh.bruhealth.R.attr.autoSizeTe...`
- `sources/androidx/biometric/ktx/R.java:1368`
  `public static int AppCompatTextView_autoSizePresetSizes = 0x00000003;`
- `sources/androidx/biometric/ktx/R.java:1752`
  `public static int[] AppCompatTextView = {android.R.attr.textAppearance, egnc.moh.bruhealth.R.attr.autoSizeMaxTextSize, egnc.moh.bruhealth.R.attr.autoSizeMinTextSize, egnc.moh.bruhealth.R.attr.autoSizePresetSizes, egnc.moh.bruhealth.R.attr.autoSizeStepGranularity, egnc.moh.bruhealth.R.attr.autoSizeTe...`
- `sources/androidx/camera/camera2/internal/Camera2CameraControlImpl.java:221`
  `this.mVideoUsageControl.resetDirectly();`
- `sources/androidx/camera/camera2/internal/Camera2CameraControlImpl.java:413`
  `void resetTemplate() {`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:490`
  `resetCaptureSession(z);`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:683`
  `public void onUseCaseReset(UseCase useCase) {`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:686`
  `resetUseCase(getUseCaseId(useCase), sessionConfig, useCase.getCurrentConfig(), useCase.getAttachedStreamSpec(), getCaptureTypes(useCase));`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:689`
  `private void resetUseCase(final String str, final SessionConfig sessionConfig, final UseCaseConfig<?> useCaseConfig, final StreamSpec streamSpec, final List<UseCaseConfigFactory.CaptureType> list) {`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:698`
  `/* JADX INFO: renamed from: lambda$resetUseCase$10$androidx-camera-camera2-internal-Camera2CameraImpl, reason: not valid java name */`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:700`
  `debugLog("Use case " + str + " RESET");`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:703`
  `resetCaptureSession(false);`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:842`
  `resetCaptureSession(false);`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:945`
  `resetCaptureSession(false);`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:952`
  `resetCaptureSession(false);`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1010`
  `resetUseCase(getMeteringRepeatingId(this.mMeteringRepeatingSession), this.mMeteringRepeatingSession.getSessionConfig(), this.mMeteringRepeatingSession.getUseCaseConfig(), null, Collections.singletonList(UseCaseConfigFactory.CaptureType.METERING_REPEATING));`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1121`
  `this.mStateCallback.resetReopenMonitor();`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1237`
  `this.mCameraControlInternal.resetTemplate();`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1282`
  `Camera2CameraImpl.this.resetCaptureSession(false);`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1306`
  `errorListener.onError(sessionConfig, SessionConfig.SessionError.SESSION_ERROR_SURFACE_NEEDS_RESET);`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1312`
  `void resetCaptureSession(boolean z) {`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1314`
  `debugLog("Resetting Capture Session");`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1677`
  `void resetReopenMonitor() {`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1678`
  `this.mCameraReopenMonitor.reset();`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1772`
  `reset();`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1776`
  `void reset() {`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:27`
  `import androidx.camera.camera2.internal.compat.workaround.TorchStateReset;`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:76`
  `private final TorchStateReset mTorchStateReset;`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:109`
  `this.mTorchStateReset = new TorchStateReset();`
- `sources/androidx/camera/camera2/internal/MeteringRepeatingSession.java:40`
  `private final SurfaceResetCallback mSurfaceResetCallback;`
- `sources/androidx/camera/camera2/internal/MeteringRepeatingSession.java:45`
  `interface SurfaceResetCallback {`
- `sources/androidx/camera/camera2/internal/MeteringRepeatingSession.java:46`
  `void onSurfaceReset();`
- `sources/androidx/camera/camera2/internal/MeteringRepeatingSession.java:49`
  `MeteringRepeatingSession(CameraCharacteristicsCompat cameraCharacteristicsCompat, DisplayInfoManager displayInfoManager, SurfaceResetCallback surfaceResetCallback) {`
- `sources/androidx/camera/camera2/internal/MeteringRepeatingSession.java:50`
  `this.mSurfaceResetCallback = surfaceResetCallback;`
- `sources/androidx/camera/camera2/internal/MeteringRepeatingSession.java:96`
  `SurfaceResetCallback surfaceResetCallback = this.mSurfaceResetCallback;`
- `sources/androidx/camera/camera2/internal/MeteringRepeatingSession.java:97`
  `if (surfaceResetCallback != null) {`
- `sources/androidx/camera/camera2/internal/MeteringRepeatingSession.java:98`
  `surfaceResetCallback.onSurfaceReset();`
- `sources/androidx/camera/camera2/internal/StreamUseCaseUtil.java:125`
  `public static boolean shouldUseStreamUseCase(SupportedSurfaceCombination.FeatureSettings featureSettings) {`
- `sources/androidx/camera/camera2/internal/StreamUseCaseUtil.java:126`
  `return featureSettings.getCameraMode() == 0 && featureSettings.getRequiredMaxBitDepth() == 8;`
- `sources/androidx/camera/camera2/internal/SupportedSurfaceCombination.java:355`
  `Map<UseCaseConfig<?>, List<Size>> mapFilterSupportedSizes = filterSupportedSizes(map, featureSettingsCreateFeatureSettings, targetFpsRange);`
- `sources/androidx/camera/camera2/internal/SupportedSurfaceCombination.java:414`
  `orderedSupportedStreamUseCaseSurfaceConfigList = getOrderedSupportedStreamUseCaseSurfaceConfigList(featureSettingsCreateFeatureSettings, (List) getSurfaceConfigListAndFpsCeiling(i, list, it3.next(), arrayList, list6, i6, map16, map15).first);`
- `sources/androidx/camera/camera2/internal/SupportedSurfaceCombination.java:592`
  `private boolean isUseCasesCombinationSupported(FeatureSettings featureSettings, List<AttachedSurfaceInfo> list, Map<UseCaseConfig<?>, List<Size>> map) {`
- `sources/androidx/camera/camera2/internal/SupportedSurfaceCombination.java:604`
  `arrayList.add(SurfaceConfig.transformSurfaceConfig(featureSettings.getCameraMode(), inputFormat, size, getUpdatedSurfaceSizeDefinitionByFormat(inputFormat)));`
- `sources/androidx/camera/camera2/internal/SupportedSurfaceCombination.java:606`
  `return checkSupported(featureSettings, arrayList);`
- `sources/androidx/camera/camera2/internal/SynchronizedCaptureSessionImpl.java:15`
  `import androidx.camera.camera2.internal.compat.workaround.SessionResetPolicy;`
- `sources/androidx/camera/camera2/internal/SynchronizedCaptureSessionImpl.java:42`
  `private final SessionResetPolicy mSessionResetPolicy;`
- `sources/androidx/camera/camera2/internal/SynchronizedCaptureSessionImpl.java:51`
  `this.mSessionResetPolicy = new SessionResetPolicy(quirks2);`
- `sources/androidx/camera/camera2/internal/SynchronizedCaptureSessionImpl.java:79`
  `if (this.mSessionResetPolicy.needAbortCapture()) {`
- `sources/androidx/camera/camera2/internal/SynchronizedCaptureSessionImpl.java:157`
  `if (this.mSessionResetPolicy.needAbortCapture()) {`
- `sources/androidx/camera/camera2/internal/VideoUsageControl.java:58`
  `public static final void reset$lambda$2(VideoUsageControl this$0) {`
- `sources/androidx/camera/camera2/internal/VideoUsageControl.java:60`
  `this$0.resetDirectly();`
- `sources/androidx/camera/camera2/internal/VideoUsageControl.java:63`
  `public final void reset() {`
- `sources/androidx/camera/camera2/internal/VideoUsageControl.java:67`
  `VideoUsageControl.reset$lambda$2(this.f$0);`
- `sources/androidx/camera/camera2/internal/VideoUsageControl.java:72`
  `public final void resetDirectly() {`

## BR076

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `resources/AndroidManifest.xml:83`
  `<uses-feature`
- `resources/AndroidManifest.xml:91`
  `<uses-feature`
- `resources/AndroidManifest.xml:94`
  `<uses-feature`
- `resources/AndroidManifest.xml:109`
  `<uses-feature android:name="android.hardware.camera.autofocus"/>`
- `resources/AndroidManifest.xml:110`
  `<uses-feature`
- `resources/AndroidManifest.xml:116`
  `<uses-feature`
- `resources/AndroidManifest.xml:119`
  `<uses-feature`
- `resources/AndroidManifest.xml:123`
  `<uses-feature`
- `resources/AndroidManifest.xml:137`
  `<uses-permission android:name="com.oplus.ocs.permission.third"/>`
- `resources/AndroidManifest.xml:230`
  `android:name="egnc.moh.bruhealth.login.activities.InformationActivity"`
- `resources/AndroidManifest.xml:262`
  `android:name="egnc.moh.bruhealth.login.activities.AccountConfirmActivity"`
- `resources/AndroidManifest.xml:265`
  `android:name="egnc.moh.bruhealth.login.activities.RegisterActivity"`
- `resources/AndroidManifest.xml:268`
  `android:name="egnc.moh.bruhealth.login.activities.MemberAddActivity"`
- `resources/AndroidManifest.xml:271`
  `android:name="egnc.moh.bruhealth.login.activities.NewbornParentVerifyActivity"`
- `resources/AndroidManifest.xml:274`
  `android:name="egnc.moh.bruhealth.login.activities.PasswordEnterActivity"`
- `resources/AndroidManifest.xml:278`
  `android:name="egnc.moh.bruhealth.login.activities.ParentPasswordEnterActivity"`
- `resources/AndroidManifest.xml:287`
  `android:name="egnc.moh.bruhealth.login.activities.BiometricRecognizeAuthenticationActivity"`
- `resources/AndroidManifest.xml:291`
  `android:name="egnc.moh.bruhealth.login.activities.SystemAuthActivity"`
- `resources/AndroidManifest.xml:298`
  `android:name="egnc.moh.bruhealth.login.activities.InspectBiometricAuthActivity"`
- `resources/assets/flutter_assets/config/language/en.json:24`
  `"biometric_id_enable": "Enable Biometric ID Login",`
- `resources/assets/flutter_assets/config/language/en.json:46`
  `"face_id_enable": "Enable Face ID Login",`
- `resources/assets/flutter_assets/config/language/en.json:82`
  `"login": "Login",`
- `resources/assets/flutter_assets/config/language/en.json:83`
  `"login_agree_policy": "Please agree to our User Agreement and Privacy Policy first.",`
- `resources/assets/flutter_assets/config/language/en.json:86`
  `"login_last_login_used": "Last Login Used",`
- `resources/assets/flutter_assets/config/language/en.json:89`
  `"login_method_pwd": "Password login",`
- `resources/assets/flutter_assets/config/language/en.json:102`
  `"login_password_input_tips": "Please enter your personal BruHealth password to login and sync your personal data.",`
- `resources/assets/flutter_assets/config/language/en.json:115`
  `"login_register_id_select_page_tips": "Your mobile number has not been used for logging in before. Kindly provide your ID information to proceed.",`
- `resources/assets/flutter_assets/config/language/en.json:125`
  `"login_switch_title": "Login",`
- `resources/assets/flutter_assets/config/language/en.json:128`
  `"login_switch_to_login": "Login with ",`
- `resources/assets/flutter_assets/config/language/en.json:129`
  `"login_switch_to_login_sms_code_1": "To login with existing linked number ",`
- `resources/assets/flutter_assets/config/language/en.json:131`
  `"login_switch_to_login_verification_code_1": "To login with existing linked number ",`
- `resources/assets/flutter_assets/config/language/en.json:160`
  `"login_tap_to_login": "Tap Below to Login",`
- `resources/assets/flutter_assets/config/language/en.json:167`
  `"login_verity_personal_account_page_proceed_to_login": "Yes, proceed to login",`
- `resources/assets/flutter_assets/config/language/en.json:170`
  `"login_width_code": "Login via Verification Code",`
- `resources/assets/flutter_assets/config/language/en.json:171`
  `"login_width_password": "Login With Password",`
- `resources/assets/flutter_assets/config/language/en.json:172`
  `"login_with_biometricid": "Login with Biometric ID",`
- `resources/assets/flutter_assets/config/language/en.json:173`
  `"login_with_faceid": "Login with Face ID",`
- `resources/assets/flutter_assets/config/language/en.json:174`
  `"login_with_touchid": "Login with Touch ID",`
- `resources/assets/flutter_assets/config/language/en.json:259`
  `"other_login_options": "Other Login Options",`
- `resources/assets/flutter_assets/config/language/en.json:299`
  `"password_reset_success_content": "Please use the new password when you login.",`
- `resources/assets/flutter_assets/config/language/en.json:307`
  `"registration_input_tips": "Your mobile number has not been used for logging in before. Kindly provide your ID information first.",`
- `resources/assets/flutter_assets/config/language/en.json:344`
  `"touch_id_enable": "Enable Touch ID Login",`
- `resources/assets/flutter_assets/config/language/en.json:601`
  `"my_health_empty_description": "Great to see you taking the first step in customizing your Routines Plan! By setting goals today, you'll be creating a roadmap for a healthier life. As a bonus, [value] is excited to start exercising with you!",`
- `resources/assets/flutter_assets/config/language/en.json:773`
  `"alert_success_newborn_set_pwd_content": "Please use the new password when you login.",`
- `resources/assets/flutter_assets/config/language/en.json:809`
  `"other_login_button_title": "Other Login",`
- `resources/assets/flutter_assets/config/language/en.json:830`
  `"login_method_list_dialog_title_login": "Login Options",`
- `resources/assets/flutter_assets/config/language/en.json:836`
  `"login_pwd_not_usable_toast": "Password login is not available. Please authenticate your account first."`
- `resources/assets/html/apache-license.txt:115`
  `wherever such third-party notices normally appear. The contents`
- `resources/assets/html/apache-license.txt:139`
  `names, trademarks, service marks, or product names of the Licensor,`
- `resources/assets/html/apache-license.txt:187`
  `identification within third-party archives.`
- `resources/org/mozilla/javascript/resources/Messages.properties:161`
  `The choice of Java method {0}.{1} matching JavaScript argument types ({2}) is ambiguous; \`
- `resources/org/mozilla/javascript/resources/Messages.properties:165`
  `The choice of Java constructor {0} matching JavaScript argument types ({1}) is ambiguous; \`
- `resources/org/mozilla/javascript/resources/Messages.properties:177`
  `different names`
- `resources/org/mozilla/javascript/resources/Messages.properties:233`
  `Only one argument may be specified if the first argument to \`
- `resources/org/mozilla/javascript/resources/Messages.properties:292`
  `missing ( before function parameters.`
- `resources/org/mozilla/javascript/resources/Messages.properties:301`
  `missing '{' before function body`
- `resources/org/mozilla/javascript/resources/Messages.properties:307`
  `missing ( before condition`
- `resources/org/mozilla/javascript/resources/Messages.properties:313`
  `missing ; before statement`
- `resources/org/mozilla/javascript/resources/Messages.properties:334`
  `missing ( before switch expression`
- `resources/org/mozilla/javascript/resources/Messages.properties:340`
  `missing '{' before switch body`
- `resources/org/mozilla/javascript/resources/Messages.properties:370`
  `missing ( before with-statement object`
- `resources/org/mozilla/javascript/resources/Messages.properties:427`
  `missing ( before catch-block condition`
- `resources/org/mozilla/javascript/resources/Messages.properties:436`
  `missing '{' before try block`
- `resources/org/mozilla/javascript/resources/Messages.properties:439`
  `missing '{' before catch-block body`
- `resources/org/mozilla/javascript/resources/Messages.properties:648`
  `Two-parameter setter must take a ScriptableObject as its first parameter.`
- `resources/org/mozilla/javascript/resources/Messages.properties:744`
  `msg.java.internal.field.type =\`
- `resources/org/mozilla/javascript/resources/Messages.properties:754`
  `Internal error: attempt to access private/protected field "{0}".`
- `resources/org/mozilla/javascript/resources/Messages.properties:766`
  `Java class "{0}" has no public instance field or method named "{1}".`
- `resources/org/mozilla/javascript/resources/Messages.properties:775`
  `Java package names may not be numbers.`
- `resources/org/mozilla/javascript/tools/resources/Messages.properties:133`
  `\                       implementation. The class must have a method matching\n\`
- `resources/org/mozilla/javascript/tools/resources/Messages.properties:173`
  `The first argument to runCommand must be a command name.`
- `resources/res/values/strings.xml:37`
  `<string name="agree_policy">Please agree to our User Agreement and Privacy Policy first.</string>`
- `resources/res/values/strings.xml:40`
  `<string name="alert_not_auth_tips">To continue, please authenticate the parent’s identity first.</string>`
- `resources/res/values/strings.xml:46`
  `<string name="auth_choose_desc">To change linked mobile phone number to %s, please authenticate first.</string>`
- `resources/res/values/strings.xml:121`
  `<string name="camera_take_birth_tips">Please align the two upper corners of the birth certificate with the two upper corners in the frame on the screen before taking the photo.</string>`
- `resources/res/values/strings.xml:122`
  `<string name="camera_take_ic_tips">Please align the four corners of the identity card with the four corners in the frame on the screen before taking the photo.</string>`
- `resources/res/values/strings.xml:123`
  `<string name="camera_take_passport_tips">Please align the two bottom corners of the information page of the passport with the two bottom corners in the frame on the screen before taking the photo.</string>`
- `resources/res/values/strings.xml:377`
  `<string name="lasted_login_tag">Last login</string>`
- `resources/res/values/strings.xml:388`
  `<string name="login">Login</string>`
- `resources/res/values/strings.xml:629`
  `<string name="please_auth_first">Please authenticate first</string>`

## BR077

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `sources/ch/qos/logback/core/net/ssl/SSLContextFactoryBean.java:80`
  `public SSLContext createContext(ContextAware contextAware) throws NoSuchAlgorithmException, UnrecoverableKeyException, KeyManagementException, KeyStoreException, CertificateException, NoSuchProviderException {`
- `sources/ch/qos/logback/core/net/ssl/SSLContextFactoryBean.java:81`
  `SSLContext sSLContext = getProvider() != null ? SSLContext.getInstance(getProtocol(), getProvider()) : SSLContext.getInstance(getProtocol());`
- `sources/ch/qos/logback/core/net/ssl/SSLContextFactoryBean.java:82`
  `contextAware.addInfo("SSL protocol '" + sSLContext.getProtocol() + "' provider '" + sSLContext.getProvider() + "'");`
- `sources/ch/qos/logback/core/net/ssl/SSLContextFactoryBean.java:83`
  `sSLContext.init(createKeyManagers(contextAware), createTrustManagers(contextAware), createSecureRandom(contextAware));`
- `sources/ch/qos/logback/core/net/ssl/SSLContextFactoryBean.java:84`
  `return sSLContext;`
- `sources/com/google/firebase/perf/network/InstrHttpsURLConnection.java:339`
  `@Override // javax.net.ssl.HttpsURLConnection`
- `sources/com/google/firebase/perf/network/InstrHttpsURLConnection.java:340`
  `public SSLSocketFactory getSSLSocketFactory() {`
- `sources/com/google/firebase/perf/network/InstrHttpsURLConnection.java:341`
  `return this.httpsURLConnection.getSSLSocketFactory();`
- `sources/com/google/firebase/perf/network/InstrHttpsURLConnection.java:344`
  `@Override // javax.net.ssl.HttpsURLConnection`
- `sources/com/google/firebase/perf/network/InstrHttpsURLConnection.java:346`
  `this.httpsURLConnection.setHostnameVerifier(hostnameVerifier);`
- `sources/com/google/firebase/perf/network/InstrHttpsURLConnection.java:349`
  `@Override // javax.net.ssl.HttpsURLConnection`
- `sources/com/google/firebase/perf/network/InstrHttpsURLConnection.java:350`
  `public void setSSLSocketFactory(SSLSocketFactory sSLSocketFactory) {`
- `sources/com/google/firebase/perf/network/InstrHttpsURLConnection.java:351`
  `this.httpsURLConnection.setSSLSocketFactory(sSLSocketFactory);`
- `sources/com/tencent/liteav/base/util/HttpDnsUtil.java:182`
  `if (httpURLConnection instanceof HttpsURLConnection) {`
- `sources/com/tencent/liteav/base/util/HttpDnsUtil.java:183`
  `HttpsURLConnection httpsURLConnection = (HttpsURLConnection) httpURLConnection;`
- `sources/com/tencent/liteav/base/util/HttpDnsUtil.java:184`
  `httpsURLConnection.setSSLSocketFactory(new b(httpsURLConnection));`
- `sources/com/tencent/liteav/base/util/HttpDnsUtil.java:190`
  `return Boolean.valueOf(HttpsURLConnection.getDefaultHostnameVerifier().verify(str, (SSLSession) objArr[1]));`
- `sources/egnc/moh/base/net/EvydSSLClient.java:30`
  `public static final SSLSocketFactory getSSLSocketFactory() {`
- `sources/egnc/moh/base/net/EvydSSLClient.java:31`
  `INSTANCE.log("getSSLSocketFactory()------>");`
- `sources/egnc/moh/base/net/EvydSSLClient.java:33`
  `SSLContext sSLContext = SSLContext.getInstance(SSL.DEFAULT_PROTOCOL);`
- `sources/egnc/moh/base/net/EvydSSLClient.java:34`
  `sSLContext.init(null, getTrustManager(), new SecureRandom());`
- `sources/egnc/moh/base/net/EvydSSLClient.java:35`
  `return sSLContext.getSocketFactory();`
- `sources/egnc/moh/base/net/EvydSSLClient.java:37`
  `INSTANCE.log("getSSLSocketFactory()---exception--->");`
- `sources/egnc/moh/base/net/SSLSocketClient.java:16`
  `public static SSLSocketFactory getSSLSocketFactory() {`
- `sources/egnc/moh/base/net/SSLSocketClient.java:18`
  `SSLContext sSLContext = SSLContext.getInstance(SSL.DEFAULT_PROTOCOL);`
- `sources/egnc/moh/base/net/SSLSocketClient.java:19`
  `sSLContext.init(null, getTrustManager(), new SecureRandom());`
- `sources/egnc/moh/base/net/SSLSocketClient.java:20`
  `return sSLContext.getSocketFactory();`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:16`
  `public static SSLSocketFactory getSSLSocketFactory() {`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:18`
  `SSLContext sSLContext = SSLContext.getInstance(SSL.DEFAULT_PROTOCOL);`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:19`
  `sSLContext.init(null, getTrustManager(), new SecureRandom());`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:20`
  `return sSLContext.getSocketFactory();`
- `sources/io/flutter/plugins/videoplayer/CustomSSLSocketFactory.java:13`
  `public class CustomSSLSocketFactory extends SSLSocketFactory {`
- `sources/io/flutter/plugins/videoplayer/CustomSSLSocketFactory.java:14`
  `private final SSLSocketFactory sslSocketFactory;`
- `sources/io/flutter/plugins/videoplayer/CustomSSLSocketFactory.java:16`
  `public CustomSSLSocketFactory() throws NoSuchAlgorithmException, KeyManagementException {`
- `sources/io/flutter/plugins/videoplayer/CustomSSLSocketFactory.java:17`
  `SSLContext sSLContext = SSLContext.getInstance("TLS");`
- `sources/io/flutter/plugins/videoplayer/CustomSSLSocketFactory.java:18`
  `sSLContext.init(null, null, null);`
- `sources/io/flutter/plugins/videoplayer/CustomSSLSocketFactory.java:19`
  `this.sslSocketFactory = sSLContext.getSocketFactory();`
- `sources/io/flutter/plugins/videoplayer/CustomSSLSocketFactory.java:22`
  `@Override // javax.net.ssl.SSLSocketFactory`
- `sources/io/flutter/plugins/videoplayer/CustomSSLSocketFactory.java:24`
  `return this.sslSocketFactory.getDefaultCipherSuites();`
- `sources/okhttp3/OkHttpClient.java:519`
  `@Metadata(d1 = {"\u0000ø\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0018...`
- `sources/okhttp3/OkHttpClient.java:720`
  `/* JADX INFO: renamed from: getSslSocketFactoryOrNull$okhttp, reason: from getter */`
- `sources/okhttp3/OkHttpClient.java:721`
  `public final SSLSocketFactory getSslSocketFactoryOrNull() {`
- `sources/okhttp3/OkHttpClient.java:722`
  `return this.sslSocketFactoryOrNull;`
- `sources/okhttp3/OkHttpClient.java:725`
  `public final void setSslSocketFactoryOrNull$okhttp(SSLSocketFactory sSLSocketFactory) {`
- `sources/okhttp3/OkHttpClient.java:726`
  `this.sslSocketFactoryOrNull = sSLSocketFactory;`
- `sources/okhttp3/OkHttpClient.java:1031`
  `@Deprecated(level = DeprecationLevel.ERROR, message = "Use the sslSocketFactory overload that accepts a X509TrustManager.")`
- `sources/okhttp3/OkHttpClient.java:1032`
  `public final Builder sslSocketFactory(SSLSocketFactory sslSocketFactory) throws IllegalAccessException {`
- `sources/okhttp3/OkHttpClient.java:1033`
  `Intrinsics.checkNotNullParameter(sslSocketFactory, "sslSocketFactory");`
- `sources/okhttp3/OkHttpClient.java:1034`
  `if (!Intrinsics.areEqual(sslSocketFactory, getSslSocketFactoryOrNull())) {`
- `sources/okhttp3/OkHttpClient.java:1037`
  `setSslSocketFactoryOrNull$okhttp(sslSocketFactory);`
- `sources/okhttp3/OkHttpClient.java:1038`
  `X509TrustManager x509TrustManagerTrustManager = Platform.INSTANCE.get().trustManager(sslSocketFactory);`
- `sources/okhttp3/OkHttpClient.java:1040`
  `throw new IllegalStateException("Unable to extract the trust manager on " + Platform.INSTANCE.get() + ", sslSocketFactory is " + sslSocketFactory.getClass());`
- `sources/okhttp3/OkHttpClient.java:1050`
  `public final Builder sslSocketFactory(SSLSocketFactory sslSocketFactory, X509TrustManager trustManager) {`
- `sources/okhttp3/OkHttpClient.java:1051`
  `Intrinsics.checkNotNullParameter(sslSocketFactory, "sslSocketFactory");`
- `sources/okhttp3/OkHttpClient.java:1053`
  `if (!Intrinsics.areEqual(sslSocketFactory, getSslSocketFactoryOrNull()) || !Intrinsics.areEqual(trustManager, getX509TrustManagerOrNull())) {`
- `sources/okhttp3/OkHttpClient.java:1056`
  `setSslSocketFactoryOrNull$okhttp(sslSocketFactory);`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:47`
  `return sSLContext;`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:56`
  `return sSLContext;`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:124`
  `public SSLSocketFactory newSslSocketFactory(X509TrustManager trustManager) throws NoSuchAlgorithmException, KeyManagementException {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:126`
  `SSLContext sSLContextNewSSLContext = newSSLContext();`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:128`
  `SSLSocketFactory socketFactory = sSLContextNewSSLContext.getSocketFactory();`
- `sources/okhttp3/internal/platform/OpenJSSEPlatform.java:45`
  `return sSLContext;`
- `sources/okhttp3/internal/platform/Platform.java:83`
  `Intrinsics.checkNotNullExpressionValue(sSLContext, "getInstance(\"TLS\")");`
- `sources/okhttp3/internal/platform/Platform.java:84`
  `return sSLContext;`
- `sources/okhttp3/internal/platform/Platform.java:178`
  `public SSLSocketFactory newSslSocketFactory(X509TrustManager trustManager) {`
- `sources/okhttp3/internal/platform/Platform.java:181`
  `SSLContext sSLContextNewSSLContext = newSSLContext();`
- `sources/okhttp3/internal/platform/Platform.java:183`
  `SSLSocketFactory socketFactory = sSLContextNewSSLContext.getSocketFactory();`

## BR078

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/egnc/moh/base/net/SSLSocketClient.java:7`
  `import javax.net.ssl.HostnameVerifier;`
- `sources/egnc/moh/base/net/SSLSocketClient.java:60`
  `public static HostnameVerifier getHostnameVerifier() {`
- `sources/egnc/moh/base/net/SSLSocketClient.java:61`
  `return new HostnameVerifier() { // from class: egnc.moh.base.net.SSLSocketClient.3`
- `sources/egnc/moh/base/net/SSLSocketClient.java:62`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/egnc/moh/base/web/manager/health/OkHttpUtils.java:23`
  `private static void setSafe(OkHttpClient.Builder builder) {`
- `sources/egnc/moh/base/web/manager/health/OkHttpUtils.java:26`
  `builder.hostnameVerifier(SSLSocketClient.getHostnameVerifier());`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:7`
  `import javax.net.ssl.HostnameVerifier;`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:60`
  `public static HostnameVerifier getHostnameVerifier() {`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:61`
  `return new HostnameVerifier() { // from class: egnc.moh.base.web.manager.health.SSLSocketClient.3`
- `sources/egnc/moh/base/web/manager/health/SSLSocketClient.java:62`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/okhttp3/OkHttpClient.java:19`
  `import javax.net.ssl.HostnameVerifier;`
- `sources/okhttp3/OkHttpClient.java:40`
  `import okhttp3.internal.tls.CertificateChainCleaner;`
- `sources/okhttp3/OkHttpClient.java:41`
  `import okhttp3.internal.tls.OkHostnameVerifier;`
- `sources/okhttp3/OkHttpClient.java:42`
  `import okhttp3.internal.ws.RealWebSocket;`
- `sources/okhttp3/OkHttpClient.java:44`
  `/* JADX INFO: compiled from: OkHttpClient.kt */`
- `sources/okhttp3/OkHttpClient.java:46`
  `@Metadata(d1 = {"\u0000î\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u001a\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u00...`
- `sources/okhttp3/OkHttpClient.java:47`
  `public class OkHttpClient implements Cloneable, Call.Factory, WebSocket.Factory {`
- `sources/okhttp3/OkHttpClient.java:518`
  `/* JADX INFO: compiled from: OkHttpClient.kt */`
- `sources/okhttp3/OkHttpClient.java:519`
  `@Metadata(d1 = {"\u0000ø\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0018...`
- `sources/okhttp3/OkHttpClient.java:863`
  `this.dns = okHttpClient.dns();`
- `sources/okhttp3/OkHttpClient.java:864`
  `this.proxy = okHttpClient.proxy();`
- `sources/okhttp3/OkHttpClient.java:865`
  `this.proxySelector = okHttpClient.proxySelector();`
- `sources/okhttp3/OkHttpClient.java:866`
  `this.proxyAuthenticator = okHttpClient.proxyAuthenticator();`
- `sources/okhttp3/OkHttpClient.java:867`
  `this.socketFactory = okHttpClient.socketFactory();`
- `sources/okhttp3/OkHttpClient.java:868`
  `this.sslSocketFactoryOrNull = okHttpClient.sslSocketFactoryOrNull;`
- `sources/okhttp3/OkHttpClient.java:869`
  `this.x509TrustManagerOrNull = okHttpClient.getX509TrustManager();`
- `sources/okhttp3/OkHttpClient.java:870`
  `this.connectionSpecs = okHttpClient.connectionSpecs();`
- `sources/okhttp3/OkHttpClient.java:871`
  `this.protocols = okHttpClient.protocols();`
- `sources/okhttp3/OkHttpClient.java:872`
  `this.hostnameVerifier = okHttpClient.hostnameVerifier();`
- `sources/okhttp3/OkHttpClient.java:873`
  `this.certificatePinner = okHttpClient.certificatePinner();`
- `sources/okhttp3/OkHttpClient.java:874`
  `this.certificateChainCleaner = okHttpClient.getCertificateChainCleaner();`
- `sources/okhttp3/OkHttpClient.java:875`
  `this.callTimeout = okHttpClient.callTimeoutMillis();`
- `sources/okhttp3/internal/connection/RealConnection.java:620`
  `if (this.http2Connection == null || routes == null || !routeMatchesAny(routes) || address.hostnameVerifier() != OkHostnameVerifier.INSTANCE || !supportsUrl(address.url())) {`
- `sources/okhttp3/internal/http2/PushObserver.java:35`
  `@Metadata(d1 = {"\u00008\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\b\u0002\u0018\u00002\u00...`
- `sources/okhttp3/internal/http2/PushObserver.java:37`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:43`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:49`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:54`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/platform/Android10Platform.java:15`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/Android10Platform.java:16`
  `import okhttp3.internal.platform.android.Android10SocketAdapter;`
- `sources/okhttp3/internal/platform/Android10Platform.java:21`
  `import okhttp3.internal.platform.android.DeferredSocketAdapter;`
- `sources/okhttp3/internal/platform/Android10Platform.java:22`
  `import okhttp3.internal.platform.android.SocketAdapter;`
- `sources/okhttp3/internal/platform/Android10Platform.java:23`
  `import okhttp3.internal.tls.CertificateChainCleaner;`
- `sources/okhttp3/internal/platform/Android10Platform.java:27`
  `@Metadata(d1 = {"\u0000J\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\...`
- `sources/okhttp3/internal/platform/Android10Platform.java:46`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Android10Platform.java:68`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Android10Platform.java:120`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Android10Platform.java:128`
  `@Metadata(d1 = {"\u0000\u001a\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\b\u0086\u0003\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002J\b\u0010\u0006\u001a\u0004\u0018\u00010\u0007R\u0011\u0010\u0003\u001a...`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:24`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:25`
  `import okhttp3.internal.platform.android.AndroidCertificateChainCleaner;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:32`
  `import okhttp3.internal.platform.android.StandardAndroidSocketAdapter;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:33`
  `import okhttp3.internal.tls.CertificateChainCleaner;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:34`
  `import okhttp3.internal.tls.TrustRootIndex;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:38`
  `@Metadata(d1 = {"\u0000x\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\...`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:73`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:95`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:168`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:175`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:189`
  `@Metadata(d1 = {"\u00008\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u000e\n\u0000\b\u0080\b\u0018\u00...`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:246`
  `@Override // okhttp3.internal.tls.TrustRootIndex`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:20`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:27`
  `@Metadata(d1 = {"\u0000J\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\...`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:50`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:70`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:76`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:22`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:24`
  `import org.conscrypt.ConscryptHostnameVerifier;`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:28`
  `@Metadata(d1 = {"\u0000H\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\...`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:40`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:59`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:70`
  `Conscrypt.setHostnameVerifier(x509TrustManager, DisabledHostnameVerifier.INSTANCE);`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:82`
  `@Metadata(d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\u0011\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\bÀ\u0002\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002J3\u0...`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:83`
  `public static final class DisabledHostnameVerifier implements ConscryptHostnameVerifier {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:84`
  `public static final DisabledHostnameVerifier INSTANCE = new DisabledHostnameVerifier();`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:94`
  `private DisabledHostnameVerifier() {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:123`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:1`
  `package okhttp3.internal.platform;`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:12`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:16`
  `@Metadata(d1 = {"\u0000<\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\...`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:54`
  `@Override // okhttp3.internal.platform.Platform`

## BR079

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/com/evgenii/jsevaluator/WebViewWrapper.java:20`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/netease/nis/captcha/CaptchaWebView.java:43`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/netease/nis/captcha/CaptchaWebView.java:47`
  `settings.setAllowFileAccess(false);`
- `sources/egnc/moh/base/web/CommonWebView.java:284`
  `this.mWebView.getSettings().setMixedContentMode(0);`
- `sources/egnc/moh/base/web/CommonWebView.java:285`
  `this.mWebView.getSettings().setAllowFileAccess(true);`
- `sources/egnc/moh/base/web/CommonWebView.java:295`
  `this.mWebView.getSettings().setJavaScriptEnabled(true);`
- `sources/egnc/moh/bruhealth/nativeLib/activities/PrivacyUserActivity.java:107`
  `webView.getSettings().setJavaScriptEnabled(true);`
- `sources/io/flutter/plugins/urllauncher/WebViewActivity.java:87`
  `this.webview.getSettings().setJavaScriptEnabled(booleanExtra);`
- `sources/org/apache/cordova/engine/SystemWebViewEngine.java:107`
  `settings.setJavaScriptEnabled(true);`
- `sources/org/apache/cordova/engine/SystemWebViewEngine.java:113`
  `settings.setAllowUniversalAccessFromFileURLs(true);`
- `sources/org/apache/cordova/inappbrowser/InAppBrowser.java:901`
  `settings.setJavaScriptEnabled(true);`

## BR080

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/android/support/v4/media/MediaBrowserCompat.java:657`
  `Log.d(MediaBrowserCompat.TAG, "addSubscription failed with RemoteException parentId=" + parentId);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:775`
  `Log.d(MediaBrowserCompat.TAG, "ServiceCallbacks.onConnect...");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:790`
  `Log.d(MediaBrowserCompat.TAG, "addSubscription failed with RemoteException.");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:888`
  `Log.d(MediaBrowserCompat.TAG, "  mServiceConnection=" + this.mServiceConnection);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:889`
  `Log.d(MediaBrowserCompat.TAG, "  mServiceBinderWrapper=" + this.mServiceBinderWrapper);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:890`
  `Log.d(MediaBrowserCompat.TAG, "  mCallbacksMessenger=" + this.mCallbacksMessenger);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:891`
  `Log.d(MediaBrowserCompat.TAG, "  mRootId=" + this.mRootId);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:892`
  `Log.d(MediaBrowserCompat.TAG, "  mMediaSessionToken=" + this.mMediaSessionToken);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2225`
  `Log.d("AppCompatDelegate", "Exception while getting ActivityInfo", e);`
- `sources/androidx/camera/core/processing/OpenGlRenderer.java:261`
  `Log.d(TAG, "EGLContext created, client version " + iArr3[0]);`
- `sources/androidx/compose/ui/autofill/AutofillCallback.java:33`
  `Log.d("Autofill Status", str);`
- `sources/androidx/constraintlayout/compose/Measurer.java:245`
  `Log.d(str, "Measuring " + LayoutIdKt.getLayoutId((Measurable) companionWidget) + " with " + ((Object) Constraints.m5633toStringimpl(jConstraints)));`
- `sources/androidx/constraintlayout/compose/Measurer.java:254`
  `Log.d(str, LayoutIdKt.getLayoutId(measurable) + " is size " + placeableMo4614measureBRTryo0.getWidth() + ' ' + placeableMo4614measureBRTryo0.getHeight());`
- `sources/androidx/constraintlayout/compose/Measurer.java:499`
  `Log.d("CCL", "Final measurement for " + LayoutIdKt.getLayoutId((Measurable) companionWidget2) + " to confirm size " + constraintWidget2.getWidth() + ' ' + constraintWidget2.getHeight());`
- `sources/androidx/constraintlayout/compose/Measurer.java:505`
  `Log.d("CCL", "ConstraintLayout is at the end " + this.root.getWidth() + ' ' + this.root.getHeight());`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:1371`
  `Log.v(MotionLayout.TAG, str2 + " done. ");`
- `sources/androidx/core/view/ViewCompat.java:676`
  `Log.d(TAG, "Error calling dispatchStartTemporaryDetach", e);`
- `sources/androidx/core/view/ViewCompat.java:697`
  `Log.d(TAG, "Error calling dispatchFinishTemporaryDetach", e);`
- `sources/androidx/exifinterface/media/ExifInterface.java:3153`
  `Log.d(TAG, "readExifSegment: Byte Align MM");`
- `sources/androidx/exifinterface/media/ExifInterface.java:3311`
  `Log.d(TAG, "Failed to skip " + i8 + " bytes.");`
- `sources/androidx/exifinterface/media/ExifInterface.java:3317`
  `Log.d(TAG, "Failed to read " + i7 + " bytes.");`
- `sources/androidx/fragment/app/FragmentLayoutInflaterFactory.java:71`
  `Log.v("FragmentManager", "Fragment " + fragmentFindFragmentById + " has been inflated via the <fragment> tag: id=0x" + Integer.toHexString(resourceId));`
- `sources/androidx/fragment/app/FragmentLayoutInflaterFactory.java:83`
  `Log.v("FragmentManager", "Retained Fragment " + fragmentFindFragmentById + " has been re-attached via the <fragment> tag: id=0x" + Integer.toHexString(resourceId));`
- `sources/androidx/fragment/app/FragmentManager.java:1710`
  `Log.v(TAG, "Discarding retained Fragment " + fragment2 + " that was not found in the set of active Fragments " + fragmentManagerState.mActive);`
- `sources/androidx/fragment/app/FragmentStateManager.java:466`
  `Log.d("FragmentManager", "moveto ACTIVITY_CREATED: " + this.mFragment);`
- `sources/androidx/fragment/app/FragmentStore.java:126`
  `Log.v("FragmentManager", "Removed fragment from active set " + fragment);`
- `sources/androidx/fragment/app/SpecialEffectsController.java:285`
  `Log.v(FragmentManager.TAG, "SpecialEffectsController: Finished executing pending operations");`
- `sources/androidx/heifwriter/EglWindowSurface.java:60`
  `Log.d(TAG, "re-create EGLSurface");`
- `sources/androidx/localbroadcastmanager/content/LocalBroadcastManager.java:151`
  `Log.v(TAG, "Resolving type " + strResolveTypeIfNeeded + " scheme " + scheme + " of intent " + intent);`
- `sources/androidx/localbroadcastmanager/content/LocalBroadcastManager.java:156`
  `Log.v(TAG, "Action list: " + arrayList2);`
- `sources/androidx/localbroadcastmanager/content/LocalBroadcastManager.java:179`
  `Log.v(TAG, "  Filter matched!  match=0x" + Integer.toHexString(iMatch));`
- `sources/androidx/media2/session/MediaControllerImplBase.java:118`
  `Log.d(TAG, "release from " + this.mToken);`
- `sources/androidx/media2/session/MediaControllerImplBase.java:702`
  `Log.d(TAG, "bind to " + this.mToken + " succeeded");`
- `sources/androidx/media2/session/MediaControllerImplBase.java:1094`
  `Log.d(TAG, "onCustomCommand cmd=" + sessionCommand.getCustomAction());`
- `sources/androidx/media2/session/MediaControllerImplBase.java:1140`
  `Log.d(MediaControllerImplBase.TAG, "onServiceConnected " + componentName + " " + this);`
- `sources/androidx/media2/session/MediaControllerImplLegacy.java:104`
  `Log.d(TAG, "close from " + this.mToken);`
- `sources/androidx/media2/session/MediaControllerImplLegacy.java:923`
  `Log.d(TAG, "onConnectedNotLocked token=" + this.mToken);`
- `sources/androidx/media2/session/MediaControllerImplLegacy.java:1053`
  `Log.d(MediaControllerImplLegacy.TAG, "Controller is closed prematually", new IllegalStateException());`
- `sources/androidx/media2/session/MediaControllerStub.java:263`
  `Log.d(TAG, "onConnected after MediaController.close()");`
- `sources/androidx/media2/session/MediaSessionImplBase.java:188`
  `Log.d(TAG, "Closing session, id=" + getId() + ", token=" + getToken());`

## BR081

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/androidx/biometric/CryptoObjectUtils.java:6`
  `import android.security.keystore.KeyGenParameterSpec;`
- `sources/androidx/biometric/CryptoObjectUtils.java:29`
  `private static final String KEYSTORE_INSTANCE = "AndroidKeyStore";`
- `sources/androidx/biometric/CryptoObjectUtils.java:124`
  `KeyStore keyStore = KeyStore.getInstance("AndroidKeyStore");`
- `sources/androidx/biometric/CryptoObjectUtils.java:126`
  `KeyGenParameterSpec.Builder builderCreateKeyGenParameterSpecBuilder = Api23Impl.createKeyGenParameterSpecBuilder(FAKE_KEY_NAME, 3);`
- `sources/androidx/biometric/CryptoObjectUtils.java:127`
  `Api23Impl.setBlockModeCBC(builderCreateKeyGenParameterSpecBuilder);`
- `sources/androidx/biometric/CryptoObjectUtils.java:128`
  `Api23Impl.setEncryptionPaddingPKCS7(builderCreateKeyGenParameterSpecBuilder);`
- `sources/androidx/biometric/CryptoObjectUtils.java:129`
  `KeyGenerator keyGenerator = KeyGenerator.getInstance("AES", "AndroidKeyStore");`
- `sources/androidx/biometric/CryptoObjectUtils.java:130`
  `Api23Impl.initKeyGenerator(keyGenerator, Api23Impl.buildKeyGenParameterSpec(builderCreateKeyGenParameterSpecBuilder));`
- `sources/androidx/biometric/CryptoObjectUtils.java:188`
  `static KeyGenParameterSpec.Builder createKeyGenParameterSpecBuilder(String str, int i) {`
- `sources/androidx/biometric/CryptoObjectUtils.java:189`
  `return new KeyGenParameterSpec.Builder(str, i);`
- `sources/androidx/biometric/CryptoObjectUtils.java:192`
  `static void setBlockModeCBC(KeyGenParameterSpec.Builder builder) {`
- `sources/androidx/biometric/CryptoObjectUtils.java:196`
  `static void setEncryptionPaddingPKCS7(KeyGenParameterSpec.Builder builder) {`
- `sources/androidx/biometric/CryptoObjectUtils.java:200`
  `static KeyGenParameterSpec buildKeyGenParameterSpec(KeyGenParameterSpec.Builder builder) {`
- `sources/androidx/biometric/CryptoObjectUtils.java:204`
  `static void initKeyGenerator(KeyGenerator keyGenerator, KeyGenParameterSpec keyGenParameterSpec) throws InvalidAlgorithmParameterException {`
- `sources/androidx/biometric/CryptoObjectUtils.java:205`
  `keyGenerator.init(keyGenParameterSpec);`
- `sources/ch/qos/logback/core/net/ssl/KeyStoreFactoryBean.java:21`
  `return getProvider() != null ? KeyStore.getInstance(getType(), getProvider()) : KeyStore.getInstance(getType());`
- `sources/com/evyd/toast/EvydToastV2$$ExternalSyntheticApiModelOutline0.java:5`
  `import android.security.keystore.KeyGenParameterSpec;`
- `sources/com/evyd/toast/EvydToastV2$$ExternalSyntheticApiModelOutline0.java:21`
  `public static /* synthetic */ KeyGenParameterSpec.Builder m(String str, int i) {`
- `sources/com/evyd/toast/EvydToastV2$$ExternalSyntheticApiModelOutline0.java:22`
  `return new KeyGenParameterSpec.Builder(str, i);`
- `sources/egnc/moh/base/account/CryptographyManager.java:16`
  `public static final String ANDROID_KEYSTORE = "AndroidKeyStore";`
- `sources/egnc/moh/base/account/CryptographyManager.java:42`
  `public static final String ANDROID_KEYSTORE = "AndroidKeyStore";`
- `sources/egnc/moh/base/account/CryptographyManager.java:61`
  `KeyStore keyStore = KeyStore.getInstance("AndroidKeyStore");`
- `sources/egnc/moh/base/account/CryptographyManagerImpl.java:4`
  `import android.security.keystore.KeyGenParameterSpec;`
- `sources/egnc/moh/base/account/CryptographyManagerImpl.java:123`
  `KeyGenParameterSpec.Builder builderM = EvydToastV2$$ExternalSyntheticApiModelOutline0.m(keyName, 3);`
- `sources/egnc/moh/base/account/CryptographyManagerImpl.java:131`
  `KeyGenParameterSpec keyGenParameterSpecBuild = builderM.build();`
- `sources/egnc/moh/base/account/CryptographyManagerImpl.java:132`
  `Intrinsics.checkNotNullExpressionValue(keyGenParameterSpecBuild, "build(...)");`
- `sources/egnc/moh/base/account/CryptographyManagerImpl.java:133`
  `KeyGenerator keyGenerator = KeyGenerator.getInstance("AES", "AndroidKeyStore");`
- `sources/egnc/moh/base/account/CryptographyManagerImpl.java:134`
  `keyGenerator.init(keyGenParameterSpecBuild);`

## BR082

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:15`
  `import androidx.core.content.FileProvider;`
- `sources/androidx/browser/customtabs/TrustedWebUtils.java:10`
  `import androidx.core.content.FileProvider;`
- `sources/androidx/browser/customtabs/TrustedWebUtils.java:44`
  `Uri uriForFile = FileProvider.getUriForFile(context, str, file);`
- `sources/androidx/core/content/FileProvider.java:269`
  `@Override // androidx.core.content.FileProvider.PathStrategy`
- `sources/androidx/core/content/FileProvider.java:296`
  `@Override // androidx.core.content.FileProvider.PathStrategy`
- `sources/com/blankj/utilcode/util/IntentUtils.java:8`
  `import androidx.core.content.FileProvider;`
- `sources/com/blankj/utilcode/util/IntentUtils.java:37`
  `uriForFile = FileProvider.getUriForFile(Utils.getApp(), Utils.getApp().getPackageName() + ".utilcode.provider", file);`
- `sources/com/blankj/utilcode/util/UriUtils.java:13`
  `import androidx.core.content.FileProvider;`
- `sources/com/blankj/utilcode/util/UriUtils.java:36`
  `return FileProvider.getUriForFile(Utils.getApp(), Utils.getApp().getPackageName() + ".utilcode.provider", file);`
- `sources/com/blankj/utilcode/util/UtilsFileProvider.java:4`
  `import androidx.core.content.FileProvider;`
- `sources/com/blankj/utilcode/util/UtilsFileProvider.java:8`
  `@Override // androidx.core.content.FileProvider, android.content.ContentProvider`
- `sources/com/evyd/core/camera/CameraGalleryActivity.java:18`
  `import androidx.core.content.FileProvider;`
- `sources/com/evyd/core/camera/CameraGalleryActivity.java:244`
  `uriFromFile = FileProvider.getUriForFile(cameraGalleryActivity, getPackageNameWithName("camera_gallery_file_provider"), fileCreateAndroidDataDirFile);`
- `sources/com/evyd/core/camera/CameraGalleryFileProvider.java:3`
  `import androidx.core.content.FileProvider;`
- `sources/com/evyd/core/multipicker/selectpic/GalleryPickerFileProvider.java:3`
  `import androidx.core.content.FileProvider;`
- `sources/de/appplant/cordova/plugin/notification/util/AssetProvider.java:3`
  `import androidx.core.content.FileProvider;`
- `sources/egnc/moh/base/provider/ShareFileProvider.java:3`
  `import androidx.core.content.FileProvider;`
- `sources/egnc/moh/base/web/CommonWebView.java:29`
  `import androidx.core.content.FileProvider;`
- `sources/egnc/moh/base/web/CommonWebView.java:367`
  `CommonWebView.this.mImageUri = new CordovaUri(FileProvider.getUriForFile(Utils.getApp(), Utils.getApp().getPackageName() + ".shareprovider", fileCreateImageFile)).getCorrectUri();`
- `sources/egnc/moh/base/web/manager/ShareManager.java:10`
  `import androidx.core.content.FileProvider;`
- `sources/egnc/moh/base/web/manager/ShareManager.java:296`
  `Uri uriForFile = FileProvider.getUriForFile(Utils.getApp(), Utils.getApp().getPackageName() + ".shareprovider", file);`
- `sources/egnc/moh/base/web/manager/camera/CameraLauncher.java:16`
  `import androidx.core.content.FileProvider;`
- `sources/egnc/moh/base/web/manager/camera/CameraLauncher.java:220`
  `CordovaUri cordovaUri = new CordovaUri(FileProvider.getUriForFile(Utils.getApp(), Utils.getApp().getPackageName() + ".shareprovider", fileCreateCaptureFile));`
- `sources/egnc/moh/base/web/manager/camera/CameraLauncher.java:661`
  `performCrop(FileProvider.getUriForFile(Utils.getApp(), Utils.getApp().getPackageName() + ".shareprovider", createCaptureFile(this.encodingType)), this.destType, intent);`
- `sources/egnc/moh/base/web/manager/filetransfer/FileTransfer.java:7`
  `import androidx.core.content.FileProvider;`
- `sources/egnc/moh/base/web/manager/filetransfer/FileTransfer.java:484`
  `uriFromFile = FileProvider.getUriForFile(Utils.getApp(), Utils.getApp().getPackageName() + ".shareprovider", file);`
- `sources/org/apache/cordova/camera/CameraLauncher.java:202`
  `CordovaUri cordovaUri = new CordovaUri(androidx.core.content.FileProvider.getUriForFile(this.cordova.getActivity(), this.applicationId + ".provider", fileCreateCaptureFile));`
- `sources/org/apache/cordova/camera/CameraLauncher.java:634`
  `performCrop(androidx.core.content.FileProvider.getUriForFile(this.cordova.getActivity(), this.applicationId + ".provider", createCaptureFile(this.encodingType)), i4, intent);`
- `sources/org/apache/cordova/camera/FileProvider.java:4`
  `public class FileProvider extends androidx.core.content.FileProvider {`

## BR084

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/android/support/v4/media/session/MediaSessionCompat.java:200`
  `mbrIntent = PendingIntent.getBroadcast(context, 0, intent, PENDING_INTENT_FLAG_MUTABLE);`
- `sources/androidx/media/session/MediaButtonReceiver.java:119`
  `return PendingIntent.getBroadcast(context, keyCode, intent, MediaSessionCompat.PENDING_INTENT_FLAG_MUTABLE);`

## BR086

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/androidx/appcompat/R.java:63`
  `public static int actionModeShareDrawable = 0x7f04001a;`
- `sources/androidx/appcompat/R.java:517`
  `public static int abc_ab_share_pack_mtrl_alpha = 0x7f08002a;`
- `sources/androidx/appcompat/R.java:525`
  `public static int abc_btn_default_mtrl_shape = 0x7f080032;`
- `sources/androidx/appcompat/R.java:1249`
  `public static int AppCompatTheme_actionModeShareDrawable = 0x0000001b;`
- `sources/androidx/appcompat/R.java:1361`
  `public static int DrawerArrowToggle_arrowShaftLength = 0x00000001;`
- `sources/androidx/appcompat/R.java:1544`
  `public static int[] AppCompatTheme = {android.R.attr.windowIsFloating, android.R.attr.windowAnimationStyle, egnc.moh.bruhealth.R.attr.actionBarDivider, egnc.moh.bruhealth.R.attr.actionBarItemBackground, egnc.moh.bruhealth.R.attr.actionBarPopupTheme, egnc.moh.bruhealth.R.attr.actionBarSize, egnc.moh....`
- `sources/androidx/appcompat/R.java:1548`
  `public static int[] DrawerArrowToggle = {egnc.moh.bruhealth.R.attr.arrowHeadLength, egnc.moh.bruhealth.R.attr.arrowShaftLength, egnc.moh.bruhealth.R.attr.barLength, egnc.moh.bruhealth.R.attr.color, egnc.moh.bruhealth.R.attr.drawableSize, egnc.moh.bruhealth.R.attr.gapBetweenBars, egnc.moh.bruhealth.R...`
- `sources/androidx/appcompat/R.java:1561`
  `public static int[] TextAppearance = {android.R.attr.textSize, android.R.attr.typeface, android.R.attr.textStyle, android.R.attr.textColor, android.R.attr.textColorHint, android.R.attr.textColorLink, android.R.attr.shadowColor, android.R.attr.shadowDx, android.R.attr.shadowDy, android.R.attr.shadowR...`
- `sources/androidx/appcompat/app/AppCompatDelegate.java:101`
  `public abstract boolean isHandleNativeActionModesEnabled();`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1152`
  `public boolean isHandleNativeActionModesEnabled() {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2641`
  `if (AppCompatDelegateImpl.this.isHandleNativeActionModesEnabled()) {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2658`
  `if (AppCompatDelegateImpl.this.isHandleNativeActionModesEnabled() && i == 0) {`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:24`
  `private float mArrowShaftLength;`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:67`
  `this.mArrowShaftLength = typedArrayObtainStyledAttributes.getDimension(R.styleable.DrawerArrowToggle_arrowShaftLength, 0.0f);`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:177`
  `float fLerp2 = lerp(this.mBarLength, this.mArrowShaftLength, this.mProgress);`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:476`
  `java.lang.String r3 = "Share records file not well-formed."`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:481`
  `java.lang.String r3 = "Share records file does not start with historical-records tag."`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:9`
  `import android.graphics.Shader;`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:32`
  `private final int[] COLORFILTER_TINT_COLOR_CONTROL_NORMAL = {R.drawable.abc_textfield_search_default_mtrl_alpha, R.drawable.abc_textfield_default_mtrl_alpha, R.drawable.abc_ab_share_pack_mtrl_alpha};`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:33`
  `private final int[] TINT_COLOR_CONTROL_NORMAL = {R.drawable.abc_ic_commit_search_api_mtrl_alpha, R.drawable.abc_seekbar_tick_mark_material, R.drawable.abc_ic_menu_share_mtrl_alpha, R.drawable.abc_ic_menu_copy_mtrl_am_alpha, R.drawable.abc_ic_menu_cut_mtrl_alpha, R.drawable.abc_ic_menu_selectall_mtrl...`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:114`
  `bitmapDrawable2.setTileModeX(Shader.TileMode.REPEAT);`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:180`
  `if (i == R.drawable.abc_btn_default_mtrl_shape) {`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:5`
  `import android.graphics.BitmapShader;`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:6`
  `import android.graphics.Shader;`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:12`
  `import android.graphics.drawable.ShapeDrawable;`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:13`
  `import android.graphics.drawable.shapes.RoundRectShape;`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:14`
  `import android.graphics.drawable.shapes.Shape;`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:75`
  `ShapeDrawable shapeDrawable = new ShapeDrawable(getDrawableShape());`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:76`
  `shapeDrawable.getPaint().setShader(new BitmapShader(bitmap, Shader.TileMode.REPEAT, Shader.TileMode.CLAMP));`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:77`
  `shapeDrawable.getPaint().setColorFilter(bitmapDrawable.getPaint().getColorFilter());`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:78`
  `return z ? new ClipDrawable(shapeDrawable, 3, 1) : shapeDrawable;`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:101`
  `private Shape getDrawableShape() {`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:102`
  `return new RoundRectShape(new float[]{5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f}, null, null);`
- `sources/androidx/appcompat/widget/DropDownListView.java:520`
  `private static boolean sHasMethods;`
- `sources/androidx/appcompat/widget/DropDownListView.java:536`
  `sHasMethods = true;`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:53`
  `activityChooserView.setActivityChooserModel(ActivityChooserModel.get(this.mContext, this.mShareHistoryFileName));`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:56`
  `this.mContext.getTheme().resolveAttribute(R.attr.actionModeShareDrawable, typedValue, true);`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:59`
  `activityChooserView.setDefaultActionButtonContentDescription(R.string.abc_shareactionprovider_share_with_application);`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:60`
  `activityChooserView.setExpandActivityOverflowButtonContentDescription(R.string.abc_shareactionprovider_share_with);`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:67`
  `ActivityChooserModel activityChooserModel = ActivityChooserModel.get(this.mContext, this.mShareHistoryFileName);`
- `sources/androidx/biometric/BiometricFragment.java:546`
  `if (fingerprintManagerCompat.isHardwareDetected()) {`
- `sources/androidx/biometric/CryptoObjectUtils.java:128`
  `Api23Impl.setEncryptionPaddingPKCS7(builderCreateKeyGenParameterSpecBuilder);`
- `sources/androidx/biometric/CryptoObjectUtils.java:129`
  `KeyGenerator keyGenerator = KeyGenerator.getInstance("AES", "AndroidKeyStore");`
- `sources/androidx/biometric/CryptoObjectUtils.java:133`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS7Padding");`
- `sources/androidx/biometric/R.java:74`
  `public static int actionModeShareDrawable = 0x7f04001a;`
- `sources/androidx/biometric/R.java:559`
  `public static int abc_ab_share_pack_mtrl_alpha = 0x7f08002a;`
- `sources/androidx/biometric/R.java:567`
  `public static int abc_btn_default_mtrl_shape = 0x7f080032;`
- `sources/androidx/biometric/R.java:911`
  `public static int abc_shareactionprovider_share_with = 0x7f130018;`
- `sources/androidx/biometric/R.java:912`
  `public static int abc_shareactionprovider_share_with_application = 0x7f130019;`
- `sources/androidx/biometric/R.java:1412`
  `public static int AppCompatTheme_actionModeShareDrawable = 0x0000001b;`
- `sources/androidx/biometric/R.java:1525`
  `public static int DrawerArrowToggle_arrowShaftLength = 0x00000001;`
- `sources/androidx/biometric/R.java:1753`
  `public static int[] AppCompatTheme = {android.R.attr.windowIsFloating, android.R.attr.windowAnimationStyle, egnc.moh.bruhealth.R.attr.actionBarDivider, egnc.moh.bruhealth.R.attr.actionBarItemBackground, egnc.moh.bruhealth.R.attr.actionBarPopupTheme, egnc.moh.bruhealth.R.attr.actionBarSize, egnc.moh....`
- `sources/androidx/biometric/R.java:1757`
  `public static int[] DrawerArrowToggle = {egnc.moh.bruhealth.R.attr.arrowHeadLength, egnc.moh.bruhealth.R.attr.arrowShaftLength, egnc.moh.bruhealth.R.attr.barLength, egnc.moh.bruhealth.R.attr.color, egnc.moh.bruhealth.R.attr.drawableSize, egnc.moh.bruhealth.R.attr.gapBetweenBars, egnc.moh.bruhealth.R...`
- `sources/androidx/biometric/R.java:1778`
  `public static int[] TextAppearance = {android.R.attr.textSize, android.R.attr.typeface, android.R.attr.textStyle, android.R.attr.textColor, android.R.attr.textColorHint, android.R.attr.textColorLink, android.R.attr.shadowColor, android.R.attr.shadowDx, android.R.attr.shadowDy, android.R.attr.shadowR...`
- `sources/androidx/biometric/ktx/R.java:74`
  `public static int actionModeShareDrawable = 0x7f04001a;`
- `sources/androidx/biometric/ktx/R.java:559`
  `public static int abc_ab_share_pack_mtrl_alpha = 0x7f08002a;`
- `sources/androidx/biometric/ktx/R.java:567`
  `public static int abc_btn_default_mtrl_shape = 0x7f080032;`
- `sources/androidx/biometric/ktx/R.java:911`
  `public static int abc_shareactionprovider_share_with = 0x7f130018;`
- `sources/androidx/biometric/ktx/R.java:912`
  `public static int abc_shareactionprovider_share_with_application = 0x7f130019;`
- `sources/androidx/biometric/ktx/R.java:1412`
  `public static int AppCompatTheme_actionModeShareDrawable = 0x0000001b;`
- `sources/androidx/biometric/ktx/R.java:1525`
  `public static int DrawerArrowToggle_arrowShaftLength = 0x00000001;`
- `sources/androidx/biometric/ktx/R.java:1753`
  `public static int[] AppCompatTheme = {android.R.attr.windowIsFloating, android.R.attr.windowAnimationStyle, egnc.moh.bruhealth.R.attr.actionBarDivider, egnc.moh.bruhealth.R.attr.actionBarItemBackground, egnc.moh.bruhealth.R.attr.actionBarPopupTheme, egnc.moh.bruhealth.R.attr.actionBarSize, egnc.moh....`
- `sources/androidx/biometric/ktx/R.java:1757`
  `public static int[] DrawerArrowToggle = {egnc.moh.bruhealth.R.attr.arrowHeadLength, egnc.moh.bruhealth.R.attr.arrowShaftLength, egnc.moh.bruhealth.R.attr.barLength, egnc.moh.bruhealth.R.attr.color, egnc.moh.bruhealth.R.attr.drawableSize, egnc.moh.bruhealth.R.attr.gapBetweenBars, egnc.moh.bruhealth.R...`
- `sources/androidx/biometric/ktx/R.java:1778`
  `public static int[] TextAppearance = {android.R.attr.textSize, android.R.attr.typeface, android.R.attr.textStyle, android.R.attr.textColor, android.R.attr.textColorHint, android.R.attr.textColorLink, android.R.attr.shadowColor, android.R.attr.shadowDx, android.R.attr.shadowDy, android.R.attr.shadowR...`
- `sources/androidx/browser/browseractions/BrowserActionsFallbackMenuUi.java:63`
  `private PendingIntent buildShareAction() {`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:7`
  `import android.content.SharedPreferences;`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:86`
  `private static boolean shouldCleanUp(SharedPreferences sharedPreferences) {`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:87`
  `return System.currentTimeMillis() > sharedPreferences.getLong(BrowserServiceFileProvider.LAST_CLEANUP_TIME_KEY, System.currentTimeMillis()) + CLEANUP_REQUIRED_TIME_SPAN;`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:46`
  `public static final String EXTRA_DEFAULT_SHARE_MENU_ITEM = "android.support.customtabs.extra.SHARE_MENU_ITEM";`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:124`
  `private int mShareState = 0;`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:195`
  `public Builder addDefaultShareMenuItem() {`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:196`
  `setShareState(1);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:201`
  `public Builder setDefaultShareMenuItemEnabled(boolean z) {`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:203`
  `setShareState(1);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:205`
  `setShareState(2);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:210`
  `public Builder setShareState(int i) {`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:218`
  `this.mIntent.putExtra(CustomTabsIntent.EXTRA_DEFAULT_SHARE_MENU_ITEM, false);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:220`
  `this.mIntent.removeExtra(CustomTabsIntent.EXTRA_DEFAULT_SHARE_MENU_ITEM);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:376`
  `this.mIntent.putExtra(CustomTabsIntent.EXTRA_SHARE_STATE, this.mShareState);`
- `sources/androidx/browser/trusted/sharing/ShareData.java:25`
  `bundle.putString("androidx.browser.trusted.sharing.KEY_TITLE", this.title);`

## BR088

paper_id: B004
paper_title: Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation

- `sources/com/google/android/exoplayer2/ExoPlayerImpl.java:2227`
  `Log.w(TAG, invariant, this.hasNotifiedFullWrongThreadWarning ? null : new IllegalStateException());`
- `sources/com/google/android/exoplayer2/ExoPlayerImpl.java:2228`
  `this.hasNotifiedFullWrongThreadWarning = true;`
- `sources/com/google/android/exoplayer2/extractor/mp4/SefReader.java:67`
  `extractorInput.readFully(parsableByteArray.getData(), 0, 8);`
- `sources/kotlin/jvm/internal/AdaptedFunctionReference.java:7`
  `public class AdaptedFunctionReference implements FunctionBase, Serializable {`
- `sources/kotlin/jvm/internal/AdaptedFunctionReference.java:16`
  `public AdaptedFunctionReference(int i, Class cls, String str, String str2, int i2) {`
- `sources/kotlin/jvm/internal/AdaptedFunctionReference.java:20`
  `public AdaptedFunctionReference(int i, Object obj, Class cls, String str, String str2, int i2) {`
- `sources/kotlin/jvm/internal/AdaptedFunctionReference.java:47`
  `if (!(obj instanceof AdaptedFunctionReference)) {`
- `sources/kotlin/jvm/internal/AdaptedFunctionReference.java:50`
  `AdaptedFunctionReference adaptedFunctionReference = (AdaptedFunctionReference) obj;`
- `sources/kotlin/jvm/internal/AdaptedFunctionReference.java:51`
  `return this.isTopLevel == adaptedFunctionReference.isTopLevel && this.arity == adaptedFunctionReference.arity && this.flags == adaptedFunctionReference.flags && Intrinsics.areEqual(this.receiver, adaptedFunctionReference.receiver) && Intrinsics.areEqual(this.owner, adaptedFunctionReference.owner) &&...`
- `sources/org/mozilla/javascript/JavaAdapter.java:19`
  `public final class JavaAdapter implements IdFunctionCall {`
- `sources/org/mozilla/javascript/JavaAdapter.java:164`
  `int iFindCachedFunction = nativeJavaMethod.findCachedFunction(context, objArr2);`
- `sources/org/mozilla/javascript/JavaAdapter.java:165`
  `if (iFindCachedFunction < 0) {`
- `sources/org/mozilla/javascript/JavaAdapter.java:168`
  `objNewInstance = NativeJavaClass.constructInternal(objArr2, nativeJavaMethod.methods[iFindCachedFunction]);`
- `sources/org/mozilla/javascript/NativeJavaClass.java:116`
  `int iFindCachedFunction = nativeJavaMethod.findCachedFunction(context, objArr);`
- `sources/org/mozilla/javascript/NativeJavaClass.java:117`
  `if (iFindCachedFunction < 0) {`
- `sources/org/mozilla/javascript/NativeJavaClass.java:120`
  `return constructSpecific(context, scriptable, objArr, nativeJavaMethod.methods[iFindCachedFunction]);`
- `sources/org/mozilla/javascript/NativeJavaMethod.java:124`
  `int iFindCachedFunction = findCachedFunction(context, objArr);`
- `sources/org/mozilla/javascript/NativeJavaMethod.java:126`
  `if (iFindCachedFunction < 0) {`
- `sources/org/mozilla/javascript/NativeJavaMethod.java:129`
  `MemberBox memberBox = this.methods[iFindCachedFunction];`

## BR090

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `BRUHEALTH_AUDIT_REPORT.md:15`
  `- 只保留源码能直接支持的 confirmed 结论。`
- `BRUHEALTH_AUDIT_REPORT.md:18`
  `- 日志问题改为“敏感数据进入日志 sink”；Product 环境文件落盘未确认，不再写成生产文件日志 confirmed。`
- `BRUHEALTH_AUDIT_REPORT.md:38`
  `- 该风险不属于 'rule_catalog.tsv' 中的一个精确规则；它与隐私、WebView、位置数据相关，但数据库规则没有专门定义“WebView geolocation auto grant”。因此这里作为独立发现，不计入规则 confirmed。`
- `BRUHEALTH_AUDIT_REPORT.md:57`
  `- 目前已有桥能力证据，但尚未证明非可信 Web origin 能触达这些桥。因此本项按独立高风险链路记录，不直接作为 confirmed 漏洞。`
- `BRUHEALTH_AUDIT_REPORT.md:110`
  `## 2. Available Evidence`
- `BRUHEALTH_AUDIT_REPORT.md:145`
  `- 静态代码足够证明的项可以给 'confirmed'。`
- `BRUHEALTH_AUDIT_REPORT.md:154`
  `- 'confirmed'`
- `BRUHEALTH_AUDIT_REPORT.md:161`
  `- 单个权限不作为 confirmed。`
- `BRUHEALTH_AUDIT_REPORT.md:162`
  `- 单个 URL 不作为 confirmed。`
- `BRUHEALTH_AUDIT_REPORT.md:163`
  `- 单个 SDK 不作为 confirmed。`
- `BRUHEALTH_AUDIT_REPORT.md:164`
  `- 单个字符串不作为 confirmed。`
- `BRUHEALTH_AUDIT_REPORT.md:165`
  `- 静态 confirmed 只用于代码/配置本身足以构成风险的规则，例如空 TrustManager、全放行 HostnameVerifier、敏感 SQLite 明文表、SharedPreferences 明文 token/cookie、导出组件 + 实际处理逻辑。`
- `BRUHEALTH_AUDIT_REPORT.md:166`
  `- BLE、动态、云端规则没有设备/抓包时不强行 confirmed。`
- `BRUHEALTH_AUDIT_REPORT.md:174`
  `- BR009 'confirmed'`
- `BRUHEALTH_AUDIT_REPORT.md:175`
  `- BR010 'confirmed'`
- `BRUHEALTH_AUDIT_REPORT.md:176`
  `- BR012 'confirmed'`
- `BRUHEALTH_AUDIT_REPORT.md:227`
  `- BR010 'confirmed'`
- `BRUHEALTH_AUDIT_REPORT.md:228`
  `- BR012 'confirmed'`
- `BRUHEALTH_AUDIT_REPORT.md:271`
  `- BR047 'confirmed'`
- `BRUHEALTH_AUDIT_REPORT.md:330`
  `- Product 环境按源码字面调用关闭日志的分支，文件日志不能作为 Product confirmed。`
- `BRUHEALTH_AUDIT_REPORT.md:338`
  `- BR025 'confirmed'`
- `BRUHEALTH_AUDIT_REPORT.md:376`
  `- BR026 'confirmed'`
- `BRUHEALTH_AUDIT_REPORT.md:417`
  `- BR032 'confirmed'`
- `BRUHEALTH_AUDIT_REPORT.md:458`
  `为什么 BR032 confirmed：`
- `BRUHEALTH_AUDIT_REPORT.md:472`
  `- BR018 'confirmed'`
- `BRUHEALTH_AUDIT_REPORT.md:473`
  `- BR019 'confirmed'`
- `BRUHEALTH_AUDIT_REPORT.md:521`
  `为什么 BR018 / BR019 confirmed：`
- `BRUHEALTH_AUDIT_REPORT.md:592`
  `为什么不能 confirmed：`
- `BRUHEALTH_AUDIT_REPORT.md:619`
  `- BR080：静态日志 sink confirmed，但没有 logcat，因此动态规则 not_testable。`
- `BRUHEALTH_AUDIT_REPORT.md:677`
  `为什么不是 confirmed 云端风险：`
- `BRUHEALTH_AUDIT_REPORT.md:679`
  `- TLS 代码问题本身已在 BR009/BR010 confirmed。`
- `BRUHEALTH_AUDIT_REPORT.md:688`
  `- BR018 'confirmed'`
- `BRUHEALTH_AUDIT_REPORT.md:689`
  `- BR047 'confirmed'`
- `BRUHEALTH_AUDIT_REPORT.md:713`
  `- BR018 'confirmed'`
- `BRUHEALTH_AUDIT_REPORT.md:733`
  `- BR032 'confirmed'`
- `BRUHEALTH_AUDIT_REPORT.md:750`
  `- 所以不能把 token 泄露定为 confirmed。`
- `BRUHEALTH_AUDIT_REPORT.md:763`
  `- 未见业务域 HTTP 明文配置；debug connection spec 的 CLEARTEXT 不作为生产 confirmed。`
- `BRUHEALTH_EVIDENCE_CHAINS.md:1`
  `# BruHealth evidence chains`
- `BRUHEALTH_EVIDENCE_CHAINS.md:16`
  `- BR009 'confirmed'`
- `BRUHEALTH_EVIDENCE_CHAINS.md:17`
  `- BR010 'confirmed'`
- `BRUHEALTH_EVIDENCE_CHAINS.md:18`
  `- BR012 'confirmed'`
- `BRUHEALTH_EVIDENCE_CHAINS.md:19`
  `- BR018 'confirmed'`
- `BRUHEALTH_EVIDENCE_CHAINS.md:104`
  `- BR010 'confirmed'`
- `BRUHEALTH_EVIDENCE_CHAINS.md:105`
  `- BR012 'confirmed'`
- `BRUHEALTH_EVIDENCE_CHAINS.md:158`
  `- BR018 'confirmed'`
- `BRUHEALTH_EVIDENCE_CHAINS.md:159`
  `- BR047 'confirmed'`
- `BRUHEALTH_EVIDENCE_CHAINS.md:180`
  `- 因此不能把 Product 环境文件落盘写成 confirmed；只能确认存在日志 sink 和非 Product 文件日志风险。`
- `BRUHEALTH_EVIDENCE_CHAINS.md:255`
  `- BR026 'confirmed'`
- `BRUHEALTH_EVIDENCE_CHAINS.md:256`
  `- BR047 'confirmed'（与 HTTP logs 交叉）`
- `BRUHEALTH_EVIDENCE_CHAINS.md:308`
  `- BR025 'confirmed'`
- `BRUHEALTH_EVIDENCE_CHAINS.md:309`
  `- BR014 'confirmed'`
- `BRUHEALTH_EVIDENCE_CHAINS.md:310`
  `- BR015 'confirmed'`
- `BRUHEALTH_EVIDENCE_CHAINS.md:373`
  `- BR032 'confirmed'`
- `BRUHEALTH_EVIDENCE_CHAINS.md:447`
  `- BR018 'confirmed'`
- `BRUHEALTH_EVIDENCE_CHAINS.md:599`
  `为什么不是 confirmed：`
- `BRUHEALTH_EVIDENCE_CHAINS.md:650`
  `- B014 / Android medical app data storage evidence organization.`
- `BRUHEALTH_EVIDENCE_CHAINS.md:662`
  `- 静态层不支持 BR028 confirmed。`
- `BRUHEALTH_EVIDENCE_CHAINS.md:671`
  `- BR058 'confirmed'`
- `BRUHEALTH_EVIDENCE_CHAINS.md:695`
  `为什么 BR058 confirmed：`
- `BRUHEALTH_SOURCE_PAPER_REVIEW.md:31`
  `- 所以不能再写成“生产环境 confirmed 文件日志泄露”。更准确是：健康/位置/HTTP BODY 等敏感信息进入日志 sink；非生产或非 Product 环境落文件风险明确；Product 环境是否另有日志分发器或配置需要运行时确认。`
- `BRUHEALTH_SOURCE_PAPER_REVIEW.md:39`
  `3. “第三方共享/云端泄露”不能 confirmed。`
- `BRUHEALTH_SOURCE_PAPER_REVIEW.md:45`
  `4. “BLE 漏洞”不能 confirmed。`
- `BRUHEALTH_SOURCE_PAPER_REVIEW.md:360`
  `- 删除“生产文件日志 confirmed”。`
- `BRUHEALTH_SOURCE_PAPER_REVIEW.md:546`
  `- 报告中把 BLE 写成“强支持的待测假设”，不要写成 confirmed 漏洞。`
- `BRUHEALTH_SOURCE_PAPER_REVIEW.md:566`
  `### F-12 Backup 和外部存储：当前证据不支持备份泄露 confirmed`
- `BRUHEALTH_SOURCE_PAPER_REVIEW.md:584`
  `导师判断：旧报告中如果只是弱提示可以保留；如果作为 confirmed 漏洞则不准确。`
- `BRUHEALTH_SOURCE_PAPER_REVIEW.md:747`
  `当前不能写 confirmed，但应安排实测。`
- `BRUHEALTH_SOURCE_PAPER_REVIEW.md:766`
  `1. 原表述：生产文件日志 confirmed。`
- `BRUHEALTH_SOURCE_PAPER_REVIEW.md:767`
  `- 修正：敏感数据进入日志 sink confirmed；Product 文件落盘不确认，按源码反而可能关闭；非 Product 文件日志风险确认。`

## BR091

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/com/evyd/core/mobile/android/health/net/HealthAPI.java:25`
  `@POST("/api/routines/app/exercise/end")`
- `sources/com/evyd/core/mobile/android/health/net/HealthAPI.java:28`
  `@GET("/api/routines/app/exercise/get-current")`
- `sources/com/evyd/core/mobile/android/health/net/HealthAPI.java:31`
  `@GET("/api/campaign/challenge/app/challenge/v2/get-merchant")`
- `sources/com/evyd/core/mobile/android/health/net/HealthAPI.java:34`
  `@GET("/api/routines-dc/adapter/data/upload-status")`
- `sources/com/evyd/core/mobile/android/health/net/HealthAPI.java:38`
  `@POST("/api/routines-dc/adapter/data/upload")`
- `sources/com/evyd/core/mobile/android/health/net/HealthAPI.java:41`
  `@POST("/api/routines/app/exercise/upload-route-screenshot")`
- `sources/com/evyd/core/mobile/android/health/net/HealthAPI.java:42`
  `@Multipart`
- `sources/com/evyd/core/mobile/android/health/net/HealthAPI.java:45`
  `@POST("/api/routines/app/exercise/pause")`
- `sources/com/evyd/core/mobile/android/health/net/HealthAPI.java:48`
  `@POST("/api/routines/app/exercise/resume")`
- `sources/com/evyd/core/mobile/android/health/net/HealthAPI.java:51`
  `@POST("/api/routines/app/exercise/upload-track-report")`
- `sources/egnc/moh/base/compat/ConfigService.java:10`
  `@GET("api/configuration/app/conf/get_app_attr?key_name=camera_passport_position")`
- `sources/egnc/moh/base/compat/ConfigService.java:13`
  `@GET("api/configuration/app/conf/get_app_attr")`
- `sources/egnc/moh/base/compat/ConfigService.java:16`
  `@GET("api/configuration/app/conf/get_app_attr")`
- `sources/egnc/moh/base/utils/eventlog/interfaces/LogService.java:10`
  `@POST("api/eventlog/multi_action")`
- `sources/egnc/moh/base/web/manager/switchMember/services/SkipBiometricService.java:14`
  `@POST("/api/wlapp-user/user/cancel-skip-pwd")`
- `sources/egnc/moh/base/web/manager/switchMember/services/SkipBiometricService.java:17`
  `@POST("/api/wlapp-user/user/enable-skip-pwd")`
- `sources/egnc/moh/base/web/manager/switchMember/services/SwitchMemberServices.java:15`
  `@POST("/api/wlapp-user/auth/check_pwd")`
- `sources/egnc/moh/base/web/manager/switchMember/services/SwitchMemberServices.java:18`
  `@POST("/api/wlapp-user/auth/need_pwd_check")`
- `sources/egnc/moh/bruhealth/health/net/HealthAPI.java:27`
  `@POST("/api/bnotm/app/activity/end")`
- `sources/egnc/moh/bruhealth/health/net/HealthAPI.java:30`
  `@GET("/api/bnotm/app/activity/detail")`
- `sources/egnc/moh/bruhealth/health/net/HealthAPI.java:33`
  `@GET("/api/data-collector/app/global/data/upload-status")`
- `sources/egnc/moh/bruhealth/health/net/HealthAPI.java:37`
  `@POST("/api/data-collector/app/global/data/upload")`
- `sources/egnc/moh/bruhealth/health/net/HealthAPI.java:40`
  `@POST("/api/bnotm/app/activity/upload-route-screenshot")`
- `sources/egnc/moh/bruhealth/health/net/HealthAPI.java:41`
  `@Multipart`
- `sources/egnc/moh/bruhealth/health/net/HealthAPI.java:44`
  `@POST("/api/data-collector/app/global/data/health/upload")`
- `sources/egnc/moh/bruhealth/health/net/HealthAPI.java:47`
  `@POST("/api/bnotm/app/activity/pause")`
- `sources/egnc/moh/bruhealth/health/net/HealthAPI.java:50`
  `@POST("/api/bnotm/app/activity/resume")`
- `sources/egnc/moh/bruhealth/health/net/HealthAPI.java:54`
  `@POST("/api/data-collector/app/global/data/upload/supplement")`
- `sources/egnc/moh/bruhealth/health/net/HealthAPI.java:57`
  `@POST("/api/bnotm/app/activity/track-report")`
- `sources/egnc/moh/bruhealth/health/net/HealthAPI.java:60`
  `@POST("/api/bnotm/app/activity/change-status")`
- `sources/egnc/moh/bruhealth/login/remote/LoginService.java:18`
  `@POST("/api/wlapp-user/auth/get_exist_identity")`
- `sources/egnc/moh/bruhealth/login/remote/LoginService.java:21`
  `@POST("/api/wlapp-user/member/id-check-and-update")`
- `sources/egnc/moh/bruhealth/login/remote/LoginService.java:24`
  `@POST("/api/wlapp-user/member/id_number_status")`
- `sources/egnc/moh/bruhealth/login/remote/LoginService.java:27`
  `@POST("/api/wlapp-user/member/pwd")`
- `sources/egnc/moh/bruhealth/login/remote/LoginService.java:30`
  `@POST("/api/wlapp-user/member/newborn/parent/info")`
- `sources/egnc/moh/bruhealth/login/remote/LoginService.java:33`
  `@GET("/api/wlapp-user/auth/member_info")`
- `sources/egnc/moh/bruhealth/login/remote/LoginService.java:36`
  `@POST("/api/wlapp-user/auth/get_mobile_state")`
- `sources/egnc/moh/bruhealth/login/remote/LoginService.java:39`
  `@GET("/api/wlapp-user/auth/get_token_state")`
- `sources/egnc/moh/bruhealth/login/remote/LoginService.java:42`
  `@GET("/api/wlapp-user/member/highest_level_id")`
- `sources/egnc/moh/bruhealth/login/remote/LoginService.java:45`
  `@POST("/api/wlapp-user/auth/login")`

## BR092

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/androidx/activity/ComponentActivity.java:501`
  `if (!TextUtils.equals(e.getMessage(), "Can not perform this action after onSaveInstanceState")) {`
- `sources/androidx/activity/compose/ActivityResultRegistryKt.java:16`
  `import androidx.compose.runtime.saveable.RememberSaveableKt;`
- `sources/androidx/activity/compose/ActivityResultRegistryKt.java:17`
  `import androidx.compose.runtime.saveable.Saver;`
- `sources/androidx/activity/compose/ReportDrawnKt.java:3`
  `import androidx.activity.FullyDrawnReporter;`
- `sources/androidx/activity/compose/ReportDrawnKt.java:4`
  `import androidx.activity.FullyDrawnReporterOwner;`
- `sources/androidx/activity/compose/ReportDrawnKt.java:57`
  `ReportDrawnKt.ReportDrawnWhen(function0, composer2, i | 1);`
- `sources/androidx/activity/compose/ReportDrawnKt.java:62`
  `EffectsKt.DisposableEffect(fullyDrawnReporter, function0, new Function1<DisposableEffectScope, DisposableEffectResult>() { // from class: androidx.activity.compose.ReportDrawnKt.ReportDrawnWhen.1`
- `sources/androidx/activity/compose/ReportDrawnKt.java:70`
  `if (!fullyDrawnReporter.isFullyDrawnReported()) {`
- `sources/androidx/activity/compose/ReportDrawnKt.java:71`
  `final ReportDrawnComposition reportDrawnComposition = new ReportDrawnComposition(fullyDrawnReporter, function0);`
- `sources/androidx/activity/compose/ReportDrawnKt.java:72`
  `return new DisposableEffectResult() { // from class: androidx.activity.compose.ReportDrawnKt$ReportDrawnWhen$1$invoke$$inlined$onDispose$2`
- `sources/androidx/activity/compose/ReportDrawnKt.java:75`
  `reportDrawnComposition.removeReporter();`
- `sources/androidx/activity/compose/ReportDrawnKt.java:79`
  `return new DisposableEffectResult() { // from class: androidx.activity.compose.ReportDrawnKt$ReportDrawnWhen$1$invoke$$inlined$onDispose$1`
- `sources/androidx/appcompat/R.java:1558`
  `public static int[] SearchView = {android.R.attr.textAppearance, android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.text, android.R.attr.hint, android.R.attr.inputType, android.R.attr.imeOptions, egnc.moh.bruhealth.R.attr.animateMenuItems, egnc.moh.bruhealth.R.attr.animateNavigationIc...`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2784`
  `return Api21Impl.isPowerSaveMode(this.mPowerManager) ? 2 : 1;`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2944`
  `static boolean isPowerSaveMode(PowerManager powerManager) {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2945`
  `return powerManager.isPowerSaveMode();`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:196`
  `canvas.save();`
- `sources/androidx/appcompat/view/menu/ActionMenuItemView.java:105`
  `this.mSavedPaddingLeft = i;`
- `sources/androidx/appcompat/widget/ActionMenuPresenter.java:473`
  `public Parcelable onSaveInstanceState() {`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:170`
  `synchronized (this.mInstanceLock) {`
- `sources/androidx/appcompat/widget/AppCompatRatingBar.java:31`
  `protected synchronized void onMeasure(int i, int i2) {`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:138`
  `int iSave = canvas.save();`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:144`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:31`
  `private boolean mAsyncFontPending;`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:260`
  `AppCompatTextHelper.this.onAsyncTypefaceReceived(weakReference, typeface);`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:270`
  `this.mAsyncFontPending = this.mFontTypeface == null;`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:105`
  `ViewCompat.saveAttributeDataForStyleable(textView, textView.getContext(), R.styleable.AppCompatTextView, attributeSet, typedArrayObtainStyledAttributes, i, 0);`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:309`
  `synchronized (rectF) {`
- `sources/androidx/appcompat/widget/SearchView.java:89`
  `private final View mSubmitArea;`
- `sources/androidx/appcompat/widget/SearchView.java:90`
  `private boolean mSubmitButtonEnabled;`
- `sources/androidx/appcompat/widget/SwitchCompat.java:912`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/biometric/R.java:1773`
  `public static int[] SearchView = {android.R.attr.textAppearance, android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.text, android.R.attr.hint, android.R.attr.inputType, android.R.attr.imeOptions, egnc.moh.bruhealth.R.attr.animateMenuItems, egnc.moh.bruhealth.R.attr.animateNavigationIc...`
- `sources/androidx/biometric/ktx/R.java:1773`
  `public static int[] SearchView = {android.R.attr.textAppearance, android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.text, android.R.attr.hint, android.R.attr.inputType, android.R.attr.imeOptions, egnc.moh.bruhealth.R.attr.animateMenuItems, egnc.moh.bruhealth.R.attr.animateNavigationIc...`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:38`
  `private static class FileCleanupTask extends AsyncTask<Void, Void, Void> {`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:448`
  `return FutureChain.from(Futures.transformAsyncOnCompletion(captureSession.open(builder.build(), cameraDevice, this.mCaptureSessionOpenerBuilder.build()))).transformAsync(new AsyncFunction() { // from class: androidx.camera.camera2.internal.Camera2CameraImpl$$ExternalSyntheticLambda12`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:449`
  `@Override // androidx.camera.core.impl.utils.futures.AsyncFunction`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1378`
  `void submitCaptureRequests(List<CaptureConfig> list) {`
- `sources/androidx/camera/camera2/internal/Camera2CapturePipeline.java:80`
  `public ListenableFuture<List<Void>> submitStillCaptures(List<CaptureConfig> list, int i, int i2, int i3) {`
- `sources/androidx/camera/camera2/internal/Camera2CapturePipeline.java:330`
  `return "submitStillCapture";`
- `sources/androidx/camera/camera2/internal/Camera2RequestProcessor.java:112`
  `synchronized (this.mLock) {`

## BR093

paper_id: B004
paper_title: Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation

- `sources/androidx/activity/compose/ActivityResultRegistryKt.java:16`
  `import androidx.compose.runtime.saveable.RememberSaveableKt;`
- `sources/androidx/activity/compose/ActivityResultRegistryKt.java:17`
  `import androidx.compose.runtime.saveable.Saver;`
- `sources/androidx/activity/compose/ActivityResultRegistryKt.java:34`
  `String str = (String) RememberSaveableKt.m2965rememberSaveable(new Object[0], (Saver) null, (String) null, (Function0) new Function0<String>() { // from class: androidx.activity.compose.ActivityResultRegistryKt$rememberLauncherForActivityResult$key$1`
- `sources/androidx/compose/material/internal/ExposedDropdownMenuPopupKt.java:141`
  `UUID popupId = (UUID) RememberSaveableKt.m2965rememberSaveable(new Object[0], (Saver) null, (String) null, (Function0) new Function0<UUID>() { // from class: androidx.compose.material.internal.ExposedDropdownMenuPopupKt$ExposedDropdownMenuPopup$popupId$1`
- `sources/androidx/compose/material/internal/PopupLayout.java:35`
  `import androidx.savedstate.ViewTreeSavedStateRegistryOwner;`
- `sources/androidx/compose/material3/ModalBottomSheetWindow.java:20`
  `import androidx.savedstate.ViewTreeSavedStateRegistryOwner;`
- `sources/androidx/compose/material3/ModalBottomSheetWindow.java:31`
  `@Metadata(d1 = {"\u0000^\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0010\b\n\u0002\b\u0003\n\u0002\u00...`
- `sources/androidx/compose/material3/ModalBottomSheetWindow.java:57`
  `public ModalBottomSheetWindow(Function0<Unit> onDismissRequest, View composeView, UUID saveId) {`
- `sources/androidx/compose/material3/ModalBottomSheetWindow.java:60`
  `Intrinsics.checkNotNullParameter(saveId, "saveId");`
- `sources/androidx/compose/material3/ModalBottomSheet_androidKt.java:496`
  `UUID id = (UUID) RememberSaveableKt.m2965rememberSaveable(new Object[0], (Saver) null, (String) null, (Function0) new Function0<UUID>() { // from class: androidx.compose.material3.ModalBottomSheet_androidKt$ModalBottomSheetPopup$id$1`
- `sources/androidx/compose/material3/TimePickerKt.java:348`
  `Saver<TextFieldValue, Object> saver = TextFieldValue.INSTANCE.getSaver();`
- `sources/androidx/compose/material3/TimePickerKt.java:390`
  `final MutableState mutableStateRememberSaveable2 = RememberSaveableKt.rememberSaveable(objArr2, (Saver) saver2, (String) null, (Function0) objRememberedValue2, composerStartRestartGroup, 72, 4);`
- `sources/androidx/compose/material3/TimePickerKt.java:457`
  `final MutableState<TextFieldValue> mutableState = mutableStateRememberSaveable;`
- `sources/androidx/compose/material3/TimePickerKt.java:489`
  `TextFieldValue textFieldValueTimeInputImpl$lambda$5 = TimePickerKt.TimeInputImpl$lambda$5(mutableStateRememberSaveable);`
- `sources/androidx/compose/material3/TimePickerKt.java:491`
  `final MutableState<TextFieldValue> mutableState2 = mutableStateRememberSaveable;`
- `sources/androidx/compose/material3/TimePickerKt.java:576`
  `final MutableState<TextFieldValue> mutableState3 = mutableStateRememberSaveable2;`
- `sources/androidx/compose/material3/TimePickerKt.java:608`
  `TextFieldValue textFieldValueTimeInputImpl$lambda$8 = TimePickerKt.TimeInputImpl$lambda$8(mutableStateRememberSaveable2);`
- `sources/androidx/compose/material3/TimePickerKt.java:610`
  `final MutableState<TextFieldValue> mutableState4 = mutableStateRememberSaveable2;`
- `sources/androidx/compose/material3/internal/ExposedDropdownMenuPopupKt.java:142`
  `UUID popupId = (UUID) RememberSaveableKt.m2965rememberSaveable(new Object[0], (Saver) null, (String) null, (Function0) new Function0<UUID>() { // from class: androidx.compose.material3.internal.ExposedDropdownMenuPopupKt$ExposedDropdownMenuPopup$popupId$1`
- `sources/androidx/compose/material3/internal/PopupLayout.java:35`
  `import androidx.savedstate.ViewTreeSavedStateRegistryOwner;`
- `sources/androidx/compose/ui/window/DialogWrapper.java:27`
  `import androidx.savedstate.ViewTreeSavedStateRegistryOwner;`
- `sources/androidx/compose/ui/window/PopupLayout.java:39`
  `import androidx.savedstate.ViewTreeSavedStateRegistryOwner;`
- `sources/androidx/datastore/preferences/protobuf/ExtensionRegistryLite.java:41`
  `synchronized (ExtensionRegistryLite.class) {`
- `sources/androidx/health/platform/client/proto/ExtensionRegistryLite.java:53`
  `synchronized (ExtensionRegistryLite.class) {`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:257`
  `synchronized (DeviceUtils.class) {`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:275`
  `return saveUdid(str + 2, androidID);`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:279`
  `return saveUdid(str + 9, "");`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:310`
  `private static String saveUdid(String str, String str2) {`
- `sources/com/evyd/core/mobile/android/health/newtrack/NewTrackLogActivity.java:14`
  `@Metadata(d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u000b\n\u0002\u0010\t\n\u0000\n\u0002\u0010\u0002\n\u0002\b\u0007\n\u0002\u0018\u0002\n\u0002\b\u0004\b\u0017\u0018\u0000 \u001d2\u00020\u0001:\u0001\u001dB\u0005¢\u0006\u0002\u0010\u0002J\...`
- `sources/com/evyd/core/mobile/android/health/newtrack/NewTrackLogActivity.java:32`
  `LogReportUtils.getInstance().lastPageId = LogReportUtils.getInstance().currentPageId;`
- `sources/com/evyd/core/mobile/android/health/newtrack/NewTrackLogActivity.java:33`
  `LogReportUtils.getInstance().currentPageId = "pa_time_tracker";`
- `sources/com/evyd/core/mobile/android/health/newtrack/NewTrackLogActivity.java:34`
  `LogReportUtils.getInstance().addSkimLog(this.pageName, LogReportUtils.getInstance().lastPageId, this.pageId, "", this.moduleName, MapsKt.emptyMap(), MapsKt.mapOf(TuplesKt.to("source", getSource()), TuplesKt.to("id", getId())));`
- `sources/com/evyd/core/mobile/android/health/newtrack/NewTrackLogActivity.java:60`
  `LogReportUtils.getInstance().addStayLog(this.pageName, Calendar.getInstance().getTimeInMillis() - this.visitDate, this.pageId, "", this.moduleName, MapsKt.emptyMap(), MapsKt.mapOf(TuplesKt.to("source", getSource()), TuplesKt.to("id", getId())));`
- `sources/com/evyd/core/trtc/GlobalVideoState.java:74`
  `synchronized (getClass()) {`
- `sources/com/evyd/core/trtc/GlobalVideoState.java:86`
  `synchronized (getClass()) {`
- `sources/com/evyd/core/trtc/GlobalVideoState.java:95`
  `synchronized (getClass()) {`
- `sources/com/evyd/core/trtc/GlobalVideoState.java:107`
  `synchronized (getClass()) {`
- `sources/com/evyd/core/trtc/TRTCVideoActivity.java:131`
  `@Metadata(d1 = {"\u0000ê\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u00...`
- `sources/com/evyd/core/trtc/net/IVideoProvider.java:21`
  `@Metadata(d1 = {"\u0000b\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0005\n\u0002\u0010$\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\u0010\u000b\n\u0002\b\u0005\n\u0002\u0010\t\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\...`
- `sources/com/evyd/core/trtcroom/room/TRTCVideoRoomActivity.java:897`
  `private static void saveUserInfo(Context context, String str, String str2) {`

## BR094

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `sources/android/support/customtabs/ICustomTabsCallback.java:44`
  `public void onPostMessage(String str, Bundle bundle) throws RemoteException {`
- `sources/android/support/customtabs/ICustomTabsCallback.java:62`
  `void onPostMessage(String str, Bundle bundle) throws RemoteException;`
- `sources/android/support/customtabs/ICustomTabsCallback.java:72`
  `static final int TRANSACTION_onPostMessage = 5;`
- `sources/android/support/customtabs/ICustomTabsCallback.java:116`
  `onPostMessage(parcel.readString(), (Bundle) _Parcel.readTypedObject(parcel, Bundle.CREATOR));`
- `sources/android/support/customtabs/ICustomTabsService.java:94`
  `boolean requestPostMessageChannelWithExtras(ICustomTabsCallback iCustomTabsCallback, Uri uri, Bundle bundle) throws RemoteException;`
- `sources/android/support/customtabs/ICustomTabsService.java:107`
  `static final int TRANSACTION_postMessage = 8;`
- `sources/android/support/customtabs/ICustomTabsService.java:109`
  `static final int TRANSACTION_requestPostMessageChannel = 7;`
- `sources/android/support/customtabs/ICustomTabsService.java:110`
  `static final int TRANSACTION_requestPostMessageChannelWithExtras = 11;`
- `sources/android/support/customtabs/ICustomTabsService.java:176`
  `int iPostMessage = postMessage(ICustomTabsCallback.Stub.asInterface(parcel.readStrongBinder()), parcel.readString(), (Bundle) _Parcel.readTypedObject(parcel, Bundle.CREATOR));`
- `sources/android/support/customtabs/ICustomTabsService.java:178`
  `parcel2.writeInt(iPostMessage);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1929`
  `synchronized (MediaSessionImplBase.this.mLock) {`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:2008`
  `postToHandler(10, uri, extras);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:2013`
  `postToHandler(11, Long.valueOf(id));`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:2018`
  `postToHandler(12);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:2043`
  `postToHandler(17);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:2048`
  `postToHandler(18, Long.valueOf(pos));`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:2053`
  `postToHandler(19, rating);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:2430`
  `MediaSessionImplApi18.this.postToHandler(18, -1, -1, Long.valueOf(newPositionMs), null);`
- `sources/androidx/activity/ComponentActivity.java:785`
  `class ReportFullyDrawnExecutorApi16Impl implements ReportFullyDrawnExecutor, ViewTreeObserver.OnDrawListener, Runnable {`
- `sources/androidx/activity/ComponentActivity.java:790`
  `ReportFullyDrawnExecutorApi16Impl() {`
- `sources/androidx/activity/compose/ComponentActivityKt.java:11`
  `import androidx.savedstate.ViewTreeSavedStateRegistryOwner;`
- `sources/androidx/activity/compose/LocalFullyDrawnReporterOwner.java:17`
  `/* JADX INFO: compiled from: ReportDrawn.kt */`
- `sources/androidx/activity/result/ActivityResultRegistry.java:162`
  `public final void onSaveInstanceState(Bundle bundle) {`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:24`
  `@Metadata(d1 = {"\u0000\u000e\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0000\n\u0002\b\u0006\u0018\u0000*\u0004\b\u0002\u0010\u00012\u00020\u0002B\r\u0012\u0006\u0010\u0003\u001a\u00028\u0002¢\u0006\u0002\u0010\u0004R\u0013\u0010\u0003\u001a\u00028\u0002¢\u0006\n\n\u0002\u0010\u0007\u001a\u0004\b\u...`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:25`
  `public static final class SynchronousResult<T> {`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:28`
  `public SynchronousResult(T t) {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:129`
  `boolean mInvalidatePanelMenuPosted;`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:311`
  `syncRequestedAndStoredLocales(context);`
- `sources/androidx/appcompat/app/AppCompatViewInflater.java:52`
  `/* JADX WARN: Failed to restore switch over string. Please report as a decompilation issue */`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:196`
  `canvas.save();`
- `sources/androidx/appcompat/view/menu/ListMenuPresenter.java:150`
  `public void saveHierarchyState(Bundle bundle) {`
- `sources/androidx/appcompat/widget/ActivityChooserView.java:93`
  `ViewCompat.saveAttributeDataForStyleable(this, context, R.styleable.ActivityChooserView, attributeSet, typedArrayObtainStyledAttributes, i, 0);`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:138`
  `int iSave = canvas.save();`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:144`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/appcompat/widget/ForwardingListener.java:136`
  `r0.postDelayed(r6, r3)`
- `sources/androidx/appcompat/widget/ForwardingListener.java:146`
  `r0.postDelayed(r6, r3)`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:65`
  `public static synchronized ResourceManagerInternal get() {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:83`
  `public synchronized void setHooks(ResourceManagerHooks resourceManagerHooks) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:110`
  `public synchronized void onConfigurationChanged(Context context) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:222`
  `private synchronized Drawable getCachedDrawable(Context context, long j) {`

## BR095

paper_id: B025
paper_title: Why Eve and Mallory Still Love Android: Revisiting TLS (In)Security in Android Applications

- `resources/assets/mobile.v2.22.1.html:877`
  `// Reference: http://es5.github.io/#x15.4.4.14`
- `resources/assets/html-de/sharing.html:12`
  `<p>Um QR-Codes auf Ihrem Computer zu erzeugen, testen Sie den ZXing QR Code Generator, er basiert auf dem selben Quelltext wie dieses Programm: <a href="http://zxing.appspot.com/generator/">http://zxing.appspot.com/generator/</a></p>`
- `resources/assets/html-en/index.html:10`
  `<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>`
- `resources/assets/html-en/sharing.html:12`
  `<p>To generate QR Codes from your computer, try the ZXing QR Code Generator: <a href="http://zxing.appspot.com/generator/">http://zxing.appspot.com/generator/</a></p>`
- `resources/assets/html-es/index.html:10`
  `<a href="http://github.com/zxing/zxing"> http://github.com/zxing/zxing </a></p>`
- `resources/assets/html-es/license.html:34`
  `<p> Este proyecto se basa en la <a class="notranslate" href="http://github.com/zxing/zxing">ZXing</a> código de barras`
- `resources/assets/html-es/license.html:36`
  `<a class="notranslate" href="http://www.apache.org/licenses/LICENSE-2.0.html">Apache License 2.0</a> : </p>`
- `resources/assets/html-es/sharing.html:12`
  `<p> Para generar códigos QR desde su computadora, pruebe el generador ZXing Código QR: <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-fr/index.html:10`
  `<a href="http://github.com/zxing/zxing"> http://github.com/zxing/zxing </a></p>`
- `resources/assets/html-fr/sharing.html:12`
  `<p> Pour générer les codes QR à partir de votre ordinateur, essayez le générateur de code QR ZXing: <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-it/sharing.html:12`
  `<p> Per generare i codici QR dal tuo computer, provare il generatore di ZXing QR Code: <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-ja/sharing.html:12`
  `<p>パソコンからQRコードを生成するには、ZXing QR Code Generator (<a href="http://zxing.appspot.com/generator/">http://zxing.appspot.com/generator/</a>)をご利用ください。</p>`
- `resources/assets/html-ko/sharing.html:12`
  `<p> 컴퓨터에서 QR 코드를 생성하려면 ZXing QR 코드 생성기를 사용해 : <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-nl/sharing.html:12`
  `<p> Om QR Codes van uw computer te genereren, probeer dan de ZXing QR Code Generator: <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-pt/sharing.html:12`
  `<p> Para gerar QR Codes do seu computador, experimente a Gerador de código QR ZXing: <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-ru/sharing.html:12`
  `<p> Для создания QR-коды с компьютера, попробуйте ZXing QR Генератор кода: <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-uk/sharing.html:12`
  `<p> Для створення QR-кода з комп'ютеру, спробуйте ZXing QR Генератор: <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-zh-rCN/sharing.html:12`
  `<p> 在电脑上可以使用 ZXing 二维码生成器： <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-zh-rHK/sharing.html:12`
  `<p>要從您的電腦產生 QR Code，請試用 ZXing QR Code 產生器（英文）：<a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-zh-rTW/sharing.html:12`
  `<p>要從您的電腦產生 QR Code，請試用 ZXing QR Code 產生器（英文）：<a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/www/index.html:1`
  `<!DOCTYPE html><html lang=en><head><meta charset=utf-8><meta http-equiv=X-UA-Compatible content="IE=edge"><meta name=viewport content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=0,viewport-fit=cover"><meta http-equiv=Content-Security-Policy content="default-src 'self' data: gap...`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:26`
  `var i=Object.freeze({}),r=Array.isArray;function o(t){return void 0===t||null===t}function a(t){return void 0!==t&&null!==t}function s(t){return!0===t}function l(t){return!1===t}function u(t){return"string"===typeof t||"number"===typeof t||"symbol"===typeof t||"boolean"===typeof t}function c(t){retu...`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:32`
  `* Based on Underscore.js 1.8.3 <http://underscorejs.org/LICENSE>`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:47`
  `var i=n("b639"),r=i.Buffer;function o(t,e){for(var n in t)e[n]=t[n]}function a(t,e,n){return r(t,e,n)}r.from&&r.alloc&&r.allocUnsafe&&r.allocUnsafeSlow?t.exports=i:(o(i,e),e.Buffer=a),a.prototype=Object.create(r.prototype),o(r,a),a.from=function(t,e,n){if("number"===typeof t)throw new TypeError("Arg...`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:83`
  `/*! http://mths.be/fromcodepoint v0.2.1 by @mathias */`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:84`
  `String.fromCodePoint||function(){var t=function(){try{var t={},e=Object.defineProperty,n=e(t,t,t)&&e}catch(i){}return n}(),e=String.fromCharCode,n=Math.floor,i=function(t){var i,r,o=16384,a=[],s=-1,l=arguments.length;if(!l)return"";var u="";while(++s<l){var c=Number(arguments[s]);if(!isFinite(c)||c<...`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:107`
  `* @author   Feross Aboukhadijeh <http://feross.org>`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:113`
  `᠎";t.exports=function(t){return r((function(){return!!o[t]()||a[t]()!==a||i&&o[t].name!==t}))}},c8ef:function(t,e,n){var i=n("6d8b"),r=n("a15a"),o=r.createSymbol,a=n("2306"),s=a.Group,l=n("3842"),u=l.parsePercent,c=n("1418"),h=3;function f(t){return i.isArray(t)||(t=[+t,+t]),t}function d(t,e){var n=...`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:117`
  `* @author   Feross Aboukhadijeh <feross@feross.org> <http://feross.org>`
- `resources/assets/www/plugins/cordova-plugin-camera/www/Camera.js:106`
  `* - Save the data locally ('LocalStorage', [Lawnchair](http://brianleroux.github.com/lawnchair/), etc.)`
- `resources/assets/www/plugins/cordova-plugin-file-transfer/www/FileTransfer.js:51`
  `// Proof: http://social.msdn.microsoft.com/Forums/windowsapps/en-US/a327cf3c-f033-4a54-8b7f-03c56ba3203f/windows-foundation-uri-security-problem`
- `resources/res/drawable/abc_ic_ab_back_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_arrow_drop_right_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_clear_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_go_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_menu_copy_mtrl_am_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_menu_cut_mtrl_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_menu_overflow_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_menu_paste_mtrl_am_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_menu_selectall_mtrl_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_menu_share_mtrl_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_voice_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_list_divider_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:tint="?android:attr/colorForeground">`
- `resources/res/drawable/abc_seekbar_tick_mark_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/abc_star_black_48dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_star_half_black_48dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_text_cursor_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/res/drawable/abc_vector_test.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/avd_hide_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_hide_password__0_res_0x7f080000">`
- `resources/res/drawable/avd_show_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_show_password__0_res_0x7f080003">`
- `resources/res/drawable/btn_checkbox_checked_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/btn_checkbox_unchecked_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/btn_radio_off_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/btn_radio_on_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/design_ic_visibility.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/design_ic_visibility_off.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/gallery_bg_select_circle_true_photos.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/gallery_ic_album_items_name_photos.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/gallery_ic_album_item_chosed.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/gallery_ic_camera_photos.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/gallery_ic_selector_photos.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/gallery_ic_selector_true_photos.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_arrow_back_black_24.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_b_splash.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/res/drawable/ic_clear_black_24.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_clock_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_keyboard_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_launcher_background.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_m3_chip_check.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_m3_chip_checked_circle.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_m3_chip_close.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_mtrl_checked_circle.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_mtrl_chip_checked_black.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_mtrl_chip_checked_circle.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_mtrl_chip_close_circle.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_search_black_24.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_t_splash.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/m3_avd_hide_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_m3_avd_hide_password__0_res_0x7f080008">`
- `resources/res/drawable/m3_avd_show_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_m3_avd_show_password__0_res_0x7f08000b">`

## BR096

paper_id: B011
paper_title: Locking it down: The privacy and security of mobile medication apps

- `resources/assets/flutter_assets/config/welcome.json:12`
  `"en": "https://healthresource-1258280810.picsgp.myqcloud.com/6d206c60-5348-4dcb-b613-0e225a8fc625.png",`
- `resources/assets/flutter_assets/config/welcome.json:13`
  `"ms": "https://healthresource-1258280810.picsgp.myqcloud.com/47b2975f-3dcd-4c22-86d1-18feb2fce75c.png"`
- `resources/assets/flutter_assets/config/welcome.json:30`
  `"en": "https://healthresource-1258280810.picsgp.myqcloud.com/9123bf0f-25f7-4471-8cae-a0b2f24b3d5c.png",`
- `resources/assets/flutter_assets/config/welcome.json:31`
  `"ms": "https://healthresource-1258280810.picsgp.myqcloud.com/e8106e23-aaae-452b-b0cf-32e0608c34b8.png"`
- `resources/assets/flutter_assets/config/welcome.json:48`
  `"en": "https://healthresource-1258280810.picsgp.myqcloud.com/665c0cdd-3f48-4582-9c53-6f1459de9943.png",`
- `resources/assets/flutter_assets/config/welcome.json:49`
  `"ms": "https://healthresource-1258280810.picsgp.myqcloud.com/665c0cdd-3f48-4582-9c53-6f1459de9943.png"`
- `resources/assets/flutter_assets/config/welcome.json:66`
  `"en": "https://healthresource-1258280810.picsgp.myqcloud.com/5ff55018-7c96-4d3e-bbc5-988c34f48273.png",`
- `resources/assets/flutter_assets/config/welcome.json:67`
  `"ms": "https://healthresource-1258280810.picsgp.myqcloud.com/5ff55018-7c96-4d3e-bbc5-988c34f48273.png"`
- `resources/assets/flutter_assets/config/floor/home_floor_config.json:85`
  `"icon": "https://healthresource-1258280810.cos.ap-singapore.myqcloud.com/69ef7d53-ab63-445e-8a90-5a744357fcde.png",`
- `resources/assets/flutter_assets/config/floor/home_floor_config.json:108`
  `"icon": "https://healthresource-1258280810.picsgp.myqcloud.com/98754f25-5e2a-4161-98c2-beb8c299fb50.png",`
- `resources/assets/flutter_assets/config/floor/home_floor_config.json:148`
  `"en": "https://healthresource-1258280810.cos.ap-singapore.myqcloud.com/d38e2ab0-287e-4cbc-ad8f-18cd1c3c29ce.png",`
- `resources/assets/flutter_assets/config/floor/home_floor_config.json:149`
  `"ms": "https://healthresource-1258280810.cos.ap-singapore.myqcloud.com/d38e2ab0-287e-4cbc-ad8f-18cd1c3c29ce.png"`
- `resources/assets/flutter_assets/config/floor/home_floor_config.json:155`
  `"en": "https://healthresource-1258280810.cos.ap-singapore.myqcloud.com/d38e2ab0-287e-4cbc-ad8f-18cd1c3c29ce.png",`
- `resources/assets/flutter_assets/config/floor/home_floor_config.json:156`
  `"ms": "https://healthresource-1258280810.cos.ap-singapore.myqcloud.com/d38e2ab0-287e-4cbc-ad8f-18cd1c3c29ce.png"`
- `resources/assets/flutter_assets/config/floor/home_floor_config.json:223`
  `"icon": "https://healthresource-1258280810.cos.ap-singapore.myqcloud.com/986dfe57-c481-4665-ab2d-7d1bf70b969d.png",`
- `resources/assets/flutter_assets/config/floor/home_floor_config.json:243`
  `"icon": "https://healthresource-1258280810.cos.ap-singapore.myqcloud.com/71ad0562-2b2b-4924-9be4-ad76b887dcce.png",`
- `resources/assets/flutter_assets/config/floor/medical_floor_config_5.0.json:150`
  `"url": "https://healthresource-1258280810.picsgp.myqcloud.com/ea82a951-4a83-4a4f-9cfa-a284cf2fd5e6.png"`
- `resources/assets/flutter_assets/config/floor/medical_floor_config_5.0.json:161`
  `"url": "https://healthresource-1258280810.cos.ap-singapore.myqcloud.com/e47448eb-1a3e-449b-bc87-835a61e54adb.png"`
- `resources/assets/flutter_assets/config/floor/medical_floor_config_5.0.json:172`
  `"url": "https://healthresource-1258280810.cos.ap-singapore.myqcloud.com/e334ba02-9232-4853-8c4f-0a93d0711f80.png"`
- `resources/assets/flutter_assets/config/floor/my_health_floor_config.json:33`
  `"url": "https://healthresource-1258280810.cos.ap-singapore.myqcloud.com/aac0c4e1-c97b-4a40-99a3-02a7a00f950a.png"`
- `resources/assets/flutter_assets/config/floor/my_health_floor_config.json:52`
  `"url": "https://healthresource-1258280810.picsgp.myqcloud.com/ea82a951-4a83-4a4f-9cfa-a284cf2fd5e6.png"`
- `resources/assets/flutter_assets/config/floor/my_health_floor_config.json:100`
  `"url": "https://healthresource-1258280810.cos.ap-singapore.myqcloud.com/aac0c4e1-c97b-4a40-99a3-02a7a00f950a.png"`
- `resources/assets/flutter_assets/config/floor/my_health_floor_config.json:136`
  `"url": "https://healthresource-1258280810.picsgp.myqcloud.com/ea82a951-4a83-4a4f-9cfa-a284cf2fd5e6.png"`
- `resources/assets/flutter_assets/config/floor/my_health_floor_config.json:147`
  `"url": "https://healthresource-1258280810.cos.ap-singapore.myqcloud.com/e47448eb-1a3e-449b-bc87-835a61e54adb.png"`
- `resources/assets/flutter_assets/config/floor/my_health_floor_config.json:158`
  `"url": "https://healthresource-1258280810.cos.ap-singapore.myqcloud.com/e334ba02-9232-4853-8c4f-0a93d0711f80.png"`
- `resources/assets/flutter_assets/config/language/en.json:547`
  `"my_health_hi_card_join_url": "https://healthresource-1258280810.picsgp.myqcloud.com/49377b10-cd69-481d-96d9-7670d6f55422.png",`
- `resources/assets/flutter_assets/config/language/ms.json:604`
  `"my_health_hi_card_join_url": "https://healthresource-1258280810.picsgp.myqcloud.com/6aa3f4b8-c97c-4979-9e4e-85d359eee972.png",`
- `resources/assets/flutter_assets/packages/flutter_image_compress_web/assets/pica.min.js:4`
  `https://github.com/nodeca/pica`
- `resources/assets/html/bruhealth_disclaimer.html:2`
  `<!-- saved from url=(0082)http://test.k8s.bruneihealth.yiducloud.cn/covid19/bruhealth/term_of_use_2.0.0.html -->`
- `resources/assets/html-de/sharing.html:12`
  `<p>Um QR-Codes auf Ihrem Computer zu erzeugen, testen Sie den ZXing QR Code Generator, er basiert auf dem selben Quelltext wie dieses Programm: <a href="http://zxing.appspot.com/generator/">http://zxing.appspot.com/generator/</a></p>`
- `resources/assets/html-en/sharing.html:12`
  `<p>To generate QR Codes from your computer, try the ZXing QR Code Generator: <a href="http://zxing.appspot.com/generator/">http://zxing.appspot.com/generator/</a></p>`
- `resources/assets/html-es/sharing.html:12`
  `<p> Para generar códigos QR desde su computadora, pruebe el generador ZXing Código QR: <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-fr/sharing.html:12`
  `<p> Pour générer les codes QR à partir de votre ordinateur, essayez le générateur de code QR ZXing: <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-it/sharing.html:12`
  `<p> Per generare i codici QR dal tuo computer, provare il generatore di ZXing QR Code: <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-nl/sharing.html:12`
  `<p> Om QR Codes van uw computer te genereren, probeer dan de ZXing QR Code Generator: <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/html-pt/sharing.html:12`
  `<p> Para gerar QR Codes do seu computador, experimente a Gerador de código QR ZXing: <a href="http://zxing.appspot.com/generator/"> http://zxing.appspot.com/generator/ </a></p>`
- `resources/assets/www/cordova.js:99`
  `// http://www.w3.org/html/wg/drafts/html/master/browsers.html#named-access-on-the-window-object`
- `resources/assets/www/index.html:1`
  `<!DOCTYPE html><html lang=en><head><meta charset=utf-8><meta http-equiv=X-UA-Compatible content="IE=edge"><meta name=viewport content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=0,viewport-fit=cover"><meta http-equiv=Content-Security-Policy content="default-src 'self' data: gap...`
- `resources/assets/www/js/app.b93f0a41.js:1`
  `(function(e){function t(t){for(var n,i,r=t[0],c=t[1],l=t[2],u=0,d=[];u<r.length;u++)i=r[u],Object.prototype.hasOwnProperty.call(o,i)&&o[i]&&d.push(o[i][0]),o[i]=0;for(n in c)Object.prototype.hasOwnProperty.call(c,n)&&(e[n]=c[n]);m&&m(t);while(d.length)d.shift()();return s.push.apply(s,l||[]),a()}fun...`
- `resources/assets/www/js/chunk-62287d62.bb968c40.js:1`
  `(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-62287d62"],{"0816":function(e){e.exports=JSON.parse('{"bm":{"common":{"cancel":"Batal","confirm":"Sah","ok":"OK","resultOptions":[{"display":"Negatif","isNegative":true,"prop":"Negative"},{"display":"Positif","isPositive":true,"prop":...`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:2`
  `/*! safe-buffer. MIT License. Feross Aboukhadijeh <https://feross.org/opensource> */`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:14`
  `return function(e){var n=t,i=n.lib,r=i.WordArray,o=i.Hasher,a=n.algo,s=r.create([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,7,4,13,1,10,6,15,3,12,0,9,5,2,14,11,8,3,10,14,4,9,15,8,1,2,7,0,6,13,11,5,12,1,9,11,10,0,8,12,4,13,3,7,15,14,5,6,2,4,0,5,9,7,12,2,10,14,1,3,8,11,6,15,13]),l=r.create([5,14,7,0,9,2,11...`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:26`
  `var i=Object.freeze({}),r=Array.isArray;function o(t){return void 0===t||null===t}function a(t){return void 0!==t&&null!==t}function s(t){return!0===t}function l(t){return!1===t}function u(t){return"string"===typeof t||"number"===typeof t||"symbol"===typeof t||"boolean"===typeof t}function c(t){retu...`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:29`
  `* Lodash <https://lodash.com/>`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:30`
  `* Copyright OpenJS Foundation and other contributors <https://openjsf.org/>`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:31`
  `* Released under MIT license <https://lodash.com/license>`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:32`
  `* Based on Underscore.js 1.8.3 <http://underscorejs.org/LICENSE>`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:34`
  `*/(function(){var o,a="4.17.21",s=200,l="Unsupported core-js use. Try https://npms.io/search?q=ponyfill.",u="Expected a function",c="Invalid 'variable' option passed into '_.template'",h="__lodash_hash_undefined__",f=500,d="__lodash_placeholder__",p=1,g=2,m=4,v=1,y=2,b=1,w=2,_=4,x=8,M=16,S=32,T=64,I...`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:46`
  `/*! safe-buffer. MIT License. Feross Aboukhadijeh <https://feross.org/opensource> */`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:47`
  `var i=n("b639"),r=i.Buffer;function o(t,e){for(var n in t)e[n]=t[n]}function a(t,e,n){return r(t,e,n)}r.from&&r.alloc&&r.allocUnsafe&&r.allocUnsafeSlow?t.exports=i:(o(i,e),e.Buffer=a),a.prototype=Object.create(r.prototype),o(r,a),a.from=function(t,e,n){if("number"===typeof t)throw new TypeError("Arg...`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:49`
  `* shallow-clone <https://github.com/jonschlinkert/shallow-clone>`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:54`
  `const i=Symbol.prototype.valueOf,r=n("84bc");function o(t,e){switch(r(t)){case"array":return t.slice();case"object":return Object.assign({},t);case"date":return new t.constructor(Number(t));case"map":return new Map(t);case"set":return new Set(t);case"buffer":return u(t);case"symbol":return c(t);case...`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:66`
  `* Surmon <https://github.com/surmon-china>`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:82`
  `***************************************************************************** */function l(){for(var t=0,e=0,n=arguments.length;e<n;e++)t+=arguments[e].length;var i=Array(t),r=0;for(e=0;e<n;e++)for(var o=arguments[e],a=0,s=o.length;a<s;a++,r++)i[r]=o[a];return i}var u,c=function(t){return t.replace(...`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:84`
  `String.fromCodePoint||function(){var t=function(){try{var t={},e=Object.defineProperty,n=e(t,t,t)&&e}catch(i){}return n}(),e=String.fromCharCode,n=Math.floor,i=function(t){var i,r,o=16384,a=[],s=-1,l=arguments.length;if(!l)return"";var u="";while(++s<l){var c=Number(arguments[s]);if(!isFinite(c)||c<...`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:85`
  `/*! ieee754. BSD-3-Clause License. Feross Aboukhadijeh <https://feross.org/opensource> */`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:88`
  `* isobject <https://github.com/jonschlinkert/isobject>`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:107`
  `* @author   Feross Aboukhadijeh <http://feross.org>`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:111`
  `/*! regenerator-runtime -- Copyright (c) 2014-present, Facebook, Inc. -- license (MIT): https://github.com/facebook/regenerator/blob/main/LICENSE */`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:113`
  `᠎";t.exports=function(t){return r((function(){return!!o[t]()||a[t]()!==a||i&&o[t].name!==t}))}},c8ef:function(t,e,n){var i=n("6d8b"),r=n("a15a"),o=r.createSymbol,a=n("2306"),s=a.Group,l=n("3842"),u=l.parsePercent,c=n("1418"),h=3;function f(t){return i.isArray(t)||(t=[+t,+t]),t}function d(t,e){var n=...`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:117`
  `* @author   Feross Aboukhadijeh <feross@feross.org> <http://feross.org>`
- `resources/assets/www/js/chunk-vendors.e85ab7fe.js:121`
  `* is-plain-object <https://github.com/jonschlinkert/is-plain-object>`
- `resources/assets/www/js/immigration.adfec475.js:1`
  `(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["immigration","ihospital-appointment33","ihospital-appointment34"],{"02a2":function(t,e,i){},"0600":function(t,e,i){},"088e":function(t,e,i){},"0b50":function(t,e,i){"use strict";i.r(e);var r=i("ade3"),a=(i("b0c0"),function(){var t,e=this,i=...`
- `resources/assets/www/js/test.544ee1a8.js:1`
  `(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["test"],{"06da":function(t,i,e){t.exports=e.p+"img/ic_back.80e951de.png"},"0f58":function(t,i,e){},"1a7f":function(t,i,e){t.exports=e.p+"img/authentication.6c7e1029.png"},"1c30":function(t,i,e){t.exports=e.p+"img/ic_front.d4ed8db3.png"},"1d5...`
- `resources/assets/www/plugins/cordova-plugin-camera/www/Camera.js:106`
  `* - Save the data locally ('LocalStorage', [Lawnchair](http://brianleroux.github.com/lawnchair/), etc.)`
- `resources/assets/www/plugins/cordova-plugin-globalization/www/globalization.js:159`
  `*                                    http://unicode.org/reports/tr35/tr35-4.html`
- `resources/assets/www/plugins/cordova-plugin-globalization/www/globalization.js:329`
  `*                                    http://unicode.org/reports/tr35/tr35-4.html`
- `resources/assets/www/plugins/cordova-plugin-globalization/www/globalization.js:364`
  `*                                    http://unicode.org/reports/tr35/tr35-4.html`
- `resources/res/color/design_box_stroke_color.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/_mtrl_switch_thumb_checked_unchecked__1_res_0x7f080024.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/res/drawable/_mtrl_switch_thumb_unchecked_checked__0_res_0x7f080027.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/res/drawable/_mtrl_switch_thumb_unchecked_checked__1_res_0x7f080028.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/res/layout/design_text_input_end_icon.xml:2`
  `<com.google.android.material.internal.CheckableImageButton xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/design_text_input_start_icon.xml:2`
  `<com.google.android.material.internal.CheckableImageButton xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/layout_login_pwd.xml:2`
  `<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto"`
- `resources/res/layout/layout_login_vc.xml:2`
  `<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto"`
- `resources/res/layout/layout_trtc_func.xml:2`
  `<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/material_chip_input_combo.xml:2`
  `<com.google.android.material.timepicker.ChipTextInputComboView xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/material_time_input.xml:2`
  `<com.google.android.material.textfield.TextInputLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto"`
- `resources/res/layout/mtrl_picker_text_input_date.xml:2`
  `<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"`

## BR097

paper_id: B019
paper_title: Pulse Oximeter App Privacy Policies During COVID-19: Scoping Assessment

- `resources/assets/www/index.html:1`
  `<!DOCTYPE html><html lang=en><head><meta charset=utf-8><meta http-equiv=X-UA-Compatible content="IE=edge"><meta name=viewport content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=0,viewport-fit=cover"><meta http-equiv=Content-Security-Policy content="default-src 'self' data: gap...`

## BR098

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/egnc/moh/base/net/ApiClient.java:89`
  `OkHttpClient.Builder builder = new OkHttpClient.Builder();`
- `sources/egnc/moh/base/net/ApiClient.java:152`
  `OkHttpClient.Builder builder = new OkHttpClient.Builder();`
- `sources/egnc/moh/base/net/ApiClient.java:232`
  `retrofitBuild = new Retrofit.Builder().baseUrl(EvydEnvironment.getBaseUrl()).addCallAdapterFactory(new LiveDataCallAdapterFactory()).addConverterFactory(GsonConverterFactory.create()).client(getInstance().mClient).build();`
- `sources/egnc/moh/base/net/ApiClient.java:246`
  `retrofitBuild = new Retrofit.Builder().baseUrl(str).addCallAdapterFactory(new LiveDataCallAdapterFactory()).addConverterFactory(GsonConverterFactory.create()).client(getInstance().mClient).build();`
- `sources/egnc/moh/base/net/ApiClient.java:253`
  `return (T) new Retrofit.Builder().baseUrl(EvydEnvironment.getBaseUrl()).addCallAdapterFactory(new LiveDataCallAdapterFactory()).addConverterFactory(GsonConverterFactory.create()).client(buildUploadOkClient()).build().create(cls);`
