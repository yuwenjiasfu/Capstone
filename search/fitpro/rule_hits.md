# Rule Search Hits

## BR001

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/AndroidManifest.xml:43`
  `<uses-permission android:name="android.permission.WAKE_LOCK"/>`
- `resources/AndroidManifest.xml:44`
  `<uses-permission android:name="android.permission.CAMERA"/>`
- `resources/AndroidManifest.xml:45`
  `<uses-permission android:name="android.permission.DOWNLOAD_WITHOUT_NOTIFICATION"/>`
- `resources/AndroidManifest.xml:46`
  `<uses-permission android:name="android.permission.READ_CONTACTS"/>`
- `resources/AndroidManifest.xml:47`
  `<uses-permission android:name="android.permission.READ_PHONE_STATE"/>`
- `resources/AndroidManifest.xml:48`
  `<uses-permission android:name="android.permission.CALL_STATE_IDLE"/>`
- `resources/AndroidManifest.xml:50`
  `<uses-permission android:name="android.permission.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS"/>`
- `resources/AndroidManifest.xml:51`
  `<uses-permission android:name="android.permission.READ_CALL_LOG"/>`
- `resources/AndroidManifest.xml:52`
  `<uses-permission android:name="android.permission.READ_SMS"/>`
- `resources/AndroidManifest.xml:53`
  `<uses-permission android:name="android.permission.RECEIVE_SMS"/>`
- `resources/AndroidManifest.xml:54`
  `<uses-permission android:name="android.permission.CALL_PHONE"/>`
- `resources/AndroidManifest.xml:55`
  `<uses-permission android:name="android.permission.ANSWER_PHONE_CALLS"/>`

## BR002

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/AndroidManifest.xml:31`
  `<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>`
- `resources/AndroidManifest.xml:32`
  `<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>`
- `resources/AndroidManifest.xml:33`
  `<uses-permission android:name="android.permission.BLUETOOTH_CONNECT"/>`

## BR003

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/AndroidManifest.xml:25`
  `<uses-permission`
- `resources/AndroidManifest.xml:28`
  `<uses-permission`
- `resources/AndroidManifest.xml:32`
  `<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>`
- `resources/AndroidManifest.xml:33`
  `<uses-permission android:name="android.permission.BLUETOOTH_CONNECT"/>`
- `resources/AndroidManifest.xml:34`
  `<uses-permission`
- `resources/AndroidManifest.xml:37`
  `<uses-permission android:name="android.permission.BLUETOOTH_ADVERTISE"/>`
- `resources/AndroidManifest.xml:38`
  `<uses-permission android:name="android.permission.VIBRATE"/>`

## BR004

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/AndroidManifest.xml:40`
  `<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>`
- `resources/AndroidManifest.xml:41`
  `<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>`
- `resources/AndroidManifest.xml:42`
  `<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>`
- `resources/AndroidManifest.xml:43`
  `<uses-permission android:name="android.permission.WAKE_LOCK"/>`

## BR005

paper_id: B021
paper_title: Metadata-Based Privacy Assessment for Mobile mHealth

- `resources/AndroidManifest.xml:115`
  `<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>`
- `resources/AndroidManifest.xml:116`
  `<uses-permission android:name="android.permission.POST_NOTIFICATIONS"/>`
- `resources/AndroidManifest.xml:133`
  `<uses-permission android:name="com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE"/>`
- `resources/AndroidManifest.xml:134`
  `<uses-permission android:name="android.permission.ACCESS_ADSERVICES_AD_ID"/>`
- `resources/AndroidManifest.xml:135`
  `<uses-permission android:name="android.permission.ACCESS_ADSERVICES_ATTRIBUTION"/>`
- `resources/AndroidManifest.xml:136`
  `<uses-permission android:name="android.permission.ACCESS_ADSERVICES_TOPICS"/>`
- `resources/AndroidManifest.xml:137`
  `<uses-permission android:name="com.applovin.array.apphub.permission.BIND_APPHUB_SERVICE"/>`

## BR006

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:154`
  `android:usesCleartextTraffic="true"`

## BR007

paper_id: B025
paper_title: Why Eve and Mallory Still Love Android: Revisiting TLS (In)Security in Android Applications

- `resources/AndroidManifest.xml:155`
  `android:networkSecurityConfig="@xml/network_security_config"`
- `resources/res/xml/network_config.xml:3`
  `<base-config cleartextTrafficPermitted="true"/>`
- `resources/res/xml/network_security_config.xml:3`
  `<domain-config cleartextTrafficPermitted="true">`
- `resources/res/xml/network_security_config.xml:7`
  `<domain-config>`
- `resources/res/xml/network_security_config.xml:13`
  `<base-config cleartextTrafficPermitted="true">`

## BR008

paper_id: B025
paper_title: Why Eve and Mallory Still Love Android: Revisiting TLS (In)Security in Android Applications

- `resources/res/xml/network_security_config.xml:14`
  `<trust-anchors>`
- `resources/res/xml/network_security_config.xml:15`
  `<certificates src="system"/>`

## BR009

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:33`
  `import javax.net.ssl.X509TrustManager;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:45`
  `@Metadata(d1 = {"\u0000î\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u001a\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u00...`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:76`
  `private final X509TrustManager x509TrustManager;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:347`
  `/* JADX INFO: renamed from: x509TrustManager, reason: from getter */`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:348`
  `public final X509TrustManager getX509TrustManager() {`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:349`
  `return this.x509TrustManager;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:396`
  `this.x509TrustManager = null;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:407`
  `X509TrustManager x509TrustManagerOrNull = builder.getX509TrustManagerOrNull();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:408`
  `Intrinsics.checkNotNull(x509TrustManagerOrNull);`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:409`
  `this.x509TrustManager = x509TrustManagerOrNull;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:414`
  `X509TrustManager x509TrustManagerPlatformTrustManager = Platform.INSTANCE.get().platformTrustManager();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:415`
  `this.x509TrustManager = x509TrustManagerPlatformTrustManager;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:417`
  `Intrinsics.checkNotNull(x509TrustManagerPlatformTrustManager);`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:418`
  `this.sslSocketFactoryOrNull = platform.newSslSocketFactory(x509TrustManagerPlatformTrustManager);`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:420`
  `Intrinsics.checkNotNull(x509TrustManagerPlatformTrustManager);`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:421`
  `CertificateChainCleaner certificateChainCleaner2 = companion.get(x509TrustManagerPlatformTrustManager);`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:431`
  `this.x509TrustManager = null;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:473`
  `if (this.x509TrustManager == null) {`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:474`
  `throw new IllegalStateException("x509TrustManager == null".toString());`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:486`
  `if (this.x509TrustManager != null) {`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:520`
  `@Metadata(d1 = {"\u0000ø\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0018...`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:551`
  `private X509TrustManager x509TrustManagerOrNull;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:694`
  `/* JADX INFO: renamed from: getX509TrustManagerOrNull$okhttp, reason: from getter */`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:695`
  `public final X509TrustManager getX509TrustManagerOrNull() {`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:696`
  `return this.x509TrustManagerOrNull;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:827`
  `public final void setX509TrustManagerOrNull$okhttp(X509TrustManager x509TrustManager) {`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:828`
  `this.x509TrustManagerOrNull = x509TrustManager;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:878`
  `this.x509TrustManagerOrNull = okHttpClient.getX509TrustManager();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:1032`
  `@Deprecated(level = DeprecationLevel.ERROR, message = "Use the sslSocketFactory overload that accepts a X509TrustManager.")`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:1039`
  `X509TrustManager x509TrustManagerTrustManager = Platform.INSTANCE.get().trustManager(sslSocketFactory);`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:1040`
  `if (x509TrustManagerTrustManager == null) {`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:1043`
  `this.x509TrustManagerOrNull = x509TrustManagerTrustManager;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:1045`
  `X509TrustManager x509TrustManager = this.x509TrustManagerOrNull;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:1046`
  `Intrinsics.checkNotNull(x509TrustManager);`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:1047`
  `this.certificateChainCleaner = platform.buildCertificateChainCleaner(x509TrustManager);`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:1051`
  `public final Builder sslSocketFactory(SSLSocketFactory sslSocketFactory, X509TrustManager trustManager) {`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:1054`
  `if (!Intrinsics.areEqual(sslSocketFactory, this.sslSocketFactoryOrNull) || !Intrinsics.areEqual(trustManager, this.x509TrustManagerOrNull)) {`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:1059`
  `this.x509TrustManagerOrNull = trustManager;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Android10Platform.java:20`
  `import javax.net.ssl.X509TrustManager;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Android10Platform.java:28`
  `@Metadata(d1 = {"\u0000J\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Android10Platform.java:48`
  `public X509TrustManager trustManager(SSLSocketFactory sslSocketFactory) {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Android10Platform.java:121`
  `public CertificateChainCleaner buildCertificateChainCleaner(X509TrustManager trustManager) {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/AndroidPlatform.java:30`
  `import javax.net.ssl.X509TrustManager;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/AndroidPlatform.java:39`
  `@Metadata(d1 = {"\u0000x\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/AndroidPlatform.java:75`
  `public X509TrustManager trustManager(SSLSocketFactory sslSocketFactory) {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/AndroidPlatform.java:163`
  `public CertificateChainCleaner buildCertificateChainCleaner(X509TrustManager trustManager) {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/AndroidPlatform.java:170`
  `public TrustRootIndex buildTrustRootIndex(X509TrustManager trustManager) {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/AndroidPlatform.java:183`
  `@Metadata(d1 = {"\u00008\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u000e\n\u0000\b\u0080\b\u0018\u00...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/AndroidPlatform.java:186`
  `private final X509TrustManager trustManager;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/AndroidPlatform.java:189`
  `private final X509TrustManager getTrustManager() {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/AndroidPlatform.java:198`
  `public static /* synthetic */ CustomTrustRootIndex copy$default(CustomTrustRootIndex customTrustRootIndex, X509TrustManager x509TrustManager, Method method, int i, Object obj) {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/AndroidPlatform.java:200`
  `x509TrustManager = customTrustRootIndex.trustManager;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/AndroidPlatform.java:205`
  `return customTrustRootIndex.copy(x509TrustManager, method);`
- `sources/com/applovin/shadow/okhttp3/internal/platform/AndroidPlatform.java:208`
  `public final CustomTrustRootIndex copy(X509TrustManager trustManager, Method findByIssuerAndSignatureMethod) {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/AndroidPlatform.java:233`
  `public CustomTrustRootIndex(X509TrustManager trustManager, Method findByIssuerAndSignatureMethod) {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/BouncyCastlePlatform.java:18`
  `import javax.net.ssl.X509TrustManager;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/BouncyCastlePlatform.java:28`
  `@Metadata(d1 = {"\u0000J\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/BouncyCastlePlatform.java:52`
  `public X509TrustManager platformTrustManager() throws NoSuchAlgorithmException, KeyStoreException, NoSuchProviderException {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/BouncyCastlePlatform.java:59`
  `if (trustManager instanceof X509TrustManager) {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/BouncyCastlePlatform.java:60`
  `Intrinsics.checkNotNull(trustManager, "null cannot be cast to non-null type javax.net.ssl.X509TrustManager");`
- `sources/com/applovin/shadow/okhttp3/internal/platform/BouncyCastlePlatform.java:61`
  `return (X509TrustManager) trustManager;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/BouncyCastlePlatform.java:71`
  `public X509TrustManager trustManager(SSLSocketFactory sslSocketFactory) {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:20`
  `import javax.net.ssl.X509TrustManager;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:29`
  `@Metadata(d1 = {"\u0000H\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:42`
  `public X509TrustManager trustManager(SSLSocketFactory sslSocketFactory) {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:61`
  `public X509TrustManager platformTrustManager() throws NoSuchAlgorithmException, KeyStoreException {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:68`
  `if (trustManager instanceof X509TrustManager) {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:69`
  `Intrinsics.checkNotNull(trustManager, "null cannot be cast to non-null type javax.net.ssl.X509TrustManager");`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:70`
  `X509TrustManager x509TrustManager = (X509TrustManager) trustManager;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:71`
  `Conscrypt.setHostnameVerifier(x509TrustManager, DisabledHostnameVerifier.INSTANCE);`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:72`
  `return x509TrustManager;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:120`
  `public SSLSocketFactory newSslSocketFactory(X509TrustManager trustManager) throws NoSuchAlgorithmException, KeyManagementException {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Jdk9Platform.java:9`
  `import javax.net.ssl.X509TrustManager;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Jdk9Platform.java:17`
  `@Metadata(d1 = {"\u0000<\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Jdk9Platform.java:51`
  `public X509TrustManager trustManager(SSLSocketFactory sslSocketFactory) {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/OpenJSSEPlatform.java:17`
  `import javax.net.ssl.X509TrustManager;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/OpenJSSEPlatform.java:26`
  `@Metadata(d1 = {"\u0000J\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/OpenJSSEPlatform.java:50`
  `public X509TrustManager platformTrustManager() throws NoSuchAlgorithmException, KeyStoreException {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/OpenJSSEPlatform.java:57`
  `if (trustManager instanceof X509TrustManager) {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/OpenJSSEPlatform.java:58`
  `Intrinsics.checkNotNull(trustManager, "null cannot be cast to non-null type javax.net.ssl.X509TrustManager");`

## BR010

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/androidx/navigation/NavArgument.java:47`
  `boolean verify(String str, Bundle bundle) {`
- `sources/com/applovin/shadow/okhttp3/internal/connection/RealConnection.java:444`
  `OkHostnameVerifier okHostnameVerifier = OkHostnameVerifier.INSTANCE;`
- `sources/com/applovin/shadow/okhttp3/internal/connection/RealConnection.java:448`
  `if (okHostnameVerifier.verify(strHost, (X509Certificate) certificate)) {`
- `sources/com/applovin/shadow/okhttp3/internal/connection/RealConnection.java:602`
  `if (this.http2Connection == null || routes == null || !routeMatchesAny(routes) || address.hostnameVerifier() != OkHostnameVerifier.INSTANCE || !supportsUrl(address.url())) {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:82`
  `@Metadata(d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\u0011\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\bÀ\u0002\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002J3\u0...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:83`
  `public static final class DisabledHostnameVerifier implements ConscryptHostnameVerifier {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:84`
  `public static final DisabledHostnameVerifier INSTANCE = new DisabledHostnameVerifier();`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:86`
  `public final boolean verify(String hostname, SSLSession session) {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:90`
  `public boolean verify(X509Certificate[] certs, String hostname, SSLSession session) {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:94`
  `private DisabledHostnameVerifier() {`
- `sources/com/applovin/shadow/okhttp3/internal/tls/BasicCertificateChainCleaner.java:76`
  `toVerify.verify(signingCert.getPublicKey());`
- `sources/com/baidu/lbsapi/auth/h.java:17`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/com/baidu/lbsapi/auth/h.java:18`
  `public boolean verify(String str, SSLSession sSLSession) {`
- `sources/com/baidu/lbsapi/auth/h.java:22`
  `return HttpsURLConnection.getDefaultHostnameVerifier().verify(str, sSLSession);`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/AbstractVerifier.java:44`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/AbstractVerifier.java:45`
  `public final boolean verify(String str, SSLSession sSLSession) {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/AbstractVerifier.java:47`
  `verify(str, (X509Certificate) sSLSession.getPeerCertificates()[0]);`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/AllowAllHostnameVerifier.java:5`
  `public class AllowAllHostnameVerifier extends AbstractVerifier {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/AllowAllHostnameVerifier.java:6`
  `public static final AllowAllHostnameVerifier INSTANCE = new AllowAllHostnameVerifier();`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/AllowAllHostnameVerifier.java:12`
  `@Override // com.google.firebase.crashlytics.buildtools.reloc.org.apache.http.conn.ssl.X509HostnameVerifier`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/AllowAllHostnameVerifier.java:13`
  `public final void verify(String str, String[] strArr, String[] strArr2) {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/DefaultHostnameVerifier.java:56`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/DefaultHostnameVerifier.java:57`
  `public boolean verify(String str, SSLSession sSLSession) {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/DefaultHostnameVerifier.java:59`
  `verify(str, (X509Certificate) sSLSession.getPeerCertificates()[0]);`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/NoopHostnameVerifier.java:14`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/NoopHostnameVerifier.java:15`
  `public boolean verify(String str, SSLSession sSLSession) {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/SSLConnectionSocketFactory.java:39`
  `public static final X509HostnameVerifier ALLOW_ALL_HOSTNAME_VERIFIER = AllowAllHostnameVerifier.INSTANCE;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/SSLConnectionSocketFactory.java:42`
  `public static final X509HostnameVerifier BROWSER_COMPATIBLE_HOSTNAME_VERIFIER = BrowserCompatHostnameVerifier.INSTANCE;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/SSLConnectionSocketFactory.java:45`
  `public static final X509HostnameVerifier STRICT_HOSTNAME_VERIFIER = StrictHostnameVerifier.INSTANCE;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/SSLSocketFactory.java:36`
  `private volatile X509HostnameVerifier hostnameVerifier;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/SSLSocketFactory.java:41`
  `public static final X509HostnameVerifier ALLOW_ALL_HOSTNAME_VERIFIER = new AllowAllHostnameVerifier();`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/SSLSocketFactory.java:42`
  `public static final X509HostnameVerifier BROWSER_COMPATIBLE_HOSTNAME_VERIFIER = new BrowserCompatHostnameVerifier();`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/SSLSocketFactory.java:43`
  `public static final X509HostnameVerifier STRICT_HOSTNAME_VERIFIER = new StrictHostnameVerifier();`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/SSLSocketFactory.java:45`
  `public X509HostnameVerifier getHostnameVerifier() {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/SSLSocketFactory.java:46`
  `return this.hostnameVerifier;`
- `sources/com/lzy/okgo/https/HttpsUtils.java:39`
  `public static HostnameVerifier UnSafeHostnameVerifier = new HostnameVerifier() { // from class: com.lzy.okgo.https.HttpsUtils.2`
- `sources/com/lzy/okgo/https/HttpsUtils.java:40`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/com/lzy/okgo/https/HttpsUtils.java:41`
  `public boolean verify(String str, SSLSession sSLSession) {`
- `sources/com/mbridge/msdk/foundation/same/net/MBridgeHostnameVerifier.java:27`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/com/mbridge/msdk/foundation/same/net/MBridgeHostnameVerifier.java:28`
  `public boolean verify(String str, SSLSession sSLSession) {`
- `sources/com/mbridge/msdk/foundation/same/net/MBridgeHostnameVerifier.java:33`
  `HostnameVerifier defaultHostnameVerifier = HttpsURLConnection.getDefaultHostnameVerifier();`
- `sources/com/mbridge/msdk/foundation/same/net/MBridgeHostnameVerifier.java:34`
  `if (defaultHostnameVerifier == null || (defaultHostnameVerifier instanceof MBridgeHostnameVerifier)) {`
- `sources/com/mbridge/msdk/thrid/okhttp/internal/tls/a.java:73`
  `x509Certificate.verify(x509Certificate2.getPublicKey());`
- `sources/com/thinkup/core/common/no/m/o/mm/o.java:61`
  `x509Certificate.verify(x509Certificate2.getPublicKey());`
- `sources/okhttp3/internal/connection/RealConnection.java:313`
  `if (this.http2Connection == null || route == null || route.proxy().type() != Proxy.Type.DIRECT || this.route.proxy().type() != Proxy.Type.DIRECT || !this.route.socketAddress().equals(route.socketAddress()) || route.address().hostnameVerifier() != OkHostnameVerifier.INSTANCE || !supportsUrl(address.u...`
- `sources/okhttp3/internal/connection/RealConnection.java:331`
  `return this.handshake != null && OkHostnameVerifier.INSTANCE.verify(httpUrl.host(), (X509Certificate) this.handshake.peerCertificates().get(0));`
- `sources/okhttp3/internal/tls/BasicCertificateChainCleaner.java:61`
  `x509Certificate.verify(x509Certificate2.getPublicKey());`

## BR011

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/com/applovin/shadow/okhttp3/internal/connection/ConnectionSpecSelector.java:12`
  `import javax.net.ssl.SSLException;`
- `sources/com/applovin/shadow/okhttp3/internal/connection/ConnectionSpecSelector.java:13`
  `import javax.net.ssl.SSLHandshakeException;`
- `sources/com/applovin/shadow/okhttp3/internal/connection/ConnectionSpecSelector.java:66`
  `return (!this.isFallbackPossible || (e instanceof ProtocolException) || (e instanceof InterruptedIOException) || ((e instanceof SSLHandshakeException) && (e.getCause() instanceof CertificateException)) || (e instanceof SSLPeerUnverifiedException) || !(e instanceof SSLException)) ? false : true;`
- `sources/com/applovin/shadow/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:22`
  `import java.security.cert.CertificateException;`
- `sources/com/applovin/shadow/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:23`
  `import javax.net.ssl.SSLHandshakeException;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/client/DefaultHttpRequestRetryHandler.java:19`
  `import javax.net.ssl.SSLException;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/client/DefaultHttpRequestRetryHandler.java:47`
  `this(i, z, Arrays.asList(InterruptedIOException.class, UnknownHostException.class, ConnectException.class, SSLException.class));`
- `sources/com/mbridge/msdk/thrid/okhttp/internal/http/j.java:19`
  `import java.security.cert.CertificateException;`
- `sources/com/mbridge/msdk/thrid/okhttp/internal/http/j.java:21`
  `import javax.net.ssl.SSLHandshakeException;`
- `sources/okhttp3/internal/connection/ConnectionSpecSelector.java:11`
  `import javax.net.ssl.SSLHandshakeException;`
- `sources/okhttp3/internal/connection/ConnectionSpecSelector.java:58`
  `boolean z = iOException instanceof SSLHandshakeException;`
- `sources/okhttp3/internal/connection/ConnectionSpecSelector.java:59`
  `if ((z && (iOException.getCause() instanceof CertificateException)) || (iOException instanceof SSLPeerUnverifiedException)) {`
- `sources/okhttp3/internal/connection/ConnectionSpecSelector.java:62`
  `return z || (iOException instanceof SSLProtocolException) || (iOException instanceof SSLException);`
- `sources/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:11`
  `import java.security.cert.CertificateException;`
- `sources/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:13`
  `import javax.net.ssl.SSLHandshakeException;`

## BR012

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/com/applovin/shadow/okhttp3/Address.java:22`
  `@Metadata(d1 = {"\u0000h\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002...`
- `sources/com/applovin/shadow/okhttp3/Address.java:24`
  `private final CertificatePinner certificatePinner;`
- `sources/com/applovin/shadow/okhttp3/Address.java:36`
  `@Deprecated(level = DeprecationLevel.ERROR, message = "moved to val", replaceWith = @ReplaceWith(expression = "certificatePinner", imports = {}))`
- `sources/com/applovin/shadow/okhttp3/Address.java:37`
  `/* JADX INFO: renamed from: -deprecated_certificatePinner, reason: not valid java name and from getter */`
- `sources/com/applovin/shadow/okhttp3/Address.java:38`
  `public final CertificatePinner getCertificatePinner() {`
- `sources/com/applovin/shadow/okhttp3/Address.java:39`
  `return this.certificatePinner;`
- `sources/com/applovin/shadow/okhttp3/Address.java:102`
  `public final CertificatePinner certificatePinner() {`
- `sources/com/applovin/shadow/okhttp3/Address.java:103`
  `return this.certificatePinner;`
- `sources/com/applovin/shadow/okhttp3/Address.java:146`
  `public Address(String uriHost, int i, Dns dns, SocketFactory socketFactory, SSLSocketFactory sSLSocketFactory, HostnameVerifier hostnameVerifier, CertificatePinner certificatePinner, Authenticator proxyAuthenticator, Proxy proxy, List<? extends Protocol> protocols, List<ConnectionSpec> connectionSpe...`
- `sources/com/applovin/shadow/okhttp3/Address.java:158`
  `this.certificatePinner = certificatePinner;`
- `sources/com/applovin/shadow/okhttp3/Address.java:178`
  `return ((((((((((((((((((527 + this.url.hashCode()) * 31) + this.dns.hashCode()) * 31) + this.proxyAuthenticator.hashCode()) * 31) + this.protocols.hashCode()) * 31) + this.connectionSpecs.hashCode()) * 31) + this.proxySelector.hashCode()) * 31) + Objects.hashCode(this.proxy)) * 31) + Objects.hashCo...`
- `sources/com/applovin/shadow/okhttp3/Address.java:183`
  `return Intrinsics.areEqual(this.dns, that.dns) && Intrinsics.areEqual(this.proxyAuthenticator, that.proxyAuthenticator) && Intrinsics.areEqual(this.protocols, that.protocols) && Intrinsics.areEqual(this.connectionSpecs, that.connectionSpecs) && Intrinsics.areEqual(this.proxySelector, that.proxySelec...`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:29`
  `/* JADX INFO: compiled from: CertificatePinner.kt */`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:31`
  `@Metadata(d1 = {"\u0000T\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\"\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0010\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u0011\...`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:32`
  `public final class CertificatePinner {`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:36`
  `public static final CertificatePinner DEFAULT = new Builder().build();`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:64`
  `public CertificatePinner(Set<Pin> pins, CertificateChainCleaner certificateChainCleaner) {`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:70`
  `public /* synthetic */ CertificatePinner(Set set, CertificateChainCleaner certificateChainCleaner, int i, DefaultConstructorMarker defaultConstructorMarker) {`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:77`
  `check$okhttp(hostname, new Function0<List<? extends X509Certificate>>() { // from class: com.applovin.shadow.okhttp3.CertificatePinner.check.1`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:87`
  `CertificateChainCleaner certificateChainCleaner = CertificatePinner.this.getCertificateChainCleaner();`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:176`
  `public final CertificatePinner withCertificateChainCleaner$okhttp(CertificateChainCleaner certificateChainCleaner) {`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:178`
  `return Intrinsics.areEqual(this.certificateChainCleaner, certificateChainCleaner) ? this : new CertificatePinner(this.pins, certificateChainCleaner);`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:182`
  `if (other instanceof CertificatePinner) {`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:183`
  `CertificatePinner certificatePinner = (CertificatePinner) other;`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:184`
  `if (Intrinsics.areEqual(certificatePinner.pins, this.pins) && Intrinsics.areEqual(certificatePinner.certificateChainCleaner, this.certificateChainCleaner)) {`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:197`
  `/* JADX INFO: compiled from: CertificatePinner.kt */`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:198`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0007\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0004\u0018\u00002\u00020\u0001B\u0015\u0012\u0006\u0010\...`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:239`
  `if (StringsKt.startsWith$default(pin, "sha256/", false, 2, (Object) null)) {`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:251`
  `throw new IllegalArgumentException("pins must start with 'sha256/' or 'sha1/': " + pin);`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:281`
  `return Intrinsics.areEqual(this.hash, CertificatePinner.INSTANCE.sha256Hash(certificate));`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:284`
  `return Intrinsics.areEqual(this.hash, CertificatePinner.INSTANCE.sha1Hash(certificate));`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:309`
  `/* JADX INFO: compiled from: CertificatePinner.kt */`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:310`
  `@Metadata(d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010!\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010\u000e\n\u0002\u0010\u0011\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\u0018\u00002\u00020\u0001B\u0005¢\u0006\u0002\u0010\u0002J'\u0010\b\u001a\u00020\u00...`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:327`
  `public final CertificatePinner build() {`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:328`
  `return new CertificatePinner(CollectionsKt.toSet(this.pins), null, 2, 0 == true ? 1 : 0);`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:332`
  `/* JADX INFO: compiled from: CertificatePinner.kt */`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:333`
  `@Metadata(d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\b\u0086\u0003\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002...`
- `sources/com/applovin/shadow/okhttp3/CertificatePinner.java:366`
  `return "sha256/" + sha256Hash((X509Certificate) certificate).base64();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:45`
  `@Metadata(d1 = {"\u0000î\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u001a\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u00...`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:51`
  `private final CertificatePinner certificatePinner;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:101`
  `@Deprecated(level = DeprecationLevel.ERROR, message = "moved to val", replaceWith = @ReplaceWith(expression = "certificatePinner", imports = {}))`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:102`
  `/* JADX INFO: renamed from: -deprecated_certificatePinner, reason: not valid java name and from getter */`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:103`
  `public final CertificatePinner getCertificatePinner() {`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:104`
  `return this.certificatePinner;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:250`
  `public final CertificatePinner certificatePinner() {`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:251`
  `return this.certificatePinner;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:397`
  `this.certificatePinner = CertificatePinner.DEFAULT;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:410`
  `CertificatePinner certificatePinner = builder.getCertificatePinner();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:412`
  `this.certificatePinner = certificatePinner.withCertificateChainCleaner$okhttp(certificateChainCleaner);`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:423`
  `CertificatePinner certificatePinner2 = builder.getCertificatePinner();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:425`
  `this.certificatePinner = certificatePinner2.withCertificateChainCleaner$okhttp(certificateChainCleaner2);`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:432`
  `this.certificatePinner = CertificatePinner.DEFAULT;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:489`
  `if (!Intrinsics.areEqual(this.certificatePinner, CertificatePinner.DEFAULT)) {`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:520`
  `@Metadata(d1 = {"\u0000ø\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0018...`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:526`
  `private CertificatePinner certificatePinner;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:573`
  `/* JADX INFO: renamed from: getCertificatePinner$okhttp, reason: from getter */`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:574`
  `public final CertificatePinner getCertificatePinner() {`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:575`
  `return this.certificatePinner;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:724`
  `public final void setCertificatePinner$okhttp(CertificatePinner certificatePinner) {`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:725`
  `Intrinsics.checkNotNullParameter(certificatePinner, "<set-?>");`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:726`
  `this.certificatePinner = certificatePinner;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:850`
  `this.certificatePinner = CertificatePinner.DEFAULT;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:882`
  `this.certificatePinner = okHttpClient.certificatePinner();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:1107`
  `public final Builder certificatePinner(CertificatePinner certificatePinner) {`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:1108`
  `Intrinsics.checkNotNullParameter(certificatePinner, "certificatePinner");`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:1109`
  `if (!Intrinsics.areEqual(certificatePinner, this.certificatePinner)) {`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:1112`
  `this.certificatePinner = certificatePinner;`
- `sources/com/applovin/shadow/okhttp3/internal/connection/RealCall.java:8`
  `import com.applovin.shadow.okhttp3.CertificatePinner;`
- `sources/com/applovin/shadow/okhttp3/internal/connection/RealCall.java:467`
  `CertificatePinner certificatePinner;`
- `sources/com/applovin/shadow/okhttp3/internal/connection/RealCall.java:471`
  `certificatePinner = this.client.certificatePinner();`
- `sources/com/applovin/shadow/okhttp3/internal/connection/RealCall.java:475`
  `certificatePinner = null;`
- `sources/com/applovin/shadow/okhttp3/internal/connection/RealCall.java:477`
  `return new Address(url.host(), url.port(), this.client.dns(), this.client.socketFactory(), sslSocketFactory, hostnameVerifier, certificatePinner, this.client.proxyAuthenticator(), this.client.proxy(), this.client.protocols(), this.client.connectionSpecs(), this.client.proxySelector());`
- `sources/com/applovin/shadow/okhttp3/internal/connection/RealConnection.java:6`
  `import com.applovin.shadow.okhttp3.CertificatePinner;`
- `sources/com/applovin/shadow/okhttp3/internal/connection/RealConnection.java:330`
  `throw new SSLPeerUnverifiedException(StringsKt.trimMargin$default("\n              |Hostname " + address.url().host() + " not verified:\n              |    certificate: " + CertificatePinner.INSTANCE.pin(x509Certificate) + "\n              |    DN: " + x509Certificate.getSubjectDN().getName() + "\n ...`
- `sources/com/applovin/shadow/okhttp3/internal/connection/RealConnection.java:332`
  `final CertificatePinner certificatePinner = address.certificatePinner();`
- `sources/com/applovin/shadow/okhttp3/internal/connection/RealConnection.java:333`
  `Intrinsics.checkNotNull(certificatePinner);`
- `sources/com/applovin/shadow/okhttp3/internal/connection/RealConnection.java:342`
  `CertificateChainCleaner certificateChainCleaner$okhttp = certificatePinner.getCertificateChainCleaner();`
- `sources/com/applovin/shadow/okhttp3/internal/connection/RealConnection.java:347`
  `certificatePinner.check$okhttp(address.url().host(), new Function0<List<? extends X509Certificate>>() { // from class: com.applovin.shadow.okhttp3.internal.connection.RealConnection.connectTls.2`
- `sources/com/applovin/shadow/okhttp3/internal/connection/RealConnection.java:606`
  `CertificatePinner certificatePinner = address.certificatePinner();`
- `sources/com/applovin/shadow/okhttp3/internal/connection/RealConnection.java:607`
  `Intrinsics.checkNotNull(certificatePinner);`

## BR013

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `resources/LICENSES.txt:287`
  `<http://lists.debian.org/debian-legal/2004/12/msg00295.html>, it gives an`
- `resources/assets/mbridge_download_dialog_view.xml:2`
  `<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/assets/mbridge_download_dialog_view.xml:3`
  `xmlns:app="http://schemas.android.com/apk/res-auto"`
- `resources/assets/html/faq.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html/index.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html/privacy_in.html:3`
  `<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns:dt="uuid:C2F41010-65B3-11d1-A29F-00AA00C14882" xmlns="http://www.w3.org/TR/REC-html40" class="translated-ltr"><head><meta http-equiv="Content-Type" content="text/html; charset=GBK"><meta nam...`
- `resources/assets/html/privacy_in.html:1192`
  `mso-bidi-font-family:&#39;Times New Roman&#39;;font-size:10.5000pt;mso-font-kerning:1.0000pt;"><o:p></o:p></span></p></div><div id="goog-gt-tt" class="skiptranslate" dir="ltr"><div style="padding: 8px;"><div><div class="logo"></div></div></div><div class="top" style="padding: 8px; float: left; width...`
- `resources/assets/html/user_guide.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-en/faq.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-en/index.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-en/user_guide.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-zh-rCN/faq.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-zh-rCN/index.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-zh-rCN/user_guide.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-zh-rHK/faq.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-zh-rHK/index.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-zh-rHK/user_guide.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-zh-rTW/faq.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-zh-rTW/index.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-zh-rTW/user_guide.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:1176`
  `//reference: http://stackoverflow.com/questions/11735636/how-to-get-401-response-without-handling-it-using-try-catch-in-android`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:1503`
  `//http://stackoverflow.com/questions/3046424/http-post-requests-using-httpclient-take-2-seconds-why`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:1595`
  `//Added this line to avoid issue at: http://stackoverflow.com/questions/5358014/android-httpclient-oom-on-4g-lte-htc-thunderbolt`
- `resources/com/androidquery/util/AQUtility.java:733`
  `//Source: http://www.source-code.biz/base64coder/java/Base64Coder.java.txt`
- `resources/META-INF/commons-codec-1.10/META-INF/NOTICE.txt:5`
  `The Apache Software Foundation (http://www.apache.org/).`
- `resources/META-INF/commons-codec-1.10/META-INF/NOTICE.txt:8`
  `contains test data from http://aspell.net/test/orig/batch0.tab.`
- `resources/META-INF/commons-codec-1.10/META-INF/NOTICE.txt:14`
  `from the original php source code available at http://stevemorse.org/phoneticinfo.htm`
- `resources/mozilla/public-suffix-list.txt:432`
  `// br : http://registro.br/dominio/categoria.html`
- `resources/mozilla/public-suffix-list.txt:1031`
  `// gg : http://www.channelisles.net/register-domains/`
- `resources/mozilla/public-suffix-list.txt:1117`
  `// gu : http://gadao.gov.gu/register.html`
- `resources/mozilla/public-suffix-list.txt:1310`
  `// io : http://www.nic.io/rules.html`
- `resources/mozilla/public-suffix-list.txt:1315`
  `// iq : http://www.cmc.iq/english/iq/iqregister1.htm`
- `resources/mozilla/public-suffix-list.txt:1763`
  `// je : http://www.channelisles.net/register-domains/`
- `resources/mozilla/public-suffix-list.txt:1770`
  `// jm : http://www.com.jm/register.html`
- `resources/mozilla/public-suffix-list.txt:1773`
  `// jo : http://www.dns.jo/Registration_policy.aspx`
- `resources/mozilla/public-suffix-list.txt:3645`
  `// http://www.dot.kn/domainRules.html`
- `resources/mozilla/public-suffix-list.txt:3816`
  `// http://www.anrt.ma/fr/admin/download/upload/file_fr782.pdf`
- `resources/mozilla/public-suffix-list.txt:3863`
  `// see also: http://dns.marnet.net.mk/postapka.php`
- `resources/mozilla/public-suffix-list.txt:3873`
  `// ml : http://www.gobin.info/domainname/ml-template.doc`
- `resources/mozilla/public-suffix-list.txt:3904`
  `// mp : http://www.dot.mp/`

## BR014

paper_id: B022
paper_title: A Study of Android Application Security

- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1495`
  `panelFeatureState.qwertyMode = KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1;`
- `sources/androidx/appcompat/app/ToolbarActionBar.java:436`
  `menu.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);`
- `sources/androidx/appcompat/app/WindowDecorActionBar.java:1277`
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
- `sources/androidx/core/content/ContextCompat.java:59`
  `import android.telephony.TelephonyManager;`
- `sources/androidx/core/content/ContextCompat.java:316`
  `map.put(TelephonyManager.class, "phone");`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:4`
  `import android.telephony.TelephonyManager;`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:9`
  `public class TelephonyManagerCompat {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:10`
  `private static Method sGetDeviceIdMethod;`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:13`
  `public static String getImei(TelephonyManager telephonyManager) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:14`
  `return Api26Impl.getImei(telephonyManager);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:17`
  `public static int getSubscriptionId(TelephonyManager telephonyManager) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:19`
  `return Api30Impl.getSubscriptionId(telephonyManager);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:23`
  `Method declaredMethod = TelephonyManager.class.getDeclaredMethod("getSubId", new Class[0]);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:27`
  `Integer num = (Integer) sGetSubIdMethod.invoke(telephonyManager, new Object[0]);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:37`
  `private TelephonyManagerCompat() {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:44`
  `static int getSubscriptionId(TelephonyManager telephonyManager) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:45`
  `return telephonyManager.getSubscriptionId();`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:53`
  `static String getImei(TelephonyManager telephonyManager) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:54`
  `return telephonyManager.getImei();`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:62`
  `static String getDeviceId(TelephonyManager telephonyManager, int i) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:63`
  `return telephonyManager.getDeviceId(i);`
- `sources/androidx/core/view/DifferentialMotionFlingController.java:81`
  `int deviceId = motionEvent.getDeviceId();`
- `sources/androidx/core/view/DifferentialMotionFlingController.java:95`
  `iArr[0] = ViewConfigurationCompat.getScaledMinimumFlingVelocity(context, viewConfiguration, motionEvent.getDeviceId(), i, motionEvent.getSource());`
- `sources/androidx/core/view/DifferentialMotionFlingController.java:96`
  `iArr[1] = ViewConfigurationCompat.getScaledMaximumFlingVelocity(context, viewConfiguration, motionEvent.getDeviceId(), i, motionEvent.getSource());`
- `sources/androidx/test/espresso/base/EventInjector.java:25`
  `int deviceId = event.getDeviceId();`
- `sources/com/amazon/device/ads/DtbDeviceData.java:7`
  `import android.telephony.TelephonyManager;`
- `sources/com/amazon/device/ads/DtbDeviceData.java:139`
  `TelephonyManager telephonyManager = (TelephonyManager) AdRegistration.getContext().getSystemService("phone");`
- `sources/com/amazon/device/ads/DtbDeviceData.java:140`
  `String networkOperatorName = telephonyManager != null ? telephonyManager.getNetworkOperatorName() : null;`
- `sources/com/amazon/device/ads/DtbGooglePlayServices.java:32`
  `return DtbCommonUtils.isClassAvailable("com.google.android.gms.ads.identifier.AdvertisingIdClient");`
- `sources/com/amazon/device/ads/DtbGooglePlayServicesAdapter.java:7`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/amazon/device/ads/DtbGooglePlayServicesAdapter.java:22`
  `AdvertisingIdClient.Info advertisingIdInfo;`
- `sources/com/amazon/device/ads/DtbGooglePlayServicesAdapter.java:24`
  `advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(AdRegistration.getContext());`
- `sources/com/amazon/device/ads/DtbGooglePlayServicesAdapter.java:35`
  `APSAnalytics.logEvent(APSEventSeverity.FATAL, APSEventType.EXCEPTION, "Illegal Argument passed to getAdvertisingIdInfo", e4);`
- `sources/com/amazon/device/ads/SDKUtilities.java:4`
  `import android.telephony.TelephonyManager;`
- `sources/com/amazon/device/ads/SDKUtilities.java:90`
  `return ((TelephonyManager) AdRegistration.getContext().getSystemService("phone")).getPhoneType() != 0;`
- `sources/com/apm/insight/d.java:83`
  `public final String getDeviceId() {`
- `sources/com/apm/insight/ICommonParams.java:10`
  `String getDeviceId();`
- `sources/com/apm/insight/entity/Header.java:6`
  `import android.telephony.TelephonyManager;`
- `sources/com/apm/insight/entity/Header.java:246`
  `TelephonyManager telephonyManager = (TelephonyManager) e.g().getSystemService("phone");`
- `sources/com/apm/insight/entity/Header.java:247`
  `if (telephonyManager != null) {`
- `sources/com/apm/insight/entity/Header.java:248`
  `String networkOperatorName = telephonyManager.getNetworkOperatorName();`
- `sources/com/apm/insight/entity/Header.java:252`
  `String networkOperator = telephonyManager.getNetworkOperator();`
- `sources/com/apm/insight/l/k.java:6`
  `import android.telephony.TelephonyManager;`
- `sources/com/apm/insight/l/k.java:91`
  `int networkType = ((TelephonyManager) context.getSystemService("phone")).getNetworkType();`
- `sources/com/apm/insight/nativecrash/b.java:332`
  `return this.b.getDeviceId();`
- `sources/com/apm/insight/runtime/g.java:25`
  `public final String getDeviceId() {`
- `sources/com/applovin/impl/v.java:8`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/applovin/impl/v.java:177`
  `AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(context);`
- `sources/com/applovin/impl/v.java:213`
  `return k7.a("com.google.android.gms.ads.identifier.AdvertisingIdClient");`
- `sources/com/applovin/impl/sdk/l.java:27`
  `import android.telephony.TelephonyManager;`
- `sources/com/applovin/impl/sdk/l.java:487`
  `TelephonyManager telephonyManager = (TelephonyManager) this.c.getSystemService("phone");`
- `sources/com/applovin/impl/sdk/l.java:488`
  `if (telephonyManager == null) {`
- `sources/com/applovin/impl/sdk/l.java:492`
  `return telephonyManager.getNetworkOperatorName();`
- `sources/com/applovin/impl/sdk/l.java:503`
  `TelephonyManager telephonyManager = (TelephonyManager) this.c.getSystemService("phone");`
- `sources/com/applovin/impl/sdk/l.java:504`
  `return telephonyManager != null ? telephonyManager.getSimCountryIso().toUpperCase(Locale.ENGLISH) : "";`
- `sources/com/applovin/impl/sdk/l.java:589`
  `TelephonyManager telephonyManager = (TelephonyManager) this.c.getSystemService("phone");`
- `sources/com/applovin/impl/sdk/l.java:590`
  `if (telephonyManager == null) {`
- `sources/com/applovin/impl/sdk/l.java:594`
  `String networkOperator = telephonyManager.getNetworkOperator();`
- `sources/com/applovin/impl/sdk/l.java:606`
  `TelephonyManager telephonyManager = (TelephonyManager) this.c.getSystemService("phone");`
- `sources/com/applovin/impl/sdk/l.java:607`
  `if (telephonyManager == null) {`
- `sources/com/applovin/impl/sdk/l.java:611`
  `String networkOperator = telephonyManager.getNetworkOperator();`
- `sources/com/applovin/impl/sdk/l.java:1067`
  `map2.put("rat", Integer.valueOf(((TelephonyManager) this.c.getSystemService("phone")).getDataNetworkType()));`
- `sources/com/baidu/location/b/d.java:21`
  `import android.telephony.TelephonyManager;`
- `sources/com/baidu/location/b/d.java:55`
  `private TelephonyManager e;`
- `sources/com/baidu/location/b/d.java:76`
  `private class a extends TelephonyManager.CellInfoCallback {`
- `sources/com/baidu/location/b/d.java:84`
  `@Override // android.telephony.TelephonyManager.CellInfoCallback`
- `sources/com/baidu/location/b/d.java:543`
  `this.e = (TelephonyManager) this.d.getSystemService("phone");`
- `sources/com/baidu/location/b/d.java:557`
  `this.v = com.baidu.location.e.k.b("android.telephony.TelephonyManager$CellInfoCallback");`
- `sources/com/baidu/location/b/d.java:604`
  `public static com.baidu.location.c.a a(CellLocation cellLocation, TelephonyManager telephonyManager, com.baidu.location.c.a aVar) {`
- `sources/com/baidu/location/b/d.java:605`
  `if (cellLocation == null || telephonyManager == null) {`
- `sources/com/baidu/location/b/d.java:610`
  `String networkOperator = telephonyManager.getNetworkOperator();`
- `sources/com/baidu/location/c/b.java:24`
  `import android.telephony.TelephonyManager;`
- `sources/com/baidu/location/c/b.java:52`
  `private TelephonyManager d = null;`

## BR015

paper_id: B022
paper_title: A Study of Android Application Security

- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:23`
  `return "OnePlus".equalsIgnoreCase(Build.BRAND) && "OnePlus6".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:27`
  `return "OnePlus".equalsIgnoreCase(Build.BRAND) && "OnePlus6T".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:31`
  `return IntentUtils.MANUFACTURER.HUAWEI.equalsIgnoreCase(Build.BRAND) && "HWANE".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:35`
  `return "SAMSUNG".equalsIgnoreCase(Build.BRAND) && "ON7XELTE".equalsIgnoreCase(Build.DEVICE) && Build.VERSION.SDK_INT >= 27;`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:39`
  `return "SAMSUNG".equalsIgnoreCase(Build.BRAND) && "J7XELTE".equalsIgnoreCase(Build.DEVICE) && Build.VERSION.SDK_INT >= 27;`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:43`
  `return "REDMI".equalsIgnoreCase(Build.BRAND) && "joyeuse".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExtraSupportedSurfaceCombinationsQuirk.java:30`
  `return "heroqltevzw".equalsIgnoreCase(Build.DEVICE) || "heroqltetmo".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExtraSupportedSurfaceCombinationsQuirk.java:34`
  `if (!"samsung".equalsIgnoreCase(Build.BRAND)) {`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExtraSupportedSurfaceCombinationsQuirk.java:37`
  `return SUPPORT_EXTRA_FULL_CONFIGURATIONS_SAMSUNG_MODELS.contains(Build.MODEL.toUpperCase(Locale.US));`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExtraSupportedSurfaceCombinationsQuirk.java:41`
  `if (!"google".equalsIgnoreCase(Build.BRAND)) {`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExtraSupportedSurfaceCombinationsQuirk.java:44`
  `return SUPPORT_EXTRA_LEVEL_3_CONFIGURATIONS_GOOGLE_MODELS.contains(Build.MODEL.toUpperCase(Locale.US));`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExtraSupportedSurfaceCombinationsQuirk.java:48`
  `if (!"samsung".equalsIgnoreCase(Build.BRAND)) {`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExtraSupportedSurfaceCombinationsQuirk.java:51`
  `return SUPPORT_EXTRA_LEVEL_3_CONFIGURATIONS_SAMSUNG_MODELS.contains(Build.MODEL.toUpperCase(Locale.US));`
- `sources/androidx/camera/camera2/internal/compat/quirk/FlashAvailabilityBufferUnderflowQuirk.java:24`
  `return KNOWN_AFFECTED_MODELS.contains(new Pair(Build.MANUFACTURER.toLowerCase(Locale.US), Build.MODEL.toLowerCase(Locale.US)));`
- `sources/androidx/camera/camera2/internal/compat/quirk/ImageCaptureFailedWhenVideoCaptureIsBoundQuirk.java:33`
  `return "motorola".equalsIgnoreCase(Build.BRAND) && "moto e13".equalsIgnoreCase(Build.MODEL);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ImageCaptureFailedWhenVideoCaptureIsBoundQuirk.java:37`
  `return "samsung".equalsIgnoreCase(Build.BRAND) && ("gta8".equalsIgnoreCase(Build.DEVICE) || "gta8wifi".equalsIgnoreCase(Build.DEVICE));`
- `sources/androidx/camera/camera2/internal/compat/quirk/InvalidVideoProfilesQuirk.java:24`
  `return "samsung".equalsIgnoreCase(Build.BRAND) && isTp1aBuild();`
- `sources/androidx/camera/camera2/internal/compat/quirk/InvalidVideoProfilesQuirk.java:40`
  `return ("redmi".equalsIgnoreCase(Build.BRAND) || "xiaomi".equalsIgnoreCase(Build.BRAND)) && (isTkq1Build() || isTp1aBuild());`
- `sources/androidx/camera/camera2/internal/compat/quirk/InvalidVideoProfilesQuirk.java:44`
  `return AFFECTED_PIXEL_MODELS.contains(Build.MODEL.toLowerCase(Locale.ROOT));`
- `sources/androidx/camera/camera2/internal/compat/quirk/JpegCaptureDownsizingQuirk.java:17`
  `return KNOWN_AFFECTED_FRONT_CAMERA_DEVICES.contains(Build.MODEL.toLowerCase(Locale.US)) && ((Integer) cameraCharacteristicsCompat.get(CameraCharacteristics.LENS_FACING)).intValue() == 0;`
- `sources/androidx/camera/camera2/internal/compat/quirk/JpegHalCorruptImageQuirk.java:16`
  `return KNOWN_AFFECTED_DEVICES.contains(Build.DEVICE.toLowerCase(Locale.US));`
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
- `sources/androidx/camera/core/impl/utils/ExifData.java:137`
  `return new Builder(ByteOrder.BIG_ENDIAN).setAttribute(ExifInterface.TAG_ORIENTATION, String.valueOf(1)).setAttribute(ExifInterface.TAG_X_RESOLUTION, "72/1").setAttribute(ExifInterface.TAG_Y_RESOLUTION, "72/1").setAttribute(ExifInterface.TAG_RESOLUTION_UNIT, String.valueOf(2)).setAttribute(ExifInterf...`
- `sources/androidx/camera/core/internal/compat/quirk/ImageCaptureRotationOptionQuirk.java:29`
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
- `sources/androidx/camera/video/internal/compat/quirk/AudioTimestampFramePositionIncorrectQuirk.java:18`
  `return "oppo".equalsIgnoreCase(Build.BRAND) && AFFECTED_OPPO_MODELS.contains(Build.MODEL.toLowerCase(Locale.ROOT));`
- `sources/androidx/camera/video/internal/compat/quirk/AudioTimestampFramePositionIncorrectQuirk.java:22`
  `return "lge".equalsIgnoreCase(Build.BRAND) && "lg-m250".equalsIgnoreCase(Build.MODEL);`
- `sources/androidx/camera/video/internal/compat/quirk/CameraUseInconsistentTimebaseQuirk.java:24`
  `return "SAMSUNG".equalsIgnoreCase(Build.BRAND) && BUILD_HARDWARE_SET.contains(Build.HARDWARE.toLowerCase());`
- `sources/androidx/camera/video/internal/compat/quirk/CameraUseInconsistentTimebaseQuirk.java:28`
  `return BUILD_MODEL_SET.contains(Build.MODEL.toLowerCase());`
- `sources/androidx/camera/video/internal/compat/quirk/EncoderNotUsePersistentInputSurfaceQuirk.java:13`
  `return DEVICE_MODELS.contains(Build.MODEL.toUpperCase());`
- `sources/androidx/camera/video/internal/compat/quirk/MediaCodecInfoReportIncorrectInfoQuirk.java:22`
  `return "Nokia".equalsIgnoreCase(Build.BRAND) && "Nokia 1".equalsIgnoreCase(Build.MODEL);`
- `sources/androidx/camera/video/internal/compat/quirk/MediaCodecInfoReportIncorrectInfoQuirk.java:71`
  `return INCORRECT_FHD_PROFILE_MODEL_LIST.contains(Build.MODEL.toLowerCase(Locale.US));`
- `sources/androidx/camera/video/internal/compat/quirk/ReportedVideoQualityNotSupportedQuirk.java:16`
  `return "Huawei".equalsIgnoreCase(Build.BRAND) && "HMA-L29".equalsIgnoreCase(Build.MODEL);`
- `sources/androidx/camera/video/internal/workaround/VideoTimebaseConverter.java:74`
  `Logger.e(TAG, String.format("Detected camera timebase inconsistent. Please file an issue at https://issuetracker.google.com/issues/new?component=618491&template=1257717 with this error message [Manufacturer: %s, Model: %s, Hardware: %s, API Level: %d%s].\nCamera timebase is inconsistent. The timebas...`
- `sources/androidx/camera/view/internal/compat/quirk/SurfaceViewStretchedQuirk.java:21`
  `return SAMSUNG.equalsIgnoreCase(Build.MANUFACTURER) && (GALAXY_Z_FOLD_2.equalsIgnoreCase(Build.DEVICE) || GALAXY_Z_FOLD_3.equalsIgnoreCase(Build.DEVICE));`
- `sources/androidx/camera/view/internal/compat/quirk/SurfaceViewStretchedQuirk.java:25`
  `return OPPO.equalsIgnoreCase(Build.MANUFACTURER) && OPPO_FIND_N.equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/view/internal/compat/quirk/SurfaceViewStretchedQuirk.java:29`
  `return LENOVO.equalsIgnoreCase(Build.MANUFACTURER) && LENOVO_TAB_P12_PRO.equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/test/espresso/base/InputManagerEventInjectionStrategy.java:119`
  `return (Build.DEVICE.contains("glass") || Build.DEVICE.contains("Glass") || Build.DEVICE.contains("wingman")) && (motionEvent.getSource() & InputDeviceCompat.SOURCE_TOUCHPAD) != 0;`
- `sources/androidx/test/runner/screenshot/BasicScreenCaptureProcessor.java:21`
  `private static String sAndroidDeviceName = Build.DEVICE;`
- `sources/cn/bertsir/zbar/utils/QRUtils.java:330`
  `return "xiaomi".equalsIgnoreCase(Build.MANUFACTURER);`
- `sources/com/alibaba/fastjson/JSON.java:57`
  `public static TimeZone defaultTimeZone = TimeZone.getDefault();`
- `sources/com/alibaba/fastjson/JSON.java:58`
  `public static Locale defaultLocale = Locale.getDefault();`
- `sources/com/alibaba/fastjson/serializer/JodaCodec.java:49`
  `private static final DateTimeFormatter ISO_FIXED_FORMAT = DateTimeFormat.forPattern("yyyy-MM-dd HH:mm:ss").withZone(DateTimeZone.getDefault());`
- `sources/com/alibaba/fastjson/serializer/JodaCodec.java:139`
  `timeZone = TimeZone.getDefault();`
- `sources/com/amazon/aps/shared/analytics/APSEvent.java:93`
  `this.deviceManufacturer = Build.MANUFACTURER;`
- `sources/com/amazon/aps/shared/analytics/APSEvent.java:94`
  `this.deviceModel = Build.MODEL;`
- `sources/com/amazon/aps/shared/metrics/model/ApsMetricsDeviceInfo.java:184`
  `jSONObject.put("dm", Build.MANUFACTURER);`
- `sources/com/amazon/aps/shared/metrics/model/ApsMetricsDeviceInfo.java:185`
  `jSONObject.put("md", Build.MODEL);`
- `sources/com/amazon/device/ads/DtbDeviceData.java:131`
  `String str = Build.MODEL;`
- `sources/com/amazon/device/ads/DtbDeviceData.java:132`
  `String str2 = Build.MANUFACTURER;`
- `sources/com/amazon/device/ads/DtbDeviceData.java:134`
  `String str4 = Build.DEVICE;`
- `sources/com/amazon/device/ads/DtbDeviceData.java:135`
  `String country = Locale.getDefault().getCountry();`
- `sources/com/amazon/device/ads/DtbDeviceData.java:136`
  `String language = Locale.getDefault().getLanguage();`
- `sources/com/amazon/device/ads/SDKUtilities.java:132`
  `String str2 = Build.MODEL;`
- `sources/com/amazon/device/ads/SDKUtilities.java:133`
  `String str3 = Build.MANUFACTURER;`
- `sources/com/amazon/device/ads/SDKUtilities.java:134`
  `if (!str.startsWith("generic") && !str.startsWith("unknown") && !str2.contains("google_sdk") && !str2.contains("Emulator") && !str2.contains("Android SDK built for x86") && !str3.contains("Genymotion") && (!Build.BRAND.startsWith("generic") || !Build.DEVICE.startsWith("generic"))) {`
- `sources/com/amazon/device/ads/SDKUtilities.java:135`
  `if (!"google_sdk".equals(Build.PRODUCT)) {`
- `sources/com/apm/insight/entity/Header.java:315`
  `int rawOffset = TimeZone.getDefault().getRawOffset() / TimeConstants.HOUR;`
- `sources/com/apm/insight/entity/Header.java:334`
  `String str3 = Build.MODEL;`
- `sources/com/apm/insight/entity/Header.java:335`
  `String str4 = Build.BRAND;`
- `sources/com/apm/insight/entity/Header.java:342`
  `jSONObject.put("device_brand", Build.BRAND);`
- `sources/com/apm/insight/entity/Header.java:343`
  `jSONObject.put("device_manufacturer", Build.MANUFACTURER);`
- `sources/com/applovin/impl/d1.java:460`
  `s2Var.a("\nDebug Info:\n").a("Platform", "fireos".equals(this.f3451a.B().y()) ? "Fire OS" : "Android").a("AppLovin SDK Version", AppLovinSdk.VERSION).a("Plugin Version", this.f3451a.a(v4.I3)).a("App Package Name", this.b.getPackageName()).a(Device.TAG, String.format("%s %s (%s)", Build.BRAND, Build....`
- `sources/com/applovin/impl/d2.java:257`
  `map2.put("model", Build.MODEL);`
- `sources/com/applovin/impl/d2.java:258`
  `map2.put("brand", Build.MANUFACTURER);`
- `sources/com/applovin/impl/d2.java:259`
  `map2.put("brand_name", Build.BRAND);`
- `sources/com/applovin/impl/d2.java:261`
  `map2.put("revision", Build.DEVICE);`
- `sources/com/applovin/impl/sdk/l.java:213`
  `map.put(CommonUrlParts.LOCALE, Locale.getDefault().toString());`
- `sources/com/applovin/impl/sdk/l.java:214`
  `map.put("model", Build.MODEL);`
- `sources/com/applovin/impl/sdk/l.java:217`
  `map.put("revision", Build.DEVICE);`

## BR016

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/AndroidManifest.xml:558`
  `android:name="com.baidu.lbsapi.API_KEY"`
- `resources/AndroidManifest.xml:565`
  `android:name="com.google.android.geo.API_KEY"`
- `resources/com/androidquery/auth/TwitterHandle.java:33`
  `private static final String OAUTH_ACCESS_TOKEN = "https://api.twitter.com/oauth/access_token";`
- `resources/com/androidquery/auth/TwitterHandle.java:163`
  `private static final String TW_SECRET = "aq.tw.secret";`
- `resources/res/values/public.xml:13398`
  `<public type="string" name="qq_app_key" id="0x7f130649" />`
- `resources/res/values/strings.xml:1612`
  `<string name="qq_app_key">f5be8933f6f68850f535eb723f776f44</string>`
- `sources/cn/xiaofengkj/fitpro/R.java:13457`
  `public static final int qq_app_key = 0x7f130649;`
- `sources/com/amazon/aps/ads/Aps.java:22`
  `private static String appKey;`
- `sources/com/amazon/aps/shared/APSAnalytics.java:20`
  `private static final String DEFAULT_API_KEY = "e9026ffd475a1a3691e6b2ce637a9b92aab1073ebf53a67c5f2583be8a804ecb";`
- `sources/com/amazon/aps/shared/ApsMetrics.java:47`
  `public static final String METRICS_DEFAULT_METRICS_API_KEY = "a5c71f6aff54eb34c826d952c285eaf0650b4259c83ae598962681a6429b63f6";`
- `sources/com/amazon/aps/shared/ApsMetrics.java:48`
  `private static String apiKey = METRICS_DEFAULT_METRICS_API_KEY;`
- `sources/com/amazon/aps/shared/ApsMetrics.java:91`
  `@Metadata(d1 = {"\u0000b\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\b\n\u0002\b\u0003\n\u0002\u0010\u0006\n\u0002\b\u000b\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010\u...`
- `sources/com/amazon/device/ads/DTBAdLoader.java:9`
  `public static final String APS_VIDEO_APP_KEY = "appkey";`
- `sources/com/amazon/device/ads/DTBMetricsConfiguration.java:22`
  `static final String API_KEY_ANALYTICS_KEY_NAME = "api_key";`
- `sources/com/amazon/device/ads/DTBMetricsConfiguration.java:23`
  `public static final String APSMETRICS_APIKEY = "apiKey";`
- `sources/com/androidquery/auth/TwitterHandle.java:29`
  `private static final String OAUTH_ACCESS_TOKEN = "https://api.twitter.com/oauth/access_token";`
- `sources/com/androidquery/auth/TwitterHandle.java:32`
  `private static final String TW_SECRET = "aq.tw.secret";`
- `sources/com/applovin/mediation/adapters/MintegralMediationAdapter.java:82`
  `private static final String APP_KEY_PARAMETER = "app_key";`
- `sources/com/baidu/lbsapi/auth/LBSAuthManager.java:250`
  `java.lang.String r2 = "com.baidu.lbsapi.API_KEY"`
- `sources/com/baidu/lbsapi/auth/LBSAuthManager.java:635`
  `return context.getPackageManager().getApplicationInfo(context.getPackageName(), 128).metaData.getString("com.baidu.lbsapi.API_KEY");`
- `sources/com/beken/beken_ota/ble2/Profile.java:164`
  `public class PBSmartBandCommandIdDeviceControlAppKeyId {`
- `sources/com/beken/beken_ota/ble2/Profile.java:165`
  `public static final byte PBSmartBandCommandIdDeviceControlAppKeyAnswerPhone = 9;`
- `sources/com/beken/beken_ota/ble2/Profile.java:166`
  `public static final byte PBSmartBandCommandIdDeviceControlAppKeyExitBlood = 6;`
- `sources/com/beken/beken_ota/ble2/Profile.java:167`
  `public static final byte PBSmartBandCommandIdDeviceControlAppKeyExitCamera = 4;`
- `sources/com/beken/beken_ota/ble2/Profile.java:168`
  `public static final byte PBSmartBandCommandIdDeviceControlAppKeyExitHeart = 5;`
- `sources/com/beken/beken_ota/ble2/Profile.java:169`
  `public static final byte PBSmartBandCommandIdDeviceControlAppKeyExitMeasure = 8;`
- `sources/com/beken/beken_ota/ble2/Profile.java:170`
  `public static final byte PBSmartBandCommandIdDeviceControlAppKeyFindPhone = 1;`
- `sources/com/beken/beken_ota/ble2/Profile.java:171`
  `public static final byte PBSmartBandCommandIdDeviceControlAppKeyOpenCamera = 3;`
- `sources/com/beken/beken_ota/ble2/Profile.java:172`
  `public static final byte PBSmartBandCommandIdDeviceControlAppKeyTakePhoto = 2;`
- `sources/com/beken/beken_ota/ble2/Profile.java:175`
  `public PBSmartBandCommandIdDeviceControlAppKeyId() {`
- `sources/com/facebook/ads/internal/bridge/fbsdk/FBLoginASID.java:7`
  `Object objInvoke = Class.forName("com.facebook.AccessToken").getDeclaredMethod("getCurrentAccessToken", new Class[0]).invoke(null, new Object[0]);`
- `sources/com/facebook/ads/internal/bridge/fbsdk/FBLoginASID.java:9`
  `return (String) Class.forName("com.facebook.AccessToken").getDeclaredMethod("getUserId", new Class[0]).invoke(objInvoke, new Object[0]);`
- `sources/com/google/ads/mediation/mintegral/MintegralConstants.java:11`
  `public static final String APP_KEY = "app_key";`
- `sources/com/google/android/datatransport/cct/CCTDestination.java:14`
  `private static final String DEFAULT_API_KEY;`
- `sources/com/google/android/datatransport/cct/CCTDestination.java:23`
  `private final String apiKey;`
- `sources/com/google/android/datatransport/cct/CCTDestination.java:50`
  `DEFAULT_API_KEY = strMergeStrings3;`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:57`
  `static final String API_KEY_HEADER_KEY = "X-Goog-Api-Key";`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:209`
  `if (httpRequest.apiKey != null) {`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:210`
  `httpURLConnection.setRequestProperty(API_KEY_HEADER_KEY, httpRequest.apiKey);`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:360`
  `final String apiKey;`
- `sources/com/google/android/gms/auth/api/signin/GoogleSignInOptions.java:208`
  `return new GoogleSignInOptions(3, new ArrayList(hashSet), !TextUtils.isEmpty(strOptString) ? new Account(strOptString, "com.google") : null, jSONObject.getBoolean("idTokenRequested"), jSONObject.getBoolean("serverAuthRequested"), jSONObject.getBoolean("forceCodeForRefreshToken"), jSONObject.has("ser...`
- `sources/com/google/android/gms/auth/api/signin/GoogleSignInOptions.java:390`
  `jSONObject.put("forceCodeForRefreshToken", this.zal);`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:62`
  `public static final Task zai(HasApiKey hasApiKey, HasApiKey... hasApiKeyArr) {`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:63`
  `Preconditions.checkNotNull(hasApiKey, "Requested API must not be null.");`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:64`
  `for (HasApiKey hasApiKey2 : hasApiKeyArr) {`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:65`
  `Preconditions.checkNotNull(hasApiKey2, "Requested API must not be null.");`
- `sources/com/google/android/gms/common/api/internal/zaae.java:22`
  `public static void zad(Activity activity, GoogleApiManager googleApiManager, ApiKey apiKey) {`
- `sources/com/google/android/gms/signin/internal/SignInClientImpl.java:50`
  `bundle.putBoolean("com.google.android.gms.signin.internal.forceCodeForRefreshToken", false);`
- `sources/com/google/android/gms/signin/internal/SignInClientImpl.java:53`
  `bundle.putBoolean("com.google.android.gms.signin.internal.waitForAccessTokenRefresh", false);`
- `sources/com/google/firebase/FirebaseError.java:11`
  `public static final int ERROR_INVALID_API_KEY = 17023;`
- `sources/com/google/firebase/FirebaseOptions.java:13`
  `private static final String API_KEY_RESOURCE_NAME = "google_api_key";`
- `sources/com/google/firebase/FirebaseOptions.java:20`
  `private final String apiKey;`
- `sources/com/google/firebase/FirebaseOptions.java:57`
  `private String apiKey;`
- `sources/com/google/firebase/crashlytics/buildtools/ApiKeyValidator.java:6`
  `public class ApiKeyValidator {`
- `sources/com/google/firebase/crashlytics/buildtools/ApiKeyValidator.java:8`
  `private static final String OPEN_SOURCE_API_KEY_PATTERN = "^0[0]*$";`
- `sources/com/google/firebase/crashlytics/buildtools/ApiKeyValidator.java:9`
  `protected static final String STRINGS_API_KEY = "@string/api_key";`
- `sources/com/google/firebase/crashlytics/buildtools/ApiKeyValidator.java:10`
  `public static final String TEST_API_KEY = "testkey";`
- `sources/com/google/firebase/crashlytics/buildtools/ApiKeyValidator.java:12`
  `public static boolean isValidApiKeyFormat(String str) {`
- `sources/com/google/firebase/installations/FirebaseInstallations.java:37`
  `private static final String API_KEY_VALIDATION_MSG = "Please set a valid API key. A Firebase API key is required to communicate with Firebase server APIs: It authenticates your project with Google.Please refer to https://firebase.google.com/support/privacy/init-options.";`
- `sources/com/google/firebase/installations/Utils.java:16`
  `private static final Pattern API_KEY_FORMAT = Pattern.compile("\\AA[\\w-]{38}\\z");`
- `sources/com/google/firebase/installations/local/PersistedInstallation.java:19`
  `private static final String REFRESH_TOKEN_KEY = "RefreshToken";`
- `sources/com/google/firebase/installations/remote/AutoValue_InstallationResponse.java:102`
  `private String refreshToken;`
- `sources/com/google/firebase/installations/remote/FirebaseInstallationServiceClient.java:39`
  `private static final String API_KEY_HEADER = "x-goog-api-key";`
- `sources/com/google/firebase/installations/remote/FirebaseInstallationServiceClient.java:299`
  `httpURLConnection.addRequestProperty(API_KEY_HEADER, str);`
- `sources/com/mbridge/msdk/MBridgeConstans.java:17`
  `public static final String APP_KEY = "app_key";`
- `sources/com/mbridge/msdk/MBridgeConstans.java:52`
  `public static final String ID_MBRIDGE_APPKEY = "mbridge_appkey";`
- `sources/com/mbridge/msdk/video/dynview/moffer/MOfferModel.java:118`
  `private final String MORE_OFFER_DEFAULT_APP_KEY = "936dcbdd57fe235fd7cf61c2e93da3c4";`
- `sources/com/monetization/ads/quality/base/model/configuration/AdQualityVerifierAdapterConfiguration.java:9`
  `@Metadata(d1 = {"\u0000&\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\t\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u000e\n\u0002\u0010\b\n\u0002\b\u0002\b\u0086\b\u0018\u00002\u00020\u0001B\u001f\u0012\u0006\u0010\u0002\u001a\u00020\u0003\u0012\u0006\u0010\u00...`
- `sources/com/monetization/ads/quality/base/model/configuration/AdQualityVerifierAdapterConfiguration.java:11`
  `private final String apiKey;`
- `sources/com/os/ck.java:158`
  `IronLog.API.info("IronSourceAds.init() appkey: " + initRequest.getAppKey() + ", legacyAdFormats: " + initRequest.getLegacyAdFormats() + ", context: " + context.getClass().getSimpleName());`
- `sources/com/os/f8.java:7`
  `@Metadata(d1 = {"\u0000 \n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\u0010\u000e\n\u0002\b\u0007\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0002\b\n\b\u0086\b\u0018\u00002\u00020\u0001B\u001f\u0012\u0006\u0010\u0006\u001a\u00020\u0002\u0012\u0006\u0010\u0007\u001a\u00020\u0002\u0012\...`
- `sources/com/os/ft.java:16`
  `@Metadata(d1 = {"\u0000n\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0010\t\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u000e\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002...`
- `sources/com/os/fv.java:21`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0005\n\u0002\u0010\u000b\n\u0002\b\u0007\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0002\b\u0007\u0018\u00002\u00020\u0001B\u0007¢\u0006\u00...`
- `sources/com/os/fv.java:29`
  `private final String a(String appKey, String sdkVersion, String bundleId, String appName, String appVersion, Boolean consent, JSONObject initResponse, boolean isRewardedVideoManual, JSONObject generalProperties, JSONObject adaptersVersions, JSONObject metaData) {`
- `sources/com/os/fv.java:30`
  `String string = new JSONObject(MapsKt.mapOf(TuplesKt.to("deviceOS", "Android"), TuplesKt.to("appKey", appKey), TuplesKt.to("sdkVersion", sdkVersion), TuplesKt.to("bundleId", bundleId), TuplesKt.to("appName", appName), TuplesKt.to(d9.i.W, appVersion), TuplesKt.to("initResponse", initResponse), Tuples...`
- `sources/com/os/fv.java:52`
  `Intrinsics.checkNotNullParameter(appKey, "appKey");`
- `sources/com/os/fv.java:57`
  `a(context, a(appKey, sdkVersion, qvVar.c(context), qvVar.a(context), qvVar.b(context), consent, initResponse, isRewardedVideoManual, qvVar.b(), qvVar.c(), a()));`
- `sources/com/os/gv.java:8`
  `@Metadata(d1 = {"\u0000\b\n\u0002\u0010\u000e\n\u0002\b&\"\u0014\u0010\u0003\u001a\u00020\u00008\u0006X\u0086T¢\u0006\u0006\n\u0004\b\u0001\u0010\u0002\"\u0014\u0010\u0005\u001a\u00020\u00008\u0006X\u0086T¢\u0006\u0006\n\u0004\b\u0004\u0010\u0002\"\u0014\u0010\u0007\u001a\u00020\u00008\u0006X\u0086T...`
- `sources/com/os/gv.java:19`
  `private static final String h = "appKey";`
- `sources/com/os/ke.java:9`
  `public static final String c = "appKey";`

## BR017

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `sources/androidx/test/internal/runner/tracker/AnalyticsBasedUsageTracker.java:128`
  `MessageDigest messageDigest = MessageDigest.getInstance(MessageDigestAlgorithms.SHA_256);`
- `sources/androidx/test/internal/runner/tracker/AnalyticsBasedUsageTracker.java:129`
  `messageDigest.reset();`
- `sources/androidx/test/internal/runner/tracker/AnalyticsBasedUsageTracker.java:130`
  `messageDigest.update(this.targetPackage.getBytes("UTF-8"));`
- `sources/androidx/test/internal/runner/tracker/AnalyticsBasedUsageTracker.java:131`
  `String strValueOf = String.valueOf(new BigInteger(messageDigest.digest()).toString(16));`
- `sources/com/amazon/device/ads/DtbDeviceData.java:171`
  `MessageDigest messageDigest = MessageDigest.getInstance("SHA-1");`
- `sources/com/amazon/device/ads/DtbDeviceData.java:172`
  `messageDigest.update(str.getBytes());`
- `sources/com/amazon/device/ads/DtbDeviceData.java:173`
  `byte[] bArrDigest = messageDigest.digest();`
- `sources/com/androidquery/util/AQUtility.java:320`
  `MessageDigest messageDigest = MessageDigest.getInstance("MD5");`
- `sources/com/androidquery/util/AQUtility.java:321`
  `messageDigest.update(bArr);`
- `sources/com/applovin/impl/s4.java:356`
  `MessageDigest messageDigest = MessageDigest.getInstance(MessageDigestAlgorithms.SHA_256);`
- `sources/com/applovin/impl/s4.java:357`
  `messageDigest.update(bArr);`
- `sources/com/applovin/impl/s4.java:358`
  `messageDigest.update(str.getBytes("UTF-8"));`
- `sources/com/applovin/impl/s4.java:359`
  `return messageDigest.digest();`
- `sources/com/applovin/impl/sdk/utils/StringUtils.java:48`
  `MessageDigest messageDigest = MessageDigest.getInstance("SHA-1");`
- `sources/com/applovin/impl/sdk/utils/StringUtils.java:49`
  `messageDigest.update(str.getBytes("UTF-8"));`
- `sources/com/applovin/impl/sdk/utils/StringUtils.java:50`
  `String hexString = toHexString(messageDigest.digest());`
- `sources/com/applovin/shadow/okio/Buffer.java:36`
  `@Metadata(d1 = {"\u0000ª\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u001a\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\t\n\u0002\b\u0005\n\u0002\u0010\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n...`
- `sources/com/applovin/shadow/okio/ByteString.java:39`
  `@Metadata(d1 = {"\u0000r\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000f\n\u0000\n\u0002\u0010\u0012\n\u0002\b\u0004\n\u0002\u0010\b\n\u0002\b\u0006\n\u0002\u0010\u000e\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u0002\n\u0002\b\b\n\u0002\u0010\u000b\n\u0002\b\u0002...`
- `sources/com/applovin/shadow/okio/HashingSink.java:22`
  `@Metadata(d1 = {"\u0000D\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000...`
- `sources/com/applovin/shadow/okio/HashingSink.java:28`
  `private final MessageDigest messageDigest;`
- `sources/com/applovin/shadow/okio/HashingSink.java:31`
  `public static final HashingSink hmacSha1(Sink sink, ByteString byteString) {`
- `sources/com/applovin/shadow/okio/HashingSink.java:32`
  `return INSTANCE.hmacSha1(sink, byteString);`
- `sources/com/applovin/shadow/okio/HashingSink.java:36`
  `public static final HashingSink hmacSha256(Sink sink, ByteString byteString) {`
- `sources/com/applovin/shadow/okio/HashingSink.java:37`
  `return INSTANCE.hmacSha256(sink, byteString);`
- `sources/com/applovin/shadow/okio/HashingSink.java:41`
  `public static final HashingSink hmacSha512(Sink sink, ByteString byteString) {`
- `sources/com/applovin/shadow/okio/HashingSink.java:42`
  `return INSTANCE.hmacSha512(sink, byteString);`
- `sources/com/applovin/shadow/okio/HashingSink.java:66`
  `public HashingSink(Sink sink, MessageDigest digest) {`
- `sources/com/applovin/shadow/okio/HashingSink.java:153`
  `@Metadata(d1 = {"\u0000 \n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0007\b\u0086\u0003\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002J\u0018\u0010\u0003\u001a\u00020\u00042\u0006\u0...`
- `sources/com/applovin/shadow/okio/HashingSource.java:22`
  `@Metadata(d1 = {"\u0000>\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0010\t\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u...`
- `sources/com/applovin/shadow/okio/HashingSource.java:28`
  `private final MessageDigest messageDigest;`
- `sources/com/applovin/shadow/okio/HashingSource.java:31`
  `public static final HashingSource hmacSha1(Source source, ByteString byteString) {`
- `sources/com/applovin/shadow/okio/HashingSource.java:32`
  `return INSTANCE.hmacSha1(source, byteString);`
- `sources/com/applovin/shadow/okio/HashingSource.java:36`
  `public static final HashingSource hmacSha256(Source source, ByteString byteString) {`
- `sources/com/applovin/shadow/okio/HashingSource.java:37`
  `return INSTANCE.hmacSha256(source, byteString);`
- `sources/com/applovin/shadow/okio/HashingSource.java:41`
  `public static final HashingSource hmacSha512(Source source, ByteString byteString) {`
- `sources/com/applovin/shadow/okio/HashingSource.java:42`
  `return INSTANCE.hmacSha512(source, byteString);`
- `sources/com/applovin/shadow/okio/HashingSource.java:66`
  `public HashingSource(Source source, MessageDigest digest) {`
- `sources/com/applovin/shadow/okio/HashingSource.java:162`
  `@Metadata(d1 = {"\u0000 \n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0007\b\u0086\u0003\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002J\u0018\u0010\u0003\u001a\u00020\u00042\u0006\u0...`
- `sources/com/applovin/shadow/okio/Okio.java:48`
  `public static final HashingSink hashingSink(Sink sink, MessageDigest messageDigest) {`
- `sources/com/applovin/shadow/okio/Okio.java:49`
  `return Okio__JvmOkioKt.hashingSink(sink, messageDigest);`
- `sources/com/applovin/shadow/okio/Okio.java:56`
  `public static final HashingSource hashingSource(Source source, MessageDigest messageDigest) {`
- `sources/com/applovin/shadow/okio/Okio.java:57`
  `return Okio__JvmOkioKt.hashingSource(source, messageDigest);`
- `sources/com/applovin/shadow/okio/Okio__JvmOkioKt.java:27`
  `@Metadata(d1 = {"\u0000\u0088\u0001\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\...`
- `sources/com/applovin/shadow/okio/Okio__JvmOkioKt.java:124`
  `public static final HashingSink hashingSink(Sink sink, MessageDigest digest) {`
- `sources/com/applovin/shadow/okio/Okio__JvmOkioKt.java:130`
  `public static final HashingSource hashingSource(Source source, MessageDigest digest) {`
- `sources/com/baidu/android/bbalbs/common/security/a.java:5`
  `import javax.crypto.spec.IvParameterSpec;`
- `sources/com/baidu/android/bbalbs/common/security/a.java:6`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/baidu/android/bbalbs/common/security/a.java:11`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(str2.getBytes(), "AES");`
- `sources/com/baidu/android/bbalbs/common/security/a.java:12`
  `Cipher cipher = Cipher.getInstance(AESEncrypter.DEFAULT_ALGORITHM);`
- `sources/com/baidu/android/bbalbs/common/security/a.java:13`
  `cipher.init(1, secretKeySpec, new IvParameterSpec(str.getBytes()));`
- `sources/com/baidu/android/bbalbs/common/security/a.java:18`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(str2.getBytes(), "AES");`
- `sources/com/baidu/android/bbalbs/common/security/a.java:19`
  `Cipher cipher = Cipher.getInstance(AESEncrypter.DEFAULT_ALGORITHM);`
- `sources/com/baidu/android/bbalbs/common/security/a.java:20`
  `cipher.init(2, secretKeySpec, new IvParameterSpec(str.getBytes()));`
- `sources/com/baidu/location/b/m.java:48`
  `IvParameterSpec ivParameterSpec = new IvParameterSpec(this.b[1].getBytes("UTF-8"));`
- `sources/com/baidu/location/b/m.java:49`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(this.b[0].getBytes("UTF-8"), "AES");`
- `sources/com/baidu/location/b/m.java:50`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING");`
- `sources/com/baidu/location/b/m.java:51`
  `cipher.init(1, secretKeySpec, ivParameterSpec);`
- `sources/com/baidu/location/b/m.java:66`
  `IvParameterSpec ivParameterSpec = new IvParameterSpec(this.b[1].getBytes("UTF-8"));`
- `sources/com/baidu/location/b/m.java:67`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(this.b[0].getBytes("UTF-8"), "AES");`
- `sources/com/baidu/location/b/m.java:68`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING");`
- `sources/com/baidu/location/b/m.java:69`
  `cipher.init(2, secretKeySpec, ivParameterSpec);`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:36`
  `return hashTemplate(bArr, MessageDigestAlgorithms.MD2);`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:107`
  `java.security.MessageDigest r4 = java.security.MessageDigest.getInstance(r4)     // Catch: java.io.IOException -> L2f java.security.NoSuchAlgorithmException -> L31 java.lang.Throwable -> L47`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:115`
  `java.security.MessageDigest r4 = r2.getMessageDigest()     // Catch: java.io.IOException -> L2f java.security.NoSuchAlgorithmException -> L31 java.lang.Throwable -> L47`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:199`
  `return hashTemplate(bArr, MessageDigestAlgorithms.SHA_256);`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:211`
  `return hashTemplate(bArr, MessageDigestAlgorithms.SHA_384);`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:239`
  `public static String encryptHmacMD5ToString(String str, String str2) {`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:240`
  `return (str == null || str.length() == 0 || str2 == null || str2.length() == 0) ? "" : encryptHmacMD5ToString(str.getBytes(), str2.getBytes());`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:243`
  `public static String encryptHmacMD5ToString(byte[] bArr, byte[] bArr2) {`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:244`
  `return UtilsBridge.bytes2HexString(encryptHmacMD5(bArr, bArr2));`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:247`
  `public static byte[] encryptHmacMD5(byte[] bArr, byte[] bArr2) {`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:248`
  `return hmacTemplate(bArr, bArr2, "HmacMD5");`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:251`
  `public static String encryptHmacSHA1ToString(String str, String str2) {`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:252`
  `return (str == null || str.length() == 0 || str2 == null || str2.length() == 0) ? "" : encryptHmacSHA1ToString(str.getBytes(), str2.getBytes());`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:255`
  `public static String encryptHmacSHA1ToString(byte[] bArr, byte[] bArr2) {`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:256`
  `return UtilsBridge.bytes2HexString(encryptHmacSHA1(bArr, bArr2));`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:259`
  `public static byte[] encryptHmacSHA1(byte[] bArr, byte[] bArr2) {`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:260`
  `return hmacTemplate(bArr, bArr2, "HmacSHA1");`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:263`
  `public static String encryptHmacSHA224ToString(String str, String str2) {`
- `sources/com/blankj/utilcode/util/EncryptUtils.java:264`
  `return (str == null || str.length() == 0 || str2 == null || str2.length() == 0) ? "" : encryptHmacSHA224ToString(str.getBytes(), str2.getBytes());`

## BR018

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:36`
  `int columnIndex4 = CursorUtil.getColumnIndex(cursorQuery, "run_attempt_count");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:77`
  `workInfoPojo.runAttemptCount = cursorQuery.getInt(columnIndex4);`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:100`
  `int columnIndex4 = CursorUtil.getColumnIndex(cursorQuery, "run_attempt_count");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:141`
  `workInfoPojo.runAttemptCount = cursorQuery.getInt(columnIndex4);`
- `sources/androidx/work/impl/model/WorkSpec.java:49`
  `public int runAttemptCount;`
- `sources/androidx/work/impl/model/WorkSpec.java:90`
  `this.runAttemptCount = other.runAttemptCount;`
- `sources/androidx/work/impl/model/WorkSpec.java:113`
  `return this.state == WorkInfo.State.ENQUEUED && this.runAttemptCount > 0;`
- `sources/androidx/work/impl/model/WorkSpec.java:143`
  `return this.periodStartTime + Math.min(WorkRequest.MAX_BACKOFF_MILLIS, this.backoffPolicy == BackoffPolicy.LINEAR ? this.backoffDelayDuration * ((long) this.runAttemptCount) : (long) Math.scalb(this.backoffDelayDuration, this.runAttemptCount - 1));`
- `sources/androidx/work/impl/model/WorkSpec.java:175`
  `if (this.initialDelay != workSpec.initialDelay || this.intervalDuration != workSpec.intervalDuration || this.flexDuration != workSpec.flexDuration || this.runAttemptCount != workSpec.runAttemptCount || this.backoffDelayDuration != workSpec.backoffDelayDuration || this.periodStartTime != workSpec.per...`
- `sources/androidx/work/impl/model/WorkSpec.java:194`
  `int iHashCode3 = (((((((i2 + ((int) (j3 ^ (j3 >>> 32)))) * 31) + this.constraints.hashCode()) * 31) + this.runAttemptCount) * 31) + this.backoffPolicy.hashCode()) * 31;`
- `sources/androidx/work/impl/model/WorkSpec.java:236`
  `public int runAttemptCount;`
- `sources/androidx/work/impl/model/WorkSpec.java:248`
  `return new WorkInfo(UUID.fromString(this.id), this.state, this.output, this.tags, data, this.runAttemptCount);`
- `sources/androidx/work/impl/model/WorkSpec.java:259`
  `if (this.runAttemptCount != workInfoPojo.runAttemptCount) {`
- `sources/androidx/work/impl/model/WorkSpec.java:288`
  `int iHashCode3 = (((iHashCode2 + (data != null ? data.hashCode() : 0)) * 31) + this.runAttemptCount) * 31;`
- `sources/androidx/work/impl/model/WorkSpecDao.java:45`
  `WorkSpec.WorkInfoPojo getWorkStatusPojoForId(String id);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:47`
  `List<WorkSpec.WorkInfoPojo> getWorkStatusPojoForIds(List<String> ids);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:49`
  `List<WorkSpec.WorkInfoPojo> getWorkStatusPojoForName(String name);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:51`
  `List<WorkSpec.WorkInfoPojo> getWorkStatusPojoForTag(String tag);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:53`
  `LiveData<List<WorkSpec.WorkInfoPojo>> getWorkStatusPojoLiveDataForIds(List<String> ids);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:55`
  `LiveData<List<WorkSpec.WorkInfoPojo>> getWorkStatusPojoLiveDataForName(String name);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:57`
  `LiveData<List<WorkSpec.WorkInfoPojo>> getWorkStatusPojoLiveDataForTag(String tag);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:61`
  `int incrementWorkSpecRunAttemptCount(String id);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:71`
  `int resetWorkSpecRunAttemptCount(String id);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:29`
  `private final SharedSQLiteStatement __preparedStmtOfIncrementWorkSpecRunAttemptCount;`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:33`
  `private final SharedSQLiteStatement __preparedStmtOfResetWorkSpecRunAttemptCount;`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:42`
  `return "INSERT OR IGNORE INTO 'WorkSpec' ('id','state','worker_class_name','input_merger_class_name','input','output','initial_delay','interval_duration','flex_duration','run_attempt_count','backoff_policy','backoff_delay_duration','period_start_time','minimum_retention_duration','schedule_requested...`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:78`
  `supportSQLiteStatement.bindLong(10, workSpec.runAttemptCount);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:132`
  `this.__preparedStmtOfIncrementWorkSpecRunAttemptCount = new SharedSQLiteStatement(__db) { // from class: androidx.work.impl.model.WorkSpecDao_Impl.5`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:135`
  `return "UPDATE workspec SET run_attempt_count=run_attempt_count+1 WHERE id=?";`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:138`
  `this.__preparedStmtOfResetWorkSpecRunAttemptCount = new SharedSQLiteStatement(__db) { // from class: androidx.work.impl.model.WorkSpecDao_Impl.6`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:141`
  `return "UPDATE workspec SET run_attempt_count=0 WHERE id=?";`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:241`
  `public int incrementWorkSpecRunAttemptCount(final String id) {`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:243`
  `SupportSQLiteStatement supportSQLiteStatementAcquire = this.__preparedStmtOfIncrementWorkSpecRunAttemptCount.acquire();`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:256`
  `this.__preparedStmtOfIncrementWorkSpecRunAttemptCount.release(supportSQLiteStatementAcquire);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:261`
  `public int resetWorkSpecRunAttemptCount(final String id) {`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:263`
  `SupportSQLiteStatement supportSQLiteStatementAcquire = this.__preparedStmtOfResetWorkSpecRunAttemptCount.acquire();`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:276`
  `this.__preparedStmtOfResetWorkSpecRunAttemptCount.release(supportSQLiteStatementAcquire);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:348`
  `RoomSQLiteQuery roomSQLiteQueryAcquire = RoomSQLiteQuery.acquire("SELECT 'required_network_type', 'requires_charging', 'requires_device_idle', 'requires_battery_not_low', 'requires_storage_not_low', 'trigger_content_update_delay', 'trigger_max_content_delay', 'content_uri_triggers', 'WorkSpec'.'id' ...`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:380`
  `int columnIndexOrThrow18 = CursorUtil.getColumnIndexOrThrow(cursorQuery, "run_attempt_count");`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:408`
  `workSpec2.runAttemptCount = cursorQuery.getInt(columnIndexOrThrow18);`

## BR019

paper_id: B011
paper_title: Locking it down: The privacy and security of mobile medication apps

- `resources/com/androidquery/callback/AbstractAjaxCallback.java:285`
  `* Current supported type: JSONObject.class, String.class, byte[].class, Bitmap.class, XmlDom.class`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:397`
  `map.put(new ComponentName(activityResolveInfo.resolveInfo.activityInfo.packageName, activityResolveInfo.resolveInfo.activityInfo.name), activityResolveInfo);`
- `sources/androidx/camera/core/internal/ViewPorts.java:40`
  `map2.put(entry.getKey(), matrix);`
- `sources/androidx/camera/video/CapabilitiesByQuality.java:37`
  `this.mAreaSortedSizeToQualityMap.put(new Size(defaultVideoProfile.getWidth(), defaultVideoProfile.getHeight()), quality);`
- `sources/androidx/camera/video/CapabilitiesByQuality.java:38`
  `this.mSupportedProfilesMap.put(quality, validatedProfiles);`
- `sources/androidx/camera/video/internal/QualityExploredEncoderProfilesProvider.java:97`
  `treeMap.put(new Size(defaultVideoProfile.getWidth(), defaultVideoProfile.getHeight()), videoValidatedEncoderProfilesProxyFindNearestHigherSupportedEncoderProfilesFor);`
- `sources/androidx/camera/video/internal/compat/quirk/ExtraSupportedQualityQuirk.java:48`
  `map.put(4, immutableEncoderProfilesProxyCreate);`
- `sources/androidx/camera/video/internal/compat/quirk/ExtraSupportedQualityQuirk.java:50`
  `map.put(1, immutableEncoderProfilesProxyCreate);`
- `sources/androidx/constraintlayout/core/state/ConstraintSetParser.java:510`
  `layoutVariables.put(str, layoutVariables.get(cLObject2.get(TypedValues.TransitionType.S_FROM)), layoutVariables.get(cLObject2.get(TypedValues.TransitionType.S_TO)), 1.0f, cLObject2.getStringOrNull("prefix"), cLObject2.getStringOrNull("postfix"));`
- `sources/androidx/constraintlayout/core/state/ConstraintSetParser.java:512`
  `layoutVariables.put(str, layoutVariables.get(cLObject2.get(TypedValues.TransitionType.S_FROM)), layoutVariables.get(cLObject2.get("step")));`
- `sources/androidx/constraintlayout/core/state/helpers/ChainReference.java:59`
  `this.mMapWeights.put(string, Float.valueOf(f));`
- `sources/androidx/constraintlayout/core/state/helpers/ChainReference.java:62`
  `this.mMapPreMargin.put(string, Float.valueOf(f2));`
- `sources/androidx/constraintlayout/core/state/helpers/ChainReference.java:79`
  `this.mMapPostGoneMargin.put(string, Float.valueOf(f5));`
- `sources/androidx/constraintlayout/core/state/helpers/FlowReference.java:239`
  `this.mMapWeights.put(str, Float.valueOf(f));`
- `sources/androidx/constraintlayout/core/state/helpers/FlowReference.java:253`
  `this.mMapPostMargin.put(str, Float.valueOf(f3));`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:953`
  `sparseArray.put(childAt.getId(), this.mFrameArrayList.get(childAt));`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:1512`
  `sparseArray.put(MotionLayout.this.getId(), constraintWidgetContainer);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:673`
  `this.mTempMapIdToWidget.put(0, this.mLayoutWidget);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:674`
  `this.mTempMapIdToWidget.put(getId(), this.mLayoutWidget);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:677`
  `this.mTempMapIdToWidget.put(childAt4.getId(), getViewWidget(childAt4));`
- `sources/androidx/coordinatorlayout/widget/DirectedAcyclicGraph.java:34`
  `this.mGraph.put(t, emptyList);`
- `sources/androidx/core/graphics/TypefaceCompatApi24Impl.java:102`
  `simpleArrayMap.put(uri, byteBufferMmap);`
- `sources/androidx/core/location/LocationManagerCompat.java:122`
  `WeakReference<LocationListenerTransport> weakReferencePut = sLocationListeners.put(locationListenerTransport.getKey(), new WeakReference<>(locationListenerTransport));`
- `sources/androidx/core/location/LocationManagerCompat.java:222`
  `GnssListenersHolder.sGnssMeasurementListeners.put(callback, gnssMeasurementsTransport);`
- `sources/androidx/core/location/LocationManagerCompat.java:953`
  `GnssListenersHolder.sGnssStatusListeners.put(callback, gnssStatusTransport);`
- `sources/androidx/core/location/LocationManagerCompat.java:1056`
  `GnssListenersHolder.sGnssStatusListeners.put(callback, preRGnssStatusTransport);`
- `sources/androidx/transition/ChangeBounds.java:133`
  `transitionValues.values.put(PROPNAME_BOUNDS, new Rect(view.getLeft(), view.getTop(), view.getRight(), view.getBottom()));`
- `sources/androidx/transition/ChangeClipBounds.java:49`
  `transitionValues.values.put(PROPNAME_CLIP, rect);`
- `sources/androidx/transition/ChangeClipBounds.java:51`
  `transitionValues.values.put(PROPNAME_BOUNDS, new Rect(0, 0, view.getWidth(), view.getHeight()));`
- `sources/androidx/transition/Explode.java:42`
  `transitionValues.values.put(PROPNAME_SCREEN_BOUNDS, new Rect(i, i2, view.getWidth() + i, view.getHeight() + i2));`
- `sources/androidx/transition/VisibilityPropagation.java:31`
  `transitionValues.values.put(PROPNAME_VIEW_CENTER, iArr);`
- `sources/androidx/webkit/ProcessGlobalConfig.java:75`
  `map.put(ProcessGlobalConfigConstants.CACHE_DIRECTORY_BASE_PATH, str2);`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:139`
  `map2.put("initial_delay", new TableInfo.Column("initial_delay", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:140`
  `map2.put("interval_duration", new TableInfo.Column("interval_duration", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:141`
  `map2.put("flex_duration", new TableInfo.Column("flex_duration", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:142`
  `map2.put("run_attempt_count", new TableInfo.Column("run_attempt_count", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:143`
  `map2.put("backoff_policy", new TableInfo.Column("backoff_policy", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:144`
  `map2.put("backoff_delay_duration", new TableInfo.Column("backoff_delay_duration", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:145`
  `map2.put("period_start_time", new TableInfo.Column("period_start_time", "INTEGER", true, 0, null, 1));`
- `sources/cn/bertsir/zbar/utils/QRUtils.java:96`
  `hashtable.put(DecodeHintType.CHARACTER_SET, "UTF-8");`

## BR020

paper_id: B012
paper_title: Reviewing the data security and privacy policies of mobile apps for depression

- `sources/androidx/appcompat/widget/SearchView.java:96`
  `CursorAdapter mSuggestionsAdapter;`
- `sources/androidx/camera/core/UseCase.java:336`
  `throw new UnsupportedOperationException("Attempt to update the implementation options for a use case without attached stream specifications.");`
- `sources/androidx/camera/video/Recorder.java:2132`
  `throw new AssertionError("Attempted to update event listener with event from incorrect recording [Recording: " + videoRecordEvent.getOutputOptions() + ", Expected: " + getOutputOptions() + d9.i.e);`
- `sources/androidx/navigation/ui/R.java:2798`
  `public static final int[] TextInputLayout = {android.R.attr.enabled, android.R.attr.textColorHint, android.R.attr.maxWidth, android.R.attr.minWidth, android.R.attr.hint, android.R.attr.maxEms, android.R.attr.minEms, cn.xiaofengkj.fitpro.R.attr.boxBackgroundColor, cn.xiaofengkj.fitpro.R.attr.boxBackg...`
- `sources/androidx/room/InvalidationTracker.java:30`
  `static final String RESET_UPDATED_TABLES_SQL = "UPDATE room_table_modification_log SET invalidated = 0 WHERE invalidated = 1 ";`
- `sources/androidx/room/InvalidationTracker.java:153`
  `supportSQLiteDatabase.execSQL("PRAGMA temp_store = MEMORY;");`
- `sources/androidx/room/InvalidationTracker.java:154`
  `supportSQLiteDatabase.execSQL("PRAGMA recursive_triggers='ON';");`
- `sources/androidx/room/InvalidationTracker.java:155`
  `supportSQLiteDatabase.execSQL(CREATE_TRACKING_TABLE_SQL);`
- `sources/androidx/room/InvalidationTracker.java:190`
  `supportSQLiteDatabase.execSQL("INSERT OR IGNORE INTO room_table_modification_log VALUES(" + i + ", 0)");`
- `sources/androidx/room/InvalidationTracker.java:197`
  `sb.append(" AFTER ").append(str2).append(" ON '").append(str).append("' BEGIN UPDATE ").append(UPDATE_TABLE_NAME).append(" SET ").append(INVALIDATED_COLUMN_NAME).append(" = 1").append(" WHERE ").append(TABLE_ID_COLUMN_NAME).append(" = ").append(i).append(" AND ").append(INVALIDATED_COLUMN_NAME).appe...`
- `sources/androidx/room/InvalidationTracker.java:198`
  `supportSQLiteDatabase.execSQL(sb.toString());`
- `sources/androidx/room/paging/LimitOffsetDataSource.java:70`
  `Cursor cursorQuery = null;`
- `sources/androidx/room/paging/LimitOffsetDataSource.java:77`
  `cursorQuery = this.mDb.query(sQLiteQuery);`
- `sources/androidx/room/paging/LimitOffsetDataSource.java:78`
  `List<T> listConvertRows = convertRows(cursorQuery);`
- `sources/androidx/room/paging/LimitOffsetDataSource.java:85`
  `if (cursorQuery != null) {`
- `sources/androidx/room/paging/LimitOffsetDataSource.java:86`
  `cursorQuery.close();`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:54`
  `_db.execSQL("CREATE TABLE IF NOT EXISTS 'Dependency' ('work_spec_id' TEXT NOT NULL, 'prerequisite_id' TEXT NOT NULL, PRIMARY KEY('work_spec_id', 'prerequisite_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE , FOREIGN KEY('prerequisite_id') REFERENCES...`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:55`
  `_db.execSQL("CREATE INDEX IF NOT EXISTS 'index_Dependency_work_spec_id' ON 'Dependency' ('work_spec_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:56`
  `_db.execSQL("CREATE INDEX IF NOT EXISTS 'index_Dependency_prerequisite_id' ON 'Dependency' ('prerequisite_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:57`
  `_db.execSQL("CREATE TABLE IF NOT EXISTS 'WorkSpec' ('id' TEXT NOT NULL, 'state' INTEGER NOT NULL, 'worker_class_name' TEXT NOT NULL, 'input_merger_class_name' TEXT, 'input' BLOB NOT NULL, 'output' BLOB NOT NULL, 'initial_delay' INTEGER NOT NULL, 'interval_duration' INTEGER NOT NULL, 'flex_duration' ...`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:58`
  `_db.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkSpec_schedule_requested_at' ON 'WorkSpec' ('schedule_requested_at')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:59`
  `_db.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkSpec_period_start_time' ON 'WorkSpec' ('period_start_time')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:60`
  `_db.execSQL("CREATE TABLE IF NOT EXISTS 'WorkTag' ('tag' TEXT NOT NULL, 'work_spec_id' TEXT NOT NULL, PRIMARY KEY('tag', 'work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:61`
  `_db.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkTag_work_spec_id' ON 'WorkTag' ('work_spec_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:62`
  `_db.execSQL("CREATE TABLE IF NOT EXISTS 'SystemIdInfo' ('work_spec_id' TEXT NOT NULL, 'system_id' INTEGER NOT NULL, PRIMARY KEY('work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:31`
  `Cursor cursorQuery = DBUtil.query(this.__db, query, true, null);`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:33`
  `int columnIndex = CursorUtil.getColumnIndex(cursorQuery, "id");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:34`
  `int columnIndex2 = CursorUtil.getColumnIndex(cursorQuery, "state");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:35`
  `int columnIndex3 = CursorUtil.getColumnIndex(cursorQuery, AgentOptions.OUTPUT);`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:36`
  `int columnIndex4 = CursorUtil.getColumnIndex(cursorQuery, "run_attempt_count");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:39`
  `while (cursorQuery.moveToNext()) {`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:40`
  `if (!cursorQuery.isNull(columnIndex)) {`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:41`
  `String string = cursorQuery.getString(columnIndex);`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:74`
  `workInfoPojo.output = Data.fromByteArray(cursorQuery.getBlob(columnIndex3));`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:77`
  `workInfoPojo.runAttemptCount = cursorQuery.getInt(columnIndex4);`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:95`
  `Cursor cursorQuery = DBUtil.query(RawWorkInfoDao_Impl.this.__db, query, true, null);`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:97`
  `int columnIndex = CursorUtil.getColumnIndex(cursorQuery, "id");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:98`
  `int columnIndex2 = CursorUtil.getColumnIndex(cursorQuery, "state");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:99`
  `int columnIndex3 = CursorUtil.getColumnIndex(cursorQuery, AgentOptions.OUTPUT);`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:100`
  `int columnIndex4 = CursorUtil.getColumnIndex(cursorQuery, "run_attempt_count");`

## BR021

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `resources/AndroidManifest.xml:620`
  `<provider`
- `resources/AndroidManifest.xml:716`
  `<provider`
- `resources/AndroidManifest.xml:957`
  `<provider`
- `resources/AndroidManifest.xml:1002`
  `<provider`
- `resources/AndroidManifest.xml:1040`
  `<provider`
- `resources/AndroidManifest.xml:1049`
  `<provider`
- `resources/AndroidManifest.xml:1098`
  `<provider`
- `resources/AndroidManifest.xml:1129`
  `<provider`
- `resources/AndroidManifest.xml:1231`
  `<provider`
- `resources/AndroidManifest.xml:1236`
  `<provider`
- `resources/AndroidManifest.xml:1272`
  `<provider`
- `resources/AndroidManifest.xml:1301`
  `<provider`
- `resources/AndroidManifest.xml:1536`
  `<provider`
- `resources/AndroidManifest.xml:1541`
  `<provider`
- `resources/AndroidManifest.xml:1573`
  `<provider`
- `resources/AndroidManifest.xml:1577`
  `<provider`
- `resources/AndroidManifest.xml:1614`
  `<provider`
- `resources/AndroidManifest.xml:1632`
  `<provider`
- `resources/AndroidManifest.xml:1652`
  `<provider`
- `resources/AndroidManifest.xml:1694`
  `<provider`
- `resources/AndroidManifest.xml:1793`
  `<provider`

## BR022

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `resources/res/xml/debug_panel_file_paths.xml:3`
  `<cache-path`
- `resources/res/xml/file_path.xml:3`
  `<root-path`
- `resources/res/xml/file_path.xml:6`
  `<files-path`
- `resources/res/xml/file_path.xml:9`
  `<external-path`
- `resources/res/xml/file_path.xml:12`
  `<external-path`
- `resources/res/xml/file_paths.xml:3`
  `<external-path`
- `resources/res/xml/file_paths.xml:6`
  `<external-files-path`
- `resources/res/xml/file_paths.xml:9`
  `<external-cache-path`
- `resources/res/xml/file_paths.xml:12`
  `<files-path`
- `resources/res/xml/file_paths.xml:15`
  `<cache-path`
- `resources/res/xml/image_share_filepaths.xml:3`
  `<files-path`
- `resources/res/xml/provider_paths.xml:3`
  `<external-path`
- `resources/res/xml/provider_paths.xml:6`
  `<external-path`
- `resources/res/xml/provider_paths.xml:9`
  `<external-path`
- `resources/res/xml/qr_file_paths.xml:3`
  `<external-path`
- `resources/res/xml/util_code_provider_paths.xml:3`
  `<files-path`
- `resources/res/xml/util_code_provider_paths.xml:6`
  `<cache-path`
- `resources/res/xml/util_code_provider_paths.xml:9`
  `<external-path`
- `resources/res/xml/util_code_provider_paths.xml:12`
  `<external-files-path`
- `resources/res/xml/util_code_provider_paths.xml:15`
  `<external-cache-path`
- `resources/res/xml/util_code_provider_paths.xml:21`
  `<root-path`
- `resources/res/xml/util_code_provider_paths.xml:22`
  `name="root-path"`
- `resources/res/xml/web_files_public.xml:3`
  `<external-cache-path`

## BR023

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `sources/androidx/startup/InitializationProvider.java:10`
  `public class InitializationProvider extends ContentProvider {`
- `sources/androidx/webkit/DropDataContentProvider.java:14`
  `public final class DropDataContentProvider extends ContentProvider {`
- `sources/com/aliyun/sls/android/producer/provider/SLSContentProvider.java:10`
  `public class SLSContentProvider extends ContentProvider {`
- `sources/com/applovin/sdk/AppLovinInitProvider.java:11`
  `public class AppLovinInitProvider extends ContentProvider {`
- `sources/com/facebook/ads/AudienceNetworkContentProvider.java:11`
  `public class AudienceNetworkContentProvider extends ContentProvider {`
- `sources/com/google/android/gms/ads/MobileAdsInitProvider.java:13`
  `public class MobileAdsInitProvider extends ContentProvider {`
- `sources/com/google/android/gms/ads/internal/client/zzey.java:16`
  `public final class zzey extends ContentProvider {`
- `sources/com/google/android/gms/measurement/AppMeasurementContentProvider.java:15`
  `public class AppMeasurementContentProvider extends ContentProvider {`
- `sources/com/google/firebase/provider/FirebaseInitProvider.java:14`
  `public class FirebaseInitProvider extends ContentProvider {`
- `sources/com/os/environment/CrashProvider.java:12`
  `public class CrashProvider extends ContentProvider {`
- `sources/com/os/lifecycle/IronsourceLifecycleProvider.java:9`
  `public class IronsourceLifecycleProvider extends ContentProvider {`
- `sources/com/smartdigimkt/sdk/api/SDMInitializationProvider.java:12`
  `public class SDMInitializationProvider extends ContentProvider {`
- `sources/com/squareup/picasso/PicassoProvider.java:10`
  `public final class PicassoProvider extends ContentProvider {`
- `sources/com/thinkup/core/api/TUInitializationProvider.java:12`
  `public class TUInitializationProvider extends ContentProvider {`
- `sources/com/vungle/ads/VungleProvider.java:17`
  `public final class VungleProvider extends ContentProvider {`
- `sources/com/yandex/mobile/ads/core/initializer/MobileAdsInitializeProvider.java:16`
  `public final class MobileAdsInitializeProvider extends ContentProvider {`
- `sources/io/appmetrica/analytics/internal/PreloadInfoContentProvider.java:23`
  `public class PreloadInfoContentProvider extends ContentProvider {`
- `sources/sg/bigo/ads/controller/provider/BigoAdsProvider.java:13`
  `public class BigoAdsProvider extends ContentProvider {`

## BR024

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `sources/androidx/core/content/FileProvider.java:78`
  `if (!providerInfo.grantUriPermissions) {`
- `sources/androidx/core/content/IntentSanitizer.java:123`
  `consumer.accept("Allowing Extra Stream requires also allowing at least  FLAG_GRANT_READ_URI_PERMISSION Flag.");`
- `sources/androidx/core/content/IntentSanitizer.java:125`
  `consumer.accept("Allowing Extra Output requires also allowing FLAG_GRANT_READ_URI_PERMISSION and FLAG_GRANT_WRITE_URI_PERMISSION Flags.");`

## BR025

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/androidx/room/InvalidationTracker.java:36`
  `final RoomDatabase mDatabase;`
- `sources/androidx/room/InvalidationTracker.java:147`
  `void internalInit(SupportSQLiteDatabase supportSQLiteDatabase) {`
- `sources/androidx/room/InvalidationTracker.java:153`
  `supportSQLiteDatabase.execSQL("PRAGMA temp_store = MEMORY;");`
- `sources/androidx/room/InvalidationTracker.java:154`
  `supportSQLiteDatabase.execSQL("PRAGMA recursive_triggers='ON';");`
- `sources/androidx/room/InvalidationTracker.java:155`
  `supportSQLiteDatabase.execSQL(CREATE_TRACKING_TABLE_SQL);`
- `sources/androidx/room/InvalidationTracker.java:156`
  `syncTriggers(supportSQLiteDatabase);`
- `sources/androidx/room/InvalidationTracker.java:157`
  `this.mCleanupStatement = supportSQLiteDatabase.compileStatement(RESET_UPDATED_TABLES_SQL);`
- `sources/androidx/room/InvalidationTracker.java:189`
  `private void startTrackingTable(SupportSQLiteDatabase supportSQLiteDatabase, int i) {`
- `sources/androidx/room/InvalidationTracker.java:190`
  `supportSQLiteDatabase.execSQL("INSERT OR IGNORE INTO room_table_modification_log VALUES(" + i + ", 0)");`
- `sources/androidx/room/InvalidationTracker.java:198`
  `supportSQLiteDatabase.execSQL(sb.toString());`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:49`
  `public void onPostMigrate(SupportSQLiteDatabase _db) {`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:53`
  `public void createAllTables(SupportSQLiteDatabase _db) {`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:26`
  `private final RoomDatabase __db;`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:37`
  `public WorkSpecDao_Impl(RoomDatabase __db) {`
- `sources/com/baidu/location/b/k.java:5`
  `import android.database.sqlite.SQLiteDatabase;`
- `sources/com/baidu/location/b/k.java:22`
  `private SQLiteDatabase f = null;`
- `sources/com/facebook/ads/redexgen/core/C5Q.java:6`
  `import android.database.sqlite.SQLiteDatabase;`
- `sources/com/facebook/ads/redexgen/core/C5Q.java:71`
  `public static void A03(SQLiteDatabase sQLiteDatabase, int i, String str) throws C5N {`
- `sources/com/facebook/ads/redexgen/core/C5Q.java:74`
  `if (!C5C.A19(sQLiteDatabase, strA01)) {`
- `sources/com/facebook/ads/redexgen/core/MV.java:6`
  `import android.database.sqlite.SQLiteDatabase;`
- `sources/com/facebook/ads/redexgen/core/TH.java:80`
  `private synchronized SQLiteDatabase A01() {`
- `sources/com/facebook/ads/redexgen/core/TI.java:3`
  `import android.database.sqlite.SQLiteDatabase;`
- `sources/com/facebook/ads/redexgen/core/TI.java:4`
  `import android.database.sqlite.SQLiteOpenHelper;`
- `sources/com/facebook/ads/redexgen/core/TI.java:13`
  `public final class TI extends SQLiteOpenHelper {`
- `sources/com/facebook/ads/redexgen/core/TL.java:3`
  `import android.database.sqlite.SQLiteDatabase;`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:4`
  `import android.database.sqlite.SQLiteDatabase;`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:5`
  `import android.database.sqlite.SQLiteOpenHelper;`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:12`
  `final class SchemaManager extends SQLiteOpenHelper {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:40`
  `void upgrade(SQLiteDatabase sQLiteDatabase);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:46`
  `public final void upgrade(SQLiteDatabase sQLiteDatabase) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:47`
  `SchemaManager.lambda$static$0(sQLiteDatabase);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:53`
  `public final void upgrade(SQLiteDatabase sQLiteDatabase) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:54`
  `SchemaManager.lambda$static$1(sQLiteDatabase);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:60`
  `public final void upgrade(SQLiteDatabase sQLiteDatabase) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:61`
  `sQLiteDatabase.execSQL("ALTER TABLE events ADD COLUMN payload_encoding TEXT");`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:67`
  `public final void upgrade(SQLiteDatabase sQLiteDatabase) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:68`
  `SchemaManager.lambda$static$3(sQLiteDatabase);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:74`
  `public final void upgrade(SQLiteDatabase sQLiteDatabase) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:75`
  `SchemaManager.lambda$static$4(sQLiteDatabase);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:83`
  `sQLiteDatabase.execSQL(CREATE_EVENTS_SQL_V1);`

## BR026

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `resources/com/androidquery/auth/FacebookHandle.java:83`
  `return PreferenceManager.getDefaultSharedPreferences(context).getString(FB_TOKEN, null);`
- `resources/com/androidquery/auth/FacebookHandle.java:221`
  `return PreferenceManager.getDefaultSharedPreferences(act).getString(FB_TOKEN, null);`
- `resources/com/androidquery/auth/FacebookHandle.java:225`
  `return PreferenceManager.getDefaultSharedPreferences(act).getString(FB_PERMISSION, null);`
- `resources/com/androidquery/auth/FacebookHandle.java:229`
  `Editor editor = PreferenceManager.getDefaultSharedPreferences(act).edit();`
- `resources/com/androidquery/auth/TwitterHandle.java:166`
  `return PreferenceManager.getDefaultSharedPreferences(act).getString(key, null);`
- `resources/com/androidquery/auth/TwitterHandle.java:170`
  `PreferenceManager.getDefaultSharedPreferences(act).edit().putString(key1, token1).putString(key2, token2).commit();`
- `sources/androidx/preference/Preference.java:27`
  `import androidx.preference.PreferenceManager;`
- `sources/androidx/preference/PreferenceManager.java:10`
  `public class PreferenceManager {`
- `sources/androidx/preference/PreferenceManager.java:15`
  `private SharedPreferences.Editor mEditor;`
- `sources/androidx/preference/PreferenceManager.java:127`
  `this.mSharedPreferences = null;`
- `sources/androidx/preference/PreferenceManager.java:132`
  `this.mSharedPreferences = null;`
- `sources/androidx/preference/PreferenceManager.java:190`
  `public SharedPreferences getSharedPreferences() {`
- `sources/androidx/preference/PreferenceManager.java:191`
  `if (getPreferenceDataStore() != null) {`
- `sources/androidx/preference/PreferenceManager.java:194`
  `if (this.mSharedPreferences == null) {`
- `sources/androidx/preference/PreferenceManager.java:195`
  `this.mSharedPreferences = (this.mStorage != 1 ? this.mContext : ContextCompat.createDeviceProtectedStorageContext(this.mContext)).getSharedPreferences(this.mSharedPreferencesName, this.mSharedPreferencesMode);`
- `sources/androidx/preference/PreferenceManager.java:197`
  `return this.mSharedPreferences;`
- `sources/com/amazon/aps/ads/privacy/ApsGdprHandler.java:8`
  `import com.amazon.device.ads.DtbSharedPreferences;`
- `sources/com/amazon/aps/ads/privacy/ApsPrivacyManager.java:4`
  `import android.content.SharedPreferences;`
- `sources/com/amazon/aps/ads/privacy/ApsPrivacyManager.java:5`
  `import android.preference.PreferenceManager;`
- `sources/com/amazon/aps/ads/privacy/ApsPrivacyManager.java:10`
  `import com.amazon.device.ads.DtbSharedPreferences;`
- `sources/com/amazon/aps/ads/util/adview/ApsAdViewFetchUtils.java:20`
  `import com.amazon.device.ads.DtbSharedPreferences;`
- `sources/com/amazon/aps/ads/util/adview/ApsAdViewFetchUtils.java:307`
  `boolean optOut = DtbSharedPreferences.getInstance().getOptOut();`
- `sources/com/amazon/device/ads/AdRegistration.java:212`
  `String versionInUse = dtbSharedPreferencesCreateInstance.getVersionInUse();`
- `sources/com/amazon/device/ads/AdRegistration.java:214`
  `dtbSharedPreferencesCreateInstance.setVersionInUse(DtbConstants.SDK_VERSION);`
- `sources/com/amazon/device/ads/AdRegistration.java:250`
  `DtbSharedPreferences.createInstance();`
- `sources/com/amazon/device/ads/DTBAdRequest.java:5`
  `import android.content.SharedPreferences;`
- `sources/com/amazon/device/ads/DTBAdRequest.java:496`
  `removeAaxHostNameFromSharedPreferences();`
- `sources/com/amazon/device/ads/DtbAdRequestParamsBuilder.java:49`
  `Boolean optOut = DtbSharedPreferences.getInstance().getOptOut();`
- `sources/com/amazon/device/ads/DtbAdRequestParamsBuilder.java:62`
  `String adId = DtbSharedPreferences.getInstance().getAdId();`
- `sources/com/amazon/device/ads/DTBAdResponse.java:364`
  `aaxHostName = DtbDebugProperties.getAaxHostName(DtbSharedPreferences.getInstance().getAaxHostname());`
- `sources/com/amazon/device/ads/DtbCommonUtils.java:4`
  `import android.content.SharedPreferences;`
- `sources/com/amazon/device/ads/DtbDeviceRegistration.java:4`
  `import android.content.SharedPreferences;`
- `sources/com/amazon/device/ads/DtbDeviceRegistration.java:6`
  `import android.preference.PreferenceManager;`
- `sources/com/amazon/device/ads/DtbDeviceRegistration.java:80`
  `if (System.currentTimeMillis() - DtbSharedPreferences.getInstance().getSisLastPing() < 2592000000L) {`
- `sources/com/amazon/device/ads/DtbDeviceRegistration.java:151`
  `long jLongValue = jCurrentTimeMillis - DtbSharedPreferences.getInstance().getConfigLastCheckIn().longValue();`
- `sources/com/amazon/device/ads/DtbDeviceRegistration.java:152`
  `long configTtlInMilliSeconds = DtbSharedPreferences.getInstance().getConfigTtlInMilliSeconds();`
- `sources/com/amazon/device/ads/DtbDeviceRegistration.java:277`
  `String adId = DtbSharedPreferences.getInstance().getAdId();`
- `sources/com/amazon/device/ads/DtbDeviceRegistration.java:281`
  `String idfa = DtbSharedPreferences.getInstance().getIdfa();`
- `sources/com/amazon/device/ads/DtbDeviceRegistration.java:282`
  `Boolean optOut = DtbSharedPreferences.getInstance().getOptOut();`
- `sources/com/amazon/device/ads/DtbDeviceRegistration.java:365`
  `DtbSharedPreferences.getInstance().saveSisLastCheckIn(System.currentTimeMillis());`

## BR027

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `resources/com/androidquery/util/AQUtility.java:642`
  `File ext = Environment.getExternalStorageDirectory();`
- `resources/com/androidquery/util/AQUtility.java:643`
  `File tempDir = new File(ext, "aquery/temp");`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:120`
  `File file = new File(this.mAppContext.getFilesDir(), BrowserServiceFileProvider.FILE_SUB_DIR);`
- `sources/androidx/camera/video/Recorder.java:2022`
  `if (outputOptions instanceof MediaStoreOutputOptions) {`
- `sources/androidx/camera/video/Recorder.java:2023`
  `final MediaStoreOutputOptions mediaStoreOutputOptions = (MediaStoreOutputOptions) outputOptions;`
- `sources/androidx/camera/video/Recorder.java:2064`
  `} else if (outputOptions instanceof MediaStoreOutputOptions) {`
- `sources/androidx/camera/video/internal/compat/quirk/DeviceQuirksLoader.java:38`
  `if (MediaStoreVideoCannotWrite.load()) {`
- `sources/androidx/camera/video/internal/compat/quirk/DeviceQuirksLoader.java:39`
  `arrayList.add(new MediaStoreVideoCannotWrite());`
- `sources/androidx/camera/view/CameraController.java:735`
  `public Recording startRecording(MediaStoreOutputOptions mediaStoreOutputOptions, AudioConfig audioConfig, Executor executor, Consumer<VideoRecordEvent> consumer) {`
- `sources/androidx/camera/view/CameraController.java:736`
  `return startRecordingInternal(mediaStoreOutputOptions, audioConfig, executor, consumer);`
- `sources/androidx/core/graphics/drawable/IconCompat.java:357`
  `return new FileInputStream(new File((String) this.mObj1));`
- `sources/androidx/core/util/AtomicFile.java:23`
  `this.mNewName = new File(file.getPath() + ".new");`
- `sources/androidx/core/util/AtomicFile.java:24`
  `this.mLegacyBackupName = new File(file.getPath() + ".bak");`
- `sources/androidx/datastore/migrations/SharedPreferencesMigration.java:403`
  `return new File(new File(context.getApplicationInfo().dataDir, "shared_prefs"), Intrinsics.stringPlus(name, ".xml"));`
- `sources/androidx/datastore/migrations/SharedPreferencesMigration.java:407`
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
- `sources/androidx/multidex/MultiDex.java:220`
  `File file = new File(context.getFilesDir(), "secondary-dexes");`
- `sources/androidx/multidex/MultiDex.java:245`
  `File file2 = new File(file, CODE_CACHE_NAME);`
- `sources/androidx/multidex/MultiDexExtractor.java:61`
  `File file3 = new File(file2, LOCK_FILENAME);`
- `sources/androidx/profileinstaller/ProfileInstaller.java:211`
  `String name = new File(applicationInfo.sourceDir).getName();`
- `sources/androidx/sqlite/db/SupportSQLiteOpenHelper.java:89`
  `SQLiteDatabase.deleteDatabase(new File(str));`
- `sources/androidx/sqlite/db/framework/FrameworkSQLiteOpenHelper.java:44`
  `this.mDelegate = new OpenHelper(this.mContext, new File(this.mContext.getNoBackupFilesDir(), this.mName).getAbsolutePath(), frameworkSQLiteDatabaseArr, this.mCallback);`
- `sources/androidx/test/internal/runner/listener/CoverageListener.java:40`
  `File file = new File(this.mCoverageFilePath);`
- `sources/androidx/webkit/WebViewAssetLoader.java:78`
  `this.mDirectory = new File(AssetHelper.getCanonicalDirPath(file));`
- `sources/androidx/work/impl/WorkDatabasePathHelper.java:50`
  `map.put(new File(defaultDatabasePath.getPath() + str), new File(databasePath.getPath() + str));`
- `sources/androidx/work/impl/WorkDatabasePathHelper.java:64`
  `return new File(context.getNoBackupFilesDir(), filePath);`
- `sources/cn/bertsir/zbar/QRActivity.java:58`
  `private String cropTempPath = Environment.getExternalStorageDirectory().getAbsolutePath() + File.separator + "cropQr.jpg";`
- `sources/cn/bertsir/zbar/utils/GetPathFromUri.java:9`
  `import android.provider.MediaStore;`
- `sources/cn/bertsir/zbar/utils/GetPathFromUri.java:30`
  `uri2 = MediaStore.Images.Media.EXTERNAL_CONTENT_URI;`
- `sources/cn/bertsir/zbar/utils/GetPathFromUri.java:32`
  `uri2 = MediaStore.Video.Media.EXTERNAL_CONTENT_URI;`
- `sources/cn/bertsir/zbar/utils/GetPathFromUri.java:34`
  `uri2 = MediaStore.Audio.Media.EXTERNAL_CONTENT_URI;`
- `sources/com/aliyun/sls/android/producer/LogProducerConfig.java:262`
  `File file = new File(path.substring(0, path.lastIndexOf(File.separator)));`
- `sources/com/aliyun/sls/android/producer/LogProducerConfig.java:283`
  `return new File(file, strSubstring).getAbsolutePath();`
- `sources/com/amazon/device/ads/DtbDebugProperties.java:77`
  `File file = new File(context.getFilesDir() + "/aps_override_properties/override.properties");`
- `sources/com/amazon/device/ads/DTBMetricsConfiguration.java:156`
  `File file = new File(filesDir.getAbsolutePath() + "/config/aps_mobile_client_config.json");`
- `sources/com/amazon/device/ads/WebResourceService.java:65`
  `renameTo(fileCreateTempFile, new File(filesDir.getAbsolutePath() + WEB_DIR + str));`

## BR028

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `resources/AndroidManifest.xml:149`
  `android:allowBackup="true"`
- `resources/AndroidManifest.xml:153`
  `android:fullBackupContent="@xml/backup_rules"`
- `resources/AndroidManifest.xml:158`
  `android:dataExtractionRules="@xml/data_extraction_rules">`

## BR029

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:202`
  `android:exported="true">`
- `resources/AndroidManifest.xml:211`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:214`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:217`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:221`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:224`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:227`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:230`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:233`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:236`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:239`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:242`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:245`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:248`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:251`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:254`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:257`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:260`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:263`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:266`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:269`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:272`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:275`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:278`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:281`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:284`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:287`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:290`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:293`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:296`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:299`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:302`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:305`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:308`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:311`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:314`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:318`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:321`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:324`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:327`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:330`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:333`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:336`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:339`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:342`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:345`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:348`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:351`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:354`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:357`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:360`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:363`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:366`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:370`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:373`
  `android:exported="true"`
- `resources/AndroidManifest.xml:377`
  `android:exported="true"`
- `resources/AndroidManifest.xml:387`
  `android:exported="true"`
- `resources/AndroidManifest.xml:392`
  `android:exported="true"`
- `resources/AndroidManifest.xml:397`
  `android:exported="true"`
- `resources/AndroidManifest.xml:402`
  `android:exported="true"`
- `resources/AndroidManifest.xml:412`
  `android:exported="true"`
- `resources/AndroidManifest.xml:416`
  `android:exported="true"`
- `resources/AndroidManifest.xml:420`
  `android:exported="true"`
- `resources/AndroidManifest.xml:424`
  `android:exported="true"`
- `resources/AndroidManifest.xml:428`
  `android:exported="true"`
- `resources/AndroidManifest.xml:432`
  `android:exported="true"`
- `resources/AndroidManifest.xml:436`
  `android:exported="true"`
- `resources/AndroidManifest.xml:440`
  `android:exported="true"`
- `resources/AndroidManifest.xml:444`
  `android:exported="true"`
- `resources/AndroidManifest.xml:448`
  `android:exported="true"`
- `resources/AndroidManifest.xml:452`
  `android:exported="true"`
- `resources/AndroidManifest.xml:456`
  `android:exported="true"`
- `resources/AndroidManifest.xml:460`
  `android:exported="true"`
- `resources/AndroidManifest.xml:464`
  `android:exported="true"`
- `resources/AndroidManifest.xml:468`
  `android:exported="true"`
- `resources/AndroidManifest.xml:472`
  `android:exported="true"`
- `resources/AndroidManifest.xml:476`
  `android:exported="true"`
- `resources/AndroidManifest.xml:481`
  `android:exported="true"`
- `resources/AndroidManifest.xml:486`
  `android:exported="true"`
- `resources/AndroidManifest.xml:491`
  `android:exported="true"`

## BR030

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:214`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:217`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:221`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:578`
  `android:exported="true"`
- `resources/AndroidManifest.xml:587`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:592`
  `android:exported="true"`
- `resources/AndroidManifest.xml:605`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:609`
  `android:exported="true"`
- `resources/AndroidManifest.xml:662`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:665`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:669`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:702`
  `android:exported="true"`
- `resources/AndroidManifest.xml:707`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:904`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:948`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:952`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:956`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:1066`
  `android:exported="true"`
- `resources/AndroidManifest.xml:1454`
  `android:exported="true"`

## BR031

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:570`
  `android:exported="true">`
- `resources/AndroidManifest.xml:891`
  `android:exported="true">`
- `resources/AndroidManifest.xml:1066`
  `android:exported="true"`
- `resources/AndroidManifest.xml:1454`
  `android:exported="true"`
- `resources/AndroidManifest.xml:1524`
  `android:exported="true"`
- `resources/AndroidManifest.xml:1586`
  `android:exported="true">`
- `resources/AndroidManifest.xml:1595`
  `android:exported="true"`
- `resources/AndroidManifest.xml:1800`
  `android:exported="true">`

## BR032

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `resources/AndroidManifest.xml:69`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:73`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:85`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:96`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:101`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:543`
  `<action android:name="android.intent.action.VIEW"/>`

## BR033

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `resources/com/androidquery/auth/BasicHandle.java:53`
  `Uri uri = Uri.parse(cb.getUrl());`
- `resources/com/androidquery/auth/BasicHandle.java:69`
  `Uri uri = Uri.parse(cb.getUrl());`
- `resources/com/androidquery/service/MarketService.java:272`
  `Uri uri = Uri.parse(url);`
- `sources/androidx/browser/browseractions/BrowserActionsIntent.java:182`
  `return context.getPackageManager().queryIntentActivities(new Intent(ACTION_BROWSER_ACTIONS_OPEN, Uri.parse(TEST_URL)), 131072);`
- `sources/cn/bertsir/zbar/utils/PermissionUtils.java:108`
  `intent.setData(Uri.parse("package:" + mApp.getPackageName()));`
- `sources/com/amazon/aps/ads/util/ApsUtils.java:81`
  `intent.setData(Uri.parse(str));`
- `sources/com/amazon/aps/ads/util/adview/ApsAdWebViewSchemeHandler.java:72`
  `this.webviewClientListener.getAdViewContext().startActivity(new Intent("android.intent.action.VIEW", Uri.parse("https://" + strSubstring)));`
- `sources/com/amazon/aps/ads/util/adview/ApsAdWebViewSchemeHandler.java:87`
  `intent.setData(Uri.parse(sb.append(strSubstring).toString()));`
- `sources/com/amazon/device/ads/DTBAdMRAIDController.java:521`
  `getContext().startActivity(new Intent("android.intent.action.VIEW", Uri.parse(strDecode)));`
- `sources/com/amazon/device/ads/DTBAdMRAIDController.java:543`
  `intent2.setData(Uri.parse("https://www.amazon.com/dp/" + str.substring(iIndexOf + 9)));`
- `sources/com/amazon/device/ads/DTBAdUtil.java:300`
  `Uri uri2 = Uri.parse(str);`
- `sources/com/androidquery/auth/BasicHandle.java:44`
  `httpRequest.addHeader("Host", Uri.parse(abstractAjaxCallback.getUrl()).getHost());`
- `sources/com/androidquery/auth/BasicHandle.java:52`
  `httpURLConnection.setRequestProperty("Host", Uri.parse(abstractAjaxCallback.getUrl()).getHost());`
- `sources/com/androidquery/service/MarketService.java:149`
  `activity.startActivity(new Intent("android.intent.action.VIEW", Uri.parse(str)));`
- `sources/com/applovin/impl/j5.java:485`
  `File fileA = this.j.a(k7.a(Uri.parse(str2), this.g.getCachePrefix(), this.f3486a), com.applovin.impl.sdk.k.o());`
- `sources/com/applovin/impl/j5.java:490`
  `return Uri.parse(AdPayload.FILE_SCHEME + fileA.getAbsolutePath());`
- `sources/com/applovin/impl/j5.java:494`
  `return Uri.parse(AdPayload.FILE_SCHEME + fileA.getAbsolutePath());`
- `sources/com/applovin/impl/t0.java:122`
  `Uri uri = URLUtil.isValidUrl(string2) ? Uri.parse(string2) : null;`
- `sources/com/applovin/impl/t0.java:124`
  `return new TermsAndPrivacyPolicyFlowSettingsImpl(bool2.booleanValue(), bool3.booleanValue(), a(string), URLUtil.isValidUrl(string3) ? Uri.parse(string3) : null, uri);`
- `sources/com/applovin/impl/t0.java:295`
  `return Uri.parse((String) this.f3774a.a(this.f3774a.I0() ? v4.M6 : v4.L6));`
- `sources/com/blankj/utilcode/util/FileUtils.java:990`
  `intent.setData(Uri.parse(AdPayload.FILE_SCHEME + file.getAbsolutePath()));`
- `sources/com/blankj/utilcode/util/PermissionUtils.java:182`
  `intent.setData(Uri.parse("package:" + Utils.getApp().getPackageName()));`
- `sources/com/blankj/utilcode/util/PermissionUtils.java:206`
  `intent.setData(Uri.parse("package:" + Utils.getApp().getPackageName()));`
- `sources/com/bytedance/sdk/openadsdk/qbp/ouw/ouw/vt.java:57`
  `Intent intent = new Intent("android.intent.action.VIEW", Uri.parse(str));`
- `sources/com/bytedance/sdk/openadsdk/utils/DeviceUtils.java:473`
  `applicationContext.getContentResolver().registerContentObserver(Uri.parse("content://settings/system/POWER_SAVE_MODE_OPEN"), false, new ContentObserver(null) { // from class: com.bytedance.sdk.openadsdk.utils.DeviceUtils.3`
- `sources/com/bytedance/sdk/openadsdk/utils/uoy.java:675`
  `return Uri.parse(str).buildUpon().appendQueryParameter(fl.SESSION_HISTORY_KEY_AD_ID, "1371").appendQueryParameter("device_platform", "android").appendQueryParameter("version_code", pno()).toString();`
- `sources/com/bytedance/sdk/openadsdk/utils/vpp.java:90`
  `intent.setData(Uri.parse(str));`
- `sources/com/google/ads/mediation/vungle/rtb/VungleRtbNativeAd.java:229`
  `setIcon(new VungleNativeMappedImage(Uri.parse(appIcon)));`
- `sources/com/google/android/gms/ads/internal/zzs.java:201`
  `intent.setData(Uri.parse(str));`
- `sources/com/google/android/gms/ads/internal/util/zzav.java:21`
  `zzs.zzab(this.zza, Uri.parse("https://support.google.com/dfp_premium/answer/7160685#push"));`
- `sources/com/google/android/gms/internal/ads/zzbws.java:29`
  `DownloadManager.Request request = new DownloadManager.Request(Uri.parse(str));`
- `sources/com/google/android/gms/internal/ads/zzbzx.java:157`
  `return packageManager.resolveActivity(new Intent("android.intent.action.VIEW", Uri.parse(str)), 65536);`
- `sources/com/google/android/gms/internal/ads/zzejf.java:295`
  `launchIntentForPackage.setData(Uri.parse(stringExtra3));`
- `sources/com/google/android/gms/internal/consent_sdk/zzcd.java:77`
  `Uri uri = Uri.parse(strOptString);`
- `sources/com/google/android/gms/internal/consent_sdk/zzcd.java:193`
  `Uri uri = Uri.parse(str);`
- `sources/com/inmobi/media/AbstractC3324z2.java:131`
  `Uri uri2 = Uri.parse(url);`
- `sources/com/inmobi/media/AbstractC3324z2.java:132`
  `Intrinsics.checkNotNullExpressionValue(uri2, "Uri.parse(this)");`
- `sources/com/iwellfitness/urllib/ManualUrlConfig.java:90`
  `intent.setData(Uri.parse(openUrlRequest.getUrl()));`
- `sources/com/just/agentweb/DefaultWebClient.java:217`
  `intent.setData(Uri.parse(str));`
- `sources/com/just/agentweb/DefaultWebClient.java:411`
  `intent.setData(Uri.parse(str));`
- `sources/com/luck/picture/lib/permissions/PermissionChecker.java:23`
  `intent.setData(Uri.parse("package:" + applicationContext.getPackageName()));`
- `sources/com/mbridge/msdk/advanced/signal/NativeAdvancedExpandDialog.java:139`
  `com.mbridge.msdk.foundation.controller.c.m().d().startActivity(new Intent("android.intent.action.VIEW", Uri.parse(str)));`
- `sources/com/mbridge/msdk/advanced/view/a.java:60`
  `strA = this.h.a(URLDecoder.decode(Uri.parse(str).getQueryParameter("uri")));`
- `sources/com/mbridge/msdk/click/c.java:145`
  `Intent intent2 = new Intent("android.intent.action.VIEW", Uri.parse(str));`
- `sources/com/mbridge/msdk/foundation/tools/t0.java:270`
  `Intent intent2 = new Intent("android.intent.action.VIEW", Uri.parse(str));`
- `sources/com/mbridge/msdk/mbbanner/common/communication/b.java:236`
  `com.mbridge.msdk.foundation.controller.c.m().d().startActivity(new Intent("android.intent.action.VIEW", Uri.parse(str)));`
- `sources/com/mbridge/msdk/mbbanner/common/communication/BannerExpandDialog.java:139`
  `com.mbridge.msdk.foundation.controller.c.m().d().startActivity(new Intent("android.intent.action.VIEW", Uri.parse(str)));`
- `sources/com/mbridge/msdk/mbbanner/view/a.java:67`
  `c.m().d().startActivity(new Intent("android.intent.action.VIEW", Uri.parse(str)));`
- `sources/com/mbridge/msdk/mbsignalcommon/commonwebview/CommonWebView.java:550`
  `Uri uri3 = Uri.parse(str);`
- `sources/com/mbridge/msdk/splash/signal/SplashExpandDialog.java:140`
  `com.mbridge.msdk.foundation.controller.c.m().d().startActivity(new Intent("android.intent.action.VIEW", Uri.parse(str)));`
- `sources/com/mbridge/msdk/video/module/listener/impl/a.java:34`
  `intent.setData(Uri.parse(strA));`
- `sources/com/os/pw.java:19`
  `intent.setData(Uri.parse(str));`
- `sources/com/os/sdk/controller/v.java:2555`
  `Uri uri = Uri.parse(SDKUtils.getControllerUrl());`
- `sources/com/realsil/sdk/support/base/BaseActivity.java:268`
  `intent.setData(Uri.parse("package:" + str));`
- `sources/com/realsil/sdk/support/file/BaseFileExplorerActivity.java:193`
  `Intent intent2 = new Intent("android.intent.action.VIEW", Uri.parse(getResources().getStringArray(R.array.rtk_app_file_browser_action)[checkedItemPosition]));`
- `sources/com/realsil/sdk/support/file/RxFileFragment.java:176`
  `Intent intent2 = new Intent("android.intent.action.VIEW", Uri.parse(getResources().getStringArray(R.array.rtk_app_file_browser_action)[checkedItemPosition]));`
- `sources/com/realsil/sdk/support/permission/PermissionHelper.java:121`
  `intent.setData(Uri.parse("package:" + activity.getPackageName()));`
- `sources/com/realsil/sdk/support/settings/DevelopmentPreferenceFragment.java:94`
  `startActivity(new Intent("android.intent.action.VIEW", Uri.parse(uriString)));`
- `sources/com/realsil/sdk/support/utilities/IntentUtils.java:124`
  `intent.setData(Uri.parse("package:" + context.getPackageName()));`
- `sources/com/smartdigimkt/e1/a.java:60`
  `com.smartdigimkt.m6.b.p().k().startActivity(new Intent("android.intent.action.VIEW", Uri.parse(str)));`
- `sources/com/smartdigimkt/expressad/advanced/js/NativeAdvancedExpandDialog.java:62`
  `b.p().k().startActivity(new Intent("android.intent.action.VIEW", Uri.parse(str)));`
- `sources/com/smartdigimkt/expressad/splash/js/SplashExpandDialog.java:62`
  `b.p().k().startActivity(new Intent("android.intent.action.VIEW", Uri.parse(str)));`
- `sources/com/smartdigimkt/g/a.java:52`
  `strReplace = this.g.a(URLDecoder.decode(Uri.parse(str).getQueryParameter("uri")));`
- `sources/com/smartdigimkt/q3/d.java:266`
  `Intent intent2 = new Intent("android.intent.action.VIEW", Uri.parse(str));`
- `sources/com/smartdigimkt/y0/b.java:111`
  `com.smartdigimkt.m6.b.p().k().startActivity(new Intent("android.intent.action.VIEW", Uri.parse(str)));`
- `sources/com/smartdigimkt/y0/c.java:105`
  `com.smartdigimkt.m6.b.p().k().startActivity(new Intent("android.intent.action.VIEW", Uri.parse(str)));`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:323`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/finderOpenProfile"), null, null, new String[]{this.appId, ((WXChannelOpenProfile.Req) baseReq).userName}, null);`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:365`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/jumpToOfflinePay"), null, null, new String[]{this.appId}, null);`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:376`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/launchWXMiniprogram"), null, null, new String[]{this.appId, req.userName, req.path, req.miniprogramType + "", req.extData}, null);`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:396`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/openTypeWebview"), null, null, new String[]{this.appId, String.valueOf(3), URLEncoder.encode(String.format("url=%s", URLEncoder.encode(((WXNontaxPay.Req) baseReq).url)))}, null);`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:472`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/openTypeWebview"), null, null, new String[]{this.appId, String.valueOf(4), URLEncoder.encode(String.format("url=%s", URLEncoder.encode(((WXPayInsurance.Req) baseReq).url)))}, null);`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:523`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/preloadWXMiniprogram"), null, null, new String[]{this.appId, req.userName, req.path, req.miniprogramType + "", req.extData}, null);`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:534`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/QRCodePay"), null, null, new String[]{this.appId, req.codeContent, req.extraMsg}, null);`
- `sources/com/thinkup/core/activity/component/PrivacyPolicyView.java:320`
  `intent.setData(Uri.parse(str));`
- `sources/com/thinkup/core/activity/component/PrivacyPolicyView.java:373`
  `intent.setData(Uri.parse(str));`
- `sources/com/thinkup/core/basead/o/n.java:261`
  `Intent intent = new Intent("android.intent.action.VIEW", Uri.parse(str));`
- `sources/com/thinkup/core/basead/o/n.java:271`
  `Intent intent2 = new Intent("android.intent.action.VIEW", Uri.parse(str));`
- `sources/com/unity3d/ads/core/domain/AndroidHandleOpenUrl.java:30`
  `intent.setData(Uri.parse(url));`
- `sources/com/unity3d/services/ads/measurements/MeasurementsService.java:75`
  `measurementManager.registerTrigger(Uri.parse(url), ExecutorsKt.asExecutor(this.dispatchers.getDefault()), new MeasurementsReceiver(this.eventSender, MeasurementsEvents.TRIGGER_SUCCESSFUL, MeasurementsEvents.TRIGGER_ERROR));`
- `sources/com/yandex/android/beacon/SendBeaconDb.java:134`
  `Uri uri = Uri.parse(cursor.getString(1));`

## BR034

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `resources/com/androidquery/service/MarketService.java:274`
  `act.startActivity(intent);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:146`
  `ContextCompat.startActivity(context, this.intent, this.startAnimationBundle);`
- `sources/androidx/browser/customtabs/TrustedWebUtils.java:31`
  `context.startActivity(intent);`
- `sources/cn/bertsir/zbar/utils/PermissionUtils.java:109`
  `mApp.startActivity(intent.addFlags(268435456));`
- `sources/com/amazon/aps/ads/util/ApsUtils.java:82`
  `context.startActivity(intent);`
- `sources/com/amazon/aps/ads/util/adview/ApsAdWebViewSchemeHandler.java:89`
  `this.webviewClientListener.getAdViewContext().startActivity(intent);`
- `sources/com/amazon/aps/ads/util/adview/ApsAdWebViewSchemeHandler.java:100`
  `this.webviewClientListener.getAdViewContext().startActivity(intent);`
- `sources/com/amazon/aps/ads/util/adview/ApsAdWebViewSchemeHandler.java:118`
  `this.webviewClientListener.getAdViewContext().startActivity(intent);`
- `sources/com/amazon/device/ads/DTBAdMRAIDController.java:537`
  `AdRegistration.getCurrentActivity().startActivity(intent);`
- `sources/com/amazon/device/ads/DTBAdMRAIDController.java:544`
  `AdRegistration.getCurrentActivity().startActivity(intent2);`
- `sources/com/amazon/device/ads/DTBAdMRAIDController.java:560`
  `AdRegistration.getCurrentActivity().startActivity(intent3);`
- `sources/com/amazon/device/ads/DTBAdUtil.java:303`
  `AdRegistration.getCurrentActivity().startActivity(intent);`
- `sources/com/blankj/utilcode/util/FileUtils.java:991`
  `Utils.getApp().sendBroadcast(intent);`
- `sources/com/bytedance/sdk/openadsdk/core/settings/cf.java:318`
  `contextOuw.sendBroadcast(intent);`
- `sources/com/bytedance/sdk/openadsdk/core/settings/cf.java:331`
  `contextOuw.sendBroadcast(intent);`
- `sources/com/bytedance/sdk/openadsdk/core/widget/ouw/fkw.java:435`
  `this.yu.startActivity(intent);`
- `sources/com/google/android/gms/ads/internal/zzs.java:202`
  `this.zzc.startActivity(intent);`
- `sources/com/google/android/gms/ads/internal/util/zzs.java:634`
  `context.startActivity(intent);`
- `sources/com/google/android/gms/internal/ads/zzejf.java:298`
  `context.startActivity(launchIntentForPackage);`
- `sources/com/google/android/gms/measurement/internal/zzfa.java:40`
  `this.zza.doStartService(context, className);`
- `sources/com/iwellfitness/urllib/ManualUrlConfig.java:92`
  `context.startActivity(intent);`
- `sources/com/just/agentweb/DefaultWebClient.java:218`
  `activity.startActivity(intent);`
- `sources/com/just/agentweb/DefaultWebClient.java:412`
  `this.mWeakReference.get().startActivity(intent);`
- `sources/com/luck/picture/lib/broadcast/BroadcastManager.java:172`
  `localBroadcastManager.sendBroadcast(this.intent);`
- `sources/com/luck/picture/lib/permissions/PermissionChecker.java:25`
  `applicationContext.startActivity(intent.addFlags(268435456));`
- `sources/com/mbridge/msdk/click/a.java:453`
  `this.d.sendBroadcast(intent);`
- `sources/com/mbridge/msdk/click/a.java:1360`
  `this.d.sendBroadcast(intent);`
- `sources/com/mbridge/msdk/playercommon/exoplayer2/offline/DownloadService.java:206`
  `context.startService(new Intent(context, cls).setAction(ACTION_INIT));`
- `sources/com/mbridge/msdk/video/module/listener/impl/a.java:35`
  `this.f7613a.startActivity(intent);`
- `sources/com/os/pw.java:23`
  `context.startActivity(intent);`
- `sources/com/realsil/sdk/support/permission/PermissionHelper.java:115`
  `activity.startActivity(intent);`
- `sources/com/realsil/sdk/support/permission/PermissionHelper.java:137`
  `activity.startActivity(intent);`
- `sources/com/realsil/sdk/support/permission/PermissionHelper.java:153`
  `activity.startActivity(intent);`
- `sources/com/realsil/sdk/support/settings/SettingsActivity.java:25`
  `context.startActivity(intent);`
- `sources/com/realsil/sdk/support/utilities/IntentUtils.java:128`
  `context.startActivity(intent);`
- `sources/com/thinkup/core/activity/component/PrivacyPolicyView.java:322`
  `context.startActivity(intent);`
- `sources/com/thinkup/core/activity/component/PrivacyPolicyView.java:375`
  `context.startActivity(intent);`
- `sources/com/unity3d/ads/core/domain/AndroidHandleOpenUrl.java:32`
  `this.context.startActivity(intent);`
- `sources/com/yandex/div/internal/util/PermissionUtils.java:126`
  `context.startActivity(new Intent("android.settings.APPLICATION_DETAILS_SETTINGS").setData(Uri.fromParts("package", context.getPackageName(), null)).addFlags(268435456));`
- `sources/com/yandex/mobile/ads/impl/vx.java:71`
  `this.f12396a.startActivity(intent);`
- `sources/xfkj/fitpro/application/MyApplication.java:368`
  `public static void doSendBroadcast(Map<String, Object> map) {`
- `sources/xfkj/fitpro/application/MyApplication.java:375`
  `getContext().sendBroadcast(intent);`
- `sources/xfkj/fitpro/utils/KeepLiveUtils.java:28`
  `context.startActivity(intent);`
- `sources/xfkj/fitpro/utils/NotificationUtil.java:69`
  `activity.startActivity(intent);`
- `sources/xfkj/fitpro/utils/NotificationUtil.java:86`
  `activity.startActivity(intent);`
- `sources/xfkj/fitpro/utils/ShareUtils.java:28`
  `ActivityUtils.startActivity(Intent.createChooser(intent, "Qrcode"));`

## BR035

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `resources/com/androidquery/WebDialog.java:103`
  `//wv.loadUrl(url);`
- `sources/cn/niuyannet/inpay/h5/BaseWebActivity.java:95`
  `AgentWeb agentWebGo = AgentWeb.with(this).setAgentWebParent(this.mLinearLayout, new LinearLayout.LayoutParams(-1, -1)).useDefaultIndicator().setWebChromeClient(this.mWebChromeClient).setMainFrameErrorView(com.just.agentweb.R.layout.agentweb_error_page, -1).setSecurityType(AgentWeb.SecurityType.STRIC...`
- `sources/com/amazon/aps/ads/util/adview/ApsAdViewImpl.java:85`
  `addJavascriptInterface(apsAdViewWebBridge, "amzn_bridge");`
- `sources/com/amazon/aps/ads/util/adview/ApsAdViewImpl.java:259`
  `super.loadUrl(url);`
- `sources/com/androidquery/WebDialog.java:80`
  `webView.loadUrl(this.url);`
- `sources/com/applovin/impl/h7.java:44`
  `((AppLovinWebViewActivity) activity).loadUrl(this.f3501a, null);`
- `sources/com/applovin/impl/h7.java:223`
  `bVarF.loadUrl(queryParameter);`
- `sources/com/applovin/impl/l8.java:23`
  `webView.loadUrl("about:blank");`
- `sources/com/applovin/impl/l8.java:129`
  `webView.loadUrl(str);`
- `sources/com/applovin/sdk/AppLovinWebViewActivity.java:68`
  `this.c.loadUrl(this.b);`
- `sources/com/applovin/sdk/AppLovinWebViewActivity.java:96`
  `webView.loadUrl(str);`
- `sources/com/applovin/sdk/AppLovinWebViewActivity.java:117`
  `AppLovinWebViewActivity.this.c.loadUrl(AppLovinWebViewActivity.this.b);`
- `sources/com/baidu/location/b/n.java:85`
  `n.this.c.loadUrl("javascript:" + bVar.b() + "('" + str + "')");`
- `sources/com/baidu/location/b/n.java:320`
  `webView.addJavascriptInterface(new d(), "BaiduLocAssistant");`
- `sources/com/bytedance/sdk/component/adexpress/fkw/fkw.java:276`
  `leVar.ouw.addJavascriptInterface(lhVar, "SDK_INJECT_GLOBAL");`
- `sources/com/bytedance/sdk/component/bly/fkw.java:49`
  `public final void addJavascriptInterface(Object obj, String str) {`
- `sources/com/bytedance/sdk/component/bly/fkw.java:50`
  `ko.vt("TTAD.PangleWebView", "addJavascriptInterface: " + str + ", " + this);`
- `sources/com/bytedance/sdk/component/bly/fkw.java:52`
  `super.addJavascriptInterface(obj, str);`
- `sources/com/bytedance/sdk/component/bly/fkw.java:55`
  `ko.fkw("TTAD.PangleWebView", "addJavascriptInterface: has destroyed or has recycler");`
- `sources/com/bytedance/sdk/component/bly/fkw.java:160`
  `super.loadUrl(str);`
- `sources/com/bytedance/sdk/component/bly/fkw.java:174`
  `super.loadUrl(str, map);`
- `sources/com/bytedance/sdk/component/utils/jg.java:22`
  `webView.loadUrl(str);`
- `sources/com/bytedance/sdk/component/utils/jg.java:51`
  `webView.loadUrl(str);`
- `sources/com/bytedance/sdk/openadsdk/ryl/ouw.java:27`
  `webView.addJavascriptInterface(yuVar, str);`
- `sources/com/bytedance/sdk/openadsdk/yu/mwh.java:157`
  `webView2.addJavascriptInterface(new ouw(iArr), "JS_LANDING_PAGE_LOG_OBJ");`
- `sources/com/bytedance/sdk/openadsdk/yu/mwh.java:159`
  `qbp.ouw("LandingPageLog", "addJavascriptInterface exception", e);`
- `sources/com/facebook/ads/redexgen/core/AbstractC1935b4.java:34`
  `webView.loadUrl(A00(0, 11, 56));`
- `sources/com/facebook/ads/redexgen/core/C2426jA.java:28`
  `webView.loadUrl(this.A00.A0L());`
- `sources/com/facebook/ads/redexgen/core/LV.java:83`
  `addJavascriptInterface(new C1931b0(this, weakReference.get(), this.A03, this.A0B, this.A0C, this.A09), A02(0, 9, 46));`
- `sources/com/google/android/gms/ads/nonagon/signalgeneration/zzau.java:492`
  `webView.addJavascriptInterface(new TaggingLibraryJsInterface(webView, this.zzh, this.zzp, this.zzq, this.zzi, this.zzJ, zzfVar, zzjVar), "gmaSdk");`
- `sources/com/google/android/gms/internal/ads/zzfto.java:34`
  `webView.loadUrl(sb.toString());`
- `sources/com/google/android/gms/internal/consent_sdk/zzda.java:31`
  `webView.loadUrl("javascript:".concat(str));`
- `sources/com/iab/omid/library/amazon/internal/h.java:151`
  `webView.loadUrl("javascript: " + str);`
- `sources/com/iab/omid/library/applovin/internal/h.java:148`
  `webView.loadUrl("javascript: " + str);`
- `sources/com/iab/omid/library/bigosg/b/e.java:74`
  `webView.loadUrl(string);`
- `sources/com/iab/omid/library/bigosg/b/e.java:79`
  `webView.loadUrl(string);`
- `sources/com/iab/omid/library/bigosg/b/e.java:120`
  `webView.loadUrl("javascript: ".concat(String.valueOf(str)));`
- `sources/com/iab/omid/library/bytedance2/internal/h.java:151`
  `webView.loadUrl("javascript: ".concat(String.valueOf(str)));`
- `sources/com/iab/omid/library/inmobi/internal/h.java:150`
  `webView.loadUrl("javascript: " + str);`
- `sources/com/iab/omid/library/ironsrc/internal/h.java:148`
  `webView.loadUrl("javascript: " + str);`
- `sources/com/iab/omid/library/mmadbridge/internal/h.java:148`
  `webView.loadUrl("javascript: " + str);`
- `sources/com/iab/omid/library/toponad/internal/h.java:148`
  `webView.loadUrl("javascript: " + str);`
- `sources/com/iab/omid/library/unity3d/internal/g.java:151`
  `webView.loadUrl("javascript: " + str);`
- `sources/com/iab/omid/library/vungle/internal/h.java:150`
  `webView.loadUrl("javascript: " + str);`
- `sources/com/inmobi/media/C3008fc.java:44`
  `webView.loadUrl(str);`
- `sources/com/inmobi/media/C3033h4.java:118`
  `super.loadUrl(url);`
- `sources/com/just/agentweb/AgentWebUtils.java:232`
  `webView.loadUrl("about:blank");`
- `sources/com/just/agentweb/AgentWebView.java:217`
  `public final void addJavascriptInterface(Object obj, String str) {`
- `sources/com/just/agentweb/AgentWebView.java:218`
  `super.addJavascriptInterface(obj, str);`
- `sources/com/just/agentweb/AgentWebView.java:222`
  `protected void addJavascriptInterfaceSupport(Object obj, String str) {`
- `sources/com/just/agentweb/BaseJsAccessEntrace.java:44`
  `this.mWebView.loadUrl(str);`
- `sources/com/just/agentweb/DefaultWebClient.java:259`
  `webView.loadUrl(returnUrl);`
- `sources/com/just/agentweb/JsCallback.java:73`
  `this.mWebViewRef.get().loadUrl(str);`
- `sources/com/just/agentweb/JsInterfaceHolderImpl.java:23`
  `this.mWebView.addJavascriptInterface(obj, str);`
- `sources/com/just/agentweb/UrlLoaderImpl.java:142`
  `this.mWebView.loadUrl(str);`
- `sources/com/just/agentweb/UrlLoaderImpl.java:144`
  `this.mWebView.loadUrl(str, map);`
- `sources/com/mbridge/msdk/activity/DomainMBCommonActivity.java:161`
  `webView.loadUrl(stringExtra);`
- `sources/com/mbridge/msdk/advanced/manager/b.java:121`
  `this.f6387a.loadUrl(this.b);`
- `sources/com/mbridge/msdk/advanced/manager/d.java:43`
  `this.f6406a.loadUrl(this.b);`
- `sources/com/mbridge/msdk/advanced/signal/NativeAdvancedExpandDialog.java:218`
  `this.e.loadUrl(this.b);`
- `sources/com/mbridge/msdk/click/o.java:86`
  `webView.loadUrl("javascript:window.navigator.vibrate([]);");`
- `sources/com/mbridge/msdk/click/o.java:95`
  `webView.loadUrl("javascript:window.navigator.vibrate([]);");`
- `sources/com/mbridge/msdk/click/o.java:225`
  `webView.loadUrl("javascript:window.navigator.vibrate([]);");`
- `sources/com/mbridge/msdk/foundation/tools/t0.java:303`
  `browserView.loadUrl(str);`
- `sources/com/mbridge/msdk/foundation/webview/a.java:245`
  `webView.loadUrl(stringExtra);`
- `sources/com/mbridge/msdk/foundation/webview/BrowserView.java:84`
  `BrowserView.this.d.loadUrl(BrowserView.this.b);`
- `sources/com/mbridge/msdk/foundation/webview/BrowserView.java:313`
  `webView.loadUrl(str);`
- `sources/com/mbridge/msdk/mbbanner/common/communication/BannerExpandDialog.java:219`
  `this.e.loadUrl(this.b);`
- `sources/com/mbridge/msdk/mbbanner/common/manager/d.java:384`
  `this.f.loadUrl(strA);`
- `sources/com/mbridge/msdk/mbsignalcommon/commonwebview/CommonWebView.java:302`
  `this.j.loadUrl(str);`
- `sources/com/mbridge/msdk/mbsignalcommon/commonwebview/CommonWebView.java:554`
  `webView.loadUrl(stringExtra);`
- `sources/com/mbridge/msdk/mbsignalcommon/mraid/a.java:105`
  `webView.loadUrl(str);`
- `sources/com/mbridge/msdk/mbsignalcommon/windvane/f.java:36`
  `aVar.b.loadUrl(str2);`
- `sources/com/mbridge/msdk/mbsignalcommon/windvane/f.java:54`
  `aVar.b.loadUrl(str3);`
- `sources/com/mbridge/msdk/mbsignalcommon/windvane/f.java:75`
  `webView.loadUrl(str3);`
- `sources/com/mbridge/msdk/mbsignalcommon/windvane/f.java:98`
  `aVar.b.loadUrl(str2);`
- `sources/com/mbridge/msdk/nativex/view/BaseMBMediaView.java:535`
  `BaseMBMediaView.this.A.loadUrl(clickURL);`
- `sources/com/mbridge/msdk/reward/adapter/b.java:2046`
  `windVaneWebView2.loadUrl(str2);`
- `sources/com/mbridge/msdk/splash/manager/g.java:158`
  `splashWebview.loadUrl(strC);`
- `sources/com/mbridge/msdk/splash/signal/SplashExpandDialog.java:219`
  `this.e.loadUrl(this.b);`

## BR040

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `resources/AndroidManifest.xml:105`
  `<action android:name="com.applovin.am.intent.action.APPHUB_SERVICE"/>`
- `resources/AndroidManifest.xml:137`
  `<uses-permission android:name="com.applovin.array.apphub.permission.BIND_APPHUB_SERVICE"/>`
- `resources/AndroidManifest.xml:612`
  `android:name="com.google.android.gms.ads.APPLICATION_ID"`
- `resources/AndroidManifest.xml:1030`
  `android:name="com.google.android.gms.ads.AD_MANAGER_APP"`
- `resources/AndroidManifest.xml:1094`
  `android:name="com.google.android.gms.ads.AdActivity"`
- `resources/AndroidManifest.xml:1099`
  `android:name="com.google.android.gms.ads.MobileAdsInitProvider"`
- `resources/AndroidManifest.xml:1104`
  `android:name="com.google.android.gms.ads.AdService"`
- `resources/AndroidManifest.xml:1108`
  `android:name="com.google.android.gms.ads.OutOfContextTestingActivity"`
- `resources/AndroidManifest.xml:1113`
  `android:name="com.google.android.gms.ads.NotificationHandlerActivity"`
- `resources/AndroidManifest.xml:1119`
  `android:name="com.google.android.gms.ads.flag.OPTIMIZE_AD_LOADING"`
- `resources/AndroidManifest.xml:1122`
  `android:name="com.google.android.gms.ads.flag.OPTIMIZE_INITIALIZATION"`
- `resources/AndroidManifest.xml:1130`
  `android:name="com.applovin.sdk.AppLovinInitProvider"`
- `resources/AndroidManifest.xml:1136`
  `android:name="com.applovin.adview.AppLovinFullscreenActivity"`
- `resources/AndroidManifest.xml:1144`
  `android:name="com.applovin.adview.AppLovinFullscreenImmersiveActivity"`
- `resources/AndroidManifest.xml:1151`
  `android:name="com.applovin.sdk.AppLovinWebViewActivity"`
- `resources/AndroidManifest.xml:1154`
  `android:theme="@style/com.applovin.mediation.MaxDebuggerActivity.Theme"`
- `resources/AndroidManifest.xml:1155`
  `android:name="com.applovin.mediation.MaxDebuggerActivity"`
- `resources/AndroidManifest.xml:1158`
  `android:theme="@style/com.applovin.mediation.MaxDebuggerActivity.Theme"`
- `resources/AndroidManifest.xml:1159`
  `android:name="com.applovin.mediation.MaxDebuggerDetailActivity"`
- `resources/AndroidManifest.xml:1162`
  `android:theme="@style/com.applovin.mediation.MaxDebuggerActivity.Theme"`
- `resources/AndroidManifest.xml:1163`
  `android:name="com.applovin.mediation.MaxDebuggerMultiAdActivity"`
- `resources/AndroidManifest.xml:1166`
  `android:theme="@style/com.applovin.mediation.MaxDebuggerActivity.Theme"`
- `resources/AndroidManifest.xml:1167`
  `android:name="com.applovin.mediation.MaxDebuggerAdUnitsListActivity"`
- `resources/AndroidManifest.xml:1170`
  `android:theme="@style/com.applovin.mediation.MaxDebuggerActivity.Theme"`
- `resources/AndroidManifest.xml:1171`
  `android:name="com.applovin.mediation.MaxDebuggerAdUnitWaterfallsListActivity"`
- `resources/AndroidManifest.xml:1174`
  `android:theme="@style/com.applovin.mediation.MaxDebuggerActivity.Theme"`
- `resources/AndroidManifest.xml:1175`
  `android:name="com.applovin.mediation.MaxDebuggerAdUnitDetailActivity"`
- `resources/AndroidManifest.xml:1178`
  `android:theme="@style/com.applovin.mediation.MaxDebuggerActivity.Theme"`
- `resources/AndroidManifest.xml:1179`
  `android:name="com.applovin.mediation.MaxDebuggerCmpNetworksListActivity"`
- `resources/AndroidManifest.xml:1182`
  `android:theme="@style/com.applovin.mediation.MaxDebuggerActivity.Theme"`
- `resources/AndroidManifest.xml:1183`
  `android:name="com.applovin.mediation.MaxDebuggerTcfConsentStatusesListActivity"`
- `resources/AndroidManifest.xml:1186`
  `android:theme="@style/com.applovin.mediation.MaxDebuggerActivity.Theme"`
- `resources/AndroidManifest.xml:1187`
  `android:name="com.applovin.mediation.MaxDebuggerTcfInfoListActivity"`
- `resources/AndroidManifest.xml:1190`
  `android:theme="@style/com.applovin.mediation.MaxDebuggerActivity.Theme"`
- `resources/AndroidManifest.xml:1191`
  `android:name="com.applovin.mediation.MaxDebuggerTcfStringActivity"`
- `resources/AndroidManifest.xml:1194`
  `android:theme="@style/com.applovin.mediation.MaxDebuggerActivity.Theme"`
- `resources/AndroidManifest.xml:1195`
  `android:name="com.applovin.mediation.MaxDebuggerTestLiveNetworkActivity"`
- `resources/AndroidManifest.xml:1198`
  `android:theme="@style/com.applovin.mediation.MaxDebuggerActivity.Theme"`
- `resources/AndroidManifest.xml:1199`
  `android:name="com.applovin.mediation.MaxDebuggerTestModeNetworkActivity"`
- `resources/AndroidManifest.xml:1202`
  `android:theme="@style/com.applovin.mediation.MaxDebuggerActivity.Theme"`
- `resources/AndroidManifest.xml:1203`
  `android:name="com.applovin.mediation.MaxDebuggerUnifiedFlowActivity"`
- `resources/AndroidManifest.xml:1206`
  `android:theme="@style/com.applovin.mediation.MaxDebuggerActivity.Theme"`
- `resources/AndroidManifest.xml:1207`
  `android:name="com.applovin.mediation.MaxDebuggerWaterfallSegmentsActivity"`
- `resources/AndroidManifest.xml:1210`
  `android:theme="@style/com.applovin.creative.CreativeDebuggerActivity.Theme"`
- `resources/AndroidManifest.xml:1211`
  `android:name="com.applovin.creative.MaxCreativeDebuggerActivity"`
- `resources/AndroidManifest.xml:1214`
  `android:theme="@style/com.applovin.creative.CreativeDebuggerActivity.Theme"`
- `resources/AndroidManifest.xml:1215`
  `android:name="com.applovin.creative.MaxCreativeDebuggerDisplayedAdActivity"`
- `resources/AndroidManifest.xml:1218`
  `android:name="com.applovin.impl.adview.activity.FullscreenAdService"`
- `resources/AndroidManifest.xml:1298`
  `android:name="com.facebook.ads.AudienceNetworkActivity"`
- `resources/AndroidManifest.xml:1302`
  `android:name="com.facebook.ads.AudienceNetworkContentProvider"`
- `resources/AndroidManifest.xml:1309`
  `android:name="com.bytedance.sdk.pangle.version"`
- `resources/AndroidManifest.xml:1312`
  `android:name="com.bytedance.sdk.openadsdk.activity.TTCeilingLandingPageActivity"`
- `resources/AndroidManifest.xml:1321`
  `android:name="com.bytedance.sdk.openadsdk.activity.TTLandingPageActivity"`
- `resources/AndroidManifest.xml:1330`
  `android:name="com.bytedance.sdk.openadsdk.activity.TTPlayableLandingPageActivity"`
- `resources/AndroidManifest.xml:1339`
  `android:name="com.bytedance.sdk.openadsdk.activity.TTVideoLandingPageLink2Activity"`
- `resources/AndroidManifest.xml:1348`
  `android:name="com.bytedance.sdk.openadsdk.activity.TTDelegateActivity"`
- `resources/AndroidManifest.xml:1356`
  `android:name="com.bytedance.sdk.openadsdk.activity.TTWebsiteActivity"`
- `resources/AndroidManifest.xml:1363`
  `<service android:name="com.bytedance.sdk.openadsdk.multipro.aidl.BinderPoolService"/>`
- `resources/AndroidManifest.xml:1366`
  `android:name="com.bytedance.sdk.openadsdk.activity.TTAppOpenAdActivity"`
- `resources/AndroidManifest.xml:1375`
  `android:name="com.bytedance.sdk.openadsdk.activity.TTAppOpenAdTransActivity"`
- `resources/AndroidManifest.xml:1384`
  `android:name="com.bytedance.sdk.openadsdk.activity.TTRewardVideoActivity"`
- `resources/AndroidManifest.xml:1393`
  `android:name="com.bytedance.sdk.openadsdk.activity.TTRewardExpressVideoActivity"`
- `resources/AndroidManifest.xml:1402`
  `android:name="com.bytedance.sdk.openadsdk.activity.TTFullScreenVideoActivity"`
- `resources/AndroidManifest.xml:1411`
  `android:name="com.bytedance.sdk.openadsdk.activity.TTFullScreenExpressVideoActivity"`
- `resources/AndroidManifest.xml:1420`
  `android:name="com.bytedance.sdk.openadsdk.activity.TTInterstitialActivity"`
- `resources/AndroidManifest.xml:1429`
  `android:name="com.bytedance.sdk.openadsdk.activity.TTInterstitialExpressActivity"`
- `resources/AndroidManifest.xml:1438`
  `android:name="com.bytedance.sdk.openadsdk.activity.TTAdActivity"`
- `resources/META-INF/com/applovin/mediation/amazon-tam-adapter/verification.properties:1`
  `#This is the verification token for the com.applovin.mediation:amazon-tam-adapter SDK.`
- `resources/META-INF/com/applovin/mediation/bytedance-adapter/verification.properties:1`
  `#This is the verification token for the com.applovin.mediation:bytedance-adapter SDK.`
- `resources/META-INF/com/applovin/mediation/google-ad-manager-adapter/verification.properties:1`
  `#This is the verification token for the com.applovin.mediation:google-ad-manager-adapter SDK.`
- `resources/META-INF/com/applovin/mediation/google-adapter/verification.properties:1`
  `#This is the verification token for the com.applovin.mediation:google-adapter SDK.`
- `resources/META-INF/com/applovin/mediation/ironsource-adapter/verification.properties:1`
  `#This is the verification token for the com.applovin.mediation:ironsource-adapter SDK.`
- `resources/META-INF/com/applovin/mediation/mintegral-adapter/verification.properties:1`
  `#This is the verification token for the com.applovin.mediation:mintegral-adapter SDK.`
- `resources/res/layout/creative_debugger_displayed_ad_detail_activity.xml:27`
  `style="@style/com.applovin.creative.debugger.ui.DisplayedAdActivity.ReportAdButton"/>`
- `resources/res/layout/max_native_ad_banner_icon_and_text_layout.xml:33`
  `style="@style/com.applovin.mediation.nativeAds.MaxNativeAdView.SmallScrollingTitleTextView"/>`
- `resources/res/layout/max_native_ad_banner_icon_and_text_layout.xml:45`
  `<TextView style="@style/com.applovin.mediation.nativeAds.MaxNativeAdView.ExtraSmallAdBadgeTextView"/>`
- `resources/res/layout/max_native_ad_banner_icon_and_text_layout.xml:48`
  `style="@style/com.applovin.mediation.nativeAds.MaxNativeAdView.ExtraSmallScrollingBodyTextView"/>`
- `resources/res/layout/max_native_ad_banner_icon_and_text_layout.xml:52`
  `style="@style/com.applovin.mediation.nativeAds.MaxNativeAdView.ExtraSmallScrollingBodyTextView"/>`
- `resources/res/layout/max_native_ad_banner_view.xml:21`
  `style="@style/com.applovin.mediation.nativeAds.MaxNativeAdView.CTAButton"/>`
- `resources/res/layout/max_native_ad_leader_view.xml:40`
  `style="@style/com.applovin.mediation.nativeAds.MaxNativeAdView.LargeScrollingTitleTextView"/>`

## BR041

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `resources/AndroidManifest.xml:1086`
  `android:name="com.google.firebase.components:com.google.firebase.analytics.connector.internal.AnalyticsConnectorRegistrar"`
- `sources/androidx/appcompat/app/TwilightManager.java:8`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/content/ContextCompat.java:77`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/privacysandbox/ads/adservices/measurement/WebTriggerRegistrationRequest.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/test/internal/runner/TestSize.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/cn/niuyannet/inpay/pay/GoogleBillHelper.java:18`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/afollestad/materialdialogs/bottomsheets/BottomSheetsKt.java:13`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/afollestad/materialdialogs/bottomsheets/GridIconDialogAdapter.java:14`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/afollestad/materialdialogs/internal/list/DialogAdapter.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/afollestad/materialdialogs/internal/list/MultiChoiceDialogAdapter.java:16`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/afollestad/materialdialogs/internal/list/PlainListDialogAdapter.java:13`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/afollestad/materialdialogs/internal/list/SingleChoiceDialogAdapter.java:17`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/afollestad/materialdialogs/list/DialogListExtKt.java:15`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/afollestad/materialdialogs/list/DialogMultiChoiceExtKt.java:11`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/afollestad/materialdialogs/list/DialogSingleChoiceExtKt.java:11`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/afollestad/materialdialogs/list/ListCallbacksKt.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/amazon/device/ads/DtbDeviceRegistration.java:14`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/amazon/device/ads/DtbGeoLocation.java:10`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/android/billingclient/api/Purchase.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/android/billingclient/api/PurchaseHistoryRecord.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/androidquery/callback/LocationAjaxCallback.java:10`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/applovin/impl/v4.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/applovin/impl/sdk/EventServiceImpl.java:20`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/applovin/mediation/MaxAdFormat.java:8`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/applovin/mediation/adapters/GoogleAdManagerMediationAdapter.java:63`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/applovin/mediation/adapters/GoogleMediationAdapter.java:69`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/applovin/shadow/okhttp3/internal/Util.java:23`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/applovin/shadow/okhttp3/internal/http2/Hpack.java:10`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/baidu/location/b/d.java:31`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/baidu/location/c/f.java:25`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/bytedance/sdk/component/adexpress/dynamic/fkw/le.java:9`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/bytedance/sdk/openadsdk/activity/TTAppOpenAdActivity.java:32`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/bytedance/sdk/openadsdk/component/yu.java:28`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/bytedance/sdk/openadsdk/core/vt.java:15`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/bytedance/sdk/openadsdk/core/bly/ouw/ouw.java:16`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/bytedance/sdk/openadsdk/core/cf/yu.java:8`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/bytedance/sdk/openadsdk/core/model/le.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/bytedance/sdk/openadsdk/core/model/vpp.java:13`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/caverock/androidsvg/SVGParser.java:12`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/facebook/ads/redexgen/core/AbstractC09930f.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/facebook/ads/redexgen/core/AbstractC10111q.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/facebook/ads/redexgen/core/AnonymousClass01.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/facebook/ads/redexgen/core/AnonymousClass04.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/facebook/ads/redexgen/core/AnonymousClass08.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/facebook/ads/redexgen/core/AnonymousClass15.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/facebook/ads/redexgen/core/C0d.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/ads/internal/client/zzam.java:8`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/ads/zzbwo.java:10`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/ads/zzflk.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/consent_sdk/zzam.java:91`
  `Class<?> cls2 = Class.forName("com.google.firebase.analytics.FirebaseAnalytics$ConsentStatus");`
- `sources/com/google/android/gms/internal/consent_sdk/zzam.java:92`
  `Class<?> cls3 = Class.forName("com.google.firebase.analytics.FirebaseAnalytics$ConsentType");`
- `sources/com/google/android/gms/measurement/internal/zzfi.java:9`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/measurement/internal/zzgo.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/measurement/internal/zzgp.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/measurement/internal/zzhx.java:18`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/measurement/internal/zzim.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/measurement/internal/zzlb.java:21`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/measurement/internal/zzs.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/firebase/analytics/FirebaseAnalytics.java:1`
  `package com.google.firebase.analytics;`
- `sources/com/google/firebase/analytics/zza.java:1`
  `package com.google.firebase.analytics;`
- `sources/com/google/firebase/analytics/zzb.java:1`
  `package com.google.firebase.analytics;`
- `sources/com/google/firebase/analytics/zzc.java:1`
  `package com.google.firebase.analytics;`
- `sources/com/google/firebase/analytics/zzd.java:1`
  `package com.google.firebase.analytics;`
- `sources/com/google/firebase/analytics/connector/AnalyticsConnector.java:1`
  `package com.google.firebase.analytics.connector;`
- `sources/com/google/firebase/analytics/connector/AnalyticsConnectorImpl.java:1`
  `package com.google.firebase.analytics.connector;`
- `sources/com/google/firebase/analytics/connector/AnalyticsConnectorImpl.java:11`
  `import com.google.firebase.analytics.connector.AnalyticsConnector;`
- `sources/com/google/firebase/analytics/connector/AnalyticsConnectorImpl.java:12`
  `import com.google.firebase.analytics.connector.internal.zzc;`
- `sources/com/google/firebase/analytics/connector/AnalyticsConnectorImpl.java:13`
  `import com.google.firebase.analytics.connector.internal.zze;`
- `sources/com/google/firebase/analytics/connector/AnalyticsConnectorImpl.java:14`
  `import com.google.firebase.analytics.connector.internal.zzg;`
- `sources/com/google/firebase/analytics/connector/AnalyticsConnectorImpl.java:55`
  `@Override // com.google.firebase.analytics.connector.AnalyticsConnector`
- `sources/com/google/firebase/analytics/connector/AnalyticsConnectorImpl.java:62`
  `@Override // com.google.firebase.analytics.connector.AnalyticsConnector`
- `sources/com/google/firebase/analytics/connector/AnalyticsConnectorImpl.java:72`
  `@Override // com.google.firebase.analytics.connector.AnalyticsConnector`
- `sources/com/google/firebase/analytics/connector/AnalyticsConnectorImpl.java:77`
  `@Override // com.google.firebase.analytics.connector.AnalyticsConnector`
- `sources/com/google/firebase/analytics/connector/AnalyticsConnectorImpl.java:82`
  `@Override // com.google.firebase.analytics.connector.AnalyticsConnector`
- `sources/com/google/firebase/analytics/connector/AnalyticsConnectorImpl.java:93`
  `@Override // com.google.firebase.analytics.connector.AnalyticsConnector`
- `sources/com/google/firebase/analytics/connector/AnalyticsConnectorImpl.java:100`
  `com.google.firebase.analytics.connector.internal.zza zzeVar = AppMeasurement.FIAM_ORIGIN.equals(str) ? new zze(appMeasurementSdk, analyticsConnectorListener) : "clx".equals(str) ? new zzg(appMeasurementSdk, analyticsConnectorListener) : null;`
- `sources/com/google/firebase/analytics/connector/AnalyticsConnectorImpl.java:105`
  `return new AnalyticsConnector.AnalyticsConnectorHandle() { // from class: com.google.firebase.analytics.connector.AnalyticsConnectorImpl.1`
- `sources/com/google/firebase/analytics/connector/AnalyticsConnectorImpl.java:106`
  `@Override // com.google.firebase.analytics.connector.AnalyticsConnector.AnalyticsConnectorHandle`
- `sources/com/google/firebase/analytics/connector/AnalyticsConnectorImpl.java:111`
  `((com.google.firebase.analytics.connector.internal.zza) AnalyticsConnectorImpl.this.zzb.get(str)).zzb(set);`
- `sources/com/google/firebase/analytics/connector/AnalyticsConnectorImpl.java:114`
  `@Override // com.google.firebase.analytics.connector.AnalyticsConnector.AnalyticsConnectorHandle`

## BR042

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `resources/AndroidManifest.xml:115`
  `<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>`
- `resources/AndroidManifest.xml:134`
  `<uses-permission android:name="android.permission.ACCESS_ADSERVICES_AD_ID"/>`
- `resources/res/layout/bigo_ad_form_question.xml:16`
  `android:id="@+id/bigo_ad_id_form_question"`
- `resources/res/layout/bigo_ad_form_question_dark.xml:16`
  `android:id="@+id/bigo_ad_id_form_question"`
- `resources/res/values/public.xml:11991`
  `<public type="string" name="bigo_ad_feedback_copy_ad_id" id="0x7f1300ca" />`
- `resources/res/values/strings.xml:205`
  `<string name="bigo_ad_feedback_copy_ad_id">ERID: %s</string>`
- `resources/res/values-ru-rRU/strings.xml:4`
  `<string name="bigo_ad_feedback_copy_ad_id">ERID: %s</string>`
- `sources/cn/xiaofengkj/fitpro/R.java:12048`
  `public static final int bigo_ad_feedback_copy_ad_id = 0x7f1300ca;`
- `sources/com/amazon/device/ads/DtbGooglePlayServices.java:32`
  `return DtbCommonUtils.isClassAvailable("com.google.android.gms.ads.identifier.AdvertisingIdClient");`
- `sources/com/amazon/device/ads/DtbGooglePlayServicesAdapter.java:7`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/amazon/device/ads/DtbGooglePlayServicesAdapter.java:22`
  `AdvertisingIdClient.Info advertisingIdInfo;`
- `sources/com/amazon/device/ads/DtbGooglePlayServicesAdapter.java:24`
  `advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(AdRegistration.getContext());`
- `sources/com/amazon/device/ads/DtbGooglePlayServicesAdapter.java:35`
  `APSAnalytics.logEvent(APSEventSeverity.FATAL, APSEventType.EXCEPTION, "Illegal Argument passed to getAdvertisingIdInfo", e4);`
- `sources/com/apm/insight/entity/Header.java:29`
  `private static final String[] f3253a = {"version_code", "manifest_version_code", fl.SESSION_HISTORY_KEY_AD_ID, "update_version_code"};`
- `sources/com/apm/insight/k/b.java:373`
  `jSONObjectOptJSONObject.put(fl.SESSION_HISTORY_KEY_AD_ID, 2010);`
- `sources/com/applovin/impl/b3.java:428`
  `m4 m4Var = new m4("com.google.android.gms.permission.AD_ID", "Please add\n<uses-permission android:name=\"com.google.android.gms.permission.AD_ID\" />\nto your AndroidManifest.xml", com.applovin.impl.sdk.k.o());`
- `sources/com/applovin/impl/e2.java:28`
  `CollectionUtils.putStringIfValid("ad_id", String.valueOf(appLovinAdImpl.getAdIdNumber()), map);`
- `sources/com/applovin/impl/e2.java:77`
  `CollectionUtils.putStringIfValid("ad_id", String.valueOf(appLovinNativeAdImpl.getAdIdNumber()), map);`
- `sources/com/applovin/impl/o4.java:10`
  `return o0.a("android.permission.ACCESS_ADSERVICES_AD_ID", context);`
- `sources/com/applovin/impl/v.java:8`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/applovin/impl/v.java:177`
  `AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(context);`
- `sources/com/applovin/impl/v.java:213`
  `return k7.a("com.google.android.gms.ads.identifier.AdvertisingIdClient");`
- `sources/com/applovin/impl/sdk/ad/AppLovinAdImpl.java:48`
  `return getLongFromAdObject("ad_id", -1L);`
- `sources/com/bykv/vk/openvk/preload/geckox/statistic/c.java:34`
  `jSONObject.put(fl.SESSION_HISTORY_KEY_AD_ID, bVar.k());`
- `sources/com/bytedance/sdk/openadsdk/ApmHelper.java:179`
  `jSONObject2.put(fl.SESSION_HISTORY_KEY_AD_ID, "10000001");`
- `sources/com/bytedance/sdk/openadsdk/ApmHelper.java:229`
  `vppVarVt.zu = jSONObjectFak.optLong("ad_id", 0L);`
- `sources/com/bytedance/sdk/openadsdk/ApmHelper.java:234`
  `map.put(fl.SESSION_HISTORY_KEY_AD_ID, String.valueOf(vppVarVt.zu));`
- `sources/com/bytedance/sdk/openadsdk/TTAdConstant.java:8`
  `public static final int AD_ID_IS_NULL_CODE = 402;`
- `sources/com/bytedance/sdk/openadsdk/core/bs.java:295`
  `jSONObject.put(fl.SESSION_HISTORY_KEY_AD_ID, "1371");`
- `sources/com/bytedance/sdk/openadsdk/core/bs.java:1276`
  `jSONObject3.put("ad_id", vppVar.pv);`
- `sources/com/bytedance/sdk/openadsdk/core/jqy.java:797`
  `jSONObject2.getJSONObject(g.B).put(fl.SESSION_HISTORY_KEY_AD_ID, "4562");`
- `sources/com/bytedance/sdk/openadsdk/core/jqy.java:1157`
  `jSONObject2.put("ad_id", adSlot.getAdId());`
- `sources/com/bytedance/sdk/openadsdk/core/le.java:255`
  `sQLiteDatabase.execSQL("ALTER TABLE trackurl ADD COLUMN ad_id TEXT ");`
- `sources/com/bytedance/sdk/openadsdk/core/vt.java:146`
  `vppVar2.pv = jSONObject.optString("ad_id");`
- `sources/com/bytedance/sdk/openadsdk/core/tlj/lh.java:126`
  `map.put("ad_id", Long.valueOf(jOptLong));`
- `sources/com/bytedance/sdk/openadsdk/ouw/ouw.java:82`
  `if (extraInfo.containsKey("ad_id") && extraInfo.get("ad_id") != null) {`
- `sources/com/bytedance/sdk/openadsdk/ouw/ouw.java:83`
  `builder.setAdId(extraInfo.get("ad_id").toString());`
- `sources/com/bytedance/sdk/openadsdk/tc/vt.java:6`
  `return "CREATE TABLE IF NOT EXISTS trackurl (_id INTEGER PRIMARY KEY AUTOINCREMENT,id TEXT UNIQUE,url TEXT ,replaceholder INTEGER default 0, retry INTEGER default 0, ad_id TEXT , url_type INTEGER default 0, error_code TEXT ,error_msg TEXT )";`
- `sources/com/bytedance/sdk/openadsdk/utils/DeviceUtils.java:19`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/bytedance/sdk/openadsdk/utils/DeviceUtils.java:518`
  `AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(com.bytedance.sdk.openadsdk.core.zih.ouw());`
- `sources/com/bytedance/sdk/openadsdk/utils/DeviceUtils.java:651`
  `static /* synthetic */ void ouw(AdvertisingIdClient.Info info, boolean z) {`
- `sources/com/bytedance/sdk/openadsdk/utils/fvf.java:56`
  `return builderBuildUpon.appendQueryParameter(ouw, str2).appendQueryParameter(fl.SESSION_HISTORY_KEY_AD_ID, "5001121").toString();`
- `sources/com/bytedance/sdk/openadsdk/utils/uoy.java:675`
  `return Uri.parse(str).buildUpon().appendQueryParameter(fl.SESSION_HISTORY_KEY_AD_ID, "1371").appendQueryParameter("device_platform", "android").appendQueryParameter("version_code", pno()).toString();`
- `sources/com/bytedance/sdk/openadsdk/yu/mwh.java:598`
  `jSONObject.putOpt("ad_id", mwhVar.th.pv);`
- `sources/com/bytedance/sdk/openadsdk/yu/ouw/ouw.java:188`
  `jSONObject.put(fl.SESSION_HISTORY_KEY_AD_ID, "1371");`
- `sources/com/bytedance/sdk/openadsdk/yu/ouw/tlj.java:32`
  `jSONObject.put("ad_id", this.ouw.le);`
- `sources/com/example/otalib/boads/TransOpcodeType.java:7`
  `public static final byte Read_ID = 1;`
- `sources/com/facebook/ads/internal/bridge/gms/AdvertisingId.java:4`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/facebook/ads/internal/bridge/gms/AdvertisingId.java:24`
  `public static AdvertisingId getAdvertisingIdInfoDirectly(Context context) {`
- `sources/com/facebook/ads/redexgen/core/C1919ao.java:62`
  `AdvertisingId advertisingIdInfoDirectly = AdvertisingId.getAdvertisingIdInfoDirectly(this.A00);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:27`
  `public class AdvertisingIdClient {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:29`
  `private static volatile AdvertisingIdClient zzh;`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:114`
  `AdvertisingIdClient advertisingIdClient = new AdvertisingIdClient(context, -1L, false, false);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:116`
  `advertisingIdClient.zzc(false);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:118`
  `synchronized (advertisingIdClient) {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:119`
  `advertisingIdClient.zzd();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:120`
  `Preconditions.checkNotNull(advertisingIdClient.zza);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:121`
  `Preconditions.checkNotNull(advertisingIdClient.zzb);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:123`
  `zZzd = advertisingIdClient.zzb.zzd();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:125`
  `Log.i("AdvertisingIdClient", "GMS remote exception ", e);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:129`
  `advertisingIdClient.zzb();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:132`
  `advertisingIdClient.zza();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:149`
  `Log.i("AdvertisingIdClient", "GMS remote exception ", e);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:250`
  `Log.d("AdvertisingIdClient", "AdvertisingIdClient is not bounded. Starting to bind it...");`
- `sources/com/google/android/gms/ads/identifier/zza.java:11`
  `zza(AdvertisingIdClient advertisingIdClient, Map map) {`
- `sources/com/google/android/gms/ads/identifier/zzb.java:14`
  `public zzb(AdvertisingIdClient advertisingIdClient, long j) {`
- `sources/com/google/android/gms/ads/identifier/zzb.java:16`
  `this.zzb = new WeakReference(advertisingIdClient);`
- `sources/com/google/android/gms/ads/identifier/zzb.java:23`
  `AdvertisingIdClient advertisingIdClient = (AdvertisingIdClient) this.zzb.get();`
- `sources/com/google/android/gms/ads/identifier/zzb.java:24`
  `if (advertisingIdClient != null) {`
- `sources/com/google/android/gms/ads/identifier/zzb.java:25`
  `advertisingIdClient.zza();`
- `sources/com/google/android/gms/ads/identifier/zzd.java:44`
  `Log.i("AdvertisingIdClient", "getting error as ".concat(String.valueOf(exc.getMessage())));`
- `sources/com/google/android/gms/ads/identifier/zzd.java:53`
  `Log.i("AdvertisingIdClient", "shouldSendLog " + atomicLong.get());`
- `sources/com/google/android/gms/ads/internal/util/zzc.java:4`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/ads/internal/util/zzc.java:22`
  `isAdIdFakeForDebugLogging = AdvertisingIdClient.getIsAdIdFakeForDebugLogging(this.zza);`
- `sources/com/google/android/gms/ads/internal/util/zzj.java:367`
  `this.zzk = this.zzf.getBoolean("gad_idless", this.zzk);`
- `sources/com/google/android/gms/ads/internal/util/zzj.java:748`
  `editor.putBoolean("gad_idless", z);`
- `sources/com/google/android/gms/internal/ads/zzbak.java:8`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/internal/ads/zzbak.java:43`
  `private volatile AdvertisingIdClient zzh = null;`
- `sources/com/google/android/gms/internal/ads/zzbhe.java:1334`
  `zzgL = new zzbgq(1, "gads:signals:ad_id_info:enabled", true, true);`
- `sources/com/google/android/gms/internal/ads/zzcdl.java:4`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`

## BR043

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/cn/bertsir/zbar/CameraScanAnalysis.java:11`
  `import cn.bertsir.zbar.Qr.ScanResult;`
- `sources/cn/bertsir/zbar/CameraScanAnalysis.java:79`
  `ScanResult scanResult = new ScanResult();`
- `sources/cn/bertsir/zbar/CameraScanAnalysis.java:80`
  `scanResult.setContent(str);`
- `sources/cn/bertsir/zbar/CameraScanAnalysis.java:81`
  `scanResult.setType(type == 64 ? 1 : 2);`
- `sources/cn/bertsir/zbar/CameraScanAnalysis.java:83`
  `messageObtainMessage.obj = scanResult;`
- `sources/cn/bertsir/zbar/CameraScanAnalysis.java:139`
  `CameraScanAnalysis.this.mCallback.onScanResult((ScanResult) message.obj);`
- `sources/cn/bertsir/zbar/CameraScanAnalysis.java:208`
  `ScanResult scanResult = new ScanResult();`
- `sources/cn/bertsir/zbar/CameraScanAnalysis.java:209`
  `scanResult.setContent(string);`
- `sources/cn/bertsir/zbar/CameraScanAnalysis.java:210`
  `scanResult.setType(barcodeFormat == BarcodeFormat.QR_CODE ? 1 : 2);`
- `sources/cn/bertsir/zbar/CameraScanAnalysis.java:212`
  `messageObtainMessage.obj = scanResult;`
- `sources/cn/bertsir/zbar/QRActivity.java:26`
  `import cn.bertsir.zbar.Qr.ScanResult;`
- `sources/cn/bertsir/zbar/QRActivity.java:62`
  `public void onScanResult(ScanResult scanResult) {`
- `sources/cn/bertsir/zbar/QRActivity.java:72`
  `QrManager.getInstance().getResultCallback().onScanSuccess(scanResult);`
- `sources/cn/bertsir/zbar/QRActivity.java:291`
  `ScanResult scanResult = new ScanResult();`
- `sources/cn/bertsir/zbar/QRActivity.java:294`
  `scanResult.setContent(strDecodeQRcode);`
- `sources/cn/bertsir/zbar/QRActivity.java:295`
  `scanResult.setType(1);`
- `sources/cn/bertsir/zbar/QRActivity.java:296`
  `QrManager.getInstance().getResultCallback().onScanSuccess(scanResult);`
- `sources/cn/bertsir/zbar/QRActivity.java:304`
  `scanResult.setContent(strDecodeQRcodeByZxing);`
- `sources/cn/bertsir/zbar/QRActivity.java:305`
  `scanResult.setType(1);`
- `sources/cn/bertsir/zbar/QRActivity.java:306`
  `QrManager.getInstance().getResultCallback().onScanSuccess(scanResult);`
- `sources/cn/bertsir/zbar/QRActivity.java:315`
  `scanResult.setContent(strDecodeBarcode);`
- `sources/cn/bertsir/zbar/QRActivity.java:316`
  `scanResult.setType(2);`
- `sources/cn/bertsir/zbar/QRActivity.java:317`
  `QrManager.getInstance().getResultCallback().onScanSuccess(scanResult);`
- `sources/cn/bertsir/zbar/QrManager.java:6`
  `import cn.bertsir.zbar.Qr.ScanResult;`
- `sources/cn/bertsir/zbar/QrManager.java:16`
  `public OnScanResultCallback resultCallback;`
- `sources/cn/bertsir/zbar/QrManager.java:18`
  `public interface OnScanResultCallback {`
- `sources/cn/bertsir/zbar/QrManager.java:19`
  `void onScanSuccess(ScanResult scanResult);`
- `sources/cn/bertsir/zbar/QrManager.java:22`
  `public OnScanResultCallback getResultCallback() {`
- `sources/cn/bertsir/zbar/QrManager.java:38`
  `public void startScan(final Activity activity, OnScanResultCallback onScanResultCallback) {`
- `sources/cn/bertsir/zbar/QrManager.java:60`
  `this.resultCallback = onScanResultCallback;`
- `sources/cn/bertsir/zbar/ScanCallback.java:3`
  `import cn.bertsir.zbar.Qr.ScanResult;`
- `sources/cn/bertsir/zbar/ScanCallback.java:7`
  `void onScanResult(ScanResult scanResult);`
- `sources/cn/bertsir/zbar/Qr/ScanResult.java:4`
  `public class ScanResult {`
- `sources/com/baidu/location/b/d.java:11`
  `import android.net.wifi.ScanResult;`
- `sources/com/baidu/location/b/d.java:259`
  `public List<ScanResult> f3939a;`
- `sources/com/baidu/location/b/d.java:265`
  `public e(List<ScanResult> list) {`
- `sources/com/baidu/location/b/d.java:290`
  `java.util.List<android.net.wifi.ScanResult> r0 = r7.f3939a`
- `sources/com/baidu/location/b/d.java:301`
  `java.util.List<android.net.wifi.ScanResult> r4 = r7.f3939a`
- `sources/com/baidu/location/b/d.java:304`
  `java.util.List<android.net.wifi.ScanResult> r4 = r7.f3939a`
- `sources/com/baidu/location/b/d.java:308`
  `java.util.List<android.net.wifi.ScanResult> r4 = r7.f3939a`
- `sources/com/baidu/location/b/d.java:310`
  `android.net.wifi.ScanResult r4 = (android.net.wifi.ScanResult) r4`
- `sources/com/baidu/location/b/d.java:312`
  `java.util.List<android.net.wifi.ScanResult> r6 = r7.f3939a`
- `sources/com/baidu/location/b/d.java:314`
  `android.net.wifi.ScanResult r6 = (android.net.wifi.ScanResult) r6`
- `sources/com/baidu/location/b/d.java:317`
  `java.util.List<android.net.wifi.ScanResult> r3 = r7.f3939a`
- `sources/com/baidu/location/b/d.java:319`
  `android.net.wifi.ScanResult r3 = (android.net.wifi.ScanResult) r3`
- `sources/com/baidu/location/b/d.java:320`
  `java.util.List<android.net.wifi.ScanResult> r4 = r7.f3939a`
- `sources/com/baidu/location/b/d.java:323`
  `java.util.List<android.net.wifi.ScanResult> r4 = r7.f3939a`
- `sources/com/baidu/location/b/d.java:340`
  `List<ScanResult> list = this.f3939a;`
- `sources/com/baidu/location/b/d.java:943`
  `this.g.startScan();`
- `sources/com/baidu/location/c/k.java:3`
  `import android.net.wifi.ScanResult;`
- `sources/com/baidu/location/c/k.java:19`
  `public List<ScanResult> f4006a;`
- `sources/com/baidu/location/c/k.java:25`
  `public k(List<ScanResult> list, long j) {`
- `sources/com/baidu/location/c/k.java:49`
  `List<ScanResult> list = this.f4006a;`
- `sources/com/baidu/location/c/k.java:70`
  `java.util.List<android.net.wifi.ScanResult> r0 = r7.f4006a`
- `sources/com/baidu/location/c/k.java:81`
  `java.util.List<android.net.wifi.ScanResult> r4 = r7.f4006a`
- `sources/com/baidu/location/c/k.java:84`
  `java.util.List<android.net.wifi.ScanResult> r4 = r7.f4006a`
- `sources/com/baidu/location/c/k.java:88`
  `java.util.List<android.net.wifi.ScanResult> r4 = r7.f4006a`
- `sources/com/baidu/location/c/k.java:90`
  `android.net.wifi.ScanResult r4 = (android.net.wifi.ScanResult) r4`
- `sources/com/baidu/location/c/k.java:92`
  `java.util.List<android.net.wifi.ScanResult> r6 = r7.f4006a`
- `sources/com/baidu/location/c/k.java:94`
  `android.net.wifi.ScanResult r6 = (android.net.wifi.ScanResult) r6`
- `sources/com/baidu/location/c/k.java:97`
  `java.util.List<android.net.wifi.ScanResult> r3 = r7.f4006a`
- `sources/com/baidu/location/c/k.java:99`
  `android.net.wifi.ScanResult r3 = (android.net.wifi.ScanResult) r3`
- `sources/com/baidu/location/c/k.java:100`
  `java.util.List<android.net.wifi.ScanResult> r4 = r7.f4006a`
- `sources/com/baidu/location/c/k.java:103`
  `java.util.List<android.net.wifi.ScanResult> r4 = r7.f4006a`
- `sources/com/baidu/location/c/k.java:120`
  `List<ScanResult> list = this.f4006a;`
- `sources/com/baidu/location/c/k.java:387`
  `List<ScanResult> list;`
- `sources/com/baidu/location/c/k.java:421`
  `List<ScanResult> list = this.f4006a;`
- `sources/com/baidu/location/c/k.java:476`
  `List<ScanResult> list = this.f4006a;`
- `sources/com/baidu/location/c/k.java:522`
  `List<ScanResult> list = this.f4006a;`
- `sources/com/baidu/location/c/k.java:564`
  `List<ScanResult> list = this.f4006a;`
- `sources/com/baidu/location/c/l.java:10`
  `import android.net.wifi.ScanResult;`
- `sources/com/baidu/location/c/l.java:101`
  `List<ScanResult> list = kVar.f4006a;`
- `sources/com/baidu/location/c/l.java:102`
  `List<ScanResult> list2 = kVar2.f4006a;`
- `sources/com/baidu/location/c/l.java:160`
  `return (wifiManager == null || com.baidu.location.e.k.f == 4) ? kVar : new k(wifiManager.getScanResults(), j);`
- `sources/com/baidu/location/c/l.java:253`
  `this.c.startScan();`
- `sources/com/beken/beken_ota/BLEScanActivity.java:7`
  `import android.bluetooth.le.BluetoothLeScanner;`
- `sources/com/beken/beken_ota/BLEScanActivity.java:10`
  `import android.bluetooth.le.ScanResult;`
- `sources/com/beken/beken_ota/BLEScanActivity.java:37`
  `private BluetoothLeScanner mBLEScanner;`
- `sources/com/beken/beken_ota/BLEScanActivity.java:117`
  `public void onScanResult(int i, ScanResult scanResult) {`
- `sources/com/beken/beken_ota/BLEScanActivity.java:118`
  `final BluetoothDevice device = scanResult.getDevice();`

## BR044

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/androidx/core/content/ContextCompat.java:43`
  `import android.net.wifi.WifiManager;`
- `sources/androidx/core/content/ContextCompat.java:323`
  `map.put(WifiManager.class, z8.b);`
- `sources/com/apm/insight/l/g.java:39`
  `hashSet.add("WifiManager");`
- `sources/com/baidu/location/b/d.java:14`
  `import android.net.wifi.WifiManager;`
- `sources/com/baidu/location/b/d.java:56`
  `private WifiManager g;`
- `sources/com/baidu/location/b/d.java:544`
  `this.g = (WifiManager) this.d.getApplicationContext().getSystemService(z8.b);`
- `sources/com/baidu/location/b/d.java:751`
  `public static boolean a(WifiManager wifiManager) {`
- `sources/com/baidu/location/b/d.java:753`
  `if (!wifiManager.isWifiEnabled()) {`
- `sources/com/baidu/location/b/d.java:754`
  `if (!wifiManager.isScanAlwaysAvailable()) {`
- `sources/com/baidu/location/b/d.java:764`
  `public static String b(WifiManager wifiManager) {`
- `sources/com/baidu/location/b/d.java:765`
  `if (wifiManager == null) {`
- `sources/com/baidu/location/b/d.java:769`
  `WifiInfo connectionInfo = wifiManager.getConnectionInfo();`
- `sources/com/baidu/location/b/d.java:835`
  `android.net.wifi.WifiManager r3 = r8.g`
- `sources/com/baidu/location/b/d.java:850`
  `android.net.wifi.WifiManager r5 = r8.g`
- `sources/com/baidu/location/b/d.java:910`
  `WifiManager wifiManager = this.g;`
- `sources/com/baidu/location/b/d.java:911`
  `if (wifiManager != null) {`
- `sources/com/baidu/location/b/d.java:912`
  `return wifiManager.getConfiguredNetworks();`
- `sources/com/baidu/location/c/l.java:12`
  `import android.net.wifi.WifiManager;`
- `sources/com/baidu/location/c/l.java:27`
  `private WifiManager c = null;`
- `sources/com/baidu/location/c/l.java:142`
  `WifiManager wifiManager = this.c;`
- `sources/com/baidu/location/c/l.java:143`
  `if (wifiManager == null) {`
- `sources/com/baidu/location/c/l.java:147`
  `k kVarA = a(wifiManager, System.currentTimeMillis());`
- `sources/com/baidu/location/c/l.java:158`
  `public k a(WifiManager wifiManager, long j) {`
- `sources/com/baidu/location/c/l.java:160`
  `return (wifiManager == null || com.baidu.location.e.k.f == 4) ? kVar : new k(wifiManager.getScanResults(), j);`
- `sources/com/baidu/location/c/l.java:172`
  `this.c = (WifiManager) com.baidu.location.f.getServiceContext().getApplicationContext().getSystemService(z8.b);`
- `sources/com/baidu/location/c/l.java:229`
  `WifiManager wifiManager = this.c;`
- `sources/com/baidu/location/c/l.java:230`
  `if (wifiManager == null) {`
- `sources/com/baidu/location/c/l.java:234`
  `if (!wifiManager.isWifiEnabled()) {`
- `sources/com/baidu/location/c/l.java:343`
  `WifiManager wifiManager = this.c;`
- `sources/com/baidu/location/c/l.java:344`
  `if (wifiManager == null || (dhcpInfo = wifiManager.getDhcpInfo()) == null) {`
- `sources/com/baidu/location/c/l.java:361`
  `WifiManager wifiManager = this.c;`
- `sources/com/baidu/location/c/l.java:362`
  `if (wifiManager != null) {`
- `sources/com/baidu/location/c/l.java:364`
  `return a(wifiManager, this.f);`
- `sources/com/baidu/location/c/l.java:368`
  `return a((WifiManager) null, 0L);`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:7`
  `import android.net.wifi.WifiManager;`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:72`
  `WifiManager wifiManager = (WifiManager) Utils.getApp().getSystemService(z8.b);`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:73`
  `if (wifiManager == null) {`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:76`
  `return wifiManager.isWifiEnabled();`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:80`
  `WifiManager wifiManager = (WifiManager) Utils.getApp().getSystemService(z8.b);`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:81`
  `if (wifiManager == null || z == wifiManager.isWifiEnabled()) {`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:84`
  `wifiManager.setWifiEnabled(z);`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:121`
  `WifiManager wifiManager = (WifiManager) Utils.getApp().getApplicationContext().getSystemService(z8.b);`
- `sources/com/blankj/utilcode/util/DeviceUtils.java:122`
  `if (wifiManager == null || (connectionInfo = wifiManager.getConnectionInfo()) == null) {`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:11`
  `import android.net.wifi.WifiManager;`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:180`
  `WifiManager wifiManager = (WifiManager) Utils.getApp().getSystemService(z8.b);`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:181`
  `if (wifiManager == null) {`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:184`
  `return wifiManager.isWifiEnabled();`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:188`
  `WifiManager wifiManager = (WifiManager) Utils.getApp().getSystemService(z8.b);`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:189`
  `if (wifiManager == null || z == wifiManager.isWifiEnabled()) {`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:192`
  `wifiManager.setWifiEnabled(z);`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:374`
  `WifiManager wifiManager = (WifiManager) Utils.getApp().getSystemService(z8.b);`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:375`
  `return wifiManager == null ? "" : Formatter.formatIpAddress(wifiManager.getDhcpInfo().ipAddress);`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:379`
  `WifiManager wifiManager = (WifiManager) Utils.getApp().getSystemService(z8.b);`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:380`
  `return wifiManager == null ? "" : Formatter.formatIpAddress(wifiManager.getDhcpInfo().gateway);`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:384`
  `WifiManager wifiManager = (WifiManager) Utils.getApp().getSystemService(z8.b);`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:385`
  `return wifiManager == null ? "" : Formatter.formatIpAddress(wifiManager.getDhcpInfo().netmask);`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:389`
  `WifiManager wifiManager = (WifiManager) Utils.getApp().getSystemService(z8.b);`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:390`
  `return wifiManager == null ? "" : Formatter.formatIpAddress(wifiManager.getDhcpInfo().serverAddress);`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:395`
  `WifiManager wifiManager = (WifiManager) Utils.getApp().getApplicationContext().getSystemService(z8.b);`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:396`
  `if (wifiManager == null || (connectionInfo = wifiManager.getConnectionInfo()) == null) {`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:418`
  `if (getWifiEnabled() && (scanResults = ((WifiManager) Utils.getApp().getSystemService(z8.b)).getScanResults()) != null) {`
- `sources/com/blankj/utilcode/util/NetworkUtils.java:472`
  `((WifiManager) Utils.getApp().getSystemService(z8.b)).startScan();`
- `sources/com/os/adqualitysdk/sdk/i/jy.java:17`
  `import android.net.wifi.WifiManager;`
- `sources/com/os/adqualitysdk/sdk/i/jy.java:450`
  `WifiInfo connectionInfo = ((WifiManager) context.getSystemService(m3604((byte) (29 - ((Process.getThreadPriority(0) + 20) >> 6)), (short) ((-43) - (ExpandableListView.getPackedPositionForChild(0, 0) > 0L ? 1 : (ExpandableListView.getPackedPositionForChild(0, 0) == 0L ? 0 : -1))), (ViewConfiguration....`
- `sources/com/pgl/ssdk/ah.java:11`
  `import android.net.wifi.WifiManager;`
- `sources/com/pgl/ssdk/ah.java:79`
  `WifiManager wifiManager = (WifiManager) context.getApplicationContext().getSystemService(z8.b);`
- `sources/com/pgl/ssdk/ah.java:80`
  `return (wifiManager == null || !wifiManager.isWifiEnabled()) ? "0" : "1";`
- `sources/com/realsil/sdk/support/utilities/NetworkHelper.java:6`
  `import android.net.wifi.WifiManager;`
- `sources/com/realsil/sdk/support/utilities/NetworkHelper.java:87`
  `return Formatter.formatIpAddress(((WifiManager) context.getApplicationContext().getSystemService(z8.b)).getConnectionInfo().getIpAddress());`
- `sources/com/yandex/mobile/ads/impl/xa0.java:9`
  `import android.net.wifi.WifiManager;`
- `sources/com/yandex/mobile/ads/impl/xa0.java:704`
  `Intrinsics.checkNotNull(systemService3, "null cannot be cast to non-null type android.net.wifi.WifiManager");`
- `sources/com/yandex/mobile/ads/impl/xa0.java:705`
  `WifiManager wifiManager = (WifiManager) systemService3;`
- `sources/com/yandex/mobile/ads/impl/xa0.java:706`
  `if (wifiManager.isWifiEnabled()) {`
- `sources/com/yandex/mobile/ads/impl/xa0.java:707`
  `List<ScanResult> scanResults = wifiManager.getScanResults();`

## BR047

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/android/support/v4/media/MediaBrowserCompat.java:651`
  `Log.d(MediaBrowserCompat.TAG, "addSubscription failed with RemoteException parentId=" + str);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:745`
  `Log.i(MediaBrowserCompat.TAG, "Remote error sending a custom action: action=" + str + ", extras=" + bundle, e);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:761`
  `Log.w(MediaBrowserCompat.TAG, "onConnect from service while mState=" + getStateLabel(this.mState) + "... ignoring");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:863`
  `Log.d(MediaBrowserCompat.TAG, "  mServiceBinderWrapper=" + this.mServiceBinderWrapper);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:864`
  `Log.d(MediaBrowserCompat.TAG, "  mCallbacksMessenger=" + this.mCallbacksMessenger);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:865`
  `Log.d(MediaBrowserCompat.TAG, "  mRootId=" + this.mRootId);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:866`
  `Log.d(MediaBrowserCompat.TAG, "  mMediaSessionToken=" + this.mMediaSessionToken);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1049`
  `Log.i(MediaBrowserCompat.TAG, "Remote error subscribing media item: " + str);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1172`
  `Log.i(MediaBrowserCompat.TAG, "The connected service doesn't support sendCustomAction.");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1185`
  `Log.i(MediaBrowserCompat.TAG, "Remote error sending a custom action: action=" + str + ", extras=" + bundle, e);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1379`
  `Log.w(MediaBrowserCompat.TAG, "Unhandled message: " + message + "\n  Client version: 1\n  Service version: " + message.arg1);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1382`
  `Log.e(MediaBrowserCompat.TAG, "Could not unparcel the data.");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1559`
  `Log.w(MediaBrowserCompat.TAG, "Unknown result code: " + i + " (extras=" + this.mExtras + ", resultData=" + bundle + ")");`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:140`
  `Log.e(TAG, "Dead object in getMediaController.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:167`
  `Log.w(TAG, "Failed to create MediaControllerImpl.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1166`
  `Log.e(MediaControllerCompat.TAG, "Dead object in setRating.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1208`
  `Log.e(MediaControllerCompat.TAG, "Dead object in sendCustomAction.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1249`
  `Log.e(MediaControllerCompat.TAG, "Dead object in registerCallback.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1270`
  `Log.e(MediaControllerCompat.TAG, "Dead object in unregisterCallback.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1297`
  `Log.e(MediaControllerCompat.TAG, "Dead object in getPlaybackState.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1379`
  `Log.e(MediaControllerCompat.TAG, "Dead object in isCaptioningEnabled.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1392`
  `Log.e(MediaControllerCompat.TAG, "Dead object in getRepeatMode.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1405`
  `Log.e(MediaControllerCompat.TAG, "Dead object in getShuffleMode.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1470`
  `Log.e(MediaControllerCompat.TAG, "Dead object in registerCallback.", e);`
- `sources/androidx/activity/result/ActivityResultRegistry.java:186`
  `Log.w(LOG_TAG, "Dropping pending result for request " + key + ": " + this.parsedPendingResults.get(key));`
- `sources/androidx/activity/result/ActivityResultRegistry.java:190`
  `Log.w(LOG_TAG, "Dropping pending result for request " + key + ": " + ((ActivityResult) BundleCompat.getParcelable(this.pendingResults, key, ActivityResult.class)));`
- `sources/androidx/appcompat/app/ActionBarDrawerToggle.java:216`
  `Log.w("ActionBarDrawerToggle", "DrawerToggle may not show up because NavigationIcon is not visible. You may need to call actionbar.setDisplayHomeAsUpEnabled(true);");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1259`
  `Log.i("AppCompatDelegate", "Failed to instantiate custom view inflater " + string + ". Falling back to default.", th);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1310`
  `Log.i("AppCompatDelegate", "The Activity's LayoutInflater already has a Factory installed so we can not install AppCompat's");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1840`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1846`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR_OVERLAY id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2078`
  `Log.d("AppCompatDelegate", "Exception while getting ActivityInfo", e);`
- `sources/androidx/appcompat/app/ResourcesFlusher.java:164`
  `Log.e(TAG, "Could not retrieve value from ThemedResourceCache#mUnthemedEntries", e3);`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:301`
  `Log.w(SupportMenuInflater.LOG_TAG, "Ignoring attribute 'actionProviderClass'. Action view already specified.");`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:358`
  `Log.w(SupportMenuInflater.LOG_TAG, "Ignoring attribute 'itemActionViewLayout'. Action view already specified.");`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:397`
  `Log.w(SupportMenuInflater.LOG_TAG, "Cannot instantiate class: " + str, e);`
- `sources/androidx/appcompat/view/menu/MenuItemImpl.java:288`
  `Log.e(TAG, "Can't find activity to handle intent; ignoring", e);`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:349`
  `Log.w(TAG, "Failed to invoke TextView#nullLayouts() method", e);`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:203`
  `Log.e(TAG, "Exception while inflating drawable", e);`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:385`
  `Log.e("VdcInflateDelegate", "Exception while inflating <vector>", e);`

## BR050

paper_id: B021
paper_title: Metadata-Based Privacy Assessment for Mobile mHealth

- `audit_reports/01_rule_based_audit.md:460`
  `| BR050 | B021 | Metadata-Based Privacy Assessment for Mobile mHealth | not_supported | 隐私 URL 存在。 |`
- `audit_reports/01_rule_based_audit.md:461`
  `| BR051 | B013 | Availability and quality of mobile health app privacy policies | supported_hypothesis | 隐私文案有入口，但未完整覆盖所有 SDK/域名/健康 BLE 类别。 |`
- `audit_reports/01_rule_based_audit.md:462`
  `| BR052 | B013 | Availability and quality of mobile health app privacy policies | supported_hypothesis | 多 SDK/广告域存在，未抓包和完整政策核对。 |`
- `audit_reports/01_rule_based_audit.md:463`
  `| BR055 | B014 | Privacy Assessment in Mobile Health Apps: Scoping Review | not_supported | 本报告每项均保留证据链；该元规则未触发。 |`
- `prompts/rule_code_search_prompt_zh.md:897`
  `十一、隐私政策 / policy 类规则`
- `prompts/rule_code_search_prompt_zh.md:901`
  `- privacy/policy URL 与 strings/xml/assets/html 组合。`
- `prompts/rule_code_search_prompt_zh.md:902`
  `- third-party/SDK/advertising/analytics 与 privacy/policy 组合。`
- `prompts/rule_code_search_prompt_zh.md:903`
  `- health/device/location/Bluetooth/SMS/contact/call 与 privacy/policy 组合。`
- `prompts/rule_code_search_prompt_zh.md:908`
  `privacy`
- `prompts/rule_code_search_prompt_zh.md:909`
  `policy`
- `prompts/rule_code_search_prompt_zh.md:910`
  `privacy_url`
- `prompts/rule_code_search_prompt_zh.md:911`
  `privacy_cn`
- `prompts/rule_code_search_prompt_zh.md:912`
  `privacy_en`
- `prompts/rule_code_search_prompt_zh.md:913`
  `user_privacy`
- `resources/assets/html/privacy_en.html:1703`
  `font-size:10.5000pt;mso-font-kerning:1.0000pt;" ><font face="宋体" >Privacy Policy and User Agreement</font></span></b><b><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;`
- `resources/assets/html/privacy_in.html:2`
  `<!-- saved from url=(0044)file:///C:/Users/ygh/Desktop/privacy_cn.html -->`
- `resources/mozilla/public-suffix-list.txt:26`
  `// see also: "Domain Name Eligibility Policy" at http://www.aeda.ae/eng/aepolicy.php`
- `resources/mozilla/public-suffix-list.txt:1018`
  `// ge : http://www.nic.net.ge/policy_en.pdf`
- `resources/mozilla/public-suffix-list.txt:1067`
  `// gm : http://www.nic.gm/htmlpages%5Cgm-policy.htm`
- `resources/mozilla/public-suffix-list.txt:1773`
  `// jo : http://www.dns.jo/Registration_policy.aspx`
- `resources/mozilla/public-suffix-list.txt:3923`
  `// mt : https://www.nic.org.mt/go/policy`
- `resources/mozilla/public-suffix-list.txt:5735`
  `// pm : http://www.afnic.fr/medias/documents/AFNIC-naming-policy2012.pdf`
- `resources/mozilla/public-suffix-list.txt:5781`
  `// http://www.nic.ps/registration/policy.html#reg`
- `resources/mozilla/public-suffix-list.txt:5871`
  `// rw : http://www.nic.rw/cgi-bin/policy.pl`
- `resources/mozilla/public-suffix-list.txt:6025`
  `// st : http://www.nic.st/html/policyrules/`
- `resources/mozilla/public-suffix-list.txt:6101`
  `// tj : http://www.nic.tj/policy.html`
- `resources/mozilla/public-suffix-list.txt:6259`
  `// ua : https://hostmaster.ua/policy/?ua`
- `resources/mozilla/public-suffix-list.txt:6708`
  `// wf : http://www.afnic.fr/medias/documents/AFNIC-naming-policy2012.pdf`
- `resources/mozilla/public-suffix-list.txt:6720`
  `// yt : http://www.afnic.fr/medias/documents/AFNIC-naming-policy2012.pdf`
- `resources/mozilla/public-suffix-list.txt:11911`
  `// .KRD : http://nic.krd/data/krd/Registration%20Policy.pdf`
- `resources/res/layout/sdm_myoffer_banner_native_ad_layout_320x50.xml:127`
  `android:layout_toLeftOf="@+id/sdm_myoffer_privacy_agreement"`
- `resources/res/layout/sdm_myoffer_banner_native_ad_layout_320x50.xml:132`
  `android:id="@+id/sdm_myoffer_privacy_agreement"`
- `resources/res/layout/sdm_myoffer_banner_native_ad_layout_320x50.xml:136`
  `android:text="@string/sdm_myoffer_panel_privacy"`
- `resources/res/layout/sdm_myoffer_include_4_element.xml:30`
  `android:id="@+id/sdm_myoffer_privacy_agreement"`
- `resources/res/layout/sdm_myoffer_include_4_element.xml:33`
  `android:text="@string/sdm_myoffer_panel_privacy"`
- `resources/res/layout/sdm_myoffer_include_4_element.xml:34`
  `style="@style/sdm_myoffer_banner_privacy_text_style"/>`
- `resources/res/layout/sdm_myoffer_include_4_element_banner.xml:43`
  `android:layout_toLeftOf="@+id/sdm_myoffer_privacy_agreement"`
- `resources/res/layout/sdm_myoffer_include_4_element_banner.xml:48`
  `android:id="@+id/sdm_myoffer_privacy_agreement"`
- `resources/res/layout/sdm_myoffer_include_4_element_banner.xml:52`
  `android:text="@string/sdm_myoffer_panel_privacy"`
- `resources/res/layout/sdm_myoffer_include_4_element_with_disclaimer.xml:48`
  `android:id="@+id/sdm_myoffer_privacy_agreement"`
- `resources/res/layout/sdm_myoffer_include_4_element_with_disclaimer.xml:51`
  `android:text="@string/sdm_myoffer_panel_privacy"`
- `resources/res/layout/sdm_myoffer_include_4_element_with_disclaimer.xml:52`
  `style="@style/sdm_myoffer_banner_privacy_text_style"/>`
- `resources/res/layout/sdm_myoffer_include_4_element_with_feedback.xml:30`
  `android:id="@+id/sdm_myoffer_privacy_agreement"`
- `resources/res/layout/sdm_myoffer_include_4_element_with_feedback.xml:33`
  `android:text="@string/sdm_myoffer_panel_privacy"`
- `resources/res/layout/sdm_myoffer_include_4_element_with_feedback.xml:34`
  `style="@style/sdm_myoffer_banner_privacy_text_style"/>`
- `resources/res/layout/thinkup_myoffer_banner_native_ad_layout_320x50.xml:127`
  `android:layout_toLeftOf="@+id/thinkup_myoffer_privacy_agreement"`
- `resources/res/layout/thinkup_myoffer_banner_native_ad_layout_320x50.xml:132`
  `android:id="@+id/thinkup_myoffer_privacy_agreement"`
- `resources/res/layout/thinkup_myoffer_banner_native_ad_layout_320x50.xml:136`
  `android:text="@string/thinkup_myoffer_panel_privacy"`
- `resources/res/layout/thinkup_myoffer_include_4_element.xml:30`
  `android:id="@+id/thinkup_myoffer_privacy_agreement"`
- `resources/res/layout/thinkup_myoffer_include_4_element.xml:33`
  `android:text="@string/thinkup_myoffer_panel_privacy"`
- `resources/res/layout/thinkup_myoffer_include_4_element.xml:34`
  `style="@style/thinkup_myoffer_banner_privacy_text_style"/>`
- `resources/res/layout/thinkup_myoffer_include_4_element_banner.xml:43`
  `android:layout_toLeftOf="@+id/thinkup_myoffer_privacy_agreement"`
- `resources/res/layout/thinkup_myoffer_include_4_element_banner.xml:48`
  `android:id="@+id/thinkup_myoffer_privacy_agreement"`
- `resources/res/layout/thinkup_myoffer_include_4_element_banner.xml:52`
  `android:text="@string/thinkup_myoffer_panel_privacy"`
- `resources/res/layout/thinkup_myoffer_include_4_element_with_feedback.xml:30`
  `android:id="@+id/thinkup_myoffer_privacy_agreement"`
- `resources/res/layout/thinkup_myoffer_include_4_element_with_feedback.xml:33`
  `android:text="@string/thinkup_myoffer_panel_privacy"`
- `resources/res/layout/thinkup_myoffer_include_4_element_with_feedback.xml:34`
  `style="@style/thinkup_myoffer_banner_privacy_text_style"/>`
- `resources/res/values/public.xml:9316`
  `<public type="id" name="sdm_myoffer_privacy_agreement" id="0x7f0a08ce" />`
- `resources/res/values/public.xml:9787`
  `<public type="id" name="thinkup_myoffer_privacy_agreement" id="0x7f0a0aa5" />`
- `resources/res/values/strings.xml:121`
  `<string name="agree_confirm_privcty2">Privacy Policy</string>`
- `resources/res/values/strings.xml:1381`
  `<string name="permission_tips_content">Please read carefully and fully understand the terms of the user privacy agreement. Including but not limited to: in order to provide you with Bluetooth communication, content sharing and other services. We need to collect your device information, operation log...`
- `resources/res/values/strings.xml:1601`
  `<string name="privacy_cn">https://app.jusonsmart.com/public/privacy_cn_fitpro.html</string>`
- `resources/res/values/strings.xml:1602`
  `<string name="privacy_en">https://app.jusonsmart.com/public/privacy_en_fitpro.html</string>`
- `resources/res/values/strings.xml:1604`
  `<string name="private_protocol">Privacy Protocol</string>`
- `resources/res/values/strings.xml:1605`
  `<string name="private_user_protcol">Privacy policy and user agreement</string>`
- `resources/res/values/strings.xml:2718`
  `<string name="user_privacy">User Privacy</string>`
- `resources/res/values-es/strings.xml:582`
  `<string name="privacy_en">https://app.jusonsmart.com/public/privacy_sp_default.html</string>`

## BR051

paper_id: B013
paper_title: Availability and quality of mobile health app privacy policies

- `audit_reports/01_rule_based_audit.md:47`
  `- B002, 'Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment'：论文系统测试 79 个健康 App，关注个人信息采集、本地存储、传输和隐私政策一致性；其结果包括本地个人信息未加密、传输披露不足等问题。`
- `audit_reports/01_rule_based_audit.md:48`
  `- B005, 'Mobile health and privacy: cross sectional study'：论文强调移动健康 App 的第三方数据共享、隐私政策和实际传输之间的差距，尤其健康场景下标识符和健康数据组合的敏感性。`
- `audit_reports/01_rule_based_audit.md:50`
  `- B007, 'Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs'：论文讨论第三方库隐私设置、默认配置和披露不一致，不把 SDK 存在本身当作泄露证明。`
- `audit_reports/01_rule_based_audit.md:51`
  `- B008, 'Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android'：论文指出 BLE/Wi-Fi 扫描结果和标识符可能被 SDK 用于定位、跟踪和画像，需要区分第一方功能扫描与 SDK 采集。`
- `audit_reports/01_rule_based_audit.md:53`
  `- B013, 'Availability and quality of mobile health app privacy policies'：论文关注健康 App 隐私政策可用性和内容完整性。`
- `audit_reports/01_rule_based_audit.md:54`
  `- B014, 'Privacy Assessment in Mobile Health Apps: Scoping Review'：论文强调健康 App 隐私评估需要证据充分，不能仅凭单项指标做过度推断。`
- `audit_reports/01_rule_based_audit.md:55`
  `- B016, 'A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps'：论文关注 Manifest、网络配置、导出组件、权限说明和隐私安全实现的一致性。`
- `audit_reports/01_rule_based_audit.md:423`
  `| BR005 | B021 | Metadata-Based Privacy Assessment for Mobile mHealth | not_testable | 需要应用商店描述/元数据与 APK 权限对照；当前只有反编译工程，无 store metadata。 |`
- `audit_reports/01_rule_based_audit.md:424`
  `| BR006 | B016 | A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | confirmed | Manifest 'usesCleartextTraffic=true'，network base-config cleartext true。 |`
- `audit_reports/01_rule_based_audit.md:437`
  `| BR019 | B011 | Locking it down: The privacy and security of mobile medication apps | not_supported | 未发现药物数据链。 |`
- `audit_reports/01_rule_based_audit.md:438`
  `| BR020 | B012 | Reviewing the data security and privacy policies of mobile apps for depression | not_supported | 未发现抑郁/戒烟/心理健康核心字段链。 |`
- `audit_reports/01_rule_based_audit.md:448`
  `| BR030 | B016 | A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | confirmed | exported 'UploadDataService' onCreate 触发历史健康上传；WebSocket/BLE service 也导出。 |`
- `audit_reports/01_rule_based_audit.md:449`
  `| BR031 | B016 | A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | supported_hypothesis | Manifest receiver 很多，未完整确认敏感模块触达。 |`
- `audit_reports/01_rule_based_audit.md:454`
  `| BR040 | B007 | Privacy Settings of Third-Party Libraries in Android Apps | supported_hypothesis | 多个广告/统计 provider 自动初始化；未动态确认同意前行为。 |`
- `audit_reports/01_rule_based_audit.md:455`
  `| BR041 | B007 | Privacy Settings of Third-Party Libraries in Android Apps | supported_hypothesis | SDK 默认隐私配置未完全审计；存在大量广告 SDK。 |`
- `audit_reports/01_rule_based_audit.md:460`
  `| BR050 | B021 | Metadata-Based Privacy Assessment for Mobile mHealth | not_supported | 隐私 URL 存在。 |`
- `audit_reports/01_rule_based_audit.md:461`
  `| BR051 | B013 | Availability and quality of mobile health app privacy policies | supported_hypothesis | 隐私文案有入口，但未完整覆盖所有 SDK/域名/健康 BLE 类别。 |`
- `audit_reports/01_rule_based_audit.md:462`
  `| BR052 | B013 | Availability and quality of mobile health app privacy policies | supported_hypothesis | 多 SDK/广告域存在，未抓包和完整政策核对。 |`
- `audit_reports/01_rule_based_audit.md:463`
  `| BR055 | B014 | Privacy Assessment in Mobile Health Apps: Scoping Review | not_supported | 本报告每项均保留证据链；该元规则未触发。 |`
- `audit_reports/01_rule_based_audit.md:466`
  `| BR060 | B016 | A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | supported_hypothesis | H5 默认 HTTP、测试支付域、静态资源域与正式 API 并存。 |`
- `audit_reports/01_rule_based_audit.md:477`
  `| BR071 | B016 | A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | supported_hypothesis | BLE/位置/SMS/联系人权限较多，政策文案不确定是否逐项解释。 |`
- `audit_reports/01_rule_based_audit.md:489`
  `| BR083 | B016 | A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | not_testable | 需要 adb 外部启动验证。 |`
- `audit_reports/01_rule_based_audit.md:493`
  `| BR090 | B014 | Privacy Assessment in Mobile Health Apps: Scoping Review | not_testable | 需要动态复核流程证据。 |`
- `audit_reports/01_rule_based_audit.md:495`
  `| BR092 | B005 | Mobile health and privacy | supported_hypothesis | AD_ID + 多广告 SDK；无抓包确认发送到第三方。 |`
- `audit_reports/01_rule_based_audit.md:496`
  `| BR093 | B004 | Assessment of the Data Sharing and Privacy Practices... | not_testable | 需完整政策和抓包收件方核对。 |`
- `audit_reports/01_rule_based_audit.md:497`
  `| BR094 | B016 | A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | supported_hypothesis | updateDeviceInfo 与天气/健康接口可组合身份、设备、位置、健康。 |`
- `audit_reports/01_rule_based_audit.md:499`
  `| BR096 | B011 | Locking it down: The privacy and security of mobile medication apps | not_supported | 未发现 medication upload。 |`
- `audit_reports/01_rule_based_audit.md:500`
  `| BR097 | B019 | Pulse Oximeter App Privacy Policies During COVID-19 | supported_hypothesis | SpO2/heart-rate 与 user token/device ID 上传链存在，缺抓包。 |`
- `audit_reports/02_evidence_chains.md:258`
  `4. 'strings.xml' 有 AdMob app id、Umeng key、多个广告 SDK privacy 文案。`
- `prompts/rule_code_search_prompt_zh.md:897`
  `十一、隐私政策 / policy 类规则`
- `prompts/rule_code_search_prompt_zh.md:901`
  `- privacy/policy URL 与 strings/xml/assets/html 组合。`
- `prompts/rule_code_search_prompt_zh.md:902`
  `- third-party/SDK/advertising/analytics 与 privacy/policy 组合。`
- `prompts/rule_code_search_prompt_zh.md:903`
  `- health/device/location/Bluetooth/SMS/contact/call 与 privacy/policy 组合。`
- `prompts/rule_code_search_prompt_zh.md:908`
  `privacy`
- `prompts/rule_code_search_prompt_zh.md:910`
  `privacy_url`
- `prompts/rule_code_search_prompt_zh.md:911`
  `privacy_cn`
- `prompts/rule_code_search_prompt_zh.md:912`
  `privacy_en`
- `prompts/rule_code_search_prompt_zh.md:913`
  `user_privacy`
- `resources/AndroidManifest.xml:1355`
  `android:theme="@style/tt_privacy_landing_page"`
- `resources/assets/html/privacy_en.html:1756`
  `mso-font-kerning:1.0000pt;" ><font face="宋体" >6. Changes to this Privacy Policy</font></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;`
- `resources/assets/html/privacy_en.html:1758`
  `mso-font-kerning:1.0000pt;" ><font face="宋体" >If we decide to change the Privacy Policy, we will post those changes in this Policy, on our website, and where we deem appropriate so that you can understand how we collect and use your personal information, who can access it, and where We will disclose...`
- `resources/assets/html/privacy_en.html:1760`
  `mso-font-kerning:1.0000pt;" ><font face="宋体" >The company reserves the right to modify this policy at any time, so please review it frequently. If there are major changes to this policy, the company will notify it through a website notice.</font></span><span style="mso-spacerun:'yes';font-family:Cal...`
- `resources/assets/html/privacy_en.html:1764`
  `mso-font-kerning:1.0000pt;" ><font face="宋体" >statistical services, and improve our products or services. We collect data based on your interactions with us and the choices you make, including your privacy settings and the products and services you use. Function. The data we collect may include</fon...`
- `resources/assets/html/privacy_en.html:1804`
  `mso-font-kerning:1.0000pt;" ><font face="宋体" >scanning, motion function positioning, and weather status acquisition. The app will not collect privately and reveal user privacy.</font></span><span style="mso-spacerun:'yes';font-family:宋体;mso-ascii-font-family:Calibri;`
- `resources/res/layout/sdm_myoffer_include_4_element.xml:66`
  `style="@style/sdm_myoffer_banner_privacy_text_style"/>`
- `resources/res/layout/sdm_myoffer_include_4_element_with_disclaimer.xml:84`
  `style="@style/sdm_myoffer_banner_privacy_text_style"/>`
- `resources/res/layout/sdm_myoffer_include_4_element_with_feedback.xml:66`
  `style="@style/sdm_myoffer_banner_privacy_text_style"/>`
- `resources/res/values/public.xml:16229`
  `<public type="style" name="unad_PrivacyThemeDialog" id="0x7f140646" />`
- `resources/res/values/public.xml:16230`
  `<public type="style" name="unad_PrivacyThemeDialog2" id="0x7f140647" />`
- `resources/res/values/strings.xml:155`
  `<string name="applovin_alt_privacy_policy_text" />`
- `resources/res/values/strings.xml:160`
  `<string name="applovin_pp_and_tos_title">To use %s you must agree to our Terms &amp; Conditions and affirm you have reviewed our Privacy Policy</string>`
- `resources/res/values/strings.xml:161`
  `<string name="applovin_pp_title">To use %s you must affirm that you have reviewed and acknowledged our Privacy Policy.</string>`
- `resources/res/values/strings.xml:162`
  `<string name="applovin_privacy_policy_text">Privacy Policy</string>`
- `resources/res/values/strings.xml:2637`
  `<string name="tt_text_privacy_app_version">Version：V</string>`
- `resources/res/values/strings.xml:2802`
  `<string name="yinsi_settings">privacy setting</string>`
- `resources/res/values-en/strings.xml:115`
  `<string name="tt_text_privacy_app_version">Version：V</string>`
- `resources/res/values-en/strings.xml:116`
  `<string name="tt_text_privacy_development">Developer：</string>`

## BR052

paper_id: B013
paper_title: Availability and quality of mobile health app privacy policies

- `audit_reports/01_rule_based_audit.md:47`
  `- B002, 'Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment'：论文系统测试 79 个健康 App，关注个人信息采集、本地存储、传输和隐私政策一致性；其结果包括本地个人信息未加密、传输披露不足等问题。`
- `audit_reports/01_rule_based_audit.md:48`
  `- B005, 'Mobile health and privacy: cross sectional study'：论文强调移动健康 App 的第三方数据共享、隐私政策和实际传输之间的差距，尤其健康场景下标识符和健康数据组合的敏感性。`
- `audit_reports/01_rule_based_audit.md:50`
  `- B007, 'Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs'：论文讨论第三方库隐私设置、默认配置和披露不一致，不把 SDK 存在本身当作泄露证明。`
- `audit_reports/01_rule_based_audit.md:51`
  `- B008, 'Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android'：论文指出 BLE/Wi-Fi 扫描结果和标识符可能被 SDK 用于定位、跟踪和画像，需要区分第一方功能扫描与 SDK 采集。`
- `audit_reports/01_rule_based_audit.md:53`
  `- B013, 'Availability and quality of mobile health app privacy policies'：论文关注健康 App 隐私政策可用性和内容完整性。`
- `audit_reports/01_rule_based_audit.md:54`
  `- B014, 'Privacy Assessment in Mobile Health Apps: Scoping Review'：论文强调健康 App 隐私评估需要证据充分，不能仅凭单项指标做过度推断。`
- `audit_reports/01_rule_based_audit.md:55`
  `- B016, 'A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps'：论文关注 Manifest、网络配置、导出组件、权限说明和隐私安全实现的一致性。`
- `audit_reports/01_rule_based_audit.md:423`
  `| BR005 | B021 | Metadata-Based Privacy Assessment for Mobile mHealth | not_testable | 需要应用商店描述/元数据与 APK 权限对照；当前只有反编译工程，无 store metadata。 |`
- `audit_reports/01_rule_based_audit.md:424`
  `| BR006 | B016 | A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | confirmed | Manifest 'usesCleartextTraffic=true'，network base-config cleartext true。 |`
- `audit_reports/01_rule_based_audit.md:437`
  `| BR019 | B011 | Locking it down: The privacy and security of mobile medication apps | not_supported | 未发现药物数据链。 |`
- `audit_reports/01_rule_based_audit.md:438`
  `| BR020 | B012 | Reviewing the data security and privacy policies of mobile apps for depression | not_supported | 未发现抑郁/戒烟/心理健康核心字段链。 |`
- `audit_reports/01_rule_based_audit.md:443`
  `| BR025 | B005 | Mobile health and privacy: cross sectional study | confirmed | 'ENCRYPTED=false'，SQLite 有健康/profile/session/位置表。 |`
- `audit_reports/01_rule_based_audit.md:444`
  `| BR026 | B002 | Unaddressed privacy risks in accredited health and wellness apps | confirmed | 普通 SharedPreferences 保存蓝牙地址、身高体重、目标、健康功能开关、实时步数。 |`
- `audit_reports/01_rule_based_audit.md:445`
  `| BR027 | B002 | Unaddressed privacy risks in accredited health and wellness apps | confirmed | DB/log/voice 使用外部 app-specific 目录；不夸大为 Android 11+ 任意读取。 |`
- `audit_reports/01_rule_based_audit.md:446`
  `| BR028 | B014 | Privacy Assessment in Mobile Health Apps: Scoping Review | confirmed | 'allowBackup=true'，'cloud-backup'，full backup，无排除敏感 DB。 |`
- `audit_reports/01_rule_based_audit.md:447`
  `| BR029 | B016 | A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | confirmed | 多个 exported Activity 到健康、调试、BLE 命令、支付二维码页面。 |`
- `audit_reports/01_rule_based_audit.md:448`
  `| BR030 | B016 | A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | confirmed | exported 'UploadDataService' onCreate 触发历史健康上传；WebSocket/BLE service 也导出。 |`
- `audit_reports/01_rule_based_audit.md:449`
  `| BR031 | B016 | A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | supported_hypothesis | Manifest receiver 很多，未完整确认敏感模块触达。 |`
- `audit_reports/01_rule_based_audit.md:454`
  `| BR040 | B007 | Privacy Settings of Third-Party Libraries in Android Apps | supported_hypothesis | 多个广告/统计 provider 自动初始化；未动态确认同意前行为。 |`
- `audit_reports/01_rule_based_audit.md:455`
  `| BR041 | B007 | Privacy Settings of Third-Party Libraries in Android Apps | supported_hypothesis | SDK 默认隐私配置未完全审计；存在大量广告 SDK。 |`
- `audit_reports/01_rule_based_audit.md:460`
  `| BR050 | B021 | Metadata-Based Privacy Assessment for Mobile mHealth | not_supported | 隐私 URL 存在。 |`
- `audit_reports/01_rule_based_audit.md:461`
  `| BR051 | B013 | Availability and quality of mobile health app privacy policies | supported_hypothesis | 隐私文案有入口，但未完整覆盖所有 SDK/域名/健康 BLE 类别。 |`
- `audit_reports/01_rule_based_audit.md:462`
  `| BR052 | B013 | Availability and quality of mobile health app privacy policies | supported_hypothesis | 多 SDK/广告域存在，未抓包和完整政策核对。 |`
- `audit_reports/01_rule_based_audit.md:463`
  `| BR055 | B014 | Privacy Assessment in Mobile Health Apps: Scoping Review | not_supported | 本报告每项均保留证据链；该元规则未触发。 |`
- `audit_reports/01_rule_based_audit.md:466`
  `| BR060 | B016 | A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | supported_hypothesis | H5 默认 HTTP、测试支付域、静态资源域与正式 API 并存。 |`
- `audit_reports/01_rule_based_audit.md:477`
  `| BR071 | B016 | A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | supported_hypothesis | BLE/位置/SMS/联系人权限较多，政策文案不确定是否逐项解释。 |`
- `audit_reports/01_rule_based_audit.md:487`
  `| BR081 | B005 | Mobile health and privacy | not_testable | 需要运行后文件系统 dump。 |`
- `audit_reports/01_rule_based_audit.md:489`
  `| BR083 | B016 | A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | not_testable | 需要 adb 外部启动验证。 |`
- `audit_reports/01_rule_based_audit.md:493`
  `| BR090 | B014 | Privacy Assessment in Mobile Health Apps: Scoping Review | not_testable | 需要动态复核流程证据。 |`
- `audit_reports/01_rule_based_audit.md:495`
  `| BR092 | B005 | Mobile health and privacy | supported_hypothesis | AD_ID + 多广告 SDK；无抓包确认发送到第三方。 |`
- `audit_reports/01_rule_based_audit.md:496`
  `| BR093 | B004 | Assessment of the Data Sharing and Privacy Practices... | not_testable | 需完整政策和抓包收件方核对。 |`
- `audit_reports/01_rule_based_audit.md:497`
  `| BR094 | B016 | A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | supported_hypothesis | updateDeviceInfo 与天气/健康接口可组合身份、设备、位置、健康。 |`
- `audit_reports/01_rule_based_audit.md:499`
  `| BR096 | B011 | Locking it down: The privacy and security of mobile medication apps | not_supported | 未发现 medication upload。 |`
- `audit_reports/01_rule_based_audit.md:500`
  `| BR097 | B019 | Pulse Oximeter App Privacy Policies During COVID-19 | supported_hypothesis | SpO2/heart-rate 与 user token/device ID 上传链存在，缺抓包。 |`
- `audit_reports/02_evidence_chains.md:258`
  `4. 'strings.xml' 有 AdMob app id、Umeng key、多个广告 SDK privacy 文案。`
- `prompts/rule_code_search_prompt_zh.md:141`
  `paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps`
- `prompts/rule_code_search_prompt_zh.md:897`
  `十一、隐私政策 / policy 类规则`
- `prompts/rule_code_search_prompt_zh.md:901`
  `- privacy/policy URL 与 strings/xml/assets/html 组合。`
- `prompts/rule_code_search_prompt_zh.md:902`
  `- third-party/SDK/advertising/analytics 与 privacy/policy 组合。`
- `prompts/rule_code_search_prompt_zh.md:903`
  `- health/device/location/Bluetooth/SMS/contact/call 与 privacy/policy 组合。`
- `prompts/rule_code_search_prompt_zh.md:908`
  `privacy`
- `prompts/rule_code_search_prompt_zh.md:909`
  `policy`
- `resources/assets/html/privacy_en.html:1710`
  `mso-font-kerning:1.0000pt;" ><font face="宋体" >This Privacy Policy describes the company's privacy data related policies and practices, which will cover the personal information we collect, use, process, store and disclose about you through the company's mobile</font></span><span style="mso-spacerun:...`
- `resources/assets/html/privacy_en.html:1712`
  `mso-font-kerning:1.0000pt;" ><font face="宋体" >. Please read our Privacy Policy carefully.</font></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;`
- `resources/assets/html/privacy_en.html:1718`
  `mso-font-kerning:1.0000pt;" ><font face="宋体" >we will collect your personal information, such as email address, phone number, during the process of user registration. In order to protect personal privacy, you should not provide any other information other than those specifically requested by the com...`
- `resources/assets/html/privacy_en.html:1764`
  `mso-font-kerning:1.0000pt;" ><font face="宋体" >statistical services, and improve our products or services. We collect data based on your interactions with us and the choices you make, including your privacy settings and the products and services you use. Function. The data we collect may include</fon...`
- `resources/assets/html/privacy_en.html:1792`
  `mso-font-kerning:1.0000pt;" ><font face="宋体" >Get contact information. Under the premise of obtaining the user's permission, it is limited to synchronizing the mobile phone contacts to the Bluetooth device, and the app will not privately collect and leak user privacy.</font></span><span style="mso-s...`
- `resources/assets/html/privacy_en.html:1794`
  `mso-font-kerning:1.0000pt;" ><font face="宋体" >Get SMS. Under the premise of obtaining the user's permission, it is limited to forwarding the SMS information received by the mobile phone to the smart device, and the app will not collect and leak user privacy privately.</font></span><span style="mso-s...`
- `resources/assets/html/privacy_en.html:1796`
  `mso-font-kerning:1.0000pt;" ><font face="宋体" >Get call history. Under the premise of obtaining the user's permission, it is limited to synchronizing the incoming and outgoing status of the mobile phone to the Bluetooth device, and the app will not privately collect and leak user privacy.</font></spa...`
- `resources/assets/html/privacy_en.html:1804`
  `mso-font-kerning:1.0000pt;" ><font face="宋体" >scanning, motion function positioning, and weather status acquisition. The app will not collect privately and reveal user privacy.</font></span><span style="mso-spacerun:'yes';font-family:宋体;mso-ascii-font-family:Calibri;`
- `resources/assets/html/privacy_en.html:1844`
  `mso-font-kerning:1.0000pt;" ><font face="宋体" >11. Privacy Issues</font></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;`
- `resources/assets/html/privacy_en.html:1846`
  `mso-font-kerning:1.0000pt;" ><font face="宋体" >If you have any questions or concerns about our privacy policy or data processing, please</font></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;`
- `resources/assets/html/user_guide.html:20`
  `<!--<li><a href="license.html">Privacy Policy, Legal and License Information</a></li>-->`
- `resources/assets/html-en/user_guide.html:20`
  `<!--<li><a href="license.html">Privacy Policy, Legal and License Information</a></li>-->`
- `resources/res/values/public.xml:13387`
  `<public type="string" name="privacy_cn" id="0x7f13063e" />`
- `resources/res/values/public.xml:13388`
  `<public type="string" name="privacy_en" id="0x7f13063f" />`
- `resources/res/values/public.xml:14242`
  `<public type="string" name="thinkup_myoffer_panel_privacy" id="0x7f130995" />`
- `resources/res/values/public.xml:16159`
  `<public type="style" name="sdm_myoffer_banner_privacy_text_style" id="0x7f140600" />`
- `resources/res/values/strings.xml:155`
  `<string name="applovin_alt_privacy_policy_text" />`
- `resources/res/values/strings.xml:162`
  `<string name="applovin_privacy_policy_text">Privacy Policy</string>`
- `resources/res/values/strings.xml:1381`
  `<string name="permission_tips_content">Please read carefully and fully understand the terms of the user privacy agreement. Including but not limited to: in order to provide you with Bluetooth communication, content sharing and other services. We need to collect your device information, operation log...`
- `resources/res/values/strings.xml:1601`
  `<string name="privacy_cn">https://app.jusonsmart.com/public/privacy_cn_fitpro.html</string>`
- `resources/res/values/strings.xml:1602`
  `<string name="privacy_en">https://app.jusonsmart.com/public/privacy_en_fitpro.html</string>`
- `resources/res/values/strings.xml:1604`
  `<string name="private_protocol">Privacy Protocol</string>`
- `resources/res/values/strings.xml:1605`
  `<string name="private_user_protcol">Privacy policy and user agreement</string>`
- `resources/res/values/strings.xml:2456`
  `<string name="thinkup_myoffer_panel_privacy">Privacy</string>`
- `resources/res/values/strings.xml:2718`
  `<string name="user_privacy">User Privacy</string>`
- `resources/res/values-en/strings.xml:115`
  `<string name="tt_text_privacy_app_version">Version：V</string>`
- `resources/res/values-en/strings.xml:116`
  `<string name="tt_text_privacy_development">Developer：</string>`
- `resources/res/values-it/strings.xml:549`
  `<string name="permission_tips_content">Leggere attentamente e comprendere appieno ogni paragrafo dell \'Accordo sulla privacy dell\'utente. Inclusi ma non limitati a: Fornire servizi come la comunicazione Bluetooth e la condivisione di contenuti. Abbiamo bisogno di raccogliere informazioni personali...`
- `resources/res/values-it/strings.xml:554`
  `<string name="please_agree_and_login">Si prega di leggere e accettare l\'informativa sulla privacy!</string>`
- `resources/res/values-nl/strings.xml:515`
  `<string name="permission_tips_content"> Lees alle alinea\'s van de Privacyovereenkomst voor gebruikers zorgvuldig en begrijp ze volledig. Met inbegrip van maar niet beperkt tot: om u diensten aan te bieden zoals Bluetooth-communicatie en het delen van inhoud. We moeten persoonlijke informatie verzam...`
- `resources/res/values-nl/strings.xml:520`
  `<string name="please_agree_and_login">Lees en ga akkoord met het privacybeleid!</string>`
- `resources/res/values-sv/strings.xml:572`
  `<string name="please_agree_and_login">Vänligen läs och godkänn integritetspolicyn!</string>`
- `resources/res/values-tl/strings.xml:552`
  `<string name="permission_tips_content">Pakitiyak na basahin nang mabuti at lubos na maunawaan ang mga tuntunin ng Kasunduan sa Privacy ng User. Kabilang ngunit hindi limitado sa: Upang mabigyan ka ng mga serbisyo tulad ng Bluetooth na komunikasyon at pagbabahagi ng nilalaman. Kailangan naming mangol...`
- `resources/res/values-tl/strings.xml:573`
  `<string name="private_protocol">Kasunduan sa Privacy</string>`
- `resources/res/values-tl/strings.xml:574`
  `<string name="private_user_protcol">Patakaran sa Privacy at Kasunduan ng User</string>`
- `resources/res/values-zh/strings.xml:273`
  `<string name="thinkup_myoffer_panel_privacy">隐私</string>`

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
- `sources/com/alibaba/fastjson/parser/JSONReaderScanner.java:199`
  `throw new JSONException("TODO");`

## BR058

paper_id: B022
paper_title: A Study of Android Application Security

- `audit_reports/01_rule_based_audit.md:50`
  `- B007, 'Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs'：论文讨论第三方库隐私设置、默认配置和披露不一致，不把 SDK 存在本身当作泄露证明。`
- `audit_reports/01_rule_based_audit.md:454`
  `| BR040 | B007 | Privacy Settings of Third-Party Libraries in Android Apps | supported_hypothesis | 多个广告/统计 provider 自动初始化；未动态确认同意前行为。 |`
- `audit_reports/01_rule_based_audit.md:455`
  `| BR041 | B007 | Privacy Settings of Third-Party Libraries in Android Apps | supported_hypothesis | SDK 默认隐私配置未完全审计；存在大量广告 SDK。 |`
- `prompts/rule_code_search_prompt_zh.md:902`
  `- third-party/SDK/advertising/analytics 与 privacy/policy 组合。`
- `prompts/rule_code_search_prompt_zh.md:916`
  `third-party`
- `prompts/rule_code_search_prompt_zh.md:948`
  `third-party`
- `prompts/rule_code_search_prompt_zh.md:949`
  `first-party`
- `resources/LICENSES.txt:541`
  `wherever such third-party notices normally appear. The contents`
- `resources/LICENSES.txt:613`
  `identification within third-party archives.`
- `resources/META-INF/androidx/annotation/annotation/LICENSE.txt:116`
  `wherever such third-party notices normally appear. The contents`
- `resources/META-INF/androidx/constraintlayout/constraintlayout-core/LICENSE.txt:116`
  `wherever such third-party notices normally appear. The contents`
- `resources/META-INF/androidx/lifecycle/lifecycle-common/LICENSE.txt:116`
  `wherever such third-party notices normally appear. The contents`
- `resources/META-INF/commons-cli-1.4/META-INF/LICENSE.txt:115`
  `wherever such third-party notices normally appear. The contents`
- `resources/META-INF/commons-cli-1.4/META-INF/LICENSE.txt:187`
  `identification within third-party archives.`
- `resources/META-INF/commons-codec-1.10/META-INF/LICENSE.txt:116`
  `wherever such third-party notices normally appear. The contents`
- `resources/META-INF/commons-codec-1.10/META-INF/LICENSE.txt:188`
  `identification within third-party archives.`
- `resources/META-INF/commons-io-2.6/META-INF/LICENSE.txt:116`
  `wherever such third-party notices normally appear. The contents`
- `resources/META-INF/commons-io-2.6/META-INF/LICENSE.txt:188`
  `identification within third-party archives.`
- `resources/META-INF/commons-logging-1.2/META-INF/LICENSE.txt:116`
  `wherever such third-party notices normally appear. The contents`
- `resources/META-INF/commons-logging-1.2/META-INF/LICENSE.txt:188`
  `identification within third-party archives.`
- `sources/com/applovin/impl/z5.java:46`
  `map3.put("AppLovin-Third-Party-Ad-Placement-Id", v2Var.Q());`
- `sources/com/bytedance/sdk/component/adexpress/dynamic/lh/ko.java:160`
  `textView8.setText("Go to details page or third-party application");`
- `sources/com/bytedance/sdk/component/adexpress/le/cf.java:84`
  `str = "Slide or click to jump to the details page or third-party application";`
- `sources/com/google/android/gms/ads/internal/client/zzex.java:452`
  `Preconditions.checkState(this.zzl != null, "MobileAds.initialize() must be called prior to enable/disable the publisher first-party ID.");`
- `sources/com/google/android/gms/ads/internal/client/zzex.java:465`
  `sb.append(" the publisher first-party ID.");`
- `sources/kotlinx/coroutines/CancellableContinuationKt.java:18`
  `throw new UnsupportedOperationException("third-party implementation of CancellableContinuation is not supported");`

## BR059

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/AndroidManifest.xml:203`
  `<intent-filter>`
- `resources/AndroidManifest.xml:542`
  `<intent-filter>`

## BR060

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `sources/com/baidu/location/b/m.java:50`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING");`
- `sources/com/baidu/location/b/m.java:68`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING");`
- `sources/com/google/android/gms/internal/ads/zzhns.java:14`
  `return (Cipher) zzhxe.zza.zzb("AES/ECB/NoPadding");`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/NTLMEngineImpl.java:409`
  `Cipher cipher = Cipher.getInstance("DES/ECB/NoPadding");`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/NTLMEngineImpl.java:412`
  `Cipher cipher2 = Cipher.getInstance("DES/ECB/NoPadding");`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/NTLMEngineImpl.java:469`
  `Cipher cipher = Cipher.getInstance("DES/ECB/NoPadding");`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/NTLMEngineImpl.java:531`
  `Cipher cipher = Cipher.getInstance("DES/ECB/NoPadding");`
- `sources/com/inmobi/media/AbstractC3066j4.java:41`
  `Cipher cipher = Cipher.getInstance("AES/ECB/PKCS7Padding");`
- `sources/com/mbridge/msdk/playercommon/exoplayer2/upstream/cache/CachedContentIndex.java:63`
  `return Cipher.getInstance("AES/CBC/PKCS5PADDING", "BC");`
- `sources/com/mbridge/msdk/playercommon/exoplayer2/upstream/cache/CachedContentIndex.java:67`
  `return Cipher.getInstance("AES/CBC/PKCS5PADDING");`
- `sources/com/os/nk.java:23`
  `public static final String b = "RSA/ECB/PKCS1Padding";`
- `sources/com/phy/otalib/utils/AESTool.java:22`
  `Cipher cipher = Cipher.getInstance("AES/ECB/NoPadding");`
- `sources/com/phy/otalib/utils/AESTool.java:42`
  `Cipher cipher = Cipher.getInstance("AES/ECB/NoPadding");`
- `sources/com/smartdigimkt/o4/h.java:186`
  `return Cipher.getInstance("AES/CBC/PKCS5PADDING", "BC");`
- `sources/com/smartdigimkt/o4/h.java:190`
  `return Cipher.getInstance("AES/CBC/PKCS5PADDING");`
- `sources/io/appmetrica/analytics/coreutils/internal/encryption/AESEncrypter.java:10`
  `public static final String DEFAULT_ALGORITHM = "AES/CBC/PKCS5Padding";`

## BR061

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `resources/com/androidquery/callback/AbstractAjaxCallback.java:1619`
  `host = new HttpHost(urlObj.getHost(), 80, urlObj.getProtocol());`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:1621`
  `host = new HttpHost(urlObj.getHost(), urlObj.getPort(), urlObj.getProtocol());`
- `sources/androidx/constraintlayout/core/motion/Motion.java:1334`
  `public boolean setValue(int i, String str) {`
- `sources/androidx/core/view/inputmethod/EditorInfoCompat.java:24`
  `static int getProtocol(EditorInfo editorInfo) {`
- `sources/androidx/datastore/core/SingleProcessDataStore.java:312`
  `((SingleProcessDataStore) this.this$0).downstreamFlow.setValue(new Final(th));`
- `sources/androidx/lifecycle/LiveData.java:63`
  `LiveData.this.setValue(obj);`
- `sources/androidx/lifecycle/LiveData.java:85`
  `LiveData.this.setValue(obj2);`
- `sources/androidx/preference/SeekBarPreference.java:228`
  `public void setValue(int i) {`
- `sources/com/amazon/aps/shared/util/APSNetworkManager.java:60`
  `sendData(APSAnalytics.getHttpUrl(), APSAnalytics.getApiKey(), aPSEvent.toJsonPayload());`
- `sources/com/amazon/aps/shared/util/APSNetworkManager.java:66`
  `sendData(ApsMetrics.INSTANCE.getEndpointUrl(), ApsMetrics.INSTANCE.getApiKey(), jSONObject.toString());`
- `sources/com/amazon/aps/shared/util/APSNetworkManager.java:142`
  `public boolean m496lambda$sendData$0$comamazonapssharedutilAPSNetworkManager(String str, String str2, String str3) throws Throwable {`
- `sources/com/androidquery/callback/AbstractAjaxCallback.java:1095`
  `httpHost = new HttpHost(url.getHost(), 80, url.getProtocol());`
- `sources/com/androidquery/callback/AbstractAjaxCallback.java:1097`
  `httpHost = new HttpHost(url.getHost(), url.getPort(), url.getProtocol());`
- `sources/com/applovin/shadow/okhttp3/Handshake.java:205`
  `String protocol = sSLSession.getProtocol();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:382`
  `this.protocols = builder.getProtocols$okhttp();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:520`
  `@Metadata(d1 = {"\u0000ø\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0018...`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:645`
  `public final List<Protocol> getProtocols$okhttp() {`
- `sources/com/applovin/shadow/okhttp3/Response.java:93`
  `public final Protocol getProtocol() {`
- `sources/com/applovin/shadow/okhttp3/Response.java:299`
  `@Metadata(d1 = {"\u0000l\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\t\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u00...`
- `sources/com/applovin/shadow/okhttp3/Response.java:360`
  `/* JADX INFO: renamed from: getProtocol$okhttp, reason: from getter */`
- `sources/com/applovin/shadow/okhttp3/Response.java:361`
  `public final Protocol getProtocol() {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Platform.java:239`
  `arrayList3.add(((Protocol) it.next()).getProtocol());`
- `sources/com/applovin/shadow/okio/internal/ResourceFileSystem.java:293`
  `if (Intrinsics.areEqual(url.getProtocol(), "file")) {`
- `sources/com/beken/beken_ota/OTAAppFunctionActivity.java:637`
  `if (this.mOTASPPFunction.sendData(bArr)) {`
- `sources/com/beken/beken_ota/OTAAppFunctionActivity.java:651`
  `if (this.mOTABLEFunction.sendData(bArr)) {`
- `sources/com/beken/beken_ota/OTAFunctionActivity.java:478`
  `if (this.mOTASPPFunction.sendData(bArr)) {`
- `sources/com/beken/beken_ota/OTAFunctionActivity.java:492`
  `if (this.mOTABLEFunction.sendData(bArr)) {`
- `sources/com/beken/beken_ota/OTAMuiltFunctionActivity.java:504`
  `if (this.mOTASPPFunction.sendData(bArr)) {`
- `sources/com/beken/beken_ota/OTAMuiltFunctionActivity.java:518`
  `if (this.mOTABLEFunction.sendData(bArr)) {`
- `sources/com/beken/beken_ota/ble/BluetoothLeService.java:351`
  `this.mBluetoothGattCharateristic.setValue(bArr);`
- `sources/com/beken/beken_ota/ble/BluetoothLeService.java:352`
  `return this.mBluetoothGatt.writeCharacteristic(this.mBluetoothGattCharateristic);`
- `sources/com/beken/beken_ota/ble/OTABLEFunction.java:195`
  `public boolean sendData(byte[] bArr) {`
- `sources/com/beken/beken_ota/ble2/MyBluetoothMannager.java:114`
  `this.mBleMannager.write(this.mCurrentBleDevice, Profile.uartServiceUUID, Profile.uartWriteCharacteristicUUID, bArr, new BleWriteCallback() { // from class: com.beken.beken_ota.ble2.MyBluetoothMannager.1`
- `sources/com/beken/beken_ota/ble2/MyBluetoothMannager.java:131`
  `this.mBleMannager.write(this.mCurrentBleDevice, Profile.uartServiceUUID, Profile.uartWriteCharacteristicUUID, bArr, new BleWriteCallback() { // from class: com.beken.beken_ota.ble2.MyBluetoothMannager.2`
- `sources/com/beken/beken_ota/br/OTASPPFunction.java:160`
  `public boolean sendData(byte[] bArr) {`
- `sources/com/blankj/utilcode/util/ThreadUtils.java:704`
  `public void setValue(T t) {`
- `sources/com/clj/fastble/bluetooth/BleConnector.java:329`
  `bleIndicateCallback.onIndicateFailure(new OtherException("gatt writeDescriptor fail"));`
- `sources/com/clj/fastble/bluetooth/BleConnector.java:332`
  `return zWriteDescriptor;`
- `sources/com/clj/fastble/bluetooth/BleConnector.java:335`
  `public void writeCharacteristic(byte[] bArr, BleWriteCallback bleWriteCallback, String str) {`
- `sources/com/clj/fastble/bluetooth/SplitWriter.java:77`
  `this.mBleBluetooth.newBleConnector().withUUIDString(this.mUuid_service, this.mUuid_write).writeCharacteristic(this.mDataQueue.poll(), new BleWriteCallback() { // from class: com.clj.fastble.bluetooth.SplitWriter.2`

## BR062

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/com/beken/beken_ota/ble/OTABLEFunction.java:179`
  `if (this.mBluetoothLeService.setCharacteristicNotification(this.mOTAUUID2, true)) {`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEAdvertiseManager.java:273`
  `public void onCharacteristicReadRequest(BluetoothDevice bluetoothDevice, int i, int i2, BluetoothGattCharacteristic bluetoothGattCharacteristic) {`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEAdvertiseManager.java:274`
  `super.onCharacteristicReadRequest(bluetoothDevice, i, i2, bluetoothGattCharacteristic);`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEManager.java:837`
  `bluetoothIn3.bluetoothGatt.setCharacteristicNotification(bluetoothIn3.characteristic, true);`
- `sources/com/phy/otalib/ble/OTACore.java:725`
  `public void onCharacteristicChanged(BluetoothGatt bluetoothGatt, BluetoothGattCharacteristic bluetoothGattCharacteristic) {`
- `sources/com/realsil/sdk/core/bluetooth/GlobalGatt.java:73`
  `it.next().onCharacteristicChanged(bluetoothGatt, bluetoothGattCharacteristic);`
- `sources/com/realsil/sdk/core/bluetooth/GlobalGatt.java:78`
  `public void onCharacteristicRead(BluetoothGatt bluetoothGatt, BluetoothGattCharacteristic bluetoothGattCharacteristic, int i) {`
- `sources/com/realsil/sdk/core/bluetooth/GlobalGatt.java:101`
  `it.next().onCharacteristicRead(bluetoothGatt, bluetoothGattCharacteristic, i);`
- `sources/com/realsil/sdk/core/bluetooth/connection/le/BluetoothGattManager.java:72`
  `it.next().onCharacteristicChanged(bluetoothGatt, bluetoothGattCharacteristic);`
- `sources/com/realsil/sdk/core/bluetooth/connection/le/BluetoothGattManager.java:77`
  `public void onCharacteristicRead(BluetoothGatt bluetoothGatt, BluetoothGattCharacteristic bluetoothGattCharacteristic, int i) {`
- `sources/com/realsil/sdk/core/bluetooth/connection/le/BluetoothGattManager.java:100`
  `it.next().onCharacteristicRead(bluetoothGatt, bluetoothGattCharacteristic, i);`
- `sources/no/nordicsemi/android/dfu/BaseButtonlessDfuImpl.java:23`
  `public void onCharacteristicChanged(BluetoothGatt bluetoothGatt, BluetoothGattCharacteristic bluetoothGattCharacteristic) {`
- `sources/no/nordicsemi/android/dfu/BaseDfuImpl.java:71`
  `public void onCharacteristicRead(BluetoothGatt bluetoothGatt, BluetoothGattCharacteristic bluetoothGattCharacteristic, int i) {`
- `sources/no/nordicsemi/android/dfu/LegacyDfuImpl.java:108`
  `public void onCharacteristicChanged(BluetoothGatt bluetoothGatt, BluetoothGattCharacteristic bluetoothGattCharacteristic) {`
- `sources/no/nordicsemi/android/dfu/SecureDfuImpl.java:99`
  `public void onCharacteristicChanged(BluetoothGatt bluetoothGatt, BluetoothGattCharacteristic bluetoothGattCharacteristic) {`
- `sources/xfkj/fitpro/service/BaseLeService.java:250`
  `public void onCharacteristicRead(BluetoothGatt bluetoothGatt, BluetoothGattCharacteristic bluetoothGattCharacteristic, int i) {`
- `sources/xfkj/fitpro/service/BaseLeService.java:262`
  `MyApplication.Logdebug(BaseLeService.this.TAG, "onCharacteristicRead Value :设备信息  电量 " + strBytesToHexString);`
- `sources/xfkj/fitpro/service/BaseLeService.java:268`
  `MyApplication.Logdebug(BaseLeService.this.TAG, "onCharacteristicRead Value :设备信息  固件版本号 " + strBytetoString);`
- `sources/xfkj/fitpro/service/BaseLeService.java:445`
  `MyApplication.Logdebug(BaseLeService.this.TAG, "onCharacteristicRead Value :设备信息  读取自定义功能 " + strBytetoString2);`
- `sources/xfkj/fitpro/service/BaseLeService.java:495`
  `public void onCharacteristicChanged(BluetoothGatt bluetoothGatt, BluetoothGattCharacteristic bluetoothGattCharacteristic) {`
- `sources/xfkj/fitpro/service/BaseLeService.java:508`
  `MyApplication.Logdebug(BaseLeService.this.TAG, "onCharacteristicRead Value :设备信息  电量 " + strBytesToHexString2);`

## BR063

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `resources/com/androidquery/util/AQUtility.java:401`
  `byte[] b = new byte[IO_BUFFER_SIZE];`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:38`
  `public static final String COMMAND_ADD_QUEUE_ITEM = "android.support.v4.media.session.command.ADD_QUEUE_ITEM";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:39`
  `public static final String COMMAND_ADD_QUEUE_ITEM_AT = "android.support.v4.media.session.command.ADD_QUEUE_ITEM_AT";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:40`
  `public static final String COMMAND_ARGUMENT_INDEX = "android.support.v4.media.session.command.ARGUMENT_INDEX";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:41`
  `public static final String COMMAND_ARGUMENT_MEDIA_DESCRIPTION = "android.support.v4.media.session.command.ARGUMENT_MEDIA_DESCRIPTION";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:42`
  `public static final String COMMAND_GET_EXTRA_BINDER = "android.support.v4.media.session.command.GET_EXTRA_BINDER";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:43`
  `public static final String COMMAND_REMOVE_QUEUE_ITEM = "android.support.v4.media.session.command.REMOVE_QUEUE_ITEM";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:44`
  `public static final String COMMAND_REMOVE_QUEUE_ITEM_AT = "android.support.v4.media.session.command.REMOVE_QUEUE_ITEM_AT";`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:260`
  `byte[] bArrJpegImageToJpegByteArray = jpegImageToJpegByteArray(imageProxy);`
- `sources/androidx/exifinterface/media/ExifInterface.java:17`
  `import com.realsil.sdk.core.usb.connector.att.AttPduOpcodeDefine;`
- `sources/androidx/exifinterface/media/ExifInterface.java:1800`
  `byte[] bArr = this.mThumbnailBytes;`
- `sources/androidx/exifinterface/media/ExifInterface.java:2052`
  `byte[] bArr = new byte[5000];`
- `sources/androidx/exifinterface/media/ExifInterface.java:2284`
  `byte[] bArr = IDENTIFIER_EXIF_APP1;`
- `sources/androidx/exifinterface/media/ExifInterface.java:2286`
  `byte[] bArr2 = new byte[bArr.length];`
- `sources/androidx/exifinterface/media/ExifInterface.java:2291`
  `byte[] bArr3 = IDENTIFIER_EXIF_APP1;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:210`
  `int iUpdatePositionWithPostponed2 = updatePositionWithPostponed(updateOp.positionStart + (i * i5), updateOp.cmd);`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:211`
  `int i6 = updateOp.cmd;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:213`
  `UpdateOp updateOpObtainUpdateOp = obtainUpdateOp(updateOp.cmd, iUpdatePositionWithPostponed, i4, updateOp.payload);`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:216`
  `if (updateOp.cmd == 4) {`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:228`
  `UpdateOp updateOpObtainUpdateOp2 = obtainUpdateOp(updateOp.cmd, iUpdatePositionWithPostponed, i4, obj);`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:236`
  `int i2 = updateOp.cmd;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:508`
  `int cmd;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:514`
  `int i = this.cmd;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:523`
  `this.cmd = i;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:569`
  `updateOpAcquire.cmd = i;`
- `sources/androidx/room/RoomSQLiteQuery.java:111`
  `this.mBlobBindings = new byte[i2][];`
- `sources/androidx/work/impl/background/systemalarm/ConstraintsCommandHandler.java:44`
  `Logger.get().debug(TAG, String.format("Creating a delay_met command for workSpec with id (%s)", str2), new Throwable[0]);`
- `sources/androidx/work/impl/model/WorkProgressDao_Impl.java:37`
  `byte[] byteArrayInternal = Data.toByteArrayInternal(value.mProgress);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:63`
  `byte[] byteArrayInternal = Data.toByteArrayInternal(workSpec.input);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:69`
  `byte[] byteArrayInternal2 = Data.toByteArrayInternal(workSpec.output);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:95`
  `byte[] bArrContentUriTriggersToByteArray = WorkTypeConverters.contentUriTriggersToByteArray(constraints.getContentUriTriggers());`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:199`
  `byte[] byteArrayInternal = Data.toByteArrayInternal(output);`
- `sources/com/airbnb/lottie/manager/ImageAssetManager.java:83`
  `byte[] bArrDecode = Base64.decode(fileName.substring(fileName.indexOf(44) + 1), 0);`
- `sources/com/alibaba/fastjson/parser/deserializer/ASMDeserializerFactory.java:50`
  `public class ASMDeserializerFactory implements Opcodes {`
- `sources/com/alibaba/fastjson/serializer/ASMSerializerFactory.java:37`
  `public class ASMSerializerFactory implements Opcodes {`
- `sources/com/androidquery/util/AQUtility.java:338`
  `byte[] bArr = new byte[4096];`
- `sources/com/applovin/impl/b2.java:34`
  `byte[] bArrDecode = Base64.decode((String) obj, 0);`
- `sources/com/applovin/shadow/okhttp3/internal/ws/RealWebSocket.java:48`
  `@Metadata(d1 = {"\u0000¶\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\t\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u000b\n\u0000\n...`
- `sources/com/applovin/shadow/okhttp3/internal/ws/WebSocketProtocol.java:11`
  `@Metadata(d1 = {"\u00004\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\b\n\u0002\b\b\n\u0002\u0010\t\n\u0002\b\u0011\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0010\u0012\n\u0002\b\u0002\bÆ\u0002\u0018\u00002\u00020\u0001B\u0007\b\u00...`
- `sources/com/applovin/shadow/okhttp3/internal/ws/WebSocketProtocol.java:26`
  `public static final int OPCODE_CONTINUATION = 0;`

## BR064

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:192`
  `String name = xml.getName();`
- `sources/androidx/browser/customtabs/PostMessageServiceConnection.java:44`
  `intent.setClassName(str, PostMessageService.class.getName());`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1037`
  `this.mUseCaseAttachState.setUseCaseDetached(this.mMeteringRepeatingSession.getName() + this.mMeteringRepeatingSession.hashCode());`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1038`
  `this.mUseCaseAttachState.setUseCaseInactive(this.mMeteringRepeatingSession.getName() + this.mMeteringRepeatingSession.hashCode());`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1378`
  `return meteringRepeatingSession.getName() + meteringRepeatingSession.hashCode();`
- `sources/androidx/camera/camera2/internal/DynamicRangeResolver.java:103`
  `DynamicRange dynamicRangeResolveDynamicRange = resolveDynamicRange(dynamicRange, set4, set2, set3, useCaseConfig.getTargetName());`
- `sources/androidx/camera/camera2/internal/DynamicRangeResolver.java:108`
  `throw new IllegalArgumentException(String.format("Unable to resolve supported dynamic range. The dynamic range may not be supported on the device or may not be allowed concurrently with other attached use cases.\nUse case:\n  %s\nRequested dynamic range:\n  %s\nSupported dynamic ranges:\n  %s\nConst...`
- `sources/androidx/camera/camera2/internal/MeteringRepeatingSession.java:46`
  `String getName() {`
- `sources/androidx/camera/video/VideoCapture.java:267`
  `return "VideoCapture:" + getName();`
- `sources/androidx/core/app/NotificationCompat.java:1441`
  `if (TextUtils.isEmpty(person.getName())) {`
- `sources/androidx/core/app/NotificationCompat.java:1449`
  `return this.mUser.getName();`
- `sources/androidx/core/app/NotificationCompat.java:1517`
  `messagingStyleCreateMessagingStyle = Api24Impl.createMessagingStyle(this.mUser.getName());`
- `sources/androidx/core/app/NotificationCompat.java:1562`
  `CharSequence name = message.getPerson() == null ? "" : message.getPerson().getName();`
- `sources/androidx/core/app/NotificationCompat.java:1566`
  `name = this.mUser.getName();`
- `sources/androidx/core/app/NotificationCompat.java:1585`
  `bundle.putCharSequence(NotificationCompat.EXTRA_SELF_DISPLAY_NAME, this.mUser.getName());`
- `sources/androidx/core/content/FileProvider.java:217`
  `String name = fileProviderPathsMetaData.getName();`
- `sources/androidx/core/graphics/WeightTypefaceApi14.java:29`
  `Log.e(TAG, e.getClass().getName(), e);`
- `sources/androidx/core/util/DebugUtils.java:14`
  `if ((simpleName == null || simpleName.length() <= 0) && (iLastIndexOf = (simpleName = obj.getClass().getName()).lastIndexOf(46)) > 0) {`
- `sources/androidx/lifecycle/serialization/SavedStateHandleDelegate.java:73`
  `return (thisRef != null ? Reflection.getOrCreateKotlinClass(thisRef.getClass()).getQualifiedName() + FilenameUtils.EXTENSION_SEPARATOR : "") + property.getName();`
- `sources/androidx/privacysandbox/ads/adservices/customaudience/CustomAudienceManager.java:71`
  `android.adservices.customaudience.LeaveCustomAudienceRequest leaveCustomAudienceRequestBuild = new LeaveCustomAudienceRequest.Builder().setBuyer(convertAdTechIdentifier(request.getBuyer())).setName(request.getName()).build();`
- `sources/androidx/privacysandbox/ads/adservices/customaudience/CustomAudienceManager.java:77`
  `android.adservices.customaudience.CustomAudience customAudienceBuild = new CustomAudience.Builder().setActivationTime(request.getActivationTime()).setAds(convertAdData(request.getAds())).setBiddingLogicUri(request.getBiddingLogicUri()).setBuyer(convertAdTechIdentifier(request.getBuyer())).setDailyUp...`
- `sources/androidx/recyclerview/widget/GridLayoutManager.java:133`
  `accessibilityNodeInfoCompat.setClassName(GridView.class.getName());`
- `sources/androidx/savedstate/SavedStateRegistry.java:73`
  `String name = clazz.getName();`
- `sources/androidx/savedstate/serialization/SavedStateRegistryOwnerDelegate.java:69`
  `return (thisRef != null ? Reflection.getOrCreateKotlinClass(thisRef.getClass()).getQualifiedName() + FilenameUtils.EXTENSION_SEPARATOR : "") + property.getName();`
- `sources/androidx/test/espresso/IdlingResource.java:10`
  `String getName();`
- `sources/androidx/test/espresso/base/IdlingResourceRegistry.java:99`
  `map.put(idlingResource2.getName(), idlingResource2);`
- `sources/androidx/test/espresso/base/IdlingResourceRegistry.java:118`
  `Preconditions.checkNotNull(idlingResource.getName(), "IdlingResource.getName() should not be null");`
- `sources/androidx/test/espresso/base/IdlingResourceRegistry.java:154`
  `if (this.idlingStates.get(i).resource.getName().equals(idlingResource.getName())) {`
- `sources/androidx/test/espresso/base/IdlingResourceRegistry.java:160`
  `Log.e(TAG, String.format("Attempted to unregister resource that is not registered: '%s'. Resource list: %s", idlingResource.getName(), getResources()));`
- `sources/androidx/test/espresso/base/IdlingResourceRegistry.java:387`
  `throw new IllegalStateException(String.format("Resource %s isIdleNow() is returning true, but a message indicating that the resource has transitioned from busy to idle was never sent.", idlingState.resource.getName()));`
- `sources/androidx/test/espresso/base/IdlingResourceRegistry.java:400`
  `Log.e(TAG, String.format("Attempted to register resource with same names: %s. R1: %s R2: %s.\nDuplicate resource registration will be ignored.", newResource.getName(), newResource, oldResource));`
- `sources/androidx/test/espresso/base/Interrogator.java:97`
  `String name = nextMessage.getTarget().getClass().getName();`
- `sources/androidx/test/espresso/base/LooperIdlingResourceInterrogationHandler.java:70`
  `public String getName() {`
- `sources/androidx/test/espresso/core/internal/deps/guava/cache/CacheBuilder.java:60`
  `private static final Logger logger = Logger.getLogger(CacheBuilder.class.getName());`
- `sources/androidx/test/espresso/core/internal/deps/guava/cache/LocalCache.java:73`
  `static final Logger logger = Logger.getLogger(LocalCache.class.getName());`
- `sources/androidx/test/espresso/idling/CountingIdlingResource.java:20`
  `public String getName() {`
- `sources/androidx/test/runner/screenshot/BasicScreenCaptureProcessor.java:21`
  `private static String sAndroidDeviceName = Build.DEVICE;`
- `sources/androidx/test/runner/screenshot/BasicScreenCaptureProcessor.java:23`
  `static void setAndroidDeviceName(String deviceName) {`
- `sources/androidx/test/runner/screenshot/BasicScreenCaptureProcessor.java:24`
  `sAndroidDeviceName = deviceName;`
- `sources/androidx/test/runner/screenshot/BasicScreenCaptureProcessor.java:86`
  `String str3 = sAndroidDeviceName;`
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
- `sources/app/akexorcist/bluetotohspp/library/BluetoothService.java:104`
  `bundle.putString(BluetoothState.DEVICE_NAME, bluetoothDevice.getName());`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothService.java:105`
  `bundle.putString(BluetoothState.DEVICE_ADDRESS, bluetoothDevice.getAddress());`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:26`
  `private String mDeviceName = null;`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:27`
  `private String mDeviceAddress = null;`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:54`
  `BluetoothSPP.this.mDeviceName = null;`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:55`
  `BluetoothSPP.this.mDeviceAddress = null;`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:96`
  `BluetoothSPP.this.mDeviceName = message.getData().getString(BluetoothState.DEVICE_NAME);`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:97`
  `BluetoothSPP.this.mDeviceAddress = message.getData().getString(BluetoothState.DEVICE_ADDRESS);`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:99`
  `BluetoothSPP.this.mBluetoothConnectionListener.onDeviceConnected(BluetoothSPP.this.mDeviceName, BluetoothSPP.this.mDeviceAddress);`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:132`
  `public String getConnectedDeviceAddress() {`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:133`
  `return this.mDeviceAddress;`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:136`
  `public String getConnectedDeviceName() {`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:137`
  `return this.mDeviceName;`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:303`
  `public String[] getPairedDeviceName() {`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:309`
  `strArr[i] = it.next().getName();`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:315`
  `public String[] getPairedDeviceAddress() {`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:321`
  `strArr[i] = it.next().getAddress();`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:340`
  `String[] pairedDeviceName = getPairedDeviceName();`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:341`
  `String[] pairedDeviceAddress = getPairedDeviceAddress();`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:342`
  `for (int i = 0; i < pairedDeviceName.length; i++) {`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:343`
  `if (pairedDeviceName[i].contains(str)) {`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:344`
  `arrayList.add(pairedDeviceAddress[i]);`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:345`
  `arrayList2.add(pairedDeviceName[i]);`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:386`
  `autoConnectionListener2.onNewConnection(pairedDeviceName[0], pairedDeviceAddress[0]);`
- `sources/app/akexorcist/bluetotohspp/library/DeviceList.java:65`
  `DeviceList.this.mPairedDevicesArrayAdapter.add(bluetoothDevice.getName() + IOUtils.LINE_SEPARATOR_UNIX + bluetoothDevice.getAddress());`
- `sources/app/akexorcist/bluetotohspp/library/DeviceList.java:116`
  `this.mPairedDevicesArrayAdapter.add(bluetoothDevice.getName() + IOUtils.LINE_SEPARATOR_UNIX + bluetoothDevice.getAddress());`
- `sources/app/akexorcist/bluetotohspp/library/DeviceList.java:140`
  `this.mPairedDevicesArrayAdapter.add(bluetoothDevice.getName() + IOUtils.LINE_SEPARATOR_UNIX + bluetoothDevice.getAddress());`
- `sources/com/airbnb/lottie/animation/content/GradientFillContent.java:51`
  `public String getName() {`
- `sources/com/airbnb/lottie/animation/content/GradientFillContent.java:62`
  `this.name = gradientFill.getName();`
- `sources/com/airbnb/lottie/animation/content/GradientStrokeContent.java:32`
  `public String getName() {`
- `sources/com/airbnb/lottie/animation/content/GradientStrokeContent.java:41`
  `this.name = gradientStroke.getName();`
- `sources/com/alibaba/fastjson/parser/ParserConfig.java:812`
  `String name = field.getName();`
- `sources/com/alibaba/fastjson/util/ASMClassLoader.java:73`
  `classMapping.put(cls.getName(), cls);`
- `sources/com/alibaba/fastjson/util/JavaBeanInfo.java:373`
  `if (cls != null && cls.getName().equals("org.springframework.security.web.savedrequest.DefaultSavedRequest")) {`
- `sources/com/alibaba/fastjson/util/TypeUtils.java:1309`
  `mappings.put(cls.getName(), cls);`

## BR065

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/com/beken/beken_ota/ble/BluetoothLeService.java:76`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/com/clj/fastble/bluetooth/BleBluetooth.java:79`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/com/clj/fastble/bluetooth/BleBluetooth.java:80`
  `super.onServicesDiscovered(bluetoothGatt, i);`
- `sources/com/clj/fastble/bluetooth/BleBluetooth.java:81`
  `BleLog.i("BluetoothGattCallback：onServicesDiscovered \nstatus: " + i + "\ncurrentThread: " + Thread.currentThread().getId());`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEManager.java:231`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEManager.java:232`
  `super.onServicesDiscovered(bluetoothGatt, i);`
- `sources/com/jieli/ble/BleManager.java:138`
  `BleManager.this.mBluetoothGattCallback.onServicesDiscovered(connectedBle2.getGatt(), 0);`
- `sources/com/jieli/ble/BleManager.java:228`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/com/jieli/ble/BleManager.java:251`
  `JL_Log.i(BleManager.TAG, "onServicesDiscovered : " + z);`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothBle.java:238`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothBle.java:239`
  `super.onServicesDiscovered(bluetoothGatt, i);`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothBle.java:869`
  `this.mBleEventCbManager.onServicesDiscovered(bluetoothGatt, i);`
- `sources/com/jieli/bluetooth_connect/tool/BleEventCbManager.java:42`
  `public void onServicesDiscovered(final BluetoothGatt bluetoothGatt, final int i) {`
- `sources/com/jieli/bluetooth_connect/tool/BleEventCbManager.java:46`
  `((OnBtBleListener) obj).onServicesDiscovered(bluetoothGatt, i);`
- `sources/com/onmicro/omtoolbox/service/BleService.java:114`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/com/onmicro/omtoolbox/service/BleService.java:115`
  `LogUtils.i(BleService.TAG, "onServicesDiscovered:" + i);`
- `sources/com/phy/otalib/ble/OTACore.java:634`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/com/realsil/sdk/core/bluetooth/GlobalGatt.java:240`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/com/realsil/sdk/core/bluetooth/GlobalGatt.java:257`
  `it.next().onServicesDiscovered(bluetoothGatt, i);`
- `sources/com/realsil/sdk/core/bluetooth/connection/le/BluetoothGattManager.java:239`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/com/realsil/sdk/core/bluetooth/connection/le/BluetoothGattManager.java:256`
  `it.next().onServicesDiscovered(bluetoothGatt, i);`
- `sources/com/realsil/sdk/core/usb/GlobalUsbGatt.java:320`
  `public void onServicesDiscovered(UsbGatt usbGatt, int i) {`
- `sources/com/realsil/sdk/core/usb/GlobalUsbGatt.java:331`
  `((UsbGattCallback) it.next()).onServicesDiscovered(usbGatt, i);`
- `sources/com/realsil/sdk/core/usb/UsbGatt.java:406`
  `UsbGatt.this.mUsbGattCallback.onServicesDiscovered(UsbGatt.this, 0);`
- `sources/com/realsil/sdk/core/usb/UsbGatt.java:415`
  `UsbGatt.this.mUsbGattCallback.onServicesDiscovered(UsbGatt.this, 257);`
- `sources/com/realsil/sdk/core/usb/UsbGatt.java:424`
  `UsbGatt.this.mUsbGattCallback.onServicesDiscovered(UsbGatt.this, 257);`
- `sources/com/realsil/sdk/core/usb/UsbGatt.java:433`
  `UsbGatt.this.mUsbGattCallback.onServicesDiscovered(UsbGatt.this, 257);`
- `sources/com/realsil/sdk/core/usb/UsbGattCallback.java:20`
  `public void onServicesDiscovered(UsbGatt usbGatt, int i) {`
- `sources/com/realsil/sdk/dfu/l/b.java:204`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/com/realsil/sdk/dfu/m/b.java:201`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/com/realsil/sdk/dfu/n/c.java:204`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/com/realsil/sdk/dfu/r/d.java:184`
  `public void onServicesDiscovered(UsbGatt usbGatt, int i) {`
- `sources/com/realsil/sdk/dfu/utils/GattDfuAdapter.java:206`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/com/realsil/sdk/dfu/utils/HidDfuAdapter.java:232`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/com/realsil/sdk/dfu/utils/UsbGattDfuAdapter.java:166`
  `public void onServicesDiscovered(UsbGatt usbGatt, int i) {`
- `sources/com/telink/ota/ble/Peripheral.java:734`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/com/telink/ota/ble/Peripheral.java:735`
  `super.onServicesDiscovered(bluetoothGatt, i);`
- `sources/com/telink/ota/ble/Peripheral.java:739`
  `onServicesDiscoveredComplete(services);`
- `sources/no/nordicsemi/android/dfu/DfuBaseService.java:300`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/xfkj/fitpro/bluetooth/BluetoothLeService.java:71`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/xfkj/fitpro/bluetooth/BluetoothLeService.java:74`
  `MyApplication.Logdebug(BluetoothLeService.TAG, "onServicesDiscovered");`
- `sources/xfkj/fitpro/bluetooth/BluetoothLeService.java:76`
  `Log.w(BluetoothLeService.TAG, "onServicesDiscovered received: " + i);`
- `sources/xfkj/fitpro/bluetooth/HTXHardwareReader.java:232`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/xfkj/fitpro/service/BaseLeService.java:162`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/xfkj/fitpro/service/BaseLeService.java:179`
  `MyApplication.Logdebug(BaseLeService.this.TAG, "onServicesDiscovered service uuid: " + uuid);`
- `sources/xfkj/fitpro/service/BaseLeService.java:244`
  `MyApplication.Logdebug(BaseLeService.this.TAG, "获取蓝牙服务失败 onServicesDiscovered received: " + i);`

## BR066

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/app/akexorcist/bluetotohspp/library/BluetoothService.java:22`
  `private static final UUID UUID_ANDROID_DEVICE = UUID.fromString("fa87c0d0-afac-11de-8a39-0800200c9a66");`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothService.java:23`
  `private static final UUID UUID_OTHER_DEVICE = UUID.fromString(ConsData.MY_BLUETOOTH3_UUID);`
- `sources/com/beken/beken_ota/ble/BluetoothLeService.java:48`
  `static final UUID UUID_OTA_SERVICE = UUID.fromString("f000ffc0-0451-4000-b000-000000000000");`
- `sources/com/beken/beken_ota/ble/BluetoothLeService.java:49`
  `static final UUID UUID_IDENTFY = UUID.fromString("f000ffc1-0451-4000-b000-000000000000");`
- `sources/com/beken/beken_ota/ble/BluetoothLeService.java:50`
  `static final UUID UUID_BLOCK = UUID.fromString("f000ffc2-0451-4000-b000-000000000000");`
- `sources/com/beken/beken_ota/ble/BluetoothLeService.java:301`
  `BluetoothGattDescriptor descriptor = bluetoothGattCharacteristic.getDescriptor(UUID.fromString("00002902-0000-1000-8000-00805f9b34fb"));`
- `sources/com/beken/beken_ota/ble/BluetoothLeService.java:317`
  `BluetoothGattDescriptor descriptor = bluetoothGattCharacteristic.getDescriptor(UUID.fromString("00002902-0000-1000-8000-00805f9b34fb"));`
- `sources/com/beken/beken_ota/ble/OTABLEFunction.java:34`
  `private UUID uuid_ota1 = UUID.fromString("f000ffc1-0451-4000-b000-000000000000");`
- `sources/com/beken/beken_ota/ble/OTABLEFunction.java:35`
  `private UUID uuid_ota2 = UUID.fromString("f000ffc2-0451-4000-b000-000000000000");`
- `sources/com/beken/beken_ota/ble2/MyBluetoothMannager.java:114`
  `this.mBleMannager.write(this.mCurrentBleDevice, Profile.uartServiceUUID, Profile.uartWriteCharacteristicUUID, bArr, new BleWriteCallback() { // from class: com.beken.beken_ota.ble2.MyBluetoothMannager.1`
- `sources/com/beken/beken_ota/ble2/MyBluetoothMannager.java:131`
  `this.mBleMannager.write(this.mCurrentBleDevice, Profile.uartServiceUUID, Profile.uartWriteCharacteristicUUID, bArr, new BleWriteCallback() { // from class: com.beken.beken_ota.ble2.MyBluetoothMannager.2`
- `sources/com/beken/beken_ota/ble2/MyBluetoothMannager.java:151`
  `BleManager.getInstance().notify(bleDevice, Profile.uartServiceUUID, Profile.uartNotifyCharacteristicUUID, new BleNotifyCallback() { // from class: com.beken.beken_ota.ble2.MyBluetoothMannager.3`
- `sources/com/beken/beken_ota/ble2/MyBluetoothMannager.java:172`
  `BleManager.getInstance().read(this.mCurrentBleDevice, Profile.deviceServiceUUID, Profile.deviceVersionUUID, bleReadCallback);`
- `sources/com/beken/beken_ota/ble2/MyBluetoothMannager.java:176`
  `BleManager.getInstance().read(this.mCurrentBleDevice, Profile.deviceServiceUUID, Profile.deviceFunctionUUID, bleReadCallback);`
- `sources/com/beken/beken_ota/ble2/MyBluetoothMannager.java:180`
  `BleManager.getInstance().read(this.mCurrentBleDevice, Profile.batteryServiceUUID, Profile.batteryCharacteristicUUID, bleReadCallback);`
- `sources/com/beken/beken_ota/ble2/Profile.java:8`
  `public static final String batteryCharacteristicUUID = "00002a19-0000-1000-8000-00805f9b34fb";`
- `sources/com/beken/beken_ota/ble2/Profile.java:9`
  `public static final String batteryServiceUUID = "0000180f-0000-1000-8000-00805f9b34fb";`
- `sources/com/beken/beken_ota/ble2/Profile.java:11`
  `public static final String deviceServiceUUID = "0000180a-0000-1000-8000-00805f9b34fb";`
- `sources/com/beken/beken_ota/ble2/Profile.java:13`
  `public static final String uartServiceUUID = Utils.getApp().getString(R.string.service_uuid);`
- `sources/com/beken/beken_ota/ble2/Profile.java:14`
  `public static final String uartWriteCharacteristicUUID = Utils.getApp().getString(R.string.write_uuid);`
- `sources/com/beken/beken_ota/ble2/Profile.java:15`
  `public static final String uartNotifyCharacteristicUUID = Utils.getApp().getString(R.string.notify_uuid);`
- `sources/com/clj/fastble/BleManager.java:188`
  `BleScanner.getInstance().scan(this.bleScanRuleConfig.getServiceUuids(), this.bleScanRuleConfig.getDeviceNames(), this.bleScanRuleConfig.getDeviceMac(), this.bleScanRuleConfig.isFuzzy(), this.bleScanRuleConfig.getScanTimeOut(), bleScanCallback);`
- `sources/com/clj/fastble/BleManager.java:200`
  `BleScanner.getInstance().scanAndConnect(this.bleScanRuleConfig.getServiceUuids(), this.bleScanRuleConfig.getDeviceNames(), this.bleScanRuleConfig.getDeviceMac(), this.bleScanRuleConfig.isFuzzy(), this.bleScanRuleConfig.getScanTimeOut(), bleScanAndConnectCallback);`
- `sources/com/clj/fastble/bluetooth/BleConnector.java:218`
  `return UUID.fromString(str);`
- `sources/com/clj/fastble/scan/BleScanRuleConfig.java:7`
  `private UUID[] mServiceUuids = null;`
- `sources/com/clj/fastble/scan/BleScanRuleConfig.java:26`
  `public UUID[] getServiceUuids() {`
- `sources/com/clj/fastble/scan/BleScanRuleConfig.java:27`
  `return this.mServiceUuids;`
- `sources/com/clj/fastble/scan/BleScanRuleConfig.java:39`
  `private UUID[] mServiceUuids = null;`
- `sources/com/clj/fastble/scan/BleScanRuleConfig.java:67`
  `public Builder setServiceUuids(UUID[] uuidArr) {`
- `sources/com/clj/fastble/scan/BleScanRuleConfig.java:68`
  `this.mServiceUuids = uuidArr;`
- `sources/com/clj/fastble/scan/BleScanRuleConfig.java:73`
  `bleScanRuleConfig.mServiceUuids = this.mServiceUuids;`
- `sources/com/example/bluetoothlibrary/bluetooth/BTBluetooth.java:52`
  `private String serviceUUID = null;`
- `sources/com/example/bluetoothlibrary/bluetooth/BTBluetooth.java:675`
  `this.serviceUUID = str;`
- `sources/com/example/bluetoothlibrary/bluetooth/BTBluetooth.java:698`
  `this.serviceUUID = str;`
- `sources/com/example/bluetoothlibrary/bluetooth/BTBluetooth.java:731`
  `LogUtil.showLogE(TAG, "setupService()-->readServiceUUID == null");`
- `sources/com/example/bluetoothlibrary/bluetooth/BTBluetooth.java:735`
  `LogUtil.showLogE(TAG, "setupService()-->writeServiceUUID == null");`
- `sources/com/example/bluetoothlibrary/bluetooth/BTBluetooth.java:799`
  `if (this.serviceUUID == null) {`
- `sources/com/example/bluetoothlibrary/bluetooth/BTBluetooth.java:800`
  `LogUtil.showLogE(TAG, "setupServiceWithMoreRead()-->serviceUUID == null");`
- `sources/com/example/bluetoothlibrary/bluetooth/BTBluetooth.java:804`
  `if (bluetoothGattService.getUuid().toString().equals(this.serviceUUID)) {`
- `sources/com/example/bluetoothlibrary/bluetooth/BTBluetooth.java:864`
  `if (this.serviceUUID == null) {`

## BR067

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/androidx/camera/view/CameraController.java:983`
  `public void setPinchToZoomEnabled(boolean z) {`
- `sources/com/example/bluetoothlibrary/bluetooth3/BTManager.java:249`
  `return ClsUtils.createBond(BluetoothDevice.class, bluetoothDevice);`
- `sources/com/example/bluetoothlibrary/bluetooth3/BTManager.java:262`
  `return bluetoothDevice.createBond();`
- `sources/com/example/bluetoothlibrary/bluetooth3/BTManager.java:272`
  `return ClsUtils.removeBond(BluetoothDevice.class, bluetoothDevice);`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEManager.java:684`
  `return ClsUtils.createBond(BluetoothDevice.class, bluetoothDevice);`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEManager.java:697`
  `return bluetoothDevice.createBond();`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEManager.java:707`
  `return ClsUtils.removeBond(BluetoothDevice.class, bluetoothDevice);`
- `sources/com/example/bluetoothlibrary/utils/ClsUtils.java:14`
  `public static boolean createBond(Class cls, BluetoothDevice bluetoothDevice) throws Exception {`
- `sources/com/example/bluetoothlibrary/utils/ClsUtils.java:15`
  `return ((Boolean) cls.getMethod("createBond", new Class[0]).invoke(bluetoothDevice, new Object[0])).booleanValue();`
- `sources/com/example/bluetoothlibrary/utils/ClsUtils.java:19`
  `return ((Boolean) cls.getMethod("setPin", byte[].class).invoke(bluetoothDevice, str.getBytes())).booleanValue();`
- `sources/com/example/bluetoothlibrary/utils/ClsUtils.java:22`
  `public static void setPairingConfirmation(BluetoothDevice bluetoothDevice) {`
- `sources/com/example/bluetoothlibrary/utils/ClsUtils.java:27`
  `Method declaredMethod = obj.getClass().getDeclaredMethod("setPairingConfirmation", BluetoothDevice.class, Boolean.TYPE);`
- `sources/com/example/bluetoothlibrary/utils/ClsUtils.java:41`
  `public static boolean removeBond(Class cls, BluetoothDevice bluetoothDevice) throws Exception {`
- `sources/com/example/bluetoothlibrary/utils/ClsUtils.java:42`
  `return ((Boolean) cls.getMethod("removeBond", new Class[0]).invoke(bluetoothDevice, new Object[0])).booleanValue();`
- `sources/com/example/bluetoothlibrary/utils/ClsUtils.java:45`
  `public static boolean setPin(Class cls, BluetoothDevice bluetoothDevice, String str) throws Exception {`
- `sources/com/example/bluetoothlibrary/utils/HidConnectUtil.java:123`
  `BluetoothDevice.class.getMethod("createBond", new Class[0]).invoke(this.device, new Object[0]);`
- `sources/com/example/bluetoothlibrary/utils/HidConnectUtil.java:132`
  `BluetoothDevice.class.getMethod("removeBond", new Class[0]).invoke(this.device, new Object[0]);`
- `sources/com/github/mikephil/charting/charts/BarLineChartBase.java:193`
  `public void setPinchZoom(boolean z) {`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothPair.java:95`
  `boolean zCreateBond;`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothPair.java:101`
  `zCreateBond = BluetoothUtil.createBond(this.mContext, bluetoothDevice, i);`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothPair.java:102`
  `JL_Log.w(TAG, "-pair- createBond ret = " + zCreateBond + ", pairWay = " + i);`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothPair.java:104`
  `zCreateBond = BluetoothUtil.createBond(this.mContext, bluetoothDevice);`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothPair.java:105`
  `JL_Log.w(TAG, "-pair- createBond ret = " + zCreateBond);`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothPair.java:107`
  `if (!zCreateBond) {`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothPair.java:120`
  `boolean zRemoveBond = BluetoothUtil.removeBond(this.mContext, bluetoothDevice);`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothPair.java:121`
  `JL_Log.w(TAG, "-unPair- result : " + zRemoveBond);`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothPair.java:122`
  `if (!zRemoveBond) {`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothPair.java:403`
  `JL_Log.i(BluetoothPair.TAG, "recv action :ACTION_BOND_STATE_CHANGED ... device : " + BluetoothUtil.printBtDeviceInfo(context, bluetoothDevice) + " ,bound : " + bondState);`
- `sources/com/jieli/bluetooth_connect/util/BluetoothUtil.java:66`
  `public static boolean createBond(Context context, BluetoothDevice bluetoothDevice, int i) {`
- `sources/com/jieli/bluetooth_connect/util/BluetoothUtil.java:71`
  `Method declaredMethod = bluetoothDevice.getClass().getDeclaredMethod("createBond", Integer.TYPE);`
- `sources/com/jieli/bluetooth_connect/util/BluetoothUtil.java:84`
  `public static boolean createBond(Context context, BluetoothDevice bluetoothDevice) {`
- `sources/com/jieli/bluetooth_connect/util/BluetoothUtil.java:88`
  `return bluetoothDevice.createBond();`
- `sources/com/jieli/bluetooth_connect/util/BluetoothUtil.java:91`
  `public static boolean removeBond(Context context, BluetoothDevice bluetoothDevice) {`
- `sources/com/jieli/bluetooth_connect/util/BluetoothUtil.java:96`
  `Object objInvoke = bluetoothDevice.getClass().getMethod("removeBond", new Class[0]).invoke(bluetoothDevice, new Object[0]);`
- `sources/com/jieli/bluetooth_connect/util/BluetoothUtil.java:103`
  `JL_Log.e(TAG, "Invoke removeBond : " + e.getMessage());`
- `sources/com/jieli/jl_bt_ota/impl/BluetoothOTAManager.java:877`
  `JL_Log.i(this.TAG, "-startUpgradeReConnect- removeBond >>> " + BluetoothUtil.removeBond(this.context, bluetoothDevice));`
- `sources/com/jieli/jl_bt_ota/util/BluetoothUtil.java:105`
  `public static boolean createBond(Context context, BluetoothDevice bluetoothDevice, int i) {`
- `sources/com/jieli/jl_bt_ota/util/BluetoothUtil.java:110`
  `Method declaredMethod = BluetoothDevice.class.getDeclaredMethod("createBond", Integer.TYPE);`
- `sources/com/jieli/jl_bt_ota/util/BluetoothUtil.java:329`
  `public static boolean removeBond(Context context, BluetoothDevice bluetoothDevice) {`
- `sources/com/jieli/jl_bt_ota/util/BluetoothUtil.java:334`
  `Object objInvoke = bluetoothDevice.getClass().getMethod("removeBond", new Class[0]).invoke(bluetoothDevice, new Object[0]);`
- `sources/com/jieli/jl_bt_ota/util/BluetoothUtil.java:341`
  `JL_Log.e(f6357a, "Invoke removeBond : " + e.getMessage());`
- `sources/com/jieli/jl_bt_ota/util/BluetoothUtil.java:406`
  `public static boolean createBond(BluetoothDevice bluetoothDevice) {`
- `sources/com/jieli/jl_bt_ota/util/BluetoothUtil.java:407`
  `return createBond(CommonUtil.getMainContext(), bluetoothDevice);`
- `sources/com/jieli/jl_bt_ota/util/BluetoothUtil.java:410`
  `public static boolean createBond(Context context, BluetoothDevice bluetoothDevice) {`
- `sources/com/jieli/jl_bt_ota/util/BluetoothUtil.java:414`
  `return bluetoothDevice.createBond();`
- `sources/com/onmicro/omtoolbox/service/BleService.java:402`
  `remoteDevice.getClass().getMethod("createBond", null).invoke(remoteDevice, null);`
- `sources/com/onmicro/omtoolbox/service/BleService.java:415`
  `Method method = remoteDevice.getClass().getMethod("removeBond", null);`
- `sources/com/realsil/ota/function/BaseBluetoothDfuActivity.java:299`
  `if (SettingsHelper.INSTANCE.getInstance().isDfuCompleteActionRemoveBondEnabled()) {`
- `sources/com/realsil/ota/function/BaseUsbGattDfuActivity.java:283`
  `if (SettingsHelper.INSTANCE.getInstance().isDfuCompleteActionRemoveBondEnabled()) {`
- `sources/com/realsil/sdk/core/bluetooth/RtkBluetoothManager.java:238`
  `public boolean createBond(byte[] bArr) {`
- `sources/com/realsil/sdk/core/bluetooth/RtkBluetoothManager.java:239`
  `return createBond(BluetoothHelper.convertMac(bArr));`
- `sources/com/realsil/sdk/core/bluetooth/RtkBluetoothManager.java:346`
  `boolean zRemoveBond = BluetoothDeviceImpl.removeBond(bluetoothDevice);`
- `sources/com/realsil/sdk/core/bluetooth/RtkBluetoothManager.java:348`
  `ZLogger.v(String.format(Locale.US, "removeBond(%d): %s, ret=%b", Integer.valueOf(i), BluetoothHelper.formatAddress(bluetoothDevice.getAddress(), !this.b), Boolean.valueOf(zRemoveBond)));`
- `sources/com/realsil/sdk/core/bluetooth/RtkBluetoothManager.java:350`
  `if (zRemoveBond) {`
- `sources/com/realsil/sdk/core/bluetooth/RtkBluetoothManager.java:390`
  `ZLogger.d("removeBond finished:" + BluetoothDeviceImpl.removeBond(bluetoothDevice));`
- `sources/com/realsil/sdk/core/bluetooth/RtkBluetoothManager.java:452`
  `public boolean createBond(String str) {`
- `sources/com/realsil/sdk/core/bluetooth/RtkBluetoothManager.java:467`
  `ZLogger.d("createBondMac=" + str);`
- `sources/com/realsil/sdk/core/bluetooth/RtkBluetoothManager.java:476`
  `ZLogger.d("attempt to createBond, state=" + Integer.toString(bondState));`
- `sources/com/realsil/sdk/core/bluetooth/RtkBluetoothManager.java:478`
  `return BluetoothDeviceImpl.createBond(remoteDevice);`
- `sources/com/realsil/sdk/core/bluetooth/RtkBluetoothManager.java:592`
  `ZLogger.d("createBondMac=" + BluetoothHelper.convertMac(bArr));`
- `sources/com/realsil/sdk/core/bluetooth/RtkBluetoothManager.java:597`
  `ZLogger.d("attempt to createBond, state=" + Integer.toString(bondState));`
- `sources/com/realsil/sdk/core/bluetooth/RtkBluetoothManager.java:599`
  `return remoteDevice.createBond();`
- `sources/com/realsil/sdk/core/bluetooth/impl/BluetoothDeviceImpl.java:82`
  `public static boolean removeBond(BluetoothDevice bluetoothDevice) {`
- `sources/com/realsil/sdk/core/bluetooth/impl/BluetoothDeviceImpl.java:84`
  `Method method = bluetoothDevice.getClass().getMethod("removeBond", null);`
- `sources/com/realsil/sdk/core/bluetooth/impl/BluetoothDeviceImpl.java:111`
  `public static boolean createBond(BluetoothDevice bluetoothDevice) {`
- `sources/com/realsil/sdk/core/bluetooth/impl/BluetoothDeviceImpl.java:112`
  `return bluetoothDevice.createBond();`
- `sources/com/realsil/sdk/core/bluetooth/impl/BluetoothDeviceImpl.java:115`
  `public static boolean createBond(BluetoothDevice bluetoothDevice, int i) {`
- `sources/com/realsil/sdk/core/bluetooth/impl/BluetoothDeviceImpl.java:120`
  `Method method = bluetoothDevice.getClass().getMethod("createBond", Integer.TYPE);`
- `sources/com/realsil/sdk/core/bluetooth/profile/BluetoothInputDeviceManager.java:86`
  `BluetoothInputDeviceManager.this.h.createBond();`
- `sources/com/realsil/sdk/core/bluetooth/profile/BluetoothInputDeviceManager.java:205`
  `bluetoothDevice.createBond();`
- `sources/com/realsil/sdk/core/bluetooth/profile/BluetoothInputDeviceManager.java:210`
  `Method method = bluetoothDevice.getClass().getMethod("removeBond", new Class[0]);`
- `sources/com/realsil/sdk/core/bluetooth/profile/BluetoothInputDeviceManager.java:217`
  `ZLogger.d("removeBond(): result: " + zBooleanValue);`
- `sources/com/realsil/sdk/core/bluetooth/profile/BluetoothInputDeviceManager.java:221`
  `ZLogger.e("removeBond(): An exception occured, e = " + e);`
- `sources/com/realsil/sdk/dfu/support/settings/SettingsHelper.java:25`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u00000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\b\n\u0002\b\u0003\n\u0002\u0010\u000b\n\u0002\b&\n\u0002\u0010\u000e\n\u0002\b\u000e\n\u0002\u0010\u0012\n\u0002\b\u0012\n\u0002\u0018\u0002\n\u0002\b\u0005\u0018\u0000 S2\u00020\u0001:\u0001SB\u0011\b\u00...`
- `sources/com/realsil/sdk/dfu/support/settings/SettingsHelper.java:136`
  `ZLogger.v("isDfuCompleteActionRemoveBondEnabled:" + isDfuCompleteActionRemoveBondEnabled());`
- `sources/com/realsil/sdk/dfu/support/settings/SettingsHelper.java:399`
  `public final boolean isDfuCompleteActionRemoveBondEnabled() {`
- `sources/com/realsil/sdk/dfu/utils/ConnectParams.java:147`
  `public boolean isCreateBond() {`
- `sources/com/realsil/sdk/dfu/utils/ConnectParams.java:159`
  `public void setCreateBond(boolean z) {`
- `sources/com/realsil/sdk/dfu/utils/GattDfuAdapter.java:338`
  `ZLogger.v(this.e, "createBond");`
- `sources/com/realsil/sdk/dfu/utils/GattDfuAdapter.java:339`
  `this.x.createBond();`

## BR068

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/com/androidquery/callback/AbstractAjaxCallback.java:823`
  `if (message != null && message.contains("No authentication challenges found")) {`
- `sources/com/applovin/shadow/okhttp3/Challenge.java:97`
  `public final Challenge withCharset(Charset charset) {`
- `sources/com/applovin/shadow/okhttp3/Challenge.java:103`
  `return new Challenge(this.scheme, (Map<String, String>) mutableMap);`
- `sources/com/applovin/shadow/okhttp3/Response.java:26`
  `@Metadata(d1 = {"\u0000p\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010\t\n\u0002\b\u...`
- `sources/com/applovin/shadow/okhttp3/internal/http/HttpHeaders.java:43`
  `readChallengeHeader(new Buffer().writeUtf8(headers.value(i)), arrayList);`
- `sources/com/applovin/shadow/okhttp3/internal/http/HttpHeaders.java:45`
  `Platform.INSTANCE.get().log("Unable to parse challenge", 5, e);`
- `sources/com/applovin/shadow/okhttp3/internal/http/HttpHeaders.java:65`
  `private static final void readChallengeHeader(com.applovin.shadow.okio.Buffer r7, java.util.List<com.applovin.shadow.okhttp3.Challenge> r8) throws java.io.EOFException {`
- `sources/com/applovin/shadow/okhttp3/internal/http/HttpHeaders.java:70`
  `throw new UnsupportedOperationException("Method not decompiled: com.applovin.shadow.okhttp3.internal.http.HttpHeaders.readChallengeHeader(com.applovin.shadow.okio.Buffer, java.util.List):void");`
- `sources/com/google/android/gms/auth/api/accounttransfer/AccountTransferStatusCodes.java:7`
  `public static final int CHALLENGE_NOT_ALLOWED = 20503;`
- `sources/com/google/android/gms/auth/api/accounttransfer/AccountTransferStatusCodes.java:21`
  `case CHALLENGE_NOT_ALLOWED /* 20503 */:`
- `sources/com/google/android/gms/auth/api/accounttransfer/AccountTransferStatusCodes.java:22`
  `return "CHALLENGE_NOT_ALLOWED";`
- `sources/com/google/android/gms/auth/api/accounttransfer/DeviceMetaData.java:41`
  `SafeParcelWriter.writeBoolean(parcel, 4, isChallengeAllowed());`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/auth/MalformedChallengeException.java:9`
  `public MalformedChallengeException() {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/auth/MalformedChallengeException.java:12`
  `public MalformedChallengeException(String str) {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/auth/MalformedChallengeException.java:16`
  `public MalformedChallengeException(String str, Throwable th) {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/client/protocol/RequestAuthCache.java:61`
  `if (proxyHost == null || proxyAuthState == null || proxyAuthState.getState() != AuthProtocolState.UNCHALLENGED || (authScheme = authCache.get(proxyHost)) == null) {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/client/protocol/RequestAuthenticationBase.java:43`
  `this.log.debug("Generating response to an authentication challenge using " + authScheme2.getSchemeName() + " scheme");`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/AuthSchemeBase.java:36`
  `public void processChallenge(Header header) throws MalformedChallengeException {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/AuthSchemeBase.java:42`
  `this.challengeState = ChallengeState.TARGET;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/AuthSchemeBase.java:44`
  `this.challengeState = ChallengeState.PROXY;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/AuthSchemeBase.java:46`
  `throw new MalformedChallengeException("Unexpected header name: " + name);`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/AuthSchemeBase.java:70`
  `throw new MalformedChallengeException("Invalid scheme identifier: " + strSubstring);`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/AuthSchemeBase.java:72`
  `parseChallenge(charArrayBuffer, i, charArrayBuffer.length());`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/DigestScheme.java:94`
  `throw new MalformedChallengeException("Authentication challenge is empty");`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/GGSSchemeBase.java:198`
  `protected void parseChallenge(CharArrayBuffer charArrayBuffer, int i, int i2) throws MalformedChallengeException {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/GGSSchemeBase.java:201`
  `this.log.debug("Received challenge '" + strSubstringTrimmed + "' from the auth server");`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/GGSSchemeBase.java:205`
  `this.state = State.CHALLENGE_RECEIVED;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/HttpAuthenticator.java:90`
  `public boolean handleAuthChallenge(HttpHost httpHost, HttpResponse httpResponse, AuthenticationStrategy authenticationStrategy, AuthState authState, HttpContext httpContext) {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/HttpAuthenticator.java:96`
  `Map<String, Header> challenges = authenticationStrategy.getChallenges(httpHost, httpResponse, httpContext);`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/HttpAuthenticator.java:97`
  `if (challenges.isEmpty()) {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/HttpAuthenticator.java:98`
  `this.log.debug("Response contains no authentication challenges");`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/HttpAuthenticator.java:113`
  `queueSelect = authenticationStrategy.select(challenges, httpHost, httpResponse, httpContext);`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/HttpAuthenticator.java:120`
  `authState.setState(AuthProtocolState.CHALLENGED);`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/HttpAuthenticator.java:148`
  `queueSelect = authenticationStrategy.select(challenges, httpHost, httpResponse, httpContext);`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/HttpAuthenticator.java:152`
  `} catch (MalformedChallengeException e) {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/HttpAuthenticator.java:154`
  `this.log.warn("Malformed challenge: " + e.getMessage());`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/HttpAuthenticator.java:174`
  `this.log.debug("Generating response to an authentication challenge using " + authScheme2.getSchemeName() + " scheme");`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/NTLMEngineImpl.java:561`
  `private final byte[] exportedSessionKey;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/NTLMEngineImpl.java:578`
  `this.exportedSessionKey = bArr;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/NTLMEngineImpl.java:1002`
  `protected final byte[] sessionKey;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/NTLMEngineImpl.java:1008`
  `public byte[] getEncryptedRandomSessionKey() {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/NTLMEngineImpl.java:1009`
  `return this.sessionKey;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/NTLMEngineImpl.java:1012`
  `public byte[] getExportedSessionKey() {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/NTLMEngineImpl.java:1013`
  `return this.exportedSessionKey;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/NTLMEngineImpl.java:1084`
  `this.exportedSessionKey = secondaryKey;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/NTLMEngineImpl.java:1085`
  `this.sessionKey = NTLMEngineImpl.RC4(secondaryKey, lMUserSessionKey);`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/NTLMEngineImpl.java:1087`
  `this.sessionKey = lMUserSessionKey;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/NTLMEngineImpl.java:1088`
  `this.exportedSessionKey = lMUserSessionKey;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/NTLMEngineImpl.java:1094`
  `this.sessionKey = null;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/auth/NTLMEngineImpl.java:1095`
  `this.exportedSessionKey = null;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/client/AbstractAuthenticationHandler.java:35`
  `protected Map<String, Header> parseChallenges(Header[] headerArr) throws MalformedChallengeException {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/client/AbstractAuthenticationHandler.java:101`
  `this.log.debug("Challenge for " + next + " authentication scheme not available");`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/client/AbstractAuthenticationHandler.java:107`
  `throw new AuthenticationException("Unable to respond to any of these challenges: " + map);`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/client/AuthenticationStrategyAdaptor.java:63`
  `authSchemeSelectScheme.processChallenge(map.get(authSchemeSelectScheme.getSchemeName().toLowerCase(Locale.ROOT)));`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/client/AuthenticationStrategyImpl.java:39`
  `private final int challengeCode;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/client/AuthenticationStrategyImpl.java:46`
  `this.challengeCode = i;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/client/AuthenticationStrategyImpl.java:124`
  `authSchemeCreate.processChallenge(header);`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/client/AuthenticationStrategyImpl.java:131`
  `this.log.debug("Challenge for " + str + " authentication scheme not available");`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/client/DefaultRequestDirector.java:276`
  `if (this.proxyAuthState.getState().compareTo(AuthProtocolState.CHALLENGED) > 0 && this.proxyAuthState.getAuthScheme() != null && this.proxyAuthState.getAuthScheme().isConnectionBased()) {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/client/DefaultRequestDirector.java:280`
  `if (this.targetAuthState.getState().compareTo(AuthProtocolState.CHALLENGED) > 0 && this.targetAuthState.getAuthScheme() != null && this.targetAuthState.getAuthScheme().isConnectionBased()) {`
- `sources/com/jieli/jl_bt_ota/model/response/TargetInfoResponse.java:8`
  `private String authKey;`
- `sources/com/jieli/jl_bt_ota/model/response/TargetInfoResponse.java:46`
  `public String getAuthKey() {`
- `sources/com/jieli/jl_bt_ota/model/response/TargetInfoResponse.java:47`
  `return this.authKey;`
- `sources/com/jieli/jl_bt_ota/model/response/TargetInfoResponse.java:187`
  `public TargetInfoResponse setAuthKey(String str) {`
- `sources/com/jieli/jl_bt_ota/model/response/TargetInfoResponse.java:188`
  `this.authKey = str;`
- `sources/com/jieli/jl_bt_ota/model/response/TargetInfoResponse.java:353`
  `return "TargetInfoResponse{versionName='" + this.versionName + "', versionCode=" + this.versionCode + ", protocolVersion='" + this.protocolVersion + "', edrAddr='" + this.edrAddr + "', edrStatus=" + this.edrStatus + ", edrProfile=" + this.edrProfile + ", bleAddr='" + this.bleAddr + "', volume=" + th...`
- `sources/com/yandex/mobile/ads/impl/hh0.java:39`
  `nh1.a(5, "Unable to parse challenge", e);`
- `sources/okhttp3/Challenge.java:13`
  `public final class Challenge {`
- `sources/okhttp3/Challenge.java:40`
  `public Challenge(String str, String str2) {`
- `sources/okhttp3/Challenge.java:76`
  `if (obj instanceof Challenge) {`
- `sources/okhttp3/Challenge.java:77`
  `Challenge challenge = (Challenge) obj;`
- `sources/okhttp3/Challenge.java:78`
  `if (challenge.scheme.equals(this.scheme) && challenge.authParams.equals(this.authParams)) {`
- `sources/okhttp3/internal/http/HttpHeaders.java:111`
  `public static List<Challenge> parseChallenges(Headers headers, String str) {`
- `sources/okhttp3/internal/http/HttpHeaders.java:115`
  `parseChallengeHeader(arrayList, new Buffer().writeUtf8(headers.value(i)));`
- `sources/okhttp3/internal/http/HttpHeaders.java:134`
  `private static void parseChallengeHeader(java.util.List<okhttp3.Challenge> r8, okio.Buffer r9) {`
- `sources/okhttp3/internal/http/HttpHeaders.java:139`
  `throw new UnsupportedOperationException("Method not decompiled: okhttp3.internal.http.HttpHeaders.parseChallengeHeader(java.util.List, okio.Buffer):void");`

## BR069

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/app/akexorcist/bluetotohspp/library/BluetoothService.java:104`
  `bundle.putString(BluetoothState.DEVICE_NAME, bluetoothDevice.getName());`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothService.java:105`
  `bundle.putString(BluetoothState.DEVICE_ADDRESS, bluetoothDevice.getAddress());`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:304`
  `Set<BluetoothDevice> bondedDevices = this.mBluetoothAdapter.getBondedDevices();`
- `sources/app/akexorcist/bluetotohspp/library/BluetoothSPP.java:306`
  `Iterator<BluetoothDevice> it = bondedDevices.iterator();`
- `sources/com/alibaba/fastjson/serializer/MiscCodec.java:83`
  `InetAddress address = inetSocketAddress.getAddress();`
- `sources/com/applovin/shadow/okio/HashingSink.java:101`
  `Intrinsics.checkNotNull(mac);`
- `sources/com/applovin/shadow/okio/HashingSink.java:102`
  `this(sink, mac);`
- `sources/com/applovin/shadow/okio/HashingSink.java:121`
  `Mac mac = this.mac;`
- `sources/com/applovin/shadow/okio/HashingSink.java:122`
  `Intrinsics.checkNotNull(mac);`
- `sources/com/applovin/shadow/okio/HashingSink.java:123`
  `mac.update(segment.data, segment.pos, iMin);`
- `sources/com/example/bluetoothlibrary/bluetooth3/BTManager.java:458`
  `public BluetoothDevice getDeviceByAddress(String str) {`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEAdvertiseManager.java:298`
  `public void onDescriptorWriteRequest(BluetoothDevice bluetoothDevice, int i, BluetoothGattDescriptor bluetoothGattDescriptor, boolean z, boolean z2, int i2, byte[] bArr) {`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEAdvertiseManager.java:299`
  `super.onDescriptorWriteRequest(bluetoothDevice, i, bluetoothGattDescriptor, z, z2, i2, bArr);`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEAdvertiseManager.java:300`
  `Log.w(BLEAdvertiseManager.TAG, String.format("BLE服务器端--接收描述符：device name = %s, address = %s", bluetoothDevice.getName(), bluetoothDevice.getAddress()));`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEAdvertiseManager.java:302`
  `BLEAdvertiseManager.this.bluetoothGattServer.sendResponse(bluetoothDevice, i, 0, i2, bArr);`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEAdvertiseManager.java:306`
  `public void onExecuteWrite(BluetoothDevice bluetoothDevice, int i, boolean z) {`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEAdvertiseManager.java:307`
  `super.onExecuteWrite(bluetoothDevice, i, z);`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEAdvertiseManager.java:308`
  `Log.w(BLEAdvertiseManager.TAG, String.format("BLE服务器端--执行写操作：device name = %s,requestId = %s", bluetoothDevice.getName(), Integer.valueOf(i)));`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEAdvertiseManager.java:312`
  `public void onNotificationSent(BluetoothDevice bluetoothDevice, int i) {`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEAdvertiseManager.java:313`
  `super.onNotificationSent(bluetoothDevice, i);`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEAdvertiseManager.java:314`
  `Log.w(BLEAdvertiseManager.TAG, String.format("BLE服务器端--发送通知或指示：device name = %s, address = %s", bluetoothDevice.getName(), bluetoothDevice.getAddress()));`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEManager.java:134`
  `BluetoothDevice device = bluetoothGatt.getDevice();`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEManager.java:135`
  `LogUtil.showLogD(BLEManager.TAG, "连接的设备：" + device.getName() + "  " + device.getAddress());`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEManager.java:139`
  `if (!TextUtils.equals(device.getAddress().toUpperCase(), BLEManager.this.curConnDevice.getAddress().toUpperCase())) {`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEManager.java:140`
  `LogUtil.showLogE(BLEManager.TAG, "连接成功的设备：" + device.getAddress() + ",需要连接的设备" + BLEManager.this.curConnDevice.getAddress());`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEManager.java:182`
  `if (!TextUtils.equals(device.getAddress().toUpperCase(), BLEManager.this.curConnDevice.getAddress().toUpperCase())) {`
- `sources/com/example/bluetoothlibrary/bluetooth4/BLEManager.java:183`
  `LogUtil.showLogE(BLEManager.TAG, "上报断开的设备：" + device.getAddress() + ",当前连接的设备" + BLEManager.this.curConnDevice.getAddress());`
- `sources/com/google/android/gms/internal/ads/zzfj.java:72`
  `zze = new String[]{"alb", NativeAdvancedJsUtils.o, "arm", "hy", "baq", "eu", "bur", "my", "tib", "bo", "chi", a.S, "cze", "cs", b.p0, "nl", "ger", "de", "gre", "el", "fre", a.W, "geo", "ka", "ice", "is", "mac", "mk", "mao", "mi", "may", "ms", com.smartdigimkt.q0.b.Z0, "fa", "rum", "ro", "scc", "hbs-...`
- `sources/com/jieli/ble/BleManager.java:277`
  `BluetoothDevice device = bluetoothGatt.getDevice();`
- `sources/com/jieli/ble/BleManager.java:289`
  `BluetoothDevice device;`
- `sources/com/jieli/bluetooth_connect/data/HistoryRecordDbHelper.java:119`
  `public void saveHistoryRecord(final BluetoothDevice bluetoothDevice, final int i) {`
- `sources/com/jieli/bluetooth_connect/data/HistoryRecordDbHelper.java:120`
  `if (bluetoothDevice == null || this.mThreadPool.isShutdown() || !ConnectUtil.isHasConnectPermission(this.mContext)) {`
- `sources/com/jieli/bluetooth_connect/data/HistoryRecordDbHelper.java:126`
  `this.f$0.m4033xa532a6c5(bluetoothDevice, i);`
- `sources/com/jieli/bluetooth_connect/data/HistoryRecordDbHelper.java:132`
  `/* synthetic */ void m4033xa532a6c5(BluetoothDevice bluetoothDevice, int i) {`
- `sources/com/jieli/bluetooth_connect/data/HistoryRecordDbHelper.java:133`
  `HistoryRecord historyRecordByDevice = getHistoryRecordByDevice(bluetoothDevice);`
- `sources/com/jieli/bluetooth_connect/data/HistoryRecordDbHelper.java:137`
  `} else if (bluetoothDevice.getAddress().equals(historyRecordByDevice.getUpdateAddress())) {`
- `sources/com/jieli/bluetooth_connect/data/HistoryRecordDbHelper.java:140`
  `historyRecordByDevice.setName(bluetoothDevice.getName());`
- `sources/com/jieli/bluetooth_connect/data/HistoryRecordDbHelper.java:141`
  `historyRecordByDevice.setAddress(bluetoothDevice.getAddress());`
- `sources/com/jieli/bluetooth_connect/data/HistoryRecordDbHelper.java:142`
  `historyRecordByDevice.setDevType(bluetoothDevice.getType());`
- `sources/com/jieli/bluetooth_connect/data/HistoryRecordDbHelper.java:145`
  `JL_Log.d("HistoryRecordDbHelper", ConnectUtil.formatString("saveHistoryRecord : %s, connectWay : %d, isAddRecord = %s", BluetoothUtil.printBtDeviceInfo(this.mContext, bluetoothDevice), Integer.valueOf(i), Boolean.valueOf(z)));`
- `sources/com/jieli/bluetooth_connect/data/HistoryRecordDbHelper.java:153`
  `public void updateDeviceIDs(final BluetoothDevice bluetoothDevice, final int i, final int i2, final int i3) {`
- `sources/com/jieli/bluetooth_connect/data/HistoryRecordDbHelper.java:154`
  `if (bluetoothDevice == null || this.mThreadPool.isShutdown()) {`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothBle.java:85`
  `if (!BluetoothUtil.isBleConnected(BluetoothBle.this.mContext, bluetoothDevice2)) {`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothBle.java:86`
  `BluetoothBle.this.notifyBleConnectStatus(bluetoothDevice2, 0);`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothBle.java:92`
  `if ((message.obj instanceof BluetoothDevice) && (deviceGatt = BluetoothBle.this.getDeviceGatt((bluetoothDevice = (BluetoothDevice) message.obj))) != null && ConnectUtil.isHasConnectPermission(BluetoothBle.this.mContext)) {`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothBle.java:95`
  `BluetoothBle.this.notifyBleConnectStatus(bluetoothDevice, 0);`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothBle.java:96`
  `BluetoothBle.this.removeDeviceFromRecord(bluetoothDevice, deviceGatt);`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothBle.java:100`
  `if (message.obj instanceof BluetoothDevice) {`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothBle.java:101`
  `BluetoothDevice bluetoothDevice3 = (BluetoothDevice) message.obj;`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothBle.java:269`
  `BluetoothDevice device;`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothBle.java:989`
  `handler.sendMessageDelayed(handler.obtainMessage(MSG_BLE_DISCOVER_SERVICES_CALLBACK_TIMEOUT, bluetoothDevice), m.D0);`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothBle.java:993`
  `removeDeviceFromRecord(bluetoothDevice, bluetoothGatt);`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothBle.java:999`
  `Long l = this.startTimeMap.get(bluetoothDevice.getAddress());`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothManager.java:878`
  `if (!this.mConnectedBtDevices.contains(bluetoothDevice)) {`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothManager.java:879`
  `this.mConnectedBtDevices.add(bluetoothDevice);`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothManager.java:882`
  `changeConnectedDevice(bluetoothDevice);`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothManager.java:884`
  `boolean zIsConnectedSppDevice = isConnectedSppDevice(bluetoothDevice);`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothManager.java:885`
  `if (!this.mSkipRecordSet.contains(bluetoothDevice.getAddress())) {`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothManager.java:886`
  `this.mHistoryRecordDbHelper.saveHistoryRecord(bluetoothDevice, zIsConnectedSppDevice ? 1 : 0);`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothManager.java:887`
  `if (this.mConnectedDevice != null && !BluetoothUtil.deviceEquals(this.mConnectedDevice, bluetoothDevice) && (historyRecord = getHistoryRecord(this.mConnectedDevice.getAddress())) != null) {`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothManager.java:892`
  `this.mSkipRecordSet.remove(bluetoothDevice.getAddress());`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothSpp.java:331`
  `BluetoothSocket bluetoothSocket = this.mSppSocketMap.get(bluetoothDevice.getAddress());`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothSpp.java:338`
  `JL_Log.i(TAG, ConnectUtil.formatString("-writeDataToSppDevice- send ret is OK, data [ %s ], device : %s.", CHexConverter.byte2HexStr(bArr), bluetoothDevice));`
- `sources/com/jieli/bluetooth_connect/util/BluetoothUtil.java:555`
  `int type = bluetoothDevice.getType();`
- `sources/com/jieli/bluetooth_connect/util/BluetoothUtil.java:557`
  `arrayList.add(bluetoothDevice);`
- `sources/com/jieli/jl_bt_ota/impl/BluetoothBase.java:81`
  `public boolean checkDeviceIsCertify(BluetoothDevice bluetoothDevice) {`
- `sources/com/jieli/jl_bt_ota/impl/BluetoothBase.java:82`
  `return !this.mBluetoothOption.isUseAuthDevice() || this.mDeviceStatusCache.isAuthBtDevice(bluetoothDevice);`
- `sources/com/jieli/jl_bt_ota/impl/BluetoothBase.java:96`
  `public CommandBase getCacheCommand(BluetoothDevice bluetoothDevice, BasePacket basePacket) {`
- `sources/com/jieli/jl_bt_ota/impl/BluetoothBase.java:100`
  `return this.mCommandCache.getCommand(bluetoothDevice, basePacket.getOpCode(), basePacket.getOpCodeSn());`
- `sources/com/jieli/jl_bt_ota/impl/BluetoothBase.java:103`
  `public boolean isConnectedDevice(BluetoothDevice bluetoothDevice) {`
- `sources/com/jieli/jl_bt_ota/impl/BluetoothBase.java:104`
  `return BluetoothUtil.deviceEquals(getConnectedDevice(), bluetoothDevice);`
- `sources/com/jieli/jl_bt_ota/impl/BluetoothBase.java:107`
  `protected void onA2dpStatus(BluetoothDevice bluetoothDevice, int i) {`
- `sources/com/jieli/jl_bt_ota/impl/BluetoothBase.java:108`
  `this.mBtEventCbHelper.onA2dpStatus(bluetoothDevice, i);`
- `sources/com/jieli/jl_bt_ota/impl/BluetoothBase.java:163`
  `public void removeCacheCommand(BluetoothDevice bluetoothDevice, BasePacket basePacket) {`
- `sources/com/jieli/jl_bt_ota/impl/BluetoothBase.java:164`
  `this.mCommandCache.removeCommandBase(bluetoothDevice, basePacket);`
- `sources/com/jieli/jl_bt_ota/impl/BluetoothBase.java:254`
  `commandBase.setOpCodeSn(a(bluetoothDevice));`
- `sources/com/jieli/jl_bt_ota/impl/BluetoothBase.java:255`
  `this.mCommandCache.putCommandBase(bluetoothDevice, commandBase);`
- `sources/com/jieli/jl_bt_ota/impl/BluetoothBase.java:262`
  `DataInfo callback = new DataInfo().setType(0).setDevice(bluetoothDevice).setBasePacket(basePacketConvert2BasePacket).setTimeoutMs(i2).setCallback(commandCallback);`
- `sources/com/jieli/jl_bt_ota/impl/BluetoothOTAManager.java:149`
  `public void onAuthFailed(BluetoothDevice bluetoothDevice, int i, String str) {`
- `sources/com/jieli/jl_bt_ota/impl/BluetoothOTAManager.java:150`
  `JL_Log.w(BluetoothOTAManager.this.TAG, String.format(Locale.getDefault(), "-onAuthFailed- device : %s, code : %d, message : %s", BluetoothOTAManager.this.printBtDeviceInfo(bluetoothDevice), Integer.valueOf(i), str));`

## BR070

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/com/android/billingclient/api/BillingClientImpl.java:410`
  `com.google.android.gms.internal.play_billing.zzb.zzl("BillingClient", "Got exception trying to get purchase history, try to reconnect", e2);`
- `sources/com/applovin/shadow/okhttp3/EventListener.java:16`
  `@Metadata(d1 = {"\u0000z\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004...`
- `sources/com/bumptech/glide/load/data/HttpUrlFetcher.java:145`
  `private HttpURLConnection buildAndConfigureConnection(URL url, Map<String, String> map) throws HttpException {`
- `sources/com/clj/fastble/bluetooth/BleBluetooth.java:381`
  `disconnectGatt();`
- `sources/com/clj/fastble/bluetooth/BleBluetooth.java:396`
  `disconnectGatt();`
- `sources/com/clj/fastble/bluetooth/BleBluetooth.java:401`
  `disconnectGatt();`
- `sources/com/clj/fastble/bluetooth/BleBluetooth.java:404`
  `removeConnectGattCallback();`
- `sources/com/clj/fastble/bluetooth/BleBluetooth.java:412`
  `public synchronized void disconnectGatt() {`
- `sources/com/clj/fastble/bluetooth/BleBluetooth.java:451`
  `BleBluetooth.this.disconnectGatt();`
- `sources/com/clj/fastble/bluetooth/BleBluetooth.java:454`
  `if (BleBluetooth.this.connectRetryCount >= BleManager.getInstance().getReConnectCount()) {`
- `sources/com/clj/fastble/bluetooth/BleBluetooth.java:466`
  `BleBluetooth.this.mainHandler.sendMessageDelayed(messageObtainMessage, BleManager.getInstance().getReConnectInterval());`
- `sources/com/clj/fastble/bluetooth/BleBluetooth.java:504`
  `BleBluetooth.this.disconnectGatt();`
- `sources/com/clj/fastble/bluetooth/BleBluetooth.java:524`
  `BleBluetooth.this.disconnectGatt();`
- `sources/com/google/android/gms/internal/ads/zzbhe.java:1804`
  `zzpz = new zzbgq(1, "gads:preconnect_initialization_task_enabled", false, false);`
- `sources/com/google/android/gms/internal/ads/zzbhe.java:1805`
  `zzpA = new zzbgu(1, "gads:preconnect_urls", "https://googleads.g.doubleclick.net,https://pubads.g.doubleclick.net", "https://googleads.g.doubleclick.net,https://pubads.g.doubleclick.net");`
- `sources/com/google/android/gms/internal/ads/zzbhe.java:1806`
  `zzpB = new zzbgq(1, "gads:preconnect_csi_logging:enabled", false, false);`
- `sources/com/google/android/gms/internal/ads/zzbhe.java:1807`
  `zzpC = new zzbgq(1, "gads:preconnect_exception_reporting:enabled", false, false);`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothBle.java:1002`
  `int i3 = this.reconnectCount + 1;`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothManager.java:28`
  `import com.jieli.bluetooth_connect.tool.ReConnectHelper;`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothManager.java:46`
  `private static final int MSG_RECONNECT_DEVICE = 4114;`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothManager.java:64`
  `private final ReConnectHelper mReConnectHelper;`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothManager.java:242`
  `if ((!zIsConnectedDevice || BluetoothManager.this.mBluetoothOption.isReconnect()) && zIsConnectedDevice) {`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothManager.java:329`
  `this.mReConnectHelper = new ReConnectHelper(context, this);`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothManager.java:744`
  `public boolean isReconnectDevice() {`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothManager.java:745`
  `return this.mReConnectHelper.isReconnecting();`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothManager.java:756`
  `this.mReConnectHelper.reconnectHistory(it.next());`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothManager.java:773`
  `this.mReConnectHelper.reconnectDevice(mappedAddress, i, onHistoryRecordCallback);`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothManager.java:777`
  `public void stopReconnect() {`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothManager.java:778`
  `this.mReConnectHelper.stopReconnect();`
- `sources/com/jieli/bluetooth_connect/impl/BluetoothManager.java:810`
  `this.mReConnectHelper.destroy();`
- `sources/com/jieli/bluetooth_connect/interfaces/IBluetoothOperation.java:91`
  `boolean isReconnectDevice();`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:127`
  `reconnectTaskFindReconnectTask = ReConnectHelper.this.findReconnectTask(bleScanMessage.getOtaBleAddress());`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:128`
  `if (reconnectTaskFindReconnectTask == null) {`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:129`
  `reconnectTaskFindReconnectTask = ReConnectHelper.this.findReconnectTask(address);`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:131`
  `if (reconnectTaskFindReconnectTask != null) {`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:132`
  `if (reconnectTaskFindReconnectTask.getConnectWay() != 0) {`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:133`
  `reconnectTaskFindReconnectTask.setConnectWay(0);`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:135`
  `HistoryRecord historyRecord = ReConnectHelper.this.mBtOp.getHistoryRecord(address);`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:138`
  `((BluetoothManager) ReConnectHelper.this.mBtOp).getHistoryRecordHelper().updateHistoryRecord(historyRecord);`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:144`
  `ReconnectTask reconnectTaskFindReconnectTask2 = ReConnectHelper.this.findReconnectTask(address);`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:145`
  `if (reconnectTaskFindReconnectTask2 != null) {`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:146`
  `bluetoothDevice = ReConnectHelper.this.findTargetDevice(bluetoothDevice, bleScanMessage, reconnectTaskFindReconnectTask2.getConnectWay());`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:187`
  `public boolean isReconnecting() {`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:188`
  `return this.mHandler.hasMessages(MSG_RECONNECT_TIMEOUT);`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:191`
  `public boolean isReconnectDev(BluetoothDevice bluetoothDevice) {`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:192`
  `return (bluetoothDevice == null || findReconnectTask(bluetoothDevice.getAddress()) == null) ? false : true;`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:195`
  `public void reconnectDevice(String str, int i, OnHistoryRecordCallback onHistoryRecordCallback) {`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:196`
  `reconnectDevice(str, i, 0, onHistoryRecordCallback);`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:199`
  `public void reconnectDevice(String str, int i, int i2, OnHistoryRecordCallback onHistoryRecordCallback) {`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:205`
  `ReconnectTask reconnectTask = new ReconnectTask(str);`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:206`
  `reconnectTask.setTaskType(1);`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:207`
  `reconnectTask.setConnectWay(i);`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:208`
  `reconnectTask.setTaskTimeout(i2);`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:209`
  `reconnectTask.setCallback(onHistoryRecordCallback);`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:210`
  `addTask(reconnectTask);`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:214`
  `public void reconnectHistory(HistoryRecord historyRecord) {`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:223`
  `ReconnectTask reconnectTask = new ReconnectTask(mappedAddress);`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:224`
  `reconnectTask.setConnectWay(i);`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:225`
  `reconnectTask.setTaskType(2);`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:226`
  `addTask(reconnectTask);`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:229`
  `public void stopReconnect() {`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:397`
  `private void removeTask(ReconnectTask reconnectTask, boolean z) {`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:398`
  `boolean zRemove = this.mTaskList.remove(reconnectTask);`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:399`
  `JL_Log.w(TAG, "removeTask >>> " + reconnectTask + ", ret = " + zRemove + ", result = " + z);`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:401`
  `if (reconnectTask.getCallback() != null) {`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:403`
  `reconnectTask.getCallback().onSuccess(this.mBtOp.getHistoryRecord(reconnectTask.getAddress()));`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:405`
  `reconnectTask.getCallback().onFailed(9, ConnectUtil.formatString("Connect device[%s] timeout.", reconnectTask.getAddress()));`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:408`
  `this.mHandler.removeMessages(reconnectTask.getTaskId());`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:410`
  `postReconnectTaskMsg(0L);`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:439`
  `public ReconnectTask findReconnectTask(String str) {`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:443`
  `for (ReconnectTask reconnectTask : new ArrayList(this.mTaskList)) {`
- `sources/com/jieli/bluetooth_connect/tool/ReConnectHelper.java:499`
  `public static class ReconnectTask {`
- `sources/com/jieli/jl_bt_ota/impl/BluetoothOTAManager.java:152`
  `if (BluetoothOTAManager.this.w.isDeviceReconnecting()) {`
- `sources/com/jieli/multidevice/ReConnectHelper.java:29`
  `/* JADX INFO: compiled from: ReConnectHelper.kt */`
- `sources/com/jieli/multidevice/ReConnectHelper.java:31`
  `@Metadata(d1 = {"\u0000T\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010%\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010!\n\u0002\u0018\u0002\n...`
- `sources/com/jieli/multidevice/ReConnectHelper.java:32`
  `public final class ReConnectHelper {`
- `sources/com/jieli/multidevice/ReConnectHelper.java:35`
  `private static final int MSG_RECONNECT_TIMEOUT = 1;`
- `sources/com/jieli/multidevice/ReConnectHelper.java:41`
  `private final List<ReconnectParam> mParams;`
- `sources/com/jieli/multidevice/ReConnectHelper.java:43`
  `private static final String TAG = "ReConnectHelper";`
- `sources/com/jieli/multidevice/ReConnectHelper.java:44`
  `private static final long RECONNECT_TIMEOUT = DeviceReConnectManager.RECONNECT_TIMEOUT;`

## BR071

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:149`
  `android:allowBackup="true"`

## BR072

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `resources/AndroidManifest.xml:59`
  `<package android:name="com.tencent.mobileqq"/>`
- `sources/com/alibaba/fastjson/util/RyuFloat.java:4`
  `import com.tencent.mm.opensdk.constants.Build;`
- `sources/com/mbridge/msdk/click/a.java:908`
  `Class<?> cls = Class.forName("com.tencent.mm.opensdk.modelbiz.WXLaunchMiniProgram$Req");`
- `sources/com/mbridge/msdk/click/a.java:913`
  `Class.forName("com.tencent.mm.opensdk.openapi.IWXAPI").getMethod("sendReq", Class.forName("com.tencent.mm.opensdk.modelbase.BaseReq")).invoke(objD, objNewInstance);`
- `sources/com/mbridge/msdk/foundation/tools/u0.java:343`
  `return ((Integer) Class.forName("com.tencent.mm.opensdk.openapi.IWXAPI").getMethod("getWXAppSupportAPI", new Class[0]).invoke(l0.d(str), new Object[0])).intValue();`
- `sources/com/mbridge/msdk/foundation/tools/u0.java:355`
  `return Class.forName("com.tencent.mm.opensdk.openapi.WXAPIFactory").getMethod("createWXAPI", Context.class, String.class).invoke(null, com.mbridge.msdk.foundation.controller.c.m().d(), str);`
- `sources/com/mbridge/msdk/foundation/tools/u0.java:743`
  `Class.forName("com.tencent.mm.opensdk.openapi.WXAPIFactory");`
- `sources/com/mbridge/msdk/foundation/tools/u0.java:744`
  `Class.forName("com.tencent.mm.opensdk.modelbiz.WXLaunchMiniProgram");`
- `sources/com/mbridge/msdk/foundation/tools/u0.java:1025`
  `return ((Integer) Class.forName("com.tencent.mm.opensdk.constants.Build").getField("SDK_INT").get(null)).intValue();`
- `sources/com/realsil/sdk/support/utilities/PluginsManager.java:6`
  `import com.tencent.bugly.crashreport.CrashReport;`
- `sources/com/smartdigimkt/n8/c.java:892`
  `Class.forName("com.tencent.mm.opensdk.openapi.WXAPIFactory");`
- `sources/com/smartdigimkt/n8/c.java:893`
  `Class.forName("com.tencent.mm.opensdk.modelbiz.WXLaunchMiniProgram");`
- `sources/com/smartdigimkt/n8/c.java:1076`
  `return Class.forName("com.tencent.mm.opensdk.openapi.WXAPIFactory").getMethod("createWXAPI", Context.class, String.class).invoke(null, com.smartdigimkt.m6.b.p().k(), str);`
- `sources/com/smartdigimkt/n8/c.java:1088`
  `I = ((Integer) Class.forName("com.tencent.mm.opensdk.openapi.IWXAPI").getMethod("getWXAppSupportAPI", null).invoke(e(str), null)).intValue();`
- `sources/com/smartdigimkt/n8/c.java:1114`
  `H = ((Integer) Class.forName("com.tencent.mm.opensdk.constants.Build").getField("SDK_INT").get(null)).intValue();`
- `sources/com/smartdigimkt/n8/q.java:77`
  `Class.forName("com.tencent.mm.opensdk.openapi.WXAPIFactory");`
- `sources/com/smartdigimkt/q3/d.java:377`
  `Class<?> cls = Class.forName("com.tencent.mm.opensdk.modelbiz.WXLaunchMiniProgram$Req");`
- `sources/com/smartdigimkt/q3/d.java:384`
  `Class.forName("com.tencent.mm.opensdk.openapi.IWXAPI").getMethod("sendReq", Class.forName("com.tencent.mm.opensdk.modelbase.BaseReq")).invoke(objE, objNewInstance);`
- `sources/com/tencent/mm/opensdk/R.java:1`
  `package com.tencent.mm.opensdk;`
- `sources/com/tencent/mm/opensdk/channel/MMessageActV2.java:1`
  `package com.tencent.mm.opensdk.channel;`
- `sources/com/tencent/mm/opensdk/channel/MMessageActV2.java:8`
  `import com.tencent.mm.opensdk.channel.a.a;`
- `sources/com/tencent/mm/opensdk/channel/MMessageActV2.java:9`
  `import com.tencent.mm.opensdk.constants.Build;`
- `sources/com/tencent/mm/opensdk/channel/MMessageActV2.java:10`
  `import com.tencent.mm.opensdk.constants.ConstantsAPI;`
- `sources/com/tencent/mm/opensdk/channel/MMessageActV2.java:11`
  `import com.tencent.mm.opensdk.utils.Log;`
- `sources/com/tencent/mm/opensdk/channel/MMessageActV2.java:12`
  `import com.tencent.mm.opensdk.utils.b;`
- `sources/com/tencent/mm/opensdk/channel/MMessageActV2.java:88`
  `PendingIntent.getActivity(context, 3, intent, 134217728).send(context, 4, null, new PendingIntent.OnFinished() { // from class: com.tencent.mm.opensdk.channel.MMessageActV2.1`
- `sources/com/tencent/mm/opensdk/channel/a/a.java:1`
  `package com.tencent.mm.opensdk.channel.a;`
- `sources/com/tencent/mm/opensdk/channel/a/a.java:6`
  `import com.tencent.mm.opensdk.constants.Build;`
- `sources/com/tencent/mm/opensdk/channel/a/a.java:7`
  `import com.tencent.mm.opensdk.constants.ConstantsAPI;`
- `sources/com/tencent/mm/opensdk/channel/a/a.java:8`
  `import com.tencent.mm.opensdk.utils.Log;`
- `sources/com/tencent/mm/opensdk/channel/a/a.java:9`
  `import com.tencent.mm.opensdk.utils.b;`
- `sources/com/tencent/mm/opensdk/channel/a/a.java:15`
  `/* JADX INFO: renamed from: com.tencent.mm.opensdk.channel.a.a$a, reason: collision with other inner class name */`
- `sources/com/tencent/mm/opensdk/channel/a/a.java:135`
  `throw new UnsupportedOperationException("Method not decompiled: com.tencent.mm.opensdk.channel.a.a.a(java.lang.String, int):byte[]");`
- `sources/com/tencent/mm/opensdk/constants/Build.java:1`
  `package com.tencent.mm.opensdk.constants;`
- `sources/com/tencent/mm/opensdk/constants/ConstantsAPI.java:1`
  `package com.tencent.mm.opensdk.constants;`
- `sources/com/tencent/mm/opensdk/diffdev/DiffDevOAuthFactory.java:1`
  `package com.tencent.mm.opensdk.diffdev;`
- `sources/com/tencent/mm/opensdk/diffdev/DiffDevOAuthFactory.java:3`
  `import com.tencent.mm.opensdk.diffdev.a.a;`
- `sources/com/tencent/mm/opensdk/diffdev/DiffDevOAuthFactory.java:4`
  `import com.tencent.mm.opensdk.utils.Log;`
- `sources/com/tencent/mm/opensdk/diffdev/IDiffDevOAuth.java:1`
  `package com.tencent.mm.opensdk.diffdev;`
- `sources/com/tencent/mm/opensdk/diffdev/OAuthErrCode.java:1`
  `package com.tencent.mm.opensdk.diffdev;`
- `sources/com/tencent/mm/opensdk/diffdev/OAuthListener.java:1`
  `package com.tencent.mm.opensdk.diffdev;`
- `sources/com/tencent/mm/opensdk/diffdev/a/a.java:1`
  `package com.tencent.mm.opensdk.diffdev.a;`
- `sources/com/tencent/mm/opensdk/diffdev/a/a.java:6`
  `import com.tencent.mm.opensdk.diffdev.IDiffDevOAuth;`
- `sources/com/tencent/mm/opensdk/diffdev/a/a.java:7`
  `import com.tencent.mm.opensdk.diffdev.OAuthErrCode;`
- `sources/com/tencent/mm/opensdk/diffdev/a/a.java:8`
  `import com.tencent.mm.opensdk.diffdev.OAuthListener;`
- `sources/com/tencent/mm/opensdk/diffdev/a/a.java:9`
  `import com.tencent.mm.opensdk.utils.Log;`
- `sources/com/tencent/mm/opensdk/diffdev/a/a.java:23`
  `/* JADX INFO: renamed from: com.tencent.mm.opensdk.diffdev.a.a$a, reason: collision with other inner class name */`
- `sources/com/tencent/mm/opensdk/diffdev/a/a.java:26`
  `/* JADX INFO: renamed from: com.tencent.mm.opensdk.diffdev.a.a$a$a, reason: collision with other inner class name */`
- `sources/com/tencent/mm/opensdk/diffdev/a/a.java:45`
  `@Override // com.tencent.mm.opensdk.diffdev.OAuthListener`
- `sources/com/tencent/mm/opensdk/diffdev/a/a.java:57`
  `@Override // com.tencent.mm.opensdk.diffdev.OAuthListener`
- `sources/com/tencent/mm/opensdk/diffdev/a/a.java:68`
  `@Override // com.tencent.mm.opensdk.diffdev.OAuthListener`
- `sources/com/tencent/mm/opensdk/diffdev/a/a.java:77`
  `@Override // com.tencent.mm.opensdk.diffdev.IDiffDevOAuth`
- `sources/com/tencent/mm/opensdk/diffdev/a/a.java:85`
  `@Override // com.tencent.mm.opensdk.diffdev.IDiffDevOAuth`
- `sources/com/tencent/mm/opensdk/diffdev/a/a.java:108`
  `@Override // com.tencent.mm.opensdk.diffdev.IDiffDevOAuth`
- `sources/com/tencent/mm/opensdk/diffdev/a/a.java:115`
  `@Override // com.tencent.mm.opensdk.diffdev.IDiffDevOAuth`
- `sources/com/tencent/mm/opensdk/diffdev/a/a.java:120`
  `@Override // com.tencent.mm.opensdk.diffdev.IDiffDevOAuth`
- `sources/com/tencent/mm/opensdk/diffdev/a/a.java:125`
  `@Override // com.tencent.mm.opensdk.diffdev.IDiffDevOAuth`
- `sources/com/tencent/mm/opensdk/diffdev/a/b.java:1`
  `package com.tencent.mm.opensdk.diffdev.a;`
- `sources/com/tencent/mm/opensdk/diffdev/a/b.java:5`
  `import com.tencent.mm.opensdk.diffdev.OAuthErrCode;`
- `sources/com/tencent/mm/opensdk/diffdev/a/b.java:6`
  `import com.tencent.mm.opensdk.diffdev.OAuthListener;`
- `sources/com/tencent/mm/opensdk/diffdev/a/b.java:7`
  `import com.tencent.mm.opensdk.utils.Log;`
- `sources/com/tencent/mm/opensdk/diffdev/a/b.java:109`
  `byte[] bArrA = com.tencent.mm.opensdk.channel.a.a.a(str, 60000);`
- `sources/com/tencent/mm/opensdk/diffdev/a/c.java:1`
  `package com.tencent.mm.opensdk.diffdev.a;`
- `sources/com/tencent/mm/opensdk/diffdev/a/c.java:4`
  `import com.tencent.mm.opensdk.diffdev.OAuthErrCode;`
- `sources/com/tencent/mm/opensdk/diffdev/a/c.java:5`
  `import com.tencent.mm.opensdk.diffdev.OAuthListener;`
- `sources/com/tencent/mm/opensdk/diffdev/a/c.java:41`
  `protected com.tencent.mm.opensdk.diffdev.a.c.a doInBackground(java.lang.Void[] r13) throws java.lang.Throwable {`
- `sources/com/tencent/mm/opensdk/diffdev/a/c.java:46`
  `throw new UnsupportedOperationException("Method not decompiled: com.tencent.mm.opensdk.diffdev.a.c.doInBackground(java.lang.Object[]):java.lang.Object");`
- `sources/com/tencent/mm/opensdk/diffdev/a/d.java:1`
  `package com.tencent.mm.opensdk.diffdev.a;`
- `sources/com/tencent/mm/opensdk/modelbase/BaseReq.java:1`
  `package com.tencent.mm.opensdk.modelbase;`
- `sources/com/tencent/mm/opensdk/modelbase/BaseReq.java:4`
  `import com.tencent.mm.opensdk.channel.a.a;`
- `sources/com/tencent/mm/opensdk/modelbase/BaseResp.java:1`
  `package com.tencent.mm.opensdk.modelbase;`
- `sources/com/tencent/mm/opensdk/modelbiz/AddCardToWXCardPackage.java:1`
  `package com.tencent.mm.opensdk.modelbiz;`
- `sources/com/tencent/mm/opensdk/modelbiz/AddCardToWXCardPackage.java:4`
  `import com.tencent.mm.opensdk.modelbase.BaseReq;`
- `sources/com/tencent/mm/opensdk/modelbiz/AddCardToWXCardPackage.java:5`
  `import com.tencent.mm.opensdk.modelbase.BaseResp;`
- `sources/com/tencent/mm/opensdk/modelbiz/AddCardToWXCardPackage.java:6`
  `import com.tencent.mm.opensdk.utils.Log;`
- `sources/com/tencent/mm/opensdk/modelbiz/AddCardToWXCardPackage.java:21`
  `@Override // com.tencent.mm.opensdk.modelbase.BaseReq`
- `sources/com/tencent/mm/opensdk/modelbiz/AddCardToWXCardPackage.java:37`
  `@Override // com.tencent.mm.opensdk.modelbase.BaseReq`
- `sources/com/tencent/mm/opensdk/modelbiz/AddCardToWXCardPackage.java:42`
  `@Override // com.tencent.mm.opensdk.modelbase.BaseReq`
- `sources/com/tencent/mm/opensdk/modelbiz/AddCardToWXCardPackage.java:77`
  `@Override // com.tencent.mm.opensdk.modelbase.BaseResp`
- `sources/com/tencent/mm/opensdk/modelbiz/AddCardToWXCardPackage.java:83`
  `@Override // com.tencent.mm.opensdk.modelbase.BaseResp`

## BR073

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `resources/com/androidquery/auth/BasicHandle.java:53`
  `Uri uri = Uri.parse(cb.getUrl());`
- `resources/com/androidquery/auth/BasicHandle.java:69`
  `Uri uri = Uri.parse(cb.getUrl());`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:456`
  `* Set the encoding used to parse the response.`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:715`
  `return (T) BitmapFactory.decodeByteArray(data, 0, data.length);`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:245`
  `private static Bitmap decode(String path, byte[] data, BitmapFactory.Options options, boolean rotate){`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:252`
  `result = decodeFile(path, options, rotate);`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:256`
  `result = BitmapFactory.decodeByteArray(data, 0, data.length, options);`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:260`
  `if(result == null && options != null && !options.inJustDecodeBounds){`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:261`
  `AQUtility.debug("decode image failed", path);`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:393`
  `info.inJustDecodeBounds = true;`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:395`
  `decode(path, data, info, rotate);`
- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:693`
  `public void restoreToolbarHierarchyState(SparseArray<Parcelable> sparseArray) {`
- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:695`
  `this.mDecorToolbar.restoreHierarchyState(sparseArray);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:552`
  `SparseArray sparseParcelableArray = extras.getSparseParcelableArray(EXTRA_COLOR_SCHEME_PARAMS);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:553`
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
- `sources/androidx/camera/camera2/internal/SupportedSurfaceCombination.java:867`
  `int i = Integer.parseInt(this.mCameraId);`
- `sources/androidx/camera/core/imagecapture/JpegBytes2CroppedBitmap.java:29`
  `return BitmapRegionDecoder.newInstance(bArr, 0, bArr.length, false).decodeRegion(rect, new BitmapFactory.Options());`
- `sources/androidx/camera/core/imagecapture/JpegBytes2CroppedBitmap.java:31`
  `throw new ImageCaptureException(1, "Failed to decode JPEG.", e);`
- `sources/androidx/camera/core/imagecapture/JpegBytes2Disk.java:65`
  `fileOutputStream.write(bArr, 0, new InvalidJpegDataParser().getValidDataLength(bArr));`
- `sources/androidx/camera/core/impl/CaptureConfig.java:31`
  `public interface OptionUnpacker {`
- `sources/androidx/camera/core/impl/utils/Exif.java:14`
  `import java.text.ParseException;`
- `sources/androidx/camera/core/impl/utils/ExifAttribute.java:163`
  `return Double.parseDouble((String) value);`
- `sources/androidx/camera/core/impl/utils/ExifAttribute.java:200`
  `return Integer.parseInt((String) value);`
- `sources/androidx/camera/core/impl/utils/ExifData.java:357`
  `iArr[i8] = Integer.parseInt(strArrSplit[i8]);`
- `sources/androidx/camera/core/impl/utils/ExifData.java:367`
  `jArr[i9] = Long.parseLong(strArrSplit2[i9]);`
- `sources/androidx/camera/core/impl/utils/ExifData.java:393`
  `iArr2[i11] = Integer.parseInt(strArrSplit5[i11]);`
- `sources/androidx/camera/core/impl/utils/ExifData.java:405`
  `longRationalArr2[i12] = new LongRational((long) Double.parseDouble(strArrSplit7[i6]), (long) Double.parseDouble(strArrSplit7[i5]));`
- `sources/androidx/camera/core/impl/utils/ExifData.java:419`
  `dArr[i13] = Double.parseDouble(strArrSplit8[i13]);`
- `sources/androidx/camera/core/impl/utils/ExifData.java:522`
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
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:261`
  `Bitmap bitmapDecodeByteArray = BitmapFactory.decodeByteArray(bArrJpegImageToJpegByteArray, 0, bArrJpegImageToJpegByteArray.length, null);`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:262`
  `if (bitmapDecodeByteArray != null) {`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:263`
  `return bitmapDecodeByteArray;`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:265`
  `throw new UnsupportedOperationException("Decode jpeg byte array failed");`
- `sources/androidx/collection/LongSparseArrayKt.java:14`
  `/* JADX INFO: compiled from: LongSparseArray.kt */`
- `sources/androidx/collection/LongSparseArrayKt.java:16`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000D\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\t\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002...`
- `sources/androidx/collection/LongSparseArrayKt.java:17`
  `public final class LongSparseArrayKt {`
- `sources/androidx/collection/LongSparseArrayKt.java:18`
  `public static final <T> int getSize(LongSparseArray<T> receiver$0) {`
- `sources/androidx/collection/LongSparseArrayKt.java:54`
  `public static final <T> boolean isNotEmpty(LongSparseArray<T> receiver$0) {`
- `sources/androidx/collection/LongSparseArrayKt.java:60`
  `public static final <T> boolean remove(LongSparseArray<T> receiver$0, long j, T t) {`
- `sources/androidx/collection/SparseArrayKt.java:14`
  `/* JADX INFO: compiled from: SparseArray.kt */`
- `sources/androidx/collection/SparseArrayKt.java:16`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000@\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0007...`
- `sources/androidx/collection/SparseArrayKt.java:17`
  `public final class SparseArrayKt {`
- `sources/androidx/collection/SparseArrayKt.java:18`
  `public static final <T> int getSize(SparseArrayCompat<T> receiver$0) {`
- `sources/androidx/collection/SparseArrayKt.java:54`
  `public static final <T> boolean isNotEmpty(SparseArrayCompat<T> receiver$0) {`
- `sources/androidx/collection/SparseArrayKt.java:60`
  `public static final <T> boolean remove(SparseArrayCompat<T> receiver$0, int i, T t) {`
- `sources/androidx/constraintlayout/core/dsl/Ref.java:75`
  `public static float parseFloat(Object obj) {`
- `sources/androidx/constraintlayout/core/state/ConstraintSetParser.java:151`
  `@Override // androidx.constraintlayout.core.state.ConstraintSetParser.GeneratedValue`
- `sources/androidx/constraintlayout/core/state/ConstraintSetParser.java:976`
  `constraintReference.setHeight(parseDimension(cLObject, str, state, state.getDpToPixel()));`
- `sources/androidx/constraintlayout/core/state/ConstraintSetParser.java:979`
  `parseMotionProperties(cLObject.get(str), constraintReference);`
- `sources/androidx/constraintlayout/core/state/ConstraintSetParser.java:1013`
  `constraintReference.setWidth(parseDimension(cLObject, str, state, state.getDpToPixel()));`
- `sources/androidx/constraintlayout/core/state/ConstraintSetParser.java:1051`
  `static void parseWidget(State state, LayoutVariables layoutVariables, ConstraintReference constraintReference, CLObject cLObject) throws CLParsingException {`
- `sources/androidx/constraintlayout/core/utils/GridCore.java:340`
  `private float[] parseWeights(int i, String str) {`
- `sources/androidx/constraintlayout/core/utils/GridCore.java:425`
  `float[] weights = parseWeights(this.mColumns, this.mColumnWeights);`
- `sources/androidx/constraintlayout/core/utils/GridCore.java:471`
  `float[] weights = parseWeights(this.mRows, this.mRowWeights);`
- `sources/androidx/constraintlayout/helper/widget/Grid.java:223`
  `private float[] parseWeights(int i, String str) {`
- `sources/androidx/constraintlayout/helper/widget/Grid.java:394`
  `float[] weights = parseWeights(this.mColumns, this.mStrColumnWeights);`
- `sources/androidx/constraintlayout/helper/widget/Grid.java:444`
  `float[] weights = parseWeights(this.mRows, this.mStrRowWeights);`
- `sources/androidx/constraintlayout/motion/utils/ViewSpline.java:164`
  `SparseArray<ConstraintAttribute> mConstraintAttributeList;`

## BR074

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `resources/com/androidquery/AbstractAQuery.java:2413`
  `* The temp file will be deleted when AQUtility.cleanCacheAsync is invoked, or the file can be explicitly deleted after use.`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:582`
  `AQUtility.report(e);`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:793`
  `AQUtility.report(e);`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:890`
  `AQUtility.report(e);`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:950`
  `async((Context) act);`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:1239`
  `AQUtility.report(e);`
- `resources/com/androidquery/callback/AjaxStatus.java:161`
  `* Close any opened inputstream associated with the response. Call this method when finish parsing the response of a synchronous call.`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:292`
  `AQUtility.report(e);`
- `resources/com/androidquery/callback/LocationAjaxCallback.java:172`
  `// if this loc is network and there's already an recent async gps update`
- `resources/com/androidquery/util/AQUtility.java:436`
  `AQUtility.report(e);`
- `resources/com/androidquery/util/AQUtility.java:637`
  `AQUtility.report(e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1490`
  `synchronized (mediaControllerImplApi21.mLock) {`
- `sources/android/support/v4/os/ResultReceiver.java:93`
  `synchronized (this) {`
- `sources/androidx/activity/ComponentActivity$activityResultRegistry$1.java:33`
  `final ActivityResultContract.SynchronousResult<O> synchronousResult = contract.getSynchronousResult(componentActivity2, input);`
- `sources/androidx/activity/ComponentActivity$activityResultRegistry$1.java:34`
  `if (synchronousResult != null) {`
- `sources/androidx/activity/ComponentActivity$activityResultRegistry$1.java:38`
  `ComponentActivity$activityResultRegistry$1.onLaunch$lambda$0(this.f$0, requestCode, synchronousResult);`
- `sources/androidx/activity/ComponentActivity$activityResultRegistry$1.java:86`
  `public static final void onLaunch$lambda$0(ComponentActivity$activityResultRegistry$1 this$0, int i, ActivityResultContract.SynchronousResult synchronousResult) {`
- `sources/androidx/activity/ComponentActivity$activityResultRegistry$1.java:88`
  `this$0.dispatchResult(i, synchronousResult.getValue());`
- `sources/androidx/activity/ComponentActivity$onBackPressedDispatcher$2.java:55`
  `if (!Intrinsics.areEqual(e.getMessage(), "Can not perform this action after onSaveInstanceState")) {`
- `sources/androidx/activity/ComponentActivity.java:81`
  `@Metadata(d1 = {"\u0000â\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u...`
- `sources/androidx/activity/ComponentActivity.java:82`
  `public class ComponentActivity extends androidx.core.app.ComponentActivity implements ContextAware, LifecycleOwner, ViewModelStoreOwner, HasDefaultViewModelProviderFactory, SavedStateRegistryOwner, OnBackPressedDispatcherOwner, ActivityResultRegistryOwner, ActivityResultCaller, OnConfigurationChange...`
- `sources/androidx/activity/ComponentActivity.java:146`
  `private static /* synthetic */ void getSavedStateRegistryController$annotations() {`
- `sources/androidx/activity/ComponentActivity.java:194`
  `componentActivity2.reportFullyDrawn();`
- `sources/androidx/activity/ComponentActivity.java:231`
  `savedStateRegistryControllerCreate.performAttach();`
- `sources/androidx/activity/ComponentActivity.java:232`
  `SavedStateHandleSupport.enableSavedStateHandles(componentActivity);`
- `sources/androidx/activity/ComponentActivity.java:233`
  `getSavedStateRegistry().registerSavedStateProvider(ACTIVITY_RESULT_TAG, new SavedStateRegistry.SavedStateProvider() { // from class: androidx.activity.ComponentActivity$$ExternalSyntheticLambda4`
- `sources/androidx/activity/ComponentActivity.java:234`
  `@Override // androidx.savedstate.SavedStateRegistry.SavedStateProvider`
- `sources/androidx/activity/ComponentActivity.java:235`
  `public final Bundle saveState() {`
- `sources/androidx/activity/ComponentActivity.java:303`
  `this$0.activityResultRegistry.onSaveInstanceState(bundle);`
- `sources/androidx/activity/ComponentActivity.java:311`
  `Bundle bundleConsumeRestoredStateForKey = this$0.getSavedStateRegistry().consumeRestoredStateForKey(ACTIVITY_RESULT_TAG);`
- `sources/androidx/activity/ComponentActivity.java:605`
  `@Override // androidx.savedstate.SavedStateRegistryOwner`
- `sources/androidx/activity/ComponentActivity.java:606`
  `public final SavedStateRegistry getSavedStateRegistry() {`
- `sources/androidx/activity/ComponentActivity.java:607`
  `return this.savedStateRegistryController.getSavedStateRegistry();`
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
- `sources/androidx/activity/result/ActivityResultRegistry.java:29`
  `@Metadata(d1 = {"\u0000r\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010%\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0010!\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0002\b\u0003\n...`
- `sources/androidx/activity/result/ActivityResultRegistry.java:200`
  `public final void onSaveInstanceState(Bundle outState) {`
- `sources/androidx/activity/result/ActivityResultRegistry.java:208`
  `public final void onRestoreInstanceState(Bundle savedInstanceState) {`
- `sources/androidx/activity/result/ActivityResultRegistry.java:209`
  `if (savedInstanceState == null) {`
- `sources/androidx/activity/result/ActivityResultRegistry.java:217`
  `ArrayList<String> stringArrayList2 = savedInstanceState.getStringArrayList(KEY_COMPONENT_ACTIVITY_LAUNCHED_KEYS);`
- `sources/androidx/activity/result/ActivityResultRegistry.java:221`
  `Bundle bundle = savedInstanceState.getBundle(KEY_COMPONENT_ACTIVITY_PENDING_RESULTS);`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:11`
  `@Metadata(d1 = {"\u0000.\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\b\u0004\b&\u0018\u0000*\u0004\b\u0000\u0010\u0001*\u0004\b\u0001\u0010\u00022\u...`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:15`
  `public SynchronousResult<O> getSynchronousResult(Context context, I input) {`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:23`
  `@Metadata(d1 = {"\u0000\u000e\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0000\n\u0002\b\u0006\u0018\u0000*\u0004\b\u0002\u0010\u00012\u00020\u0002B\r\u0012\u0006\u0010\u0003\u001a\u00028\u0002¢\u0006\u0002\u0010\u0004R\u0013\u0010\u0003\u001a\u00028\u0002¢\u0006\n\n\u0002\u0010\u0007\u001a\u0004\b\u...`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:24`
  `public static final class SynchronousResult<T> {`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:31`
  `public SynchronousResult(T t) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:90`
  `@Metadata(d1 = {"\u0000>\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0011\n\u0002\u0010\u000e\n\u0002\u0010$\n\u0002\u0010\u000b\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:125`
  `public ActivityResultContract.SynchronousResult<Map<String, Boolean>> getSynchronousResult(Context context, String[] input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:129`
  `return new ActivityResultContract.SynchronousResult<>(MapsKt.emptyMap());`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:141`
  `return new ActivityResultContract.SynchronousResult<>(linkedHashMap);`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:166`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\u0018\u00002\u000e\u0012\u0004\u0012\u00020\u00...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:201`
  `public ActivityResultContract.SynchronousResult<Boolean> getSynchronousResult(Context context, String input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:205`
  `return new ActivityResultContract.SynchronousResult<>(true);`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:212`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0016\u0018\u00002\u0012\u0012\u0006\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:215`
  `public final ActivityResultContract.SynchronousResult<Bitmap> getSynchronousResult(Context context, Void input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:240`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\b\u0016\u0018\u00002\u000e\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:243`
  `public final ActivityResultContract.SynchronousResult<Boolean> getSynchronousResult(Context context, Uri input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:266`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0017\u0018\u00002\u0010\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:270`
  `public final ActivityResultContract.SynchronousResult<Bitmap> getSynchronousResult(Context context, Uri input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:299`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\b\u0016\u0018\u00002\u000e\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:302`
  `public final ActivityResultContract.SynchronousResult<Boolean> getSynchronousResult(Context context, Uri input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:349`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0016\u0018\u00002\u0010\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:352`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(Context context, String input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:381`
  `@Metadata(d1 = {"\u0000:\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\b\u0016\u001...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:388`
  `public final ActivityResultContract.SynchronousResult<List<Uri>> getSynchronousResult(Context context, String input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:448`
  `@Metadata(d1 = {"\u00006\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0011\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\b\u0002\b\u0016\u0018\u00002\u0016\...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:451`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(Context context, String[] input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:480`
  `@Metadata(d1 = {"\u0000>\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0011\n\u0002\u0010\u000e\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:483`
  `public final ActivityResultContract.SynchronousResult<List<Uri>> getSynchronousResult(Context context, String[] input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:509`
  `@Metadata(d1 = {"\u0000.\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0017\u0018\u00002\u0012\u0012\u0006\u0012\u0004\u0018\u00010\u00...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:512`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(Context context, Uri input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:541`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0016\u0018\u00002\u0010\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:546`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(Context context, String input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:585`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\b\b\u0016\u0018\u0000 \u00102\u0010\u0012\u0004\u0012...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:612`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(Context context, PickVisualMediaRequest input) {`

## BR075

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `resources/com/androidquery/callback/AjaxStatus.java:149`
  `protected AjaxStatus reset(){`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:482`
  `}else if(fallback == AQuery.PRESET){`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:483`
  `bm = preset;`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:838`
  `private void presetBitmap(String url, ImageView v){`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:841`
  `if(!url.equals(v.getTag(AQuery.TAG_URL)) || preset != null){`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:845`
  `if(preset != null && !cacheAvailable(v.getContext())){`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:846`
  `setBitmap(url, v, preset, true);`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:858`
  `private void setBitmap(String url, ImageView iv, Bitmap bm, boolean isPreset){`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:865`
  `if(isPreset){`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:871`
  `setBmAnimate(iv, bm, preset, fallback, animation, ratio, anchor, status.getSource());`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:890`
  `private static void setBmAnimate(ImageView iv, Bitmap bm, Bitmap preset, int fallback, int animation, float ratio, float anchor, int source){`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:902`
  `if(preset == null){`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:908`
  `Drawable pd = makeDrawable(iv, preset, ratio, anchor);`
- `resources/com/androidquery/util/Constants.java:34`
  `public static final int PRESET = -3;`
- `sources/androidx/appcompat/R.java:1205`
  `public static final int AppCompatTextView_autoSizePresetSizes = 0x00000003;`
- `sources/androidx/appcompat/R.java:1543`
  `public static final int[] AppCompatTextView = {android.R.attr.textAppearance, cn.xiaofengkj.fitpro.R.attr.autoSizeMaxTextSize, cn.xiaofengkj.fitpro.R.attr.autoSizeMinTextSize, cn.xiaofengkj.fitpro.R.attr.autoSizePresetSizes, cn.xiaofengkj.fitpro.R.attr.autoSizeStepGranularity, cn.xiaofengkj.fitpro.R...`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:246`
  `public void resetGroup() {`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:257`
  `resetGroup();`
- `sources/androidx/appcompat/view/menu/MenuItemImpl.java:632`
  `actionProvider2.reset();`
- `sources/androidx/appcompat/widget/AppCompatButton.java:236`
  `public void setAutoSizeTextTypeUniformWithPresetSizes(int[] iArr, int i) throws IllegalArgumentException {`
- `sources/androidx/appcompat/widget/AppCompatButton.java:238`
  `super.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatButton.java:243`
  `appCompatTextHelper.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:57`
  `void setAutoSizeTextTypeUniformWithPresetSizes(int[] iArr, int i);`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:296`
  `public void setAutoSizeTextTypeUniformWithPresetSizes(int[] iArr, int i) throws IllegalArgumentException {`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:298`
  `getSuperCaller().setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:303`
  `appCompatTextHelper.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:124`
  `if (typedArrayObtainStyledAttributes.hasValue(R.styleable.AppCompatTextView_autoSizePresetSizes) && (resourceId = typedArrayObtainStyledAttributes.getResourceId(R.styleable.AppCompatTextView_autoSizePresetSizes, 0)) > 0) {`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:126`
  `setupAutoSizeUniformPresetSizes(typedArrayObtainTypedArray);`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:291`
  `this.mAutoSizeTextSizesInPx = cleanupAutoSizePresetSizes(iArr);`
- `sources/androidx/camera/camera2/internal/Camera2CameraControlImpl.java:385`
  `void resetTemplate() {`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:484`
  `resetCaptureSession(z);`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:677`
  `public void onUseCaseReset(UseCase useCase) {`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:679`
  `resetUseCase(getUseCaseId(useCase), useCase.getSessionConfig(), useCase.getCurrentConfig(), useCase.getAttachedStreamSpec(), getCaptureTypes(useCase));`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:682`
  `private void resetUseCase(final String str, final SessionConfig sessionConfig, final UseCaseConfig<?> useCaseConfig, final StreamSpec streamSpec, final List<UseCaseConfigFactory.CaptureType> list) {`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:691`
  `/* JADX INFO: renamed from: lambda$resetUseCase$10$androidx-camera-camera2-internal-Camera2CameraImpl, reason: not valid java name */`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:693`
  `debugLog("Use case " + str + " RESET");`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:696`
  `resetCaptureSession(false);`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:835`
  `resetCaptureSession(false);`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:933`
  `resetCaptureSession(false);`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:940`
  `resetCaptureSession(false);`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:996`
  `resetUseCase(getMeteringRepeatingId(this.mMeteringRepeatingSession), this.mMeteringRepeatingSession.getSessionConfig(), this.mMeteringRepeatingSession.getUseCaseConfig(), null, Collections.singletonList(UseCaseConfigFactory.CaptureType.METERING_REPEATING));`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1093`
  `this.mStateCallback.resetReopenMonitor();`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1209`
  `this.mCameraControlInternal.resetTemplate();`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1255`
  `Camera2CameraImpl.this.resetCaptureSession(false);`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1281`
  `errorListener.onError(sessionConfig, SessionConfig.SessionError.SESSION_ERROR_SURFACE_NEEDS_RESET);`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1286`
  `void resetCaptureSession(boolean z) {`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1288`
  `debugLog("Resetting Capture Session");`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1481`
  `resetReopenMonitor();`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1605`
  `void resetReopenMonitor() {`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1606`
  `this.mCameraReopenMonitor.reset();`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1701`
  `reset();`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:24`
  `import androidx.camera.camera2.internal.compat.workaround.TorchStateReset;`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:69`
  `private final TorchStateReset mTorchStateReset;`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:94`
  `this.mTorchStateReset = new TorchStateReset();`
- `sources/androidx/camera/camera2/internal/MeteringRepeatingSession.java:34`
  `private final SurfaceResetCallback mSurfaceResetCallback;`
- `sources/androidx/camera/camera2/internal/MeteringRepeatingSession.java:38`
  `interface SurfaceResetCallback {`
- `sources/androidx/camera/camera2/internal/MeteringRepeatingSession.java:39`
  `void onSurfaceReset();`
- `sources/androidx/camera/camera2/internal/MeteringRepeatingSession.java:99`
  `SurfaceResetCallback surfaceResetCallback = this.mSurfaceResetCallback;`
- `sources/androidx/camera/camera2/internal/MeteringRepeatingSession.java:100`
  `if (surfaceResetCallback != null) {`
- `sources/androidx/camera/camera2/internal/MeteringRepeatingSession.java:101`
  `surfaceResetCallback.onSurfaceReset();`
- `sources/androidx/camera/camera2/internal/StreamUseCaseUtil.java:125`
  `public static boolean shouldUseStreamUseCase(SupportedSurfaceCombination.FeatureSettings featureSettings) {`
- `sources/androidx/camera/camera2/internal/StreamUseCaseUtil.java:126`
  `return featureSettings.getCameraMode() == 0 && featureSettings.getRequiredMaxBitDepth() == 8;`
- `sources/androidx/camera/camera2/internal/SupportedSurfaceCombination.java:355`
  `Map<UseCaseConfig<?>, List<Size>> mapFilterSupportedSizes = filterSupportedSizes(map, featureSettingsCreateFeatureSettings, targetFpsRange);`
- `sources/androidx/camera/camera2/internal/SupportedSurfaceCombination.java:414`
  `orderedSupportedStreamUseCaseSurfaceConfigList = getOrderedSupportedStreamUseCaseSurfaceConfigList(featureSettingsCreateFeatureSettings, (List) getSurfaceConfigListAndFpsCeiling(i, list, it2.next(), arrayList, list6, i6, map16, map15).first);`
- `sources/androidx/camera/camera2/internal/SupportedSurfaceCombination.java:588`
  `private boolean isUseCasesCombinationSupported(FeatureSettings featureSettings, List<AttachedSurfaceInfo> list, Map<UseCaseConfig<?>, List<Size>> map) {`
- `sources/androidx/camera/camera2/internal/SupportedSurfaceCombination.java:600`
  `arrayList.add(SurfaceConfig.transformSurfaceConfig(featureSettings.getCameraMode(), inputFormat, size, getUpdatedSurfaceSizeDefinitionByFormat(inputFormat)));`
- `sources/androidx/camera/camera2/internal/SupportedSurfaceCombination.java:602`
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
- `sources/androidx/camera/camera2/internal/ZoomControl.java:122`
  `this.mZoomImpl.resetZoom();`
- `sources/androidx/camera/camera2/internal/compat/workaround/TorchStateReset.java:13`
  `public class TorchStateReset {`
- `sources/androidx/camera/camera2/internal/compat/workaround/TorchStateReset.java:16`
  `public TorchStateReset() {`
- `sources/androidx/camera/camera2/internal/compat/workaround/TorchStateReset.java:20`
  `public boolean isTorchResetRequired(List<CaptureRequest> list, boolean z) {`
- `sources/androidx/camera/camera2/internal/compat/workaround/TorchStateReset.java:34`
  `public CaptureConfig createTorchResetRequest(CaptureConfig captureConfig) {`
- `sources/androidx/camera/core/ImageAnalysis.java:225`
  `notifyReset();`
- `sources/androidx/camera/core/Preview.java:78`
  `this.f$0.notifyReset();`
- `sources/androidx/camera/core/Preview.java:95`
  `this.f$0.notifyReset();`

## BR076

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `resources/AndroidManifest.xml:19`
  `<uses-feature`
- `resources/AndroidManifest.xml:22`
  `<uses-feature android:name="android.hardware.camera"/>`
- `resources/AndroidManifest.xml:23`
  `<uses-feature android:name="android.hardware.camera.autofocus"/>`
- `resources/AndroidManifest.xml:24`
  `<uses-feature android:name="android.hardware.telephony"/>`
- `resources/AndroidManifest.xml:118`
  `<uses-feature`
- `resources/AndroidManifest.xml:123`
  `<uses-feature android:name="android.hardware.usb.host"/>`
- `resources/AndroidManifest.xml:359`
  `android:name="xfkj.fitpro.activity.login.RegisterFinishActivity"`
- `resources/AndroidManifest.xml:362`
  `android:name="xfkj.fitpro.activity.login.ForgetPsdActivity"`
- `resources/AndroidManifest.xml:365`
  `android:name="xfkj.fitpro.activity.login.RegisterActivity"`
- `resources/AndroidManifest.xml:369`
  `android:name="xfkj.fitpro.activity.login.LoginActivity"`
- `resources/LICENSE-junit.txt:67`
  `needed, if any. For example, if a third party patent license is required to`
- `resources/LICENSE-junit.txt:69`
  `acquire that license before distributing the Program.`
- `resources/LICENSE-junit.txt:94`
  `offered by that Contributor alone and not by any other party; and`
- `resources/LICENSE-junit.txt:125`
  `actions brought by a third party against the Indemnified Contributor to the`
- `resources/LICENSE-junit.txt:210`
  `intellectual property laws of the United States of America. No party to this`
- `resources/LICENSE-junit.txt:212`
  `after the cause of action arose. Each party waives its rights to a jury trial`
- `resources/LICENSES.txt:16`
  `This software bundles several 3rd party libraries. These libraries are used at`
- `resources/LICENSES.txt:140`
  `3. Names of the copyright holders must not be used to endorse or promote`
- `resources/LICENSES.txt:352`
  `4. Neither the name of the University nor the names of its contributors`
- `resources/LICENSES.txt:541`
  `wherever such third-party notices normally appear. The contents`
- `resources/LICENSES.txt:565`
  `names, trademarks, service marks, or product names of the Licensor,`
- `resources/LICENSES.txt:613`
  `identification within third-party archives.`
- `resources/com/androidquery/AbstractAQuery.java:241`
  `* If no parent with matching id is found, operating view will be null and isExist() will return false.`
- `resources/com/androidquery/AbstractAQuery.java:298`
  `* Points the current operating view to the first view found with the id under the root.`
- `resources/com/androidquery/AbstractAQuery.java:333`
  `* Find the first view with first id, under that view, find again with 2nd id, etc...`
- `resources/com/androidquery/AbstractAQuery.java:344`
  `* Find the progress bar and show the progress for the next ajax/image request.`
- `resources/com/androidquery/AbstractAQuery.java:361`
  `* Set the progress bar and show the progress for the next ajax/image request.`
- `resources/com/androidquery/AbstractAQuery.java:379`
  `* Set the progress dialog and show the progress for the next ajax/image request.`
- `resources/com/androidquery/AbstractAQuery.java:386`
  `* It's the caller responsibility to dismiss the dialog when the activity terminates before the ajax is completed.`
- `resources/com/androidquery/AbstractAQuery.java:400`
  `* Apply the account handler for authentication for the next ajax request.`
- `resources/com/androidquery/AbstractAQuery.java:411`
  `* Apply the transformer to convert raw data to desired object type for the next ajax request.`
- `resources/com/androidquery/AbstractAQuery.java:427`
  `* Apply the proxy info to next ajax request.`
- `resources/com/androidquery/AbstractAQuery.java:746`
  `* @param preset Default image to show before real image loaded. null = no preset.`
- `resources/com/androidquery/AbstractAQuery.java:766`
  `* @param preset Default image to show before real image loaded. null = no preset.`
- `resources/com/androidquery/AbstractAQuery.java:1586`
  `* Register a callback method for when a textview text is changed. Method must have signature of method(CharSequence s, int start, int before, int count)).`
- `resources/com/androidquery/auth/FacebookHandle.java:54`
  `private boolean first;`
- `resources/com/androidquery/auth/FacebookHandle.java:74`
  `first = token == null;`
- `resources/com/androidquery/auth/FacebookHandle.java:205`
  `if(!first || token != null){`
- `resources/com/androidquery/auth/FacebookHandle.java:254`
  `first = false;`
- `resources/com/androidquery/auth/FacebookHandle.java:335`
  `boolean first = true;`
- `resources/com/androidquery/auth/FacebookHandle.java:337`
  `if (first)`
- `resources/com/androidquery/auth/FacebookHandle.java:338`
  `first = false;`
- `resources/com/androidquery/auth/FacebookHandle.java:566`
  `first = false;`
- `resources/com/androidquery/auth/FacebookHandle.java:575`
  `// An error occurred before we could be redirected.`
- `resources/com/androidquery/auth/GoogleHandle.java:119`
  `String[] names = new String[size];`
- `resources/com/androidquery/auth/GoogleHandle.java:121`
  `names[i] = accs[i].name;`
- `resources/com/androidquery/auth/GoogleHandle.java:123`
  `builder.setItems(names, this);`
- `resources/com/androidquery/auth/GoogleHandle.java:209`
  `public void applyToken(AbstractAjaxCallback<?, ?> cb, HttpRequest request) {`
- `resources/com/androidquery/auth/GoogleHandle.java:213`
  `request.addHeader("Authorization", "GoogleLogin auth=" + token);`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:155`
  `private HttpUriRequest request;`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:169`
  `request = null;`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:341`
  `* Set ajax request to be file cached.`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:352`
  `* Indicate ajax request to be memcached. Note: The default ajax handler does not supply a memcache.`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:369`
  `* Indicate the ajax request should ignore memcache and filecache.`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:380`
  `* Indicate the ajax request should use the main ui thread for callback. Default is true.`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:402`
  `* Set the header fields for the http request.`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:417`
  `* Set the header fields for the http request.`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:429`
  `* Set the cookies for the http request.`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:444`
  `* Set cookies for the http request.`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:509`
  `* Header field "Content-Type: application/x-www-form-urlencoded;charset=UTF-8" will be added if no Content-Type header field presents.`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:1342`
  `//convert get to post request, if url length is too long to be handled on web`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:1695`
  `request = hr;`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:1904`
  `* Set the authentication type of this request. This method requires API 5+.`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:2001`
  `* Abort the http request that will interrupt the network transfer.`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:2012`
  `if(request != null && !request.isAborted()){`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:2013`
  `request.abort();`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:322`
  `AQUtility.debug("before", bm.getWidth() + ":" + bm.getHeight());`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:562`
  `//check if view queue already contains first view`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:630`
  `* Sets the file cache write policy. If set to true, images load from network will be served quicker before caching to disk,`
- `resources/com/androidquery/util/Common.java:167`
  `public void onScroll(AbsListView view, int first, int visibleItemCount, int totalItemCount) {`
- `resources/com/androidquery/util/Common.java:171`
  `if(osl != null) osl.onScroll(view, first, visibleItemCount, totalItemCount);`
- `resources/com/androidquery/util/Common.java:222`
  `int first = elv.getFirstVisiblePosition();`
- `resources/com/androidquery/util/Common.java:225`
  `int count = last - first;`
- `resources/com/androidquery/util/Common.java:231`
  `long packed = elv.getExpandableListPosition(i + first);`
- `resources/com/androidquery/util/Common.java:274`
  `int first = lv.getFirstVisiblePosition();`
- `resources/com/androidquery/util/Common.java:277`
  `int count = last - first;`
- `resources/com/androidquery/util/Common.java:283`
  `long packed = i + first;`
- `resources/com/androidquery/util/Common.java:374`
  `int first = gallery.getFirstVisiblePosition();`
- `resources/com/androidquery/util/Common.java:377`
  `int diff = last - first;`
- `resources/com/androidquery/util/Common.java:416`
  `public void onTextChanged(CharSequence s, int start, int before, int count) {`

## BR077

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:514`
  `/* JADX INFO: renamed from: -deprecated_sslSocketFactory, reason: not valid java name */`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:515`
  `public final SSLSocketFactory m807deprecated_sslSocketFactory() {`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:516`
  `return sslSocketFactory();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:520`
  `@Metadata(d1 = {"\u0000ø\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0018...`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:819`
  `public final void setSslSocketFactoryOrNull$okhttp(SSLSocketFactory sSLSocketFactory) {`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:820`
  `this.sslSocketFactoryOrNull = sSLSocketFactory;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/BouncyCastlePlatform.java:48`
  `return sSLContext;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:57`
  `return sSLContext;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:120`
  `public SSLSocketFactory newSslSocketFactory(X509TrustManager trustManager) throws NoSuchAlgorithmException, KeyManagementException {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:122`
  `SSLContext sSLContextNewSSLContext = newSSLContext();`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:124`
  `SSLSocketFactory socketFactory = sSLContextNewSSLContext.getSocketFactory();`
- `sources/com/applovin/shadow/okhttp3/internal/platform/OpenJSSEPlatform.java:46`
  `return sSLContext;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Platform.java:87`
  `Intrinsics.checkNotNullExpressionValue(sSLContext, "getInstance(\"TLS\")");`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Platform.java:88`
  `return sSLContext;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Platform.java:181`
  `public SSLSocketFactory newSslSocketFactory(X509TrustManager trustManager) {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Platform.java:184`
  `SSLContext sSLContextNewSSLContext = newSSLContext();`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Platform.java:186`
  `SSLSocketFactory socketFactory = sSLContextNewSSLContext.getSocketFactory();`
- `sources/com/baidu/lbsapi/auth/g.java:120`
  `HttpsURLConnection httpsURLConnection = (HttpsURLConnection) (strA.equals("cmwap") ? url.openConnection(new Proxy(Proxy.Type.HTTP, new InetSocketAddress("10.0.0.172", 80))) : strA.equals("ctwap") ? url.openConnection(new Proxy(Proxy.Type.HTTP, new InetSocketAddress("10.0.0.200", 80))) : url.openConn...`
- `sources/com/baidu/lbsapi/auth/g.java:121`
  `httpsURLConnection.setHostnameVerifier(new h(this));`
- `sources/com/baidu/lbsapi/auth/g.java:122`
  `httpsURLConnection.setDoInput(true);`
- `sources/com/baidu/lbsapi/auth/g.java:123`
  `httpsURLConnection.setDoOutput(true);`
- `sources/com/baidu/lbsapi/auth/g.java:124`
  `httpsURLConnection.setRequestMethod("POST");`
- `sources/com/baidu/lbsapi/auth/g.java:125`
  `httpsURLConnection.setConnectTimeout(50000);`
- `sources/com/baidu/lbsapi/auth/g.java:126`
  `httpsURLConnection.setReadTimeout(50000);`
- `sources/com/baidu/lbsapi/auth/g.java:127`
  `return httpsURLConnection;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/SSLContextBuilder.java:122`
  `sSLContext.init(keyManagerArr, trustManagerArr, this.secureRandom);`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/SSLContextBuilder.java:123`
  `return sSLContext;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/SSLContexts.java:10`
  `public static SSLContext createDefault() throws SSLInitializationException {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/SSLContexts.java:12`
  `SSLContext sSLContext = SSLContext.getInstance("TLS");`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/SSLContexts.java:13`
  `sSLContext.init(null, null, null);`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/conn/ssl/SSLContexts.java:14`
  `return sSLContext;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/client/HttpClientBuilder.java:348`
  `public final HttpClientBuilder setSSLSocketFactory(LayeredConnectionSocketFactory layeredConnectionSocketFactory) {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/impl/client/HttpClientBuilder.java:349`
  `this.sslSocketFactory = layeredConnectionSocketFactory;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/ssl/SSLContextBuilder.java:226`
  `protected void initSSLContext(SSLContext sSLContext, Collection<KeyManager> collection, Collection<TrustManager> collection2, SecureRandom secureRandom) throws KeyManagementException {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/ssl/SSLContextBuilder.java:227`
  `sSLContext.init(!collection.isEmpty() ? (KeyManager[]) collection.toArray(new KeyManager[collection.size()]) : null, collection2.isEmpty() ? null : (TrustManager[]) collection2.toArray(new TrustManager[collection2.size()]), secureRandom);`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/ssl/SSLContextBuilder.java:230`
  `public SSLContext build() throws NoSuchAlgorithmException, KeyManagementException {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/ssl/SSLContextBuilder.java:231`
  `SSLContext sSLContext;`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/ssl/SSLContexts.java:9`
  `public static SSLContext createDefault() throws SSLInitializationException {`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/ssl/SSLContexts.java:11`
  `SSLContext sSLContext = SSLContext.getInstance("TLS");`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/ssl/SSLContexts.java:12`
  `sSLContext.init(null, null, null);`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/ssl/SSLContexts.java:13`
  `return sSLContext;`
- `sources/com/lzy/okgo/https/HttpsUtils.java:75`
  `SSLContext sSLContext = SSLContext.getInstance("TLS");`
- `sources/com/lzy/okgo/https/HttpsUtils.java:76`
  `sSLContext.init(keyManagerArrPrepareKeyManager, new TrustManager[]{x509TrustManager}, null);`
- `sources/com/lzy/okgo/https/HttpsUtils.java:77`
  `sSLParams.sSLSocketFactory = sSLContext.getSocketFactory();`
- `sources/com/mbridge/msdk/click/i.java:43`
  `httpsURLConnection = (HttpsURLConnection) new URL(strReplace).openConnection();`
- `sources/com/mbridge/msdk/click/i.java:48`
  `httpsURLConnection.setHostnameVerifier(new MBridgeHostnameVerifier(strReplace));`
- `sources/com/mbridge/msdk/click/i.java:49`
  `httpsURLConnection.setRequestMethod("GET");`
- `sources/com/mbridge/msdk/click/i.java:51`
  `httpsURLConnection.setRequestProperty("User-Agent", l0.i());`
- `sources/com/mbridge/msdk/click/i.java:54`
  `httpsURLConnection.setRequestProperty("User-Agent", l0.i());`
- `sources/com/mbridge/msdk/playercommon/exoplayer2/upstream/DefaultHttpDataSource.java:406`
  `private HttpsURLConnection makeConnection(URL url, byte[] bArr, long j, long j2, boolean z, boolean z2) throws IOException {`
- `sources/com/mbridge/msdk/playercommon/exoplayer2/upstream/DefaultHttpDataSource.java:407`
  `HttpsURLConnection httpsURLConnection = (HttpsURLConnection) url.openConnection();`
- `sources/com/mbridge/msdk/playercommon/exoplayer2/upstream/DefaultHttpDataSource.java:408`
  `httpsURLConnection.setHostnameVerifier(new MBridgeHostnameVerifier(url));`
- `sources/com/mbridge/msdk/playercommon/exoplayer2/upstream/DefaultHttpDataSource.java:409`
  `httpsURLConnection.setConnectTimeout(this.connectTimeoutMillis);`
- `sources/com/mbridge/msdk/playercommon/exoplayer2/upstream/DefaultHttpDataSource.java:410`
  `httpsURLConnection.setReadTimeout(this.readTimeoutMillis);`
- `sources/com/mbridge/msdk/playercommon/exoplayer2/upstream/DefaultHttpDataSource.java:414`
  `httpsURLConnection.setRequestProperty(entry.getKey(), entry.getValue());`
- `sources/com/mbridge/msdk/thrid/okhttp/t.java:133`
  `private static SSLSocketFactory a(X509TrustManager x509TrustManager) {`
- `sources/com/mbridge/msdk/thrid/okhttp/t.java:135`
  `SSLContext sSLContextE = com.mbridge.msdk.thrid.okhttp.internal.platform.g.d().e();`
- `sources/com/mbridge/msdk/tracker/network/toolbox/h.java:161`
  `protected HttpsURLConnection a(URL url) throws IOException {`
- `sources/com/mbridge/msdk/tracker/network/toolbox/h.java:162`
  `HttpsURLConnection httpsURLConnection = (HttpsURLConnection) url.openConnection();`
- `sources/com/mbridge/msdk/tracker/network/toolbox/h.java:163`
  `httpsURLConnection.setHostnameVerifier(new MBridgeHostnameVerifier(url));`
- `sources/com/mbridge/msdk/tracker/network/toolbox/h.java:164`
  `httpsURLConnection.setInstanceFollowRedirects(HttpURLConnection.getFollowRedirects());`
- `sources/com/mbridge/msdk/tracker/network/toolbox/h.java:165`
  `return httpsURLConnection;`
- `sources/com/mbridge/msdk/tracker/network/toolbox/h.java:168`
  `private HttpsURLConnection a(URL url, t<?> tVar) throws IOException {`
- `sources/com/mbridge/msdk/tracker/network/toolbox/h.java:169`
  `SSLSocketFactory sSLSocketFactory;`
- `sources/com/mbridge/msdk/tracker/network/toolbox/h.java:172`
  `httpsURLConnectionA.setConnectTimeout(iQ);`
- `sources/com/mbridge/msdk/tracker/network/toolbox/h.java:173`
  `httpsURLConnectionA.setReadTimeout(iQ);`
- `sources/com/mbridge/msdk/tracker/network/toolbox/h.java:174`
  `httpsURLConnectionA.setUseCaches(false);`
- `sources/com/mbridge/msdk/tracker/network/toolbox/h.java:175`
  `httpsURLConnectionA.setDoInput(true);`
- `sources/com/mbridge/msdk/tracker/network/toolbox/h.java:176`
  `if ("https".equals(url.getProtocol()) && (sSLSocketFactory = this.f7405a) != null) {`
- `sources/com/mbridge/msdk/tracker/network/toolbox/h.java:177`
  `httpsURLConnectionA.setSSLSocketFactory(sSLSocketFactory);`
- `sources/com/mbridge/msdk/tracker/network/toolbox/h.java:179`
  `return httpsURLConnectionA;`
- `sources/com/smartdigimkt/m0/b.java:167`
  `if ("https".equals(url.getProtocol()) && (sSLSocketFactory = this.b) != null) {`
- `sources/com/smartdigimkt/m0/b.java:168`
  `((HttpsURLConnection) httpURLConnectionA).setSSLSocketFactory(sSLSocketFactory);`
- `sources/com/thinkup/core/common/no/m/omm.java:297`
  `private static SSLSocketFactory o(X509TrustManager x509TrustManager) {`
- `sources/com/thinkup/core/common/no/m/omm.java:299`
  `SSLContext sSLContextN = com.thinkup.core.common.no.m.o.on.n.oo().n();`
- `sources/com/yandex/mobile/ads/impl/at1.java:20`
  `public final SSLContext a() {`
- `sources/com/yandex/mobile/ads/impl/at1.java:22`
  `SSLContext sSLContext = SSLContext.getInstance("TLS");`
- `sources/com/yandex/mobile/ads/impl/at1.java:23`
  `sSLContext.init(null, new X509TrustManager[]{this.f10301a}, null);`
- `sources/com/yandex/mobile/ads/impl/at1.java:24`
  `Intrinsics.checkNotNull(sSLContext);`
- `sources/com/yandex/mobile/ads/impl/at1.java:25`
  `return sSLContext;`

## BR078

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:31`
  `import javax.net.ssl.HostnameVerifier;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:43`
  `/* JADX INFO: compiled from: OkHttpClient.kt */`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:45`
  `@Metadata(d1 = {"\u0000î\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u001a\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u00...`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:46`
  `public class OkHttpClient implements Cloneable, Call.Factory, WebSocket.Factory {`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:352`
  `public OkHttpClient(Builder builder) throws NoSuchAlgorithmException, KeyStoreException {`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:519`
  `/* JADX INFO: compiled from: OkHttpClient.kt */`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:520`
  `@Metadata(d1 = {"\u0000ø\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0018...`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:872`
  `this.dns = okHttpClient.dns();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:873`
  `this.proxy = okHttpClient.proxy();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:874`
  `this.proxySelector = okHttpClient.proxySelector();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:875`
  `this.proxyAuthenticator = okHttpClient.proxyAuthenticator();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:876`
  `this.socketFactory = okHttpClient.socketFactory();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:877`
  `this.sslSocketFactoryOrNull = okHttpClient.sslSocketFactoryOrNull;`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:878`
  `this.x509TrustManagerOrNull = okHttpClient.getX509TrustManager();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:879`
  `this.connectionSpecs = okHttpClient.connectionSpecs();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:880`
  `this.protocols = okHttpClient.protocols();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:881`
  `this.hostnameVerifier = okHttpClient.hostnameVerifier();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:882`
  `this.certificatePinner = okHttpClient.certificatePinner();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:883`
  `this.certificateChainCleaner = okHttpClient.getCertificateChainCleaner();`
- `sources/com/applovin/shadow/okhttp3/OkHttpClient.java:884`
  `this.callTimeout = okHttpClient.callTimeoutMillis();`
- `sources/com/applovin/shadow/okhttp3/internal/connection/RealConnection.java:444`
  `OkHostnameVerifier okHostnameVerifier = OkHostnameVerifier.INSTANCE;`
- `sources/com/applovin/shadow/okhttp3/internal/connection/RealConnection.java:448`
  `if (okHostnameVerifier.verify(strHost, (X509Certificate) certificate)) {`
- `sources/com/applovin/shadow/okhttp3/internal/connection/RealConnection.java:455`
  `public final ExchangeCodec newCodec$okhttp(OkHttpClient client, RealInterceptorChain chain) throws SocketException {`
- `sources/com/applovin/shadow/okhttp3/internal/connection/RealConnection.java:602`
  `if (this.http2Connection == null || routes == null || !routeMatchesAny(routes) || address.hostnameVerifier() != OkHostnameVerifier.INSTANCE || !supportsUrl(address.url())) {`
- `sources/com/applovin/shadow/okhttp3/internal/http/CallServerInterceptor.java:24`
  `@Metadata(d1 = {"\u0000&\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0000\u0018\u00002\u00020\u0001B\r\u0012\u0006\u0010\u0002\u001a\u00020\u0003¢\u0006\u0002\u0010\u0004J\u0010...`
- `sources/com/applovin/shadow/okhttp3/internal/http2/PushObserver.java:37`
  `@Metadata(d1 = {"\u00008\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\b\u0002\u0018\u00002\u00...`
- `sources/com/applovin/shadow/okhttp3/internal/http2/PushObserver.java:39`
  `@Override // com.applovin.shadow.okhttp3.internal.http2.PushObserver`
- `sources/com/applovin/shadow/okhttp3/internal/http2/PushObserver.java:45`
  `@Override // com.applovin.shadow.okhttp3.internal.http2.PushObserver`
- `sources/com/applovin/shadow/okhttp3/internal/http2/PushObserver.java:51`
  `@Override // com.applovin.shadow.okhttp3.internal.http2.PushObserver`
- `sources/com/applovin/shadow/okhttp3/internal/http2/PushObserver.java:56`
  `@Override // com.applovin.shadow.okhttp3.internal.http2.PushObserver`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Android10Platform.java:14`
  `import com.unity3d.services.core.network.core.OkHttp3Client;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Android10Platform.java:28`
  `@Metadata(d1 = {"\u0000J\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Android10Platform.java:47`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.Platform`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Android10Platform.java:69`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.Platform`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Android10Platform.java:120`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.Platform`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Android10Platform.java:128`
  `@Metadata(d1 = {"\u0000\u001a\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\b\u0086\u0003\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002J\b\u0010\u0006\u001a\u0004\u0018\u00010\u0007R\u0011\u0010\u0003\u001a...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/AndroidPlatform.java:39`
  `@Metadata(d1 = {"\u0000x\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/AndroidPlatform.java:74`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.Platform`
- `sources/com/applovin/shadow/okhttp3/internal/platform/AndroidPlatform.java:96`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.Platform`
- `sources/com/applovin/shadow/okhttp3/internal/platform/AndroidPlatform.java:162`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.Platform`
- `sources/com/applovin/shadow/okhttp3/internal/platform/AndroidPlatform.java:169`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.Platform`
- `sources/com/applovin/shadow/okhttp3/internal/platform/AndroidPlatform.java:183`
  `@Metadata(d1 = {"\u00008\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u000e\n\u0000\b\u0080\b\u0018\u00...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/AndroidPlatform.java:240`
  `@Override // com.applovin.shadow.okhttp3.internal.tls.TrustRootIndex`
- `sources/com/applovin/shadow/okhttp3/internal/platform/BouncyCastlePlatform.java:28`
  `@Metadata(d1 = {"\u0000J\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/BouncyCastlePlatform.java:51`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.Platform`
- `sources/com/applovin/shadow/okhttp3/internal/platform/BouncyCastlePlatform.java:70`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.Platform`
- `sources/com/applovin/shadow/okhttp3/internal/platform/BouncyCastlePlatform.java:76`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.Platform`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:25`
  `import org.conscrypt.ConscryptHostnameVerifier;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:29`
  `@Metadata(d1 = {"\u0000H\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:41`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.Platform`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:60`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.Platform`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:71`
  `Conscrypt.setHostnameVerifier(x509TrustManager, DisabledHostnameVerifier.INSTANCE);`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:82`
  `@Metadata(d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\u0011\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\bÀ\u0002\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002J3\u0...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:83`
  `public static final class DisabledHostnameVerifier implements ConscryptHostnameVerifier {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:84`
  `public static final DisabledHostnameVerifier INSTANCE = new DisabledHostnameVerifier();`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:94`
  `private DisabledHostnameVerifier() {`
- `sources/com/applovin/shadow/okhttp3/internal/platform/ConscryptPlatform.java:119`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.Platform`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Jdk9Platform.java:3`
  `import com.applovin.shadow.okhttp3.Protocol;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Jdk9Platform.java:4`
  `import com.unity3d.services.core.network.core.OkHttp3Client;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Jdk9Platform.java:17`
  `@Metadata(d1 = {"\u0000<\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Jdk9Platform.java:50`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.Platform`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Jdk9Platform.java:57`
  `@Metadata(d1 = {"\u0000\u001a\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\b\u0086\u0003\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002J\b\u0010\u0006\u001a\u0004\u0018\u00010\u0007R\u0011\u0010\u0003\u001a...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/OpenJSSEPlatform.java:26`
  `@Metadata(d1 = {"\u0000J\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/OpenJSSEPlatform.java:49`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.Platform`
- `sources/com/applovin/shadow/okhttp3/internal/platform/OpenJSSEPlatform.java:68`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.Platform`
- `sources/com/applovin/shadow/okhttp3/internal/platform/OpenJSSEPlatform.java:74`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.Platform`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Platform.java:47`
  `@Metadata(d1 = {"\u0000t\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/Platform.java:164`
  `message = message + " To see where this was allocated, set the OkHttpClient logger level to FINE: Logger.getLogger(OkHttpClient.class.getName()).setLevel(Level.FINE);";`
- `sources/com/applovin/shadow/okhttp3/internal/platform/android/Android10SocketAdapter.java:8`
  `import com.unity3d.services.core.network.core.OkHttp3Client;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/android/Android10SocketAdapter.java:27`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.android.SocketAdapter`
- `sources/com/applovin/shadow/okhttp3/internal/platform/android/Android10SocketAdapter.java:32`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.android.SocketAdapter`
- `sources/com/applovin/shadow/okhttp3/internal/platform/android/Android10SocketAdapter.java:37`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.android.SocketAdapter`
- `sources/com/applovin/shadow/okhttp3/internal/platform/android/AndroidCertificateChainCleaner.java:1`
  `package com.applovin.shadow.okhttp3.internal.platform.android;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/android/AndroidCertificateChainCleaner.java:4`
  `import com.applovin.shadow.okhttp3.internal.tls.CertificateChainCleaner;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/android/AndroidCertificateChainCleaner.java:5`
  `import com.unity3d.services.core.network.core.OkHttp3Client;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/android/AndroidCertificateChainCleaner.java:18`
  `@Metadata(d1 = {"\u0000>\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\b\n\u0002\b\u0...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/android/AndroidCertificateChainCleaner.java:33`
  `@Override // com.applovin.shadow.okhttp3.internal.tls.CertificateChainCleaner`
- `sources/com/applovin/shadow/okhttp3/internal/platform/android/AndroidCertificateChainCleaner.java:57`
  `@Metadata(d1 = {"\u0000\u0018\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\b\u0086\u0003\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002J\u0012\u0010\u0003\u001a\u0004\u0018\u00010\u00042\u0006\u0010\u0005\u001a\u00...`
- `sources/com/applovin/shadow/okhttp3/internal/platform/android/AndroidSocketAdapter.java:10`
  `import com.unity3d.services.core.network.core.OkHttp3Client;`
- `sources/com/applovin/shadow/okhttp3/internal/platform/android/AndroidSocketAdapter.java:48`
  `@Override // com.applovin.shadow.okhttp3.internal.platform.android.SocketAdapter`

## BR079

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `resources/com/androidquery/WebDialog.java:100`
  `ws.setJavaScriptEnabled(true);`
- `resources/com/androidquery/util/WebImage.java:307`
  `ws.setJavaScriptEnabled(true);`
- `sources/androidx/webkit/internal/ApiHelperForN.java:57`
  `public static void setAllowFileAccess(ServiceWorkerWebSettings serviceWorkerWebSettings, boolean z) {`
- `sources/androidx/webkit/internal/ApiHelperForN.java:58`
  `serviceWorkerWebSettings.setAllowFileAccess(z);`
- `sources/androidx/webkit/internal/ServiceWorkerWebSettingsImpl.java:92`
  `public void setAllowFileAccess(boolean z) {`
- `sources/androidx/webkit/internal/ServiceWorkerWebSettingsImpl.java:95`
  `ApiHelperForN.setAllowFileAccess(getFrameworksImpl(), z);`
- `sources/androidx/webkit/internal/ServiceWorkerWebSettingsImpl.java:98`
  `getBoundaryInterface().setAllowFileAccess(z);`
- `sources/cn/niuyannet/inpay/h5/BaseWebActivity.java:100`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/amazon/aps/ads/util/adview/ApsAdViewUtils.java:214`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/amazon/aps/ads/util/adview/ApsAdViewUtils.java:218`
  `settings.setAllowFileAccess(false);`
- `sources/com/androidquery/WebDialog.java:73`
  `this.wv.getSettings().setJavaScriptEnabled(true);`
- `sources/com/androidquery/util/WebImage.java:65`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/applovin/impl/i8.java:189`
  `webViewB.getSettings().setJavaScriptEnabled(true);`
- `sources/com/applovin/impl/adview/a.java:911`
  `this.o.getSettings().setJavaScriptEnabled(true);`
- `sources/com/applovin/impl/adview/AppLovinWebViewBase.java:34`
  `settings.setAllowFileAccess(boolE.booleanValue());`
- `sources/com/applovin/impl/adview/b.java:75`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/applovin/impl/adview/l.java:20`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/applovin/impl/adview/l.java:24`
  `settings.setAllowFileAccess(true);`
- `sources/com/applovin/sdk/AppLovinWebViewActivity.java:83`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/baidu/location/b/n.java:332`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/baidu/location/b/n.java:333`
  `settings.setAllowFileAccess(false);`
- `sources/com/bytedance/sdk/component/bly/fkw.java:43`
  `settings.setAllowFileAccess(false);`
- `sources/com/bytedance/sdk/component/bly/le.java:623`
  `private void setJavaScriptEnabled(String str) {`
- `sources/com/bytedance/sdk/component/bly/le.java:630`
  `settings.setJavaScriptEnabled(false);`
- `sources/com/bytedance/sdk/component/utils/od.java:151`
  `leVar.setJavaScriptEnabled(true);`
- `sources/com/bytedance/sdk/openadsdk/activity/TTLandingPageActivity.java:396`
  `leVar9.setMixedContentMode(0);`
- `sources/com/bytedance/sdk/openadsdk/activity/TTVideoLandingPageActivity.java:327`
  `leVar3.setMixedContentMode(0);`
- `sources/com/bytedance/sdk/openadsdk/activity/TTWebsiteActivity.java:273`
  `settings.setMixedContentMode(0);`
- `sources/com/bytedance/sdk/openadsdk/activity/TTWebsiteActivity.java:275`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/bytedance/sdk/openadsdk/activity/TTWebsiteActivity.java:278`
  `settings.setAllowFileAccess(false);`
- `sources/com/bytedance/sdk/openadsdk/component/reward/view/ryl.java:450`
  `thVar.ko.setMixedContentMode(0);`
- `sources/com/bytedance/sdk/openadsdk/component/reward/vt/vt.java:950`
  `leVar2.setMixedContentMode(0);`
- `sources/com/bytedance/sdk/openadsdk/component/reward/vt/vt.java:1022`
  `leVar3.setAllowFileAccess(false);`
- `sources/com/bytedance/sdk/openadsdk/core/bly/ex.java:186`
  `leVar.setMixedContentMode(0);`
- `sources/com/bytedance/sdk/openadsdk/core/bly/ex.java:187`
  `leVar.setJavaScriptEnabled(true);`
- `sources/com/bytedance/sdk/openadsdk/core/bly/ex.java:191`
  `leVar.setAllowFileAccess(false);`
- `sources/com/bytedance/sdk/openadsdk/core/bly/yu.java:58`
  `fkwVar.setAllowFileAccess(false);`
- `sources/com/bytedance/sdk/openadsdk/core/bly/yu.java:59`
  `fkwVar.setJavaScriptEnabled(true);`
- `sources/com/bytedance/sdk/openadsdk/core/bly/yu.java:71`
  `fkwVar.setMixedContentMode(0);`
- `sources/com/bytedance/sdk/openadsdk/core/cf/lh/yu.java:95`
  `leVar2.setMixedContentMode(0);`
- `sources/com/bytedance/sdk/openadsdk/core/cf/lh/yu.java:96`
  `leVar2.setJavaScriptEnabled(true);`
- `sources/com/bytedance/sdk/openadsdk/core/cf/lh/yu.java:100`
  `leVar2.setAllowFileAccess(false);`
- `sources/com/bytedance/sdk/openadsdk/core/widget/ouw/lh.java:38`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/bytedance/sdk/openadsdk/core/widget/ouw/lh.java:55`
  `settings.setAllowFileAccess(false);`
- `sources/com/bytedance/sdk/openadsdk/core/widget/ouw/vt.java:91`
  `leVar.setMixedContentMode(0);`
- `sources/com/bytedance/sdk/openadsdk/core/widget/ouw/vt.java:92`
  `leVar.setJavaScriptEnabled(true);`
- `sources/com/bytedance/sdk/openadsdk/core/widget/ouw/vt.java:97`
  `leVar.setAllowFileAccess(false);`
- `sources/com/bytedance/sdk/openadsdk/jg/ouw.java:211`
  `leVar.setMixedContentMode(0);`
- `sources/com/bytedance/sdk/openadsdk/zin/pno.java:279`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/bytedance/sdk/openadsdk/zin/pno.java:281`
  `ra.ouw("WebViewSettings", "setJavaScriptEnabled error", th3);`
- `sources/com/bytedance/sdk/openadsdk/zin/pno.java:291`
  `settings.setAllowFileAccess(false);`
- `sources/com/bytedance/sdk/openadsdk/zin/pno.java:294`
  `settings.setAllowFileAccessFromFileURLs(false);`
- `sources/com/bytedance/sdk/openadsdk/zin/pno.java:295`
  `settings.setAllowUniversalAccessFromFileURLs(false);`
- `sources/com/bytedance/sdk/openadsdk/zin/pno.java:308`
  `webView.getSettings().setMixedContentMode(0);`
- `sources/com/bytedance/sdk/openadsdk/zin/pno.java:310`
  `webView.getSettings().setMixedContentMode(0);`
- `sources/com/bytedance/sdk/openadsdk/zin/ouw/ouw.java:303`
  `this.lh.setMixedContentMode(0);`
- `sources/com/facebook/ads/redexgen/core/AbstractC1929ay.java:61`
  `getSettings().setJavaScriptEnabled(true);`
- `sources/com/facebook/ads/redexgen/core/AbstractC1935b4.java:39`
  `webView.getSettings().setMixedContentMode(0);`
- `sources/com/facebook/ads/redexgen/core/C2134eI.java:131`
  `settings.setAllowFileAccess(true);`
- `sources/com/facebook/ads/redexgen/core/C2134eI.java:132`
  `settings.setAllowFileAccessFromFileURLs(true);`
- `sources/com/facebook/ads/redexgen/core/M3.java:104`
  `settings.setAllowFileAccessFromFileURLs(false);`
- `sources/com/facebook/ads/redexgen/core/M3.java:105`
  `settings.setAllowUniversalAccessFromFileURLs(false);`
- `sources/com/facebook/ads/redexgen/core/M3.java:106`
  `settings.setAllowFileAccess(false);`
- `sources/com/google/android/gms/ads/internal/zzs.java:60`
  `this.zze.getSettings().setJavaScriptEnabled(true);`
- `sources/com/google/android/gms/ads/internal/util/zzs.java:858`
  `webSettings.setAllowFileAccessFromFileURLs(false);`
- `sources/com/google/android/gms/ads/internal/util/zzs.java:859`
  `webSettings.setAllowUniversalAccessFromFileURLs(false);`
- `sources/com/google/android/gms/internal/ads/zzcko.java:132`
  `settings.setAllowFileAccess(false);`
- `sources/com/google/android/gms/internal/ads/zzcko.java:134`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/google/android/gms/internal/ads/zzfty.java:11`
  `webView.getSettings().setJavaScriptEnabled(true);`
- `sources/com/google/android/gms/internal/ads/zzfub.java:27`
  `webView.getSettings().setJavaScriptEnabled(true);`
- `sources/com/google/android/gms/internal/ads/zzfub.java:29`
  `this.zza.getSettings().setAllowFileAccess(false);`
- `sources/com/google/android/gms/internal/consent_sdk/zzbe.java:114`
  `zzbxVar.getSettings().setJavaScriptEnabled(true);`
- `sources/com/google/android/gms/internal/consent_sdk/zzbe.java:115`
  `zzbxVar.getSettings().setAllowFileAccess(false);`
- `sources/com/iab/omid/library/amazon/publisher/a.java:10`
  `webView.getSettings().setJavaScriptEnabled(true);`
- `sources/com/iab/omid/library/amazon/publisher/b.java:90`
  `webView.getSettings().setJavaScriptEnabled(true);`
- `sources/com/iab/omid/library/amazon/publisher/b.java:92`
  `this.g.getSettings().setAllowFileAccess(false);`
- `sources/com/iab/omid/library/applovin/publisher/a.java:10`
  `webView.getSettings().setJavaScriptEnabled(true);`
- `sources/com/iab/omid/library/applovin/publisher/b.java:90`
  `webView.getSettings().setJavaScriptEnabled(true);`
- `sources/com/iab/omid/library/applovin/publisher/b.java:92`
  `this.g.getSettings().setAllowFileAccess(false);`
- `sources/com/iab/omid/library/bigosg/publisher/a.java:9`
  `webView.getSettings().setJavaScriptEnabled(true);`

## BR080

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/android/support/v4/media/MediaBrowserCompat.java:651`
  `Log.d(MediaBrowserCompat.TAG, "addSubscription failed with RemoteException parentId=" + str);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:769`
  `Log.d(MediaBrowserCompat.TAG, "ServiceCallbacks.onConnect...");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:784`
  `Log.d(MediaBrowserCompat.TAG, "addSubscription failed with RemoteException.");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:862`
  `Log.d(MediaBrowserCompat.TAG, "  mServiceConnection=" + this.mServiceConnection);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:863`
  `Log.d(MediaBrowserCompat.TAG, "  mServiceBinderWrapper=" + this.mServiceBinderWrapper);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:864`
  `Log.d(MediaBrowserCompat.TAG, "  mCallbacksMessenger=" + this.mCallbacksMessenger);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:865`
  `Log.d(MediaBrowserCompat.TAG, "  mRootId=" + this.mRootId);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:866`
  `Log.d(MediaBrowserCompat.TAG, "  mMediaSessionToken=" + this.mMediaSessionToken);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2078`
  `Log.d("AppCompatDelegate", "Exception while getting ActivityInfo", e);`
- `sources/androidx/camera/core/processing/OpenGlRenderer.java:314`
  `Log.d(TAG, "EGLContext created, client version " + iArr3[0]);`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:1614`
  `Log.v(MotionLayout.TAG, str2 + " done. ");`
- `sources/androidx/exifinterface/media/ExifInterface.java:2428`
  `Log.d(TAG, "getRafAttributes starting with: " + byteOrderedDataInputStream);`
- `sources/androidx/exifinterface/media/ExifInterface.java:2710`
  `Log.d(TAG, "getWebpAttributes starting with: " + byteOrderedDataInputStream);`
- `sources/androidx/exifinterface/media/ExifInterface.java:3086`
  `Log.d(TAG, "readExifSegment: Byte Align MM");`
- `sources/androidx/exifinterface/media/ExifInterface.java:3248`
  `Log.d(TAG, "Failed to skip " + i7 + " bytes.");`
- `sources/androidx/exifinterface/media/ExifInterface.java:3254`
  `Log.d(TAG, "Failed to read " + i6 + " bytes.");`
- `sources/androidx/fragment/app/FragmentLayoutInflaterFactory.java:71`
  `Log.v("FragmentManager", "Fragment " + fragmentFindFragmentById + " has been inflated via the <fragment> tag: id=0x" + Integer.toHexString(resourceId));`
- `sources/androidx/fragment/app/FragmentLayoutInflaterFactory.java:83`
  `Log.v("FragmentManager", "Retained Fragment " + fragmentFindFragmentById + " has been re-attached via the <fragment> tag: id=0x" + Integer.toHexString(resourceId));`
- `sources/androidx/fragment/app/FragmentManager.java:1702`
  `Log.v(TAG, "Discarding retained Fragment " + fragment2 + " that was not found in the set of active Fragments " + fragmentManagerState.mActive);`
- `sources/androidx/fragment/app/FragmentStateManager.java:466`
  `Log.d("FragmentManager", "moveto ACTIVITY_CREATED: " + this.mFragment);`
- `sources/androidx/fragment/app/FragmentStore.java:125`
  `Log.v("FragmentManager", "Removed fragment from active set " + fragment);`
- `sources/androidx/fragment/app/SpecialEffectsController.java:197`
  `Log.v(FragmentManager.TAG, "SpecialEffectsController: Finished executing pending operations");`
- `sources/androidx/localbroadcastmanager/content/LocalBroadcastManager.java:155`
  `Log.v(TAG, "Resolving type " + strResolveTypeIfNeeded + " scheme " + scheme + " of intent " + intent);`
- `sources/androidx/localbroadcastmanager/content/LocalBroadcastManager.java:160`
  `Log.v(TAG, "Action list: " + arrayList2);`
- `sources/androidx/localbroadcastmanager/content/LocalBroadcastManager.java:186`
  `Log.v(TAG, "  Filter matched!  match=0x" + Integer.toHexString(iMatch));`
- `sources/androidx/profileinstaller/ProfileInstaller.java:41`
  `Log.d(TAG, i != 1 ? i != 2 ? i != 3 ? i != 4 ? i != 5 ? "" : "DIAGNOSTIC_PROFILE_IS_COMPRESSED" : "DIAGNOSTIC_REF_PROFILE_DOES_NOT_EXIST" : "DIAGNOSTIC_REF_PROFILE_EXISTS" : "DIAGNOSTIC_CURRENT_PROFILE_DOES_NOT_EXIST" : "DIAGNOSTIC_CURRENT_PROFILE_EXISTS");`
- `sources/androidx/profileinstaller/ProfileInstaller.java:86`
  `Log.d(TAG, str);`
- `sources/androidx/profileinstaller/ProfileInstaller.java:217`
  `Log.d(TAG, "Installing profile for " + context.getPackageName());`
- `sources/androidx/profileinstaller/ProfileInstaller.java:224`
  `Log.d(TAG, "Skipping profile installation for " + context.getPackageName());`
- `sources/androidx/test/espresso/base/RootViewPicker.java:286`
  `Log.d(RootViewPicker.TAG, String.format("No matching root available - waiting: %sms for one to appear.", Long.valueOf(backoffForAttempt)));`
- `sources/androidx/test/espresso/base/RootViewPicker.java:301`
  `Log.d(RootViewPicker.TAG, String.format("Root not ready - waiting: %sms for one to appear.", Long.valueOf(backoffForAttempt)));`
- `sources/androidx/test/internal/runner/lifecycle/ActivityLifecycleMonitorImpl.java:108`
  `Log.d(TAG, new StringBuilder(String.valueOf(strValueOf).length() + 30 + String.valueOf(strValueOf2).length()).append("Lifecycle status change: ").append(strValueOf).append(" in: ").append(strValueOf2).toString());`
- `sources/androidx/test/runner/MonitoringInstrumentation.java:299`
  `Log.d(TAG, "execStartActivities(context, ibinder, ibinder, activity, intent[], bundle)");`
- `sources/androidx/test/runner/MonitoringInstrumentation.java:306`
  `Log.d(TAG, "execStartActivity(context, IBinder, IBinder, Fragment, Intent, int, Bundle)");`
- `sources/app/akexorcist/bluetotohspp/library/DeviceList.java:136`
  `Log.d(TAG, "doDiscovery()");`
- `sources/com/amazon/aps/shared/util/APSNetworkManager.java:155`
  `Log.d(str4, "Sending the event data: " + str3);`
- `sources/com/amazon/aps/shared/util/APSNetworkManager.java:157`
  `Log.d(str4, "Response code received : " + responseCode);`
- `sources/com/amazon/aps/shared/util/APSNetworkManager.java:163`
  `Log.d(str4, "Response received: ".concat(new String(bArr)));`
- `sources/com/beken/beken_ota/ble/OTABLEFunction.java:85`
  `Log.d(OTABLEFunction.TAG, BleService.ACTION_GATT_SERVICES_DISCOVERED);`
- `sources/com/blankj/utilcode/util/KeyboardUtils.java:134`
  `Log.d("KeyboardUtils", "getDecorViewInvisibleHeight: " + (decorView.getBottom() - rect.bottom));`

## BR081

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/com/google/android/gms/internal/ads/zzhue.java:9`
  `import java.security.spec.RSAKeyGenParameterSpec;`
- `sources/com/google/android/gms/internal/ads/zzhue.java:24`
  `keyPairGenerator.initialize(new RSAKeyGenParameterSpec(zzhtyVar.zzc(), new BigInteger(1, zzhtyVar.zzd().toByteArray())));`
- `sources/com/google/android/gms/internal/ads/zzhuq.java:9`
  `import java.security.spec.RSAKeyGenParameterSpec;`
- `sources/com/google/android/gms/internal/ads/zzhuq.java:24`
  `keyPairGenerator.initialize(new RSAKeyGenParameterSpec(zzhukVar.zzc(), new BigInteger(1, zzhukVar.zzd().toByteArray())));`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/ssl/SSLContextBuilder.java:124`
  `KeyStore keyStore = KeyStore.getInstance(this.keyStoreType);`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/ssl/SSLContextBuilder.java:146`
  `KeyStore keyStore = KeyStore.getInstance(this.keyStoreType);`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/ssl/SSLContextBuilder.java:192`
  `KeyStore keyStore = KeyStore.getInstance(this.keyStoreType);`
- `sources/com/google/firebase/crashlytics/buildtools/reloc/org/apache/http/ssl/SSLContextBuilder.java:210`
  `KeyStore keyStore = KeyStore.getInstance(this.keyStoreType);`
- `sources/com/lzy/okgo/https/HttpsUtils.java:90`
  `KeyStore keyStore = KeyStore.getInstance("BKS");`
- `sources/com/lzy/okgo/https/HttpsUtils.java:106`
  `KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());`
- `sources/com/yandex/mobile/ads/impl/nw1.java:99`
  `keyStore = KeyStore.getInstance(KeyStore.getDefaultType());`

## BR082

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:15`
  `import androidx.core.content.FileProvider;`
- `sources/androidx/browser/customtabs/TrustedWebUtils.java:9`
  `import androidx.core.content.FileProvider;`
- `sources/androidx/browser/customtabs/TrustedWebUtils.java:43`
  `Uri uriForFile = FileProvider.getUriForFile(context, str, file);`
- `sources/androidx/core/content/FileProvider.java:271`
  `@Override // androidx.core.content.FileProvider.PathStrategy`
- `sources/androidx/core/content/FileProvider.java:298`
  `@Override // androidx.core.content.FileProvider.PathStrategy`
- `sources/cn/bertsir/zbar/utils/QrFileProvider.java:3`
  `import androidx.core.content.FileProvider;`
- `sources/com/blankj/utilcode/util/IntentUtils.java:7`
  `import androidx.core.content.FileProvider;`
- `sources/com/blankj/utilcode/util/IntentUtils.java:33`
  `return getInstallAppIntent(FileProvider.getUriForFile(Utils.getApp(), Utils.getApp().getPackageName() + ".utilcode.fileprovider", file));`
- `sources/com/blankj/utilcode/util/UriUtils.java:12`
  `import androidx.core.content.FileProvider;`
- `sources/com/blankj/utilcode/util/UriUtils.java:32`
  `return FileProvider.getUriForFile(Utils.getApp(), Utils.getApp().getPackageName() + ".utilcode.fileprovider", file);`
- `sources/com/blankj/utilcode/util/UtilsFileProvider.java:4`
  `import androidx.core.content.FileProvider;`
- `sources/com/blankj/utilcode/util/UtilsFileProvider.java:8`
  `@Override // androidx.core.content.FileProvider, android.content.ContentProvider`
- `sources/com/just/agentweb/AgentWebFileProvider.java:5`
  `import androidx.core.content.FileProvider;`
- `sources/com/just/agentweb/AgentWebFileProvider.java:9`
  `@Override // androidx.core.content.FileProvider, android.content.ContentProvider`
- `sources/com/just/agentweb/AgentWebUtils.java:33`
  `import androidx.core.content.FileProvider;`
- `sources/com/just/agentweb/AgentWebUtils.java:515`
  `return FileProvider.getUriForFile(context, context.getPackageName() + ".AgentWebFileProvider", file);`
- `sources/com/luck/picture/lib/PictureFileProvider.java:3`
  `import androidx.core.content.FileProvider;`
- `sources/com/luck/picture/lib/tools/FileUtils.java:9`
  `import androidx.core.content.FileProvider;`
- `sources/com/luck/picture/lib/tools/FileUtils.java:90`
  `return FileProvider.getUriForFile(context, context.getPackageName() + ".luckProvider", file);`
- `sources/com/luck/picture/lib/tools/PictureFileUtils.java:12`
  `import androidx.core.content.FileProvider;`
- `sources/com/luck/picture/lib/tools/PictureFileUtils.java:416`
  `return FileProvider.getUriForFile(context, context.getPackageName() + ".luckProvider", file);`
- `sources/com/onmicro/omtoolbox/util/FileUtils.java:9`
  `import androidx.core.content.FileProvider;`
- `sources/com/onmicro/omtoolbox/util/FileUtils.java:73`
  `Uri uriForFile = FileProvider.getUriForFile(context, context.getPackageName() + ".fileprovider", file);`
- `sources/com/onmicro/omtoolbox/util/IntentUtils.java:8`
  `import androidx.core.content.FileProvider;`
- `sources/com/onmicro/omtoolbox/util/IntentUtils.java:28`
  `Uri uriForFile = FileProvider.getUriForFile(context.getApplicationContext(), "com.onmicro.omtoolbox.fileprovider", file);`
- `sources/com/onmicro/omtoolbox/util/IntentUtils.java:103`
  `return FileProvider.getUriForFile(context.getApplicationContext(), "com.onmicro.fileprovider", file);`
- `sources/com/phy/ota_demo/utils/FileUtil.java:9`
  `import androidx.core.content.FileProvider;`
- `sources/com/phy/ota_demo/utils/FileUtil.java:129`
  `return FileProvider.getUriForFile(mContext, mContext.getPackageName() + ".fileprovider", new File(str));`
- `sources/com/yandex/mobile/ads/features/debugpanel/data/local/DebugPanelFileProvider.java:3`
  `import androidx.core.content.FileProvider;`
- `sources/com/yandex/mobile/ads/impl/yk0.java:5`
  `import androidx.core.content.FileProvider;`
- `sources/com/yandex/mobile/ads/impl/yk0.java:38`
  `Uri uriForFile = FileProvider.getUriForFile(this.f12696a, this.f12696a.getPackageName() + ".monetization.ads.inspector.fileprovider", fileA);`

## BR086

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `resources/com/androidquery/AbstractAQuery.java:2399`
  `* The returned file is accessable to all apps, therefore it is ideal for sharing content (such as photo) via the intent mechanism.`
- `resources/com/androidquery/AbstractAQuery.java:2409`
  `*	startActivityForResult(Intent.createChooser(intent, "Share via:"), 0);`
- `resources/com/androidquery/callback/BitmapAjaxCallback.java:275`
  `options.inInputShareable = true;`
- `resources/com/androidquery/util/Common.java:46`
  `* AQuery internal use only. A shared listener class to reduce the number of classes.`
- `resources/com/androidquery/util/WebImage.java:63`
  `SharedPreferences prefs = context.getSharedPreferences(PREF_FILE, Context.MODE_PRIVATE);`
- `sources/androidx/appcompat/R.java:63`
  `public static final int actionModeShareDrawable = 0x7f040024;`
- `sources/androidx/appcompat/R.java:517`
  `public static final int abc_ab_share_pack_mtrl_alpha = 0x7f080032;`
- `sources/androidx/appcompat/R.java:525`
  `public static final int abc_btn_default_mtrl_shape = 0x7f08003a;`
- `sources/androidx/appcompat/R.java:1249`
  `public static final int AppCompatTheme_actionModeShareDrawable = 0x0000001b;`
- `sources/androidx/appcompat/R.java:1361`
  `public static final int DrawerArrowToggle_arrowShaftLength = 0x00000001;`
- `sources/androidx/appcompat/R.java:1544`
  `public static final int[] AppCompatTheme = {android.R.attr.windowIsFloating, android.R.attr.windowAnimationStyle, cn.xiaofengkj.fitpro.R.attr.actionBarDivider, cn.xiaofengkj.fitpro.R.attr.actionBarItemBackground, cn.xiaofengkj.fitpro.R.attr.actionBarPopupTheme, cn.xiaofengkj.fitpro.R.attr.actionBarS...`
- `sources/androidx/appcompat/R.java:1548`
  `public static final int[] DrawerArrowToggle = {cn.xiaofengkj.fitpro.R.attr.arrowHeadLength, cn.xiaofengkj.fitpro.R.attr.arrowShaftLength, cn.xiaofengkj.fitpro.R.attr.barLength, cn.xiaofengkj.fitpro.R.attr.color, cn.xiaofengkj.fitpro.R.attr.drawableSize, cn.xiaofengkj.fitpro.R.attr.gapBetweenBars, cn...`
- `sources/androidx/appcompat/R.java:1561`
  `public static final int[] TextAppearance = {android.R.attr.textSize, android.R.attr.typeface, android.R.attr.textStyle, android.R.attr.textColor, android.R.attr.textColorHint, android.R.attr.textColorLink, android.R.attr.shadowColor, android.R.attr.shadowDx, android.R.attr.shadowDy, android.R.attr.s...`
- `sources/androidx/appcompat/app/AppCompatDelegate.java:124`
  `public abstract boolean isHandleNativeActionModesEnabled();`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:178`
  `public boolean isHandleNativeActionModesEnabled() {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2505`
  `if (AppCompatDelegateImpl.this.isHandleNativeActionModesEnabled() && i == 0) {`
- `sources/androidx/appcompat/app/SkinAppCompatDelegateImpl.java:79`
  `public /* bridge */ /* synthetic */ boolean isHandleNativeActionModesEnabled() {`
- `sources/androidx/appcompat/app/SkinAppCompatDelegateImpl.java:80`
  `return super.isHandleNativeActionModesEnabled();`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:24`
  `private float mArrowShaftLength;`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:109`
  `this.mArrowShaftLength = typedArrayObtainStyledAttributes.getDimension(R.styleable.DrawerArrowToggle_arrowShaftLength, 0.0f);`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:195`
  `float fLerp2 = lerp(this.mBarLength, this.mArrowShaftLength, this.mProgress);`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:9`
  `import android.graphics.Shader;`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:32`
  `private final int[] COLORFILTER_TINT_COLOR_CONTROL_NORMAL = {R.drawable.abc_textfield_search_default_mtrl_alpha, R.drawable.abc_textfield_default_mtrl_alpha, R.drawable.abc_ab_share_pack_mtrl_alpha};`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:33`
  `private final int[] TINT_COLOR_CONTROL_NORMAL = {R.drawable.abc_ic_commit_search_api_mtrl_alpha, R.drawable.abc_seekbar_tick_mark_material, R.drawable.abc_ic_menu_share_mtrl_alpha, R.drawable.abc_ic_menu_copy_mtrl_am_alpha, R.drawable.abc_ic_menu_cut_mtrl_alpha, R.drawable.abc_ic_menu_selectall_mtrl...`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:114`
  `bitmapDrawable2.setTileModeX(Shader.TileMode.REPEAT);`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:178`
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
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:76`
  `ShapeDrawable shapeDrawable = new ShapeDrawable(getDrawableShape());`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:77`
  `shapeDrawable.getPaint().setShader(new BitmapShader(bitmap, Shader.TileMode.REPEAT, Shader.TileMode.CLAMP));`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:78`
  `shapeDrawable.getPaint().setColorFilter(bitmapDrawable.getPaint().getColorFilter());`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:79`
  `return z ? new ClipDrawable(shapeDrawable, 3, 1) : shapeDrawable;`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:102`
  `private Shape getDrawableShape() {`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:103`
  `return new RoundRectShape(new float[]{5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f}, null, null);`
- `sources/androidx/appcompat/widget/DropDownListView.java:516`
  `private static boolean sHasMethods;`
- `sources/androidx/appcompat/widget/DropDownListView.java:522`
  `return sHasMethods;`
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
- `sources/androidx/browser/browseractions/BrowserActionsFallbackMenuUi.java:62`
  `private PendingIntent buildShareAction() {`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:7`
  `import android.content.SharedPreferences;`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:86`
  `private static boolean shouldCleanUp(SharedPreferences sharedPreferences) {`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:87`
  `return System.currentTimeMillis() > sharedPreferences.getLong(BrowserServiceFileProvider.LAST_CLEANUP_TIME_KEY, System.currentTimeMillis()) + CLEANUP_REQUIRED_TIME_SPAN;`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:35`
  `public static final int ACTIVITY_SIDE_SHEET_DECORATION_TYPE_SHADOW = 2;`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:65`
  `public static final String EXTRA_DEFAULT_SHARE_MENU_ITEM = "android.support.customtabs.extra.SHARE_MENU_ITEM";`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:160`
  `private boolean mShareIdentity;`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:163`
  `private int mShareState = 0;`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:171`
  `public Builder setShareIdentityEnabled(boolean z) {`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:172`
  `this.mShareIdentity = z;`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:244`
  `public Builder addDefaultShareMenuItem() {`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:245`
  `setShareState(1);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:250`
  `public Builder setDefaultShareMenuItemEnabled(boolean z) {`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:252`
  `setShareState(1);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:254`
  `setShareState(2);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:259`
  `public Builder setShareState(int i) {`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:267`
  `this.mIntent.putExtra(CustomTabsIntent.EXTRA_DEFAULT_SHARE_MENU_ITEM, false);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:269`
  `this.mIntent.removeExtra(CustomTabsIntent.EXTRA_DEFAULT_SHARE_MENU_ITEM);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:495`
  `this.mIntent.putExtra(CustomTabsIntent.EXTRA_SHARE_STATE, this.mShareState);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:498`
  `setShareIdentityEnabled();`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:521`
  `private void setShareIdentityEnabled() {`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:525`
  `Api34Impl.setShareIdentityEnabled(this.mActivityOptions, this.mShareIdentity);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:667`
  `static void setShareIdentityEnabled(ActivityOptions activityOptions, boolean z) {`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:668`
  `activityOptions.setShareIdentityEnabled(z);`
- `sources/androidx/browser/trusted/sharing/ShareData.java:25`
  `bundle.putString("androidx.browser.trusted.sharing.KEY_TITLE", this.title);`
- `sources/androidx/browser/trusted/sharing/ShareData.java:26`
  `bundle.putString("androidx.browser.trusted.sharing.KEY_TEXT", this.text);`
- `sources/androidx/browser/trusted/sharing/ShareData.java:33`
  `public static ShareData fromBundle(Bundle bundle) {`
- `sources/androidx/browser/trusted/sharing/ShareData.java:34`
  `return new ShareData(bundle.getString("androidx.browser.trusted.sharing.KEY_TITLE"), bundle.getString("androidx.browser.trusted.sharing.KEY_TEXT"), bundle.getParcelableArrayList(KEY_URIS));`
- `sources/androidx/browser/trusted/sharing/ShareTarget.java:1`
  `package androidx.browser.trusted.sharing;`
- `sources/androidx/browser/trusted/sharing/ShareTarget.java:13`
  `public final class ShareTarget {`
- `sources/androidx/browser/trusted/sharing/ShareTarget.java:78`
  `bundle.putString("androidx.browser.trusted.sharing.KEY_TITLE", this.title);`
- `sources/androidx/browser/trusted/sharing/ShareTarget.java:79`
  `bundle.putString("androidx.browser.trusted.sharing.KEY_TEXT", this.text);`
- `sources/androidx/browser/trusted/sharing/ShareTarget.java:104`
  `return new Params(bundle.getString("androidx.browser.trusted.sharing.KEY_TITLE"), bundle.getString("androidx.browser.trusted.sharing.KEY_TEXT"), arrayList);`
- `sources/androidx/browser/trusted/sharing/ShareTarget.java:109`
  `public static final String KEY_ACCEPTED_TYPES = "androidx.browser.trusted.sharing.KEY_ACCEPTED_TYPES";`
- `sources/androidx/browser/trusted/sharing/ShareTarget.java:110`
  `public static final String KEY_NAME = "androidx.browser.trusted.sharing.KEY_FILE_NAME";`

## BR088

paper_id: B004
paper_title: Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation

- `sources/cn/xiaofengkj/fitpro/R.java:6052`
  `public static final int ic_stat_notify_dfu = 0x7f080204;`
- `sources/cn/xiaofengkj/fitpro/R.java:7460`
  `public static final int btn_select_firmware = 0x7f0a016d;`
- `sources/cn/xiaofengkj/fitpro/R.java:12355`
  `public static final int dfu_status_error_msg = 0x7f1301fd;`
- `sources/cn/xiaofengkj/fitpro/R.java:12356`
  `public static final int dfu_status_fialed = 0x7f1301fe;`
- `sources/cn/xiaofengkj/fitpro/R.java:12357`
  `public static final int dfu_status_foreground_content = 0x7f1301ff;`
- `sources/cn/xiaofengkj/fitpro/R.java:12358`
  `public static final int dfu_status_foreground_title = 0x7f130200;`
- `sources/cn/xiaofengkj/fitpro/R.java:12359`
  `public static final int dfu_status_initializing = 0x7f130201;`
- `sources/cn/xiaofengkj/fitpro/R.java:12360`
  `public static final int dfu_status_starting = 0x7f130202;`
- `sources/cn/xiaofengkj/fitpro/R.java:12361`
  `public static final int dfu_status_starting_msg = 0x7f130203;`
- `sources/cn/xiaofengkj/fitpro/R.java:12362`
  `public static final int dfu_status_successed = 0x7f130204;`
- `sources/cn/xiaofengkj/fitpro/R.java:12363`
  `public static final int dfu_status_switching_to_dfu = 0x7f130205;`
- `sources/cn/xiaofengkj/fitpro/R.java:12364`
  `public static final int dfu_status_switching_to_dfu_msg = 0x7f130206;`
- `sources/cn/xiaofengkj/fitpro/R.java:12365`
  `public static final int dfu_status_uploading = 0x7f130207;`
- `sources/cn/xiaofengkj/fitpro/R.java:12366`
  `public static final int dfu_status_uploading_msg = 0x7f130208;`
- `sources/cn/xiaofengkj/fitpro/R.java:12367`
  `public static final int dfu_status_uploading_part = 0x7f130209;`
- `sources/cn/xiaofengkj/fitpro/R.java:12368`
  `public static final int dfu_status_validating = 0x7f13020a;`
- `sources/cn/xiaofengkj/fitpro/R.java:12369`
  `public static final int dfu_status_validating_msg = 0x7f13020b;`
- `sources/cn/xiaofengkj/fitpro/R.java:12370`
  `public static final int dfu_unknown_name = 0x7f13020c;`
- `sources/cn/xiaofengkj/fitpro/R.java:12639`
  `public static final int htx_ota_dfu_process_starting = 0x7f130319;`
- `sources/cn/xiaofengkj/fitpro/R.java:12640`
  `public static final int htx_ota_dfu_process_starting_status = 0x7f13031a;`
- `sources/cn/xiaofengkj/fitpro/R.java:12641`
  `public static final int htx_ota_dfu_progress = 0x7f13031b;`
- `sources/cn/xiaofengkj/fitpro/R.java:13399`
  `public static final int pref_title_dfu_image_section_size_check_summary_on = 0x7f13060f;`
- `sources/cn/xiaofengkj/fitpro/R.java:13400`
  `public static final int pref_title_dfu_mtu_update = 0x7f130610;`
- `sources/cn/xiaofengkj/fitpro/R.java:13401`
  `public static final int pref_title_dfu_ota_service_uuid = 0x7f130611;`
- `sources/cn/xiaofengkj/fitpro/R.java:13402`
  `public static final int pref_title_dfu_production_priotiry_work_mode = 0x7f130612;`
- `sources/cn/xiaofengkj/fitpro/R.java:13403`
  `public static final int pref_title_dfu_progress_type = 0x7f130613;`
- `sources/cn/xiaofengkj/fitpro/R.java:13404`
  `public static final int pref_title_dfu_speed_control_level = 0x7f130614;`
- `sources/cn/xiaofengkj/fitpro/R.java:13405`
  `public static final int pref_title_dfu_success_hint = 0x7f130615;`
- `sources/cn/xiaofengkj/fitpro/R.java:13406`
  `public static final int pref_title_dfu_throughput = 0x7f130616;`
- `sources/cn/xiaofengkj/fitpro/R.java:13407`
  `public static final int pref_title_dfu_throughput_summary_off = 0x7f130617;`
- `sources/cn/xiaofengkj/fitpro/R.java:13408`
  `public static final int pref_title_dfu_throughput_summary_on = 0x7f130618;`
- `sources/cn/xiaofengkj/fitpro/R.java:13409`
  `public static final int pref_title_dfu_upload_file_prompt = 0x7f130619;`
- `sources/cn/xiaofengkj/fitpro/R.java:13410`
  `public static final int pref_title_dfu_upload_file_prompt_summary_off = 0x7f13061a;`
- `sources/cn/xiaofengkj/fitpro/R.java:13411`
  `public static final int pref_title_dfu_upload_file_prompt_summary_on = 0x7f13061b;`
- `sources/cn/xiaofengkj/fitpro/R.java:13412`
  `public static final int pref_title_dfu_usb_gatt = 0x7f13061c;`
- `sources/cn/xiaofengkj/fitpro/R.java:13413`
  `public static final int pref_title_dfu_usb_gatt_endpoint = 0x7f13061d;`
- `sources/cn/xiaofengkj/fitpro/R.java:13414`
  `public static final int pref_title_dfu_version_check = 0x7f13061e;`
- `sources/cn/xiaofengkj/fitpro/R.java:13415`
  `public static final int pref_title_dfu_version_check_mode = 0x7f13061f;`
- `sources/cn/xiaofengkj/fitpro/R.java:13416`
  `public static final int pref_title_dfu_version_check_summary_off = 0x7f130620;`
- `sources/cn/xiaofengkj/fitpro/R.java:13417`
  `public static final int pref_title_dfu_version_check_summary_on = 0x7f130621;`
- `sources/cn/xiaofengkj/fitpro/R.java:13418`
  `public static final int pref_title_dfu_wait_disconnect_when_enter_ota_mode = 0x7f130622;`
- `sources/cn/xiaofengkj/fitpro/R.java:13419`
  `public static final int pref_title_dfu_workmode_prompt = 0x7f130623;`
- `sources/cn/xiaofengkj/fitpro/R.java:13420`
  `public static final int pref_title_dfu_workmode_prompt_summary_off = 0x7f130624;`
- `sources/cn/xiaofengkj/fitpro/R.java:13421`
  `public static final int pref_title_dfu_workmode_prompt_summary_on = 0x7f130625;`
- `sources/cn/xiaofengkj/fitpro/R.java:13526`
  `public static final int rtk_dfu_action_disconnect = 0x7f13068e;`
- `sources/cn/xiaofengkj/fitpro/R.java:13527`
  `public static final int rtk_dfu_action_reset = 0x7f13068f;`
- `sources/cn/xiaofengkj/fitpro/R.java:13528`
  `public static final int rtk_dfu_action_submit = 0x7f130690;`
- `sources/cn/xiaofengkj/fitpro/R.java:13529`
  `public static final int rtk_dfu_bin_indicator_00 = 0x7f130691;`
- `sources/cn/xiaofengkj/fitpro/R.java:13530`
  `public static final int rtk_dfu_bin_indicator_01 = 0x7f130692;`
- `sources/cn/xiaofengkj/fitpro/R.java:13531`
  `public static final int rtk_dfu_bin_indicator_10 = 0x7f130693;`
- `sources/cn/xiaofengkj/fitpro/R.java:13532`
  `public static final int rtk_dfu_bin_indicator_11 = 0x7f130694;`
- `sources/cn/xiaofengkj/fitpro/R.java:13561`
  `public static final int rtk_dfu_file_type_merge_config_file = 0x7f1306b1;`
- `sources/cn/xiaofengkj/fitpro/R.java:13562`
  `public static final int rtk_dfu_file_type_merge_external_flash_image = 0x7f1306b2;`
- `sources/cn/xiaofengkj/fitpro/R.java:13563`
  `public static final int rtk_dfu_file_type_merge_patch = 0x7f1306b3;`
- `sources/cn/xiaofengkj/fitpro/R.java:13564`
  `public static final int rtk_dfu_file_type_merge_patch_extension = 0x7f1306b4;`
- `sources/cn/xiaofengkj/fitpro/R.java:13565`
  `public static final int rtk_dfu_file_type_merge_user_data = 0x7f1306b5;`
- `sources/cn/xiaofengkj/fitpro/R.java:13566`
  `public static final int rtk_dfu_file_type_pack = 0x7f1306b6;`
- `sources/cn/xiaofengkj/fitpro/R.java:13567`
  `public static final int rtk_dfu_file_type_single = 0x7f1306b7;`
- `sources/cn/xiaofengkj/fitpro/R.java:13568`
  `public static final int rtk_dfu_file_type_unknown = 0x7f1306b8;`
- `sources/cn/xiaofengkj/fitpro/R.java:13569`
  `public static final int rtk_dfu_file_version_text_detail = 0x7f1306b9;`
- `sources/cn/xiaofengkj/fitpro/R.java:13570`
  `public static final int rtk_dfu_image_section_size = 0x7f1306ba;`
- `sources/cn/xiaofengkj/fitpro/R.java:13571`
  `public static final int rtk_dfu_no_available_upload_file = 0x7f1306bb;`
- `sources/cn/xiaofengkj/fitpro/R.java:13572`
  `public static final int rtk_dfu_pref_category_title_general = 0x7f1306bc;`
- `sources/cn/xiaofengkj/fitpro/R.java:13573`
  `public static final int rtk_dfu_pref_title_aes_encrypt = 0x7f1306bd;`
- `sources/cn/xiaofengkj/fitpro/R.java:13574`
  `public static final int rtk_dfu_pref_title_copy_fail = 0x7f1306be;`
- `sources/cn/xiaofengkj/fitpro/R.java:13575`
  `public static final int rtk_dfu_pref_title_skip_fail = 0x7f1306bf;`
- `sources/cn/xiaofengkj/fitpro/R.java:13576`
  `public static final int rtk_dfu_pref_title_stress_test = 0x7f1306c0;`
- `sources/cn/xiaofengkj/fitpro/R.java:13577`
  `public static final int rtk_dfu_progress_state_origin = 0x7f1306c1;`
- `sources/cn/xiaofengkj/fitpro/R.java:13578`
  `public static final int rtk_dfu_scanner_action_cancel = 0x7f1306c2;`
- `sources/cn/xiaofengkj/fitpro/R.java:13579`
  `public static final int rtk_dfu_scanner_action_scan = 0x7f1306c3;`
- `sources/cn/xiaofengkj/fitpro/R.java:13580`
  `public static final int rtk_dfu_scanner_empty = 0x7f1306c4;`
- `sources/cn/xiaofengkj/fitpro/R.java:13581`
  `public static final int rtk_dfu_scanner_subtitle_bonded = 0x7f1306c5;`
- `sources/cn/xiaofengkj/fitpro/R.java:13610`
  `public static final int rtk_dfu_text_collapse = 0x7f1306e2;`
- `sources/cn/xiaofengkj/fitpro/R.java:13611`
  `public static final int rtk_dfu_text_dualbank = 0x7f1306e3;`
- `sources/cn/xiaofengkj/fitpro/R.java:13612`
  `public static final int rtk_dfu_text_file_ic_type = 0x7f1306e4;`
- `sources/cn/xiaofengkj/fitpro/R.java:13613`
  `public static final int rtk_dfu_text_file_image_size = 0x7f1306e5;`
- `sources/cn/xiaofengkj/fitpro/R.java:13614`
  `public static final int rtk_dfu_text_file_image_version = 0x7f1306e6;`
- `sources/cn/xiaofengkj/fitpro/R.java:13615`
  `public static final int rtk_dfu_text_file_name = 0x7f1306e7;`
- `sources/cn/xiaofengkj/fitpro/R.java:13616`
  `public static final int rtk_dfu_text_file_path = 0x7f1306e8;`
- `sources/cn/xiaofengkj/fitpro/R.java:13617`
  `public static final int rtk_dfu_text_file_size = 0x7f1306e9;`

## BR090

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `audit_reports/00_app_summary_and_independent_findings.md:5`
  `本次审计已按 'database_beginner' 的 README、STRUCTURE、TSV 规则表和 'prompts/per_app_beginner_audit_prompt_zh.md' 执行。结论只使用 'confirmed'、'supported_hypothesis'、'not_supported'、'not_testable' 四种状态。BLE 类问题除非有真实设备或动态证据，否则不提升到 'confirmed'；单个权限、单个 SDK、单个 URL、单个字符串不会单独作为 confirmed。`
- `audit_reports/00_app_summary_and_independent_findings.md:71`
  `报告中的 confirmed 只在证据能指向第一方实现或 Manifest 明确配置时确认。第三方 SDK 只作为 supported_hypothesis、not_supported 或 not_testable 的依据，不把 SDK 名称本身当成 confirmed。`
- `audit_reports/00_app_summary_and_independent_findings.md:90`
  `因此动态规则和 BLE 可利用性规则不提升为 confirmed。`
- `audit_reports/01_rule_based_audit.md:3`
  `本报告按 'per_app_beginner_audit_prompt_zh.md' 的章节结构组织。规则结论只使用四种值：'confirmed'、'supported_hypothesis'、'not_supported'、'not_testable'。所有漏洞类型均来自 'rule_catalog.tsv'，未新增 rule_id。`
- `audit_reports/01_rule_based_audit.md:15`
  `## Available Evidence`
- `audit_reports/01_rule_based_audit.md:42`
  `5. BLE 规则如果只有协议构造、UUID、回调解析、缓存 MAC、缺少明显应用层校验，只能 'supported_hypothesis'；没有真实设备时不写 confirmed。`
- `audit_reports/01_rule_based_audit.md:68`
  `结论：'confirmed'`
- `audit_reports/01_rule_based_audit.md:93`
  `结论：'confirmed'`
- `audit_reports/01_rule_based_audit.md:110`
  `- 对社交 app id/app key，部分可能是公开客户端标识，单独不提升为严重 confirmed。`
- `audit_reports/01_rule_based_audit.md:115`
  `结论：'confirmed'`
- `audit_reports/01_rule_based_audit.md:137`
  `- 这不是单个 exported 属性推断。已看到外部入口对应源码可触达健康数据读取、历史数据上传、BLE 写命令、调试模式开启，所以 BR029/BR030/BR059 confirmed。`
- `audit_reports/01_rule_based_audit.md:142`
  `结论：'confirmed'`
- `audit_reports/01_rule_based_audit.md:162`
  `- SQLite 未加密且 schema 包含明确健康/身份/session 字段，满足 BR025 confirmed。`
- `audit_reports/01_rule_based_audit.md:163`
  `- SharedPreferences 明确保存设备地址和健康设置，满足 BR026 confirmed；未把 token 放入 SP。`
- `audit_reports/01_rule_based_audit.md:164`
  `- DB 位于外部 app-specific 目录。现代 Android 访问限制使其不等同于公共根目录，但结合未加密、legacy 外部存储、外部读写权限和日志导出，BR027 可作为 confirmed 的“外部 app-specific 明文健康存储风险”；报告中不声称任意 App 在 Android 11+ 可直接读取。`
- `audit_reports/01_rule_based_audit.md:165`
  `- 备份规则没有排除 DB/session/健康数据，BR028 confirmed，但实际是否被云备份取决于设备、系统和备份服务。`
- `audit_reports/01_rule_based_audit.md:169`
  `结论：'confirmed'`
- `audit_reports/01_rule_based_audit.md:188`
  `- 不是单条 debug 字符串；多条第一方路径写入 token、蓝牙 MAC、BLE 原始包、健康同步对象，满足 BR047 confirmed。`
- `audit_reports/01_rule_based_audit.md:210`
  `- Provider 路径宽是工程风险，但 provider 不导出，不能按 BR021-BR024 confirmed。`
- `audit_reports/01_rule_based_audit.md:235`
  `- 没有真实设备/抓包，不能确认设备端是否另有校验，因此不写 confirmed。`
- `audit_reports/01_rule_based_audit.md:296`
  `结论：'confirmed' 用于代码链存在；真实网络传输字段值未抓包时，对云端实际接收为 'supported_hypothesis'`
- `audit_reports/01_rule_based_audit.md:338`
  `- SDK 和 AD_ID 权限不能单独 confirmed。`
- `audit_reports/01_rule_based_audit.md:366`
  `结论：'confirmed'`
- `audit_reports/01_rule_based_audit.md:379`
  `- URI 明文和 token/userId 静态可确认，不需要抓包也能 confirmed。`
- `audit_reports/01_rule_based_audit.md:419`
  `| BR001 | B023 | Android Permissions Demystified | supported_hypothesis | 权限面很大，含短信/通话/联系人/位置/BLE/外部存储；部分可由通知同步解释，不 confirmed。 |`
- `audit_reports/01_rule_based_audit.md:421`
  `| BR003 | B023 | Android Permissions Demystified | supported_hypothesis | 多个 SDK 命名空间和 AD_ID/Location 相关库存在；SDK 单独不足 confirmed。 |`
- `audit_reports/01_rule_based_audit.md:424`
  `| BR006 | B016 | A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | confirmed | Manifest 'usesCleartextTraffic=true'，network base-config cleartext true。 |`
- `audit_reports/01_rule_based_audit.md:426`
  `| BR008 | B025 | Why Eve and Mallory Still Love Android: Revisiting TLS (In)Security in Android Applications | confirmed | base-config cleartext true，业务明文 WebSocket/HTTP 端点存在。 |`
- `audit_reports/01_rule_based_audit.md:431`
  `| BR013 | B010 | Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues | confirmed | 'ws://hiapi.../websocket/<userId>/<token>'。 |`
- `audit_reports/01_rule_based_audit.md:433`
  `| BR015 | B022 | A Study of Android Application Security | confirmed | 'updateDeviceInfo' 上传 MAC、设备型号、系统版本、语言、手机型号、用户 ID。 |`
- `audit_reports/01_rule_based_audit.md:434`
  `| BR016 | B006 | Analyzing security issues of android mobile health and medical applications | confirmed | 'Constant.TOKEN' hardcoded bearer；strings 有社交/统计 key。 |`
- `audit_reports/01_rule_based_audit.md:436`
  `| BR018 | B001 | Security Concerns in Android mHealth Apps | confirmed | DB/API/BLE 代码有 heart、blood、spo、sleep、step、ECG、profile 字段。 |`
- `audit_reports/01_rule_based_audit.md:443`
  `| BR025 | B005 | Mobile health and privacy: cross sectional study | confirmed | 'ENCRYPTED=false'，SQLite 有健康/profile/session/位置表。 |`
- `audit_reports/01_rule_based_audit.md:444`
  `| BR026 | B002 | Unaddressed privacy risks in accredited health and wellness apps | confirmed | 普通 SharedPreferences 保存蓝牙地址、身高体重、目标、健康功能开关、实时步数。 |`
- `audit_reports/01_rule_based_audit.md:445`
  `| BR027 | B002 | Unaddressed privacy risks in accredited health and wellness apps | confirmed | DB/log/voice 使用外部 app-specific 目录；不夸大为 Android 11+ 任意读取。 |`
- `audit_reports/01_rule_based_audit.md:446`
  `| BR028 | B014 | Privacy Assessment in Mobile Health Apps: Scoping Review | confirmed | 'allowBackup=true'，'cloud-backup'，full backup，无排除敏感 DB。 |`
- `audit_reports/01_rule_based_audit.md:447`
  `| BR029 | B016 | A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | confirmed | 多个 exported Activity 到健康、调试、BLE 命令、支付二维码页面。 |`
- `audit_reports/01_rule_based_audit.md:448`
  `| BR030 | B016 | A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | confirmed | exported 'UploadDataService' onCreate 触发历史健康上传；WebSocket/BLE service 也导出。 |`
- `audit_reports/01_rule_based_audit.md:459`
  `| BR047 | B001 | Security Concerns in Android mHealth Apps | confirmed | 日志输出 token、BLE MAC、WebSocket 消息、健康上传对象、BLE raw hex。 |`
- `audit_reports/01_rule_based_audit.md:465`
  `| BR059 | B006 | Analyzing security issues of android mobile health and medical applications | confirmed | targetSdk 35 但大量 exported=true，多个敏感入口外部可达。 |`
- `audit_reports/02_evidence_chains.md:11`
  `- BR006：'confirmed'`
- `audit_reports/02_evidence_chains.md:12`
  `- BR013：'confirmed'`
- `audit_reports/02_evidence_chains.md:13`
  `- BR047：'confirmed'`
- `audit_reports/02_evidence_chains.md:104`
  `- BR030：'confirmed'`
- `audit_reports/02_evidence_chains.md:105`
  `- BR059：'confirmed'`
- `audit_reports/02_evidence_chains.md:136`
  `- BR029/BR059：'confirmed'`
- `audit_reports/02_evidence_chains.md:167`
  `- BR029：'confirmed'`
- `audit_reports/02_evidence_chains.md:187`
  `结论：'confirmed'`
- `audit_reports/02_evidence_chains.md:213`
  `- 但 DB 未加密、可备份、可由调试/导出功能复制、旧系统/授权文件管理器/USB 备份下更易暴露，仍构成 confirmed 的本地保护不足。`
- `audit_reports/02_evidence_chains.md:221`
  `- BR047：'confirmed'`
- `audit_reports/02_evidence_chains.md:233`
  `为什么 confirmed：`
- `audit_reports/02_evidence_chains.md:261`
  `为什么不是 confirmed：`
- `audit_reports/03_mentor_review.md:47`
  `- BR006、BR013 confirmed 合理。`
- `audit_reports/03_mentor_review.md:48`
  `- BR095 不能 confirmed 到“HTTPS 端点弱 TLS”，因为 Retrofit base URL 是 HTTPS 且未见 permissive TrustManager/HostnameVerifier；因此报告中保持 supported_hypothesis，仅指明明文 WebSocket 和 cleartext config 的传输弱点。`
- `audit_reports/03_mentor_review.md:50`
  `### 2. BLE 缺少应用层安全是否能 confirmed`
- `audit_reports/03_mentor_review.md:64`
  `- 不能 confirmed。设备固件可能在 GATT 层或命令语义外另有校验，反编译 App 侧不能排除。`
- `audit_reports/03_mentor_review.md:67`
  `### 3. 第三方 SDK 是否能作为数据泄露 confirmed`
- `audit_reports/03_mentor_review.md:81`
  `- 不能 confirmed 第三方泄露。`
- `audit_reports/03_mentor_review.md:95`
  `- BR025/BR026/BR028 confirmed 合理。`
- `audit_reports/03_mentor_review.md:111`
  `- BR029/BR030/BR059 confirmed 合理，因为不是单个 exported 属性，已经有敏感动作代码链。`
- `audit_reports/03_mentor_review.md:122`
  `- BR047 confirmed 合理。`
- `audit_reports/03_mentor_review.md:135`
  `- 文件路径宽作为工程风险可在独立观察中保留，但不能按论文规则 confirmed。`
- `audit_reports/03_mentor_review.md:139`
  `高置信 confirmed：`
- `audit_reports/03_mentor_review.md:170`
  `1. BLE 相关没有写 confirmed，全部保守为 supported_hypothesis 或 not_supported。`
- `audit_reports/03_mentor_review.md:171`
  `2. 第三方 SDK 不写 confirmed 泄露，只写 supported_hypothesis。`
- `audit_reports/03_mentor_review.md:172`
  `3. BR095 不写 HTTPS 弱 TLS confirmed，只写明文 WebSocket/cleartext config 支持假设。`
- `audit_reports/03_mentor_review.md:175`
  `6. 对 'Constant.TOKEN' 的 confirmed 限于“硬编码 bearer 被网络请求使用”，不推断服务端一定可被任意滥用。`
- `prompts/rule_code_search_prompt_zh.md:9`
  `- 不写 confirmed / supported_hypothesis / not_supported / not_testable。`
- `prompts/rule_code_search_prompt_zh.md:35`
  `不要输出 confirmed / supported_hypothesis / not_supported / not_testable。`
- `prompts/rule_code_search_prompt_zh.md:951`
  `evidence`
- `prompts/rule_code_search_prompt_zh.md:952`
  `confirmed`
- `prompts/rule_code_search_prompt_zh.md:953`
  `hypothesis`
- `prompts/rule_code_search_prompt_zh.md:989`
  `- evidence`
- `resources/mozilla/public-suffix-list.txt:188`
  `// Confirmed by registry <iana-questions@icann.org> 2008-06-18`
- `resources/mozilla/public-suffix-list.txt:205`
  `// Confirmed by registry <it@nic.at> 2008-06-17`
- `resources/mozilla/public-suffix-list.txt:302`
  `// Confirmed by registry <tech@dns.be> 2008-06-08`
- `resources/mozilla/public-suffix-list.txt:814`
  `// Confirmed by registry <registry@una.net> 2013-03-26`
- `resources/mozilla/public-suffix-list.txt:847`
  `// Confirmed by registry <ops@denic.de> (with technical`
- `resources/mozilla/public-suffix-list.txt:855`
  `// Confirmed by registry <robert@dk-hostmaster.dk> 2008-06-17`
- `resources/mozilla/public-suffix-list.txt:1032`
  `// Confirmed by registry <nigel@channelisles.net> 2013-11-28`

## BR091

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/retrofit2/ServiceMethod.java:152`
  `throw methodError("HTTP method annotation is required (e.g., @GET, @POST, etc.).", new Object[0]);`
- `sources/xfkj/fitpro/api/CommonService.java:79`
  `@FormUrlEncoded`
- `sources/xfkj/fitpro/api/CommonService.java:80`
  `@POST("api/v1/register/email/active/send")`
- `sources/xfkj/fitpro/api/CommonService.java:83`
  `@GET("/api/v1/addfriend/agree")`
- `sources/xfkj/fitpro/api/CommonService.java:86`
  `@POST("/api/v1/convert/8bit")`
- `sources/xfkj/fitpro/api/CommonService.java:87`
  `@Multipart`
- `sources/xfkj/fitpro/api/CommonService.java:90`
  `@FormUrlEncoded`
- `sources/xfkj/fitpro/api/CommonService.java:91`
  `@POST("/api/v1/habbit/add")`
- `sources/xfkj/fitpro/api/CommonService.java:94`
  `@FormUrlEncoded`
- `sources/xfkj/fitpro/api/CommonService.java:95`
  `@POST("/api/v1/habbit/remove")`
- `sources/xfkj/fitpro/api/CommonService.java:98`
  `@FormUrlEncoded`
- `sources/xfkj/fitpro/api/CommonService.java:99`
  `@POST("/api/v1/watchfriend/del")`
- `sources/xfkj/fitpro/api/CommonService.java:103`
  `@GET("api/v1/user/data/export")`
- `sources/xfkj/fitpro/api/CommonService.java:106`
  `@FormUrlEncoded`
- `sources/xfkj/fitpro/api/CommonService.java:107`
  `@POST("/api/v1/user/password/callback")`
- `sources/xfkj/fitpro/api/CommonService.java:110`
  `@POST("/api/v1/advice/list")`
- `sources/xfkj/fitpro/api/CommonService.java:113`
  `@GET("/api/v1/manual/find")`
- `sources/xfkj/fitpro/api/CommonService.java:116`
  `@GET("/wechat/device/get_authorized_qrcode")`
- `sources/xfkj/fitpro/api/CommonService.java:119`
  `@FormUrlEncoded`
- `sources/xfkj/fitpro/api/CommonService.java:120`
  `@POST("/api/v1/step/beatCount")`
- `sources/xfkj/fitpro/api/CommonService.java:123`
  `@FormUrlEncoded`
- `sources/xfkj/fitpro/api/CommonService.java:124`
  `@POST("/api/v1/habbit/rank")`
- `sources/xfkj/fitpro/api/CommonService.java:127`
  `@GET("/api/v1/qiniu/token")`
- `sources/xfkj/fitpro/api/CommonService.java:130`
  `@FormUrlEncoded`
- `sources/xfkj/fitpro/api/CommonService.java:131`
  `@POST("/api/v1/step/realtime/load")`
- `sources/xfkj/fitpro/api/CommonService.java:134`
  `@FormUrlEncoded`
- `sources/xfkj/fitpro/api/CommonService.java:135`
  `@POST("/api/v1/habbit/signCount")`
- `sources/xfkj/fitpro/api/CommonService.java:138`
  `@FormUrlEncoded`
- `sources/xfkj/fitpro/api/CommonService.java:139`
  `@POST("/api/v1/step/myrank")`
- `sources/xfkj/fitpro/api/CommonService.java:142`
  `@GET("/api/v2/watchcharge/status")`
- `sources/xfkj/fitpro/api/CommonService.java:145`
  `@GET("/api/v1/watchpro/version/find/all")`
- `sources/xfkj/fitpro/api/CommonService.java:148`
  `@GET("/api/v1/weather")`
- `sources/xfkj/fitpro/api/CommonService.java:151`
  `@GET("/api/v1/weather/forecast/3day")`
- `sources/xfkj/fitpro/api/CommonService.java:154`
  `@GET("/api/v1/weather/forecast")`
- `sources/xfkj/fitpro/api/CommonService.java:157`
  `@FormUrlEncoded`
- `sources/xfkj/fitpro/api/CommonService.java:158`
  `@POST("/api/v1/app/launch/save")`
- `sources/xfkj/fitpro/api/CommonService.java:161`
  `@FormUrlEncoded`
- `sources/xfkj/fitpro/api/CommonService.java:162`
  `@POST("/api/v1/step/like")`
- `sources/xfkj/fitpro/api/CommonService.java:165`
  `@GET("/api/v1/app/setting/loadall")`
- `sources/xfkj/fitpro/api/CommonService.java:168`
  `@FormUrlEncoded`

## BR092

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `resources/com/androidquery/AbstractAQuery.java:2413`
  `* The temp file will be deleted when AQUtility.cleanCacheAsync is invoked, or the file can be explicitly deleted after use.`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:950`
  `async((Context) act);`
- `resources/com/androidquery/callback/AjaxStatus.java:161`
  `* Close any opened inputstream associated with the response. Call this method when finish parsing the response of a synchronous call.`
- `resources/com/androidquery/util/AQUtility.java:637`
  `AQUtility.report(e);`
- `sources/androidx/activity/ComponentActivity$onBackPressedDispatcher$2.java:55`
  `if (!Intrinsics.areEqual(e.getMessage(), "Can not perform this action after onSaveInstanceState")) {`
- `sources/androidx/appcompat/R.java:1558`
  `public static final int[] SearchView = {android.R.attr.textAppearance, android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.text, android.R.attr.hint, android.R.attr.inputType, android.R.attr.imeOptions, cn.xiaofengkj.fitpro.R.attr.animateMenuItems, cn.xiaofengkj.fitpro.R.attr.animateNa...`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2631`
  `return Api21Impl.isPowerSaveMode(this.mPowerManager) ? 2 : 1;`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2764`
  `static boolean isPowerSaveMode(PowerManager powerManager) {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2765`
  `return powerManager.isPowerSaveMode();`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:214`
  `canvas.save();`
- `sources/androidx/appcompat/view/menu/ActionMenuItemView.java:118`
  `this.mSavedPaddingLeft = i;`
- `sources/androidx/appcompat/widget/ActionMenuPresenter.java:485`
  `public Parcelable onSaveInstanceState() {`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:171`
  `synchronized (this.mInstanceLock) {`
- `sources/androidx/appcompat/widget/AppCompatRatingBar.java:31`
  `protected synchronized void onMeasure(int i, int i2) {`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:138`
  `int iSave = canvas.save();`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:144`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:26`
  `private boolean mAsyncFontPending;`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:107`
  `AppCompatTextHelper.this.onAsyncTypefaceReceived(weakReference, typeface);`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:117`
  `this.mAsyncFontPending = this.mFontTypeface == null;`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:117`
  `ViewCompat.saveAttributeDataForStyleable(textView, textView.getContext(), R.styleable.AppCompatTextView, attributeSet, typedArrayObtainStyledAttributes, i, 0);`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:312`
  `synchronized (rectF) {`
- `sources/androidx/appcompat/widget/SearchView.java:92`
  `private final View mSubmitArea;`
- `sources/androidx/appcompat/widget/SearchView.java:93`
  `private boolean mSubmitButtonEnabled;`
- `sources/androidx/appcompat/widget/SwitchCompat.java:966`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:38`
  `private static class FileCleanupTask extends AsyncTask<Void, Void, Void> {`
- `sources/androidx/camera/camera2/internal/Camera2CameraControlImpl.java:368`
  `return this.mCamera2CapturePipeline.submitStillCaptures(list, i, i2, i3);`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:442`
  `return FutureChain.from(Futures.transformAsyncOnCompletion(captureSession.open(builder.build(), cameraDevice, this.mCaptureSessionOpenerBuilder.build()))).transformAsync(new AsyncFunction() { // from class: androidx.camera.camera2.internal.Camera2CameraImpl$$ExternalSyntheticLambda14`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:443`
  `@Override // androidx.camera.core.impl.utils.futures.AsyncFunction`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1347`
  `void submitCaptureRequests(List<CaptureConfig> list) {`
- `sources/androidx/camera/camera2/internal/Camera2CapturePipeline.java:274`
  `return "submitStillCapture";`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:63`
  `SynchronizedCaptureSession.Opener mSessionOpener;`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:67`
  `SynchronizedCaptureSession mSynchronizedCaptureSession;`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:104`
  `synchronized (this.mSessionLock) {`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:138`
  `Logger.d(TAG, "Attempting to submit CaptureRequest after setting");`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:516`
  `CaptureRequest captureRequestBuild = Camera2CaptureRequestBuilder.build(repeatingCaptureConfig, this.mSynchronizedCaptureSession.getDevice(), this.mConfiguredSurfaceMap, true, this.mTemplateParamsOverride);`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:521`
  `return this.mSynchronizedCaptureSession.setSingleRepeatingRequest(captureRequestBuild, this.mRequestMonitor.createMonitorListener(createCamera2CaptureCallback(repeatingCaptureConfig.getCameraCaptureCallbacks(), new CameraCaptureSession.CaptureCallback[0])));`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:595`
  `CaptureRequest captureRequestBuild = Camera2CaptureRequestBuilder.build(builderFrom.build(), this.mSynchronizedCaptureSession.getDevice(), this.mConfiguredSurfaceMap, false, this.mTemplateParamsOverride);`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:732`
  `CaptureSession.this.mSynchronizedCaptureSession = synchronizedCaptureSession;`
- `sources/androidx/camera/core/AndroidImageReaderProxy.java:72`
  `synchronized (this.mLock) {`
- `sources/androidx/camera/core/CameraX.java:222`
  `String str = "Device reporting less cameras than anticipated. On real devices: Retrying initialization might resolve temporary camera errors. On emulators: Ensure virtual camera configuration matches supported camera features as reported by PackageManager#hasSystemFeature. Available cameras: " + ((C...`

## BR093

paper_id: B004
paper_title: Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation

- `sources/androidx/fragment/app/FragmentLayoutInflaterFactory.java:37`
  `String attributeValue = attributeSet.getAttributeValue(null, InstrumentationResultPrinter.REPORT_KEY_NAME_CLASS);`
- `sources/androidx/navigation/NavBackStackEntry.java:14`
  `import androidx.savedstate.SavedStateRegistry;`
- `sources/androidx/navigation/NavBackStackEntry.java:15`
  `import androidx.savedstate.SavedStateRegistryController;`
- `sources/androidx/navigation/NavBackStackEntry.java:16`
  `import androidx.savedstate.SavedStateRegistryOwner;`
- `sources/androidx/navigation/NavBackStackEntry.java:20`
  `public final class NavBackStackEntry implements LifecycleOwner, ViewModelStoreOwner, HasDefaultViewModelProviderFactory, SavedStateRegistryOwner {`
- `sources/androidx/navigation/NavBackStackEntry.java:30`
  `private final SavedStateRegistryController mSavedStateRegistryController;`
- `sources/androidx/navigation/NavBackStackEntry.java:55`
  `SavedStateRegistryController savedStateRegistryControllerCreate = SavedStateRegistryController.create(this);`
- `sources/androidx/navigation/NavBackStackEntry.java:56`
  `this.mSavedStateRegistryController = savedStateRegistryControllerCreate;`
- `sources/androidx/navigation/NavBackStackEntry.java:64`
  `savedStateRegistryControllerCreate.performRestore(bundle2);`
- `sources/androidx/navigation/NavBackStackEntryState.java:25`
  `private final Bundle mSavedState;`
- `sources/androidx/navigation/NavBackStackEntryState.java:41`
  `Bundle getSavedState() {`
- `sources/androidx/navigation/NavBackStackEntryState.java:42`
  `return this.mSavedState;`
- `sources/androidx/navigation/NavBackStackEntryState.java:54`
  `this.mSavedState = bundle;`
- `sources/androidx/navigation/NavBackStackEntryState.java:55`
  `navBackStackEntry.saveState(bundle);`
- `sources/androidx/navigation/NavBackStackEntryState.java:62`
  `this.mSavedState = parcel.readBundle(getClass().getClassLoader());`
- `sources/androidx/navigation/NavBackStackEntryState.java:70`
  `parcel.writeBundle(this.mSavedState);`
- `sources/androidx/navigation/NavController.java:295`
  `this.mBackStack.add(new NavBackStackEntry(this.mContext, navDestinationFindDestination, args, this.mLifecycleOwner, this.mViewModel, navBackStackEntryState.getUUID(), navBackStackEntryState.getSavedState()));`
- `sources/androidx/test/internal/runner/InstrumentationConnection.java:110`
  `public synchronized void requestRemoteInstancesActivityCleanup() {`
- `sources/androidx/test/internal/runner/InstrumentationConnection.java:141`
  `public synchronized void registerClient(String type, Messenger messenger) {`
- `sources/androidx/test/internal/runner/InstrumentationConnection.java:278`
  `InstrumentationConnection.mInstrumentation.runOnMainSync(InstrumentationConnection.mActivityFinisher);`
- `sources/androidx/test/internal/runner/InstrumentationConnection.java:303`
  `runSyncTask(new Callable<Void>() { // from class: androidx.test.internal.runner.InstrumentationConnection.IncomingHandler.1`
- `sources/androidx/test/internal/runner/InstrumentationConnection.java:314`
  `runSyncTask(new Callable<Void>() { // from class: androidx.test.internal.runner.InstrumentationConnection.IncomingHandler.2`
- `sources/androidx/work/ForegroundUpdater.java:9`
  `ListenableFuture<Void> setForegroundAsync(Context context, UUID id, ForegroundInfo foregroundInfo);`
- `sources/androidx/work/impl/utils/WorkForegroundUpdater.java:31`
  `public ListenableFuture<Void> setForegroundAsync(final Context context, final UUID id, final ForegroundInfo foregroundInfo) {`
- `sources/cn/xiaofengkj/fitpro/R.java:14625`
  `public static final int write_sync_settings_permission = 0x7f130ad9;`
- `sources/com/amazon/aps/ads/ApsAd.java:139`
  `APSAnalytics.logEvent(APSEventSeverity.FATAL, APSEventType.LOG, "Invalid ad format received from the AAX in ApsAd - getApsAdFormat:" + this.width + StringUtils.PROCESS_POSTFIX_DELIMITER + this.height);`
- `sources/com/amazon/device/ads/DTBAdRequest.java:74`
  `private boolean submitMetrics;`
- `sources/com/amazon/device/ads/DTBAdRequest.java:147`
  `this.submitMetrics = true;`
- `sources/com/amazon/device/ads/DTBAdRequest.java:186`
  `this.submitMetrics = true;`
- `sources/com/amazon/device/ads/DTBAdRequest.java:224`
  `this.submitMetrics = true;`
- `sources/com/amazon/device/ads/DTBAdRequest.java:260`
  `this.submitMetrics = true;`
- `sources/com/apm/insight/i/a.java:17`
  `public static synchronized String a(Context context) {`
- `sources/com/apm/insight/i/a.java:31`
  `synchronized (a.class) {`
- `sources/com/apm/insight/k/b.java:120`
  `if (!Npth.isStopUpload() && z) {`
- `sources/com/apm/insight/k/d.java:52`
  `if (z && !Npth.isStopUpload()) {`
- `sources/com/apm/insight/k/d.java:53`
  `jSONObject.put("upload_scene", "direct");`
- `sources/com/applovin/impl/p5.java:97`
  `JsonUtils.putAll(jSONObject, andResetCustomPostBody);`
- `sources/com/applovin/impl/sdk/l.java:862`
  `this.f3737a.r0().a((g5) new p6(this.f3737a, "reportAppExitInfoStackTrace", new Runnable() { // from class: com.applovin.impl.sdk.l$$ExternalSyntheticLambda0`
- `sources/com/applovin/impl/sdk/network/d.java:139`
  `return "PostbackRequest{uniqueId='" + this.f3761a + "', communicatorRequestId='" + this.m + "', httpMethod='" + this.b + "', targetUrl='" + this.c + "', backupUrl='" + this.d + "', attemptNumber=" + this.n + ", isEncodingEnabled=" + this.i + ", isGzipBodyEncoding=" + this.j + ", isAllowedPreInitEven...`
- `sources/com/beken/beken_ota/ble/BluetoothLeService.java:16`
  `import com.beken.beken_ota.EventBusReportItem;`

## BR094

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/com/androidquery/WebDialog.java:44`
  `protected void onCreate(Bundle savedInstanceState) {`
- `resources/com/androidquery/WebDialog.java:46`
  `super.onCreate(savedInstanceState);`
- `resources/com/androidquery/WebDialog.java:101`
  `//ws.setSaveFormData(false);`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:793`
  `AQUtility.report(e);`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:809`
  `AQUtility.report(e);`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:821`
  `AQUtility.report(e);`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:931`
  `* Starts the async process.`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:938`
  `public void async(Activity act){`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:1342`
  `//convert get to post request, if url length is too long to be handled on web`
- `resources/com/androidquery/callback/AjaxStatus.java:161`
  `* Close any opened inputstream associated with the response. Call this method when finish parsing the response of a synchronous call.`
- `resources/com/androidquery/callback/LocationAjaxCallback.java:58`
  `public void async(Context context){`
- `resources/com/androidquery/callback/LocationAjaxCallback.java:172`
  `// if this loc is network and there's already an recent async gps update`
- `resources/com/androidquery/util/AQUtility.java:343`
  `public static void removePost(Runnable run){`
- `resources/com/androidquery/util/AQUtility.java:347`
  `public static void postDelayed(Runnable run, long delay){`
- `resources/com/androidquery/util/AQUtility.java:348`
  `getHandler().postDelayed(run, delay);`
- `resources/com/androidquery/util/AQUtility.java:488`
  `public static void storeAsync(File file, byte[] data, long delay){`
- `resources/com/androidquery/util/AQUtility.java:595`
  `public static void cleanCacheAsync(Context context){`
- `resources/com/androidquery/util/AQUtility.java:599`
  `cleanCacheAsync(context, triggerSize, targetSize);`
- `resources/com/androidquery/util/AQUtility.java:602`
  `public static void cleanCacheAsync(Context context, long triggerSize, long targetSize){`
- `resources/com/androidquery/util/AQUtility.java:614`
  `AQUtility.report(e);`
- `resources/com/androidquery/util/RatioDrawable.java:198`
  `m.postTranslate(dx, dy);`
- `resources/com/google/firebase/crashlytics/buildtools/reloc/javax/annotation/concurrent/Immutable.java:30`
  `* threads or published without synchronization.`
- `resources/com/google/firebase/crashlytics/buildtools/reloc/javax/annotation/meta/When.java:7`
  `* In particular, an issues should be reported if an ALWAYS or MAYBE value is`
- `sources/android/support/customtabs/ICustomTabsCallback.java:54`
  `public void onPostMessage(String str, Bundle bundle) throws RemoteException {`
- `sources/android/support/customtabs/ICustomTabsCallback.java:84`
  `void onPostMessage(String str, Bundle bundle) throws RemoteException;`
- `sources/android/support/customtabs/ICustomTabsCallback.java:100`
  `static final int TRANSACTION_onPostMessage = 5;`
- `sources/android/support/customtabs/ICustomTabsCallback.java:147`
  `onPostMessage(parcel.readString(), (Bundle) _Parcel.readTypedObject(parcel, Bundle.CREATOR));`
- `sources/android/support/customtabs/ICustomTabsService.java:126`
  `static final int TRANSACTION_requestPostMessageChannel = 7;`
- `sources/android/support/customtabs/ICustomTabsService.java:127`
  `static final int TRANSACTION_requestPostMessageChannelWithExtras = 11;`
- `sources/android/support/customtabs/ICustomTabsService.java:195`
  `int iPostMessage = postMessage(ICustomTabsCallback.Stub.asInterface(parcel.readStrongBinder()), parcel.readString(), (Bundle) _Parcel.readTypedObject(parcel, Bundle.CREATOR));`
- `sources/android/support/customtabs/ICustomTabsService.java:197`
  `parcel2.writeInt(iPostMessage);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1671`
  `synchronized (MediaSessionImplBase.this.mLock) {`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1750`
  `postToHandler(10, uri, bundle);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1755`
  `postToHandler(11, Long.valueOf(j));`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1760`
  `postToHandler(12);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1785`
  `postToHandler(17);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1790`
  `postToHandler(18, Long.valueOf(j));`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1795`
  `postToHandler(19, ratingCompat);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:2168`
  `MediaSessionImplApi18.this.postToHandler(18, -1, -1, Long.valueOf(j), null);`
- `sources/androidx/activity/ComponentActivity.java:876`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0007\n\u0002\u0010\t\n\u0002\b\u0003\n\u0002\u0010\u000b\n\u0002\b\u0005\n\u0002\u0010\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0000\b\u0082\u0004\u0018\u00002\u00020\u00012\u00020...`

## BR095

paper_id: B025
paper_title: Why Eve and Mallory Still Love Android: Revisiting TLS (In)Security in Android Applications

- `resources/LICENSES.txt:287`
  `<http://lists.debian.org/debian-legal/2004/12/msg00295.html>, it gives an`
- `resources/assets/mbridge_download_dialog_view.xml:2`
  `<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/assets/mbridge_download_dialog_view.xml:3`
  `xmlns:app="http://schemas.android.com/apk/res-auto"`
- `resources/assets/html/faq.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html/index.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html/privacy_in.html:1192`
  `mso-bidi-font-family:&#39;Times New Roman&#39;;font-size:10.5000pt;mso-font-kerning:1.0000pt;"><o:p></o:p></span></p></div><div id="goog-gt-tt" class="skiptranslate" dir="ltr"><div style="padding: 8px;"><div><div class="logo"></div></div></div><div class="top" style="padding: 8px; float: left; width...`
- `resources/assets/html/user_guide.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-en/faq.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-en/index.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-en/user_guide.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-zh-rCN/faq.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-zh-rCN/index.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-zh-rCN/user_guide.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-zh-rHK/faq.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-zh-rHK/index.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-zh-rHK/user_guide.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-zh-rTW/faq.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-zh-rTW/index.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/assets/html-zh-rTW/user_guide.html:10`
  `<!--<a href="http://github.com/zxing/zxing">http://github.com/zxing/zxing</a></p>-->`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:1176`
  `//reference: http://stackoverflow.com/questions/11735636/how-to-get-401-response-without-handling-it-using-try-catch-in-android`
- `resources/META-INF/commons-codec-1.10/META-INF/NOTICE.txt:5`
  `The Apache Software Foundation (http://www.apache.org/).`
- `resources/META-INF/commons-codec-1.10/META-INF/NOTICE.txt:8`
  `contains test data from http://aspell.net/test/orig/batch0.tab.`
- `resources/META-INF/commons-codec-1.10/META-INF/NOTICE.txt:14`
  `from the original php source code available at http://stevemorse.org/phoneticinfo.htm`
- `resources/mozilla/public-suffix-list.txt:432`
  `// br : http://registro.br/dominio/categoria.html`
- `resources/mozilla/public-suffix-list.txt:3645`
  `// http://www.dot.kn/domainRules.html`
- `resources/mozilla/public-suffix-list.txt:3816`
  `// http://www.anrt.ma/fr/admin/download/upload/file_fr782.pdf`
- `resources/mozilla/public-suffix-list.txt:3873`
  `// ml : http://www.gobin.info/domainname/ml-template.doc`
- `resources/mozilla/public-suffix-list.txt:3904`
  `// mp : http://www.dot.mp/`
- `resources/mozilla/public-suffix-list.txt:5499`
  `// ph : http://www.domains.ph/FAQ2.asp`
- `resources/mozilla/public-suffix-list.txt:6731`
  `// http://nic.ae/english/arabicdomain/rules.jsp`
- `resources/mozilla/public-suffix-list.txt:6873`
  `// http://nic.lk`
- `resources/mozilla/public-suffix-list.txt:11677`
  `// Futureweb OG : http://www.futureweb.at`
- `resources/mozilla/public-suffix-list.txt:11899`
  `// JS.ORG : http://dns.js.org`
- `resources/mozilla/public-suffix-list.txt:11907`
  `// KnightPoint Systems, LLC : http://www.knightpoint.com/`
- `resources/mozilla/public-suffix-list.txt:11911`
  `// .KRD : http://nic.krd/data/krd/Registration%20Policy.pdf`
- `resources/mozilla/public-suffix-list.txt:12183`
  `// NYC.mn : http://www.information.nyc.mn`
- `resources/mozilla/public-suffix-list.txt:12245`
  `// One Fold Media : http://www.onefoldmedia.com/`
- `resources/mozilla/public-suffix-list.txt:12366`
  `// Revitalised Limited : http://www.revitalised.co.uk`
- `resources/mozilla/public-suffix-list.txt:12462`
  `// Studenten Net Twente : http://www.snt.utwente.nl/`
- `resources/mozilla/public-suffix-list.txt:12466`
  `// Sub 6 Limited: http://www.sub6.com`
- `resources/res/color/selector_step_number_bottom_week_color.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
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
- `resources/res/drawable/admob_close_button_black_circle_white_cross.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/admob_close_button_white_circle_black_cross.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/admob_close_button_white_cross.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/applovin_ic_mediation_placeholder.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/res/drawable/applovin_mediation_debugger_switch_thumb.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/applovin_mediation_debugger_switch_track.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/avd_hide_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_hide_password__0_res_0x7f08000a">`
- `resources/res/drawable/avd_show_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_show_password__0_res_0x7f08000d">`
- `resources/res/drawable/baseline_ios_share_24.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/begin_marker.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/bigo_ad_banner_button_bg_rectangle_blue.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/res/drawable/bigo_ad_button_bg_circle_grey.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/bigo_ad_button_bg_rectangle_blue.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/res/drawable/bigo_ad_button_bg_rectangle_blue_2.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/res/drawable/bigo_ad_button_bg_rectangle_green.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/res/drawable/bigo_ad_button_stroke_circle_white.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/bigo_ad_cardview_bg.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/res/drawable/bigo_ad_click_guide2.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/bigo_ad_click_ripple.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/bigo_ad_close_btn_background.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/bigo_ad_domain_left_drawable.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`

## BR096

paper_id: B011
paper_title: Locking it down: The privacy and security of mobile medication apps

- `resources/assets/aps-mraid.js:1`
  `/*! @amzn/aps-mraid.js - v1.4.0 - 2023-08-01 15:21:05 */!function(n){var o={};function r(e){var t;return(o[e]||(t=o[e]={i:e,l:!1,exports:{}},n[e].call(t.exports,t,t.exports,r),t.l=!0,t)).exports}r.m=n,r.c=o,r.d=function(e,t,n){r.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},r.r=function(...`
- `resources/assets/dtb-m.js:1`
  `/*! @amzn/dtb-m.js - v2.47.0 - 2024-08-27 15:56:23 */!function(){"use strict";var e;!function(e){e.info="info",e.warn="warn",e.error="error"}(e||(e={}));class t{static Instance(){return this._instance}static SessionId(){return this._sessionId}info(...t){const n=new Date(Date.now()),r=e.info;return c...`
- `resources/assets/html/privacy_in.html:3`
  `<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns:dt="uuid:C2F41010-65B3-11d1-A29F-00AA00C14882" xmlns="http://www.w3.org/TR/REC-html40" class="translated-ltr"><head><meta http-equiv="Content-Type" content="text/html; charset=GBK"><meta nam...`
- `resources/com/androidquery/auth/FacebookHandle.java:49`
  `private static final String OAUTH_ENDPOINT = "https://graph.facebook.com/oauth/authorize";`
- `resources/com/androidquery/auth/FacebookHandle.java:50`
  `private static final String REDIRECT_URI = "https://www.facebook.com/connect/login_success.html";`
- `resources/com/androidquery/auth/TwitterHandle.java:32`
  `private static final String OAUTH_REQUEST_TOKEN = "https://api.twitter.com/oauth/request_token";`
- `resources/com/androidquery/auth/TwitterHandle.java:33`
  `private static final String OAUTH_ACCESS_TOKEN = "https://api.twitter.com/oauth/access_token";`
- `resources/com/androidquery/auth/TwitterHandle.java:34`
  `private static final String OAUTH_AUTHORIZE = "https://api.twitter.com/oauth/authorize";`
- `resources/com/androidquery/callback/AbstractAjaxCallback.java:1503`
  `//http://stackoverflow.com/questions/3046424/http-post-requests-using-httpclient-take-2-seconds-why`
- `resources/com/androidquery/service/MarketService.java:215`
  `return "https://androidquery.appspot.com";`
- `resources/mozilla/public-suffix-list.txt:310`
  `// bg : https://en.wikipedia.org/wiki/.bg`
- `resources/mozilla/public-suffix-list.txt:632`
  `// bz : https://en.wikipedia.org/wiki/.bz`
- `resources/mozilla/public-suffix-list.txt:854`
  `// dk : https://en.wikipedia.org/wiki/.dk`
- `resources/mozilla/public-suffix-list.txt:858`
  `// dm : https://en.wikipedia.org/wiki/.dm`
- `resources/mozilla/public-suffix-list.txt:1028`
  `// gf : https://en.wikipedia.org/wiki/.gf`
- `resources/mozilla/public-suffix-list.txt:1031`
  `// gg : http://www.channelisles.net/register-domains/`
- `resources/mozilla/public-suffix-list.txt:1763`
  `// je : http://www.channelisles.net/register-domains/`
- `resources/mozilla/public-suffix-list.txt:1770`
  `// jm : http://www.com.jm/register.html`
- `resources/mozilla/public-suffix-list.txt:3815`
  `// ma : https://en.wikipedia.org/wiki/.ma`
- `resources/mozilla/public-suffix-list.txt:3862`
  `// mk : https://en.wikipedia.org/wiki/.mk`
- `resources/mozilla/public-suffix-list.txt:3863`
  `// see also: http://dns.marnet.net.mk/postapka.php`
- `resources/mozilla/public-suffix-list.txt:4604`
  `// ng : http://www.nira.org.ng/index.php/join-us/register-ng-domain/189-nira-slds`
- `resources/mozilla/public-suffix-list.txt:5409`
  `// np : http://www.mos.com.np/register.html`
- `resources/mozilla/public-suffix-list.txt:5412`
  `// nr : http://cenpac.net.nr/dns/index.html`
- `resources/mozilla/public-suffix-list.txt:5746`
  `// post : https://en.wikipedia.org/wiki/.post`
- `resources/mozilla/public-suffix-list.txt:10717`
  `// Alces Software Ltd : http://alces-software.com`
- `resources/mozilla/public-suffix-list.txt:10722`
  `// alwaysdata : https://www.alwaysdata.com`
- `resources/mozilla/public-suffix-list.txt:10726`
  `// Amazon CloudFront : https://aws.amazon.com/cloudfront/`
- `resources/mozilla/public-suffix-list.txt:10730`
  `// Amazon Elastic Compute Cloud : https://aws.amazon.com/ec2/`
- `resources/mozilla/public-suffix-list.txt:10737`
  `// Amazon Elastic Beanstalk : https://aws.amazon.com/elasticbeanstalk/`
- `resources/mozilla/public-suffix-list.txt:10948`
  `// certmgr.org : https://certmgr.org`
- `resources/mozilla/public-suffix-list.txt:10952`
  `// Citrix : https://citrix.com`
- `resources/mozilla/public-suffix-list.txt:10960`
  `// Clever Cloud : https://www.clever-cloud.com/`
- `resources/mozilla/public-suffix-list.txt:10964`
  `// Cloud66 : https://www.cloud66.com/`
- `resources/mozilla/public-suffix-list.txt:10969`
  `// CloudAccess.net : https://www.cloudaccess.net/`
- `resources/mozilla/public-suffix-list.txt:10977`
  `// cloudControl : https://www.cloudcontrol.com/`
- `resources/mozilla/public-suffix-list.txt:10982`
  `// co.ca : http://registry.co.ca/`
- `resources/mozilla/public-suffix-list.txt:11001`
  `// Cloud DNS Ltd : http://www.cloudns.net`
- `resources/mozilla/public-suffix-list.txt:11015`
  `// Cloudeity Inc : https://cloudeity.com`
- `resources/mozilla/public-suffix-list.txt:11027`
  `// Combell.com : https://www.combell.com`
- `resources/mozilla/public-suffix-list.txt:11032`
  `// COSIMO GmbH : http://www.cosimo.de`
- `resources/mozilla/public-suffix-list.txt:11044`
  `// Craynic, s.r.o. : http://www.craynic.com/`
- `resources/mozilla/public-suffix-list.txt:11061`
  `// Daplie, Inc : https://daplie.com`
- `resources/mozilla/public-suffix-list.txt:11066`
  `// Datto, Inc. : https://www.datto.com/`
- `resources/mozilla/public-suffix-list.txt:11099`
  `// DreamHost : http://www.dreamhost.com/`
- `resources/mozilla/public-suffix-list.txt:11103`
  `// Drobo : http://www.drobo.com/`
- `resources/mozilla/public-suffix-list.txt:11414`
  `// Definima : http://www.definima.com/`
- `resources/mozilla/public-suffix-list.txt:11460`
  `// EU.org https://eu.org/`
- `resources/mozilla/public-suffix-list.txt:11530`
  `// eDirect Corp. : https://hosting.url.com.tw/`
- `resources/mozilla/public-suffix-list.txt:11639`
  `// Featherhead : https://featherhead.xyz/`
- `resources/mozilla/public-suffix-list.txt:11643`
  `// Fedora : https://fedoraproject.org/`
- `resources/mozilla/public-suffix-list.txt:11659`
  `// Flynn : https://flynn.io`
- `resources/mozilla/public-suffix-list.txt:11907`
  `// KnightPoint Systems, LLC : http://www.knightpoint.com/`
- `resources/mozilla/public-suffix-list.txt:11921`
  `// Lightmaker Property Manager, Inc. : https://app.lmpm.com/`
- `resources/mozilla/public-suffix-list.txt:11934`
  `// LiquidNet Ltd : http://www.liquidnetlimited.com/`
- `resources/mozilla/public-suffix-list.txt:11945`
  `// Lukanet Ltd : https://lukanet.com`
- `resources/mozilla/public-suffix-list.txt:11975`
  `// May First - People Link : https://mayfirst.org/`
- `resources/mozilla/public-suffix-list.txt:11984`
  `// Memset hosting : https://www.memset.com`
- `resources/mozilla/public-suffix-list.txt:11999`
  `// Meteor Development Group : https://www.meteor.com/hosting`
- `resources/mozilla/public-suffix-list.txt:12014`
  `// Mozilla Corporation : https://mozilla.com`
- `resources/mozilla/public-suffix-list.txt:12041`
  `// Nimbus Hosting Ltd. : https://www.nimbushosting.co.uk/`
- `resources/mozilla/public-suffix-list.txt:12045`
  `// NFSN, Inc. : https://www.NearlyFreeSpeech.NET/`
- `resources/mozilla/public-suffix-list.txt:12049`
  `// Now-DNS : https://now-dns.com`
- `resources/mozilla/public-suffix-list.txt:12179`
  `// Nucleos Inc. : https://nucleos.com`
- `resources/mozilla/public-suffix-list.txt:12241`
  `// Omnibond Systems, LLC. : https://www.omnibond.com`
- `resources/mozilla/public-suffix-list.txt:12245`
  `// One Fold Media : http://www.onefoldmedia.com/`
- `resources/mozilla/public-suffix-list.txt:12249`
  `// OpenCraft GmbH : http://opencraft.com/`
- `resources/mozilla/public-suffix-list.txt:12261`
  `// OwnProvider GmbH: http://www.ownprovider.com`
- `resources/mozilla/public-suffix-list.txt:12333`
  `// QNAP System Inc : https://www.qnap.com`
- `resources/mozilla/public-suffix-list.txt:12339`
  `// Quip : https://quip.com`
- `resources/mozilla/public-suffix-list.txt:12343`
  `// Qutheory LLC : http://qutheory.io`
- `resources/mozilla/public-suffix-list.txt:12348`
  `// Rackmaze LLC : https://www.rackmaze.com`
- `resources/mozilla/public-suffix-list.txt:12353`
  `// Red Hat, Inc. OpenShift : https://openshift.redhat.com/`
- `resources/mozilla/public-suffix-list.txt:12357`
  `// Resin.io : https://resin.io`
- `resources/mozilla/public-suffix-list.txt:12402`
  `// SensioLabs, SAS : https://sensiolabs.com/`
- `resources/mozilla/public-suffix-list.txt:12421`
  `// SinaAppEngine : http://sae.sina.com.cn/`
- `resources/mozilla/public-suffix-list.txt:12458`
  `// Storj Labs Inc. : https://storj.io/`
- `resources/mozilla/public-suffix-list.txt:12470`
  `// Synology, Inc. : https://www.synology.com/`
- `resources/mozilla/public-suffix-list.txt:12567`
  `// UDR Limited : http://www.udr.hk.com`
- `resources/mozilla/public-suffix-list.txt:12587`
  `// Viprinet Europe GmbH : http://www.viprinet.com`

## BR097

paper_id: B019
paper_title: Pulse Oximeter App Privacy Policies During COVID-19: Scoping Assessment

- `sources/xfkj/fitpro/websocket/JWebSocketClientService.java:42`
  `private URI uri = URI.create(String.format("ws://hiapi.jusonsmart.com:7780/websocket/%1$s/%2$s", Long.valueOf(DBHelper.getUserId()), DBHelper.getUserToken().replaceAll(HelpFormatter.DEFAULT_LONG_OPT_SEPARATOR, HelpFormatter.DEFAULT_OPT_PREFIX)));`

## BR098

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/com/amazon/aps/ads/util/adview/ApsAdViewFetchUtils.java:183`
  `webView.loadDataWithBaseURL("https://c.amazon-adsystem.com/", sb.toString(), "text/html", "UTF-8", null);`
- `sources/com/amazon/aps/ads/util/adview/ApsAdViewFetchUtils.java:202`
  `webView.loadDataWithBaseURL("https://c.amazon-adsystem.com/", sb.toString(), "text/html", "UTF-8", null);`
- `sources/com/applovin/impl/adview/a.java:912`
  `this.o.loadDataWithBaseURL((String) this.c.a(v4.Z6), "<html><head><link rel=\"icon\" href=\"data:,\"><G-SCRIPT_TAG></head><body></body></html>".replace("<G-SCRIPT_TAG>", "<script src='https://www.googletagmanager.com/gtag/js?id=<G-TRACKING_ID>'></script><script>window.dataLayer = window.dataLayer ||...`
- `sources/com/inmobi/media/C2947c3.java:25`
  `OkHttpClient.Builder builder = new OkHttpClient.Builder();`
- `sources/com/lzy/okgo/OkGo.java:88`
  `OkHttpClient.Builder builder = new OkHttpClient.Builder();`
- `sources/com/onmicro/omtoolbox/network/Api.java:18`
  `apiService = (ApiService) new Retrofit.Builder().client(new OkHttpClient.Builder().readTimeout(7676L, TimeUnit.MILLISECONDS).connectTimeout(7676L, TimeUnit.MILLISECONDS).build()).baseUrl(BASE_URL).addConverterFactory(GsonConverterFactory.create()).addCallAdapterFactory(RxJava2CallAdapterFactory.crea...`
- `sources/com/vungle/ads/internal/network/VungleApiClient.java:265`
  `OkHttpClient.Builder builderProxySelector = new OkHttpClient.Builder().readTimeout(60L, TimeUnit.SECONDS).connectTimeout(60L, TimeUnit.SECONDS).addInterceptor(this.responseInterceptor).proxySelector(new ProxySelector() { // from class: com.vungle.ads.internal.network.VungleApiClient$builder$1`
- `sources/com/yandex/mobile/ads/impl/fk.java:36`
  `loadDataWithBaseURL("https://yandex.ru", a(sourcePageData), "text/html", "UTF-8", null);`
- `sources/sg/bigo/ads/core/g/a/b.java:345`
  `loadDataWithBaseURL("http://127.0.0.1/", "<html lang=\"en\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n    <meta charset=\"UTF-8\">\n    <title>VPAID AD</title>\n    <script>\n        window.onload = function() {\n            tryToPrepareAd();\n        }\n\n        document.onreadystatechange ...`
- `sources/sg/bigo/ads/core/mraid/c.java:366`
  `this.g.loadDataWithBaseURL("https://mraid.bigo.sg", str, "text/html", null, null);`
- `sources/xfkj/fitpro/api/NetWorkManager.java:75`
  `Retrofit retrofitBuild = new Retrofit.Builder().baseUrl(Api.APP_SERVICE_DOMAIN).addCallAdapterFactory(RxJava2CallAdapterFactory.create()).addConverterFactory(GsonConverterFactory.create(gsonCreate)).client(this.mOkHttpClient).build();`
- `sources/xfkj/fitpro/api/NetWorkManager.java:92`
  `OkHttpClient.Builder builder = new OkHttpClient.Builder();`
- `sources/yqy/yichip/ota3genbandupgrade/request/RequestUtil.java:15`
  `Call<dataFile> call = ((GetRequestDataFile_Interface) new Retrofit.Builder().baseUrl(str).addConverterFactory(GsonConverterFactory.create()).build().create(GetRequestDataFile_Interface.class)).getCall();`
