# Rule Search Hits

## BR002

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/com.ble_health_plus.apk/AndroidManifest.xml:17`
  `<uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM"/>`
- `resources/com.ble_health_plus.apk/AndroidManifest.xml:18`
  `<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>`
- `resources/com.ble_health_plus.apk/AndroidManifest.xml:19`
  `<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>`
- `resources/com.ble_health_plus.apk/AndroidManifest.xml:20`
  `<uses-permission`

## BR003

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/com.ble_health_plus.apk/AndroidManifest.xml:14`
  `<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>`
- `resources/com.ble_health_plus.apk/AndroidManifest.xml:15`
  `<uses-permission android:name="android.permission.BLUETOOTH_CONNECT"/>`
- `resources/com.ble_health_plus.apk/AndroidManifest.xml:16`
  `<uses-permission android:name="android.permission.BLUETOOTH_ADMIN"/>`
- `resources/com.ble_health_plus.apk/AndroidManifest.xml:17`
  `<uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM"/>`
- `resources/com.ble_health_plus.apk/AndroidManifest.xml:20`
  `<uses-permission`
- `resources/com.ble_health_plus.apk/AndroidManifest.xml:23`
  `<uses-permission android:name="android.permission.BLUETOOTH"/>`
- `resources/com.ble_health_plus.apk/AndroidManifest.xml:24`
  `<uses-permission android:name="android.permission.BLUETOOTH_ADVERTISE"/>`
- `resources/com.ble_health_plus.apk/AndroidManifest.xml:25`
  `<uses-permission android:name="android.permission.EXPAND_STATUS_BAR"/>`

## BR006

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/com.ble_health_plus.apk/AndroidManifest.xml:47`
  `android:usesCleartextTraffic="true"`

## BR009

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/com/google/api/client/json/webtoken/JsonWebSignature.java:24`
  `import javax.net.ssl.X509TrustManager;`
- `sources/com/google/api/client/json/webtoken/JsonWebSignature.java:172`
  `public final X509Certificate verifySignature(X509TrustManager x509TrustManager) throws GeneralSecurityException {`
- `sources/com/google/api/client/json/webtoken/JsonWebSignature.java:177`
  `return SecurityUtils.verify(SecurityUtils.getSha256WithRsaSignatureAlgorithm(), x509TrustManager, x509Certificates, this.signatureBytes, this.signedContentBytes);`
- `sources/com/google/api/client/json/webtoken/JsonWebSignature.java:180`
  `return SecurityUtils.verify(SecurityUtils.getEs256SignatureAlgorithm(), x509TrustManager, x509Certificates, DerEncoder.encode(this.signatureBytes), this.signedContentBytes);`
- `sources/com/google/api/client/json/webtoken/JsonWebSignature.java:187`
  `X509TrustManager defaultX509TrustManager = getDefaultX509TrustManager();`
- `sources/com/google/api/client/json/webtoken/JsonWebSignature.java:188`
  `if (defaultX509TrustManager == null) {`
- `sources/com/google/api/client/json/webtoken/JsonWebSignature.java:191`
  `return verifySignature(defaultX509TrustManager);`
- `sources/com/google/api/client/json/webtoken/JsonWebSignature.java:194`
  `private static X509TrustManager getDefaultX509TrustManager() {`
- `sources/com/google/api/client/json/webtoken/JsonWebSignature.java:202`
  `if (trustManager instanceof X509TrustManager) {`
- `sources/com/google/api/client/json/webtoken/JsonWebSignature.java:203`
  `return (X509TrustManager) trustManager;`
- `sources/com/google/api/client/testing/json/webtoken/TestCertificates.java:19`
  `import javax.net.ssl.X509TrustManager;`
- `sources/com/google/api/client/testing/json/webtoken/TestCertificates.java:50`
  `public X509TrustManager getTrustManager() throws GeneralSecurityException, IOException {`
- `sources/com/google/api/client/testing/json/webtoken/TestCertificates.java:56`
  `return (X509TrustManager) trustManagerFactory.getTrustManagers()[0];`
- `sources/com/google/api/client/util/SecurityUtils.java:25`
  `import javax.net.ssl.X509TrustManager;`
- `sources/com/google/api/client/util/SecurityUtils.java:90`
  `public static X509Certificate verify(Signature signature, X509TrustManager x509TrustManager, List<String> list, byte[] bArr, byte[] bArr2) throws SignatureException, InvalidKeyException {`
- `sources/com/google/api/client/util/SecurityUtils.java:109`
  `x509TrustManager.checkServerTrusted(x509CertificateArr, "RSA");`
- `sources/com/google/api/client/util/SslUtils.java:14`
  `import javax.net.ssl.X509TrustManager;`
- `sources/com/google/api/client/util/SslUtils.java:56`
  `TrustManager[] trustManagerArr = {new X509TrustManager() { // from class: com.google.api.client.util.SslUtils.1`
- `sources/com/google/api/client/util/SslUtils.java:57`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/com/google/api/client/util/SslUtils.java:58`
  `public void checkClientTrusted(X509Certificate[] x509CertificateArr, String str) throws CertificateException {`
- `sources/com/google/api/client/util/SslUtils.java:61`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/com/google/api/client/util/SslUtils.java:62`
  `public void checkServerTrusted(X509Certificate[] x509CertificateArr, String str) throws CertificateException {`
- `sources/com/google/api/client/util/SslUtils.java:65`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/okhttp3/OkHttpClient.java:21`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/OkHttpClient.java:46`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000î\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u001a\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u00...`
- `sources/okhttp3/OkHttpClient.java:77`
  `private final X509TrustManager x509TrustManager;`
- `sources/okhttp3/OkHttpClient.java:140`
  `this.x509TrustManager = null;`
- `sources/okhttp3/OkHttpClient.java:147`
  `X509TrustManager x509TrustManagerOrNull = builder.getX509TrustManagerOrNull();`
- `sources/okhttp3/OkHttpClient.java:148`
  `Intrinsics.checkNotNull(x509TrustManagerOrNull);`
- `sources/okhttp3/OkHttpClient.java:149`
  `this.x509TrustManager = x509TrustManagerOrNull;`
- `sources/okhttp3/OkHttpClient.java:154`
  `X509TrustManager x509TrustManagerPlatformTrustManager = Platform.INSTANCE.get().platformTrustManager();`
- `sources/okhttp3/OkHttpClient.java:155`
  `this.x509TrustManager = x509TrustManagerPlatformTrustManager;`
- `sources/okhttp3/OkHttpClient.java:157`
  `Intrinsics.checkNotNull(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/OkHttpClient.java:158`
  `this.sslSocketFactoryOrNull = platform.newSslSocketFactory(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/OkHttpClient.java:160`
  `Intrinsics.checkNotNull(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/OkHttpClient.java:161`
  `CertificateChainCleaner certificateChainCleaner2 = companion.get(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/OkHttpClient.java:246`
  `/* JADX INFO: renamed from: x509TrustManager, reason: from getter */`
- `sources/okhttp3/OkHttpClient.java:247`
  `public final X509TrustManager getX509TrustManager() {`
- `sources/okhttp3/OkHttpClient.java:248`
  `return this.x509TrustManager;`
- `sources/okhttp3/OkHttpClient.java:339`
  `if (!(this.x509TrustManager == null)) {`
- `sources/okhttp3/OkHttpClient.java:353`
  `if (this.x509TrustManager == null) {`
- `sources/okhttp3/OkHttpClient.java:354`
  `throw new IllegalStateException("x509TrustManager == null".toString());`
- `sources/okhttp3/OkHttpClient.java:534`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000ø\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b...`
- `sources/okhttp3/OkHttpClient.java:565`
  `private X509TrustManager x509TrustManagerOrNull;`
- `sources/okhttp3/OkHttpClient.java:744`
  `/* JADX INFO: renamed from: getX509TrustManagerOrNull$okhttp, reason: from getter */`
- `sources/okhttp3/OkHttpClient.java:745`
  `public final X509TrustManager getX509TrustManagerOrNull() {`
- `sources/okhttp3/OkHttpClient.java:746`
  `return this.x509TrustManagerOrNull;`
- `sources/okhttp3/OkHttpClient.java:749`
  `public final void setX509TrustManagerOrNull$okhttp(X509TrustManager x509TrustManager) {`
- `sources/okhttp3/OkHttpClient.java:750`
  `this.x509TrustManagerOrNull = x509TrustManager;`
- `sources/okhttp3/OkHttpClient.java:884`
  `this.x509TrustManagerOrNull = okHttpClient.getX509TrustManager();`
- `sources/okhttp3/OkHttpClient.java:1046`
  `@Deprecated(level = DeprecationLevel.ERROR, message = "Use the sslSocketFactory overload that accepts a X509TrustManager.")`
- `sources/okhttp3/OkHttpClient.java:1053`
  `X509TrustManager x509TrustManagerTrustManager = Platform.INSTANCE.get().trustManager(sslSocketFactory);`
- `sources/okhttp3/OkHttpClient.java:1054`
  `if (x509TrustManagerTrustManager == null) {`
- `sources/okhttp3/OkHttpClient.java:1057`
  `this.x509TrustManagerOrNull = x509TrustManagerTrustManager;`
- `sources/okhttp3/OkHttpClient.java:1059`
  `X509TrustManager x509TrustManager = this.x509TrustManagerOrNull;`
- `sources/okhttp3/OkHttpClient.java:1060`
  `Intrinsics.checkNotNull(x509TrustManager);`
- `sources/okhttp3/OkHttpClient.java:1061`
  `this.certificateChainCleaner = platform.buildCertificateChainCleaner(x509TrustManager);`
- `sources/okhttp3/OkHttpClient.java:1065`
  `public final Builder sslSocketFactory(SSLSocketFactory sslSocketFactory, X509TrustManager trustManager) {`
- `sources/okhttp3/OkHttpClient.java:1068`
  `if ((!Intrinsics.areEqual(sslSocketFactory, this.sslSocketFactoryOrNull)) || (!Intrinsics.areEqual(trustManager, this.x509TrustManagerOrNull))) {`
- `sources/okhttp3/OkHttpClient.java:1073`
  `this.x509TrustManagerOrNull = trustManager;`
- `sources/okhttp3/internal/platform/Android10Platform.java:10`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/platform/Android10Platform.java:27`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000J\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\...`
- `sources/okhttp3/internal/platform/Android10Platform.java:47`
  `public X509TrustManager trustManager(SSLSocketFactory sslSocketFactory) {`
- `sources/okhttp3/internal/platform/Android10Platform.java:120`
  `public CertificateChainCleaner buildCertificateChainCleaner(X509TrustManager trustManager) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:18`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:37`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000x\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\...`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:73`
  `public X509TrustManager trustManager(SSLSocketFactory sslSocketFactory) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:169`
  `public CertificateChainCleaner buildCertificateChainCleaner(X509TrustManager trustManager) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:176`
  `public TrustRootIndex buildTrustRootIndex(X509TrustManager trustManager) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:189`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u00008\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u000e\n\u0000\b\u...`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:192`
  `private final X509TrustManager trustManager;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:195`
  `private final X509TrustManager getTrustManager() {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:204`
  `public static /* synthetic */ CustomTrustRootIndex copy$default(CustomTrustRootIndex customTrustRootIndex, X509TrustManager x509TrustManager, Method method, int i, Object obj) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:206`
  `x509TrustManager = customTrustRootIndex.trustManager;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:211`
  `return customTrustRootIndex.copy(x509TrustManager, method);`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:214`
  `public final CustomTrustRootIndex copy(X509TrustManager trustManager, Method findByIssuerAndSignatureMethod) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:232`
  `X509TrustManager x509TrustManager = this.trustManager;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:233`
  `int iHashCode = (x509TrustManager != null ? x509TrustManager.hashCode() : 0) * 31;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:242`
  `public CustomTrustRootIndex(X509TrustManager trustManager, Method findByIssuerAndSignatureMethod) {`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:15`
  `import javax.net.ssl.X509TrustManager;`

## BR010

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/com/google/api/client/googleapis/auth/oauth2/GoogleIdTokenVerifier.java:64`
  `if (!super.verify((IdToken) googleIdToken)) {`
- `sources/com/google/api/client/googleapis/auth/oauth2/GoogleIdTokenVerifier.java:76`
  `public GoogleIdToken verify(String str) throws GeneralSecurityException, IOException {`
- `sources/com/google/api/client/http/apache/ApacheHttpTransport.java:164`
  `sSLSocketFactoryExtension.setHostnameVerifier(SSLSocketFactory.ALLOW_ALL_HOSTNAME_VERIFIER);`
- `sources/com/google/api/client/util/SslUtils.java:75`
  `public static HostnameVerifier trustAllHostnameVerifier() {`
- `sources/com/google/api/client/util/SslUtils.java:76`
  `return new HostnameVerifier() { // from class: com.google.api.client.util.SslUtils.2`
- `sources/com/google/api/client/util/SslUtils.java:77`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/com/google/api/client/util/SslUtils.java:78`
  `public boolean verify(String str, SSLSession sSLSession) {`
- `sources/okhttp3/internal/connection/RealConnection.java:444`
  `OkHostnameVerifier okHostnameVerifier = OkHostnameVerifier.INSTANCE;`
- `sources/okhttp3/internal/connection/RealConnection.java:448`
  `if (okHostnameVerifier.verify(strHost, (X509Certificate) certificate)) {`
- `sources/okhttp3/internal/connection/RealConnection.java:632`
  `if (this.http2Connection == null || routes == null || !routeMatchesAny(routes) || address.hostnameVerifier() != OkHostnameVerifier.INSTANCE || !supportsUrl(address.url())) {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:83`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\u0011\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\bÀ\u0002\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\...`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:84`
  `public static final class DisabledHostnameVerifier implements ConscryptHostnameVerifier {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:85`
  `public static final DisabledHostnameVerifier INSTANCE = new DisabledHostnameVerifier();`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:87`
  `public final boolean verify(String hostname, SSLSession session) {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:91`
  `public boolean verify(X509Certificate[] certs, String hostname, SSLSession session) {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:95`
  `private DisabledHostnameVerifier() {`
- `sources/okhttp3/internal/tls/BasicCertificateChainCleaner.java:81`
  `toVerify.verify(signingCert.getPublicKey());`
- `sources/org/apache/http/conn/ssl/AbstractVerifier.java:44`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/org/apache/http/conn/ssl/AbstractVerifier.java:45`
  `public final boolean verify(String str, SSLSession sSLSession) {`
- `sources/org/apache/http/conn/ssl/AbstractVerifier.java:47`
  `verify(str, (X509Certificate) sSLSession.getPeerCertificates()[0]);`
- `sources/org/apache/http/conn/ssl/AllowAllHostnameVerifier.java:5`
  `public class AllowAllHostnameVerifier extends AbstractVerifier {`
- `sources/org/apache/http/conn/ssl/AllowAllHostnameVerifier.java:6`
  `public static final AllowAllHostnameVerifier INSTANCE = new AllowAllHostnameVerifier();`
- `sources/org/apache/http/conn/ssl/AllowAllHostnameVerifier.java:12`
  `@Override // org.apache.http.conn.ssl.X509HostnameVerifier`
- `sources/org/apache/http/conn/ssl/AllowAllHostnameVerifier.java:13`
  `public final void verify(String str, String[] strArr, String[] strArr2) {`
- `sources/org/apache/http/conn/ssl/DefaultHostnameVerifier.java:54`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/org/apache/http/conn/ssl/DefaultHostnameVerifier.java:55`
  `public boolean verify(String str, SSLSession sSLSession) {`
- `sources/org/apache/http/conn/ssl/DefaultHostnameVerifier.java:57`
  `verify(str, (X509Certificate) sSLSession.getPeerCertificates()[0]);`
- `sources/org/apache/http/conn/ssl/NoopHostnameVerifier.java:14`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/org/apache/http/conn/ssl/NoopHostnameVerifier.java:15`
  `public boolean verify(String str, SSLSession sSLSession) {`
- `sources/org/apache/http/conn/ssl/SSLConnectionSocketFactory.java:43`
  `public static final X509HostnameVerifier ALLOW_ALL_HOSTNAME_VERIFIER = AllowAllHostnameVerifier.INSTANCE;`
- `sources/org/apache/http/conn/ssl/SSLConnectionSocketFactory.java:46`
  `public static final X509HostnameVerifier BROWSER_COMPATIBLE_HOSTNAME_VERIFIER = BrowserCompatHostnameVerifier.INSTANCE;`
- `sources/org/apache/http/conn/ssl/SSLConnectionSocketFactory.java:49`
  `public static final X509HostnameVerifier STRICT_HOSTNAME_VERIFIER = StrictHostnameVerifier.INSTANCE;`
- `sources/org/apache/http/conn/ssl/SSLSocketFactory.java:38`
  `private volatile X509HostnameVerifier hostnameVerifier;`
- `sources/org/apache/http/conn/ssl/SSLSocketFactory.java:43`
  `public static final X509HostnameVerifier ALLOW_ALL_HOSTNAME_VERIFIER = new AllowAllHostnameVerifier();`
- `sources/org/apache/http/conn/ssl/SSLSocketFactory.java:44`
  `public static final X509HostnameVerifier BROWSER_COMPATIBLE_HOSTNAME_VERIFIER = new BrowserCompatHostnameVerifier();`
- `sources/org/apache/http/conn/ssl/SSLSocketFactory.java:45`
  `public static final X509HostnameVerifier STRICT_HOSTNAME_VERIFIER = new StrictHostnameVerifier();`

## BR011

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/okhttp3/internal/connection/ConnectionSpecSelector.java:10`
  `import javax.net.ssl.SSLException;`
- `sources/okhttp3/internal/connection/ConnectionSpecSelector.java:11`
  `import javax.net.ssl.SSLHandshakeException;`
- `sources/okhttp3/internal/connection/ConnectionSpecSelector.java:73`
  `return (!this.isFallbackPossible || (e instanceof ProtocolException) || (e instanceof InterruptedIOException) || ((e instanceof SSLHandshakeException) && (e.getCause() instanceof CertificateException)) || (e instanceof SSLPeerUnverifiedException) || !(e instanceof SSLException)) ? false : true;`
- `sources/org/apache/http/impl/client/DefaultHttpRequestRetryHandler.java:12`
  `import javax.net.ssl.SSLException;`
- `sources/org/apache/http/impl/client/DefaultHttpRequestRetryHandler.java:39`
  `this(i, z, Arrays.asList(InterruptedIOException.class, UnknownHostException.class, ConnectException.class, SSLException.class));`

## BR012

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/okhttp3/Address.java:23`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000h\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002...`
- `sources/okhttp3/Address.java:25`
  `private final CertificatePinner certificatePinner;`
- `sources/okhttp3/Address.java:37`
  `public Address(String uriHost, int i, Dns dns, SocketFactory socketFactory, SSLSocketFactory sSLSocketFactory, HostnameVerifier hostnameVerifier, CertificatePinner certificatePinner, Authenticator proxyAuthenticator, Proxy proxy, List<? extends Protocol> protocols, List<ConnectionSpec> connectionSpe...`
- `sources/okhttp3/Address.java:49`
  `this.certificatePinner = certificatePinner;`
- `sources/okhttp3/Address.java:74`
  `public final CertificatePinner certificatePinner() {`
- `sources/okhttp3/Address.java:75`
  `return this.certificatePinner;`
- `sources/okhttp3/Address.java:162`
  `@Deprecated(level = DeprecationLevel.ERROR, message = "moved to val", replaceWith = @ReplaceWith(expression = "certificatePinner", imports = {}))`
- `sources/okhttp3/Address.java:163`
  `/* JADX INFO: renamed from: -deprecated_certificatePinner, reason: not valid java name and from getter */`
- `sources/okhttp3/Address.java:164`
  `public final CertificatePinner getCertificatePinner() {`
- `sources/okhttp3/Address.java:165`
  `return this.certificatePinner;`
- `sources/okhttp3/Address.java:179`
  `return ((((((((((((((((((527 + this.url.hashCode()) * 31) + this.dns.hashCode()) * 31) + this.proxyAuthenticator.hashCode()) * 31) + this.protocols.hashCode()) * 31) + this.connectionSpecs.hashCode()) * 31) + this.proxySelector.hashCode()) * 31) + Objects.hashCode(this.proxy)) * 31) + Objects.hashCo...`
- `sources/okhttp3/Address.java:184`
  `return Intrinsics.areEqual(this.dns, that.dns) && Intrinsics.areEqual(this.proxyAuthenticator, that.proxyAuthenticator) && Intrinsics.areEqual(this.protocols, that.protocols) && Intrinsics.areEqual(this.connectionSpecs, that.connectionSpecs) && Intrinsics.areEqual(this.proxySelector, that.proxySelec...`
- `sources/okhttp3/CertificatePinner.java:27`
  `/* JADX INFO: compiled from: CertificatePinner.kt */`
- `sources/okhttp3/CertificatePinner.java:29`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000T\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\"\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0010\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0...`
- `sources/okhttp3/CertificatePinner.java:30`
  `public final class CertificatePinner {`
- `sources/okhttp3/CertificatePinner.java:34`
  `public static final CertificatePinner DEFAULT = new Builder().build();`
- `sources/okhttp3/CertificatePinner.java:53`
  `public CertificatePinner(Set<Pin> pins, CertificateChainCleaner certificateChainCleaner) {`
- `sources/okhttp3/CertificatePinner.java:64`
  `public /* synthetic */ CertificatePinner(Set set, CertificateChainCleaner certificateChainCleaner, int i, DefaultConstructorMarker defaultConstructorMarker) {`
- `sources/okhttp3/CertificatePinner.java:79`
  `check$okhttp(hostname, new Function0<List<? extends X509Certificate>>() { // from class: okhttp3.CertificatePinner.check.1`
- `sources/okhttp3/CertificatePinner.java:88`
  `CertificateChainCleaner certificateChainCleaner = CertificatePinner.this.getCertificateChainCleaner();`
- `sources/okhttp3/CertificatePinner.java:190`
  `public final CertificatePinner withCertificateChainCleaner$okhttp(CertificateChainCleaner certificateChainCleaner) {`
- `sources/okhttp3/CertificatePinner.java:192`
  `return Intrinsics.areEqual(this.certificateChainCleaner, certificateChainCleaner) ? this : new CertificatePinner(this.pins, certificateChainCleaner);`
- `sources/okhttp3/CertificatePinner.java:196`
  `if (other instanceof CertificatePinner) {`
- `sources/okhttp3/CertificatePinner.java:197`
  `CertificatePinner certificatePinner = (CertificatePinner) other;`
- `sources/okhttp3/CertificatePinner.java:198`
  `if (Intrinsics.areEqual(certificatePinner.pins, this.pins) && Intrinsics.areEqual(certificatePinner.certificateChainCleaner, this.certificateChainCleaner)) {`
- `sources/okhttp3/CertificatePinner.java:211`
  `/* JADX INFO: compiled from: CertificatePinner.kt */`
- `sources/okhttp3/CertificatePinner.java:212`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0007\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0004\u0018\u00002\u00020\u0001B\u0015\u0...`
- `sources/okhttp3/CertificatePinner.java:241`
  `if (StringsKt.startsWith$default(pin, "sha256/", false, 2, (Object) null)) {`
- `sources/okhttp3/CertificatePinner.java:253`
  `throw new IllegalArgumentException("pins must start with 'sha256/' or 'sha1/': " + pin);`
- `sources/okhttp3/CertificatePinner.java:297`
  `return Intrinsics.areEqual(this.hash, CertificatePinner.INSTANCE.sha256Hash(certificate));`
- `sources/okhttp3/CertificatePinner.java:300`
  `return Intrinsics.areEqual(this.hash, CertificatePinner.INSTANCE.sha1Hash(certificate));`
- `sources/okhttp3/CertificatePinner.java:325`
  `/* JADX INFO: compiled from: CertificatePinner.kt */`
- `sources/okhttp3/CertificatePinner.java:326`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010!\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010\u000e\n\u0002\u0010\u0011\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\u0018\u00002\u00020\u0001B\u0005¢\u0006\u0002\u0010\u0002J'\u0010\b\...`
- `sources/okhttp3/CertificatePinner.java:343`
  `public final CertificatePinner build() {`
- `sources/okhttp3/CertificatePinner.java:344`
  `return new CertificatePinner(CollectionsKt.toSet(this.pins), null, 2, 0 == true ? 1 : 0);`
- `sources/okhttp3/CertificatePinner.java:348`
  `/* JADX INFO: compiled from: CertificatePinner.kt */`
- `sources/okhttp3/CertificatePinner.java:349`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\b\u0086\u0003\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u...`
- `sources/okhttp3/CertificatePinner.java:386`
  `return "sha256/" + sha256Hash((X509Certificate) certificate).base64();`
- `sources/okhttp3/OkHttpClient.java:46`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000î\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u001a\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u00...`
- `sources/okhttp3/OkHttpClient.java:52`
  `private final CertificatePinner certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:141`
  `this.certificatePinner = CertificatePinner.DEFAULT;`
- `sources/okhttp3/OkHttpClient.java:150`
  `CertificatePinner certificatePinner = builder.getCertificatePinner();`
- `sources/okhttp3/OkHttpClient.java:152`
  `this.certificatePinner = certificatePinner.withCertificateChainCleaner$okhttp(certificateChainCleaner);`
- `sources/okhttp3/OkHttpClient.java:163`
  `CertificatePinner certificatePinner2 = builder.getCertificatePinner();`
- `sources/okhttp3/OkHttpClient.java:165`
  `this.certificatePinner = certificatePinner2.withCertificateChainCleaner$okhttp(certificateChainCleaner2);`
- `sources/okhttp3/OkHttpClient.java:263`
  `public final CertificatePinner certificatePinner() {`
- `sources/okhttp3/OkHttpClient.java:264`
  `return this.certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:342`
  `if (!Intrinsics.areEqual(this.certificatePinner, CertificatePinner.DEFAULT)) {`
- `sources/okhttp3/OkHttpClient.java:497`
  `@Deprecated(level = DeprecationLevel.ERROR, message = "moved to val", replaceWith = @ReplaceWith(expression = "certificatePinner", imports = {}))`
- `sources/okhttp3/OkHttpClient.java:498`
  `/* JADX INFO: renamed from: -deprecated_certificatePinner, reason: not valid java name and from getter */`
- `sources/okhttp3/OkHttpClient.java:499`
  `public final CertificatePinner getCertificatePinner() {`
- `sources/okhttp3/OkHttpClient.java:500`
  `return this.certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:534`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000ø\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b...`
- `sources/okhttp3/OkHttpClient.java:540`
  `private CertificatePinner certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:586`
  `this.certificatePinner = CertificatePinner.DEFAULT;`
- `sources/okhttp3/OkHttpClient.java:781`
  `/* JADX INFO: renamed from: getCertificatePinner$okhttp, reason: from getter */`
- `sources/okhttp3/OkHttpClient.java:782`
  `public final CertificatePinner getCertificatePinner() {`
- `sources/okhttp3/OkHttpClient.java:783`
  `return this.certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:786`
  `public final void setCertificatePinner$okhttp(CertificatePinner certificatePinner) {`
- `sources/okhttp3/OkHttpClient.java:787`
  `Intrinsics.checkNotNullParameter(certificatePinner, "<set-?>");`
- `sources/okhttp3/OkHttpClient.java:788`
  `this.certificatePinner = certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:888`
  `this.certificatePinner = okHttpClient.certificatePinner();`
- `sources/okhttp3/OkHttpClient.java:1123`
  `public final Builder certificatePinner(CertificatePinner certificatePinner) {`
- `sources/okhttp3/OkHttpClient.java:1124`
  `Intrinsics.checkNotNullParameter(certificatePinner, "certificatePinner");`
- `sources/okhttp3/OkHttpClient.java:1125`
  `if (!Intrinsics.areEqual(certificatePinner, this.certificatePinner)) {`
- `sources/okhttp3/OkHttpClient.java:1128`
  `this.certificatePinner = certificatePinner;`
- `sources/okhttp3/internal/connection/RealCall.java:30`
  `import okhttp3.CertificatePinner;`
- `sources/okhttp3/internal/connection/RealCall.java:422`
  `CertificatePinner certificatePinner;`
- `sources/okhttp3/internal/connection/RealCall.java:426`
  `certificatePinner = this.client.certificatePinner();`
- `sources/okhttp3/internal/connection/RealCall.java:430`
  `certificatePinner = null;`
- `sources/okhttp3/internal/connection/RealCall.java:432`
  `return new Address(url.host(), url.port(), this.client.dns(), this.client.socketFactory(), sslSocketFactory, hostnameVerifier, certificatePinner, this.client.proxyAuthenticator(), this.client.proxy(), this.client.protocols(), this.client.connectionSpecs(), this.client.proxySelector());`
- `sources/okhttp3/internal/connection/RealConnection.java:32`
  `import okhttp3.CertificatePinner;`
- `sources/okhttp3/internal/connection/RealConnection.java:314`
  `sb.append(CertificatePinner.INSTANCE.pin(x509Certificate));`
- `sources/okhttp3/internal/connection/RealConnection.java:326`
  `final CertificatePinner certificatePinner = address.certificatePinner();`
- `sources/okhttp3/internal/connection/RealConnection.java:327`
  `Intrinsics.checkNotNull(certificatePinner);`
- `sources/okhttp3/internal/connection/RealConnection.java:336`
  `CertificateChainCleaner certificateChainCleaner = certificatePinner.getCertificateChainCleaner();`
- `sources/okhttp3/internal/connection/RealConnection.java:341`
  `certificatePinner.check$okhttp(address.url().host(), new Function0<List<? extends X509Certificate>>() { // from class: okhttp3.internal.connection.RealConnection.connectTls.2`
- `sources/okhttp3/internal/connection/RealConnection.java:636`
  `CertificatePinner certificatePinner = address.certificatePinner();`
- `sources/okhttp3/internal/connection/RealConnection.java:637`
  `Intrinsics.checkNotNull(certificatePinner);`
- `sources/okhttp3/internal/connection/RealConnection.java:641`
  `certificatePinner.check(strHost, handshake.peerCertificates());`

## BR013

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:447`
  `// br : http://registro.br/dominio/categoria.html`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:1079`
  `// gg : http://www.channelisles.net/register-domains/`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:1165`
  `// gu : http://gadao.gov.gu/register.html`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:1359`
  `// io : http://www.nic.io/rules.html`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:1364`
  `// iq : http://www.cmc.iq/english/iq/iqregister1.htm`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:1812`
  `// je : http://www.channelisles.net/register-domains/`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:1819`
  `// jm : http://www.com.jm/register.html`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:1822`
  `// jo : http://www.dns.jo/Registration_policy.aspx`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:3694`
  `// http://www.dot.kn/domainRules.html`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:3881`
  `// http://www.anrt.ma/fr/admin/download/upload/file_fr782.pdf`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:3928`
  `// see also: http://dns.marnet.net.mk/postapka.php`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:3938`
  `// ml : http://www.gobin.info/domainname/ml-template.doc`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:3969`
  `// mp : http://www.dot.mp/`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:4667`
  `// ng : http://www.nira.org.ng/index.php/join-us/register-ng-domain/189-nira-slds`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:5468`
  `// np : http://www.mos.com.np/register.html`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:5471`
  `// nr : http://cenpac.net.nr/dns/index.html`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:5558`
  `// ph : http://www.domains.ph/FAQ2.asp`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:5808`
  `// pr : http://www.nic.pr/index.asp?f=1`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:6794`
  `// http://nic.ae/english/arabicdomain/rules.jsp`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:10680`
  `// Alces Software Ltd : http://alces-software.com`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:11591`
  `// Enonic : http://enonic.com/`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:12161`
  `// I-O DATA DEVICE, INC. : http://www.iodata.com/`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:12222`
  `// KnightPoint Systems, LLC : http://www.knightpoint.com/`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:12230`
  `// .KRD : http://nic.krd/data/krd/Registration%20Policy.pdf`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:12279`
  `// LiquidNet Ltd : http://www.liquidnetlimited.com/`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:13035`
  `// Studenten Net Twente : http://www.snt.utwente.nl/`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:13044`
  `// Sub 6 Limited: http://www.sub6.com`
- `resources/com.ble_health_plus.apk/res/color/design_box_stroke_color.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/com.ble_health_plus.apk/res/drawable/$avd_hide_password__0.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.ble_health_plus.apk/res/drawable/$avd_hide_password__1.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.ble_health_plus.apk/res/drawable/$avd_hide_password__2.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.ble_health_plus.apk/res/drawable/$avd_show_password__0.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.ble_health_plus.apk/res/drawable/$avd_show_password__1.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.ble_health_plus.apk/res/drawable/$avd_show_password__2.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_ic_ab_back_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_ic_arrow_drop_right_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_ic_clear_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_ic_go_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_ic_menu_copy_mtrl_am_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_ic_menu_cut_mtrl_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`

## BR014

paper_id: B022
paper_title: A Study of Android Application Security

- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1443`
  `panelFeatureState.qwertyMode = KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1;`
- `sources/androidx/appcompat/app/ToolbarActionBar.java:436`
  `menu.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);`
- `sources/androidx/appcompat/app/WindowDecorActionBar.java:1279`
  `menu.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);`
- `sources/androidx/core/content/ContextCompat.java:56`
  `import android.telephony.TelephonyManager;`
- `sources/androidx/core/content/ContextCompat.java:306`
  `map.put(TelephonyManager.class, "phone");`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:4`
  `import android.telephony.TelephonyManager;`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:9`
  `public class TelephonyManagerCompat {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:10`
  `private static Method sGetDeviceIdMethod;`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:13`
  `public static String getImei(TelephonyManager telephonyManager) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:16`
  `return Api26Impl.getImei(telephonyManager);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:18`
  `if (Build.VERSION.SDK_INT >= 22 && (subscriptionId = getSubscriptionId(telephonyManager)) != Integer.MAX_VALUE && subscriptionId != -1) {`
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
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:46`
  `Method declaredMethod = TelephonyManager.class.getDeclaredMethod("getSubId", new Class[0]);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:50`
  `Integer num = (Integer) sGetSubIdMethod.invoke(telephonyManager, new Object[0]);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:60`
  `private TelephonyManagerCompat() {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:67`
  `static int getSubscriptionId(TelephonyManager telephonyManager) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:68`
  `return telephonyManager.getSubscriptionId();`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:76`
  `static String getImei(TelephonyManager telephonyManager) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:77`
  `return telephonyManager.getImei();`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:85`
  `static String getDeviceId(TelephonyManager telephonyManager, int i) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:86`
  `return telephonyManager.getDeviceId(i);`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:8`
  `import android.telephony.TelephonyManager;`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:112`
  `private static TelephonyManager getTelephonyManager(Context context) {`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:113`
  `return (TelephonyManager) context.getSystemService("phone");`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:128`
  `return eventInternal.toBuilder().addMetadata(KEY_SDK_VERSION, Build.VERSION.SDK_INT).addMetadata(KEY_MODEL, Build.MODEL).addMetadata(KEY_HARDWARE, Build.HARDWARE).addMetadata(KEY_DEVICE, Build.DEVICE).addMetadata(KEY_PRODUCT, Build.PRODUCT).addMetadata(KEY_OS_BUILD, Build.ID).addMetadata(KEY_MANUFAC...`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:27`
  `public class AdvertisingIdClient {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:67`
  `private WeakReference<AdvertisingIdClient> zzm;`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:72`
  `public zza(AdvertisingIdClient advertisingIdClient, long j) {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:73`
  `this.zzm = new WeakReference<>(advertisingIdClient);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:79`
  `AdvertisingIdClient advertisingIdClient = this.zzm.get();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:80`
  `if (advertisingIdClient != null) {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:81`
  `advertisingIdClient.finish();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:99`
  `public AdvertisingIdClient(Context context) {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:103`
  `private AdvertisingIdClient(Context context, long j, boolean z, boolean z2) {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:116`
  `public static Info getAdvertisingIdInfo(Context context) throws GooglePlayServicesRepairableException, IllegalStateException, GooglePlayServicesNotAvailableException, IOException {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:121`
  `AdvertisingIdClient advertisingIdClient = new AdvertisingIdClient(context, -1L, z, zzbVar.getBoolean("gads:ad_id_use_persistent_service:enabled", false));`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:124`
  `advertisingIdClient.zza(false);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:125`
  `Info info = advertisingIdClient.getInfo();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:126`
  `advertisingIdClient.zza(info, z, f, SystemClock.elapsedRealtime() - jElapsedRealtime, string, null);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:134`
  `AdvertisingIdClient advertisingIdClient = new AdvertisingIdClient(context, -1L, zzbVar.getBoolean("gads:ad_id_app_context:enabled", false), zzbVar.getBoolean("com.google.android.gms.ads.identifier.service.PERSISTENT_START", false));`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:136`
  `advertisingIdClient.zza(false);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:137`
  `return advertisingIdClient.zzb();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:139`
  `advertisingIdClient.finish();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:230`
  `map.put("tag", "AdvertisingIdClient");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:248`
  `throw new IOException("AdvertisingIdClient is not connected.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:254`
  `throw new IOException("AdvertisingIdClient cannot reconnect.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:261`
  `Log.i("AdvertisingIdClient", "GMS remote exception ", e);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:265`
  `throw new IOException("AdvertisingIdClient cannot reconnect.", e2);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:289`
  `Log.i("AdvertisingIdClient", "AdvertisingIdClient unbindService failed.", th);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:309`
  `throw new IOException("AdvertisingIdClient is not connected.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:315`
  `throw new IOException("AdvertisingIdClient cannot reconnect.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:322`
  `Log.i("AdvertisingIdClient", "GMS remote exception ", e);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:326`
  `throw new IOException("AdvertisingIdClient cannot reconnect.", e2);`
- `sources/com/google/android/gms/ads/identifier/zza.java:14`
  `zza(AdvertisingIdClient advertisingIdClient, Map map) {`
- `sources/com/google/android/gms/fitness/data/zzo.java:7`
  `import android.telephony.TelephonyManager;`
- `sources/com/google/android/gms/fitness/data/zzo.java:56`
  `return ((TelephonyManager) Preconditions.checkNotNull((TelephonyManager) context.getSystemService("phone"))).getPhoneType() != 0;`
- `sources/com/google/android/gms/measurement/internal/zzfa.java:5`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/measurement/internal/zzfa.java:85`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(true);`
- `sources/com/google/android/gms/measurement/internal/zzfa.java:87`
  `AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(this.zzs.zzau());`
- `sources/com/google/android/gms/measurement/internal/zzfa.java:98`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(false);`
- `sources/com/google/android/gms/measurement/internal/zzjp.java:4`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/measurement/internal/zzjp.java:49`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(true);`
- `sources/com/google/android/gms/measurement/internal/zzjp.java:51`
  `AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(this.zzs.zzau());`
- `sources/com/google/android/gms/measurement/internal/zzjp.java:62`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(false);`

## BR015

paper_id: B022
paper_title: A Study of Android Application Security

- `sources/com/ble_health_plus/common/DateTimeHelper.java:86`
  `Date date = new SimpleDateFormat(format, Locale.getDefault()).parse(dateString);`
- `sources/com/ble_health_plus/common/DateTimeHelper.java:94`
  `Date date = new SimpleDateFormat(format, Locale.getDefault()).parse(dateString);`
- `sources/com/ble_health_plus/extensions/ExtensionsKt.java:215`
  `String str2 = new SimpleDateFormat(str, Locale.getDefault()).format(calendar.getTime());`
- `sources/com/ble_health_plus/extensions/ExtensionsKt.java:227`
  `Date date = new SimpleDateFormat(str2, Locale.getDefault()).parse(str);`
- `sources/com/ble_health_plus/extensions/ExtensionsKt.java:228`
  `SimpleDateFormat simpleDateFormat = new SimpleDateFormat(str3, Locale.getDefault());`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:128`
  `return eventInternal.toBuilder().addMetadata(KEY_SDK_VERSION, Build.VERSION.SDK_INT).addMetadata(KEY_MODEL, Build.MODEL).addMetadata(KEY_HARDWARE, Build.HARDWARE).addMetadata(KEY_DEVICE, Build.DEVICE).addMetadata(KEY_PRODUCT, Build.PRODUCT).addMetadata(KEY_OS_BUILD, Build.ID).addMetadata(KEY_MANUFAC...`
- `sources/com/google/android/gms/fitness/data/Device.java:35`
  `return new Device(Build.MANUFACTURER, Build.MODEL, zzo.zzb(context), iZza, 2);`
- `sources/com/google/android/gms/fitness/data/zzo.java:36`
  `if (TextUtils.isEmpty(Build.PRODUCT) || !Build.PRODUCT.startsWith("glass_")) {`
- `sources/com/google/android/material/color/DynamicColors.java:175`
  `DeviceSupportCondition deviceSupportCondition = DYNAMIC_COLOR_SUPPORTED_MANUFACTURERS.get(Build.MANUFACTURER.toLowerCase());`
- `sources/com/google/android/material/color/DynamicColors.java:177`
  `deviceSupportCondition = DYNAMIC_COLOR_SUPPORTED_BRANDS.get(Build.BRAND.toLowerCase());`
- `sources/com/google/android/material/datepicker/DaysOfWeekAdapter.java:58`
  `textView.setContentDescription(String.format(viewGroup.getContext().getString(R.string.mtrl_picker_day_of_week_column_header), this.calendar.getDisplayName(7, 2, Locale.getDefault())));`
- `sources/com/google/android/material/internal/ManufacturerUtils.java:16`
  `return Build.MANUFACTURER.toLowerCase(Locale.ENGLISH).equals(MEIZU);`
- `sources/com/google/android/material/internal/ManufacturerUtils.java:20`
  `return Build.MANUFACTURER.toLowerCase(Locale.ENGLISH).equals(LGE);`
- `sources/com/google/android/material/internal/ManufacturerUtils.java:24`
  `return Build.MANUFACTURER.toLowerCase(Locale.ENGLISH).equals(SAMSUNG);`
- `sources/com/google/firebase/FirebaseCommonRegistrar.java:37`
  `arrayList.add(LibraryVersionComponent.create(DEVICE_NAME, safeValue(Build.PRODUCT)));`
- `sources/com/google/firebase/FirebaseCommonRegistrar.java:38`
  `arrayList.add(LibraryVersionComponent.create(DEVICE_MODEL, safeValue(Build.DEVICE)));`
- `sources/com/google/firebase/FirebaseCommonRegistrar.java:39`
  `arrayList.add(LibraryVersionComponent.create(DEVICE_BRAND, safeValue(Build.BRAND)));`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsController.java:465`
  `return StaticSessionData.DeviceData.create(CommonUtils.getCpuArchitectureInt(), Build.MODEL, Runtime.getRuntime().availableProcessors(), CommonUtils.getTotalRamInBytes(), ((long) statFs.getBlockCount()) * ((long) statFs.getBlockSize()), CommonUtils.isEmulator(context), CommonUtils.getDeviceState(con...`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsReportDataCapture.java:87`
  `String str = Build.MANUFACTURER;`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsReportDataCapture.java:88`
  `return CrashlyticsReport.Session.Device.builder().setArch(deviceArchitecture).setModel(Build.MODEL).setCores(iAvailableProcessors).setRam(totalRamInBytes).setDiskSpace(blockCount).setSimulator(zIsEmulator).setState(deviceState).setManufacturer(str).setModelClass(Build.PRODUCT).build();`
- `sources/com/michalsvec/singlerowcalendar/utils/DateUtils.java:26`
  `String str = new SimpleDateFormat("EEEE", Locale.getDefault()).format(date);`
- `sources/com/michalsvec/singlerowcalendar/utils/DateUtils.java:33`
  `String str = new SimpleDateFormat("EE", Locale.getDefault()).format(date);`
- `sources/com/michalsvec/singlerowcalendar/utils/DateUtils.java:40`
  `String str = new SimpleDateFormat("EEEEE", Locale.getDefault()).format(date);`
- `sources/com/michalsvec/singlerowcalendar/utils/DateUtils.java:47`
  `String str = new SimpleDateFormat("MM", Locale.getDefault()).format(date);`
- `sources/com/michalsvec/singlerowcalendar/utils/DateUtils.java:54`
  `String str = new SimpleDateFormat(Constant.DATE_FORMAT_MONTH_NAME, Locale.getDefault()).format(date);`
- `sources/com/michalsvec/singlerowcalendar/utils/DateUtils.java:61`
  `String str = new SimpleDateFormat("MMM", Locale.getDefault()).format(date);`
- `sources/com/michalsvec/singlerowcalendar/utils/DateUtils.java:68`
  `String str = new SimpleDateFormat(Constant.DATE_FORMAT_YYYY, Locale.getDefault()).format(date);`
- `sources/com/michalsvec/singlerowcalendar/utils/DateUtils.java:75`
  `String str = new SimpleDateFormat("dd", Locale.getDefault()).format(date);`
- `sources/kotlin/text/StringsKt__StringsJVMKt.java:168`
  `@Deprecated(message = "Use uppercase() instead.", replaceWith = @ReplaceWith(expression = "uppercase(Locale.getDefault())", imports = {"java.util.Locale"}))`
- `sources/kotlin/text/StringsKt__StringsJVMKt.java:184`
  `@Deprecated(message = "Use lowercase() instead.", replaceWith = @ReplaceWith(expression = "lowercase(Locale.getDefault())", imports = {"java.util.Locale"}))`
- `sources/kotlin/text/StringsKt__StringsJVMKt.java:736`
  `@Deprecated(message = "Use replaceFirstChar instead.", replaceWith = @ReplaceWith(expression = "replaceFirstChar { if (it.isLowerCase()) it.titlecase(Locale.getDefault()) else it.toString() }", imports = {"java.util.Locale"}))`
- `sources/kotlin/text/StringsKt__StringsJVMKt.java:740`
  `Locale locale = Locale.getDefault();`
- `sources/kotlin/text/StringsKt__StringsJVMKt.java:777`
  `@Deprecated(message = "Use replaceFirstChar instead.", replaceWith = @ReplaceWith(expression = "replaceFirstChar { it.lowercase(Locale.getDefault()) }", imports = {"java.util.Locale"}))`
- `sources/org/joda/time/chrono/ZonedChronology.java:56`
  `dateTimeZone = DateTimeZone.getDefault();`

## BR016

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/res/values/strings.xml:71`
  `<string name="google_api_key">AIzaSyASBaE5juvUPw7m247M095FhMezG7RTYao</string>`
- `resources/res/values/strings.xml:73`
  `<string name="google_crash_reporting_api_key">AIzaSyASBaE5juvUPw7m247M095FhMezG7RTYao</string>`
- `sources/com/ble_health_plus/R.java:5148`
  `public static final int google_api_key = 0x7f120044;`
- `sources/com/ble_health_plus/R.java:5150`
  `public static final int google_crash_reporting_api_key = 0x7f120046;`
- `sources/com/google/android/datatransport/cct/CCTDestination.java:14`
  `private static final String DEFAULT_API_KEY;`
- `sources/com/google/android/datatransport/cct/CCTDestination.java:23`
  `private final String apiKey;`
- `sources/com/google/android/datatransport/cct/CCTDestination.java:37`
  `DEFAULT_API_KEY = strMergeStrings3;`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:58`
  `static final String API_KEY_HEADER_KEY = "X-Goog-Api-Key";`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:210`
  `if (httpRequest.apiKey != null) {`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:211`
  `httpURLConnection.setRequestProperty(API_KEY_HEADER_KEY, httpRequest.apiKey);`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:361`
  `final String apiKey;`
- `sources/com/google/android/gms/auth/api/proxy/ProxyClient.java:9`
  `public interface ProxyClient extends HasApiKey<AuthProxyOptions> {`
- `sources/com/google/android/gms/auth/api/signin/GoogleSignInOptions.java:207`
  `return new GoogleSignInOptions(3, (ArrayList<Scope>) new ArrayList(hashSet), !TextUtils.isEmpty(strOptString) ? new Account(strOptString, "com.google") : null, jSONObject.getBoolean("idTokenRequested"), jSONObject.getBoolean("serverAuthRequested"), jSONObject.getBoolean("forceCodeForRefreshToken"), ...`
- `sources/com/google/android/gms/auth/api/signin/GoogleSignInOptions.java:388`
  `jSONObject.put("forceCodeForRefreshToken", this.zal);`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:57`
  `public static final Task<Map<ApiKey<?>, String>> zai(HasApiKey<?> hasApiKey, HasApiKey<?>... hasApiKeyArr) {`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:58`
  `Preconditions.checkNotNull(hasApiKey, "Requested API must not be null.");`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:59`
  `for (HasApiKey<?> hasApiKey2 : hasApiKeyArr) {`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:60`
  `Preconditions.checkNotNull(hasApiKey2, "Requested API must not be null.");`
- `sources/com/google/android/gms/common/api/internal/zaae.java:22`
  `public static void zad(Activity activity, GoogleApiManager googleApiManager, ApiKey<?> apiKey) {`
- `sources/com/google/android/gms/signin/internal/SignInClientImpl.java:50`
  `bundle.putBoolean("com.google.android.gms.signin.internal.forceCodeForRefreshToken", false);`
- `sources/com/google/android/gms/signin/internal/SignInClientImpl.java:53`
  `bundle.putBoolean("com.google.android.gms.signin.internal.waitForAccessTokenRefresh", false);`
- `sources/com/google/api/client/auth/oauth2/BearerToken.java:16`
  `static final String PARAM_NAME = "access_token";`
- `sources/com/google/api/client/auth/oauth2/BearerToken.java:30`
  `public String getAccessTokenFromRequest(HttpRequest httpRequest) {`
- `sources/com/google/api/client/auth/oauth2/Credential.java:28`
  `private String accessToken;`
- `sources/com/google/api/client/auth/oauth2/StoredCredential.java:16`
  `private String accessToken;`
- `sources/com/google/api/client/auth/oauth2/StoredCredential.java:88`
  `return Objects.toStringHelper(StoredCredential.class).add("accessToken", getAccessToken()).add("refreshToken", getRefreshToken()).add("expirationTimeMilliseconds", getExpirationTimeMilliseconds()).toString();`
- `sources/com/google/api/client/auth/openidconnect/IdToken.java:59`
  `private String accessTokenHash;`
- `sources/com/google/api/client/googleapis/auth/oauth2/CloudShellCredential.java:16`
  `private static final int ACCESS_TOKEN_INDEX = 2;`
- `sources/com/google/api/client/googleapis/auth/oauth2/GoogleCredential.java:140`
  `return super.executeRefreshToken();`
- `sources/com/google/api/client/googleapis/compute/ComputeCredential.java:33`
  `protected TokenResponse executeRefreshToken() throws IOException {`
- `sources/com/google/api/client/googleapis/testing/auth/oauth2/MockGoogleCredential.java:18`
  `private static final String TOKEN_RESPONSE = "{\"access_token\": \"%s\", \"expires_in\":  %s, \"refresh_token\": \"%s\", \"token_type\": \"%s\"}";`
- `sources/com/google/api/client/googleapis/testing/auth/oauth2/MockGoogleCredential.java:19`
  `public static final String ACCESS_TOKEN = "access_xyz";`
- `sources/com/google/api/client/googleapis/testing/auth/oauth2/MockGoogleCredential.java:21`
  `public static final String REFRESH_TOKEN = "refresh123";`
- `sources/com/google/api/client/googleapis/testing/auth/oauth2/MockGoogleCredential.java:23`
  `private static final String DEFAULT_TOKEN_RESPONSE_JSON = String.format(TOKEN_RESPONSE, ACCESS_TOKEN, EXPIRES_IN_SECONDS, REFRESH_TOKEN, TOKEN_TYPE);`
- `sources/com/google/api/client/googleapis/testing/auth/oauth2/MockTokenServerTransport.java:26`
  `Map<String, String> refreshTokens;`
- `sources/com/google/api/client/googleapis/testing/compute/MockMetadataServerTransport.java:21`
  `String accessToken;`
- `sources/com/google/firebase/FirebaseError.java:11`
  `public static final int ERROR_INVALID_API_KEY = 17023;`
- `sources/com/google/firebase/FirebaseOptions.java:12`
  `private static final String API_KEY_RESOURCE_NAME = "google_api_key";`
- `sources/com/google/firebase/FirebaseOptions.java:19`
  `private final String apiKey;`
- `sources/com/google/firebase/FirebaseOptions.java:28`
  `private String apiKey;`
- `sources/com/google/firebase/crashlytics/internal/send/DataTransportCrashlyticsReportSender.java:26`
  `private static final String CRASHLYTICS_API_KEY = mergeStrings("AzSBpY4F0rHiHFdinTvM", "IayrSTFL9eJ69YeSUO2");`
- `sources/com/google/firebase/crashlytics/internal/settings/SettingsJsonConstants.java:5`
  `static final String APP_KEY = "app";`
- `sources/com/google/firebase/installations/FirebaseInstallations.java:36`
  `private static final String API_KEY_VALIDATION_MSG = "Please set a valid API key. A Firebase API key is required to communicate with Firebase server APIs: It authenticates your project with Google.Please refer to https://firebase.google.com/support/privacy/init-options.";`
- `sources/com/google/firebase/installations/Utils.java:16`
  `private static final Pattern API_KEY_FORMAT = Pattern.compile("\\AA[\\w-]{38}\\z");`
- `sources/com/google/firebase/installations/local/PersistedInstallation.java:19`
  `private static final String REFRESH_TOKEN_KEY = "RefreshToken";`
- `sources/com/google/firebase/installations/remote/AutoValue_InstallationResponse.java:102`
  `private String refreshToken;`
- `sources/com/google/firebase/installations/remote/FirebaseInstallationServiceClient.java:38`
  `private static final String API_KEY_HEADER = "x-goog-api-key";`
- `sources/com/google/firebase/installations/remote/FirebaseInstallationServiceClient.java:298`
  `httpURLConnection.addRequestProperty(API_KEY_HEADER, str);`

## BR017

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `sources/com/ble_health_plus/common/AESCipher.java:82`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(keyBytes, "AES");`
- `sources/com/ble_health_plus/common/AESCipher.java:87`
  `IvParameterSpec ivParameterSpec = new IvParameterSpec(bytes);`
- `sources/com/ble_health_plus/common/AESCipher.java:88`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/ble_health_plus/common/AESCipher.java:89`
  `cipher.init(mode, secretKeySpec, ivParameterSpec);`
- `sources/com/ble_health_plus/common/AESCipher.java:107`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(bytes, "AES");`
- `sources/com/ble_health_plus/common/AESCipher.java:108`
  `Cipher cipher = Cipher.getInstance("AES");`
- `sources/com/ble_health_plus/common/AESCipher.java:109`
  `cipher.init(1, secretKeySpec);`
- `sources/com/ble_health_plus/common/AESCipher.java:142`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(bytes, "AES");`
- `sources/com/ble_health_plus/common/AESCipher.java:143`
  `Cipher cipher = Cipher.getInstance("AES");`
- `sources/com/ble_health_plus/common/AESCipher.java:144`
  `cipher.init(2, secretKeySpec);`
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
- `sources/com/bumptech/glide/load/engine/ResourceCacheKey.java:10`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/engine/cache/SafeKeyGenerator.java:47`
  `return Util.sha256BytesToHex(poolableDigestContainer.messageDigest.digest());`
- `sources/com/bumptech/glide/load/engine/cache/SafeKeyGenerator.java:54`
  `final MessageDigest messageDigest;`
- `sources/com/bumptech/glide/load/engine/cache/SafeKeyGenerator.java:57`
  `PoolableDigestContainer(MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/engine/cache/SafeKeyGenerator.java:58`
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
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:17`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:31`
  `public void update(byte[] bArr, Long l, MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:32`
  `messageDigest.update(bArr);`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:35`
  `messageDigest.update(this.buffer.putLong(l.longValue()).array());`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:43`
  `public void update(byte[] bArr, Integer num, MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:50`
  `messageDigest.update(this.buffer.putInt(num.intValue()).array());`
- `sources/com/bumptech/glide/signature/EmptySignature.java:4`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/signature/MediaStoreSignature.java:39`
  `public void updateDiskCacheKey(MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/signature/MediaStoreSignature.java:40`
  `messageDigest.update(ByteBuffer.allocate(12).putLong(this.dateModified).putInt(this.orientation).array());`
- `sources/com/bumptech/glide/signature/MediaStoreSignature.java:41`
  `messageDigest.update(this.mimeType.getBytes(CHARSET));`
- `sources/com/bumptech/glide/signature/ObjectKey.java:33`
  `public void updateDiskCacheKey(MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/signature/ObjectKey.java:34`
  `messageDigest.update(this.object.toString().getBytes(CHARSET));`
- `sources/com/google/android/gms/common/zzm.java:76`
  `Preconditions.checkNotNull(messageDigestZza);`
- `sources/com/google/android/gms/common/zzm.java:77`
  `return String.format("%s: pkg=%s, sha1=%s, atk=%s, ver=%s", str2, str, Hex.bytesToStringLowercase(messageDigestZza.digest(zziVar.zzf())), Boolean.valueOf(z), "12451000.false");`
- `sources/com/google/android/gms/measurement/internal/zzjp.java:79`
  `MessageDigest messageDigestZzE = zzkz.zzE();`
- `sources/com/google/android/gms/measurement/internal/zzjp.java:80`
  `if (messageDigestZzE == null) {`
- `sources/com/google/android/gms/measurement/internal/zzjp.java:83`
  `return String.format(Locale.US, "%032X", new BigInteger(1, messageDigestZzE.digest(str2.getBytes())));`
- `sources/com/google/android/gms/measurement/internal/zzkz.java:39`
  `import org.apache.commons.codec.digest.MessageDigestAlgorithms;`
- `sources/com/google/api/client/auth/oauth2/AuthorizationCodeFlow.java:230`
  `MessageDigest messageDigest = MessageDigest.getInstance(MessageDigestAlgorithms.SHA_256);`
- `sources/com/google/api/client/auth/oauth2/AuthorizationCodeFlow.java:231`
  `messageDigest.update(bytes, 0, bytes.length);`
- `sources/com/google/api/client/auth/oauth2/AuthorizationCodeFlow.java:232`
  `this.challenge = Base64.encodeBase64URLSafeString(messageDigest.digest());`
- `sources/com/google/common/hash/Hashing.java:13`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/google/common/hash/Hashing.java:14`
  `import org.apache.commons.codec.digest.MessageDigestAlgorithms;`
- `sources/com/google/common/hash/Hashing.java:80`
  `static final HashFunction MD5 = new MessageDigestHashFunction(MessageDigestAlgorithms.MD5, "Hashing.md5()");`
- `sources/com/google/common/hash/Hashing.java:92`
  `static final HashFunction SHA_1 = new MessageDigestHashFunction(MessageDigestAlgorithms.SHA_1, "Hashing.sha1()");`
- `sources/com/google/common/hash/Hashing.java:103`
  `static final HashFunction SHA_256 = new MessageDigestHashFunction(MessageDigestAlgorithms.SHA_256, "Hashing.sha256()");`
- `sources/com/google/common/hash/Hashing.java:114`
  `static final HashFunction SHA_384 = new MessageDigestHashFunction(MessageDigestAlgorithms.SHA_384, "Hashing.sha384()");`
- `sources/com/google/common/hash/Hashing.java:125`
  `static final HashFunction SHA_512 = new MessageDigestHashFunction(MessageDigestAlgorithms.SHA_512, "Hashing.sha512()");`
- `sources/com/google/common/hash/Hashing.java:131`
  `public static HashFunction hmacMd5(Key key) {`
- `sources/com/google/common/hash/MessageDigestHashFunction.java:72`
  `return new MessageDigestHasher(getMessageDigest(this.prototype.getAlgorithm()), this.bytes);`
- `sources/com/google/common/hash/MessageDigestHashFunction.java:96`
  `private static final class MessageDigestHasher extends AbstractByteHasher {`
- `sources/com/google/common/hash/MessageDigestHashFunction.java:98`
  `private final MessageDigest digest;`
- `sources/com/google/common/hash/MessageDigestHashFunction.java:101`
  `private MessageDigestHasher(MessageDigest messageDigest, int i) {`
- `sources/com/google/common/hash/MessageDigestHashFunction.java:102`
  `this.digest = messageDigest;`
- `sources/com/google/firebase/crashlytics/internal/common/CommonUtils.java:236`
  `MessageDigest messageDigest = MessageDigest.getInstance(str);`
- `sources/com/google/firebase/crashlytics/internal/common/CommonUtils.java:237`
  `messageDigest.update(bArr);`
- `sources/com/google/firebase/messaging/GmsRpc.java:22`
  `import org.apache.commons.codec.digest.MessageDigestAlgorithms;`
- `sources/com/google/firebase/messaging/GmsRpc.java:115`
  `return base64UrlSafe(MessageDigest.getInstance(MessageDigestAlgorithms.SHA_1).digest(this.app.getName().getBytes()));`
- `sources/com/google/thirdparty/publicsuffix/PublicSuffixPatterns.java:7`
  `public static final ImmutableMap<String, PublicSuffixType> EXACT = TrieParser.parseTrie("a&0&0trk9--nx?27qjf--nx?e9ebgn--nx?nbb0c7abgm--nx??1&2oa08--nx?apg6qpcbgm--nx?hbbgm--nx?rdceqa08--nx??2&8ugbgm--nx?eyh3la2ckx--nx?qbd9--nx??3&2wqq1--nx?60a0y8--nx??4x1d77xrck--nx?6&1f4a3abgm--nx?2yqyn--nx?3np8lv...`
- `sources/okio/ByteString.java:35`
  `import org.apache.commons.codec.digest.MessageDigestAlgorithms;`
- `sources/okio/ByteString.java:39`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000p\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000f\n\u0000\n\u0002\u0010\u0012\n\u0002\b\u0004\n\u0002\u0010\b\n\u0002\b\u0006\n\u0002\u0010\u000e\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010\u0000...`
- `sources/okio/HashingSink.java:21`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000B\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002...`
- `sources/okio/HashingSink.java:27`
  `private final MessageDigest messageDigest;`
- `sources/okio/HashingSink.java:30`
  `public static final HashingSink hmacSha1(Sink sink, ByteString byteString) {`
- `sources/okio/HashingSink.java:31`
  `return INSTANCE.hmacSha1(sink, byteString);`
- `sources/okio/HashingSink.java:35`
  `public static final HashingSink hmacSha256(Sink sink, ByteString byteString) {`
- `sources/okio/HashingSink.java:36`
  `return INSTANCE.hmacSha256(sink, byteString);`

## BR018

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/com/airbnb/lottie/model/DocumentData.java:9`
  `public float lineHeight;`
- `sources/com/airbnb/lottie/model/DocumentData.java:36`
  `this.lineHeight = f2;`
- `sources/com/airbnb/lottie/model/DocumentData.java:46`
  `long jFloatToRawIntBits = Float.floatToRawIntBits(this.lineHeight);`
- `sources/com/airbnb/lottie/model/layer/BaseLayer.java:64`
  `private final RectF tempMaskBoundsRect;`
- `sources/com/airbnb/lottie/model/layer/BaseLayer.java:111`
  `this.tempMaskBoundsRect = new RectF();`
- `sources/com/airbnb/lottie/model/layer/BaseLayer.java:259`
  `this.canvasBounds.set(0.0f, 0.0f, canvas.getWidth(), canvas.getHeight());`
- `sources/com/airbnb/lottie/model/layer/BaseLayer.java:270`
  `if (this.rect.width() >= 1.0f && this.rect.height() >= 1.0f) {`
- `sources/com/airbnb/lottie/model/layer/BaseLayer.java:337`
  `this.path.computeBounds(this.tempMaskBoundsRect, false);`
- `sources/com/airbnb/lottie/model/layer/BaseLayer.java:339`
  `this.maskBoundsRect.set(this.tempMaskBoundsRect);`
- `sources/com/airbnb/lottie/model/layer/BaseLayer.java:342`
  `rectF2.set(Math.min(rectF2.left, this.tempMaskBoundsRect.left), Math.min(this.maskBoundsRect.top, this.tempMaskBoundsRect.top), Math.max(this.maskBoundsRect.right, this.tempMaskBoundsRect.right), Math.max(this.maskBoundsRect.bottom, this.tempMaskBoundsRect.bottom));`
- `sources/com/airbnb/lottie/model/layer/CompositionLayer.java:118`
  `this.newClipRect.set(0.0f, 0.0f, this.layerModel.getPreCompWidth(), this.layerModel.getPreCompHeight());`
- `sources/com/airbnb/lottie/model/layer/ImageLayer.java:50`
  `this.src.set(0, 0, bitmap.getWidth(), bitmap.getHeight());`
- `sources/com/airbnb/lottie/model/layer/ImageLayer.java:52`
  `this.dst.set(0, 0, (int) (this.lottieImageAsset.getWidth() * fDpScale), (int) (this.lottieImageAsset.getHeight() * fDpScale));`
- `sources/com/airbnb/lottie/model/layer/ImageLayer.java:54`
  `this.dst.set(0, 0, (int) (bitmap.getWidth() * fDpScale), (int) (bitmap.getHeight() * fDpScale));`
- `sources/com/airbnb/lottie/model/layer/ImageLayer.java:65`
  `rectF.set(0.0f, 0.0f, this.lottieImageAsset.getWidth() * fDpScale, this.lottieImageAsset.getHeight() * fDpScale);`
- `sources/com/airbnb/lottie/model/layer/Layer.java:29`
  `private final int preCompHeight;`
- `sources/com/airbnb/lottie/model/layer/Layer.java:34`
  `private final int solidHeight;`
- `sources/com/airbnb/lottie/model/layer/Layer.java:73`
  `this.solidHeight = i2;`
- `sources/com/airbnb/lottie/model/layer/Layer.java:78`
  `this.preCompHeight = i5;`
- `sources/com/airbnb/lottie/model/layer/Layer.java:121`
  `int getPreCompHeight() {`
- `sources/com/airbnb/lottie/model/layer/Layer.java:122`
  `return this.preCompHeight;`
- `sources/com/airbnb/lottie/model/layer/Layer.java:153`
  `int getSolidHeight() {`
- `sources/com/airbnb/lottie/model/layer/Layer.java:154`
  `return this.solidHeight;`
- `sources/com/airbnb/lottie/model/layer/Layer.java:213`
  `if (getSolidWidth() != 0 && getSolidHeight() != 0) {`
- `sources/com/airbnb/lottie/model/layer/Layer.java:216`
  `sb.append(String.format(Locale.US, "%dx%d %X\n", Integer.valueOf(getSolidWidth()), Integer.valueOf(getSolidHeight()), Integer.valueOf(getSolidColor())));`
- `sources/com/airbnb/lottie/model/layer/SolidLayer.java:59`
  `this.points[5] = this.layerModel.getSolidHeight();`
- `sources/com/airbnb/lottie/model/layer/SolidLayer.java:62`
  `fArr3[7] = this.layerModel.getSolidHeight();`
- `sources/com/airbnb/lottie/model/layer/SolidLayer.java:88`
  `this.rect.set(0.0f, 0.0f, this.layerModel.getSolidWidth(), this.layerModel.getSolidHeight());`
- `sources/com/airbnb/lottie/model/layer/TextLayer.java:108`
  `rectF.set(0.0f, 0.0f, this.composition.getBounds().width(), this.composition.getBounds().height());`
- `sources/com/airbnb/lottie/model/layer/TextLayer.java:178`
  `float fDpScale = documentData.lineHeight * Utils.dpScale();`
- `sources/com/airbnb/lottie/parser/AnimatableTransformParser.java:39`
  `private static boolean isPositionIdentity(AnimatableValue<PointF, PointF> animatableValue) {`
- `sources/com/airbnb/lottie/parser/LayerParser.java:32`
  `return new Layer(Collections.emptyList(), lottieComposition, "__container", -1L, Layer.LayerType.PRE_COMP, -1L, null, Collections.emptyList(), new AnimatableTransform(), 0, 0, 0, 0.0f, 0.0f, bounds.width(), bounds.height(), null, null, Collections.emptyList(), Layer.MatteType.NONE, null, false, null...`
- `sources/com/airbnb/lottie/parser/moshi/LinkedHashTreeMap.java:207`
  `Node<K, V> nodeLast = node2.height > node3.height ? node2.last() : node3.first();`
- `sources/com/airbnb/lottie/parser/moshi/LinkedHashTreeMap.java:211`
  `i = node5.height;`
- `sources/com/airbnb/lottie/parser/moshi/LinkedHashTreeMap.java:220`
  `i2 = node6.height;`
- `sources/com/airbnb/lottie/parser/moshi/LinkedHashTreeMap.java:225`
  `nodeLast.height = Math.max(i, i2) + 1;`
- `sources/com/airbnb/lottie/parser/moshi/LinkedHashTreeMap.java:274`
  `int i = node2 != null ? node2.height : 0;`
- `sources/com/airbnb/lottie/parser/moshi/LinkedHashTreeMap.java:275`
  `int i2 = node3 != null ? node3.height : 0;`
- `sources/com/airbnb/lottie/parser/moshi/LinkedHashTreeMap.java:280`
  `int i4 = (node4 != null ? node4.height : 0) - (node5 != null ? node5.height : 0);`
- `sources/com/airbnb/lottie/parser/moshi/LinkedHashTreeMap.java:293`
  `int i5 = (node6 != null ? node6.height : 0) - (node7 != null ? node7.height : 0);`

## BR019

paper_id: B011
paper_title: Locking it down: The privacy and security of mobile medication apps

- `sources/androidx/appcompat/widget/ActivityChooserModel.java:387`
  `map.put(new ComponentName(activityResolveInfo.resolveInfo.activityInfo.packageName, activityResolveInfo.resolveInfo.activityInfo.name), activityResolveInfo);`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:943`
  `sparseArray.put(childAt.getId(), this.mFrameArrayList.get(childAt));`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:1506`
  `sparseArray.put(MotionLayout.this.getId(), base);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:645`
  `this.mTempMapIdToWidget.put(0, this.mLayoutWidget);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:646`
  `this.mTempMapIdToWidget.put(getId(), this.mLayoutWidget);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:649`
  `this.mTempMapIdToWidget.put(childAt4.getId(), getViewWidget(childAt4));`
- `sources/androidx/coordinatorlayout/widget/DirectedAcyclicGraph.java:34`
  `this.mGraph.put(t, emptyList);`
- `sources/androidx/core/graphics/TypefaceCompatApi24Impl.java:102`
  `simpleArrayMap.put(uri, byteBufferMmap);`
- `sources/androidx/core/location/LocationManagerCompat.java:130`
  `WeakReference<LocationListenerTransport> weakReferencePut = sLocationListeners.put(locationListenerTransport.getKey(), new WeakReference<>(locationListenerTransport));`
- `sources/androidx/core/location/LocationManagerCompat.java:836`
  `GnssLazyLoader.sGnssStatusListeners.put(callback, gnssStatusTransport);`
- `sources/androidx/core/location/LocationManagerCompat.java:931`
  `GnssLazyLoader.sGnssStatusListeners.put(callback, preRGnssStatusTransport);`
- `sources/androidx/transition/ChangeBounds.java:154`
  `transitionValues.values.put(PROPNAME_BOUNDS, new Rect(view.getLeft(), view.getTop(), view.getRight(), view.getBottom()));`
- `sources/androidx/transition/ChangeBounds.java:155`
  `transitionValues.values.put(PROPNAME_PARENT, transitionValues.view.getParent());`
- `sources/androidx/transition/ChangeBounds.java:158`
  `transitionValues.values.put(PROPNAME_WINDOW_X, Integer.valueOf(this.mTempLocation[0]));`
- `sources/androidx/transition/ChangeBounds.java:159`
  `transitionValues.values.put(PROPNAME_WINDOW_Y, Integer.valueOf(this.mTempLocation[1]));`
- `sources/androidx/transition/ChangeBounds.java:162`
  `transitionValues.values.put(PROPNAME_CLIP, ViewCompat.getClipBounds(view));`
- `sources/androidx/transition/ChangeClipBounds.java:39`
  `transitionValues.values.put(PROPNAME_CLIP, clipBounds);`
- `sources/androidx/transition/ChangeClipBounds.java:41`
  `transitionValues.values.put(PROPNAME_BOUNDS, new Rect(0, 0, view.getWidth(), view.getHeight()));`
- `sources/androidx/transition/Explode.java:37`
  `transitionValues.values.put(PROPNAME_SCREEN_BOUNDS, new Rect(i, i2, view.getWidth() + i, view.getHeight() + i2));`
- `sources/androidx/transition/VisibilityPropagation.java:26`
  `transitionValues.values.put(PROPNAME_VIEW_CENTER, iArr);`
- `sources/com/airbnb/lottie/manager/FontAssetManager.java:47`
  `this.fontMap.put(this.tempPair, typefaceTypefaceForStyle);`
- `sources/com/airbnb/lottie/network/NetworkFetcher.java:117`
  `lottieResultFromZipStream = fromJsonStream(str, inputStream, str3);`
- `sources/com/airbnb/lottie/network/NetworkFetcher.java:132`
  `private LottieResult<LottieComposition> fromJsonStream(String str, InputStream inputStream, String str2) throws IOException {`
- `sources/com/airbnb/lottie/network/NetworkFetcher.java:134`
  `return LottieCompositionFactory.fromJsonInputStreamSync(inputStream, null);`
- `sources/com/airbnb/lottie/network/NetworkFetcher.java:136`
  `return LottieCompositionFactory.fromJsonInputStreamSync(new FileInputStream(this.networkCache.writeTempCacheFile(str, inputStream, FileExtension.JSON).getAbsolutePath()), str);`
- `sources/com/ble_health_plus/DataBinderMapperImpl.java:192`
  `sparseIntArray.put(R.layout.activity_all_reading, 1);`
- `sources/com/ble_health_plus/DataBinderMapperImpl.java:193`
  `sparseIntArray.put(R.layout.activity_blood_pressure, 2);`
- `sources/com/ble_health_plus/DataBinderMapperImpl.java:194`
  `sparseIntArray.put(R.layout.activity_device_list, 3);`
- `sources/com/ble_health_plus/DataBinderMapperImpl.java:195`
  `sparseIntArray.put(R.layout.activity_gluco_meter, 4);`
- `sources/com/ble_health_plus/DataBinderMapperImpl.java:196`
  `sparseIntArray.put(R.layout.activity_heart_rate, 5);`
- `sources/com/ble_health_plus/DataBinderMapperImpl.java:197`
  `sparseIntArray.put(R.layout.activity_home, 6);`
- `sources/com/ble_health_plus/DataBinderMapperImpl.java:198`
  `sparseIntArray.put(R.layout.activity_profile, 7);`
- `sources/com/ble_health_plus/DataBinderMapperImpl.java:199`
  `sparseIntArray.put(R.layout.activity_reminder_add, 8);`
- `sources/com/ble_health_plus/DataBinderMapperImpl.java:200`
  `sparseIntArray.put(R.layout.activity_subscribe, 9);`
- `sources/com/ble_health_plus/DataBinderMapperImpl.java:201`
  `sparseIntArray.put(R.layout.activity_web_view, 10);`
- `sources/com/ble_health_plus/DataBinderMapperImpl.java:202`
  `sparseIntArray.put(R.layout.activity_weigh_scale, 11);`
- `sources/com/ble_health_plus/DataBinderMapperImpl.java:203`
  `sparseIntArray.put(R.layout.bottom_sheet_bloodpressure, 12);`
- `sources/com/ble_health_plus/DataBinderMapperImpl.java:204`
  `sparseIntArray.put(R.layout.bottom_sheet_gluecose, 13);`
- `sources/com/ble_health_plus/DataBinderMapperImpl.java:205`
  `sparseIntArray.put(R.layout.bottom_sheet_heartrate, 14);`
- `sources/com/ble_health_plus/DataBinderMapperImpl.java:206`
  `sparseIntArray.put(R.layout.bottom_sheet_weight, 15);`

## BR020

paper_id: B012
paper_title: Reviewing the data security and privacy policies of mobile apps for depression

- `sources/androidx/appcompat/widget/SearchView.java:95`
  `CursorAdapter mSuggestionsAdapter;`
- `sources/androidx/core/provider/FontProvider.java:73`
  `Cursor cursorQuery = null;`
- `sources/androidx/core/provider/FontProvider.java:78`
  `cursorQuery = Api16Impl.query(contentResolver, uriBuild, strArr, "query = ?", new String[]{fontRequest.getQuery()}, null, cancellationSignal);`
- `sources/androidx/core/provider/FontProvider.java:80`
  `cursorQuery = contentResolver.query(uriBuild, strArr, "query = ?", new String[]{fontRequest.getQuery()}, null);`
- `sources/androidx/core/provider/FontProvider.java:83`
  `int columnIndex = cursorQuery.getColumnIndex(FontsContractCompat.Columns.RESULT_CODE);`
- `sources/androidx/core/provider/FontProvider.java:85`
  `int columnIndex2 = cursorQuery.getColumnIndex("_id");`
- `sources/androidx/core/provider/FontProvider.java:86`
  `int columnIndex3 = cursorQuery.getColumnIndex(FontsContractCompat.Columns.FILE_ID);`
- `sources/androidx/core/provider/FontProvider.java:87`
  `int columnIndex4 = cursorQuery.getColumnIndex(FontsContractCompat.Columns.TTC_INDEX);`
- `sources/androidx/core/provider/FontProvider.java:88`
  `int columnIndex5 = cursorQuery.getColumnIndex(FontsContractCompat.Columns.WEIGHT);`
- `sources/androidx/core/provider/FontProvider.java:89`
  `int columnIndex6 = cursorQuery.getColumnIndex(FontsContractCompat.Columns.ITALIC);`
- `sources/androidx/core/provider/FontProvider.java:90`
  `while (cursorQuery.moveToNext()) {`
- `sources/androidx/core/provider/FontProvider.java:91`
  `int i3 = columnIndex != -1 ? cursorQuery.getInt(columnIndex) : 0;`
- `sources/androidx/core/provider/FontProvider.java:92`
  `int i4 = columnIndex4 != -1 ? cursorQuery.getInt(columnIndex4) : 0;`
- `sources/androidx/room/AutoClosingRoomOpenHelper.java:750`
  `@Override // android.database.Cursor`
- `sources/androidx/room/InvalidationTracker.java:31`
  `static final String RESET_UPDATED_TABLES_SQL = "UPDATE room_table_modification_log SET invalidated = 0 WHERE invalidated = 1 ";`
- `sources/androidx/room/InvalidationTracker.java:189`
  `supportSQLiteDatabase.execSQL("PRAGMA temp_store = MEMORY;");`
- `sources/androidx/room/InvalidationTracker.java:190`
  `supportSQLiteDatabase.execSQL("PRAGMA recursive_triggers='ON';");`
- `sources/androidx/room/InvalidationTracker.java:191`
  `supportSQLiteDatabase.execSQL(CREATE_TRACKING_TABLE_SQL);`
- `sources/androidx/room/InvalidationTracker.java:238`
  `supportSQLiteDatabase.execSQL("INSERT OR IGNORE INTO room_table_modification_log VALUES(" + i + ", 0)");`
- `sources/androidx/room/paging/LimitOffsetDataSource.java:91`
  `Cursor cursorQuery = null;`
- `sources/androidx/room/paging/LimitOffsetDataSource.java:98`
  `cursorQuery = this.mDb.query(sQLiteQuery);`
- `sources/androidx/room/paging/LimitOffsetDataSource.java:99`
  `List<T> listConvertRows = convertRows(cursorQuery);`
- `sources/androidx/room/paging/LimitOffsetDataSource.java:106`
  `if (cursorQuery != null) {`
- `sources/androidx/room/paging/LimitOffsetDataSource.java:107`
  `cursorQuery.close();`
- `sources/com/ble_health_plus/R.java:130`
  `public static final int OtpCursorColor = 0x7f040000;`
- `sources/com/ble_health_plus/R.java:131`
  `public static final int OtpCursorWidth = 0x7f040001;`
- `sources/com/ble_health_plus/R.java:2632`
  `public static final int material_cursor_inset_bottom = 0x7f0701d3;`
- `sources/com/ble_health_plus/R.java:2633`
  `public static final int material_cursor_inset_top = 0x7f0701d4;`
- `sources/com/ble_health_plus/R.java:5645`
  `public static final int strUpdate = 0x7f120235;`
- `sources/com/ble_health_plus/R.java:8442`
  `public static final int OtpView_OtpCursorColor = 0x00000003;`
- `sources/com/ble_health_plus/R.java:8443`
  `public static final int OtpView_OtpCursorWidth = 0x00000004;`
- `sources/com/ble_health_plus/R.java:9016`
  `public static final int[] OtpView = {android.R.attr.itemBackground, android.R.attr.cursorVisible, android.R.attr.textAllCaps, R.attr.OtpCursorColor, R.attr.OtpCursorWidth, R.attr.OtpHideLineWhenFilled, R.attr.OtpItemCount, R.attr.OtpItemHeight, R.attr.OtpItemRadius, R.attr.OtpItemSpacing, R.attr.Otp...`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:61`
  `_db.execSQL("CREATE TABLE IF NOT EXISTS 'DevicesTBL' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'user_id' TEXT, 'device_serial' TEXT, 'device_model' TEXT, 'device_manufacture' TEXT, 'device_name' TEXT, 'alias_name' TEXT, 'device_mac' TEXT, 'battery' INTEGER, 'device_Type' TEXT, 'sync' INTEGER...`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:62`
  `_db.execSQL("CREATE UNIQUE INDEX IF NOT EXISTS 'index_DevicesTBL_device_mac' ON 'DevicesTBL' ('device_mac')");`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:63`
  `_db.execSQL("CREATE TABLE IF NOT EXISTS 'GlucoseTbl' ('glucoseValue' INTEGER, 'eventType' TEXT, 'description' TEXT, 'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'data' TEXT, 'user_id' TEXT, 'device_mac' TEXT, 'epoch' INTEGER, 'date_time' TEXT, 'device_id' INTEGER, 'dataType' TEXT, 'sync' INTEGER...`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:64`
  `_db.execSQL("CREATE UNIQUE INDEX IF NOT EXISTS 'index_GlucoseTbl_data' ON 'GlucoseTbl' ('data')");`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:65`
  `_db.execSQL("CREATE TABLE IF NOT EXISTS 'HeartRateTBL' ('heartRateValue' INTEGER, 'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'data' TEXT, 'user_id' TEXT, 'device_mac' TEXT, 'epoch' INTEGER, 'date_time' TEXT, 'device_id' INTEGER, 'dataType' TEXT, 'sync' INTEGER, 'deviceType' TEXT)");`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:66`
  `_db.execSQL("CREATE TABLE IF NOT EXISTS 'BloodPressureTBL' ('systolicValue' INTEGER, 'diastolicValue' INTEGER, 'heartRateValue' INTEGER, 'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'data' TEXT, 'user_id' TEXT, 'device_mac' TEXT, 'epoch' INTEGER, 'date_time' TEXT, 'device_id' INTEGER, 'dataType'...`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:67`
  `_db.execSQL("CREATE UNIQUE INDEX IF NOT EXISTS 'index_BloodPressureTBL_epoch' ON 'BloodPressureTBL' ('epoch')");`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:68`
  `_db.execSQL("CREATE UNIQUE INDEX IF NOT EXISTS 'index_BloodPressureTBL_date_time' ON 'BloodPressureTBL' ('date_time')");`

## BR021

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `resources/com.ble_health_plus.apk/AndroidManifest.xml:51`
  `<provider`
- `resources/com.ble_health_plus.apk/AndroidManifest.xml:223`
  `<provider`
- `resources/com.ble_health_plus.apk/AndroidManifest.xml:250`
  `<provider`

## BR022

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `resources/com.ble_health_plus.apk/res/xml/file_provider_path.xml:3`
  `<cache-path`
- `resources/com.ble_health_plus.apk/res/xml/file_provider_path.xml:6`
  `<external-path`

## BR023

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `sources/androidx/startup/InitializationProvider.java:10`
  `public class InitializationProvider extends ContentProvider {`
- `sources/com/google/android/gms/measurement/AppMeasurementContentProvider.java:15`
  `public class AppMeasurementContentProvider extends ContentProvider {`
- `sources/com/google/firebase/provider/FirebaseInitProvider.java:14`
  `public class FirebaseInitProvider extends ContentProvider {`

## BR024

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `sources/androidx/core/content/FileProvider.java:69`
  `if (!providerInfo.grantUriPermissions) {`

## BR025

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

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
- `sources/androidx/room/InvalidationTracker.java:183`
  `void internalInit(SupportSQLiteDatabase supportSQLiteDatabase) {`
- `sources/androidx/room/InvalidationTracker.java:189`
  `supportSQLiteDatabase.execSQL("PRAGMA temp_store = MEMORY;");`
- `sources/androidx/room/InvalidationTracker.java:190`
  `supportSQLiteDatabase.execSQL("PRAGMA recursive_triggers='ON';");`
- `sources/androidx/room/InvalidationTracker.java:191`
  `supportSQLiteDatabase.execSQL(CREATE_TRACKING_TABLE_SQL);`
- `sources/androidx/room/InvalidationTracker.java:192`
  `syncTriggers(supportSQLiteDatabase);`
- `sources/androidx/room/InvalidationTracker.java:193`
  `this.mCleanupStatement = supportSQLiteDatabase.compileStatement(RESET_UPDATED_TABLES_SQL);`
- `sources/androidx/room/InvalidationTracker.java:237`
  `private void startTrackingTable(SupportSQLiteDatabase supportSQLiteDatabase, int i) {`
- `sources/androidx/room/InvalidationTracker.java:238`
  `supportSQLiteDatabase.execSQL("INSERT OR IGNORE INTO room_table_modification_log VALUES(" + i + ", 0)");`
- `sources/androidx/room/SQLiteCopyOpenHelper.java:171`
  `SupportSQLiteDatabase readableDatabase;`
- `sources/androidx/room/util/FtsTableInfo.java:29`
  `return new FtsTableInfo(str, readColumns(supportSQLiteDatabase, str), readOptions(supportSQLiteDatabase, str));`
- `sources/androidx/room/util/FtsTableInfo.java:32`
  `private static Set<String> readColumns(SupportSQLiteDatabase supportSQLiteDatabase, String str) {`
- `sources/androidx/room/util/FtsTableInfo.java:33`
  `Cursor cursorQuery = supportSQLiteDatabase.query("PRAGMA table_info('" + str + "')");`
- `sources/androidx/room/util/TableInfo.java:132`
  `private static Map<String, Column> readColumns(SupportSQLiteDatabase supportSQLiteDatabase, String str) {`
- `sources/androidx/room/util/TableInfo.java:133`
  `Cursor cursorQuery = supportSQLiteDatabase.query("PRAGMA table_info('" + str + "')");`
- `sources/androidx/room/util/TableInfo.java:153`
  `private static Set<Index> readIndices(SupportSQLiteDatabase supportSQLiteDatabase, String str) {`
- `sources/androidx/room/util/TableInfo.java:154`
  `Cursor cursorQuery = supportSQLiteDatabase.query("PRAGMA index_list('" + str + "')");`
- `sources/androidx/room/util/TableInfo.java:183`
  `private static Index readIndex(SupportSQLiteDatabase supportSQLiteDatabase, String str, boolean z) {`
- `sources/androidx/room/util/TableInfo.java:184`
  `Cursor cursorQuery = supportSQLiteDatabase.query("PRAGMA index_xinfo('" + str + "')");`
- `sources/com/ble_health_plus/database/AppDatabase.java:5`
  `import androidx.room.RoomDatabase;`
- `sources/com/ble_health_plus/database/AppDatabase.java:23`
  `@Metadata(d1 = {"\u0000D\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u...`
- `sources/com/ble_health_plus/database/AppDatabase.java:24`
  `public abstract class AppDatabase extends RoomDatabase {`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:12`
  `import androidx.sqlite.db.SupportSQLiteDatabase;`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:13`
  `import androidx.sqlite.db.SupportSQLiteOpenHelper;`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:52`
  `@Override // androidx.room.RoomDatabase`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:53`
  `protected SupportSQLiteOpenHelper createOpenHelper(DatabaseConfiguration configuration) {`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:54`
  `return configuration.sqliteOpenHelperFactory.create(SupportSQLiteOpenHelper.Configuration.builder(configuration.context).name(configuration.name).callback(new RoomOpenHelper(configuration, new RoomOpenHelper.Delegate(1) { // from class: com.ble_health_plus.database.AppDatabase_Impl.1`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:56`
  `public void onPostMigrate(SupportSQLiteDatabase _db) {`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:60`
  `public void createAllTables(SupportSQLiteDatabase _db) {`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:80`
  `public void dropAllTables(SupportSQLiteDatabase _db) {`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:93`
  `((RoomDatabase.Callback) AppDatabase_Impl.this.mCallbacks.get(i)).onDestructiveMigration(_db);`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:121`
  `public void onPreMigrate(SupportSQLiteDatabase _db) {`

## BR026

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/com/ble_health_plus/common/AppPref.java:4`
  `import android.content.SharedPreferences;`
- `sources/com/ble_health_plus/common/AppPref.java:31`
  `private static SharedPreferences.Editor sEditor;`
- `sources/com/ble_health_plus/common/AppPref.java:33`
  `private static SharedPreferences sPref;`
- `sources/com/ble_health_plus/common/AppPref.java:164`
  `SharedPreferences.Editor editor = sEditor;`
- `sources/com/ble_health_plus/common/AppPref.java:191`
  `@Metadata(d1 = {"\u0000.\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\t\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\b\u0086\u0003\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002...`
- `sources/com/google/api/client/auth/oauth2/AuthorizationCodeFlow.java:67`
  `this.credentialDataStore = builder.credentialDataStore;`
- `sources/com/google/api/client/auth/oauth2/AuthorizationCodeFlow.java:104`
  `DataStore<StoredCredential> dataStore = this.credentialDataStore;`
- `sources/com/google/api/client/auth/oauth2/AuthorizationCodeFlow.java:105`
  `if (dataStore != null) {`
- `sources/com/google/api/client/auth/oauth2/AuthorizationCodeFlow.java:106`
  `dataStore.set(str, new StoredCredential(fromTokenResponse));`
- `sources/com/google/api/client/auth/oauth2/AuthorizationCodeFlow.java:123`
  `DataStore<StoredCredential> dataStore = this.credentialDataStore;`
- `sources/com/google/api/client/auth/oauth2/AuthorizationCodeFlow.java:124`
  `if (dataStore != null) {`
- `sources/com/google/api/client/auth/oauth2/AuthorizationCodeFlow.java:125`
  `StoredCredential storedCredential = (StoredCredential) dataStore.get(str);`
- `sources/com/google/api/client/auth/oauth2/AuthorizationCodeFlow.java:140`
  `DataStore<StoredCredential> dataStore = this.credentialDataStore;`
- `sources/com/google/api/client/auth/oauth2/AuthorizationCodeFlow.java:141`
  `if (dataStore != null) {`
- `sources/com/google/api/client/auth/oauth2/AuthorizationCodeFlow.java:142`
  `clock.addRefreshListener(new DataStoreCredentialRefreshListener(str, dataStore));`
- `sources/com/google/api/client/auth/oauth2/DataStoreCredentialRefreshListener.java:5`
  `import com.google.api.client.util.store.DataStoreFactory;`
- `sources/com/google/api/client/auth/oauth2/DataStoreCredentialRefreshListener.java:9`
  `public final class DataStoreCredentialRefreshListener implements CredentialRefreshListener {`
- `sources/com/google/api/client/auth/oauth2/DataStoreCredentialRefreshListener.java:10`
  `private final DataStore<StoredCredential> credentialDataStore;`
- `sources/com/google/api/client/auth/oauth2/DataStoreCredentialRefreshListener.java:13`
  `public DataStoreCredentialRefreshListener(String str, DataStoreFactory dataStoreFactory) throws IOException {`
- `sources/com/google/api/client/auth/oauth2/DataStoreCredentialRefreshListener.java:14`
  `this(str, StoredCredential.getDefaultDataStore(dataStoreFactory));`
- `sources/com/google/api/client/auth/oauth2/DataStoreCredentialRefreshListener.java:17`
  `public DataStoreCredentialRefreshListener(String str, DataStore<StoredCredential> dataStore) {`
- `sources/com/google/api/client/auth/oauth2/DataStoreCredentialRefreshListener.java:19`
  `this.credentialDataStore = (DataStore) Preconditions.checkNotNull(dataStore);`
- `sources/com/google/api/client/auth/oauth2/DataStoreCredentialRefreshListener.java:32`
  `public DataStore<StoredCredential> getCredentialDataStore() {`
- `sources/com/google/api/client/auth/oauth2/DataStoreCredentialRefreshListener.java:33`
  `return this.credentialDataStore;`
- `sources/com/google/api/client/auth/oauth2/DataStoreCredentialRefreshListener.java:37`
  `this.credentialDataStore.set(this.userId, new StoredCredential(credential));`
- `sources/com/google/api/client/auth/oauth2/StoredCredential.java:106`
  `public static DataStore<StoredCredential> getDefaultDataStore(DataStoreFactory dataStoreFactory) throws IOException {`
- `sources/com/google/api/client/auth/oauth2/StoredCredential.java:107`
  `return dataStoreFactory.getDataStore(DEFAULT_DATA_STORE_ID);`
- `sources/com/google/api/client/googleapis/auth/oauth2/GoogleAuthorizationCodeFlow.java:17`
  `import com.google.api.client.util.store.DataStore;`
- `sources/com/google/api/client/googleapis/auth/oauth2/GoogleAuthorizationCodeFlow.java:18`
  `import com.google.api.client.util.store.DataStoreFactory;`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsController.java:318`
  `new MetaDataStore(CrashlyticsController.this.fileStore).writeUserData(currentSessionId, userMetadata);`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsController.java:331`
  `new MetaDataStore(CrashlyticsController.this.fileStore).writeKeyData(CrashlyticsController.this.getCurrentSessionId(), map, z);`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsController.java:531`
  `MetaDataStore metaDataStore = new MetaDataStore(fileStore);`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsController.java:532`
  `File userDataFileForSession = metaDataStore.getUserDataFileForSession(str);`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsController.java:533`
  `File keysFileForSession = metaDataStore.getKeysFileForSession(str);`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsController.java:553`
  `userMetadata.setCustomKeys(new MetaDataStore(this.fileStore).readKeyData(str));`
- `sources/com/google/firebase/crashlytics/internal/common/MetaDataStore.java:19`
  `class MetaDataStore {`
- `sources/com/google/firebase/crashlytics/internal/common/MetaDataStore.java:27`
  `public MetaDataStore(FileStore fileStore) {`
- `sources/com/google/firebase/crashlytics/internal/common/MetaDataStore.java:184`
  `/* JADX WARN: Type inference failed for: r0v0, types: [com.google.firebase.crashlytics.internal.common.MetaDataStore$1] */`
- `sources/com/google/firebase/crashlytics/internal/common/MetaDataStore.java:186`
  `return new JSONObject() { // from class: com.google.firebase.crashlytics.internal.common.MetaDataStore.1`
- `sources/com/google/firebase/crashlytics/internal/common/MetaDataStore.java:188`
  `put(MetaDataStore.KEY_USER_ID, this.val$userData.getUserId());`

## BR027

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/android/print/PdfPrint.java:53`
  `File file2 = new File(file, str);`
- `sources/androidx/core/content/ContextCompat.java:174`
  `return createFilesDir(new File(context.getApplicationInfo().dataDir, "no_backup"));`
- `sources/androidx/core/graphics/drawable/IconCompat.java:375`
  `return new FileInputStream(new File((String) this.mObj1));`
- `sources/androidx/core/os/EnvironmentCompat.java:22`
  `return file.getCanonicalPath().startsWith(Environment.getExternalStorageDirectory().getCanonicalPath()) ? Environment.getExternalStorageState() : "unknown";`
- `sources/androidx/core/util/AtomicFile.java:19`
  `this.mNewName = new File(file.getPath() + ".new");`
- `sources/androidx/core/util/AtomicFile.java:20`
  `this.mLegacyBackupName = new File(file.getPath() + ".bak");`
- `sources/androidx/documentfile/provider/RawDocumentFile.java:30`
  `File file = new File(this.mFile, str2);`
- `sources/androidx/sqlite/db/SupportSQLiteOpenHelper.java:91`
  `SupportSQLiteCompat.Api16Impl.deleteDatabase(new File(str));`
- `sources/androidx/sqlite/db/SupportSQLiteOpenHelper.java:94`
  `if (!new File(str).delete()) {`
- `sources/androidx/sqlite/db/framework/FrameworkSQLiteOpenHelper.java:41`
  `this.mDelegate = new OpenHelper(this.mContext, new File(SupportSQLiteCompat.Api21Impl.getNoBackupFilesDir(this.mContext), this.mName).getAbsolutePath(), frameworkSQLiteDatabaseArr, this.mCallback);`
- `sources/com/airbnb/lottie/network/NetworkCache.java:77`
  `File file = new File(parentDir(), filenameForUrl(str, fileExtension, true));`
- `sources/com/airbnb/lottie/network/NetworkCache.java:78`
  `File file2 = new File(file.getAbsolutePath().replace(".temp", ""));`
- `sources/com/airbnb/lottie/network/NetworkCache.java:88`
  `File file = new File(parentDir(), filenameForUrl(str, FileExtension.JSON, false));`
- `sources/com/ble_health_plus/common/AESCipher.java:101`
  `File externalCacheDir = myApp.getExternalCacheDir();`
- `sources/com/ble_health_plus/common/AESCipher.java:125`
  `File externalCacheDir2 = myApp2.getExternalCacheDir();`
- `sources/com/ble_health_plus/common/AESCipher.java:128`
  `return new File(sb2.toString());`
- `sources/com/ble_health_plus/common/AESCipher.java:137`
  `sb.append((myApp == null || (externalCacheDir = myApp.getExternalCacheDir()) == null) ? null : externalCacheDir.getAbsolutePath());`
- `sources/com/ble_health_plus/database/AppDatabase.java:84`
  `RoomDatabase roomDatabaseBuild = Room.databaseBuilder(context, AppDatabase.class, "ble_health_restore").createFromFile(new File(context.getExternalCacheDir(), "ble_health_restore")).build();`
- `sources/com/ble_health_plus/ui/custom/PdfView.java:86`
  `File file = new File(path);`
- `sources/com/ble_health_plus/ui/menu/BackUpFragment.java:470`
  `File fileEncrypt = AESCipher.INSTANCE.encrypt(new File(base.getDatabasePath(AppDatabase.DATABASE_NAME).getAbsolutePath()));`
- `sources/com/ble_health_plus/ui/menu/BackUpFragment.java:590`
  `File externalCacheDir = base.getExternalCacheDir();`
- `sources/com/ble_health_plus/ui/menu/BackUpFragment.java:593`
  `File file2 = new File(sb.toString());`
- `sources/com/ble_health_plus/ui/menu/BackUpFragment.java:721`
  `sb.append((myApp == null || (externalCacheDir = myApp.getExternalCacheDir()) == null) ? null : externalCacheDir.getAbsolutePath());`
- `sources/com/ble_health_plus/ui/menu/BackUpFragment.java:723`
  `if (new File(sb.toString()).exists()) {`
- `sources/com/ble_health_plus/ui/menu/BackUpFragment.java:1022`
  `sb.append((myApp == null || (externalCacheDir = myApp.getExternalCacheDir()) == null) ? null : externalCacheDir.getAbsolutePath());`
- `sources/com/ble_health_plus/ui/menu/BackUpFragment.java:1024`
  `File file = new File(sb.toString());`
- `sources/com/ble_health_plus/ui/menu/BackUpFragment.java:1029`
  `File file2 = new File(requireActivity().getDatabasePath("ble_health_restore").getAbsolutePath());`
- `sources/com/ble_health_plus/ui/profile/RegisterFragment.java:972`
  `UCrop uCropOf = UCrop.of(uri, Uri.fromFile(new File(requireActivity().getExternalCacheDir(), str)));`
- `sources/com/ble_health_plus/ui/profile/RegisterFragment.java:974`
  `AppLog.INSTANCE.e("Crop", "Crop " + new File(requireActivity().getExternalCacheDir(), str).getAbsolutePath());`
- `sources/com/ble_health_plus/ui/profile/UserProfileActivity.java:806`
  `UCrop uCropOf = UCrop.of(uri, Uri.fromFile(new File(getExternalCacheDir(), str)));`
- `sources/com/ble_health_plus/ui/profile/UserProfileActivity.java:808`
  `AppLog.INSTANCE.e("Crop", "Crop " + new File(getExternalCacheDir(), str).getAbsolutePath());`
- `sources/com/ble_health_plus/ui/report/ShareReportFragment.java:566`
  `final File externalCacheDir = requireActivity().getExternalCacheDir();`
- `sources/com/bumptech/glide/Glide.java:137`
  `File file = new File(cacheDir, str);`
- `sources/com/bumptech/glide/disklrucache/DiskLruCache.java:73`
  `this.journalFile = new File(file, JOURNAL_FILE);`
- `sources/com/bumptech/glide/disklrucache/DiskLruCache.java:74`
  `this.journalFileTmp = new File(file, JOURNAL_FILE_TEMP);`
- `sources/com/bumptech/glide/disklrucache/DiskLruCache.java:75`
  `this.journalFileBackup = new File(file, JOURNAL_FILE_BACKUP);`
- `sources/com/bumptech/glide/disklrucache/DiskLruCache.java:87`
  `File file2 = new File(file, JOURNAL_FILE_BACKUP);`
- `sources/com/bumptech/glide/disklrucache/DiskLruCache.java:89`
  `File file3 = new File(file, JOURNAL_FILE);`
- `sources/com/bumptech/glide/load/data/mediastore/ThumbFetcher.java:1`
  `package com.bumptech.glide.load.data.mediastore;`
- `sources/com/bumptech/glide/load/data/mediastore/ThumbFetcher.java:7`
  `import android.provider.MediaStore;`

## BR029

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/com.ble_health_plus.apk/AndroidManifest.xml:101`
  `android:exported="true"`
- `resources/com.ble_health_plus.apk/AndroidManifest.xml:124`
  `android:exported="true"`
- `resources/com.ble_health_plus.apk/AndroidManifest.xml:144`
  `android:exported="true"`

## BR030

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/com.ble_health_plus.apk/AndroidManifest.xml:82`
  `android:exported="true"/>`
- `resources/com.ble_health_plus.apk/AndroidManifest.xml:86`
  `android:exported="true"/>`
- `resources/com.ble_health_plus.apk/AndroidManifest.xml:90`
  `android:exported="true">`
- `resources/com.ble_health_plus.apk/AndroidManifest.xml:166`
  `android:exported="true"`

## BR031

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/com.ble_health_plus.apk/AndroidManifest.xml:63`
  `android:exported="true">`
- `resources/com.ble_health_plus.apk/AndroidManifest.xml:74`
  `android:exported="true">`
- `resources/com.ble_health_plus.apk/AndroidManifest.xml:206`
  `android:exported="true">`

## BR033

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/com/ble_health_plus/ui/menu/MoreFragment.java:431`
  `startActivity(new Intent("android.intent.action.VIEW", Uri.parse("https://www.blehealthplus.com/")));`
- `sources/com/ble_health_plus/ui/menu/MoreFragment.java:734`
  `startActivity(new Intent("android.intent.action.VIEW", Uri.parse("market://details?id=" + requireActivity().getPackageName())));`
- `sources/com/ble_health_plus/ui/menu/MoreFragment.java:739`
  `startActivity(new Intent("android.intent.action.VIEW", Uri.parse("http://play.google.com/store/apps/details?id=" + requireActivity().getPackageName())));`
- `sources/com/ble_health_plus/ui/profile/OTPVerifyFragment.java:196`
  `InputStream inputStreamOpenInputStream = requireActivity().getContentResolver().openInputStream(Uri.parse(signUpReq.getProfile()));`
- `sources/com/ble_health_plus/ui/profile/RegisterFragment.java:895`
  `InputStream inputStreamOpenInputStream = requireActivity().getContentResolver().openInputStream(Uri.parse(uri.toString()));`

## BR034

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:452`
  `LocalBroadcastManager.getInstance(context).sendBroadcast(intent);`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:460`
  `LocalBroadcastManager.getInstance(context).sendBroadcast(intent);`
- `sources/com/google/android/gms/measurement/internal/zzfe.java:40`
  `this.zza.doStartService(context, className);`

## BR035

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/com/ble_health_plus/ui/menu/WebViewActivity.java:80`
  `view.loadUrl(url);`
- `sources/com/ble_health_plus/ui/menu/WebViewActivity.java:108`
  `activityWebViewBinding.webView.loadUrl(this.URL);`
- `sources/com/ble_health_plus/ui/report/ShareReportFragment.java:494`
  `view.loadUrl(url);`
- `sources/com/ble_health_plus/ui/report/ShareReportFragment.java:536`
  `fragmentShareReprotBinding.webView.addJavascriptInterface(new WebAppInterface(this), "Android");`
- `sources/com/ble_health_plus/ui/report/ShareReportFragment.java:537`
  `fragmentShareReprotBinding.webView.loadUrl("file:///android_asset/report.html");`

## BR040

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `sources/com/ble_health_plus/ui/menu/FitDataFragment.java:55`
  `import com.google.android.gms.fitness.request.DataReadRequest;`
- `sources/com/ble_health_plus/ui/menu/FitDataFragment.java:91`
  `@Metadata(d1 = {"\u0000¾\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u00...`
- `sources/com/ble_health_plus/ui/menu/FitDataFragment.java:133`
  `@DebugMetadata(c = "com.ble_health_plus.ui.menu.FitDataFragment", f = "FitDataFragment.kt", i = {0, 0, 0, 0}, l = {246}, m = "getDataByType", n = {"this", "account", "type", "readRequest"}, s = {"L$0", "L$1", "L$2", "L$3"})`
- `sources/com/ble_health_plus/ui/menu/FitDataFragment.java:560`
  `com.google.android.gms.fitness.request.DataReadRequest r6 = (com.google.android.gms.fitness.request.DataReadRequest) r6`
- `sources/com/ble_health_plus/ui/menu/FitDataFragment.java:577`
  `com.google.android.gms.fitness.request.DataReadRequest r8 = r5.queryFitnessData(r7)`
- `sources/com/ble_health_plus/ui/menu/FitDataFragment.java:687`
  `private final DataReadRequest queryFitnessData(DeviceType type) {`
- `sources/com/ble_health_plus/ui/menu/FitDataFragment.java:701`
  `DataReadRequest.Builder builder = new DataReadRequest.Builder();`
- `sources/com/ble_health_plus/ui/menu/FitDataFragment.java:715`
  `DataReadRequest dataReadRequestBuild = builder.build();`
- `sources/com/ble_health_plus/ui/menu/FitDataFragment.java:716`
  `Intrinsics.checkNotNullExpressionValue(dataReadRequestBuild, "dataReadBuilder.build()");`
- `sources/com/ble_health_plus/ui/menu/FitDataFragment.java:717`
  `return dataReadRequestBuild;`
- `sources/com/bumptech/glide/ListPreloader.java:29`
  `RequestBuilder<?> getPreloadRequestBuilder(U u);`
- `sources/com/bumptech/glide/ListPreloader.java:108`
  `RequestBuilder<?> preloadRequestBuilder;`
- `sources/com/bumptech/glide/ListPreloader.java:109`
  `if (t == null || (preloadSize = this.preloadDimensionProvider.getPreloadSize(t, i, i2)) == null || (preloadRequestBuilder = this.preloadModelProvider.getPreloadRequestBuilder(t)) == null) {`
- `sources/com/bumptech/glide/ListPreloader.java:112`
  `preloadRequestBuilder.into(this.preloadTargetQueue.next(preloadSize[0], preloadSize[1]));`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:1`
  `package com.google.android.gms.ads.identifier;`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:134`
  `AdvertisingIdClient advertisingIdClient = new AdvertisingIdClient(context, -1L, zzbVar.getBoolean("gads:ad_id_app_context:enabled", false), zzbVar.getBoolean("com.google.android.gms.ads.identifier.service.PERSISTENT_START", false));`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:153`
  `String str = z ? "com.google.android.gms.ads.identifier.service.PERSISTENT_START" : "com.google.android.gms.ads.identifier.service.START";`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:232`
  `new com.google.android.gms.ads.identifier.zza(this, map).start();`
- `sources/com/google/android/gms/ads/identifier/zza.java:1`
  `package com.google.android.gms.ads.identifier;`
- `sources/com/google/android/gms/ads/identifier/zzb.java:1`
  `package com.google.android.gms.ads.identifier;`
- `sources/com/google/android/gms/ads/identifier/zzc.java:1`
  `package com.google.android.gms.ads.identifier;`
- `sources/com/google/android/gms/ads_identifier/R.java:1`
  `package com.google.android.gms.ads_identifier;`
- `sources/com/google/android/gms/fitness/GoalsApi.java:5`
  `import com.google.android.gms.fitness.request.GoalsReadRequest;`
- `sources/com/google/android/gms/fitness/GoalsApi.java:12`
  `PendingResult<GoalsResult> readCurrentGoals(GoogleApiClient googleApiClient, GoalsReadRequest goalsReadRequest);`
- `sources/com/google/android/gms/fitness/GoalsClient.java:10`
  `import com.google.android.gms.fitness.request.GoalsReadRequest;`
- `sources/com/google/android/gms/fitness/GoalsClient.java:27`
  `public Task<List<Goal>> readCurrentGoals(GoalsReadRequest goalsReadRequest) {`
- `sources/com/google/android/gms/fitness/GoalsClient.java:28`
  `return PendingResultUtil.toTask(zza.readCurrentGoals(asGoogleApiClient(), goalsReadRequest), new PendingResultUtil.ResultConverter() { // from class: com.google.android.gms.fitness.zzj`
- `sources/com/google/android/gms/fitness/HistoryApi.java:17`
  `import com.google.android.gms.fitness.request.DataReadRequest;`
- `sources/com/google/android/gms/fitness/HistoryApi.java:86`
  `PendingResult<DataReadResult> readData(GoogleApiClient googleApiClient, DataReadRequest dataReadRequest);`
- `sources/com/google/android/gms/fitness/HistoryClient.java:14`
  `import com.google.android.gms.fitness.request.DataReadRequest;`
- `sources/com/google/android/gms/fitness/HistoryClient.java:62`
  `public Task<DataReadResponse> readData(DataReadRequest dataReadRequest) {`
- `sources/com/google/android/gms/fitness/HistoryClient.java:63`
  `return PendingResultUtil.toResponseTask(zzb.readData(asGoogleApiClient(), dataReadRequest), new DataReadResponse());`
- `sources/com/google/android/gms/fitness/SessionsApi.java:15`
  `import com.google.android.gms.fitness.request.SessionReadRequest;`
- `sources/com/google/android/gms/fitness/SessionsApi.java:67`
  `PendingResult<SessionReadResult> readSession(GoogleApiClient googleApiClient, SessionReadRequest sessionReadRequest);`
- `sources/com/google/android/gms/fitness/SessionsClient.java:12`
  `import com.google.android.gms.fitness.request.SessionReadRequest;`
- `sources/com/google/android/gms/fitness/SessionsClient.java:34`
  `public Task<SessionReadResponse> readSession(SessionReadRequest sessionReadRequest) {`
- `sources/com/google/android/gms/fitness/SessionsClient.java:35`
  `return PendingResultUtil.toResponseTask(zza.readSession(asGoogleApiClient(), sessionReadRequest), new SessionReadResponse());`
- `sources/com/google/android/gms/fitness/request/DataReadRequest.java:24`
  `public class DataReadRequest extends AbstractSafeParcelable {`
- `sources/com/google/android/gms/fitness/request/DataReadRequest.java:25`
  `public static final Parcelable.Creator<DataReadRequest> CREATOR = new zzm();`
- `sources/com/google/android/gms/fitness/request/DataReadRequest.java:43`
  `public DataReadRequest(DataReadRequest dataReadRequest, zzbn zzbnVar) {`
- `sources/com/google/android/gms/fitness/request/DataReadRequest.java:44`
  `this(dataReadRequest.zza, dataReadRequest.zzb, dataReadRequest.zzc, dataReadRequest.zzd, dataReadRequest.zze, dataReadRequest.zzf, dataReadRequest.zzg, dataReadRequest.zzh, dataReadRequest.zzi, dataReadRequest.zzj, dataReadRequest.zzk, dataReadRequest.zzl, zzbnVar, dataReadRequest.zzn, dataReadReque...`
- `sources/com/google/android/gms/fitness/request/DataReadRequest.java:49`
  `if (!(obj instanceof DataReadRequest)) {`
- `sources/com/google/android/gms/fitness/request/DataReadRequest.java:52`
  `DataReadRequest dataReadRequest = (DataReadRequest) obj;`
- `sources/com/google/android/gms/fitness/request/DataReadRequest.java:53`
  `if (!this.zza.equals(dataReadRequest.zza) || !this.zzb.equals(dataReadRequest.zzb) || this.zzc != dataReadRequest.zzc || this.zzd != dataReadRequest.zzd || this.zzg != dataReadRequest.zzg || !this.zzf.equals(dataReadRequest.zzf) || !this.zze.equals(dataReadRequest.zze) || !Objects.equal(this.zzi, da...`
- `sources/com/google/android/gms/fitness/request/DataReadRequest.java:106`
  `sb.append("DataReadRequest{");`
- `sources/com/google/android/gms/fitness/request/DataReadRequest.java:179`
  `DataReadRequest(List list, List list2, long j, long j2, List list3, List list4, int i, long j3, DataSource dataSource, int i2, boolean z, boolean z2, IBinder iBinder, List list5, List list6) {`
- `sources/com/google/android/gms/fitness/request/DataReadRequest.java:263`
  `public DataReadRequest build() {`
- `sources/com/google/android/gms/fitness/request/DataReadRequest.java:276`
  `return new DataReadRequest(this.zza, this.zzb, this.zzf, this.zzg, this.zzc, this.zzd, this.zzj, this.zzk, this.zze, this.zzl, false, this.zzm, (zzbn) null, this.zzh, this.zzi);`
- `sources/com/google/android/gms/fitness/request/DataReadRequest.java:384`
  `public DataReadRequest(List list, List list2, long j, long j2, List list3, List list4, int i, long j3, DataSource dataSource, int i2, boolean z, boolean z2, zzbn zzbnVar, List list5, List list6) {`
- `sources/com/google/android/gms/fitness/request/GoalsReadRequest.java:20`
  `public class GoalsReadRequest extends AbstractSafeParcelable {`
- `sources/com/google/android/gms/fitness/request/GoalsReadRequest.java:21`
  `public static final Parcelable.Creator<GoalsReadRequest> CREATOR = new zzy();`
- `sources/com/google/android/gms/fitness/request/GoalsReadRequest.java:66`
  `public GoalsReadRequest build() {`
- `sources/com/google/android/gms/fitness/request/GoalsReadRequest.java:68`
  `return new GoalsReadRequest(this);`
- `sources/com/google/android/gms/fitness/request/GoalsReadRequest.java:72`
  `GoalsReadRequest(IBinder iBinder, List list, List list2, List list3) {`
- `sources/com/google/android/gms/fitness/request/GoalsReadRequest.java:83`
  `if (!(obj instanceof GoalsReadRequest)) {`
- `sources/com/google/android/gms/fitness/request/GoalsReadRequest.java:86`
  `GoalsReadRequest goalsReadRequest = (GoalsReadRequest) obj;`
- `sources/com/google/android/gms/fitness/request/GoalsReadRequest.java:87`
  `return Objects.equal(this.zzb, goalsReadRequest.zzb) && Objects.equal(this.zzc, goalsReadRequest.zzc) && Objects.equal(this.zzd, goalsReadRequest.zzd);`
- `sources/com/google/android/gms/fitness/request/GoalsReadRequest.java:136`
  `private GoalsReadRequest(zzbw zzbwVar, List list, List list2, List list3) {`
- `sources/com/google/android/gms/fitness/request/GoalsReadRequest.java:140`
  `public GoalsReadRequest(GoalsReadRequest goalsReadRequest, zzbw zzbwVar) {`
- `sources/com/google/android/gms/fitness/request/GoalsReadRequest.java:141`
  `this(zzbwVar, goalsReadRequest.getDataTypes(), goalsReadRequest.zzc, goalsReadRequest.zzd);`
- `sources/com/google/android/gms/fitness/request/SessionReadRequest.java:20`
  `public class SessionReadRequest extends AbstractSafeParcelable {`
- `sources/com/google/android/gms/fitness/request/SessionReadRequest.java:21`
  `public static final Parcelable.Creator<SessionReadRequest> CREATOR = new zzaq();`
- `sources/com/google/android/gms/fitness/request/SessionReadRequest.java:36`
  `public SessionReadRequest(SessionReadRequest sessionReadRequest, zzcj zzcjVar) {`
- `sources/com/google/android/gms/fitness/request/SessionReadRequest.java:37`
  `this(sessionReadRequest.zza, sessionReadRequest.zzb, sessionReadRequest.zzc, sessionReadRequest.zzd, sessionReadRequest.zze, sessionReadRequest.zzf, sessionReadRequest.zzg, sessionReadRequest.zzh, sessionReadRequest.zzi, zzcjVar, sessionReadRequest.zzk, sessionReadRequest.zzl);`
- `sources/com/google/android/gms/fitness/request/SessionReadRequest.java:44`
  `if (!(obj instanceof SessionReadRequest)) {`
- `sources/com/google/android/gms/fitness/request/SessionReadRequest.java:47`
  `SessionReadRequest sessionReadRequest = (SessionReadRequest) obj;`
- `sources/com/google/android/gms/fitness/request/SessionReadRequest.java:48`
  `return Objects.equal(this.zza, sessionReadRequest.zza) && this.zzb.equals(sessionReadRequest.zzb) && this.zzc == sessionReadRequest.zzc && this.zzd == sessionReadRequest.zzd && Objects.equal(this.zze, sessionReadRequest.zze) && Objects.equal(this.zzf, sessionReadRequest.zzf) && this.zzg == sessionRe...`
- `sources/com/google/android/gms/fitness/request/SessionReadRequest.java:125`
  `public SessionReadRequest build() {`
- `sources/com/google/android/gms/fitness/request/SessionReadRequest.java:133`
  `return new SessionReadRequest(this.zza, this.zzb, this.zzc, this.zzd, this.zze, this.zzf, this.zzg, this.zzh, this.zzi, null, this.zzj, this.zzk);`
- `sources/com/google/android/gms/fitness/request/SessionReadRequest.java:199`
  `SessionReadRequest(String str, String str2, long j, long j2, List list, List list2, boolean z, boolean z2, List list3, IBinder iBinder, boolean z3, boolean z4) {`
- `sources/com/google/android/gms/fitness/request/zzaq.java:75`
  `return new SessionReadRequest(strCreateString, strCreateString2, j, j2, arrayListCreateTypedList, arrayListCreateTypedList2, z, z2, arrayListCreateStringList, iBinder, z3, z4);`
- `sources/com/google/android/gms/fitness/request/zzaq.java:80`
  `return new SessionReadRequest[i];`
- `sources/com/google/android/gms/fitness/request/zzm.java:90`
  `return new DataReadRequest(arrayListCreateTypedList, arrayListCreateTypedList2, j, j2, arrayListCreateTypedList3, arrayListCreateTypedList4, i, j3, dataSource, i2, z, z2, iBinder, arrayListCreateLongList, arrayListCreateLongList2);`
- `sources/com/google/android/gms/fitness/request/zzm.java:95`
  `return new DataReadRequest[i];`
- `sources/com/google/android/gms/fitness/request/zzy.java:35`
  `return new GoalsReadRequest(iBinder, arrayList, arrayList2, arrayList3);`
- `sources/com/google/android/gms/fitness/request/zzy.java:40`
  `return new GoalsReadRequest[i];`
- `sources/com/google/android/gms/internal/ads_identifier/zzf.java:12`
  `IInterface iInterfaceQueryLocalInterface = iBinder.queryLocalInterface("com.google.android.gms.ads.identifier.internal.IAdvertisingIdService");`
- `sources/com/google/android/gms/internal/ads_identifier/zzg.java:10`
  `super(iBinder, "com.google.android.gms.ads.identifier.internal.IAdvertisingIdService");`
- `sources/com/google/android/gms/internal/auth/zzby.java:47`
  `BAD_REQUEST("BadRequest"),`
- `sources/com/google/android/gms/internal/fitness/zzbz.java:7`
  `import com.google.android.gms.fitness.request.GoalsReadRequest;`

## BR041

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `resources/com.ble_health_plus.apk/AndroidManifest.xml:185`
  `android:name="com.google.firebase.components:com.google.firebase.analytics.ktx.FirebaseAnalyticsKtxRegistrar"`
- `resources/com.ble_health_plus.apk/AndroidManifest.xml:197`
  `android:name="com.google.firebase.components:com.google.firebase.analytics.connector.internal.AnalyticsConnectorRegistrar"`
- `sources/androidx/annotation/RequiresOptIn.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/annotation/experimental/Experimental.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/appcompat/app/TwilightManager.java:8`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/appcompat/widget/SuggestionsAdapter.java:26`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/LongSparseArrayKt.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/SparseArrayKt.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/content/ContextCompat.java:69`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/content/FileProvider.java:17`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/content/res/TypedArrayApi26ImplKt.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/content/res/TypedArrayKt.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/database/CursorKt.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/graphics/drawable/IconCompat.java:35`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/provider/FontProvider.java:16`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/util/LongSparseArrayKt.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/util/SparseArrayKt.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/view/MenuKt.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/view/ViewGroupKt.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/fragment/app/FragmentContainerView.java:18`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/android/billingclient/api/Purchase.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/android/billingclient/api/PurchaseHistoryRecord.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/android/billingclient/api/SkuDetails.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/base/BaseActivity.java:64`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/base/BaseFragment.java:26`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/billing/BillingListener.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/billing/BillingManager.java:29`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/common/AESCipher.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/common/AppDialog.java:29`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/network/ApiController.java:25`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/network/ApiService.java:28`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/network/Resource.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/bloodpressure/BloodPressureActivity.java:71`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/custom/CustomBarChartRender.java:19`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/custom/PdfView.java:13`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/custom/RulerView.java:24`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/custom/horizontalcalendar/HorizontalCalendarView.java:14`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/glucose/GlucoMeterActivity.java:80`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/heartrate/HeartRateActivity.java:78`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/home/HomeActivity.java:67`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/home/ReminderAddActivity.java:35`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/home/SubscribeActivity.java:32`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/menu/FeedbackFragment.java:16`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/menu/InquiryFragment.java:16`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/menu/MoreFragment.java:62`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/menu/NotificationDataFragment.java:19`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/profile/ForgotPasswordFragment.java:20`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/profile/LoginFragment.java:53`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/profile/OTPVerifyFragment.java:30`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/profile/ProfileFragment.java:27`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/profile/RegisterFragment.java:59`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/profile/ResetPasswordFragment.java:20`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/profile/UserProfileActivity.java:60`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/ble_health_plus/ui/weight/WeightScaleActivity.java:72`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/bumptech/glide/load/data/mediastore/MediaStoreUtil.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/bumptech/glide/load/model/UriLoader.java:14`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/auth/api/accounttransfer/zzr.java:9`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/common/internal/zzn.java:9`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/common/zzaf.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/common/zzag.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/common/zzai.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/common/zzs.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/common/zzt.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/common/zzz.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/fitness/zzff.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/fitness/zzfh.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/fitness/zzfl.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/fitness/zzfm.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/fitness/zzfq.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/location/zzbr.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/location/zzbt.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/location/zzbw.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/location/zzbx.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/location/zzby.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/measurement/zzat.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/measurement/zzee.java:82`
  `Class.forName("com.google.firebase.analytics.FirebaseAnalytics");`
- `sources/com/google/android/gms/internal/play_billing/zzaa.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/play_billing/zzab.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/play_billing/zzae.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/internal/play_billing/zzaf.java:3`
  `import com.google.firebase.analytics.FirebaseAnalytics;`

## BR042

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:27`
  `public class AdvertisingIdClient {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:99`
  `public AdvertisingIdClient(Context context) {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:103`
  `private AdvertisingIdClient(Context context, long j, boolean z, boolean z2) {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:116`
  `public static Info getAdvertisingIdInfo(Context context) throws GooglePlayServicesRepairableException, IllegalStateException, GooglePlayServicesNotAvailableException, IOException {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:118`
  `boolean z = zzbVar.getBoolean("gads:ad_id_app_context:enabled", false);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:119`
  `float f = zzbVar.getFloat("gads:ad_id_app_context:ping_ratio", 0.0f);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:120`
  `String string = zzbVar.getString("gads:ad_id_use_shared_preference:experiment_id", "");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:121`
  `AdvertisingIdClient advertisingIdClient = new AdvertisingIdClient(context, -1L, z, zzbVar.getBoolean("gads:ad_id_use_persistent_service:enabled", false));`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:124`
  `advertisingIdClient.zza(false);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:125`
  `Info info = advertisingIdClient.getInfo();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:126`
  `advertisingIdClient.zza(info, z, f, SystemClock.elapsedRealtime() - jElapsedRealtime, string, null);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:134`
  `AdvertisingIdClient advertisingIdClient = new AdvertisingIdClient(context, -1L, zzbVar.getBoolean("gads:ad_id_app_context:enabled", false), zzbVar.getBoolean("com.google.android.gms.ads.identifier.service.PERSISTENT_START", false));`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:136`
  `advertisingIdClient.zza(false);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:137`
  `return advertisingIdClient.zzb();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:139`
  `advertisingIdClient.finish();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:222`
  `map.put("ad_id_size", Integer.toString(info.getId().length()));`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:230`
  `map.put("tag", "AdvertisingIdClient");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:248`
  `throw new IOException("AdvertisingIdClient is not connected.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:254`
  `throw new IOException("AdvertisingIdClient cannot reconnect.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:261`
  `Log.i("AdvertisingIdClient", "GMS remote exception ", e);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:265`
  `throw new IOException("AdvertisingIdClient cannot reconnect.", e2);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:309`
  `throw new IOException("AdvertisingIdClient is not connected.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:315`
  `throw new IOException("AdvertisingIdClient cannot reconnect.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:322`
  `Log.i("AdvertisingIdClient", "GMS remote exception ", e);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:326`
  `throw new IOException("AdvertisingIdClient cannot reconnect.", e2);`
- `sources/com/google/android/gms/ads/identifier/zza.java:14`
  `zza(AdvertisingIdClient advertisingIdClient, Map map) {`
- `sources/com/google/android/gms/internal/measurement/zznh.java:49`
  `zza = zzhrVar.zzc("measurement.ad_id_cache_time", 10000L);`
- `sources/com/google/android/gms/measurement/internal/zzdy.java:87`
  `public static final zzdx<Long> zza = zza("measurement.ad_id_cache_time", 10000L, 10000L, new zzdu() { // from class: com.google.android.gms.measurement.internal.zzav`
- `sources/com/google/android/gms/measurement/internal/zzfa.java:5`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/measurement/internal/zzfa.java:85`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(true);`
- `sources/com/google/android/gms/measurement/internal/zzfa.java:87`
  `AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(this.zzs.zzau());`
- `sources/com/google/android/gms/measurement/internal/zzfa.java:98`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(false);`
- `sources/com/google/android/gms/measurement/internal/zzjp.java:4`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/measurement/internal/zzjp.java:49`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(true);`
- `sources/com/google/android/gms/measurement/internal/zzjp.java:51`
  `AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(this.zzs.zzau());`
- `sources/com/google/android/gms/measurement/internal/zzjp.java:62`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(false);`

## BR043

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/com/ble_health_plus/ble/scan/BleScanService.java:6`
  `import android.bluetooth.le.BluetoothLeScanner;`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:10`
  `import android.bluetooth.le.ScanResult;`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:32`
  `@Metadata(d1 = {"\u0000t\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000b\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u...`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:37`
  `private BluetoothLeScanner bleScanner;`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:144`
  `bleScanService2.reStartScan();`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:167`
  `BluetoothLeScanner bluetoothLeScanner = this.bleScanner;`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:169`
  `if (bluetoothLeScanner == null) {`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:171`
  `bluetoothLeScanner = null;`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:178`
  `bluetoothLeScanner.stopScan(scanCallback);`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:204`
  `BluetoothLeScanner bluetoothLeScanner = ((BluetoothManager) systemService).getAdapter().getBluetoothLeScanner();`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:205`
  `Intrinsics.checkNotNullExpressionValue(bluetoothLeScanner, "bluetoothManager.adapter.bluetoothLeScanner");`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:206`
  `this.bleScanner = bluetoothLeScanner;`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:215`
  `public void onScanResult(int callbackType, ScanResult result) {`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:216`
  `super.onScanResult(callbackType, result);`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:245`
  `BluetoothLeScanner bluetoothLeScanner = this$0.bleScanner;`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:247`
  `if (bluetoothLeScanner == null) {`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:249`
  `bluetoothLeScanner = null;`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:256`
  `bluetoothLeScanner.stopScan(scanCallback);`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:285`
  `public final void parseBLEFrame(BluetoothDevice device, int rssi, ScanResult result) {`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:369`
  `public final void reStartScan() {`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:370`
  `BluetoothLeScanner bluetoothLeScanner = this.bleScanner;`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:372`
  `if (bluetoothLeScanner == null) {`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:374`
  `bluetoothLeScanner = null;`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:382`
  `bluetoothLeScanner.stopScan(scanCallback);`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:395`
  `this$0.startScan();`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:398`
  `private final void startScan() {`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:402`
  `BluetoothLeScanner bluetoothLeScanner = this.bleScanner;`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:404`
  `if (bluetoothLeScanner == null) {`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:406`
  `bluetoothLeScanner = null;`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:415`
  `bluetoothLeScanner.startScan(arrayList, scanSettings, scanCallback);`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:435`
  `startScan();`
- `sources/com/ble_health_plus/ui/home/DeviceListActivity.java:144`
  `private final void startScan() {`
- `sources/com/ble_health_plus/ui/home/DeviceListActivity.java:619`
  `startScan();`
- `sources/com/ble_health_plus/ui/home/DeviceListActivity.java:636`
  `startScan();`

## BR044

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/androidx/core/content/ContextCompat.java:40`
  `import android.net.wifi.WifiManager;`
- `sources/androidx/core/content/ContextCompat.java:313`
  `map.put(WifiManager.class, "wifi");`

## BR047

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/android/support/v4/media/MediaBrowserCompat.java:681`
  `Log.d(MediaBrowserCompat.TAG, "addSubscription failed with RemoteException parentId=" + str);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:775`
  `Log.i(MediaBrowserCompat.TAG, "Remote error sending a custom action: action=" + str + ", extras=" + bundle, e);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:791`
  `Log.w(MediaBrowserCompat.TAG, "onConnect from service while mState=" + getStateLabel(this.mState) + "... ignoring");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:913`
  `Log.d(MediaBrowserCompat.TAG, "  mServiceBinderWrapper=" + this.mServiceBinderWrapper);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:914`
  `Log.d(MediaBrowserCompat.TAG, "  mCallbacksMessenger=" + this.mCallbacksMessenger);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:915`
  `Log.d(MediaBrowserCompat.TAG, "  mRootId=" + this.mRootId);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:916`
  `Log.d(MediaBrowserCompat.TAG, "  mMediaSessionToken=" + this.mMediaSessionToken);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1094`
  `Log.i(MediaBrowserCompat.TAG, "Remote error subscribing media item: " + str);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1217`
  `Log.i(MediaBrowserCompat.TAG, "The connected service doesn't support sendCustomAction.");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1230`
  `Log.i(MediaBrowserCompat.TAG, "Remote error sending a custom action: action=" + str + ", extras=" + bundle, e);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1429`
  `Log.w(MediaBrowserCompat.TAG, "Unhandled message: " + message + "\n  Client version: 1\n  Service version: " + message.arg1);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1432`
  `Log.e(MediaBrowserCompat.TAG, "Could not unparcel the data.");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1610`
  `Log.w(MediaBrowserCompat.TAG, "Unknown result code: " + i + " (extras=" + this.mExtras + ", resultData=" + bundle + ")");`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:138`
  `Log.e(TAG, "Dead object in getMediaController.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:165`
  `Log.w(TAG, "Failed to create MediaControllerImpl.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1200`
  `Log.e(MediaControllerCompat.TAG, "Dead object in setRating.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1242`
  `Log.e(MediaControllerCompat.TAG, "Dead object in sendCustomAction.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1278`
  `Log.e(MediaControllerCompat.TAG, "Dead object in registerCallback.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1299`
  `Log.e(MediaControllerCompat.TAG, "Dead object in unregisterCallback.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1326`
  `Log.e(MediaControllerCompat.TAG, "Dead object in getPlaybackState.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1401`
  `Log.e(MediaControllerCompat.TAG, "Dead object in getRatingType.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1415`
  `Log.e(MediaControllerCompat.TAG, "Dead object in isCaptioningEnabled.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1428`
  `Log.e(MediaControllerCompat.TAG, "Dead object in getRepeatMode.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1441`
  `Log.e(MediaControllerCompat.TAG, "Dead object in getShuffleMode.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1511`
  `Log.e(MediaControllerCompat.TAG, "Dead object in registerCallback.", e);`
- `sources/androidx/activity/result/ActivityResultRegistry.java:150`
  `Log.w(LOG_TAG, "Dropping pending result for request " + str + ": " + this.mParsedPendingResults.get(str));`
- `sources/androidx/activity/result/ActivityResultRegistry.java:154`
  `Log.w(LOG_TAG, "Dropping pending result for request " + str + ": " + this.mPendingResults.getParcelable(str));`
- `sources/androidx/appcompat/app/ActionBarDrawerToggle.java:218`
  `Log.w("ActionBarDrawerToggle", "DrawerToggle may not show up because NavigationIcon is not visible. You may need to call actionbar.setDisplayHomeAsUpEnabled(true);");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1158`
  `Log.i("AppCompatDelegate", "Failed to instantiate custom view inflater " + string + ". Falling back to default.", th);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1209`
  `Log.i("AppCompatDelegate", "The Activity's LayoutInflater already has a Factory installed so we can not install AppCompat's");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1788`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1794`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR_OVERLAY id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2017`
  `Log.d("AppCompatDelegate", "Exception while getting ActivityInfo", e);`
- `sources/androidx/appcompat/app/ResourcesFlusher.java:166`
  `Log.e(TAG, "Could not retrieve value from ThemedResourceCache#mUnthemedEntries", e3);`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:286`
  `Log.w(SupportMenuInflater.LOG_TAG, "Ignoring attribute 'actionProviderClass'. Action view already specified.");`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:343`
  `Log.w(SupportMenuInflater.LOG_TAG, "Ignoring attribute 'itemActionViewLayout'. Action view already specified.");`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:386`
  `Log.w(SupportMenuInflater.LOG_TAG, "Cannot instantiate class: " + str, e);`
- `sources/androidx/appcompat/view/menu/MenuItemImpl.java:101`
  `Log.e(TAG, "Can't find activity to handle intent; ignoring", e);`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:355`
  `Log.w(TAG, "Failed to invoke TextView#nullLayouts() method", e);`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:213`
  `Log.e(TAG, "Exception while inflating drawable", e);`

## BR050

paper_id: B021
paper_title: Metadata-Based Privacy Assessment for Mobile mHealth

- `audit_reports_integrated/02_规则映射与论文依据_zh.md:335`
  `| R037 | P010 | PolicyLint: Investigating Internal Privacy Policy Contradictions on Google Play | Internal privacy policy contradiction | not_testable | 当前材料未发现支持该规则的证据。 |`
- `resources/com.ble_health_plus.apk/assets/terms-conditions.html:691`
  `<div id="pf5" class="pf w0 h0" data-page-no="5"><div class="pc pc5 w0 h0"><img class="bi x0 y0 w1 h1" alt="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABMkAAAYxCAIAAAAsbFyeAAAACXBIWXMAABYlAAAWJQFJUiTwAAAe1UlEQVR42uzXMQEAAAjDMMC/500EbyKhXzfJAAAAwMNJAAAAgLcEAADAWwIAAOAtAQAA8JYAAADgLQEAAPCWAAAA...`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:26`
  `// see also: "Domain Name Eligibility Policy" at http://www.aeda.ae/eng/aepolicy.php`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:157`
  `// am : https://www.amnic.net/policy/en/Policy_EN.pdf`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:1029`
  `// domaines descriptifs : https://www.afnic.fr/medias/documents/Cadre_legal/Afnic_Naming_Policy_12122016_VEN.pdf`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:1066`
  `// ge : http://www.nic.net.ge/policy_en.pdf`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:1115`
  `// gm : http://www.nic.gm/htmlpages%5Cgm-policy.htm`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:1822`
  `// jo : http://www.dns.jo/Registration_policy.aspx`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:3988`
  `// mt : https://www.nic.org.mt/go/policy`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:5794`
  `// pm : http://www.afnic.fr/medias/documents/AFNIC-naming-policy2012.pdf`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:5840`
  `// http://www.nic.ps/registration/policy.html#reg`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:6090`
  `// st : http://www.nic.st/html/policyrules/`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:6166`
  `// tj : http://www.nic.tj/policy.html`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:6323`
  `// ua : https://hostmaster.ua/policy/?ua`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:6771`
  `// wf : http://www.afnic.fr/medias/documents/AFNIC-naming-policy2012.pdf`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:6783`
  `// yt : http://www.afnic.fr/medias/documents/AFNIC-naming-policy2012.pdf`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:12230`
  `// .KRD : http://nic.krd/data/krd/Registration%20Policy.pdf`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:12797`
  `// privacytools.io : https://www.privacytools.io/`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:12798`
  `// Submitted by Jonah Aragon <jonah@privacytools.io>`

## BR051

paper_id: B013
paper_title: Availability and quality of mobile health app privacy policies

- `audit_reports_integrated/02_规则映射与论文依据_zh.md:335`
  `| R037 | P010 | PolicyLint: Investigating Internal Privacy Policy Contradictions on Google Play | Internal privacy policy contradiction | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:336`
  `| R038 | P010 | PolicyLint: Investigating Internal Privacy Policy Contradictions on Google Play | Policy omits a data recipient or category used by the app | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:337`
  `| R039 | P010 | PolicyLint: Investigating Internal Privacy Policy Contradictions on Google Play | Claimed consent or opt-out not reflected in implementation | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:338`
  `| R040 | P010 | PolicyLint: Investigating Internal Privacy Policy Contradictions on Google Play | Policy narrower than actual technical capability | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:341`
  `| R043 | P011 | A Fait Accompli? An Empirical Study into the Absence of Consent to Third-Party Tracking in Android Apps | Identifier collection before privacy choice | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:351`
  `| R053 | P014 | Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment | Accredited app still uses insecure transport | not_supported | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:352`
  `| R054 | P014 | Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment | Unencrypted local cache of personal data | supported_hypothesis | Room DB 明文 schema 存健康/身份，SharedPreferences 存 USER_DATA JSON；无设备文件恢复。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:353`
  `| R055 | P014 | Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment | Sensitive information recoverable from device after normal use | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:354`
  `| R056 | P014 | Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment | Trust indicators create misleading security expectations | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:355`
  `| R057 | P015 | Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android | Health-sensitivity level exceeds implemented protection | supported_hypothesis | 健康+身份+设备 MAC 同库，备份静态 key，BODY logging；缺运行时确认。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:356`
  `| R058 | P015 | Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android | Role mismatch between app purpose and breadth of data collected | not_supported | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:357`
  `| R059 | P015 | Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android | Cloud sync expands exposure surface for health data | supported_hypothesis | Drive 备份上传完整 DB，硬编码 key 使云端备份保护强度不足；无备份样本。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:358`
  `| R060 | P015 | Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android | Combination of identifiers and health context enables re-identification | supported_hypothesis | ProfileTBL 与健康表、device_mac 同库并进入报告；无运行时 DB 样本。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:359`
  `| R061 | P016 | Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation | Third-party sharing not disclosed in health app privacy materials | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:360`
  `| R062 | P016 | Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation | Health-status inference from metadata or app context | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:361`
  `| R063 | P016 | Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation | Policy and observed traffic mismatch in vulnerable health categories | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:362`
  `| R064 | P016 | Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation | Third-party analytics receive stable identifiers in sensitive app contexts | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:363`
  `| R065 | P017 | Mobile health and privacy: cross sectional study | Third-party trackers embedded in mHealth apps | supported_hypothesis | Firebase Analytics/Crashlytics 作为第三方数据面存在；无实际 tracker payload。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:364`
  `| R066 | P017 | Mobile health and privacy: cross sectional study | Sensitive mHealth traffic lacks sufficient transport protection | not_supported | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:365`
  `| R067 | P017 | Mobile health and privacy: cross sectional study | Privacy policy omits third-party sharing actually observed | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:366`
  `| R068 | P017 | Mobile health and privacy: cross sectional study | Permission and certificate risk profile inconsistent with app sensitivity | not_supported | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:383`
  `| R085 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | Facebook SDK privacy settings left at permissive defaults | not_supported | 未发现 Facebook SDK。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:384`
  `| R086 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | Privacy toggles not explicitly set in app code | not_supported | 未发现 Facebook SDK。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:385`
  `| R087 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | SDK initializes before consent or user control | not_supported | 此规则限定 Facebook SDK；当前无 Facebook。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:386`
  `| R088 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | Disclosed data practices diverge from actual SDK configuration | not_supported | 无 Facebook SDK，且无政策材料。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:387`
  `| R089 | P023 | Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android | SDK collects BLE or Wi-Fi scans for profiling | not_supported | BLE 扫描是一方核心功能，未发现第三方扫描画像 SDK。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:388`
  `| R090 | P023 | Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android | Scan data linked with stable identifiers | not_supported | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:389`
  `| R091 | P023 | Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android | Location surrogate collection despite limited user awareness | not_supported | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:390`
  `| R092 | P023 | Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android | Wireless-scanning SDK traffic to remote profiling services | not_supported | 当前材料未发现支持该规则的证据。 |`
- `resources/com.ble_health_plus.apk/assets/terms-conditions.html:691`
  `<div id="pf5" class="pf w0 h0" data-page-no="5"><div class="pc pc5 w0 h0"><img class="bi x0 y0 w1 h1" alt="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABMkAAAYxCAIAAAAsbFyeAAAACXBIWXMAABYlAAAWJQFJUiTwAAAe1UlEQVR42uzXMQEAAAjDMMC/500EbyKhXzfJAAAAwMNJAAAAgLcEAADAWwIAAOAtAQAA8JYAAADgLQEAAPCWAAAA...`

## BR052

paper_id: B013
paper_title: Availability and quality of mobile health app privacy policies

- `audit_reports_integrated/00_审计总览与结论_zh.md:48`
  `- 论文标题：Security Concerns in Android mHealth Apps；Unaddressed privacy risks in accredited health and wellness apps；Exploring the Far Side of Mobile Health`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:341`
  `| R043 | P011 | A Fait Accompli? An Empirical Study into the Absence of Consent to Third-Party Tracking in Android Apps | Identifier collection before privacy choice | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:351`
  `| R053 | P014 | Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment | Accredited app still uses insecure transport | not_supported | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:352`
  `| R054 | P014 | Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment | Unencrypted local cache of personal data | supported_hypothesis | Room DB 明文 schema 存健康/身份，SharedPreferences 存 USER_DATA JSON；无设备文件恢复。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:353`
  `| R055 | P014 | Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment | Sensitive information recoverable from device after normal use | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:354`
  `| R056 | P014 | Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment | Trust indicators create misleading security expectations | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:355`
  `| R057 | P015 | Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android | Health-sensitivity level exceeds implemented protection | supported_hypothesis | 健康+身份+设备 MAC 同库，备份静态 key，BODY logging；缺运行时确认。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:356`
  `| R058 | P015 | Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android | Role mismatch between app purpose and breadth of data collected | not_supported | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:357`
  `| R059 | P015 | Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android | Cloud sync expands exposure surface for health data | supported_hypothesis | Drive 备份上传完整 DB，硬编码 key 使云端备份保护强度不足；无备份样本。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:358`
  `| R060 | P015 | Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android | Combination of identifiers and health context enables re-identification | supported_hypothesis | ProfileTBL 与健康表、device_mac 同库并进入报告；无运行时 DB 样本。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:359`
  `| R061 | P016 | Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation | Third-party sharing not disclosed in health app privacy materials | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:360`
  `| R062 | P016 | Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation | Health-status inference from metadata or app context | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:361`
  `| R063 | P016 | Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation | Policy and observed traffic mismatch in vulnerable health categories | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:362`
  `| R064 | P016 | Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation | Third-party analytics receive stable identifiers in sensitive app contexts | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:363`
  `| R065 | P017 | Mobile health and privacy: cross sectional study | Third-party trackers embedded in mHealth apps | supported_hypothesis | Firebase Analytics/Crashlytics 作为第三方数据面存在；无实际 tracker payload。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:364`
  `| R066 | P017 | Mobile health and privacy: cross sectional study | Sensitive mHealth traffic lacks sufficient transport protection | not_supported | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:365`
  `| R067 | P017 | Mobile health and privacy: cross sectional study | Privacy policy omits third-party sharing actually observed | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:366`
  `| R068 | P017 | Mobile health and privacy: cross sectional study | Permission and certificate risk profile inconsistent with app sensitivity | not_supported | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:383`
  `| R085 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | Facebook SDK privacy settings left at permissive defaults | not_supported | 未发现 Facebook SDK。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:384`
  `| R086 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | Privacy toggles not explicitly set in app code | not_supported | 未发现 Facebook SDK。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:385`
  `| R087 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | SDK initializes before consent or user control | not_supported | 此规则限定 Facebook SDK；当前无 Facebook。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:386`
  `| R088 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | Disclosed data practices diverge from actual SDK configuration | not_supported | 无 Facebook SDK，且无政策材料。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:387`
  `| R089 | P023 | Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android | SDK collects BLE or Wi-Fi scans for profiling | not_supported | BLE 扫描是一方核心功能，未发现第三方扫描画像 SDK。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:388`
  `| R090 | P023 | Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android | Scan data linked with stable identifiers | not_supported | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:389`
  `| R091 | P023 | Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android | Location surrogate collection despite limited user awareness | not_supported | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:390`
  `| R092 | P023 | Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android | Wireless-scanning SDK traffic to remote profiling services | not_supported | 当前材料未发现支持该规则的证据。 |`
- `resources/com.ble_health_plus.apk/assets/terms-conditions.html:691`
  `<div id="pf5" class="pf w0 h0" data-page-no="5"><div class="pc pc5 w0 h0"><img class="bi x0 y0 w1 h1" alt="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABMkAAAYxCAIAAAAsbFyeAAAACXBIWXMAABYlAAAWJQFJUiTwAAAe1UlEQVR42uzXMQEAAAjDMMC/500EbyKhXzfJAAAAwMNJAAAAgLcEAADAWwIAAOAtAQAA8JYAAADgLQEAAPCWAAAA...`

## BR055

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `sources/androidx/core/util/PatternsCompat.java:15`
  `static final String IANA_TOP_LEVEL_DOMAINS = "(?:(?:aaa|aarp|abb|abbott|abogado|academy|accenture|accountant|accountants|aco|active|actor|ads|adult|aeg|aero|afl|agency|aig|airforce|airtel|allfinanz|alsace|amica|amsterdam|android|apartments|app|apple|aquarelle|aramco|archi|army|arpa|arte|asia|associa...`
- `sources/androidx/core/util/PatternsCompat.java:25`
  `private static final String STRICT_HOST_NAME = "(?:(?:[a-zA-Z0-9[ -\ud7ff豈-﷏ﷰ-\uffef𐀀-\u1fffd𠀀-\u2fffd𰀀-\u3fffd\u40000-\u4fffd\u50000-\u5fffd\u60000-\u6fffd\u70000-\u7fffd\u80000-\u8fffd\u90000-\u9fffd\ua0000-\uafffd\ub0000-\ubfffd\uc0000-\ucfffd\ud0000-\udfffd\ue1000-\uefffd&&[^ [\u2000-\u200a]\u20...`
- `sources/androidx/core/util/PatternsCompat.java:26`
  `private static final String STRICT_TLD = "(?:(?:(?:aaa|aarp|abb|abbott|abogado|academy|accenture|accountant|accountants|aco|active|actor|ads|adult|aeg|aero|afl|agency|aig|airforce|airtel|allfinanz|alsace|amica|amsterdam|android|apartments|app|apple|aquarelle|aramco|archi|army|arpa|arte|asia|associat...`
- `sources/androidx/core/util/PatternsCompat.java:42`
  `Pattern patternCompile3 = Pattern.compile("(?:(?:(?:[a-zA-Z0-9[ -\ud7ff豈-﷏ﷰ-\uffef𐀀-\u1fffd𠀀-\u2fffd𰀀-\u3fffd\u40000-\u4fffd\u50000-\u5fffd\u60000-\u6fffd\u70000-\u7fffd\u80000-\u8fffd\u90000-\u9fffd\ua0000-\uafffd\ub0000-\ubfffd\uc0000-\ucfffd\ud0000-\udfffd\ue1000-\uefffd&&[^ [\u2000-\u200a]\u2028...`

## BR058

paper_id: B022
paper_title: A Study of Android Application Security

- `audit_reports_integrated/02_规则映射与论文依据_zh.md:300`
  `| R002 | P001 | A Study of Android Application Security | Third-party library data concentration | supported_hypothesis | Firebase Analytics/Crashlytics/Messaging/Installations/DataTransport 已注册；无抓包，不能确认具体数据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:333`
  `| R035 | P009 | Cross-Boundary Mobile Tracking: Exploring Java-to-JavaScript Information Diffusion in WebViews | Third-party web content receives native app metadata | supported_hypothesis | 同一 report.html 加载第三方 CDN 脚本；无运行时证据证明脚本读取或外传。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:339`
  `| R041 | P011 | A Fait Accompli? An Empirical Study into the Absence of Consent to Third-Party Tracking in Android Apps | Third-party tracking before consent | supported_hypothesis | Firebase Analytics/Crashlytics 自动注册；无同意 UI/抓包验证。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:340`
  `| R042 | P011 | A Fait Accompli? An Empirical Study into the Absence of Consent to Third-Party Tracking in Android Apps | Consent gate only at UI level | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:341`
  `| R043 | P011 | A Fait Accompli? An Empirical Study into the Absence of Consent to Third-Party Tracking in Android Apps | Identifier collection before privacy choice | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:342`
  `| R044 | P011 | A Fait Accompli? An Empirical Study into the Absence of Consent to Third-Party Tracking in Android Apps | No effective suppression of third-party tracking on decline | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:350`
  `| R052 | P013 | Security Concerns in Android mHealth Apps | Third-party server sharing of mHealth data | supported_hypothesis | Google Drive 上传完整 DB 备份；是用户授权功能但加密弱，缺抓包/备份样本。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:359`
  `| R061 | P016 | Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation | Third-party sharing not disclosed in health app privacy materials | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:362`
  `| R064 | P016 | Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation | Third-party analytics receive stable identifiers in sensitive app contexts | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:363`
  `| R065 | P017 | Mobile health and privacy: cross sectional study | Third-party trackers embedded in mHealth apps | supported_hypothesis | Firebase Analytics/Crashlytics 作为第三方数据面存在；无实际 tracker payload。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:365`
  `| R067 | P017 | Mobile health and privacy: cross sectional study | Privacy policy omits third-party sharing actually observed | not_testable | 当前材料未发现支持该规则的证据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:383`
  `| R085 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | Facebook SDK privacy settings left at permissive defaults | not_supported | 未发现 Facebook SDK。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:384`
  `| R086 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | Privacy toggles not explicitly set in app code | not_supported | 未发现 Facebook SDK。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:385`
  `| R087 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | SDK initializes before consent or user control | not_supported | 此规则限定 Facebook SDK；当前无 Facebook。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:386`
  `| R088 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | Disclosed data practices diverge from actual SDK configuration | not_supported | 无 Facebook SDK，且无政策材料。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:394`
  `| R096 | P024 | Panoptispy: Characterizing Audio and Video Exfiltration from Android Applications | Third-party SDK performs media-related exfiltration in host app | not_supported | 未发现媒体外传第三方 SDK。 |`

## BR060

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `sources/com/ble_health_plus/common/AESCipher.java:88`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/org/apache/http/impl/auth/NTLMEngineImpl.java:409`
  `Cipher cipher = Cipher.getInstance("DES/ECB/NoPadding");`
- `sources/org/apache/http/impl/auth/NTLMEngineImpl.java:412`
  `Cipher cipher2 = Cipher.getInstance("DES/ECB/NoPadding");`
- `sources/org/apache/http/impl/auth/NTLMEngineImpl.java:469`
  `Cipher cipher = Cipher.getInstance("DES/ECB/NoPadding");`
- `sources/org/apache/http/impl/auth/NTLMEngineImpl.java:531`
  `Cipher cipher = Cipher.getInstance("DES/ECB/NoPadding");`

## BR061

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/constraintlayout/core/state/WidgetFrame.java:400`
  `public boolean setValue(String str, CLElement cLElement) throws CLParsingException {`
- `sources/androidx/constraintlayout/motion/widget/KeyAttributes.java:178`
  `public void setValue(String tag, Object value) {`
- `sources/androidx/constraintlayout/motion/widget/KeyCycle.java:526`
  `public void setValue(String tag, Object value) {`
- `sources/androidx/constraintlayout/motion/widget/KeyTimeCycle.java:177`
  `public void setValue(String tag, Object value) {`
- `sources/androidx/constraintlayout/motion/widget/KeyTrigger.java:82`
  `public void setValue(String tag, Object value) {`
- `sources/androidx/core/view/inputmethod/EditorInfoCompat.java:195`
  `static int getProtocol(EditorInfo editorInfo) {`
- `sources/androidx/core/view/inputmethod/InputConnectionCompat.java:98`
  `int protocol = EditorInfoCompat.getProtocol(editorInfo);`
- `sources/androidx/lifecycle/LiveData.java:43`
  `LiveData.this.setValue(obj);`
- `sources/androidx/lifecycle/LiveData.java:65`
  `LiveData.this.setValue(obj2);`
- `sources/com/google/android/gms/auth/api/accounttransfer/AccountTransferClient.java:53`
  `public Task<Void> sendData(String str, byte[] bArr) {`
- `sources/com/google/api/client/http/GenericUrl.java:58`
  `this(url.getProtocol(), url.getHost(), url.getPort(), url.getPath(), url.getRef(), url.getQuery(), url.getUserInfo(), z);`
- `sources/com/google/api/services/people/v1/model/ImClient.java:54`
  `public String getProtocol() {`
- `sources/com/google/common/collect/Synchronized.java:2032`
  `public V setValue(V v) {`
- `sources/com/google/common/collect/Synchronized.java:2035`
  `value = delegate().setValue(v);`
- `sources/com/google/common/reflect/ClassPath.java:377`
  `if (classPathEntry.getProtocol().equals("file")) {`
- `sources/com/google/common/reflect/ClassPath.java:399`
  `if (next.getProtocol().equals("file")) {`
- `sources/com/google/common/reflect/ClassPath.java:447`
  `Preconditions.checkArgument(url.getProtocol().equals("file"));`
- `sources/com/google/common/util/concurrent/CombinedFuture.java:117`
  `public void setValue(ListenableFuture<V> listenableFuture) {`
- `sources/okhttp3/Handshake.java:225`
  `String protocol = handshake.getProtocol();`
- `sources/okhttp3/OkHttpClient.java:114`
  `this.protocols = builder.getProtocols$okhttp();`
- `sources/okhttp3/OkHttpClient.java:534`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000ø\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b...`
- `sources/okhttp3/OkHttpClient.java:762`
  `public final List<Protocol> getProtocols$okhttp() {`
- `sources/okhttp3/Response.java:124`
  `public final Protocol getProtocol() {`
- `sources/okhttp3/Response.java:294`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000l\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\t\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u...`
- `sources/okhttp3/Response.java:319`
  `/* JADX INFO: renamed from: getProtocol$okhttp, reason: from getter */`
- `sources/okhttp3/Response.java:320`
  `public final Protocol getProtocol() {`
- `sources/okhttp3/internal/platform/Platform.java:233`
  `arrayList3.add(((Protocol) it.next()).getProtocol());`
- `sources/org/apache/http/HttpMessage.java:24`
  `ProtocolVersion getProtocolVersion();`
- `sources/org/apache/http/ProtocolVersion.java:19`
  `public final String getProtocol() {`
- `sources/org/apache/http/RequestLine.java:7`
  `ProtocolVersion getProtocolVersion();`
- `sources/org/apache/http/StatusLine.java:5`
  `ProtocolVersion getProtocolVersion();`
- `sources/org/apache/http/client/methods/HttpRequestBase.java:26`
  `public ProtocolVersion getProtocolVersion() {`
- `sources/org/apache/http/client/methods/HttpRequestBase.java:39`
  `ProtocolVersion protocolVersion = getProtocolVersion();`
- `sources/org/apache/http/client/methods/HttpRequestBase.java:66`
  `return getMethod() + " " + getURI() + " " + getProtocolVersion();`
- `sources/org/apache/http/client/methods/HttpRequestWrapper.java:35`
  `this.version = httpRequest2.getRequestLine().getProtocolVersion();`
- `sources/org/apache/http/client/methods/HttpRequestWrapper.java:46`
  `public ProtocolVersion getProtocolVersion() {`
- `sources/org/apache/http/client/methods/HttpRequestWrapper.java:48`
  `return protocolVersion != null ? protocolVersion : this.original.getProtocolVersion();`
- `sources/org/apache/http/client/methods/HttpRequestWrapper.java:89`
  `this.requestLine = new BasicRequestLine(this.method, uri, getProtocolVersion());`
- `sources/org/apache/http/client/methods/RequestBuilder.java:170`
  `this.version = httpRequest.getRequestLine().getProtocolVersion();`
- `sources/org/apache/http/client/protocol/RequestExpectContinue.java:23`
  `ProtocolVersion protocolVersion = httpRequest.getRequestLine().getProtocolVersion();`

## BR062

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:60`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0012\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0006\bf\u0018\u00002\u00020\u0001J.\u0010\u0002\...`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:62`
  `void onCharacteristicChanged(String macAddress, BluetoothGatt gatt, BluetoothGattCharacteristic characteristic, byte[] value);`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:54`
  `@Metadata(d1 = {"\u0000h\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\t...`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:429`
  `public void onCharacteristicRead(String macAddress, BluetoothGatt gatt, BluetoothGattCharacteristic characteristic, byte[] value) {`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:496`
  `public void onCharacteristicChanged(String macAddress, BluetoothGatt gatt, BluetoothGattCharacteristic characteristic, byte[] value) {`

## BR063

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

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
- `sources/androidx/exifinterface/media/ExifInterface.java:1876`
  `byte[] bArr = this.mThumbnailBytes;`
- `sources/androidx/exifinterface/media/ExifInterface.java:2136`
  `byte[] bArr = new byte[5000];`
- `sources/androidx/exifinterface/media/ExifInterface.java:2367`
  `byte[] bArr = IDENTIFIER_EXIF_APP1;`
- `sources/androidx/exifinterface/media/ExifInterface.java:2369`
  `byte[] bArr2 = new byte[bArr.length];`
- `sources/androidx/exifinterface/media/ExifInterface.java:2374`
  `byte[] bArr3 = IDENTIFIER_EXIF_APP1;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:204`
  `int iUpdatePositionWithPostponed2 = updatePositionWithPostponed(updateOp.positionStart + (i * i5), updateOp.cmd);`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:205`
  `int i6 = updateOp.cmd;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:209`
  `UpdateOp updateOpObtainUpdateOp = obtainUpdateOp(updateOp.cmd, iUpdatePositionWithPostponed, i4, updateOp.payload);`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:212`
  `if (updateOp.cmd == 4) {`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:222`
  `UpdateOp updateOpObtainUpdateOp2 = obtainUpdateOp(updateOp.cmd, iUpdatePositionWithPostponed, i4, obj);`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:230`
  `int i2 = updateOp.cmd;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:508`
  `int cmd;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:514`
  `this.cmd = i;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:521`
  `int i = this.cmd;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:569`
  `updateOpAcquire.cmd = i;`
- `sources/androidx/room/RoomSQLiteQuery.java:96`
  `this.mBlobBindings = new byte[i2][];`
- `sources/com/airbnb/lottie/LottieCompositionFactory.java:29`
  `private static final byte[] MAGIC = {80, 75, 3, 4};`
- `sources/com/airbnb/lottie/manager/ImageAssetManager.java:86`
  `byte[] bArrDecode = Base64.decode(fileName.substring(fileName.indexOf(44) + 1), 0);`
- `sources/com/ble_health_plus/ble/model/HeartRateModel.java:167`
  `this.heartRate = BLEUtils.INSTANCE.byteToInt(new byte[]{data[1]});`
- `sources/com/ble_health_plus/ble/model/HeartRateModel.java:169`
  `this.heartRate = BLEUtils.INSTANCE.byteToInt(new byte[]{data[2], data[1]});`
- `sources/com/bumptech/glide/gifdecoder/GifHeaderParser.java:32`
  `private final byte[] block = new byte[256];`
- `sources/com/bumptech/glide/load/resource/bitmap/Downsampler.java:111`
  `byte[] bArr = (byte[]) this.byteArrayPool.get(65536, byte[].class);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:114`
  `byte[] bytes = eventInternal.getEncodedPayload().getBytes();`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:125`
  `contentValues.put("payload", z ? bytes : new byte[0]);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:130`
  `byte[] bArrCopyOfRange = Arrays.copyOfRange(bytes, (i - 1) * maxBlobByteSizePerRow, Math.min(i * maxBlobByteSizePerRow, bytes.length));`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:452`
  `byte[] blob = cursor.getBlob(0);`
- `sources/com/google/android/gms/common/zzs.java:31`
  `byte[] bArr = iObjectWrapperZzd == null ? null : (byte[]) ObjectWrapper.unwrap(iObjectWrapperZzd);`
- `sources/com/google/android/gms/location/SleepClassifyEvent.java:53`
  `byte[] bArr = (byte[]) arrayList.get(i);`
- `sources/com/google/android/gms/location/SleepSegmentEvent.java:49`
  `byte[] bArr = (byte[]) arrayList.get(i);`
- `sources/com/google/android/gms/measurement/internal/zzee.java:121`
  `return zzq(3, new byte[0]);`
- `sources/com/google/api/client/googleapis/mtls/MtlsUtils.java:68`
  `throw new IOException("Interrupted executing certificate provider command", e);`
- `sources/com/google/api/client/json/webtoken/JsonWebSignature.java:216`
  `byte[] bArr = this.signedContentBytes;`
- `sources/com/google/api/client/json/webtoken/JsonWebSignature.java:262`
  `byte[] bArrDecodeBase64 = Base64.decodeBase64(str.substring(0, iIndexOf));`

## BR064

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:202`
  `String name = xml.getName();`
- `sources/androidx/core/app/NotificationCompat.java:1362`
  `if (TextUtils.isEmpty(person.getName())) {`
- `sources/androidx/core/app/NotificationCompat.java:1370`
  `return this.mUser.getName();`
- `sources/androidx/core/app/NotificationCompat.java:1461`
  `messagingStyle = new Notification.MessagingStyle(this.mUser.getName());`
- `sources/androidx/core/app/NotificationCompat.java:1543`
  `CharSequence name = message.getPerson() == null ? "" : message.getPerson().getName();`
- `sources/androidx/core/app/NotificationCompat.java:1545`
  `name = this.mUser.getName();`
- `sources/androidx/core/app/NotificationCompat.java:1564`
  `bundle.putCharSequence(NotificationCompat.EXTRA_SELF_DISPLAY_NAME, this.mUser.getName());`
- `sources/androidx/core/content/FileProvider.java:194`
  `String name = fileProviderPathsMetaData.getName();`
- `sources/androidx/core/util/DebugUtils.java:12`
  `if ((simpleName == null || simpleName.length() <= 0) && (iLastIndexOf = (simpleName = obj.getClass().getName()).lastIndexOf(46)) > 0) {`
- `sources/androidx/savedstate/SavedStateRegistry.java:120`
  `String name = clazz.getName();`
- `sources/androidx/versionedparcelable/VersionedParcel.java:991`
  `Method method = this.mWriteCache.get(cls.getName());`
- `sources/androidx/versionedparcelable/VersionedParcel.java:998`
  `this.mWriteCache.put(cls.getName(), declaredMethod);`
- `sources/androidx/versionedparcelable/VersionedParcel.java:1003`
  `Class cls2 = this.mParcelizerCache.get(cls.getName());`
- `sources/androidx/versionedparcelable/VersionedParcel.java:1007`
  `Class<?> cls3 = Class.forName(String.format("%s.%sParcelizer", cls.getPackage().getName(), cls.getSimpleName()), false, cls.getClassLoader());`
- `sources/androidx/versionedparcelable/VersionedParcel.java:1008`
  `this.mParcelizerCache.put(cls.getName(), cls3);`
- `sources/com/airbnb/lottie/animation/content/GradientFillContent.java:65`
  `this.name = gradientFill.getName();`
- `sources/com/airbnb/lottie/animation/content/GradientFillContent.java:166`
  `public String getName() {`
- `sources/com/airbnb/lottie/animation/content/GradientStrokeContent.java:41`
  `this.name = gradientStroke.getName();`
- `sources/com/airbnb/lottie/animation/content/GradientStrokeContent.java:77`
  `public String getName() {`
- `sources/com/airbnb/lottie/model/layer/CompositionLayer.java:131`
  `if (((!this.clipToCompositionBounds && "__container".equals(this.layerModel.getName())) || this.newClipRect.isEmpty()) ? true : canvas.clipRect(this.newClipRect)) {`
- `sources/com/ble_health_plus/R.java:4458`
  `public static final int tvDeviceName = 0x7f0a03cd;`
- `sources/com/ble_health_plus/R.java:5318`
  `public static final int strDeviceName = 0x7f1200ee;`
- `sources/com/ble_health_plus/R.java:5408`
  `public static final int strHintDeviceName = 0x7f120148;`
- `sources/com/ble_health_plus/R.java:5651`
  `public static final int strWarAddDevicename = 0x7f12023b;`
- `sources/com/ble_health_plus/adapter/DashboardAdapter.java:54`
  `@Metadata(d1 = {"\u0000v\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u0002\n\u0000\n\u0002\u0010 \n\u0...`
- `sources/com/ble_health_plus/adapter/DashboardAdapter.java:205`
  `AppCompatTextView tvDeviceName = binding.tvDeviceName;`
- `sources/com/ble_health_plus/adapter/DashboardAdapter.java:206`
  `Intrinsics.checkNotNullExpressionValue(tvDeviceName, "tvDeviceName");`
- `sources/com/ble_health_plus/adapter/DashboardAdapter.java:207`
  `setDeviceName(tvDeviceName, deviceDataModel);`
- `sources/com/ble_health_plus/adapter/DashboardAdapter.java:258`
  `AppCompatTextView tvDeviceName2 = binding2.tvDeviceName;`
- `sources/com/ble_health_plus/adapter/DashboardAdapter.java:259`
  `Intrinsics.checkNotNullExpressionValue(tvDeviceName2, "tvDeviceName");`
- `sources/com/ble_health_plus/adapter/DashboardAdapter.java:260`
  `setDeviceName(tvDeviceName2, deviceDataModel);`
- `sources/com/ble_health_plus/adapter/DashboardAdapter.java:313`
  `AppCompatTextView tvDeviceName3 = binding3.tvDeviceName;`
- `sources/com/ble_health_plus/adapter/DashboardAdapter.java:314`
  `Intrinsics.checkNotNullExpressionValue(tvDeviceName3, "tvDeviceName");`
- `sources/com/ble_health_plus/adapter/DashboardAdapter.java:315`
  `setDeviceName(tvDeviceName3, deviceDataModel);`
- `sources/com/ble_health_plus/adapter/DashboardAdapter.java:351`
  `TextView tvDeviceName4 = binding4.tvDeviceName;`
- `sources/com/ble_health_plus/adapter/DashboardAdapter.java:352`
  `Intrinsics.checkNotNullExpressionValue(tvDeviceName4, "tvDeviceName");`
- `sources/com/ble_health_plus/adapter/DashboardAdapter.java:353`
  `setDeviceName(tvDeviceName4, deviceDataModel);`
- `sources/com/ble_health_plus/adapter/DashboardAdapter.java:541`
  `private final void setDeviceName(TextView tvDeviceName, DeviceDataModel dataModel) {`
- `sources/com/ble_health_plus/adapter/DashboardAdapter.java:544`
  `tvDeviceName.setText(dataModel.getDevice_name());`
- `sources/com/ble_health_plus/adapter/DashboardAdapter.java:546`
  `tvDeviceName.setText(dataModel.getAliasName());`
- `sources/com/ble_health_plus/adapter/DeviceListAdapter.java:58`
  `if (!TextUtils.isEmpty(String.valueOf(scanDataModel != null ? scanDataModel.getDeviceName() : null))) {`
- `sources/com/ble_health_plus/adapter/DeviceListAdapter.java:59`
  `holder.getItemDeviceListBinding().tvDeviceName.setText(String.valueOf(scanDataModel != null ? scanDataModel.getDeviceName() : null));`
- `sources/com/ble_health_plus/adapter/DeviceListAdapter.java:61`
  `holder.getItemDeviceListBinding().tvDeviceName.setText("N/A");`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor$mGattCallback$1.java:51`
  `bleConnectionListener.onDisconnected(device.getAddress());`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor$mGattCallback$1.java:61`
  `bleConnectionListener2.onConnected(device2.getAddress());`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor$mGattCallback$1.java:96`
  `bleConnectionListener.onServiceDiscovered(baseBleActor, device.getAddress());`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor$mGattCallback$1.java:111`
  `String address = device.getAddress();`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor$mGattCallback$1.java:128`
  `bleConnectionListener.onCharacteristicChanged(device.getAddress(), gatt, characteristic, value);`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor$mGattCallback$1.java:143`
  `String address = device.getAddress();`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor$mGattCallback$1.java:159`
  `bleConnectionListener.onCharacteristicRead(device.getAddress(), gatt, characteristic, value);`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor$mGattCallback$1.java:201`
  `bleConnectionListener.onDescriptorWrite(baseBleActor2, device.getAddress());`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:109`
  `bleConnectionListener.pairedDevice(device.getAddress(), this.getType());`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:283`
  `if (Intrinsics.areEqual(((BluetoothDevice) next).getAddress(), bluetoothDevice.getAddress())) {`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:405`
  `bleConnectionListener.onDescriptorWrite(this, bluetoothDevice.getAddress());`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:492`
  `listener.onConnectionFailed(device != null ? device.getAddress() : null);`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:54`
  `@Metadata(d1 = {"\u0000h\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\t...`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:122`
  `@Metadata(d1 = {"\u0000<\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0015\n\u0002\u0010\u000e\n\u0002\b\t\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\b\u0086...`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:195`
  `public final void addDeviceInConnectionQueue(String mac, String type, BluetoothDevice device) {`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:196`
  `Intrinsics.checkNotNullParameter(mac, "mac");`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:200`
  `bleConnectionService.connectionQueue(mac, type, device);`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:323`
  `public final void connectionQueue(String mac, String type, BluetoothDevice device) {`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:324`
  `AppLog.INSTANCE.e(TAG, "--------> connectionQueue:  " + mac + TokenParser.SP);`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:325`
  `if (!this.connectDevice.containsKey(mac)) {`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:328`
  `this.connectDevice.put(mac, baseBleActor);`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:332`
  `BaseBleActor baseBleActor2 = this.connectDevice.get(mac);`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:338`
  `sendEvent(mac, ConnectionStatus.ALREADY_CONNECTED);`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:286`
  `AppLog.INSTANCE.d(TAG, "device : " + device.getAddress());`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:301`
  `if (Intrinsics.areEqual(((ScanDataModel) next).getDeviceMac(), device.getAddress())) {`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:316`
  `String name = device.getName();`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:317`
  `scanDataModel.setDeviceName(name != null ? name : "");`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:320`
  `intent.putExtra(KEY_MAC_ADDRESS, device.getAddress());`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:328`
  `AppLog.INSTANCE.e(TAG, "device : " + device.getAddress());`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:344`
  `sb2.append(device.getAddress());`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:345`
  `String name2 = device.getName();`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:351`
  `String address = device.getAddress();`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:358`
  `String name3 = device.getName();`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:359`
  `scanDataModel2.setDeviceName(name3 != null ? name3 : "");`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:363`
  `intent2.putExtra(KEY_MAC_ADDRESS, device.getAddress());`
- `sources/com/ble_health_plus/ble/scan/ScanDataModel.java:11`
  `@Metadata(d1 = {"\u00004\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\b\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\t\n\u0002\b\u0005\n\u0002\u0010\u0012\n\u0002\b\u0007\u0018\u00002\u00020\u0001B\u0005¢\u0006\u0002\u...`
- `sources/com/ble_health_plus/ble/scan/ScanDataModel.java:18`
  `private String deviceName = new String();`

## BR065

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/com/ble_health_plus/ble/connection/BaseBleActor$mGattCallback$1.java:19`
  `@Metadata(d1 = {"\u00005\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0012\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0003*\u0001\u0000\b\n\u0018\u00002\u00020\u0001J\u0018\u...`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor$mGattCallback$1.java:88`
  `public void onServicesDiscovered(BluetoothGatt gatt, int status) {`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor$mGattCallback$1.java:90`
  `super.onServicesDiscovered(gatt, status);`

## BR066

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:530`
  `if (TextUtils.isEmpty(serUUID) || TextUtils.isEmpty(charUUID) || (bluetoothGatt = this.mBluetoothGatt) == null || bluetoothGatt == null || (service = bluetoothGatt.getService(UUID.fromString(serUUID))) == null) {`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:534`
  `BluetoothGattCharacteristic characteristic = service.getCharacteristic(UUID.fromString(charUUID));`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:556`
  `if (!TextUtils.isEmpty(serUUID) && !TextUtils.isEmpty(charUUID) && (bluetoothGatt = this.mBluetoothGatt) != null && (service = bluetoothGatt.getService(UUID.fromString(serUUID))) != null) {`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:558`
  `BluetoothGattCharacteristic characteristic = service.getCharacteristic(UUID.fromString(charUUID));`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:225`
  `ParcelUuid parcelUuidFromString = ParcelUuid.fromString("00001810-0000-1000-8000-00805F9B34FB");`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:228`
  `ParcelUuid parcelUuidFromString2 = ParcelUuid.fromString("00002A35-0000-1000-8000-00805F9B34FB");`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:231`
  `ParcelUuid parcelUuidFromString3 = ParcelUuid.fromString("0000180D-0000-1000-8000-00805F9B34FB");`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:234`
  `ParcelUuid parcelUuidFromString4 = ParcelUuid.fromString("00002A37-0000-1000-8000-00805F9B34FB");`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:237`
  `ParcelUuid parcelUuidFromString5 = ParcelUuid.fromString("0000181D-0000-1000-8000-00805F9B34FB");`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:240`
  `ParcelUuid parcelUuidFromString6 = ParcelUuid.fromString("00002A9D-0000-1000-8000-00805F9B34FB");`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:243`
  `ParcelUuid parcelUuidFromString7 = ParcelUuid.fromString("00002A9E-0000-1000-8000-00805F9B34FB");`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:246`
  `ParcelUuid parcelUuidFromString8 = ParcelUuid.fromString("23434100-1FE4-1EFF-80CB-00FF78297D8B");`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:249`
  `ParcelUuid parcelUuidFromString9 = ParcelUuid.fromString("23434101-1FE4-1EFF-80CB-00FF78297D8B");`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:252`
  `ParcelUuid parcelUuidFromString10 = ParcelUuid.fromString("00001808-0000-1000-8000-00805F9B34FB");`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:255`
  `ParcelUuid parcelUuidFromString11 = ParcelUuid.fromString("00002A18-0000-1000-8000-00805F9B34FB");`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:258`
  `ParcelUuid parcelUuidFromString12 = ParcelUuid.fromString("00002A34-0000-1000-8000-00805F9B34FB");`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:261`
  `ParcelUuid parcelUuidFromString13 = ParcelUuid.fromString("00002A52-0000-1000-8000-00805F9B34FB");`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:272`
  `this.filters.add(new ScanFilter.Builder().setServiceUuid(BleConnectionService.INSTANCE.getHEART_RATE_SERVICE()).build());`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:276`
  `this.filters.add(new ScanFilter.Builder().setServiceUuid(BleConnectionService.INSTANCE.getBLOOD_PRESSURE_SERVICE()).build());`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:278`
  `this.filters.add(new ScanFilter.Builder().setServiceUuid(BleConnectionService.INSTANCE.getWEIGHT_SCALE_SERVICE()).build());`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:280`
  `this.filters.add(new ScanFilter.Builder().setServiceUuid(BleConnectionService.INSTANCE.getGLUCOSE_SERVICE()).build());`
- `sources/com/ble_health_plus/ble/scan/BleScanService.java:334`
  `sb.append(scanRecord3.getServiceUuids());`

## BR067

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/com/ble_health_plus/adapter/DashboardAdapter.java:694`
  `binding.chart2.setPinchZoom(false);`
- `sources/com/ble_health_plus/adapter/DashboardAdapter.java:755`
  `binding.chart1.setPinchZoom(false);`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:334`
  `device.createBond();`
- `sources/com/ble_health_plus/extensions/ExtensionsKt.java:48`
  `@Metadata(d1 = {"\u0000z\n\u0000\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\t\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0011\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u...`
- `sources/com/ble_health_plus/extensions/ExtensionsKt.java:762`
  `public static final void removeBond(BluetoothDevice bluetoothDevice) {`
- `sources/com/ble_health_plus/extensions/ExtensionsKt.java:765`
  `bluetoothDevice.getClass().getMethod("removeBond", new Class[0]).invoke(bluetoothDevice, new Object[0]);`
- `sources/com/ble_health_plus/ui/bloodpressure/BloodPressureActivity.java:1434`
  `candleStickChart.setPinchZoom(false);`
- `sources/com/ble_health_plus/ui/glucose/GlucoMeterActivity.java:1521`
  `lineChart.setPinchZoom(false);`
- `sources/com/ble_health_plus/ui/heartrate/HeartRateActivity.java:1328`
  `barChart.setPinchZoom(false);`
- `sources/com/ble_health_plus/ui/heartrate/HeartRateActivity.java:1513`
  `lineChart.setPinchZoom(false);`
- `sources/com/ble_health_plus/ui/weight/WeightScaleActivity.java:1102`
  `lineChart.setPinchZoom(false);`
- `sources/com/github/mikephil/charting/charts/BarLineChartBase.java:869`
  `public void setPinchZoom(boolean z) {`

## BR068

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/com/google/android/gms/auth/api/accounttransfer/AccountTransferStatusCodes.java:8`
  `public static final int CHALLENGE_NOT_ALLOWED = 20503;`
- `sources/com/google/android/gms/auth/api/accounttransfer/AccountTransferStatusCodes.java:25`
  `case CHALLENGE_NOT_ALLOWED /* 20503 */:`
- `sources/com/google/android/gms/auth/api/accounttransfer/AccountTransferStatusCodes.java:26`
  `return "CHALLENGE_NOT_ALLOWED";`
- `sources/com/google/android/gms/auth/api/accounttransfer/DeviceMetaData.java:28`
  `public boolean isChallengeAllowed() {`
- `sources/com/google/android/gms/auth/api/accounttransfer/DeviceMetaData.java:42`
  `SafeParcelWriter.writeBoolean(parcel, 4, isChallengeAllowed());`
- `sources/com/google/android/gms/internal/auth/zzby.java:27`
  `CHALLENGE_REQUIRED("ChallengeRequired"),`
- `sources/okhttp3/Challenge.java:87`
  `public final Challenge withCharset(Charset charset) {`
- `sources/okhttp3/Challenge.java:93`
  `return new Challenge(this.scheme, (Map<String, String>) mutableMap);`
- `sources/okhttp3/Response.java:22`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000p\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u00...`
- `sources/okhttp3/internal/http/HttpHeaders.java:37`
  `int size = parseChallenges.size();`
- `sources/okhttp3/internal/http/HttpHeaders.java:39`
  `if (StringsKt.equals(headerName, parseChallenges.name(i), true)) {`
- `sources/okhttp3/internal/http/HttpHeaders.java:41`
  `readChallengeHeader(new Buffer().writeUtf8(parseChallenges.value(i)), arrayList);`
- `sources/okhttp3/internal/http/HttpHeaders.java:43`
  `Platform.INSTANCE.get().log("Unable to parse challenge", 5, e);`
- `sources/okhttp3/internal/http/HttpHeaders.java:63`
  `private static final void readChallengeHeader(okio.Buffer r7, java.util.List<okhttp3.Challenge> r8) throws java.io.EOFException {`
- `sources/okhttp3/internal/http/HttpHeaders.java:68`
  `throw new UnsupportedOperationException("Method not decompiled: okhttp3.internal.http.HttpHeaders.readChallengeHeader(okio.Buffer, java.util.List):void");`
- `sources/org/apache/http/auth/MalformedChallengeException.java:9`
  `public MalformedChallengeException() {`
- `sources/org/apache/http/auth/MalformedChallengeException.java:12`
  `public MalformedChallengeException(String str) {`
- `sources/org/apache/http/auth/MalformedChallengeException.java:16`
  `public MalformedChallengeException(String str, Throwable th) {`
- `sources/org/apache/http/client/protocol/RequestAuthCache.java:61`
  `if (proxyHost == null || proxyAuthState == null || proxyAuthState.getState() != AuthProtocolState.UNCHALLENGED || (authScheme = authCache.get(proxyHost)) == null) {`
- `sources/org/apache/http/client/protocol/RequestAuthenticationBase.java:43`
  `this.log.debug("Generating response to an authentication challenge using " + authScheme2.getSchemeName() + " scheme");`
- `sources/org/apache/http/impl/auth/AuthSchemeBase.java:32`
  `public void processChallenge(Header header) throws MalformedChallengeException {`
- `sources/org/apache/http/impl/auth/AuthSchemeBase.java:38`
  `this.challengeState = ChallengeState.TARGET;`
- `sources/org/apache/http/impl/auth/AuthSchemeBase.java:40`
  `this.challengeState = ChallengeState.PROXY;`
- `sources/org/apache/http/impl/auth/AuthSchemeBase.java:42`
  `throw new MalformedChallengeException("Unexpected header name: " + name);`
- `sources/org/apache/http/impl/auth/AuthSchemeBase.java:66`
  `throw new MalformedChallengeException("Invalid scheme identifier: " + strSubstring);`
- `sources/org/apache/http/impl/auth/AuthSchemeBase.java:68`
  `parseChallenge(charArrayBuffer, i, charArrayBuffer.length());`
- `sources/org/apache/http/impl/auth/DigestScheme.java:76`
  `throw new MalformedChallengeException("Authentication challenge is empty");`
- `sources/org/apache/http/impl/auth/GGSSchemeBase.java:194`
  `protected void parseChallenge(CharArrayBuffer charArrayBuffer, int i, int i2) throws MalformedChallengeException {`
- `sources/org/apache/http/impl/auth/GGSSchemeBase.java:197`
  `this.log.debug("Received challenge '" + strSubstringTrimmed + "' from the auth server");`
- `sources/org/apache/http/impl/auth/GGSSchemeBase.java:201`
  `this.state = State.CHALLENGE_RECEIVED;`
- `sources/org/apache/http/impl/auth/HttpAuthenticator.java:90`
  `public boolean handleAuthChallenge(HttpHost httpHost, HttpResponse httpResponse, AuthenticationStrategy authenticationStrategy, AuthState authState, HttpContext httpContext) {`
- `sources/org/apache/http/impl/auth/HttpAuthenticator.java:96`
  `Map<String, Header> challenges = authenticationStrategy.getChallenges(httpHost, httpResponse, httpContext);`
- `sources/org/apache/http/impl/auth/HttpAuthenticator.java:97`
  `if (challenges.isEmpty()) {`
- `sources/org/apache/http/impl/auth/HttpAuthenticator.java:98`
  `this.log.debug("Response contains no authentication challenges");`
- `sources/org/apache/http/impl/auth/HttpAuthenticator.java:113`
  `queueSelect = authenticationStrategy.select(challenges, httpHost, httpResponse, httpContext);`
- `sources/org/apache/http/impl/auth/HttpAuthenticator.java:120`
  `authState.setState(AuthProtocolState.CHALLENGED);`
- `sources/org/apache/http/impl/auth/HttpAuthenticator.java:148`
  `queueSelect = authenticationStrategy.select(challenges, httpHost, httpResponse, httpContext);`
- `sources/org/apache/http/impl/auth/HttpAuthenticator.java:152`
  `} catch (MalformedChallengeException e) {`
- `sources/org/apache/http/impl/auth/HttpAuthenticator.java:154`
  `this.log.warn("Malformed challenge: " + e.getMessage());`
- `sources/org/apache/http/impl/auth/HttpAuthenticator.java:174`
  `this.log.debug("Generating response to an authentication challenge using " + authScheme2.getSchemeName() + " scheme");`
- `sources/org/apache/http/impl/auth/NTLMEngineImpl.java:561`
  `private final byte[] exportedSessionKey;`
- `sources/org/apache/http/impl/auth/NTLMEngineImpl.java:570`
  `this.exportedSessionKey = bArr;`
- `sources/org/apache/http/impl/auth/NTLMEngineImpl.java:1024`
  `byte[] lMUserSessionKey;`
- `sources/org/apache/http/impl/auth/NTLMEngineImpl.java:1080`
  `this.exportedSessionKey = secondaryKey;`
- `sources/org/apache/http/impl/auth/NTLMEngineImpl.java:1081`
  `this.sessionKey = NTLMEngineImpl.RC4(secondaryKey, lMUserSessionKey);`
- `sources/org/apache/http/impl/auth/NTLMEngineImpl.java:1083`
  `this.sessionKey = lMUserSessionKey;`
- `sources/org/apache/http/impl/auth/NTLMEngineImpl.java:1084`
  `this.exportedSessionKey = lMUserSessionKey;`
- `sources/org/apache/http/impl/auth/NTLMEngineImpl.java:1090`
  `this.sessionKey = null;`
- `sources/org/apache/http/impl/auth/NTLMEngineImpl.java:1091`
  `this.exportedSessionKey = null;`
- `sources/org/apache/http/impl/auth/NTLMEngineImpl.java:1099`
  `public byte[] getEncryptedRandomSessionKey() {`
- `sources/org/apache/http/impl/auth/NTLMEngineImpl.java:1100`
  `return this.sessionKey;`
- `sources/org/apache/http/impl/auth/NTLMEngineImpl.java:1103`
  `public byte[] getExportedSessionKey() {`
- `sources/org/apache/http/impl/auth/NTLMEngineImpl.java:1104`
  `return this.exportedSessionKey;`
- `sources/org/apache/http/impl/auth/RFC2617Scheme.java:15`
  `import org.apache.http.auth.ChallengeState;`
- `sources/org/apache/http/impl/auth/RFC2617Scheme.java:16`
  `import org.apache.http.auth.MalformedChallengeException;`
- `sources/org/apache/http/impl/client/AbstractAuthenticationHandler.java:30`
  `protected Map<String, Header> parseChallenges(Header[] headerArr) throws MalformedChallengeException {`
- `sources/org/apache/http/impl/client/AbstractAuthenticationHandler.java:94`
  `this.log.debug("Challenge for " + str + " authentication scheme not available");`
- `sources/org/apache/http/impl/client/AbstractAuthenticationHandler.java:100`
  `throw new AuthenticationException("Unable to respond to any of these challenges: " + map);`
- `sources/org/apache/http/impl/client/AuthenticationStrategyAdaptor.java:59`
  `authSchemeSelectScheme.processChallenge(map.get(authSchemeSelectScheme.getSchemeName().toLowerCase(Locale.ROOT)));`
- `sources/org/apache/http/impl/client/AuthenticationStrategyImpl.java:39`
  `private final int challengeCode;`
- `sources/org/apache/http/impl/client/AuthenticationStrategyImpl.java:46`
  `this.challengeCode = i;`
- `sources/org/apache/http/impl/client/AuthenticationStrategyImpl.java:124`
  `authSchemeCreate.processChallenge(header);`
- `sources/org/apache/http/impl/client/AuthenticationStrategyImpl.java:131`
  `this.log.debug("Challenge for " + str + " authentication scheme not available");`
- `sources/org/apache/http/impl/client/DefaultRequestDirector.java:273`
  `if (this.proxyAuthState.getState().compareTo(AuthProtocolState.CHALLENGED) > 0 && this.proxyAuthState.getAuthScheme() != null && this.proxyAuthState.getAuthScheme().isConnectionBased()) {`
- `sources/org/apache/http/impl/client/DefaultRequestDirector.java:277`
  `if (this.targetAuthState.getState().compareTo(AuthProtocolState.CHALLENGED) > 0 && this.targetAuthState.getAuthScheme() != null && this.targetAuthState.getAuthScheme().isConnectionBased()) {`

## BR069

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/com/ble_health_plus/ble/connection/BaseBleActor$mGattCallback$1.java:157`
  `BluetoothDevice device = this.this$0.getDevice();`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor$mGattCallback$1.java:159`
  `bleConnectionListener.onCharacteristicRead(device.getAddress(), gatt, characteristic, value);`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor$mGattCallback$1.java:199`
  `BluetoothDevice device = baseBleActor2.getDevice();`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor$mGattCallback$1.java:201`
  `bleConnectionListener.onDescriptorWrite(baseBleActor2, device.getAddress());`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:40`
  `@Metadata(d1 = {"\u0000\u009e\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0005\...`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:46`
  `private BluetoothDevice device;`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:403`
  `BluetoothDevice bluetoothDevice = this.device;`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:404`
  `Intrinsics.checkNotNull(bluetoothDevice);`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:405`
  `bleConnectionListener.onDescriptorWrite(this, bluetoothDevice.getAddress());`
- `sources/com/ble_health_plus/ui/bloodpressure/BloodPressureActivity.java:103`
  `@Metadata(d1 = {"\u0000¶\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\t\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u00...`
- `sources/com/ble_health_plus/ui/glucose/GlucoMeterActivity.java:116`
  `@Metadata(d1 = {"\u0000Ö\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0002\n\u0002\u0010\u0011\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0010\b\n\u00...`
- `sources/com/ble_health_plus/ui/heartrate/HeartRateActivity.java:113`
  `@Metadata(d1 = {"\u0000Ê\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0002\n\u0002\u0010\u0011\n\u0002\u0010\u0000\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0002\b\u0006\n\u0002\u0018\u0002\n...`
- `sources/com/ble_health_plus/ui/weight/WeightScaleActivity.java:90`
  `@Metadata(d1 = {"\u0000Ê\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u000b\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u...`
- `sources/okio/HashingSink.java:83`
  `this.mac = mac;`
- `sources/okio/HashingSink.java:103`
  `Mac mac = this.mac;`
- `sources/okio/HashingSink.java:104`
  `Intrinsics.checkNotNull(mac);`
- `sources/okio/HashingSink.java:105`
  `mac.update(segment.data, segment.pos, iMin);`

## BR070

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/com/android/billingclient/api/BillingClientImpl.java:271`
  `com.google.android.gms.internal.play_billing.zzb.zzp("BillingClient", "Got exception trying to get purchase history, try to reconnect", e2);`
- `sources/com/android/billingclient/api/BillingClientImpl.java:840`
  `com.google.android.gms.internal.play_billing.zzb.zzp("BillingClient", "Exception caught while launching Price Change Flow for sku: " + sku + "; try to reconnect", e3);`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:40`
  `@Metadata(d1 = {"\u0000\u009e\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0005\...`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:43`
  `private int attemptReconnect;`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:180`
  `public final void setAttemptReconnect(int i) {`
- `sources/com/ble_health_plus/ble/connection/BaseBleActor.java:181`
  `this.attemptReconnect = i;`
- `sources/com/bumptech/glide/load/data/HttpUrlFetcher.java:142`
  `private HttpURLConnection buildAndConfigureConnection(URL url, Map<String, String> map) throws HttpException {`
- `sources/kotlinx/coroutines/flow/FlowKt__MigrationKt.java:375`
  `@Deprecated(level = DeprecationLevel.ERROR, message = "Flow analogue of 'replay(bufferSize)' is 'shareIn' with the specified replay parameter. \nreplay().connect() is the default strategy (no extra call is needed), \nreplay().autoConnect() translates to 'started = SharingStared.Lazily' argument, \nr...`
- `sources/okhttp3/EventListener.java:15`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000z\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002...`
- `sources/okhttp3/logging/LoggingEventListener.java:27`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000z\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\t\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u...`

## BR073

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:705`
  `public void restoreToolbarHierarchyState(SparseArray<Parcelable> sparseArray) {`
- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:707`
  `this.mDecorToolbar.restoreHierarchyState(sparseArray);`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:463`
  `java.lang.String r5 = r2.getAttributeValue(r6, r5)     // Catch: java.lang.Throwable -> L85 java.io.IOException -> L87 org.xmlpull.v1.XmlPullParserException -> La1`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:465`
  `java.lang.String r7 = r2.getAttributeValue(r6, r7)     // Catch: java.lang.Throwable -> L85 java.io.IOException -> L87 org.xmlpull.v1.XmlPullParserException -> La1`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:466`
  `long r7 = java.lang.Long.parseLong(r7)     // Catch: java.lang.Throwable -> L85 java.io.IOException -> L87 org.xmlpull.v1.XmlPullParserException -> La1`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:468`
  `java.lang.String r6 = r2.getAttributeValue(r6, r9)     // Catch: java.lang.Throwable -> L85 java.io.IOException -> L87 org.xmlpull.v1.XmlPullParserException -> La1`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:469`
  `float r6 = java.lang.Float.parseFloat(r6)     // Catch: java.lang.Throwable -> L85 java.io.IOException -> L87 org.xmlpull.v1.XmlPullParserException -> La1`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:470`
  `androidx.appcompat.widget.ActivityChooserModel$HistoricalRecord r9 = new androidx.appcompat.widget.ActivityChooserModel$HistoricalRecord     // Catch: java.lang.Throwable -> L85 java.io.IOException -> L87 org.xmlpull.v1.XmlPullParserException -> La1`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:471`
  `r9.<init>(r5, r7, r6)     // Catch: java.lang.Throwable -> L85 java.io.IOException -> L87 org.xmlpull.v1.XmlPullParserException -> La1`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:472`
  `r3.add(r9)     // Catch: java.lang.Throwable -> L85 java.io.IOException -> L87 org.xmlpull.v1.XmlPullParserException -> La1`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:207`
  `TextViewCompat.setCompoundDrawableTintMode(this.mView, DrawableUtils.parseTintMode(tintTypedArrayObtainStyledAttributes4.getInt(R.styleable.AppCompatTextView_drawableTintMode, -1), null));`
- `sources/androidx/collection/LongSparseArrayKt.java:17`
  `/* JADX INFO: compiled from: LongSparseArray.kt */`
- `sources/androidx/collection/LongSparseArrayKt.java:19`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000D\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\t\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002...`
- `sources/androidx/collection/LongSparseArrayKt.java:20`
  `public final class LongSparseArrayKt {`
- `sources/androidx/collection/LongSparseArrayKt.java:21`
  `public static final <T> int getSize(LongSparseArray<T> receiver$0) {`
- `sources/androidx/collection/LongSparseArrayKt.java:57`
  `public static final <T> boolean isNotEmpty(LongSparseArray<T> receiver$0) {`
- `sources/androidx/collection/LongSparseArrayKt.java:63`
  `public static final <T> boolean remove(LongSparseArray<T> receiver$0, long j, T t) {`
- `sources/androidx/collection/SparseArrayKt.java:17`
  `/* JADX INFO: compiled from: SparseArray.kt */`
- `sources/androidx/collection/SparseArrayKt.java:19`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000@\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0007...`
- `sources/androidx/collection/SparseArrayKt.java:20`
  `public final class SparseArrayKt {`
- `sources/androidx/collection/SparseArrayKt.java:21`
  `public static final <T> int getSize(SparseArrayCompat<T> receiver$0) {`
- `sources/androidx/collection/SparseArrayKt.java:57`
  `public static final <T> boolean isNotEmpty(SparseArrayCompat<T> receiver$0) {`
- `sources/androidx/collection/SparseArrayKt.java:63`
  `public static final <T> boolean remove(SparseArrayCompat<T> receiver$0, int i, T t) {`
- `sources/androidx/constraintlayout/motion/utils/ViewSpline.java:254`
  `SparseArray<ConstraintAttribute> mConstraintAttributeList;`
- `sources/androidx/constraintlayout/motion/utils/ViewSpline.java:257`
  `public CustomSet(String attribute, SparseArray<ConstraintAttribute> attrList) {`
- `sources/androidx/constraintlayout/motion/utils/ViewTimeCycle.java:290`
  `SparseArray<ConstraintAttribute> mConstraintAttributeList;`
- `sources/androidx/constraintlayout/motion/utils/ViewTimeCycle.java:292`
  `SparseArray<float[]> mWaveProperties = new SparseArray<>();`
- `sources/androidx/constraintlayout/motion/utils/ViewTimeCycle.java:294`
  `public CustomSet(String attribute, SparseArray<ConstraintAttribute> attrList) {`
- `sources/androidx/constraintlayout/motion/widget/DesignTool.java:81`
  `set.setVerticalBias(view.getId(), Float.parseFloat(str));`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:943`
  `sparseArray.put(childAt.getId(), this.mFrameArrayList.get(childAt));`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:996`
  `if (!sparseBooleanArray.get(childAt2.getId()) && motionController6 != null) {`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:1504`
  `sparseArray.clear();`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:1505`
  `sparseArray.put(0, base);`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:1506`
  `sparseArray.put(MotionLayout.this.getId(), base);`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:1513`
  `sparseArray.put(((View) constraintWidget.getCompanionWidget()).getId(), constraintWidget);`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:1521`
  `cSet.applyToHelper((ConstraintHelper) view, constraintWidget2, layoutParams, sparseArray);`
- `sources/androidx/constraintlayout/motion/widget/MotionScene.java:1047`
  `SparseArray<ConstraintSet> sparseArray = this.mConstraintSetMap;`
- `sources/androidx/constraintlayout/motion/widget/MotionScene.java:1048`
  `return sparseArray.get(sparseArray.keyAt(0));`
- `sources/androidx/constraintlayout/motion/widget/TouchResponse.java:15`
  `import org.xmlpull.v1.XmlPullParser;`
- `sources/androidx/constraintlayout/motion/widget/TouchResponse.java:76`
  `TouchResponse(Context context, MotionLayout layout, XmlPullParser parser) {`
- `sources/androidx/constraintlayout/motion/widget/TouchResponse.java:107`
  `fillFromAttributeList(context, Xml.asAttributeSet(parser));`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:37`
  `SparseArray<View> mChildrenByIds;`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:61`
  `private SparseArray<ConstraintWidget> mTempMapIdToWidget;`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:103`
  `this.mChildrenByIds = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:122`
  `this.mTempMapIdToWidget = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:131`
  `this.mChildrenByIds = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:150`
  `this.mTempMapIdToWidget = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:159`
  `this.mChildrenByIds = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:178`
  `this.mTempMapIdToWidget = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:187`
  `this.mChildrenByIds = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:206`
  `this.mTempMapIdToWidget = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:663`
  `public void applyConstraintsFromLayoutParams(boolean isInEditMode, View child, ConstraintWidget widget, LayoutParams layoutParams, SparseArray<ConstraintWidget> idToWidget) {`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:853`
  `private void setWidgetBaseline(ConstraintWidget widget, LayoutParams layoutParams, SparseArray<ConstraintWidget> idToWidget, int baselineTarget, ConstraintAnchor.Type type) {`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1208`
  `int i3 = Integer.parseInt(strArrSplit[0]);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1209`
  `int i4 = Integer.parseInt(strArrSplit[1]);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1210`
  `int i5 = Integer.parseInt(strArrSplit[2]);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1219`
  `float f4 = i7 + ((int) ((Integer.parseInt(strArrSplit[3]) / 1920.0f) * height));`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1580`
  `SparseIntArray sparseIntArray = new SparseIntArray();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1581`
  `map = sparseIntArray;`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1582`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintWidth, 64);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1583`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHeight, 65);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1584`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintLeft_toLeftOf, 8);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1585`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintLeft_toRightOf, 9);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1586`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintRight_toLeftOf, 10);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1587`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintRight_toRightOf, 11);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1588`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintTop_toTopOf, 12);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1589`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintTop_toBottomOf, 13);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1614`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_goneMarginEnd, 26);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1615`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_goneMarginBaseline, 55);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1616`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_marginBaseline, 54);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1617`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHorizontal_bias, 29);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1618`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintVertical_bias, 30);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1619`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintDimensionRatio, 44);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1620`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHorizontal_weight, 45);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1621`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintVertical_weight, 46);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1622`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHorizontal_chainStyle, 47);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1623`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintVertical_chainStyle, 48);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1624`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constrainedWidth, 27);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1625`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constrainedHeight, 28);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1626`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintWidth_default, 31);`

## BR074

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/android/support/v4/media/session/MediaControllerCompat.java:1531`
  `synchronized (mediaControllerImplApi21.mLock) {`
- `sources/android/support/v4/os/ResultReceiver.java:93`
  `synchronized (this) {`
- `sources/androidx/activity/ComponentActivity.java:67`
  `public class ComponentActivity extends androidx.core.app.ComponentActivity implements ContextAware, LifecycleOwner, ViewModelStoreOwner, HasDefaultViewModelProviderFactory, SavedStateRegistryOwner, OnBackPressedDispatcherOwner, ActivityResultRegistryOwner, ActivityResultCaller, OnConfigurationChange...`
- `sources/androidx/activity/ComponentActivity.java:126`
  `final ActivityResultContract.SynchronousResult<O> synchronousResult = activityResultContract.getSynchronousResult(componentActivity, i2);`
- `sources/androidx/activity/ComponentActivity.java:127`
  `if (synchronousResult != null) {`
- `sources/androidx/activity/ComponentActivity.java:131`
  `dispatchResult(i, synchronousResult.getValue());`
- `sources/androidx/activity/ComponentActivity.java:215`
  `savedStateRegistryControllerCreate.performAttach();`
- `sources/androidx/activity/ComponentActivity.java:216`
  `SavedStateHandleSupport.enableSavedStateHandles(this);`
- `sources/androidx/activity/ComponentActivity.java:220`
  `getSavedStateRegistry().registerSavedStateProvider(ACTIVITY_RESULT_TAG, new SavedStateRegistry.SavedStateProvider() { // from class: androidx.activity.ComponentActivity$$ExternalSyntheticLambda1`
- `sources/androidx/activity/ComponentActivity.java:221`
  `@Override // androidx.savedstate.SavedStateRegistry.SavedStateProvider`
- `sources/androidx/activity/ComponentActivity.java:222`
  `public final Bundle saveState() {`
- `sources/androidx/activity/ComponentActivity.java:237`
  `this.mActivityResultRegistry.onSaveInstanceState(bundle);`
- `sources/androidx/activity/ComponentActivity.java:243`
  `Bundle bundleConsumeRestoredStateForKey = getSavedStateRegistry().consumeRestoredStateForKey(ACTIVITY_RESULT_TAG);`
- `sources/androidx/activity/ComponentActivity.java:469`
  `public final SavedStateRegistry getSavedStateRegistry() {`
- `sources/androidx/activity/ComponentActivity.java:470`
  `return this.mSavedStateRegistryController.getSavedStateRegistry();`
- `sources/androidx/activity/result/ActivityResultRegistry.java:164`
  `public final void onSaveInstanceState(Bundle bundle) {`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:11`
  `@Metadata(d1 = {"\u0000.\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\b\u0004\b&\u0018\u0000*\u0004\b\u0000\u0010\u0001*\u0004\b\u0001\u0010\u00022\u...`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:15`
  `public SynchronousResult<O> getSynchronousResult(Context context, I input) {`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:23`
  `@Metadata(d1 = {"\u0000\u000e\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0000\n\u0002\b\u0006\u0018\u0000*\u0004\b\u0002\u0010\u00012\u00020\u0002B\r\u0012\u0006\u0010\u0003\u001a\u00028\u0002¢\u0006\u0002\u0010\u0004R\u0013\u0010\u0003\u001a\u00028\u0002¢\u0006\n\n\u0002\u0010\u0007\u001a\u0004\b\u...`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:24`
  `public static final class SynchronousResult<T> {`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:27`
  `public SynchronousResult(T t) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:81`
  `@Metadata(d1 = {"\u0000>\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0011\n\u0002\u0010\u000e\n\u0002\u0010$\n\u0002\u0010\u000b\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:116`
  `public ActivityResultContract.SynchronousResult<Map<String, Boolean>> getSynchronousResult(Context context, String[] input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:121`
  `return new ActivityResultContract.SynchronousResult<>(MapsKt.emptyMap());`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:144`
  `return new ActivityResultContract.SynchronousResult<>(linkedHashMap);`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:169`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\u0018\u00002\u000e\u0012\u0004\u0012\u00020\u00...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:209`
  `public ActivityResultContract.SynchronousResult<Boolean> getSynchronousResult(Context context, String input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:213`
  `return new ActivityResultContract.SynchronousResult<>(true);`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:220`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0016\u0018\u00002\u0012\u0012\u0006\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:223`
  `public final ActivityResultContract.SynchronousResult<Bitmap> getSynchronousResult(Context context, Void input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:248`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\b\u0016\u0018\u00002\u000e\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:251`
  `public final ActivityResultContract.SynchronousResult<Boolean> getSynchronousResult(Context context, Uri input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:274`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0017\u0018\u00002\u0010\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:278`
  `public final ActivityResultContract.SynchronousResult<Bitmap> getSynchronousResult(Context context, Uri input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:307`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\b\u0016\u0018\u00002\u000e\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:310`
  `public final ActivityResultContract.SynchronousResult<Boolean> getSynchronousResult(Context context, Uri input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:357`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0016\u0018\u00002\u0010\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:360`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(Context context, String input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:389`
  `@Metadata(d1 = {"\u0000:\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\b\u0017\u001...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:396`
  `public final ActivityResultContract.SynchronousResult<List<Uri>> getSynchronousResult(Context context, String input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:456`
  `@Metadata(d1 = {"\u00006\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0011\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\b\u0002\b\u0017\u0018\u00002\u0016\...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:459`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(Context context, String[] input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:488`
  `@Metadata(d1 = {"\u0000>\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0011\n\u0002\u0010\u000e\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:491`
  `public final ActivityResultContract.SynchronousResult<List<Uri>> getSynchronousResult(Context context, String[] input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:517`
  `@Metadata(d1 = {"\u0000.\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0017\u0018\u00002\u0012\u0012\u0006\u0012\u0004\u0018\u00010\u00...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:520`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(Context context, Uri input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:549`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0017\u0018\u00002\u0010\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:554`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(Context context, String input) {`
- `sources/androidx/appcompat/R.java:678`
  `public static final int submit_area = 0x7f0a0365;`
- `sources/androidx/appcompat/R.java:1546`
  `public static final int[] SearchView = {android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.inputType, android.R.attr.imeOptions, com.ble_health_plus.R.attr.closeIcon, com.ble_health_plus.R.attr.commitIcon, com.ble_health_plus.R.attr.defaultQueryHint, com.ble_health_plus.R.attr.goIcon,...`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2575`
  `return (Build.VERSION.SDK_INT < 21 || !Api21Impl.isPowerSaveMode(this.mPowerManager)) ? 1 : 2;`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2732`
  `static boolean isPowerSaveMode(PowerManager powerManager) {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2733`
  `return powerManager.isPowerSaveMode();`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:196`
  `canvas.save();`
- `sources/androidx/appcompat/view/menu/ActionMenuItemView.java:105`
  `this.mSavedPaddingLeft = i;`
- `sources/androidx/appcompat/widget/ActionMenuPresenter.java:481`
  `public Parcelable onSaveInstanceState() {`
- `sources/androidx/appcompat/widget/ActionMenuPresenter.java:482`
  `SavedState savedState = new SavedState();`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:154`
  `synchronized (this.mInstanceLock) {`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:170`
  `synchronized (this.mInstanceLock) {`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:187`
  `new PersistHistoryAsyncTask().executeOnExecutor(AsyncTask.THREAD_POOL_EXECUTOR, new ArrayList(this.mHistoricalRecords), this.mHistoryFileName);`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:192`
  `synchronized (this.mInstanceLock) {`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:204`
  `synchronized (this.mInstanceLock) {`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:226`
  `synchronized (this.mInstanceLock) {`
- `sources/androidx/appcompat/widget/AppCompatRatingBar.java:31`
  `protected synchronized void onMeasure(int i, int i2) {`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:138`
  `int iSave = canvas.save();`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:144`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:31`
  `private boolean mAsyncFontPending;`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:262`
  `AppCompatTextHelper.this.onAsyncTypefaceReceived(weakReference, typeface);`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:272`
  `this.mAsyncFontPending = this.mFontTypeface == null;`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:105`
  `ViewCompat.saveAttributeDataForStyleable(textView, textView.getContext(), R.styleable.AppCompatTextView, attributeSet, typedArrayObtainStyledAttributes, i, 0);`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:309`
  `synchronized (rectF) {`
- `sources/androidx/appcompat/widget/SearchView.java:91`
  `private final View mSubmitArea;`
- `sources/androidx/appcompat/widget/SearchView.java:92`
  `private boolean mSubmitButtonEnabled;`
- `sources/androidx/appcompat/widget/SwitchCompat.java:136`
  `ViewCompat.saveAttributeDataForStyleable(this, context, androidx.appcompat.R.styleable.SwitchCompat, attributeSet, tintTypedArrayObtainStyledAttributes.getWrappedTypeArray(), i, 0);`
- `sources/androidx/appcompat/widget/SwitchCompat.java:915`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:34`
  `int iSave = canvas.save();`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:46`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:192`
  `int iSave = canvas.save();`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:206`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:207`
  `int iSave3 = canvas.save();`

## BR075

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/androidx/appcompat/R.java:1205`
  `public static final int AppCompatTextView_autoSizePresetSizes = 0x00000003;`
- `sources/androidx/appcompat/R.java:1531`
  `public static final int[] AppCompatTextView = {android.R.attr.textAppearance, com.ble_health_plus.R.attr.autoSizeMaxTextSize, com.ble_health_plus.R.attr.autoSizeMinTextSize, com.ble_health_plus.R.attr.autoSizePresetSizes, com.ble_health_plus.R.attr.autoSizeStepGranularity, com.ble_health_plus.R.attr...`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:233`
  `resetGroup();`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:236`
  `public void resetGroup() {`
- `sources/androidx/appcompat/view/menu/MenuItemImpl.java:615`
  `actionProvider2.reset();`
- `sources/androidx/appcompat/widget/AppCompatButton.java:187`
  `public void setAutoSizeTextTypeUniformWithPresetSizes(int[] iArr, int i) throws IllegalArgumentException {`
- `sources/androidx/appcompat/widget/AppCompatButton.java:189`
  `super.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatButton.java:194`
  `appCompatTextHelper.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:185`
  `Api26Impl.setAutoSizeTextTypeUniformWithPresetSizes(this.mView, autoSizeTextAvailableSizes, 0);`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:216`
  `public void setAutoSizeTextTypeUniformWithPresetSizes(int[] iArr, int i) throws IllegalArgumentException {`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:218`
  `super.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:223`
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
- `sources/androidx/constraintlayout/core/ArrayRow.java:80`
  `public void reset() {`
- `sources/androidx/constraintlayout/core/LinearSystem.java:139`
  `public void reset() {`
- `sources/androidx/constraintlayout/core/LinearSystem.java:143`
  `solverVariable.reset();`
- `sources/androidx/constraintlayout/core/LinearSystem.java:183`
  `constraintAnchor.resetSolverVariable(this.mCache);`
- `sources/androidx/constraintlayout/core/LinearSystem.java:188`
  `solverVariable.reset();`
- `sources/androidx/constraintlayout/core/LinearSystem.java:217`
  `arrayRowAcquire.reset();`
- `sources/androidx/constraintlayout/core/LinearSystem.java:317`
  `solverVariableAcquire.reset();`
- `sources/androidx/constraintlayout/core/Metrics.java:55`
  `public void reset() {`
- `sources/androidx/constraintlayout/core/PriorityGoalRow.java:112`
  `public void reset() {`
- `sources/androidx/constraintlayout/core/PriorityGoalRow.java:203`
  `this.accessor.reset();`
- `sources/androidx/constraintlayout/core/SolverVariable.java:279`
  `public void reset() {`
- `sources/androidx/constraintlayout/core/widgets/ConstraintAnchor.java:124`
  `public void resetSolverVariable(Cache cache) {`
- `sources/androidx/constraintlayout/core/widgets/ConstraintAnchor.java:129`
  `solverVariable.reset();`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:840`
  `public void resetSolverVariables(Cache cache) {`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:841`
  `this.mLeft.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:842`
  `this.mTop.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:843`
  `this.mRight.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:844`
  `this.mBottom.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:845`
  `this.mBaseline.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:846`
  `this.mCenter.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:847`
  `this.mCenterX.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:848`
  `this.mCenterY.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/WidgetContainer.java:90`
  `public void resetSolverVariables(Cache cache) {`
- `sources/androidx/constraintlayout/core/widgets/WidgetContainer.java:91`
  `super.resetSolverVariables(cache);`
- `sources/androidx/constraintlayout/core/widgets/WidgetContainer.java:94`
  `this.mChildren.get(i).resetSolverVariables(cache);`
- `sources/androidx/constraintlayout/core/widgets/analyzer/BasicMeasure.java:251`
  `boolean zDirectMeasureSetup = constraintWidgetContainer.directMeasureSetup(zEnabled);`
- `sources/androidx/constraintlayout/core/widgets/analyzer/BasicMeasure.java:253`
  `zDirectMeasureSetup &= constraintWidgetContainer.directMeasureWithOrientation(zEnabled, 0);`
- `sources/androidx/constraintlayout/core/widgets/analyzer/BasicMeasure.java:259`
  `zDirectMeasureWithOrientation = constraintWidgetContainer.directMeasureWithOrientation(zEnabled, 1) & zDirectMeasureSetup;`
- `sources/androidx/constraintlayout/core/widgets/analyzer/BasicMeasure.java:262`
  `zDirectMeasureWithOrientation = zDirectMeasureSetup;`
- `sources/androidx/constraintlayout/core/widgets/analyzer/WidgetGroup.java:105`
  `linearSystem.reset();`
- `sources/androidx/constraintlayout/core/widgets/analyzer/WidgetGroup.java:128`
  `linearSystem.reset();`
- `sources/androidx/constraintlayout/core/widgets/analyzer/WidgetGroup.java:132`
  `linearSystem.reset();`
- `sources/androidx/constraintlayout/helper/widget/MotionEffect.java:129`
  `public void onPreSetup(androidx.constraintlayout.motion.widget.MotionLayout r22, java.util.HashMap<android.view.View, androidx.constraintlayout.motion.widget.MotionController> r23) {`
- `sources/androidx/constraintlayout/helper/widget/MotionEffect.java:134`
  `throw new UnsupportedOperationException("Method not decompiled: androidx.constraintlayout.helper.widget.MotionEffect.onPreSetup(androidx.constraintlayout.motion.widget.MotionLayout, java.util.HashMap):void");`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:2269`
  `this.mPath.reset();`
- `sources/androidx/constraintlayout/utils/widget/ImageFilterButton.java:256`
  `matrix.reset();`
- `sources/androidx/constraintlayout/utils/widget/ImageFilterView.java:298`
  `matrix.reset();`
- `sources/androidx/constraintlayout/widget/R.java:1717`
  `public static final int AppCompatTextView_autoSizePresetSizes = 0x00000003;`
- `sources/androidx/constraintlayout/widget/R.java:2905`
  `public static final int[] AppCompatTextView = {android.R.attr.textAppearance, com.ble_health_plus.R.attr.autoSizeMaxTextSize, com.ble_health_plus.R.attr.autoSizeMinTextSize, com.ble_health_plus.R.attr.autoSizePresetSizes, com.ble_health_plus.R.attr.autoSizeStepGranularity, com.ble_health_plus.R.attr...`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:324`
  `((LayoutParams) getChildAt(i2).getLayoutParams()).resetTouchBehaviorTracking();`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:327`
  `this.mDisallowInterceptReset = false;`
- `sources/androidx/core/app/NotificationCompat.java:2413`
  `private int mCustomSizePreset;`
- `sources/androidx/core/app/NotificationCompat.java:2427`
  `this.mCustomSizePreset = 0;`
- `sources/androidx/core/app/NotificationCompat.java:2437`
  `this.mCustomSizePreset = 0;`
- `sources/androidx/core/app/NotificationCompat.java:2465`
  `this.mCustomSizePreset = bundle.getInt(KEY_CUSTOM_SIZE_PRESET, 0);`
- `sources/androidx/core/app/NotificationCompat.java:2591`
  `wearableExtender.mCustomSizePreset = this.mCustomSizePreset;`
- `sources/androidx/core/app/NotificationCompat.java:2707`
  `public WearableExtender setCustomSizePreset(int i) {`
- `sources/androidx/core/app/NotificationCompat.java:2708`
  `this.mCustomSizePreset = i;`
- `sources/androidx/core/app/NotificationCompat.java:2713`
  `public int getCustomSizePreset() {`
- `sources/androidx/core/app/NotificationCompat.java:2714`
  `return this.mCustomSizePreset;`
- `sources/androidx/core/text/BidiFormatter.java:151`
  `if (getStereoReset() && z) {`
- `sources/androidx/core/widget/AutoScrollHelper.java:40`
  `boolean mNeedsReset;`
- `sources/androidx/core/widget/AutoScrollHelper.java:235`
  `this.mNeedsReset = true;`
- `sources/androidx/core/widget/AutoScrollHelper.java:245`
  `if (this.mNeedsReset) {`
- `sources/androidx/core/widget/AutoScrollHelper.java:316`
  `if (AutoScrollHelper.this.mNeedsReset) {`
- `sources/androidx/core/widget/AutoScrollHelper.java:317`
  `AutoScrollHelper.this.mNeedsReset = false;`
- `sources/androidx/core/widget/AutoSizeableTextView.java:21`
  `void setAutoSizeTextTypeUniformWithPresetSizes(int[] iArr, int i) throws IllegalArgumentException;`
- `sources/androidx/core/widget/TextViewCompat.java:223`
  `public static void setAutoSizeTextTypeUniformWithPresetSizes(TextView textView, int[] iArr, int i) throws IllegalArgumentException {`
- `sources/androidx/core/widget/TextViewCompat.java:225`
  `Api26Impl.setAutoSizeTextTypeUniformWithPresetSizes(textView, iArr, i);`
- `sources/androidx/core/widget/TextViewCompat.java:227`
  `((AutoSizeableTextView) textView).setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/databinding/library/baseAdapters/R.java:1271`
  `public static final int AppCompatTextView_autoSizePresetSizes = 0x00000003;`
- `sources/androidx/databinding/library/baseAdapters/R.java:1660`
  `public static final int[] AppCompatTextView = {android.R.attr.textAppearance, com.ble_health_plus.R.attr.autoSizeMaxTextSize, com.ble_health_plus.R.attr.autoSizeMinTextSize, com.ble_health_plus.R.attr.autoSizePresetSizes, com.ble_health_plus.R.attr.autoSizeStepGranularity, com.ble_health_plus.R.attr...`

## BR076

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `resources/com.ble_health_plus.apk/drive.v3.json:176`
  `"description": "Whether changes should include the file resource if the file is still accessible by the user at the time of the request, even when a file was removed from the list of changes and there will be no further change entries for this file.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:213`
  `"description": "The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response or to the response from the getStartPageToken method.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:278`
  `"description": "Whether changes should include the file resource if the file is still accessible by the user at the time of the request, even when a file was removed from the list of changes and there will be no further change entries for this file.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:315`
  `"description": "The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response or to the response from the getStartPageToken method.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:351`
  `"request": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:378`
  `"request": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:412`
  `"request": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:519`
  `"description": "The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:562`
  `"request": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:586`
  `"description": "An ID, such as a random UUID, which uniquely identifies this user's request for idempotent creation of a shared drive. A repeated request by the same user and with the same request ID will avoid creating duplicates by attempting to create the same shared drive. If the shared drive al...`
- `resources/com.ble_health_plus.apk/drive.v3.json:593`
  `"request": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:639`
  `"description": "Issue the request as a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the shared drive belongs.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:702`
  `"description": "Issue the request as a domain administrator; if set to true, then all shared drives of the domain in which the requester is an administrator are returned.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:755`
  `"description": "Issue the request as a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the shared drive belongs.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:761`
  `"request": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:797`
  `"description": "Whether to ignore the domain's default visibility settings for the created file. Domain administrators can choose to make all uploaded files visible to the domain by default; this parameter bypasses that behavior for the request. Permissions are still inherited from parent folders.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:808`
  `"description": "Whether to set the 'keepForever' field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:831`
  `"request": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:873`
  `"description": "Whether to ignore the domain's default visibility settings for the created file. Domain administrators can choose to make all uploaded files visible to the domain by default; this parameter bypasses that behavior for the request. Permissions are still inherited from parent folders.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:884`
  `"description": "Whether to set the 'keepForever' field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:913`
  `"request": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:1158`
  `"description": "The maximum number of files to return per page. Partial or empty result pages are possible even before the end of the files list has been reached.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:1166`
  `"description": "The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:1214`
  `"description": "Updates a file's metadata and/or content. When calling this method, only populate fields in the request that you want to modify. When updating fields, some fields might change automatically, such as modifiedDate. This method supports patch semantics.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:1261`
  `"description": "Whether to set the 'keepForever' field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:1295`
  `"request": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:1349`
  `"request": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:1400`
  `"description": "This parameter will only take effect if the item is not in a shared drive and the request is attempting to transfer the ownership of the item. If set to true, the item will be moved to the new owner's My Drive root folder and all prior parents removed. If set to false, parents are no...`
- `resources/com.ble_health_plus.apk/drive.v3.json:1429`
  `"description": "Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:1435`
  `"request": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:1481`
  `"description": "Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:1527`
  `"description": "Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:1573`
  `"description": "The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:1591`
  `"description": "Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:1656`
  `"description": "Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:1662`
  `"request": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:1700`
  `"request": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:1828`
  `"description": "The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:1873`
  `"request": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:1985`
  `"description": "The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:2027`
  `"request": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:2052`
  `"description": "An ID, such as a random UUID, which uniquely identifies this user's request for idempotent creation of a Team Drive. A repeated request by the same user and with the same request ID will avoid creating duplicates by attempting to create the same Team Drive. If the Team Drive already ...`
- `resources/com.ble_health_plus.apk/drive.v3.json:2059`
  `"request": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:2105`
  `"description": "Issue the request as a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the Team Drive belongs.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:2145`
  `"description": "Issue the request as a domain administrator; if set to true, then all Team Drives of the domain in which the requester is an administrator are returned.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:2175`
  `"description": "Issue the request as a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the Team Drive belongs.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:2181`
  `"request": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:2407`
  `"description": "The page token for the next page of changes. This will be absent if the end of the changes list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:2485`
  `"description": "The plain text content of the comment. This field is used for setting the content, while htmlContent should be displayed.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:2560`
  `"description": "The page token for the next page of comments. This will be absent if the end of the comments list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:2599`
  `"description": "An image file and cropping parameters from which a background image for this shared drive is set. This is a write only field; it can only be set on drive.drives.update requests that don't set themeId. When specified, all fields of the backgroundImageFile must be set.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:2706`
  `"description": "The color of this shared drive as an RGB hex string. It can only be set on a drive.drives.update request that does not set themeId.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:2739`
  `"description": "Whether the options to copy, print, or download files inside this shared drive, should be disabled for readers and commenters. When this restriction is set to true, it will override the similarly named field to true for any file inside this shared drive.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:2754`
  `"description": "The ID of the theme from which the background image and color will be set. The set of possible driveThemes can be retrieved from a drive.about.get response. When not specified on a drive.drives.create request, a random theme is chosen from which the background image and color are set...`
- `resources/com.ble_health_plus.apk/drive.v3.json:2777`
  `"description": "The page token for the next page of shared drives. This will be absent if the end of the list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:2791`
  `"description": "A collection of arbitrary key-value pairs which are private to the requesting app.\nEntries with null values are cleared in update and copy requests. These properties can only be retrieved using an authenticated request. An authenticated request uses an access token obtained with a O...`
- `resources/com.ble_health_plus.apk/drive.v3.json:2810`
  `"description": "Whether the current user can add a parent for the item without removing an existing parent in the same request. Not populated for shared drive files.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:2818`
  `"description": "Whether the current user can change the securityUpdateEnabled field on link share metadata.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:2870`
  `"description": "Whether the current user can move children of this folder within this drive. This is false when the item is not a folder. Note that a request to move the child may still fail depending on the current user's access to the child and to the destination folder.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:2882`
  `"description": "Whether the current user can move this item outside of this drive by changing its parent. Note that a request to change the parent of the item may still fail depending on the new parent that is being added.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:2890`
  `"description": "Whether the current user can move this item within this drive. Note that a request to change the parent of the item may still fail depending on the new parent that is being added and the parent that is being removed.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:2918`
  `"description": "Whether the current user can remove a parent from the item without adding another parent in the same request. Not populated for shared drive files.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:3011`
  `"description": "The color for a folder or shortcut to a folder as an RGB hex string. The supported colors are published in the folderColorPalette field of the About resource.\nIf an unsupported color is specified, the closest color in the palette will be used instead.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:3015`
  `"description": "The full file extension extracted from the name field. May contain multiple concatenated extensions, such as \"tar.gz\". This is only available for files with binary content in Google Drive.\nThis is automatically updated when the name field changes, however it is not cleared if the ...`
- `resources/com.ble_health_plus.apk/drive.v3.json:3019`
  `"description": "Whether there are permissions directly on this file. This field is only populated for items in shared drives.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:3023`
  `"description": "Whether this file has a thumbnail. This does not indicate whether the requesting app has access to the thumbnail. To check access, look for the presence of the thumbnailLink field.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:3209`
  `"description": "The original filename of the uploaded content if available, or else the original value of the name field. This is only available for files with binary content in Google Drive.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:3217`
  `"description": "The owner of this file. Only certain legacy files may have more than one owner. This field isn't populated for items in shared drives.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:3224`
  `"description": "The IDs of the parent folders which contain the file.\nIf not specified as part of a create request, the file will be placed directly in the user's My Drive folder. If not specified as part of a copy request, the file will inherit any discoverable parents of the source file. Update r...`
- `resources/com.ble_health_plus.apk/drive.v3.json:3274`
  `"description": "Shortcut file details. Only populated for shortcut files, which have the mimeType field set to application/vnd.google-apps.shortcut.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:3281`
  `"description": "The MIME type of the file that this shortcut points to. The value of this field is a snapshot of the target's MIME type, captured when the shortcut is created.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:3312`
  `"description": "A short-lived link to the file's thumbnail, if available. Typically lasts on the order of hours. Only populated when the requesting app can access the file's content. If the file isn't shared publicly, the URL returned in Files.thumbnailLink must be fetched using a credentialed reque...`
- `resources/com.ble_health_plus.apk/drive.v3.json:3408`
  `"description": "The page token for the next page of files. This will be absent if the end of the files list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:3446`
  `"description": "Whether the account associated with this permission has been deleted. This field only pertains to user and group permissions.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:3480`
  `"description": "Details of whether the permissions on this shared drive item are inherited or directly on this item. This is an output-only field which is present only for shared drive items.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:3484`
  `"description": "Whether this permission is inherited. This field is always populated. This is an output-only field.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:3488`
  `"description": "The ID of the item from which this permission is inherited. This is an output-only field.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:3570`
  `"description": "The page token for the next page of permissions. This field will be absent if the end of the permissions list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:3601`
  `"description": "The plain text content of the reply. This field is used for setting the content, while htmlContent should be displayed. This is required on creates if no action is specified.",`
- `resources/com.ble_health_plus.apk/drive.v3.json:3644`
  `"description": "The page token for the next page of replies. This will be absent if the end of the replies list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results.",`

## BR077

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `sources/com/google/api/client/googleapis/apache/GoogleApacheHttpTransport.java:26`
  `SSLContext tlsSslContext = SslUtils.getTlsSslContext();`
- `sources/com/google/api/client/googleapis/apache/GoogleApacheHttpTransport.java:28`
  `return new ApacheHttpTransport(HttpClientBuilder.create().useSystemProperties().setSSLSocketFactory(new SSLConnectionSocketFactory(tlsSslContext)).setDefaultSocketConfig(socketConfigBuild).setMaxConnTotal(200).setMaxConnPerRoute(20).setRoutePlanner(new SystemDefaultRoutePlanner(ProxySelector.getDefa...`
- `sources/com/google/api/client/http/apache/ApacheHttpTransport.java:158`
  `return setSocketFactory(new SSLSocketFactoryExtension(tlsSslContext));`
- `sources/com/google/api/client/http/apache/ApacheHttpTransport.java:162`
  `SSLSocketFactoryExtension sSLSocketFactoryExtension = new SSLSocketFactoryExtension(SslUtils.trustAllSSLContext());`
- `sources/com/google/api/client/http/apache/ApacheHttpTransport.java:163`
  `this.socketFactory = sSLSocketFactoryExtension;`
- `sources/com/google/api/client/http/apache/ApacheHttpTransport.java:164`
  `sSLSocketFactoryExtension.setHostnameVerifier(SSLSocketFactory.ALLOW_ALL_HOSTNAME_VERIFIER);`
- `sources/com/google/api/client/http/apache/ApacheHttpTransport.java:168`
  `public Builder setSocketFactory(SSLSocketFactory sSLSocketFactory) {`
- `sources/com/google/api/client/http/apache/ApacheHttpTransport.java:169`
  `this.socketFactory = (SSLSocketFactory) Preconditions.checkNotNull(sSLSocketFactory);`
- `sources/com/google/api/client/http/apache/v2/ApacheHttpTransport.java:51`
  `return HttpClientBuilder.create().useSystemProperties().setSSLSocketFactory(SSLConnectionSocketFactory.getSocketFactory()).setMaxConnTotal(200).setMaxConnPerRoute(20).setConnectionTimeToLive(-1L, TimeUnit.MILLISECONDS).setRoutePlanner(new SystemDefaultRoutePlanner(ProxySelector.getDefault())).disabl...`
- `sources/com/google/api/client/http/javanet/NetHttpTransport.java:83`
  `if (httpURLConnectionOpenConnection instanceof HttpsURLConnection) {`
- `sources/com/google/api/client/http/javanet/NetHttpTransport.java:84`
  `HttpsURLConnection httpsURLConnection = (HttpsURLConnection) httpURLConnectionOpenConnection;`
- `sources/com/google/api/client/http/javanet/NetHttpTransport.java:87`
  `httpsURLConnection.setHostnameVerifier(hostnameVerifier);`
- `sources/com/google/api/client/http/javanet/NetHttpTransport.java:89`
  `SSLSocketFactory sSLSocketFactory = this.sslSocketFactory;`
- `sources/com/google/api/client/http/javanet/NetHttpTransport.java:90`
  `if (sSLSocketFactory != null) {`
- `sources/com/google/api/client/http/javanet/NetHttpTransport.java:91`
  `httpsURLConnection.setSSLSocketFactory(sSLSocketFactory);`
- `sources/com/google/api/client/http/javanet/NetHttpTransport.java:128`
  `SSLContext tlsSslContext = SslUtils.getTlsSslContext();`
- `sources/com/google/api/client/http/javanet/NetHttpTransport.java:130`
  `return setSslSocketFactory(tlsSslContext.getSocketFactory());`
- `sources/com/google/api/client/http/javanet/NetHttpTransport.java:137`
  `SSLContext tlsSslContext = SslUtils.getTlsSslContext();`
- `sources/com/google/api/client/http/javanet/NetHttpTransport.java:139`
  `return setSslSocketFactory(tlsSslContext.getSocketFactory());`
- `sources/com/google/api/client/http/javanet/NetHttpTransport.java:144`
  `this.sslSocketFactory = SslUtils.trustAllSSLContext().getSocketFactory();`
- `sources/com/google/api/client/http/javanet/NetHttpTransport.java:148`
  `public SSLSocketFactory getSslSocketFactory() {`
- `sources/com/google/api/client/http/javanet/NetHttpTransport.java:149`
  `return this.sslSocketFactory;`
- `sources/com/google/api/client/http/javanet/NetHttpTransport.java:152`
  `public Builder setSslSocketFactory(SSLSocketFactory sSLSocketFactory) {`
- `sources/com/google/api/client/http/javanet/NetHttpTransport.java:153`
  `this.sslSocketFactory = sSLSocketFactory;`
- `sources/com/google/api/client/util/SslUtils.java:42`
  `public static SSLContext initSslContext(SSLContext sSLContext, KeyStore keyStore, TrustManagerFactory trustManagerFactory) throws GeneralSecurityException {`
- `sources/com/google/api/client/util/SslUtils.java:44`
  `sSLContext.init(null, trustManagerFactory.getTrustManagers(), null);`
- `sources/com/google/api/client/util/SslUtils.java:45`
  `return sSLContext;`
- `sources/com/google/api/client/util/SslUtils.java:48`
  `public static SSLContext initSslContext(SSLContext sSLContext, KeyStore keyStore, TrustManagerFactory trustManagerFactory, KeyStore keyStore2, String str, KeyManagerFactory keyManagerFactory) throws GeneralSecurityException {`
- `sources/com/google/api/client/util/SslUtils.java:51`
  `sSLContext.init(keyManagerFactory.getKeyManagers(), trustManagerFactory.getTrustManagers(), null);`
- `sources/com/google/api/client/util/SslUtils.java:52`
  `return sSLContext;`
- `sources/com/google/api/client/util/SslUtils.java:55`
  `public static SSLContext trustAllSSLContext() throws GeneralSecurityException {`
- `sources/com/google/api/client/util/SslUtils.java:70`
  `SSLContext tlsSslContext = getTlsSslContext();`
- `sources/okhttp3/OkHttpClient.java:534`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000ø\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b...`
- `sources/okhttp3/OkHttpClient.java:735`
  `/* JADX INFO: renamed from: getSslSocketFactoryOrNull$okhttp, reason: from getter */`
- `sources/okhttp3/OkHttpClient.java:736`
  `public final SSLSocketFactory getSslSocketFactoryOrNull() {`
- `sources/okhttp3/OkHttpClient.java:737`
  `return this.sslSocketFactoryOrNull;`
- `sources/okhttp3/OkHttpClient.java:740`
  `public final void setSslSocketFactoryOrNull$okhttp(SSLSocketFactory sSLSocketFactory) {`
- `sources/okhttp3/OkHttpClient.java:741`
  `this.sslSocketFactoryOrNull = sSLSocketFactory;`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:46`
  `return sSLContext;`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:55`
  `return sSLContext;`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:125`
  `public SSLSocketFactory newSslSocketFactory(X509TrustManager trustManager) throws NoSuchAlgorithmException, KeyManagementException {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:127`
  `SSLContext sSLContextNewSSLContext = newSSLContext();`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:129`
  `SSLSocketFactory socketFactory = sSLContextNewSSLContext.getSocketFactory();`
- `sources/okhttp3/internal/platform/OpenJSSEPlatform.java:44`
  `return sSLContext;`
- `sources/okhttp3/internal/platform/Platform.java:83`
  `Intrinsics.checkNotNullExpressionValue(sSLContext, "SSLContext.getInstance(\"TLS\")");`
- `sources/okhttp3/internal/platform/Platform.java:84`
  `return sSLContext;`
- `sources/okhttp3/internal/platform/Platform.java:175`
  `public SSLSocketFactory newSslSocketFactory(X509TrustManager trustManager) {`
- `sources/okhttp3/internal/platform/Platform.java:178`
  `SSLContext sSLContextNewSSLContext = newSSLContext();`
- `sources/okhttp3/internal/platform/Platform.java:180`
  `SSLSocketFactory socketFactory = sSLContextNewSSLContext.getSocketFactory();`
- `sources/org/apache/http/conn/ssl/SSLContextBuilder.java:122`
  `sSLContext.init(keyManagerArr, trustManagerArr, this.secureRandom);`
- `sources/org/apache/http/conn/ssl/SSLContextBuilder.java:123`
  `return sSLContext;`
- `sources/org/apache/http/conn/ssl/SSLContexts.java:10`
  `public static SSLContext createDefault() throws SSLInitializationException {`
- `sources/org/apache/http/conn/ssl/SSLContexts.java:12`
  `SSLContext sSLContext = SSLContext.getInstance("TLS");`
- `sources/org/apache/http/conn/ssl/SSLContexts.java:13`
  `sSLContext.init(null, null, null);`
- `sources/org/apache/http/conn/ssl/SSLContexts.java:14`
  `return sSLContext;`
- `sources/org/apache/http/impl/client/HttpClientBuilder.java:187`
  `public final HttpClientBuilder setSSLContext(SSLContext sSLContext) {`
- `sources/org/apache/http/impl/client/HttpClientBuilder.java:188`
  `this.sslContext = sSLContext;`
- `sources/org/apache/http/impl/client/HttpClientBuilder.java:192`
  `public final HttpClientBuilder setSSLSocketFactory(LayeredConnectionSocketFactory layeredConnectionSocketFactory) {`
- `sources/org/apache/http/impl/client/HttpClientBuilder.java:193`
  `this.sslSocketFactory = layeredConnectionSocketFactory;`
- `sources/org/apache/http/ssl/SSLContextBuilder.java:222`
  `protected void initSSLContext(SSLContext sSLContext, Collection<KeyManager> collection, Collection<TrustManager> collection2, SecureRandom secureRandom) throws KeyManagementException {`
- `sources/org/apache/http/ssl/SSLContextBuilder.java:223`
  `sSLContext.init(!collection.isEmpty() ? (KeyManager[]) collection.toArray(new KeyManager[collection.size()]) : null, collection2.isEmpty() ? null : (TrustManager[]) collection2.toArray(new TrustManager[collection2.size()]), secureRandom);`
- `sources/org/apache/http/ssl/SSLContextBuilder.java:226`
  `public SSLContext build() throws NoSuchAlgorithmException, KeyManagementException {`
- `sources/org/apache/http/ssl/SSLContextBuilder.java:227`
  `SSLContext sSLContext;`
- `sources/org/apache/http/ssl/SSLContexts.java:9`
  `public static SSLContext createDefault() throws SSLInitializationException {`
- `sources/org/apache/http/ssl/SSLContexts.java:11`
  `SSLContext sSLContext = SSLContext.getInstance("TLS");`
- `sources/org/apache/http/ssl/SSLContexts.java:12`
  `sSLContext.init(null, null, null);`
- `sources/org/apache/http/ssl/SSLContexts.java:13`
  `return sSLContext;`

## BR078

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/com/google/api/client/http/javanet/NetHttpTransport.java:143`
  `this.hostnameVerifier = SslUtils.trustAllHostnameVerifier();`
- `sources/com/google/api/client/util/SslUtils.java:8`
  `import javax.net.ssl.HostnameVerifier;`
- `sources/com/google/api/client/util/SslUtils.java:75`
  `public static HostnameVerifier trustAllHostnameVerifier() {`
- `sources/com/google/api/client/util/SslUtils.java:76`
  `return new HostnameVerifier() { // from class: com.google.api.client.util.SslUtils.2`
- `sources/com/google/api/client/util/SslUtils.java:77`
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
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000î\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u001a\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u00...`
- `sources/okhttp3/OkHttpClient.java:47`
  `public class OkHttpClient implements Cloneable, Call.Factory, WebSocket.Factory {`
- `sources/okhttp3/OkHttpClient.java:358`
  `@Override // okhttp3.Call.Factory`
- `sources/okhttp3/OkHttpClient.java:533`
  `/* JADX INFO: compiled from: OkHttpClient.kt */`
- `sources/okhttp3/OkHttpClient.java:534`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000ø\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b...`
- `sources/okhttp3/OkHttpClient.java:878`
  `this.dns = okHttpClient.dns();`
- `sources/okhttp3/OkHttpClient.java:879`
  `this.proxy = okHttpClient.proxy();`
- `sources/okhttp3/OkHttpClient.java:880`
  `this.proxySelector = okHttpClient.proxySelector();`
- `sources/okhttp3/OkHttpClient.java:881`
  `this.proxyAuthenticator = okHttpClient.proxyAuthenticator();`
- `sources/okhttp3/OkHttpClient.java:882`
  `this.socketFactory = okHttpClient.socketFactory();`
- `sources/okhttp3/OkHttpClient.java:883`
  `this.sslSocketFactoryOrNull = okHttpClient.sslSocketFactoryOrNull;`
- `sources/okhttp3/OkHttpClient.java:884`
  `this.x509TrustManagerOrNull = okHttpClient.getX509TrustManager();`
- `sources/okhttp3/OkHttpClient.java:885`
  `this.connectionSpecs = okHttpClient.connectionSpecs();`
- `sources/okhttp3/OkHttpClient.java:886`
  `this.protocols = okHttpClient.protocols();`
- `sources/okhttp3/OkHttpClient.java:887`
  `this.hostnameVerifier = okHttpClient.hostnameVerifier();`
- `sources/okhttp3/OkHttpClient.java:888`
  `this.certificatePinner = okHttpClient.certificatePinner();`
- `sources/okhttp3/OkHttpClient.java:889`
  `this.certificateChainCleaner = okHttpClient.getCertificateChainCleaner();`
- `sources/okhttp3/OkHttpClient.java:890`
  `this.callTimeout = okHttpClient.callTimeoutMillis();`
- `sources/okhttp3/internal/connection/RealConnection.java:444`
  `OkHostnameVerifier okHostnameVerifier = OkHostnameVerifier.INSTANCE;`
- `sources/okhttp3/internal/connection/RealConnection.java:448`
  `if (okHostnameVerifier.verify(strHost, (X509Certificate) certificate)) {`
- `sources/okhttp3/internal/connection/RealConnection.java:632`
  `if (this.http2Connection == null || routes == null || !routeMatchesAny(routes) || address.hostnameVerifier() != OkHostnameVerifier.INSTANCE || !supportsUrl(address.url())) {`
- `sources/okhttp3/internal/http2/PushObserver.java:40`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u00008\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\b\u0002\...`
- `sources/okhttp3/internal/http2/PushObserver.java:42`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:48`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:54`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:59`
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
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000J\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\...`
- `sources/okhttp3/internal/platform/Android10Platform.java:46`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Android10Platform.java:68`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Android10Platform.java:119`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Android10Platform.java:127`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000\u001a\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\b\u0086\u0003\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002J\b\u0010\u0006\u001a\u0004\u0018\u00010\u0007R\u0011\u...`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:23`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:24`
  `import okhttp3.internal.platform.android.AndroidCertificateChainCleaner;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:31`
  `import okhttp3.internal.platform.android.StandardAndroidSocketAdapter;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:32`
  `import okhttp3.internal.tls.CertificateChainCleaner;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:33`
  `import okhttp3.internal.tls.TrustRootIndex;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:37`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000x\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\...`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:72`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:94`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:168`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:175`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:189`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u00008\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u000e\n\u0000\b\u...`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:249`
  `@Override // okhttp3.internal.tls.TrustRootIndex`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:19`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:26`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000J\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\...`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:49`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:71`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:77`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:21`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:23`
  `import org.conscrypt.ConscryptHostnameVerifier;`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:27`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000H\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\...`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:35`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:58`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:78`
  `Conscrypt.setHostnameVerifier(x509TrustManager, DisabledHostnameVerifier.INSTANCE);`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:83`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\u0011\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\bÀ\u0002\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\...`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:84`
  `public static final class DisabledHostnameVerifier implements ConscryptHostnameVerifier {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:85`
  `public static final DisabledHostnameVerifier INSTANCE = new DisabledHostnameVerifier();`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:95`
  `private DisabledHostnameVerifier() {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:124`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:1`
  `package okhttp3.internal.platform;`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:12`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:16`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000<\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\...`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:58`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:65`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000\u001a\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\b\u0086\u0003\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002J\b\u0010\u0006\u001a\u0004\u0018\u00010\u0007R\u0011\u...`
- `sources/okhttp3/internal/platform/OpenJSSEPlatform.java:18`
  `import okhttp3.Protocol;`

## BR079

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/com/ble_health_plus/ui/menu/WebViewActivity.java:105`
  `activityWebViewBinding.webView.getSettings().setJavaScriptEnabled(true);`
- `sources/com/ble_health_plus/ui/menu/WebViewActivity.java:106`
  `activityWebViewBinding.webView.getSettings().setAllowFileAccess(true);`
- `sources/com/ble_health_plus/ui/report/ShareReportFragment.java:527`
  `fragmentShareReprotBinding.webView.getSettings().setJavaScriptEnabled(true);`
- `sources/com/ble_health_plus/ui/report/ShareReportFragment.java:529`
  `fragmentShareReprotBinding.webView.getSettings().setAllowFileAccess(true);`

## BR080

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/android/support/v4/media/MediaBrowserCompat.java:681`
  `Log.d(MediaBrowserCompat.TAG, "addSubscription failed with RemoteException parentId=" + str);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:799`
  `Log.d(MediaBrowserCompat.TAG, "ServiceCallbacks.onConnect...");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:814`
  `Log.d(MediaBrowserCompat.TAG, "addSubscription failed with RemoteException.");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:912`
  `Log.d(MediaBrowserCompat.TAG, "  mServiceConnection=" + this.mServiceConnection);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:913`
  `Log.d(MediaBrowserCompat.TAG, "  mServiceBinderWrapper=" + this.mServiceBinderWrapper);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:914`
  `Log.d(MediaBrowserCompat.TAG, "  mCallbacksMessenger=" + this.mCallbacksMessenger);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:915`
  `Log.d(MediaBrowserCompat.TAG, "  mRootId=" + this.mRootId);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:916`
  `Log.d(MediaBrowserCompat.TAG, "  mMediaSessionToken=" + this.mMediaSessionToken);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2017`
  `Log.d("AppCompatDelegate", "Exception while getting ActivityInfo", e);`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:1697`
  `Log.v(MotionLayout.TAG, str + " done. ");`
- `sources/androidx/constraintlayout/widget/ConstraintLayoutStates.java:94`
  `Log.v("ConstraintLayoutStates", "NO Constraint set found ! id=" + id + ", dim =" + width + ", " + height);`
- `sources/androidx/core/view/ViewCompat.java:651`
  `Log.d(TAG, "Error calling dispatchStartTemporaryDetach", e);`
- `sources/androidx/core/view/ViewCompat.java:672`
  `Log.d(TAG, "Error calling dispatchFinishTemporaryDetach", e);`
- `sources/androidx/exifinterface/media/ExifInterface.java:2513`
  `Log.d(TAG, "getRafAttributes starting with: " + byteOrderedDataInputStream);`
- `sources/androidx/exifinterface/media/ExifInterface.java:2817`
  `Log.d(TAG, "getWebpAttributes starting with: " + byteOrderedDataInputStream);`
- `sources/androidx/exifinterface/media/ExifInterface.java:3075`
  `Log.d(TAG, "readExifSegment: Byte Align MM");`
- `sources/androidx/exifinterface/media/ExifInterface.java:3237`
  `Log.d(TAG, "Failed to skip " + i8 + " bytes.");`
- `sources/androidx/exifinterface/media/ExifInterface.java:3243`
  `Log.d(TAG, "Failed to read " + i7 + " bytes.");`
- `sources/androidx/fragment/app/FragmentLayoutInflaterFactory.java:70`
  `Log.v("FragmentManager", "Fragment " + fragmentFindFragmentById + " has been inflated via the <fragment> tag: id=0x" + Integer.toHexString(resourceId));`
- `sources/androidx/fragment/app/FragmentLayoutInflaterFactory.java:82`
  `Log.v("FragmentManager", "Retained Fragment " + fragmentFindFragmentById + " has been re-attached via the <fragment> tag: id=0x" + Integer.toHexString(resourceId));`
- `sources/androidx/fragment/app/FragmentManager.java:1633`
  `Log.v(TAG, "Discarding retained Fragment " + fragment2 + " that was not found in the set of active Fragments " + fragmentManagerState.mActive);`
- `sources/androidx/fragment/app/FragmentStateManager.java:462`
  `Log.d("FragmentManager", "moveto ACTIVITY_CREATED: " + this.mFragment);`
- `sources/androidx/fragment/app/FragmentStore.java:124`
  `Log.v("FragmentManager", "Removed fragment from active set " + fragment);`
- `sources/androidx/fragment/app/SpecialEffectsController.java:197`
  `Log.v(FragmentManager.TAG, "SpecialEffectsController: Finished executing pending operations");`
- `sources/androidx/localbroadcastmanager/content/LocalBroadcastManager.java:153`
  `Log.v(TAG, "Resolving type " + strResolveTypeIfNeeded + " scheme " + scheme + " of intent " + intent);`
- `sources/androidx/localbroadcastmanager/content/LocalBroadcastManager.java:158`
  `Log.v(TAG, "Action list: " + arrayList3);`
- `sources/androidx/localbroadcastmanager/content/LocalBroadcastManager.java:185`
  `Log.v(TAG, "  Filter matched!  match=0x" + Integer.toHexString(iMatch));`
- `sources/com/ble_health_plus/ui/custom/CircleAlarmTimerView.java:354`
  `Log.d(TAG, "onMeasure");`
- `sources/com/bumptech/glide/Glide.java:228`
  `Log.d(TAG, "Discovered GlideModule from manifest: " + it2.next().getClass());`
- `sources/com/bumptech/glide/load/data/HttpUrlFetcher.java:137`
  `Log.d(TAG, "Failed to get a response code", e);`
- `sources/com/bumptech/glide/load/engine/Engine.java:113`
  `Log.v(TAG, str + " in " + LogTime.getElapsedMillis(j) + "ms, key: " + key);`
- `sources/com/bumptech/glide/load/engine/bitmap_recycle/LruArrayPool.java:94`
  `Log.v(adapterFromType.getTag(), "Allocated " + key.size + " bytes");`
- `sources/com/bumptech/glide/load/engine/bitmap_recycle/LruArrayPool.java:146`
  `Log.v(adapterFromObject.getTag(), "evicted: " + adapterFromObject.getArrayLength(objRemoveLast));`
- `sources/com/bumptech/glide/load/engine/prefill/BitmapPreFillRunner.java:71`
  `Log.d(TAG, "allocated [" + preFillTypeRemove.getWidth() + "x" + preFillTypeRemove.getHeight() + "] " + preFillTypeRemove.getConfig() + " size: " + bitmapByteSize);`
- `sources/com/bumptech/glide/load/resource/ImageDecoderResourceDecoder.java:67`
  `Log.v(ImageDecoderResourceDecoder.TAG, "Resizing from [" + size.getWidth() + "x" + size.getHeight() + "] to [" + iRound + "x" + iRound2 + "] scaleFactor: " + scaleFactor);`
- `sources/com/bumptech/glide/load/resource/bitmap/BitmapImageDecoderResourceDecoder.java:21`
  `Log.v(TAG, "Decoded [" + bitmapDecodeBitmap.getWidth() + "x" + bitmapDecodeBitmap.getHeight() + "] for [" + i + "x" + i2 + "]");`
- `sources/com/bumptech/glide/load/resource/bitmap/DefaultImageHeaderParser.java:151`
  `Log.d(TAG, "Missing jpeg exif preamble");`
- `sources/com/bumptech/glide/load/resource/bitmap/DefaultImageHeaderParser.java:217`
  `Log.d(TAG, "Unknown endianness = " + ((int) int16));`
- `sources/com/bumptech/glide/load/resource/bitmap/DefaultImageHeaderParser.java:231`
  `Log.d(TAG, "Got invalid format code = " + ((int) int164));`
- `sources/com/bumptech/glide/load/resource/bitmap/DefaultImageHeaderParser.java:237`
  `Log.d(TAG, "Negative tiff component count");`

## BR081

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/com/google/api/client/testing/json/webtoken/TestCertificates.java:51`
  `KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());`
- `sources/com/google/api/client/util/SecurityUtils.java:30`
  `return KeyStore.getInstance(KeyStore.getDefaultType());`
- `sources/com/google/api/client/util/SecurityUtils.java:34`
  `return KeyStore.getInstance("JKS");`
- `sources/com/google/api/client/util/SecurityUtils.java:38`
  `return KeyStore.getInstance("PKCS12");`
- `sources/com/google/api/client/util/SecurityUtils.java:132`
  `KeyStore keyStore = KeyStore.getInstance("JKS");`
- `sources/org/apache/http/ssl/SSLContextBuilder.java:122`
  `KeyStore keyStore = KeyStore.getInstance(this.keyStoreType);`
- `sources/org/apache/http/ssl/SSLContextBuilder.java:144`
  `KeyStore keyStore = KeyStore.getInstance(this.keyStoreType);`
- `sources/org/apache/http/ssl/SSLContextBuilder.java:188`
  `KeyStore keyStore = KeyStore.getInstance(this.keyStoreType);`
- `sources/org/apache/http/ssl/SSLContextBuilder.java:206`
  `KeyStore keyStore = KeyStore.getInstance(this.keyStoreType);`

## BR082

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/androidx/core/content/FileProvider.java:248`
  `@Override // androidx.core.content.FileProvider.PathStrategy`
- `sources/androidx/core/content/FileProvider.java:275`
  `@Override // androidx.core.content.FileProvider.PathStrategy`
- `sources/com/ble_health_plus/common/Utils.java:6`
  `import androidx.core.content.FileProvider;`
- `sources/com/ble_health_plus/common/Utils.java:267`
  `Uri uriForFile = FileProvider.getUriForFile(context, "com.ble_health_plus.provider", fileCreateTempFile);`
- `sources/com/ble_health_plus/ui/custom/PdfView.java:11`
  `import androidx.core.content.FileProvider;`
- `sources/com/ble_health_plus/ui/custom/PdfView.java:88`
  `intent.setDataAndType(FileProvider.getUriForFile(activity, "com.package.name.fileprovider", file), "application/pdf");`
- `sources/com/ble_health_plus/ui/report/ShareReportFragment.java:18`
  `import androidx.core.content.FileProvider;`
- `sources/com/ble_health_plus/ui/report/ShareReportFragment.java:616`
  `intent.putExtra("android.intent.extra.STREAM", FileProvider.getUriForFile(requireActivity(), requireActivity().getPackageName() + ".provider", new File(filePath)));`
- `sources/com/webviewtopdf/PdfView.java:12`
  `import androidx.core.content.FileProvider;`
- `sources/com/webviewtopdf/PdfView.java:76`
  `intent.setDataAndType(FileProvider.getUriForFile(activity, "com.package.name.fileprovider", file), "application/pdf");`

## BR086

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/androidx/appcompat/R.java:63`
  `public static final int actionModeShareDrawable = 0x7f04002a;`
- `sources/androidx/appcompat/R.java:517`
  `public static final int abc_ab_share_pack_mtrl_alpha = 0x7f080007;`
- `sources/androidx/appcompat/R.java:525`
  `public static final int abc_btn_default_mtrl_shape = 0x7f08000f;`
- `sources/androidx/appcompat/R.java:1249`
  `public static final int AppCompatTheme_actionModeShareDrawable = 0x0000001b;`
- `sources/androidx/appcompat/R.java:1361`
  `public static final int DrawerArrowToggle_arrowShaftLength = 0x00000001;`
- `sources/androidx/appcompat/R.java:1532`
  `public static final int[] AppCompatTheme = {android.R.attr.windowIsFloating, android.R.attr.windowAnimationStyle, com.ble_health_plus.R.attr.actionBarDivider, com.ble_health_plus.R.attr.actionBarItemBackground, com.ble_health_plus.R.attr.actionBarPopupTheme, com.ble_health_plus.R.attr.actionBarSize,...`
- `sources/androidx/appcompat/R.java:1536`
  `public static final int[] DrawerArrowToggle = {com.ble_health_plus.R.attr.arrowHeadLength, com.ble_health_plus.R.attr.arrowShaftLength, com.ble_health_plus.R.attr.barLength, com.ble_health_plus.R.attr.color, com.ble_health_plus.R.attr.drawableSize, com.ble_health_plus.R.attr.gapBetweenBars, com.ble_...`
- `sources/androidx/appcompat/R.java:1549`
  `public static final int[] TextAppearance = {android.R.attr.textSize, android.R.attr.typeface, android.R.attr.textStyle, android.R.attr.textColor, android.R.attr.textColorHint, android.R.attr.textColorLink, android.R.attr.shadowColor, android.R.attr.shadowDx, android.R.attr.shadowDy, android.R.attr.s...`
- `sources/androidx/appcompat/app/AppCompatDelegate.java:78`
  `public abstract boolean isHandleNativeActionModesEnabled();`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1055`
  `public boolean isHandleNativeActionModesEnabled() {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2432`
  `if (AppCompatDelegateImpl.this.isHandleNativeActionModesEnabled()) {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2449`
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
- `sources/androidx/appcompat/widget/DropDownListView.java:522`
  `private static boolean sHasMethods;`
- `sources/androidx/appcompat/widget/DropDownListView.java:538`
  `sHasMethods = true;`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:54`
  `activityChooserView.setActivityChooserModel(ActivityChooserModel.get(this.mContext, this.mShareHistoryFileName));`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:57`
  `this.mContext.getTheme().resolveAttribute(R.attr.actionModeShareDrawable, typedValue, true);`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:60`
  `activityChooserView.setDefaultActionButtonContentDescription(R.string.abc_shareactionprovider_share_with_application);`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:61`
  `activityChooserView.setExpandActivityOverflowButtonContentDescription(R.string.abc_shareactionprovider_share_with);`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:68`
  `ActivityChooserModel activityChooserModel = ActivityChooserModel.get(this.mContext, this.mShareHistoryFileName);`
- `sources/androidx/cardview/widget/CardView.java:60`
  `this.mShadowBounds = new Rect();`
- `sources/androidx/cardview/widget/CardViewApi17Impl.java:6`
  `import androidx.cardview.widget.RoundRectDrawableWithShadow;`
- `sources/androidx/cardview/widget/CardViewApi17Impl.java:15`
  `RoundRectDrawableWithShadow.sRoundRectHelper = new RoundRectDrawableWithShadow.RoundRectHelper() { // from class: androidx.cardview.widget.CardViewApi17Impl.1`
- `sources/androidx/cardview/widget/CardViewApi17Impl.java:16`
  `@Override // androidx.cardview.widget.RoundRectDrawableWithShadow.RoundRectHelper`
- `sources/androidx/cardview/widget/CardViewApi21Impl.java:69`
  `cardViewDelegate.setShadowPadding(0, 0, 0, 0);`
- `sources/androidx/cardview/widget/CardViewApi21Impl.java:74`
  `int iCeil = (int) Math.ceil(RoundRectDrawableWithShadow.calculateHorizontalPadding(maxElevation, radius, cardViewDelegate.getPreventCornerOverlap()));`
- `sources/androidx/cardview/widget/CardViewApi21Impl.java:75`
  `int iCeil2 = (int) Math.ceil(RoundRectDrawableWithShadow.calculateVerticalPadding(maxElevation, radius, cardViewDelegate.getPreventCornerOverlap()));`
- `sources/androidx/cardview/widget/CardViewApi21Impl.java:76`
  `cardViewDelegate.setShadowPadding(iCeil, iCeil2, iCeil, iCeil2);`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:9`
  `import androidx.cardview.widget.RoundRectDrawableWithShadow;`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:24`
  `RoundRectDrawableWithShadow.sRoundRectHelper = new RoundRectDrawableWithShadow.RoundRectHelper() { // from class: androidx.cardview.widget.CardViewBaseImpl.1`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:25`
  `@Override // androidx.cardview.widget.RoundRectDrawableWithShadow.RoundRectHelper`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:57`
  `RoundRectDrawableWithShadow roundRectDrawableWithShadowCreateBackground = createBackground(context, colorStateList, f, f2, f3);`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:58`
  `roundRectDrawableWithShadowCreateBackground.setAddPaddingForCorners(cardViewDelegate.getPreventCornerOverlap());`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:59`
  `cardViewDelegate.setCardBackground(roundRectDrawableWithShadowCreateBackground);`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:63`
  `private RoundRectDrawableWithShadow createBackground(Context context, ColorStateList colorStateList, float f, float f2, float f3) {`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:64`
  `return new RoundRectDrawableWithShadow(context.getResources(), colorStateList, f, f2, f3);`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:70`
  `getShadowBackground(cardViewDelegate).getMaxShadowAndCornerPadding(rect);`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:72`
  `cardViewDelegate.setShadowPadding(rect.left, rect.top, rect.right, rect.bottom);`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:125`
  `return getShadowBackground(cardViewDelegate).getMinWidth();`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:130`
  `return getShadowBackground(cardViewDelegate).getMinHeight();`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:133`
  `private RoundRectDrawableWithShadow getShadowBackground(CardViewDelegate cardViewDelegate) {`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:134`
  `return (RoundRectDrawableWithShadow) cardViewDelegate.getCardBackground();`
- `sources/androidx/cardview/widget/CardViewDelegate.java:20`
  `void setShadowPadding(int i, int i2, int i3, int i4);`
- `sources/androidx/cardview/widget/RoundRectDrawable.java:88`
  `this.mBoundsI.inset((int) Math.ceil(RoundRectDrawableWithShadow.calculateHorizontalPadding(this.mPadding, this.mRadius, this.mInsetForRadius)), (int) Math.ceil(RoundRectDrawableWithShadow.calculateVerticalPadding(this.mPadding, this.mRadius, this.mInsetForRadius)));`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:13`
  `import android.graphics.Shader;`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:18`
  `class RoundRectDrawableWithShadow extends Drawable {`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:20`
  `private static final float SHADOW_MULTIPLIER = 1.5f;`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:25`
  `private Paint mCornerShadowPaint;`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:26`
  `private Path mCornerShadowPath;`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:27`
  `private Paint mEdgeShadowPaint;`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:28`
  `private final int mInsetShadow;`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:29`
  `private float mRawMaxShadowSize;`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:33`
  `private final int mShadowStartColor;`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:36`
  `private boolean mPrintedShadowClipWarning = false;`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:48`
  `RoundRectDrawableWithShadow(Resources resources, ColorStateList colorStateList, float f, float f2, float f3) {`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:49`
  `this.mShadowStartColor = resources.getColor(R.color.cardview_shadow_start_color);`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:50`
  `this.mShadowEndColor = resources.getColor(R.color.cardview_shadow_end_color);`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:51`
  `this.mInsetShadow = resources.getDimensionPixelSize(R.dimen.cardview_compat_inset_shadow);`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:54`
  `this.mCornerShadowPaint = paint;`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:58`
  `Paint paint2 = new Paint(this.mCornerShadowPaint);`

## BR088

paper_id: B004
paper_title: Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation

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
- `sources/kotlinx/coroutines/flow/FlowKt__CollectionKt.java:123`
  `static final class AnonymousClass2<T> implements FlowCollector, SuspendFunction {`

## BR090

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `audit_reports_integrated/00_审计总览与结论_zh.md:7`
  `本报告只使用 'rule_catalog.tsv' 中的规则，结论只写 'confirmed'、'supported_hypothesis'、'not_supported'、'not_testable'。没有把单个权限、单个 URL、单个 SDK 或单个字符串当作 confirmed。当前工程目录没有 'pcap/pcapng/har/log/db/sqlite' 运行样本；因此抓包、logcat、运行时文件系统、真实 BLE 外设、隐私政策对照相关规则均按证据强度降级。`
- `audit_reports_integrated/00_审计总览与结论_zh.md:15`
  `3. 'BleScanService' 是导出服务，外部启动后会调用 'startScan()'，并通过普通 'sendBroadcast' 发出 BLE MAC、'BluetoothDevice'、设备类型。这更像组件 hardening 与本地广播泄露问题，映射到 R017/R019/R020/R076，但没有运行时 PoC，不能 confirmed。`
- `audit_reports_integrated/00_审计总览与结论_zh.md:18`
  `## Confirmed Findings`
- `audit_reports_integrated/00_审计总览与结论_zh.md:25`
  `- 结论：'confirmed'`
- `audit_reports_integrated/00_审计总览与结论_zh.md:36`
  `- 结论：R033 'confirmed'，R034 'confirmed'`
- `audit_reports_integrated/00_审计总览与结论_zh.md:51`
  `证据链：Room DB 同时保存 profile、健康读数和 BLE 设备标识；'BackUpFragment' 对完整 DB 文件调用 'AESCipher.encrypt(...)'；'AESCipher' 使用硬编码 key 和默认 'AES'；Drive 上传加密后的 'ble_health_backup.bkup'。P014 的评估方法覆盖本地存储和信息传输，P015 强调健康数据敏感性和保护措施不匹配。没有真实备份文件和运行时缓存目录，所以不写 confirmed。`
- `audit_reports_integrated/00_审计总览与结论_zh.md:68`
  `证据链：Manifest 中 'BleScanService' exported=true 且无权限；'onStartCommand' 不验证调用者并直接 'startScan()'；扫描结果通过普通广播发出 MAC、BluetoothDevice、deviceType。P005 讨论导出组件被外部利用导致信息泄露或完整性破坏。缺第三方 App/adb PoC，所以不写 confirmed。`
- `audit_reports_integrated/00_审计总览与结论_zh.md:84`
  `证据链：'ApiController.getHttpClient()' 创建 'HttpLoggingInterceptor' 并设置 'Level.BODY'；Retrofit 使用该 client；'BuildConfig.DEBUG=false'；API 包括登录、注册、OTP、profile、订阅和上传。没有 logcat，因此不 confirmed。`
- `audit_reports_integrated/01_完整证据链_zh.md:19`
  `本链路支持 R006 confirmed。由于没有真实 BLE 外设，不能确认空中 payload 明文，也不能确认设备端没有额外保护；因此 R073/R074/R077/R078/R080/R081/R084 均保持 supported_hypothesis。`
- `audit_reports_integrated/01_完整证据链_zh.md:36`
  `判断：同一 App 私有数据库/偏好中组合了身份、健康数据和设备标识。没有运行时文件系统样本，因此 R054/R060 不写 confirmed。`
- `audit_reports_integrated/01_完整证据链_zh.md:85`
  `Java 到 JS：页面完成后执行 'evaluateJavascript("javascript:loadData('" + new Gson().toJson(reportModel) + "')", null)'。这是 R033/R034 confirmed 的关键路径。`
- `audit_reports_integrated/01_完整证据链_zh.md:121`
  `'ApiController.getHttpClient()' 创建 'HttpLoggingInterceptor' 并设置 'Level.BODY'，再加入 OkHttp client。该 client 被 Retrofit 使用。由于这是 release build 且接口包含凭据/profile/token 类数据，R050 有强静态可达证据；但无 logcat，所以不 confirmed。`
- `audit_reports_integrated/01_完整证据链_zh.md:184`
  `解释：'usesCleartextTraffic=true' 是弱面，但不是 R023 confirmed。必须看到敏感 HTTP 代码路径或抓包。当前一方 API 使用 HTTPS。`
- `audit_reports_integrated/01_完整证据链_zh.md:214`
  `Manifest line 87-94：'HealthPlusMessagingService' exported=true，action 为 'com.google.firebase.MESSAGING_EVENT'。Firebase 官方服务通常可设为非导出或由 SDK 处理；这里没有进一步证明可被外部滥用，因此未单独作为 confirmed。`
- `audit_reports_integrated/01_完整证据链_zh.md:271`
  `影响：代码中大量 'AppLog.INSTANCE.e(...)' 包含 token、profile、BLE 数据、健康对象的字符串拼接，但当前 release 反编译结果显示不会真正写日志。报告中没有把这些作为 confirmed。`
- `audit_reports_integrated/01_完整证据链_zh.md:408`
  `判断：R033/R034 confirmed；R030/R035 supported_hypothesis。无证据证明外部 CDN 脚本实际 exfiltrate。`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:42`
  `- R006 'confirmed'：健康输入捕获和持久化有完整链路。`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:60`
  `补充：FileProvider 的 '<external-path path="."/>' 是独立 hardening 问题，但不是 P003 confirmed，因为 provider 不导出。`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:111`
  `判定：R021-R024 均 'not_supported'。R023 特别说明：cleartext flag 是修复建议，但不足以 confirmed。`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:154`
  `- R033 'confirmed'：标识/身份数据进入 WebView JS。`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:155`
  `- R034 'confirmed'：健康敏感值进入 WebView JS。`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:259`
  `为什么不是 confirmed：没有真实 BLE 外设、无同址恶意 App PoC、无法证明设备端没有额外应用层协议。`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:280`
  `本轮没有把以下证据单独作为 confirmed：`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:295`
  `本表覆盖 rule_catalog.tsv 全部 96 条规则。结论只使用 confirmed、supported_hypothesis、not_supported、not_testable。`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:304`
  `| R006 | P002 | SUPOR: Precise and Scalable Sensitive User Input Detection for Android Apps | Medical or health input capture | confirmed | Room 表和 BLE 解析链路明确保存血糖、心率、血压、体重等健康数据。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:331`
  `| R033 | P009 | Cross-Boundary Mobile Tracking: Exploring Java-to-JavaScript Information Diffusion in WebViews | Java objects injected into WebView with identifiers | confirmed | ReportModel 中 name/email/profileUrl/age/gender 被 Gson JSON 注入 WebView JS。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:332`
  `| R034 | P009 | Cross-Boundary Mobile Tracking: Exploring Java-to-JavaScript Information Diffusion in WebViews | Sensitive values passed from Java to JavaScript | confirmed | 健康读数数组、设备类型、用户设置、身份字段进入 loadData(...)。 |`
- `audit_reports_integrated/02_规则映射与论文依据_zh.md:346`
  `| R048 | P012 | What’s Done Is Not What’s Claimed: Detecting and Interpreting Inconsistencies in App Behaviors | Multi-layer inconsistency requiring combined evidence | supported_hypothesis | WebView 注入+远程脚本、备份+弱静态 key、BLE service+广播均需跨层复测。 |`
- `audit_reports_integrated/03_独立安全分析_zh.md:3`
  `本文件回应“先分析出你觉得存在但是不是论文中提到的漏洞”。这里不新增 rule_id，不把独立观察混成数据库 confirmed；能映射的部分已在主报告和逐规则映射中给出。`
- `audit_reports_integrated/03_独立安全分析_zh.md:15`
  `'file_provider_path.xml' 包含 '<cache-path path="."/>' 和 '<external-path path="."/>'。Provider 本身 'exported=false'，所以不构成 R009/R010 confirmed。但 '<external-path path="."/>' 范围过宽，未来新增分享功能时容易把不应分享的外部文件纳入授权范围。当前备份/恢复也使用 externalCacheDir，虽然未见直接分享备份文件，仍建议将报告 PDF、头像裁剪、备份中间文件分目录隔离，并删除全局 external-path。`
- `audit_reports_integrated/03_独立安全分析_zh.md:31`
  `这不是“第三方已外传”的 confirmed，因为没有抓包或 DOM hook。独立风险在于供应链：健康报告数据进入了一个包含远程脚本的 JS 上下文。`
- `audit_reports_integrated/04_复测与PoC计划_zh.md:3`
  `本文件把 supported_hypothesis 转换成可执行验证任务。目标是把证据不足的假设尽量推进到 confirmed 或 not_supported。以下步骤默认在授权测试设备、测试账号、测试 BLE 外设环境下执行。`
- `audit_reports_integrated/04_复测与PoC计划_zh.md:42`
  `升级为 confirmed 的条件：外部启动成功，且第三方 receiver 能收到 MAC/设备类型/设备对象。若只能启动但收不到广播，则 R017/R019 可能仍成立但 R076 降级。若 Android 系统阻止外部启动且测试 App 无法触发，则保留 not_supported 或 not_testable，视错误原因而定。`
- `audit_reports_integrated/04_复测与PoC计划_zh.md:83`
  `- 如果 logcat 出现请求/响应 JSON、email、password、OTP、token、profile、multipart 元数据，则 R050 可升级 confirmed。`
- `audit_reports_integrated/04_复测与PoC计划_zh.md:117`
  `- 如果解密后能打开 SQLite，并读取身份/健康/设备数据，则 R051/R054/R057/R059/R060 中至少部分可升级 confirmed。`
- `audit_reports_integrated/04_复测与PoC计划_zh.md:154`
  `- 如果第三方脚本上下文可读取 'AuditSentinelName' 或健康值，但没有外传，R035 仍可能是 supported_hypothesis，R034 保持 confirmed。`
- `audit_reports_integrated/04_复测与PoC计划_zh.md:155`
  `- 如果第三方请求携带哨兵数据，则 R035/R036 可升级 confirmed。`
- `audit_reports_integrated/04_复测与PoC计划_zh.md:196`
  `- 如果 raw bytes 可直接对应健康语义值，且无签名/MAC/加密，R073/R074 可升级 confirmed。`
- `audit_reports_integrated/04_复测与PoC计划_zh.md:197`
  `- 如果同址 App 能读取或触发相同 characteristic，R081 可升级 confirmed。`
- `audit_reports_integrated/04_复测与PoC计划_zh.md:198`
  `- 如果目标 App 接受伪造或误绑定设备数据并入库，R082/R084 可升级 confirmed。`
- `audit_reports_integrated/04_复测与PoC计划_zh.md:229`
  `- 外部可触发 DB 修改或通知行为：R017/R018/R019 可升级 confirmed。`
- `audit_reports_integrated/04_复测与PoC计划_zh.md:281`
  `只有政策与实际行为都具备时，才能把相关规则从 not_testable 改为 confirmed/not_supported。`
- `audit_reports_integrated/04_复测与PoC计划_zh.md:287`
  `| R050 supported_hypothesis | logcat 中出现敏感 BODY | confirmed |`
- `audit_reports_integrated/04_复测与PoC计划_zh.md:288`
  `| R051/R054/R059 supported_hypothesis | 备份文件离线解密出 DB | confirmed |`
- `audit_reports_integrated/04_复测与PoC计划_zh.md:289`
  `| R030/R035 supported_hypothesis | 第三方脚本读取或发送报告数据 | confirmed |`
- `audit_reports_integrated/04_复测与PoC计划_zh.md:290`
  `| R017/R019/R020 supported_hypothesis | 外部 App 启动 BLE service 并触发扫描/广播 | confirmed |`
- `audit_reports_integrated/04_复测与PoC计划_zh.md:291`
  `| R073/R074 supported_hypothesis | BLE raw payload 明文且无应用层认证 | confirmed |`
- `audit_reports_integrated/04_复测与PoC计划_zh.md:292`
  `| R081/R082/R084 supported_hypothesis | 同址 App 读/注入/误绑定并被目标 App 信任 | confirmed |`
- `audit_reports_integrated/04_复测与PoC计划_zh.md:293`
  `| 政策类 not_testable | 政策文本 + 抓包 + 同意路径 | confirmed 或 not_supported |`
- `audit_reports_integrated/README.md:8`
  `- App 摘要、证据边界、confirmed / supported_hypothesis / not_supported / not_testable 结论总览。`
- `audit_reports_integrated/README.md:22`
  `- 运行时验证和 PoC 操作计划，用于把 supported_hypothesis 推进到 confirmed 或 not_supported。`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:192`
  `// Confirmed by registry <iana-questions@icann.org> 2008-06-18`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:209`
  `// Confirmed by registry <it@nic.at> 2008-06-17`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:312`
  `// Confirmed by registry <tech@dns.be> 2008-06-08`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:735`
  `// Confirmed by .CL registry <hsalgado@nic.cl>`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:845`
  `// Confirmed by registry <registry@una.net> 2013-03-26`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:878`
  `// Confirmed by registry <ops@denic.de> (with technical`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:886`
  `// Confirmed by registry <robert@dk-hostmaster.dk> 2008-06-17`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:1080`
  `// Confirmed by registry <nigel@channelisles.net> 2013-11-28`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:1256`
  `// Confirmed by registry <pasztor@iszt.hu> 2008-06-12`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:1355`
  `// Confirmed by registry <iana-questions@icann.org> 2008-06-18`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:1390`
  `// Confirmed by registry <marius@isgate.is> 2008-12-06`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:1813`
  `// Confirmed by registry <nigel@channelisles.net> 2013-11-28`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:3745`
  `// Confirmed by registry <nic.tech@citra.gov.kw>`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:3756`
  `// Confirmed by registry <kysupport@perimeterusa.com> 2008-06-17`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:3836`
  `// Confirmed by registry <lsadmin@nic.ls>`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:3970`
  `// Confirmed by registry <dcamacho@saipan.com> 2008-06-17`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:7102`
  `// Confirmed by registry <bmtengwa@potraz.gov.zw> 2017-01-25`

## BR091

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/com/ble_health_plus/network/ApiService.java:42`
  `@POST("addchilduser")`
- `sources/com/ble_health_plus/network/ApiService.java:45`
  `@POST("changepassword")`
- `sources/com/ble_health_plus/network/ApiService.java:48`
  `@POST("feedback")`
- `sources/com/ble_health_plus/network/ApiService.java:51`
  `@POST("notificationlist")`
- `sources/com/ble_health_plus/network/ApiService.java:54`
  `@POST("getofferplanlist")`
- `sources/com/ble_health_plus/network/ApiService.java:57`
  `@POST("getprofile")`
- `sources/com/ble_health_plus/network/ApiService.java:60`
  `@POST("inquiry")`
- `sources/com/ble_health_plus/network/ApiService.java:63`
  `@POST(FirebaseAnalytics.Event.LOGIN)`
- `sources/com/ble_health_plus/network/ApiService.java:66`
  `@POST("userregister")`
- `sources/com/ble_health_plus/network/ApiService.java:69`
  `@POST("removechilduser")`
- `sources/com/ble_health_plus/network/ApiService.java:72`
  `@POST("updateBackupTime")`
- `sources/com/ble_health_plus/network/ApiService.java:75`
  `@POST("savesubscription")`
- `sources/com/ble_health_plus/network/ApiService.java:78`
  `@POST("sendOTP")`
- `sources/com/ble_health_plus/network/ApiService.java:81`
  `@POST("editprofile")`
- `sources/com/ble_health_plus/network/ApiService.java:84`
  `@POST("updatesubscription")`
- `sources/com/ble_health_plus/network/ApiService.java:87`
  `@POST("uploadImage")`
- `sources/com/ble_health_plus/network/ApiService.java:88`
  `@Multipart`

## BR092

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/androidx/appcompat/R.java:1546`
  `public static final int[] SearchView = {android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.inputType, android.R.attr.imeOptions, com.ble_health_plus.R.attr.closeIcon, com.ble_health_plus.R.attr.commitIcon, com.ble_health_plus.R.attr.defaultQueryHint, com.ble_health_plus.R.attr.goIcon,...`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2575`
  `return (Build.VERSION.SDK_INT < 21 || !Api21Impl.isPowerSaveMode(this.mPowerManager)) ? 1 : 2;`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2732`
  `static boolean isPowerSaveMode(PowerManager powerManager) {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2733`
  `return powerManager.isPowerSaveMode();`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:196`
  `canvas.save();`
- `sources/androidx/appcompat/view/menu/ActionMenuItemView.java:105`
  `this.mSavedPaddingLeft = i;`
- `sources/androidx/appcompat/widget/ActionMenuPresenter.java:481`
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
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:262`
  `AppCompatTextHelper.this.onAsyncTypefaceReceived(weakReference, typeface);`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:272`
  `this.mAsyncFontPending = this.mFontTypeface == null;`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:105`
  `ViewCompat.saveAttributeDataForStyleable(textView, textView.getContext(), R.styleable.AppCompatTextView, attributeSet, typedArrayObtainStyledAttributes, i, 0);`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:309`
  `synchronized (rectF) {`
- `sources/androidx/appcompat/widget/SearchView.java:91`
  `private final View mSubmitArea;`
- `sources/androidx/appcompat/widget/SearchView.java:92`
  `private boolean mSubmitButtonEnabled;`
- `sources/androidx/appcompat/widget/SwitchCompat.java:915`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:34`
  `int iSave = canvas.save();`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:192`
  `int iSave = canvas.save();`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:207`
  `int iSave3 = canvas.save();`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:214`
  `canvas.restoreToCount(iSave3);`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:215`
  `int iSave4 = canvas.save();`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:222`
  `canvas.restoreToCount(iSave4);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:1228`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:39:0x0085 -> B:40:0x0086). Please report as a decompilation issue!!! */`
- `sources/androidx/constraintlayout/core/widgets/Flow.java:998`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:105:0x010d -> B:42:0x0059). Please report as a decompilation issue!!! */`
- `sources/androidx/constraintlayout/core/widgets/Flow.java:999`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:106:0x010f -> B:42:0x0059). Please report as a decompilation issue!!! */`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:2042`
  `canvas.save();`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:131`
  `sRectPool = new Pools.SynchronizedPool(12);`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:821`
  `int iSave = canvas.save();`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:826`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/core/content/ContextCompat.java:79`
  `private static final Object sSync = new Object();`
- `sources/androidx/core/content/ContextCompat.java:144`
  `synchronized (sLock) {`
- `sources/androidx/core/content/pm/ShortcutManagerCompat.java:191`
  `public static void reportShortcutUsed(Context context, String str) {`
- `sources/androidx/core/content/res/FontResourcesParserCompat.java:23`
  `public static final int FETCH_STRATEGY_ASYNC = 1;`
- `sources/androidx/core/content/res/ResourcesCompat.java:30`
  `synchronized (sColorStateCacheLock) {`
- `sources/androidx/core/location/LocationManagerCompat.java:121`
  `synchronized (sLocationListeners) {`
- `sources/androidx/core/location/LocationManagerCompat.java:148`
  `synchronized (weakHashMap) {`
- `sources/androidx/core/location/LocationManagerCompat.java:238`
  `synchronized (GnssLazyLoader.sGnssStatusListeners) {`

## BR093

paper_id: B004
paper_title: Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation

- `sources/androidx/core/os/ProcessCompat.java:76`
  `synchronized (sResolvedLock) {`
- `sources/com/ble_health_plus/billing/model/SaveSubReq.java:8`
  `/* JADX INFO: compiled from: SaveSubReq.kt */`
- `sources/com/ble_health_plus/billing/model/SaveSubReq.java:10`
  `@Metadata(d1 = {"\u0000$\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u001c\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0086\b\u0018\u00002\u00020\u0001B\u0007\b\u0016¢\u0006\u0002\u0010\u0002B5\u0012\u0006\u0010\u0003\u001a\u00020\...`
- `sources/com/ble_health_plus/billing/model/SaveSubReq.java:11`
  `public final /* data */ class SaveSubReq {`
- `sources/com/ble_health_plus/billing/model/SaveSubReq.java:31`
  `public static /* synthetic */ SaveSubReq copy$default(SaveSubReq saveSubReq, String str, String str2, String str3, String str4, String str5, String str6, int i, Object obj) {`
- `sources/com/ble_health_plus/billing/model/SaveSubReq.java:33`
  `str = saveSubReq.expireDate;`
- `sources/com/ble_health_plus/billing/model/SaveSubReq.java:48`
  `str5 = saveSubReq.token;`
- `sources/com/ble_health_plus/billing/model/SaveSubReq.java:52`
  `str6 = saveSubReq.userId;`
- `sources/com/ble_health_plus/billing/model/SaveSubReq.java:54`
  `return saveSubReq.copy(str, str7, str8, str9, str10, str6);`
- `sources/com/ble_health_plus/billing/model/SaveSubReq.java:87`
  `public final SaveSubReq copy(String expireDate, String orderId, String purchaseDate, String purchaseId, String token, String userId) {`
- `sources/com/ble_health_plus/billing/model/SaveSubReq.java:94`
  `return new SaveSubReq(expireDate, orderId, purchaseDate, purchaseId, token, userId);`
- `sources/com/ble_health_plus/billing/model/SaveSubReq.java:101`
  `if (!(other instanceof SaveSubReq)) {`
- `sources/com/ble_health_plus/billing/model/SaveSubReq.java:104`
  `SaveSubReq saveSubReq = (SaveSubReq) other;`
- `sources/com/ble_health_plus/billing/model/SaveSubReq.java:105`
  `return Intrinsics.areEqual(this.expireDate, saveSubReq.expireDate) && Intrinsics.areEqual(this.orderId, saveSubReq.orderId) && Intrinsics.areEqual(this.purchaseDate, saveSubReq.purchaseDate) && Intrinsics.areEqual(this.purchaseId, saveSubReq.purchaseId) && Intrinsics.areEqual(this.token, saveSubReq....`
- `sources/com/ble_health_plus/billing/model/SaveSubReq.java:113`
  `return "SaveSubReq(expireDate=" + this.expireDate + ", orderId=" + this.orderId + ", purchaseDate=" + this.purchaseDate + ", purchaseId=" + this.purchaseId + ", token=" + this.token + ", userId=" + this.userId + ')';`
- `sources/com/ble_health_plus/billing/model/SaveSubReq.java:116`
  `public SaveSubReq(String expireDate, String orderId, String purchaseDate, String purchaseId, String token, String userId) {`
- `sources/com/ble_health_plus/billing/model/SaveSubReq.java:185`
  `public SaveSubReq() {`
- `sources/com/ble_health_plus/ble/connection/BleConnectionService.java:204`
  `public final synchronized void start(Context context) {`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:66`
  `_db.execSQL("CREATE TABLE IF NOT EXISTS 'BloodPressureTBL' ('systolicValue' INTEGER, 'diastolicValue' INTEGER, 'heartRateValue' INTEGER, 'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'data' TEXT, 'user_id' TEXT, 'device_mac' TEXT, 'epoch' INTEGER, 'date_time' TEXT, 'device_id' INTEGER, 'dataType'...`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:69`
  `_db.execSQL("CREATE TABLE IF NOT EXISTS 'WeightScaleTBL' ('weightValue' REAL, 'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'data' TEXT, 'user_id' TEXT, 'device_mac' TEXT, 'epoch' INTEGER, 'date_time' TEXT, 'device_id' INTEGER, 'dataType' TEXT, 'sync' INTEGER, 'deviceType' TEXT)");`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:71`
  `_db.execSQL("CREATE TABLE IF NOT EXISTS 'ReminderTbl' ('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'title' TEXT, 'userId' TEXT, 'description' TEXT, 'alarmTime' TEXT, 'days' TEXT NOT NULL, 'isRepeat' INTEGER NOT NULL, 'sync' INTEGER)");`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:72`
  `_db.execSQL("CREATE TABLE IF NOT EXISTS 'ProfileTBL' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'birthdate' TEXT, 'email' TEXT, 'gender' TEXT, 'height' TEXT, 'name' TEXT, 'profile' TEXT, 'profile_url' TEXT, 'user_id' TEXT, 'weight' TEXT, 'unit' TEXT, 'is_primary' INTEGER NOT NULL, 'isSubscrib...`
- `sources/com/ble_health_plus/database/AppDatabase_Impl.java:241`
  `map6.put("sync", new TableInfo.Column("sync", "INTEGER", false, 0, null, 1));`
- `sources/com/ble_health_plus/database/BaseTableClass.java:12`
  `@Metadata(d1 = {"\u0000,\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u000e\n\u0002\u0010\b\n\u0002\b\t\n\u0002\u0010\t\n\u0002\b\u000b\n\u0002\u0010\u000b\n\u0002\b\n\b\u0016\u0018\u00002\u00020\u0001B\u0005¢\u0006\u0002\u0010\u0002J\b\u00102\u001a\u00020\u0...`
- `sources/com/ble_health_plus/database/BaseTableClass.java:25`
  `@SerializedName("sync")`
- `sources/com/ble_health_plus/database/BaseTableClass.java:26`
  `private Boolean sync;`
- `sources/com/ble_health_plus/database/device/DevicesTBL.java:10`
  `@Metadata(d1 = {"\u0000,\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u001e\n\u0002\u0010\t\n\u0002\b\u000e\n\u0002\u0010\u000b\n\u0002\b\n\b\u0007\u0018\u00002\u00020\u0001B\u0005¢\u0006\u0002\u0010\u0002J\b\u0010A\u001a\u0002...`
- `sources/com/ble_health_plus/database/device/DevicesTBL.java:22`
  `private Boolean sync;`
- `sources/com/ble_health_plus/database/profile/ProfileTBL.java:14`
  `@Metadata(d1 = {"\u0000\"\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u000e\n\u0002\b\n\n\u0002\u0010\u000b\n\u0002\bG\b\u0087\b\u0018\u00002\u00020\u0001B\u0007\b\u0016¢\u0006\u0002\u0010\u0002B¯\u0001\u0012\b\b\u0002\u0010\u0003\u001a\u00020\u0004\...`
- `sources/com/ble_health_plus/database/profile/ProfileTBL.java:42`
  `@SerializedName("sync")`
- `sources/com/ble_health_plus/database/profile/ProfileTBL.java:43`
  `private Boolean sync;`
- `sources/com/ble_health_plus/database/profile/ProfileTBL.java:135`
  `public final ProfileTBL copy(int id, String birthdate, String email, String gender, String height, String name, String profile, String profileUrl, String userId, String weight, String unit, boolean primary, boolean isSubscribed, String subscriptionToken, Boolean sync, Boolean isLoginFirstTime, Strin...`
- `sources/com/ble_health_plus/database/profile/ProfileTBL.java:136`
  `return new ProfileTBL(id, birthdate, email, gender, height, name, profile, profileUrl, userId, weight, unit, primary, isSubscribed, subscriptionToken, sync, isLoginFirstTime, lastBackupDate);`
- `sources/com/ble_health_plus/database/profile/ProfileTBL.java:147`
  `return this.id == profileTBL.id && Intrinsics.areEqual(this.birthdate, profileTBL.birthdate) && Intrinsics.areEqual(this.email, profileTBL.email) && Intrinsics.areEqual(this.gender, profileTBL.gender) && Intrinsics.areEqual(this.height, profileTBL.height) && Intrinsics.areEqual(this.name, profileTBL...`
- `sources/com/ble_health_plus/database/reminder/AddReminderDao_Impl.java:39`
  `return "INSERT OR REPLACE INTO 'ReminderTbl' ('id','title','userId','description','alarmTime','days','isRepeat','sync') VALUES (?,?,?,?,?,?,?,?)";`
- `sources/com/ble_health_plus/database/reminder/AddReminderDao_Impl.java:118`
  `return "INSERT OR ABORT INTO 'ReminderTbl' ('id','title','userId','description','alarmTime','days','isRepeat','sync') VALUES (?,?,?,?,?,?,?,?)";`
- `sources/com/ble_health_plus/database/reminder/AddReminderDao_Impl.java:212`
  `return "UPDATE OR ABORT 'ReminderTbl' SET 'id' = ?,'title' = ?,'userId' = ?,'description' = ?,'alarmTime' = ?,'days' = ?,'isRepeat' = ?,'sync' = ? WHERE 'id' = ?";`
- `sources/com/ble_health_plus/database/reminder/AddReminderDao_Impl.java:495`
  `int columnIndexOrThrow8 = CursorUtil.getColumnIndexOrThrow(cursorQuery, "sync");`
- `sources/com/ble_health_plus/database/reminder/AddReminderDao_Impl.java:545`
  `int columnIndexOrThrow8 = CursorUtil.getColumnIndexOrThrow(cursorQuery, "sync");`
- `sources/com/ble_health_plus/database/reminder/AddReminderDao_Impl.java:666`
  `int columnIndexOrThrow8 = CursorUtil.getColumnIndexOrThrow(cursorQuery, "sync");`

## BR094

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `sources/android/support/v4/media/session/MediaSessionCompat.java:1700`
  `synchronized (MediaSessionImplBase.this.mLock) {`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1779`
  `postToHandler(10, uri, bundle);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1784`
  `postToHandler(11, Long.valueOf(j));`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1789`
  `postToHandler(12);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1814`
  `postToHandler(17);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1819`
  `postToHandler(18, Long.valueOf(j));`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1824`
  `postToHandler(19, ratingCompat);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:2197`
  `MediaSessionImplApi18.this.postToHandler(18, -1, -1, Long.valueOf(j), null);`
- `sources/androidx/activity/result/ActivityResultRegistry.java:164`
  `public final void onSaveInstanceState(Bundle bundle) {`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:23`
  `@Metadata(d1 = {"\u0000\u000e\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0000\n\u0002\b\u0006\u0018\u0000*\u0004\b\u0002\u0010\u00012\u00020\u0002B\r\u0012\u0006\u0010\u0003\u001a\u00028\u0002¢\u0006\u0002\u0010\u0004R\u0013\u0010\u0003\u001a\u00028\u0002¢\u0006\n\n\u0002\u0010\u0007\u001a\u0004\b\u...`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:24`
  `public static final class SynchronousResult<T> {`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:27`
  `public SynchronousResult(T t) {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:127`
  `boolean mInvalidatePanelMenuPosted;`
- `sources/androidx/appcompat/app/AppCompatViewInflater.java:51`
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
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:238`
  `private synchronized boolean addDrawableToCache(Context context, long j, Drawable drawable) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:252`
  `synchronized Drawable onDrawableLoadedFromResources(Context context, VectorEnabledTintResources vectorEnabledTintResources, int i) {`
- `sources/androidx/appcompat/widget/SearchView.java:91`
  `private final View mSubmitArea;`
- `sources/androidx/appcompat/widget/SearchView.java:237`
  `ViewCompat.saveAttributeDataForStyleable(this, context, R.styleable.SearchView, attributeSet, tintTypedArrayObtainStyledAttributes.getWrappedTypeArray(), i, 0);`
- `sources/androidx/appcompat/widget/SearchView.java:245`
  `View viewFindViewById2 = findViewById(R.id.submit_area);`
- `sources/androidx/appcompat/widget/SearchView.java:246`
  `this.mSubmitArea = viewFindViewById2;`
- `sources/androidx/appcompat/widget/SearchView.java:627`
  `post(this.mUpdateDrawableStateRunnable);`
- `sources/androidx/appcompat/widget/SearchView.java:636`
  `Drawable background2 = this.mSubmitArea.getBackground();`
- `sources/androidx/appcompat/widget/SwitchCompat.java:915`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/appcompat/widget/TooltipCompatHandler.java:140`
  `this.mAnchor.postDelayed(this.mHideRunnable, j2);`
- `sources/androidx/appcompat/widget/TooltipCompatHandler.java:175`
  `this.mAnchor.postDelayed(this.mShowRunnable, ViewConfiguration.getLongPressTimeout());`
- `sources/androidx/asynclayoutinflater/R.java:1`
  `package androidx.asynclayoutinflater;`
- `sources/androidx/asynclayoutinflater/view/AsyncLayoutInflater.java:1`
  `package androidx.asynclayoutinflater.view;`
- `sources/androidx/asynclayoutinflater/view/AsyncLayoutInflater.java:15`
  `public final class AsyncLayoutInflater {`
- `sources/androidx/asynclayoutinflater/view/AsyncLayoutInflater.java:16`
  `private static final String TAG = "AsyncLayoutInflater";`

## BR095

paper_id: B025
paper_title: Why Eve and Mallory Still Love Android: Revisiting TLS (In)Security in Android Applications

- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:447`
  `// br : http://registro.br/dominio/categoria.html`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:3694`
  `// http://www.dot.kn/domainRules.html`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:3881`
  `// http://www.anrt.ma/fr/admin/download/upload/file_fr782.pdf`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:3938`
  `// ml : http://www.gobin.info/domainname/ml-template.doc`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:3969`
  `// mp : http://www.dot.mp/`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:5558`
  `// ph : http://www.domains.ph/FAQ2.asp`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:6794`
  `// http://nic.ae/english/arabicdomain/rules.jsp`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:11591`
  `// Enonic : http://enonic.com/`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:11852`
  `// Futureweb OG : http://www.futureweb.at`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:12161`
  `// I-O DATA DEVICE, INC. : http://www.iodata.com/`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:12208`
  `// KaasHosting : http://www.kaashosting.nl/`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:12222`
  `// KnightPoint Systems, LLC : http://www.knightpoint.com/`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:12230`
  `// .KRD : http://nic.krd/data/krd/Registration%20Policy.pdf`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:12279`
  `// LiquidNet Ltd : http://www.liquidnetlimited.com/`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:12900`
  `// Revitalised Limited : http://www.revitalised.co.uk`
- `resources/com.ble_health_plus.apk/mozilla/public-suffix-list.txt:13044`
  `// Sub 6 Limited: http://www.sub6.com`
- `resources/com.ble_health_plus.apk/res/drawable/$avd_hide_password__0.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.ble_health_plus.apk/res/drawable/$avd_hide_password__1.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.ble_health_plus.apk/res/drawable/$avd_hide_password__2.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.ble_health_plus.apk/res/drawable/$avd_show_password__0.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.ble_health_plus.apk/res/drawable/$avd_show_password__1.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.ble_health_plus.apk/res/drawable/$avd_show_password__2.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_ic_ab_back_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_ic_arrow_drop_right_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_ic_clear_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_ic_go_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_ic_menu_copy_mtrl_am_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_ic_menu_cut_mtrl_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_ic_menu_overflow_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_ic_menu_paste_mtrl_am_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_ic_menu_selectall_mtrl_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_ic_menu_share_mtrl_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_ic_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_ic_voice_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_seekbar_tick_mark_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/com.ble_health_plus.apk/res/drawable/abc_star_black_48dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_star_half_black_48dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/abc_text_cursor_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/com.ble_health_plus.apk/res/drawable/abc_vector_test.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/avd_hide_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_hide_password__0_res_0x7f080000">`
- `resources/com.ble_health_plus.apk/res/drawable/avd_show_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_show_password__0_res_0x7f080003">`
- `resources/com.ble_health_plus.apk/res/drawable/bg_circle_drawable.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/com.ble_health_plus.apk/res/drawable/bg_heart_rate.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/com.ble_health_plus.apk/res/drawable/bg_hr_chart.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/com.ble_health_plus.apk/res/drawable/bg_spinner.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/com.ble_health_plus.apk/res/drawable/bg_ws_chart.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/com.ble_health_plus.apk/res/drawable/btn_checkbox_checked_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/btn_checkbox_unchecked_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/btn_radio_off_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/btn_radio_on_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/button_corner.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/com.ble_health_plus.apk/res/drawable/button_round_corner_bp.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/com.ble_health_plus.apk/res/drawable/button_round_corner_hr.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/com.ble_health_plus.apk/res/drawable/button_round_corner_hr_chart.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/com.ble_health_plus.apk/res/drawable/design_ic_visibility.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/design_ic_visibility_off.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/fade_graph_weight.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/com.ble_health_plus.apk/res/drawable/heart_rate_box_bg.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/com.ble_health_plus.apk/res/drawable/heart_rate_icon_bg.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/com.ble_health_plus.apk/res/drawable/icon_export.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/icon_history.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/icon_settings.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/ic_arrow_upward.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/ic_auto.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/ic_blue_dot.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/ic_bt_disconnect.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/ic_circle_.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/com.ble_health_plus.apk/res/drawable/ic_circle_green.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/com.ble_health_plus.apk/res/drawable/ic_circle_orange.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/com.ble_health_plus.apk/res/drawable/ic_circle_white_8dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/ic_clock_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/ic_delete.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/ic_dia_dot.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/ic_done_chk.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/ic_dot_small.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/ic_ellipse_21.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/ic_green_dot.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/ic_keyboard_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/ic_launcher_background.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.ble_health_plus.apk/res/drawable/ic_m3_chip_check.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`

## BR096

paper_id: B011
paper_title: Locking it down: The privacy and security of mobile medication apps

- `resources/com.ble_health_plus.apk/drive.v3.json:5`
  `"https://www.googleapis.com/auth/drive": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:8`
  `"https://www.googleapis.com/auth/drive.appdata": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:11`
  `"https://www.googleapis.com/auth/drive.file": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:14`
  `"https://www.googleapis.com/auth/drive.metadata": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:17`
  `"https://www.googleapis.com/auth/drive.metadata.readonly": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:20`
  `"https://www.googleapis.com/auth/drive.photos.readonly": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:23`
  `"https://www.googleapis.com/auth/drive.readonly": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:26`
  `"https://www.googleapis.com/auth/drive.scripts": {`
- `resources/com.ble_health_plus.apk/drive.v3.json:33`
  `"baseUrl": "https://www.googleapis.com/drive/v3/",`
- `resources/com.ble_health_plus.apk/drive.v3.json:37`
  `"documentationLink": "https://developers.google.com/drive/",`
- `resources/com.ble_health_plus.apk/drive.v3.json:106`
  `"https://www.googleapis.com/auth/drive",`
- `resources/com.ble_health_plus.apk/drive.v3.json:107`
  `"https://www.googleapis.com/auth/drive.appdata",`
- `resources/com.ble_health_plus.apk/drive.v3.json:108`
  `"https://www.googleapis.com/auth/drive.file",`
- `resources/com.ble_health_plus.apk/drive.v3.json:109`
  `"https://www.googleapis.com/auth/drive.metadata",`
- `resources/com.ble_health_plus.apk/drive.v3.json:110`
  `"https://www.googleapis.com/auth/drive.metadata.readonly",`
- `resources/com.ble_health_plus.apk/drive.v3.json:111`
  `"https://www.googleapis.com/auth/drive.photos.readonly",`
- `resources/com.ble_health_plus.apk/drive.v3.json:112`
  `"https://www.googleapis.com/auth/drive.readonly"`
- `resources/com.ble_health_plus.apk/drive.v3.json:152`
  `"https://www.googleapis.com/auth/drive",`
- `resources/com.ble_health_plus.apk/drive.v3.json:153`
  `"https://www.googleapis.com/auth/drive.appdata",`
- `resources/com.ble_health_plus.apk/drive.v3.json:154`
  `"https://www.googleapis.com/auth/drive.file",`
- `resources/com.ble_health_plus.apk/drive.v3.json:155`
  `"https://www.googleapis.com/auth/drive.metadata",`
- `resources/com.ble_health_plus.apk/drive.v3.json:156`
  `"https://www.googleapis.com/auth/drive.metadata.readonly",`
- `resources/com.ble_health_plus.apk/drive.v3.json:157`
  `"https://www.googleapis.com/auth/drive.photos.readonly",`
- `resources/com.ble_health_plus.apk/drive.v3.json:158`
  `"https://www.googleapis.com/auth/drive.readonly"`
- `resources/com.ble_health_plus.apk/drive.v3.json:253`
  `"https://www.googleapis.com/auth/drive",`
- `resources/com.ble_health_plus.apk/drive.v3.json:254`
  `"https://www.googleapis.com/auth/drive.appdata",`
- `resources/com.ble_health_plus.apk/drive.v3.json:255`
  `"https://www.googleapis.com/auth/drive.file",`
- `resources/com.ble_health_plus.apk/drive.v3.json:256`
  `"https://www.googleapis.com/auth/drive.metadata",`
- `resources/com.ble_health_plus.apk/drive.v3.json:257`
  `"https://www.googleapis.com/auth/drive.metadata.readonly",`
- `resources/com.ble_health_plus.apk/drive.v3.json:258`
  `"https://www.googleapis.com/auth/drive.photos.readonly",`
- `resources/com.ble_health_plus.apk/drive.v3.json:259`
  `"https://www.googleapis.com/auth/drive.readonly"`
- `resources/com.ble_health_plus.apk/drive.v3.json:359`
  `"https://www.googleapis.com/auth/drive",`
- `resources/com.ble_health_plus.apk/drive.v3.json:360`
  `"https://www.googleapis.com/auth/drive.appdata",`
- `resources/com.ble_health_plus.apk/drive.v3.json:361`
  `"https://www.googleapis.com/auth/drive.file",`
- `resources/com.ble_health_plus.apk/drive.v3.json:362`
  `"https://www.googleapis.com/auth/drive.metadata",`
- `resources/com.ble_health_plus.apk/drive.v3.json:363`
  `"https://www.googleapis.com/auth/drive.metadata.readonly",`
- `resources/com.ble_health_plus.apk/drive.v3.json:364`
  `"https://www.googleapis.com/auth/drive.photos.readonly",`
- `resources/com.ble_health_plus.apk/drive.v3.json:365`
  `"https://www.googleapis.com/auth/drive.readonly"`
- `resources/com.ble_health_plus.apk/drive.v3.json:383`
  `"https://www.googleapis.com/auth/drive",`
- `resources/com.ble_health_plus.apk/drive.v3.json:384`
  `"https://www.googleapis.com/auth/drive.appdata",`
- `resources/com.ble_health_plus.apk/drive.v3.json:385`
  `"https://www.googleapis.com/auth/drive.file",`
- `resources/com.ble_health_plus.apk/drive.v3.json:386`
  `"https://www.googleapis.com/auth/drive.metadata",`
- `resources/com.ble_health_plus.apk/drive.v3.json:387`
  `"https://www.googleapis.com/auth/drive.metadata.readonly",`
- `resources/com.ble_health_plus.apk/drive.v3.json:388`
  `"https://www.googleapis.com/auth/drive.photos.readonly",`
- `resources/com.ble_health_plus.apk/drive.v3.json:389`
  `"https://www.googleapis.com/auth/drive.readonly"`
- `resources/com.ble_health_plus.apk/drive.v3.json:419`
  `"https://www.googleapis.com/auth/drive",`
- `resources/com.ble_health_plus.apk/drive.v3.json:420`
  `"https://www.googleapis.com/auth/drive.file"`
- `resources/com.ble_health_plus.apk/drive.v3.json:447`
  `"https://www.googleapis.com/auth/drive",`
- `resources/com.ble_health_plus.apk/drive.v3.json:448`
  `"https://www.googleapis.com/auth/drive.file"`
- `resources/com.ble_health_plus.apk/drive.v3.json:484`
  `"https://www.googleapis.com/auth/drive",`
- `resources/com.ble_health_plus.apk/drive.v3.json:485`
  `"https://www.googleapis.com/auth/drive.file",`
- `resources/com.ble_health_plus.apk/drive.v3.json:486`
  `"https://www.googleapis.com/auth/drive.readonly"`
- `resources/com.ble_health_plus.apk/drive.v3.json:534`
  `"https://www.googleapis.com/auth/drive",`
- `resources/com.ble_health_plus.apk/drive.v3.json:535`
  `"https://www.googleapis.com/auth/drive.file",`
- `resources/com.ble_health_plus.apk/drive.v3.json:536`
  `"https://www.googleapis.com/auth/drive.readonly"`
- `resources/com.ble_health_plus.apk/drive.v3.json:569`
  `"https://www.googleapis.com/auth/drive",`
- `resources/com.ble_health_plus.apk/drive.v3.json:570`
  `"https://www.googleapis.com/auth/drive.file"`
- `resources/com.ble_health_plus.apk/drive.v3.json:600`
  `"https://www.googleapis.com/auth/drive"`
- `resources/com.ble_health_plus.apk/drive.v3.json:620`
  `"https://www.googleapis.com/auth/drive"`
- `resources/com.ble_health_plus.apk/drive.v3.json:649`
  `"https://www.googleapis.com/auth/drive",`
- `resources/com.ble_health_plus.apk/drive.v3.json:650`
  `"https://www.googleapis.com/auth/drive.readonly"`
- `resources/com.ble_health_plus.apk/drive.v3.json:673`
  `"https://www.googleapis.com/auth/drive"`
- `resources/com.ble_health_plus.apk/drive.v3.json:712`
  `"https://www.googleapis.com/auth/drive",`
- `resources/com.ble_health_plus.apk/drive.v3.json:713`
  `"https://www.googleapis.com/auth/drive.readonly"`
- `resources/com.ble_health_plus.apk/drive.v3.json:736`
  `"https://www.googleapis.com/auth/drive"`
- `resources/com.ble_health_plus.apk/drive.v3.json:768`
  `"https://www.googleapis.com/auth/drive"`
- `resources/com.ble_health_plus.apk/drive.v3.json:838`
  `"https://www.googleapis.com/auth/drive",`
- `resources/com.ble_health_plus.apk/drive.v3.json:839`
  `"https://www.googleapis.com/auth/drive.appdata",`
- `resources/com.ble_health_plus.apk/drive.v3.json:840`
  `"https://www.googleapis.com/auth/drive.file",`
- `resources/com.ble_health_plus.apk/drive.v3.json:841`
  `"https://www.googleapis.com/auth/drive.photos.readonly"`
- `resources/com.ble_health_plus.apk/drive.v3.json:920`
  `"https://www.googleapis.com/auth/drive",`
- `resources/com.ble_health_plus.apk/drive.v3.json:921`
  `"https://www.googleapis.com/auth/drive.appdata",`
- `resources/com.ble_health_plus.apk/drive.v3.json:922`
  `"https://www.googleapis.com/auth/drive.file"`
- `resources/com.ble_health_plus.apk/drive.v3.json:962`
  `"https://www.googleapis.com/auth/drive",`
- `resources/com.ble_health_plus.apk/drive.v3.json:963`
  `"https://www.googleapis.com/auth/drive.appdata",`
- `resources/com.ble_health_plus.apk/drive.v3.json:964`
  `"https://www.googleapis.com/auth/drive.file"`
- `resources/com.ble_health_plus.apk/drive.v3.json:981`
  `"https://www.googleapis.com/auth/drive"`
- `resources/com.ble_health_plus.apk/drive.v3.json:1008`
  `"https://www.googleapis.com/auth/drive",`
- `resources/com.ble_health_plus.apk/drive.v3.json:1009`
  `"https://www.googleapis.com/auth/drive.file",`
- `resources/com.ble_health_plus.apk/drive.v3.json:1010`
  `"https://www.googleapis.com/auth/drive.readonly"`

## BR098

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/com/ble_health_plus/network/ApiController.java:1304`
  `return new OkHttpClient.Builder().connectTimeout(30L, TimeUnit.SECONDS).readTimeout(30L, TimeUnit.SECONDS).writeTimeout(120L, TimeUnit.SECONDS).addInterceptor(new Interceptor() { // from class: com.ble_health_plus.network.ApiController$$ExternalSyntheticLambda0`
- `sources/com/ble_health_plus/network/RetroClient.java:22`
  `Retrofit retrofitBuild = new Retrofit.Builder().baseUrl(BuildConfig.BASE_URL).addConverterFactory(GsonConverterFactory.create(new GsonBuilder().setLenient().create())).client(okHttpClient).build();`
