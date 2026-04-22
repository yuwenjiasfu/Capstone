# Rule Search Hits

## BR001

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/AndroidManifest.xml:17`
  `<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>`
- `resources/AndroidManifest.xml:18`
  `<uses-permission android:name="android.permission.CAMERA"/>`
- `resources/AndroidManifest.xml:19`
  `<uses-permission android:name="android.permission.GET_ACCOUNTS"/>`

## BR002

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/AndroidManifest.xml:23`
  `<uses-permission`
- `resources/AndroidManifest.xml:26`
  `<uses-permission`

## BR003

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/AndroidManifest.xml:29`
  `<uses-permission`
- `resources/AndroidManifest.xml:32`
  `<uses-permission`
- `resources/AndroidManifest.xml:35`
  `<uses-permission`
- `resources/AndroidManifest.xml:38`
  `<uses-permission android:name="android.permission.BLUETOOTH_CONNECT"/>`

## BR005

paper_id: B021
paper_title: Metadata-Based Privacy Assessment for Mobile mHealth

- `resources/AndroidManifest.xml:47`
  `<uses-permission android:name="com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE"/>`
- `resources/AndroidManifest.xml:48`
  `<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>`
- `resources/AndroidManifest.xml:49`
  `<uses-permission android:name="android.permission.ACCESS_ADSERVICES_ATTRIBUTION"/>`
- `resources/AndroidManifest.xml:50`
  `<uses-permission android:name="android.permission.ACCESS_ADSERVICES_AD_ID"/>`
- `resources/AndroidManifest.xml:51`
  `<uses-permission android:name="com.google.android.providers.gsf.permission.READ_GSERVICES"/>`
- `resources/AndroidManifest.xml:52`
  `<uses-permission android:name="android.permission.ACCESS_ADSERVICES_CUSTOM_AUDIENCE"/>`
- `resources/AndroidManifest.xml:53`
  `<uses-permission android:name="android.permission.ACCESS_ADSERVICES_TOPICS"/>`

## BR009

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:26`
  `public final class AdvancedTlsX509TrustManager extends X509ExtendedTrustManager {`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:27`
  `private static final Logger log = Logger.getLogger(AdvancedTlsX509TrustManager.class.getName());`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:49`
  `private AdvancedTlsX509TrustManager(Verification verification, SslSocketAndEnginePeerVerifier sslSocketAndEnginePeerVerifier) throws CertificateException {`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:55`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:56`
  `public void checkClientTrusted(X509Certificate[] x509CertificateArr, String str) throws CertificateException {`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:61`
  `public void checkClientTrusted(X509Certificate[] x509CertificateArr, String str, Socket socket) throws CertificateException {`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:66`
  `public void checkClientTrusted(X509Certificate[] x509CertificateArr, String str, SSLEngine sSLEngine) throws CertificateException {`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:71`
  `public void checkServerTrusted(X509Certificate[] x509CertificateArr, String str, SSLEngine sSLEngine) throws CertificateException {`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:75`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:76`
  `public void checkServerTrusted(X509Certificate[] x509CertificateArr, String str) throws CertificateException {`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:81`
  `public void checkServerTrusted(X509Certificate[] x509CertificateArr, String str, Socket socket) throws CertificateException {`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:85`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:150`
  `x509ExtendedTrustManager.checkServerTrusted(x509CertificateArr, str, sSLEngine);`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:159`
  `x509ExtendedTrustManager.checkServerTrusted(x509CertificateArr, str, sSLSocket);`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:162`
  `x509ExtendedTrustManager.checkClientTrusted(x509CertificateArr, str, sSLEngine);`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:180`
  `return new Closeable() { // from class: io.grpc.util.AdvancedTlsX509TrustManager.1`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:181`
  `@Override // io.grpc.util.AdvancedTlsX509TrustManager.Closeable, java.io.Closeable, java.lang.AutoCloseable`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:199`
  `this.currentTime = AdvancedTlsX509TrustManager.this.readAndUpdate(this.file, this.currentTime);`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:201`
  `AdvancedTlsX509TrustManager.log.log(Level.SEVERE, "Failed refreshing trust CAs from file. Using previous CAs", e2);`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:249`
  `public AdvancedTlsX509TrustManager build() throws CertificateException {`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:250`
  `return new AdvancedTlsX509TrustManager(this.verification, this.socketAndEnginePeerVerifier);`
- `sources/okhttp3/OkHttpClient.java:23`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/OkHttpClient.java:49`
  `@Metadata(d1 = {"\u0000ú\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0002\b\u0003\n\u000...`
- `sources/okhttp3/OkHttpClient.java:83`
  `private final X509TrustManager x509TrustManager;`
- `sources/okhttp3/OkHttpClient.java:154`
  `this.x509TrustManager = null;`
- `sources/okhttp3/OkHttpClient.java:165`
  `X509TrustManager x509TrustManagerOrNull = builder.getX509TrustManagerOrNull();`
- `sources/okhttp3/OkHttpClient.java:166`
  `Intrinsics.checkNotNull(x509TrustManagerOrNull);`
- `sources/okhttp3/OkHttpClient.java:167`
  `this.x509TrustManager = x509TrustManagerOrNull;`
- `sources/okhttp3/OkHttpClient.java:172`
  `X509TrustManager x509TrustManagerPlatformTrustManager = Platform.INSTANCE.get().platformTrustManager();`
- `sources/okhttp3/OkHttpClient.java:173`
  `this.x509TrustManager = x509TrustManagerPlatformTrustManager;`
- `sources/okhttp3/OkHttpClient.java:175`
  `Intrinsics.checkNotNull(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/OkHttpClient.java:176`
  `this.sslSocketFactoryOrNull = platform.newSslSocketFactory(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/OkHttpClient.java:178`
  `Intrinsics.checkNotNull(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/OkHttpClient.java:179`
  `CertificateChainCleaner certificateChainCleaner2 = companion.get(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/OkHttpClient.java:189`
  `this.x509TrustManager = null;`
- `sources/okhttp3/OkHttpClient.java:268`
  `/* JADX INFO: renamed from: x509TrustManager, reason: from getter */`
- `sources/okhttp3/OkHttpClient.java:269`
  `public final X509TrustManager getX509TrustManager() {`
- `sources/okhttp3/OkHttpClient.java:270`
  `return this.x509TrustManager;`
- `sources/okhttp3/OkHttpClient.java:381`
  `if (this.x509TrustManager == null) {`
- `sources/okhttp3/OkHttpClient.java:382`
  `throw new IllegalStateException("x509TrustManager == null".toString());`
- `sources/okhttp3/OkHttpClient.java:394`
  `if (this.x509TrustManager != null) {`
- `sources/okhttp3/OkHttpClient.java:579`
  `@Metadata(d1 = {"\u0000\u0086\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010!\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010...`
- `sources/okhttp3/OkHttpClient.java:613`
  `private X509TrustManager x509TrustManagerOrNull;`
- `sources/okhttp3/OkHttpClient.java:801`
  `/* JADX INFO: renamed from: getX509TrustManagerOrNull$okhttp, reason: from getter */`
- `sources/okhttp3/OkHttpClient.java:802`
  `public final X509TrustManager getX509TrustManagerOrNull() {`
- `sources/okhttp3/OkHttpClient.java:803`
  `return this.x509TrustManagerOrNull;`
- `sources/okhttp3/OkHttpClient.java:806`
  `public final void setX509TrustManagerOrNull$okhttp(X509TrustManager x509TrustManager) {`
- `sources/okhttp3/OkHttpClient.java:807`
  `this.x509TrustManagerOrNull = x509TrustManager;`
- `sources/okhttp3/OkHttpClient.java:960`
  `this.x509TrustManagerOrNull = okHttpClient.getX509TrustManager();`
- `sources/okhttp3/OkHttpClient.java:1135`
  `@Deprecated(level = DeprecationLevel.ERROR, message = "Use the sslSocketFactory overload that accepts a X509TrustManager.")`
- `sources/okhttp3/OkHttpClient.java:1142`
  `X509TrustManager x509TrustManagerTrustManager = Platform.INSTANCE.get().trustManager(sslSocketFactory);`
- `sources/okhttp3/OkHttpClient.java:1143`
  `if (x509TrustManagerTrustManager != null) {`
- `sources/okhttp3/OkHttpClient.java:1144`
  `this.x509TrustManagerOrNull = x509TrustManagerTrustManager;`
- `sources/okhttp3/OkHttpClient.java:1146`
  `X509TrustManager x509TrustManager = this.x509TrustManagerOrNull;`
- `sources/okhttp3/OkHttpClient.java:1147`
  `Intrinsics.checkNotNull(x509TrustManager);`
- `sources/okhttp3/OkHttpClient.java:1148`
  `this.certificateChainCleaner = platform.buildCertificateChainCleaner(x509TrustManager);`
- `sources/okhttp3/OkHttpClient.java:1154`
  `public final Builder sslSocketFactory(SSLSocketFactory sslSocketFactory, X509TrustManager trustManager) {`
- `sources/okhttp3/OkHttpClient.java:1157`
  `if (!Intrinsics.areEqual(sslSocketFactory, this.sslSocketFactoryOrNull) || !Intrinsics.areEqual(trustManager, this.x509TrustManagerOrNull)) {`
- `sources/okhttp3/OkHttpClient.java:1162`
  `this.x509TrustManagerOrNull = trustManager;`
- `sources/okhttp3/internal/platform/Android10Platform.java:16`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/platform/Android10Platform.java:34`
  `@Metadata(d1 = {"\u0000j\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\...`
- `sources/okhttp3/internal/platform/Android10Platform.java:65`
  `public X509TrustManager trustManager(SSLSocketFactory sslSocketFactory) {`
- `sources/okhttp3/internal/platform/Android10Platform.java:93`
  `public TrustRootIndex buildTrustRootIndex(X509TrustManager trustManager) {`
- `sources/okhttp3/internal/platform/Android10Platform.java:173`
  `public CertificateChainCleaner buildCertificateChainCleaner(X509TrustManager trustManager) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:26`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:44`
  `@Metadata(d1 = {"\u0000\u0082\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0000\n...`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:89`
  `public X509TrustManager trustManager(SSLSocketFactory sslSocketFactory) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:162`
  `public CertificateChainCleaner buildCertificateChainCleaner(X509TrustManager trustManager) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:169`
  `public TrustRootIndex buildTrustRootIndex(X509TrustManager trustManager) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:199`
  `@Metadata(d1 = {"\u00008\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u000e\n\u0000\b\u0080\b\u0018\u00...`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:202`
  `private final X509TrustManager trustManager;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:205`
  `private final X509TrustManager getTrustManager() {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:214`
  `public static /* synthetic */ CustomTrustRootIndex copy$default(CustomTrustRootIndex customTrustRootIndex, X509TrustManager x509TrustManager, Method method, int i, Object obj) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:216`
  `x509TrustManager = customTrustRootIndex.trustManager;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:221`
  `return customTrustRootIndex.copy(x509TrustManager, method);`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:224`
  `public final CustomTrustRootIndex copy(X509TrustManager trustManager, Method findByIssuerAndSignatureMethod) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:249`
  `public CustomTrustRootIndex(X509TrustManager trustManager, Method findByIssuerAndSignatureMethod) {`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:10`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:19`
  `@Metadata(d1 = {"\u0000B\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\...`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:52`
  `public X509TrustManager trustManager(SSLSocketFactory sslSocketFactory) {`

## BR010

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/okhttp3/internal/connection/RealConnection.java:218`
  `if (this.http2Connection == null || routes == null || !routeMatchesAny(routes) || address.hostnameVerifier() != OkHostnameVerifier.INSTANCE || !supportsUrl(address.url())) {`
- `sources/okhttp3/internal/connection/RealConnection.java:268`
  `OkHostnameVerifier okHostnameVerifier = OkHostnameVerifier.INSTANCE;`
- `sources/okhttp3/internal/connection/RealConnection.java:272`
  `if (okHostnameVerifier.verify(strHost, (X509Certificate) certificate)) {`
- `sources/okhttp3/internal/tls/BasicCertificateChainCleaner.java:76`
  `toVerify.verify(signingCert.getPublicKey());`

## BR011

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/okhttp3/internal/connection/RetryTlsHandshakeKt.java:7`
  `import java.security.cert.CertificateException;`
- `sources/okhttp3/internal/connection/RetryTlsHandshakeKt.java:8`
  `import javax.net.ssl.SSLException;`
- `sources/okhttp3/internal/connection/RetryTlsHandshakeKt.java:9`
  `import javax.net.ssl.SSLHandshakeException;`
- `sources/okhttp3/internal/connection/RetryTlsHandshakeKt.java:23`
  `return (((e2 instanceof SSLHandshakeException) && (e2.getCause() instanceof CertificateException)) || (e2 instanceof SSLPeerUnverifiedException) || !(e2 instanceof SSLException)) ? false : true;`

## BR012

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/okhttp3/Address.java:23`
  `@Metadata(d1 = {"\u0000h\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002...`
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
- `sources/okhttp3/Address.java:177`
  `return ((((((((((((((((((527 + this.url.hashCode()) * 31) + this.dns.hashCode()) * 31) + this.proxyAuthenticator.hashCode()) * 31) + this.protocols.hashCode()) * 31) + this.connectionSpecs.hashCode()) * 31) + this.proxySelector.hashCode()) * 31) + Objects.hashCode(this.proxy)) * 31) + Objects.hashCo...`
- `sources/okhttp3/Address.java:182`
  `return Intrinsics.areEqual(this.dns, that.dns) && Intrinsics.areEqual(this.proxyAuthenticator, that.proxyAuthenticator) && Intrinsics.areEqual(this.protocols, that.protocols) && Intrinsics.areEqual(this.connectionSpecs, that.connectionSpecs) && Intrinsics.areEqual(this.proxySelector, that.proxySelec...`
- `sources/okhttp3/CertificatePinner.java:27`
  `/* JADX INFO: compiled from: CertificatePinner.kt */`
- `sources/okhttp3/CertificatePinner.java:29`
  `@Metadata(d1 = {"\u0000T\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\"\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0007\n\u0002\u0010\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\...`
- `sources/okhttp3/CertificatePinner.java:30`
  `public final class CertificatePinner {`
- `sources/okhttp3/CertificatePinner.java:34`
  `public static final CertificatePinner DEFAULT = new Builder().build();`
- `sources/okhttp3/CertificatePinner.java:53`
  `public CertificatePinner(Set<Pin> pins, CertificateChainCleaner certificateChainCleaner) {`
- `sources/okhttp3/CertificatePinner.java:59`
  `public /* synthetic */ CertificatePinner(Set set, CertificateChainCleaner certificateChainCleaner, int i, DefaultConstructorMarker defaultConstructorMarker) {`
- `sources/okhttp3/CertificatePinner.java:75`
  `check$okhttp(hostname, new Function0() { // from class: okhttp3.CertificatePinner$$ExternalSyntheticLambda0`
- `sources/okhttp3/CertificatePinner.java:78`
  `return CertificatePinner.check$lambda$1(this.f$0, peerCertificates, hostname);`
- `sources/okhttp3/CertificatePinner.java:84`
  `public static final List check$lambda$1(CertificatePinner certificatePinner, List list, String str) {`
- `sources/okhttp3/CertificatePinner.java:86`
  `CertificateChainCleaner certificateChainCleaner = certificatePinner.certificateChainCleaner;`
- `sources/okhttp3/CertificatePinner.java:171`
  `public final CertificatePinner withCertificateChainCleaner$okhttp(CertificateChainCleaner certificateChainCleaner) {`
- `sources/okhttp3/CertificatePinner.java:173`
  `return Intrinsics.areEqual(this.certificateChainCleaner, certificateChainCleaner) ? this : new CertificatePinner(this.pins, certificateChainCleaner);`
- `sources/okhttp3/CertificatePinner.java:177`
  `if (!(other instanceof CertificatePinner)) {`
- `sources/okhttp3/CertificatePinner.java:180`
  `CertificatePinner certificatePinner = (CertificatePinner) other;`
- `sources/okhttp3/CertificatePinner.java:181`
  `return Intrinsics.areEqual(certificatePinner.pins, this.pins) && Intrinsics.areEqual(certificatePinner.certificateChainCleaner, this.certificateChainCleaner);`
- `sources/okhttp3/CertificatePinner.java:190`
  `/* JADX INFO: compiled from: CertificatePinner.kt */`
- `sources/okhttp3/CertificatePinner.java:191`
  `@Metadata(d1 = {"\u00000\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0002\b\b\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u000b\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010\b\n\u0000\u0018\u00002\u00020\u0001B\u0017\u0012\u0006\u0010\u0002\u001a\...`
- `sources/okhttp3/CertificatePinner.java:218`
  `if (StringsKt.startsWith$default(pin, "sha256/", false, 2, (Object) null)) {`
- `sources/okhttp3/CertificatePinner.java:230`
  `throw new IllegalArgumentException("pins must start with 'sha256/' or 'sha1/': " + pin);`
- `sources/okhttp3/CertificatePinner.java:265`
  `return Intrinsics.areEqual(this.hash, CertificatePinner.INSTANCE.sha256Hash(certificate));`
- `sources/okhttp3/CertificatePinner.java:268`
  `return Intrinsics.areEqual(this.hash, CertificatePinner.INSTANCE.sha1Hash(certificate));`
- `sources/okhttp3/CertificatePinner.java:293`
  `/* JADX INFO: compiled from: CertificatePinner.kt */`
- `sources/okhttp3/CertificatePinner.java:294`
  `@Metadata(d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0010!\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010\u000e\n\u0002\u0010\u0011\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\u0018\u00002\u00020\u0001B\u0007¢\u0006\u0004\b\u0002\u0010\u0003J'\u0010\t\u001a\u0...`
- `sources/okhttp3/CertificatePinner.java:311`
  `public final CertificatePinner build() {`
- `sources/okhttp3/CertificatePinner.java:312`
  `return new CertificatePinner(CollectionsKt.toSet(this.pins), null, 2, 0 == true ? 1 : 0);`
- `sources/okhttp3/CertificatePinner.java:316`
  `/* JADX INFO: compiled from: CertificatePinner.kt */`
- `sources/okhttp3/CertificatePinner.java:317`
  `@Metadata(d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\b\u0086\u0003\u0018\u00002\u00020\u0001B\t\b\u0002¢\u0006\u0004\b\u0002\u0010\u...`
- `sources/okhttp3/CertificatePinner.java:350`
  `return "sha256/" + sha256Hash((X509Certificate) certificate).base64();`
- `sources/okhttp3/OkHttpClient.java:49`
  `@Metadata(d1 = {"\u0000ú\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0002\b\u0003\n\u000...`
- `sources/okhttp3/OkHttpClient.java:55`
  `private final CertificatePinner certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:155`
  `this.certificatePinner = CertificatePinner.DEFAULT;`
- `sources/okhttp3/OkHttpClient.java:168`
  `CertificatePinner certificatePinner = builder.getCertificatePinner();`
- `sources/okhttp3/OkHttpClient.java:170`
  `this.certificatePinner = certificatePinner.withCertificateChainCleaner$okhttp(certificateChainCleaner);`
- `sources/okhttp3/OkHttpClient.java:181`
  `CertificatePinner certificatePinner2 = builder.getCertificatePinner();`
- `sources/okhttp3/OkHttpClient.java:183`
  `this.certificatePinner = certificatePinner2.withCertificateChainCleaner$okhttp(certificateChainCleaner2);`
- `sources/okhttp3/OkHttpClient.java:190`
  `this.certificatePinner = CertificatePinner.DEFAULT;`
- `sources/okhttp3/OkHttpClient.java:285`
  `public final CertificatePinner certificatePinner() {`
- `sources/okhttp3/OkHttpClient.java:286`
  `return this.certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:345`
  `CertificatePinner certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:350`
  `certificatePinner = this.certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:354`
  `certificatePinner = null;`
- `sources/okhttp3/OkHttpClient.java:356`
  `return new Address(url.host(), url.port(), this.dns, this.socketFactory, sslSocketFactory, hostnameVerifier, certificatePinner, this.proxyAuthenticator, this.proxy, this.protocols, this.connectionSpecs, this.proxySelector);`
- `sources/okhttp3/OkHttpClient.java:397`
  `if (!Intrinsics.areEqual(this.certificatePinner, CertificatePinner.DEFAULT)) {`
- `sources/okhttp3/OkHttpClient.java:542`
  `@Deprecated(level = DeprecationLevel.ERROR, message = "moved to val", replaceWith = @ReplaceWith(expression = "certificatePinner", imports = {}))`
- `sources/okhttp3/OkHttpClient.java:543`
  `/* JADX INFO: renamed from: -deprecated_certificatePinner, reason: not valid java name and from getter */`
- `sources/okhttp3/OkHttpClient.java:544`
  `public final CertificatePinner getCertificatePinner() {`
- `sources/okhttp3/OkHttpClient.java:545`
  `return this.certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:579`
  `@Metadata(d1 = {"\u0000\u0086\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010!\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010...`
- `sources/okhttp3/OkHttpClient.java:585`
  `private CertificatePinner certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:634`
  `this.certificatePinner = CertificatePinner.DEFAULT;`
- `sources/okhttp3/OkHttpClient.java:838`
  `/* JADX INFO: renamed from: getCertificatePinner$okhttp, reason: from getter */`
- `sources/okhttp3/OkHttpClient.java:839`
  `public final CertificatePinner getCertificatePinner() {`
- `sources/okhttp3/OkHttpClient.java:840`
  `return this.certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:843`
  `public final void setCertificatePinner$okhttp(CertificatePinner certificatePinner) {`
- `sources/okhttp3/OkHttpClient.java:844`
  `Intrinsics.checkNotNullParameter(certificatePinner, "<set-?>");`
- `sources/okhttp3/OkHttpClient.java:845`
  `this.certificatePinner = certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:964`
  `this.certificatePinner = okHttpClient.certificatePinner();`
- `sources/okhttp3/OkHttpClient.java:1210`
  `public final Builder certificatePinner(CertificatePinner certificatePinner) {`
- `sources/okhttp3/OkHttpClient.java:1211`
  `Intrinsics.checkNotNullParameter(certificatePinner, "certificatePinner");`
- `sources/okhttp3/OkHttpClient.java:1212`
  `if (!Intrinsics.areEqual(certificatePinner, this.certificatePinner)) {`
- `sources/okhttp3/OkHttpClient.java:1215`
  `this.certificatePinner = certificatePinner;`
- `sources/okhttp3/internal/connection/ConnectPlan.java:29`
  `import okhttp3.CertificatePinner;`
- `sources/okhttp3/internal/connection/ConnectPlan.java:311`
  `throw new SSLPeerUnverifiedException(StringsKt.trimMargin$default("\n            |Hostname " + address.url().host() + " not verified:\n            |    certificate: " + CertificatePinner.INSTANCE.pin(x509Certificate) + "\n            |    DN: " + x509Certificate.getSubjectDN().getName() + "\n       ...`
- `sources/okhttp3/internal/connection/ConnectPlan.java:313`
  `final CertificatePinner certificatePinner = address.certificatePinner();`
- `sources/okhttp3/internal/connection/ConnectPlan.java:314`
  `Intrinsics.checkNotNull(certificatePinner);`
- `sources/okhttp3/internal/connection/ConnectPlan.java:318`
  `return ConnectPlan.connectTls$lambda$4(certificatePinner, handshake, address);`
- `sources/okhttp3/internal/connection/ConnectPlan.java:322`
  `certificatePinner.check$okhttp(address.url().host(), new Function0() { // from class: okhttp3.internal.connection.ConnectPlan$$ExternalSyntheticLambda1`
- `sources/okhttp3/internal/connection/ConnectPlan.java:342`
  `public static final List connectTls$lambda$4(CertificatePinner certificatePinner, Handshake handshake, Address address) {`

## BR013

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `resources/res/color/design_box_stroke_color.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/color/m3_textfield_input_text_color.xml:2`
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
- `resources/res/drawable/avd_hide_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_hide_password__0_res_0x7f080000">`
- `resources/res/drawable/avd_show_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_show_password__0_res_0x7f080003">`
- `resources/res/drawable/btn_checkbox_checked_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/btn_checkbox_unchecked_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/btn_create_account.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/btn_health_blood_pressure_save.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/btn_ic_device_next_arrow.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android" android:autoMirrored="true">`
- `resources/res/drawable/btn_ic_male_overweight.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/btn_ic_male_underweight.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/btn_ic_profile_edit_button.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android" android:autoMirrored="true">`
- `resources/res/drawable/btn_ic_vital_blood_pressure.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/btn_ic_vital_spo2.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/btn_ic_vital_temperature.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/btn_ic_vital_weight.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/btn_radio_off_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/btn_radio_on_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ccp_ic_arrow_drop_down.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/com_facebook_button_icon.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/com_facebook_favicon_blue.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/design_ic_visibility.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`

## BR014

paper_id: B022
paper_title: A Study of Android Application Security

- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1459`
  `panelFeatureState.qwertyMode = KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1;`
- `sources/androidx/appcompat/app/ToolbarActionBar.java:436`
  `menu.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);`
- `sources/androidx/appcompat/app/WindowDecorActionBar.java:1280`
  `menu.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);`
- `sources/androidx/core/content/ContextCompat.java:59`
  `import android.telephony.TelephonyManager;`
- `sources/androidx/core/content/ContextCompat.java:310`
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
- `sources/com/facebook/internal/AttributionIdentifiers.java:107`
  `Method methodQuietly = Utility.getMethodQuietly("com.google.android.gms.ads.identifier.AdvertisingIdClient", "getAdvertisingIdInfo", (Class<?>[]) new Class[]{Context.class});`
- `sources/com/facebook/internal/Utility.java:17`
  `import android.telephony.TelephonyManager;`
- `sources/com/facebook/internal/Utility.java:1223`
  `Intrinsics.checkNotNull(systemService, "null cannot be cast to non-null type android.telephony.TelephonyManager");`
- `sources/com/facebook/internal/Utility.java:1224`
  `String networkOperatorName = ((TelephonyManager) systemService).getNetworkOperatorName();`
- `sources/com/facebook/internal/Utility.java:1225`
  `Intrinsics.checkNotNullExpressionValue(networkOperatorName, "telephonyManager.networkOperatorName");`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:8`
  `import android.telephony.TelephonyManager;`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:117`
  `private static TelephonyManager getTelephonyManager(Context context) {`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:118`
  `return (TelephonyManager) context.getSystemService("phone");`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:122`
  `String simOperator = getTelephonyManager(context).getSimOperator();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:27`
  `public class AdvertisingIdClient {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:67`
  `public AdvertisingIdClient(Context context) {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:71`
  `public static Info getAdvertisingIdInfo(Context context) throws GooglePlayServicesRepairableException, IllegalStateException, GooglePlayServicesNotAvailableException, IOException {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:72`
  `AdvertisingIdClient advertisingIdClient = new AdvertisingIdClient(context, -1L, true, false);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:75`
  `advertisingIdClient.zzb(false);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:76`
  `Info infoZzd = advertisingIdClient.zzd(-1);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:77`
  `advertisingIdClient.zzc(infoZzd, true, 0.0f, SystemClock.elapsedRealtime() - jElapsedRealtime, "", null);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:85`
  `AdvertisingIdClient advertisingIdClient = new AdvertisingIdClient(context, -1L, false, false);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:87`
  `advertisingIdClient.zzb(false);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:89`
  `synchronized (advertisingIdClient) {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:90`
  `if (advertisingIdClient.zzc) {`
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
  `Log.i("AdvertisingIdClient", "GMS remote exception ", e2);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:115`
  `throw new IOException("AdvertisingIdClient cannot reconnect.", e3);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:119`
  `advertisingIdClient.zze();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:122`
  `advertisingIdClient.zza();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:141`
  `throw new IOException("AdvertisingIdClient is not connected.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:147`
  `throw new IOException("AdvertisingIdClient cannot reconnect.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:154`
  `Log.i("AdvertisingIdClient", "GMS remote exception ", e2);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:158`
  `throw new IOException("AdvertisingIdClient cannot reconnect.", e3);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:207`
  `Log.i("AdvertisingIdClient", "AdvertisingIdClient unbindService failed.", th);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:276`
  `map.put(ViewHierarchyConstants.TAG_KEY, "AdvertisingIdClient");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:282`
  `public AdvertisingIdClient(Context context, long j, boolean z, boolean z2) {`
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
- `sources/com/google/android/gms/measurement/internal/zzhg.java:7`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/measurement/internal/zzhg.java:78`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(true);`
- `sources/com/google/android/gms/measurement/internal/zzhg.java:80`
  `AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(zzibVar.zzaY());`
- `sources/com/google/android/gms/measurement/internal/zzhg.java:91`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(false);`
- `sources/com/google/android/gms/measurement/internal/zznm.java:5`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/measurement/internal/zznm.java:59`
  `AdvertisingIdClient.Info advertisingIdInfo;`

## BR015

paper_id: B022
paper_title: A Study of Android Application Security

- `sources/com/facebook/GraphRequest.java:888`
  `httpURLConnection.setRequestProperty("Accept-Language", Locale.getDefault().toString());`
- `sources/com/facebook/appevents/codeless/CodelessManager.java:204`
  `jSONArray.put(Build.MODEL != null ? Build.MODEL : "");`
- `sources/com/facebook/appevents/integrity/MACARuleMatchingManager.java:267`
  `String str2 = Build.MODEL;`
- `sources/com/facebook/appevents/internal/AppEventUtility.java:103`
  `String BRAND = Build.BRAND;`
- `sources/com/facebook/appevents/internal/AppEventUtility.java:106`
  `String DEVICE = Build.DEVICE;`
- `sources/com/facebook/appevents/internal/AppEventUtility.java:112`
  `return Intrinsics.areEqual("google_sdk", Build.PRODUCT);`
- `sources/com/facebook/devicerequests/internal/DeviceRequestsHelper.java:60`
  `String DEVICE = Build.DEVICE;`
- `sources/com/facebook/devicerequests/internal/DeviceRequestsHelper.java:63`
  `String MODEL = Build.MODEL;`
- `sources/com/facebook/internal/FacebookSignatureValidator.java:38`
  `String brand = Build.BRAND;`
- `sources/com/facebook/internal/Utility.java:839`
  `jSONArray.put(Build.MODEL);`
- `sources/com/facebook/internal/Utility.java:843`
  `locale2 = Locale.getDefault();`
- `sources/com/facebook/internal/Utility.java:1208`
  `TimeZone timeZone = TimeZone.getDefault();`
- `sources/com/facebook/internal/instrument/InstrumentData.java:295`
  `jSONObject.put(PARAM_DEVICE_MODEL, Build.MODEL);`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:138`
  `return eventInternal.toBuilder().addMetadata(KEY_SDK_VERSION, Build.VERSION.SDK_INT).addMetadata("model", Build.MODEL).addMetadata(KEY_HARDWARE, Build.HARDWARE).addMetadata("device", Build.DEVICE).addMetadata(KEY_PRODUCT, Build.PRODUCT).addMetadata(KEY_OS_BUILD, Build.ID).addMetadata(KEY_MANUFACTURE...`
- `sources/com/google/android/material/color/DynamicColors.java:210`
  `DeviceSupportCondition deviceSupportCondition = DYNAMIC_COLOR_SUPPORTED_MANUFACTURERS.get(Build.MANUFACTURER.toLowerCase(Locale.ROOT));`
- `sources/com/google/android/material/color/DynamicColors.java:212`
  `deviceSupportCondition = DYNAMIC_COLOR_SUPPORTED_BRANDS.get(Build.BRAND.toLowerCase(Locale.ROOT));`
- `sources/com/google/android/material/datepicker/DaysOfWeekAdapter.java:60`
  `textView.setContentDescription(String.format(viewGroup.getContext().getString(R.string.mtrl_picker_day_of_week_column_header), this.calendar.getDisplayName(7, 2, Locale.getDefault())));`
- `sources/com/google/android/material/internal/ManufacturerUtils.java:32`
  `String str = Build.MANUFACTURER;`
- `sources/com/google/android/recaptcha/internal/zzn.java:44`
  `zztfVarZzf.zze(CollectionsKt.listOf((Object[]) new zzth[]{zzg(Build.MANUFACTURER), zzg(Build.MODEL), zzg(Build.DEVICE), zzg(Build.HARDWARE), zzg(Build.FINGERPRINT), zzg(Build.PRODUCT), zzg(Build.BOARD), zzg(Build.BRAND), zzg(ArraysKt.joinToString$default(Build.SUPPORTED_ABIS, a.SEPARATOR_TEXT_COMMA,...`
- `sources/com/google/firebase/FirebaseCommonRegistrar.java:36`
  `arrayList.add(LibraryVersionComponent.create(DEVICE_NAME, safeValue(Build.PRODUCT)));`
- `sources/com/google/firebase/FirebaseCommonRegistrar.java:37`
  `arrayList.add(LibraryVersionComponent.create(DEVICE_MODEL, safeValue(Build.DEVICE)));`
- `sources/com/google/firebase/FirebaseCommonRegistrar.java:38`
  `arrayList.add(LibraryVersionComponent.create(DEVICE_BRAND, safeValue(Build.BRAND)));`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsController.java:557`
  `return StaticSessionData.DeviceData.create(CommonUtils.getCpuArchitectureInt(), Build.MODEL, Runtime.getRuntime().availableProcessors(), CommonUtils.calculateTotalRamInBytes(context), ((long) statFs.getBlockCount()) * ((long) statFs.getBlockSize()), CommonUtils.isEmulator(), CommonUtils.getDeviceSta...`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsReportDataCapture.java:114`
  `String str = Build.MANUFACTURER;`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsReportDataCapture.java:115`
  `return CrashlyticsReport.Session.Device.builder().setArch(deviceArchitecture).setModel(Build.MODEL).setCores(iAvailableProcessors).setRam(jCalculateTotalRamInBytes).setDiskSpace(blockCount).setSimulator(zIsEmulator).setState(deviceState).setManufacturer(str).setModelClass(Build.PRODUCT).build();`
- `sources/com/journeyapps/barcodescanner/camera/CameraConfigurationUtils.java:281`
  `sb.append(Build.BRAND).append("\nCPU_ABI=");`
- `sources/com/journeyapps/barcodescanner/camera/CameraConfigurationUtils.java:283`
  `sb.append(Build.DEVICE).append("\nDISPLAY=");`
- `sources/com/journeyapps/barcodescanner/camera/CameraConfigurationUtils.java:288`
  `sb.append(Build.MANUFACTURER).append("\nMODEL=");`
- `sources/com/journeyapps/barcodescanner/camera/CameraConfigurationUtils.java:289`
  `sb.append(Build.MODEL).append("\nPRODUCT=");`
- `sources/com/journeyapps/barcodescanner/camera/CameraManager.java:207`
  `if (Build.DEVICE.equals("glass-1")) {`
- `sources/com/lifesense/ble/b/b/a/g.java:671`
  `boolean zMatches = strA.toUpperCase(Locale.getDefault()).matches("(80)|(C7)|(CC)|(98)");`
- `sources/com/lifesense/ble/b/b/a/g.java:770`
  `if (strA.toUpperCase(Locale.getDefault()).matches("(83)|(CE)")) {`
- `sources/com/viwave/rossmaxconnect/ViApplication.java:113`
  `Locale locale2 = Locale.getDefault();`
- `sources/com/viwave/rossmaxconnect/datastore/vital/Vital.java:212`
  `this.deviceRecKey = new Timestamp(new Date(deviceRecKey.toDate().getTime() + ((long) TimeZone.getDefault().getRawOffset())));`
- `sources/kotlin/text/StringsKt__StringsJVMKt.java:163`
  `@Deprecated(message = "Use uppercase() instead.", replaceWith = @ReplaceWith(expression = "uppercase(Locale.getDefault())", imports = {"java.util.Locale"}))`
- `sources/kotlin/text/StringsKt__StringsJVMKt.java:179`
  `@Deprecated(message = "Use lowercase() instead.", replaceWith = @ReplaceWith(expression = "lowercase(Locale.getDefault())", imports = {"java.util.Locale"}))`
- `sources/kotlin/text/StringsKt__StringsJVMKt.java:676`
  `@Deprecated(message = "Use replaceFirstChar instead.", replaceWith = @ReplaceWith(expression = "replaceFirstChar { if (it.isLowerCase()) it.titlecase(Locale.getDefault()) else it.toString() }", imports = {"java.util.Locale"}))`
- `sources/kotlin/text/StringsKt__StringsJVMKt.java:680`
  `Locale locale = Locale.getDefault();`
- `sources/kotlin/text/StringsKt__StringsJVMKt.java:715`
  `@Deprecated(message = "Use replaceFirstChar instead.", replaceWith = @ReplaceWith(expression = "replaceFirstChar { it.lowercase(Locale.getDefault()) }", imports = {"java.util.Locale"}))`

## BR016

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/AndroidManifest.xml:270`
  `android:name="com.facebook.CurrentAccessTokenExpirationBroadcastReceiver"`
- `resources/AndroidManifest.xml:273`
  `<action android:name="com.facebook.sdk.ACTION_CURRENT_ACCESS_TOKEN_CHANGED"/>`
- `resources/res/values/public.xml:7028`
  `<public type="string" name="google_api_key" id="0x7f13015d" />`
- `resources/res/values/public.xml:7030`
  `<public type="string" name="google_crash_reporting_api_key" id="0x7f13015f" />`
- `resources/res/values/strings.xml:352`
  `<string name="google_api_key">AIzaSyDa8BZDOjNFq8pND-PB7ZaJPEVeuDtn0IE</string>`
- `resources/res/values/strings.xml:354`
  `<string name="google_crash_reporting_api_key">AIzaSyDa8BZDOjNFq8pND-PB7ZaJPEVeuDtn0IE</string>`
- `sources/com/facebook/AccessToken.java:28`
  `/* JADX INFO: compiled from: AccessToken.kt */`
- `sources/com/facebook/AccessToken.java:30`
  `@Metadata(d1 = {"\u0000j\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0003\n\u0002\u0010\u001e\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\"\n\u0002\b\u0007\n\u0002\u0010\u000b\n\u...`
- `sources/com/facebook/AccessToken.java:31`
  `public final class AccessToken implements Parcelable {`
- `sources/com/facebook/AccessToken.java:32`
  `public static final String ACCESS_TOKEN_KEY = "access_token";`
- `sources/com/facebook/AccessToken.java:34`
  `public static final Parcelable.Creator<AccessToken> CREATOR;`
- `sources/com/facebook/AccessToken.java:41`
  `private static final AccessTokenSource DEFAULT_ACCESS_TOKEN_SOURCE;`
- `sources/com/facebook/AccessToken.java:68`
  `/* JADX INFO: compiled from: AccessToken.kt */`
- `sources/com/facebook/AccessToken.java:69`
  `@Metadata(d1 = {"\u0000\u001e\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\bf\u0018\u00002\u00020\u0001J\u0012\u0010\u0002\u001a\u00020\u00032\b\u0010\u0004\u001a\u0004\u0018\u00010\u0005H&J\u0012\u0010\u0...`
- `sources/com/facebook/AccessToken.java:70`
  `public interface AccessTokenCreationCallback {`
- `sources/com/facebook/AccessToken.java:76`
  `/* JADX INFO: compiled from: AccessToken.kt */`
- `sources/com/facebook/AccessToken.java:77`
  `@Metadata(d1 = {"\u0000\u001e\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\bf\u0018\u00002\u00020\u0001J\u0012\u0010\u0002\u001a\u00020\u00032\b\u0010\u0004\u001a\u0004\u0018\u00010\u0005H&J\u0012\u0010\u0...`
- `sources/com/facebook/AccessToken.java:78`
  `public interface AccessTokenRefreshCallback {`
- `sources/com/facebook/AccessToken.java:84`
  `/* JADX INFO: compiled from: AccessToken.kt */`
- `sources/com/facebook/AccessToken.java:90`
  `int[] iArr = new int[AccessTokenSource.values().length];`
- `sources/com/facebook/AccessToken.java:116`
  `public static final void createFromNativeLinkingIntent(Intent intent, String str, AccessTokenCreationCallback accessTokenCreationCallback) {`
- `sources/com/facebook/AccessToken.java:117`
  `INSTANCE.createFromNativeLinkingIntent(intent, str, accessTokenCreationCallback);`
- `sources/com/facebook/AccessToken.java:121`
  `public static final void expireCurrentAccessToken() {`
- `sources/com/facebook/AccessToken.java:122`
  `INSTANCE.expireCurrentAccessToken();`
- `sources/com/facebook/AccessToken.java:126`
  `public static final AccessToken getCurrentAccessToken() {`
- `sources/com/facebook/AccessToken.java:127`
  `return INSTANCE.getCurrentAccessToken();`
- `sources/com/facebook/AccessToken.java:131`
  `public static final boolean isCurrentAccessTokenActive() {`
- `sources/com/facebook/AccessToken.java:132`
  `return INSTANCE.isCurrentAccessTokenActive();`
- `sources/com/facebook/AccessToken.java:146`
  `public static final void refreshCurrentAccessTokenAsync() {`
- `sources/com/facebook/AccessToken.java:147`
  `INSTANCE.refreshCurrentAccessTokenAsync();`
- `sources/com/facebook/AccessToken.java:151`
  `public static final void refreshCurrentAccessTokenAsync(AccessTokenRefreshCallback accessTokenRefreshCallback) {`
- `sources/com/facebook/AccessToken.java:152`
  `INSTANCE.refreshCurrentAccessTokenAsync(accessTokenRefreshCallback);`
- `sources/com/facebook/AccessToken.java:156`
  `public static final void setCurrentAccessToken(AccessToken accessToken) {`
- `sources/com/facebook/AccessToken.java:157`
  `INSTANCE.setCurrentAccessToken(accessToken);`
- `sources/com/facebook/AccessToken.java:307`
  `if (FacebookSdk.isLoggingBehaviorEnabled(LoggingBehavior.INCLUDE_ACCESS_TOKENS)) {`
- `sources/com/facebook/AccessToken.java:310`
  `return "ACCESS_TOKEN_REMOVED";`
- `sources/com/facebook/AccessToken.java:388`
  `/* JADX INFO: compiled from: AccessToken.kt */`
- `sources/com/facebook/AccessToken.java:389`
  `@Metadata(d1 = {"\u0000n\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0012\n\u0002\u0010 \n\u0000\n\u0002\u0018\u0...`
- `sources/com/facebook/AccessToken.java:445`
  `public final void createFromNativeLinkingIntent(Intent intent, final String applicationId, final AccessTokenCreationCallback accessTokenCallback) {`
- `sources/com/facebook/AccessToken.java:448`
  `Intrinsics.checkNotNullParameter(accessTokenCallback, "accessTokenCallback");`
- `sources/com/facebook/AccessToken.java:450`
  `accessTokenCallback.onError(new FacebookException("No extras found on intent"));`
- `sources/com/facebook/AccessTokenCache.java:13`
  `/* JADX INFO: compiled from: AccessTokenCache.kt */`
- `sources/com/facebook/AccessTokenCache.java:15`
  `@Metadata(d1 = {"\u00008\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010\u0002\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0007\b\u0000\u0018\u0000...`
- `sources/com/facebook/AccessTokenCache.java:16`
  `public final class AccessTokenCache {`
- `sources/com/facebook/AccessTokenCache.java:17`
  `public static final String CACHED_ACCESS_TOKEN_KEY = "com.facebook.AccessTokenManager.CachedAccessToken";`
- `sources/com/facebook/AccessTokenCache.java:22`
  `public AccessTokenCache(SharedPreferences sharedPreferences, SharedPreferencesTokenCachingStrategyFactory tokenCachingStrategyFactory) {`
- `sources/com/facebook/AccessTokenCache.java:54`
  `public AccessTokenCache() {`
- `sources/com/facebook/AccessTokenCache.java:55`
  `SharedPreferences sharedPreferences = FacebookSdk.getApplicationContext().getSharedPreferences("com.facebook.AccessTokenManager.SharedPreferences", 0);`
- `sources/com/facebook/AccessTokenCache.java:118`
  `/* JADX INFO: compiled from: AccessTokenCache.kt */`
- `sources/com/facebook/AccessTokenCache.java:119`
  `@Metadata(d1 = {"\u0000\u0012\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\b\u0000\u0018\u00002\u00020\u0001B\u0005¢\u0006\u0002\u0010\u0002J\u0006\u0010\u0003\u001a\u00020\u0004¨\u0006\u0005"}, d2 = {"Lcom/facebook/AccessTokenCache$SharedPreferencesTokenCachin...`
- `sources/com/facebook/AccessTokenManager.java:27`
  `/* JADX INFO: compiled from: AccessTokenManager.kt */`
- `sources/com/facebook/AccessTokenManager.java:29`
  `@Metadata(d1 = {"\u0000D\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0007\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0002\b\u0002...`
- `sources/com/facebook/AccessTokenManager.java:30`
  `public final class AccessTokenManager {`
- `sources/com/facebook/AccessTokenManager.java:31`
  `public static final String ACTION_CURRENT_ACCESS_TOKEN_CHANGED = "com.facebook.sdk.ACTION_CURRENT_ACCESS_TOKEN_CHANGED";`
- `sources/com/facebook/AccessTokenManager.java:35`
  `public static final String EXTRA_NEW_ACCESS_TOKEN = "com.facebook.sdk.EXTRA_NEW_ACCESS_TOKEN";`
- `sources/com/facebook/AccessTokenManager.java:36`
  `public static final String EXTRA_OLD_ACCESS_TOKEN = "com.facebook.sdk.EXTRA_OLD_ACCESS_TOKEN";`
- `sources/com/facebook/AccessTokenManager.java:38`
  `public static final String SHARED_PREFERENCES_NAME = "com.facebook.AccessTokenManager.SharedPreferences";`
- `sources/com/facebook/AccessTokenManager.java:39`
  `public static final String TAG = "AccessTokenManager";`
- `sources/com/facebook/AccessTokenManager.java:42`
  `private static AccessTokenManager instanceField;`
- `sources/com/facebook/AccessTokenManager.java:43`
  `private final AccessTokenCache accessTokenCache;`
- `sources/com/facebook/AccessTokenManager.java:44`
  `private AccessToken currentAccessTokenField;`
- `sources/com/facebook/AccessTokenManager.java:49`
  `/* JADX INFO: compiled from: AccessTokenManager.kt */`
- `sources/com/facebook/AccessTokenManager.java:50`
  `@Metadata(d1 = {"\u0000\u0012\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0005\bf\u0018\u00002\u00020\u0001R\u0012\u0010\u0002\u001a\u00020\u0003X¦\u0004¢\u0006\u0006\u001a\u0004\b\u0004\u0010\u0005R\u0012\u0010\u0006\u001a\u00020\u0003X¦\u0004¢\u0006\u0006\u001a\u...`
- `sources/com/facebook/AccessTokenManager.java:51`
  `public interface RefreshTokenInfo {`
- `sources/com/facebook/AccessTokenManager.java:58`
  `public static final AccessTokenManager getInstance() {`
- `sources/com/facebook/AccessTokenManager.java:62`
  `public AccessTokenManager(LocalBroadcastManager localBroadcastManager, AccessTokenCache accessTokenCache) {`
- `sources/com/facebook/AccessTokenManager.java:64`
  `Intrinsics.checkNotNullParameter(accessTokenCache, "accessTokenCache");`
- `sources/com/facebook/AccessTokenManager.java:66`
  `this.accessTokenCache = accessTokenCache;`
- `sources/com/facebook/AccessTokenManager.java:80`
  `/* JADX INFO: compiled from: AccessTokenManager.kt */`
- `sources/com/facebook/AccessTokenManager.java:81`
  `@Metadata(d1 = {"\u0000\u0014\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0005\u0018\u00002\u00020\u0001B\u0005¢\u0006\u0002\u0010\u0002R\u0014\u0010\u0003\u001a\u00020\u0004X\u0096D¢\u0006\b\n\u0000\u001a\u0004\b\u0005\u0010\u0006R\u0014\u0010\u0007\u001a\...`
- `sources/com/facebook/AccessTokenManager.java:82`
  `public static final class FacebookRefreshTokenInfo implements RefreshTokenInfo {`
- `sources/com/facebook/AccessTokenManager.java:83`
  `private final String graphPath = "oauth/access_token";`
- `sources/com/facebook/AccessTokenManager.java:86`
  `@Override // com.facebook.AccessTokenManager.RefreshTokenInfo`
- `sources/com/facebook/AccessTokenManager.java:97`
  `/* JADX INFO: compiled from: AccessTokenManager.kt */`
- `sources/com/facebook/AccessTokenManager.java:98`
  `@Metadata(d1 = {"\u0000\u0014\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0005\u0018\u00002\u00020\u0001B\u0005¢\u0006\u0002\u0010\u0002R\u0014\u0010\u0003\u001a\u00020\u0004X\u0096D¢\u0006\b\n\u0000\u001a\u0004\b\u0005\u0010\u0006R\u0014\u0010\u0007\u001a\...`
- `sources/com/facebook/AccessTokenManager.java:99`
  `public static final class InstagramRefreshTokenInfo implements RefreshTokenInfo {`
- `sources/com/facebook/AccessTokenManager.java:100`
  `private final String graphPath = "refresh_access_token";`
- `sources/com/facebook/AccessTokenManager.java:101`
  `private final String grantType = "ig_refresh_token";`
- `sources/com/facebook/AccessTokenManager.java:103`
  `@Override // com.facebook.AccessTokenManager.RefreshTokenInfo`
- `sources/com/facebook/AccessTokenManager.java:188`
  `/* JADX INFO: compiled from: AccessTokenManager.kt */`

## BR017

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `sources/androidx/credentials/webauthn/AuthenticatorAssertionResponse.java:100`
  `MessageDigest messageDigest = MessageDigest.getInstance("SHA-256");`
- `sources/androidx/credentials/webauthn/AuthenticatorAssertionResponse.java:103`
  `byte[] rpHash = messageDigest.digest(bytes);`
- `sources/androidx/credentials/webauthn/AuthenticatorAssertionResponse.java:122`
  `MessageDigest messageDigest = MessageDigest.getInstance("SHA-256");`
- `sources/androidx/credentials/webauthn/AuthenticatorAssertionResponse.java:129`
  `bArrDigest = messageDigest.digest(bytes);`
- `sources/androidx/credentials/webauthn/AuthenticatorAttestationResponse.java:97`
  `MessageDigest messageDigest = MessageDigest.getInstance("SHA-256");`
- `sources/androidx/credentials/webauthn/AuthenticatorAttestationResponse.java:100`
  `byte[] rpHash = messageDigest.digest(bytes);`
- `sources/com/facebook/appevents/internal/HashUtils.java:56`
  `MessageDigest messageDigest = MessageDigest.getInstance(MD5);`
- `sources/com/facebook/appevents/internal/HashUtils.java:61`
  `messageDigest.update(bArr, 0, i);`
- `sources/com/facebook/internal/Utility.java:89`
  `@Metadata(d1 = {"\u0000\u009a\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\b\n\u0002\b\f\n\u0002\u0010\t\n\u0002\b\n\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0007\n\u0002\u0010\u000b\n\u0002\b\u0010\n\u0002\u0010\u0...`
- `sources/com/facebook/internal/Utility.java:229`
  `MessageDigest hash = MessageDigest.getInstance(algorithm);`
- `sources/com/facebook/internal/security/OidcSecurityUtil.java:133`
  `PublicKey publicKeyGeneratePublic = KeyFactory.getInstance("RSA").generatePublic(new X509EncodedKeySpec(bArrDecode));`
- `sources/com/facebook/login/PKCEUtil.java:69`
  `MessageDigest messageDigest = MessageDigest.getInstance("SHA-256");`
- `sources/com/facebook/login/PKCEUtil.java:70`
  `messageDigest.update(bytes, 0, bytes.length);`
- `sources/com/facebook/login/PKCEUtil.java:71`
  `String strEncodeToString = Base64.encodeToString(messageDigest.digest(), 11);`
- `sources/com/google/android/gms/common/zzn.java:49`
  `Preconditions.checkNotNull(messageDigestZza);`
- `sources/com/google/android/gms/common/zzn.java:50`
  `return String.format("%s: pkg=%s, sha256=%s, atk=%s, ver=%s", str2, str, Hex.bytesToStringLowercase(messageDigestZza.digest(zzjVar.zzf())), Boolean.valueOf(z), "12451000.false");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzaem.java:11`
  `String str2 = new String(MessageDigest.getInstance("SHA-256").digest(str.getBytes()));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzafu.java:62`
  `MessageDigest messageDigest = MessageDigest.getInstance("SHA-256");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzafu.java:63`
  `messageDigest.update(str3.getBytes(StandardCharsets.UTF_8));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzafu.java:64`
  `String strSubstring = Base64.encodeToString(Arrays.copyOf(messageDigest.digest(), 9), 3).substring(0, 11);`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzdh.java:35`
  `throw new GeneralSecurityException("AES key size must be 16 or 32 bytes");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzdw.java:32`
  `throw new GeneralSecurityException("192 bit AES GCM Parameters are not valid");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzec.java:32`
  `throw new GeneralSecurityException("Registering AES GCM SIV is not supported in FIPS mode");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzgt.java:16`
  `return zzzd.zza.zza("AES/GCM/NoPadding");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzgu.java:8`
  `import javax.crypto.spec.IvParameterSpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzgu.java:9`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzhc.java:10`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzhk.java:10`
  `import javax.crypto.spec.IvParameterSpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzhk.java:11`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzhk.java:83`
  `IvParameterSpec ivParameterSpec = new IvParameterSpec(bArr4);`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzhk.java:85`
  `cipher.init(2, this.zzf, ivParameterSpec);`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzhr.java:17`
  `throw new GeneralSecurityException("Can not use AES-GCM in FIPS-mode, as BoringCrypto module is not available.");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzhv.java:8`
  `import java.security.MessageDigest;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzhv.java:58`
  `if (!MessageDigest.isEqual(zzib.zza(zza(bArr), zza(bArr2, byteBuffer)), bArr3)) {`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzhy.java:8`
  `import javax.crypto.spec.IvParameterSpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzhy.java:9`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzij.java:8`
  `import javax.crypto.spec.IvParameterSpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzij.java:9`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzij.java:55`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(zzhs.zza(this.zzb, bArr4), "ChaCha20");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzij.java:56`
  `IvParameterSpec ivParameterSpec = new IvParameterSpec(zza(bArr4));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzij.java:58`
  `cipherZza.init(2, secretKeySpec, ivParameterSpec);`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzly.java:26`
  `macZza.init(new SecretKeySpec(bArr, this.zza));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzly.java:49`
  `macZza.init(new SecretKeySpec(new byte[macZza.getMacLength()], this.zza));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzly.java:51`
  `macZza.init(new SecretKeySpec(bArr2, this.zza));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zznb.java:30`
  `Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zznb.java:42`
  `Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zznj.java:6`
  `import java.security.MessageDigest;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzsh.java:13`
  `throw new GeneralSecurityException("Can not use AES-CMAC in FIPS-mode.");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyl.java:6`
  `import javax.crypto.spec.IvParameterSpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyl.java:7`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyl.java:14`
  `private final SecretKeySpec zzc;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyl.java:36`
  `IvParameterSpec ivParameterSpec = new IvParameterSpec(bArr4);`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyl.java:38`
  `cipher.init(1, this.zzc, ivParameterSpec);`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyl.java:40`
  `cipher.init(2, this.zzc, ivParameterSpec);`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyn.java:11`
  `import javax.crypto.spec.IvParameterSpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyn.java:12`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyn.java:23`
  `private final SecretKeySpec zzg;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyn.java:45`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(bArr, "AES");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyn.java:46`
  `this.zzg = secretKeySpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyn.java:48`
  `cipher.init(1, secretKeySpec);`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyn.java:110`
  `cipher2.init(1, this.zzg, new IvParameterSpec(bArrZza2));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyo.java:16`
  `return zzzd.zza.zza("AES/CTR/NoPadding");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyp.java:16`
  `return zzzd.zza.zza("AES/CTR/NOPADDING");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyq.java:16`
  `return zzzd.zza.zza("AES/ECB/NOPADDING");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyr.java:11`
  `import javax.crypto.spec.IvParameterSpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyr.java:12`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyr.java:59`
  `cipher.init(2, new SecretKeySpec(this.zzf, "AES"), new IvParameterSpec(bArr5));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyu.java:16`
  `return zzzd.zza.zza("AES/CTR/NoPadding");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyx.java:24`
  `macZza.init(new SecretKeySpec(new byte[macZza.getMacLength()], str));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyx.java:26`
  `macZza.init(new SecretKeySpec(bArr2, str));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyx.java:29`
  `macZza.init(new SecretKeySpec(macZza.doFinal(bArrZza), str));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyy.java:34`
  `return "HmacSha1";`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyy.java:37`
  `return "HmacSha224";`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzzt.java:9`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzzt.java:29`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(bArr, "AES");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzzt.java:30`
  `this.zzc = secretKeySpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzzt.java:32`
  `cipherZza.init(1, secretKeySpec);`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzzw.java:16`
  `return zzzd.zza.zza("AES/ECB/NoPadding");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzzx.java:9`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzzx.java:41`
  `this.zzb = new zzzv("HMAC" + String.valueOf(((zzrj) ((zzrm) zzrcVar.zza())).zze()), new SecretKeySpec(zzrcVar.zzf().zza(zzbj.zza()), "HMAC"));`

## BR018

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/com/android/installreferrer/api/InstallReferrerClient.java:12`
  `public @interface InstallReferrerResponse {`
- `sources/com/facebook/share/model/ShareMediaContent.java:60`
  `ArrayList arrayListEmptyList;`
- `sources/com/facebook/share/model/ShareMediaContent.java:65`
  `arrayListEmptyList = CollectionsKt.emptyList();`
- `sources/com/facebook/share/model/ShareMediaContent.java:74`
  `arrayListEmptyList = arrayList;`
- `sources/com/facebook/share/model/ShareMediaContent.java:76`
  `this.media = arrayListEmptyList;`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:18`
  `@Metadata(d1 = {"\u0000B\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u000b\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010\u0002\n\u0002\b\u0002\n\u0002\u00...`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:24`
  `private final WebviewHeightRatio webviewHeightRatio;`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:41`
  `@Metadata(d1 = {"\u0000\f\n\u0002\u0018\u0002\n\u0002\u0010\u0010\n\u0002\b\u0005\b\u0086\u0001\u0018\u00002\b\u0012\u0004\u0012\u00020\u00000\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002j\u0002\b\u0003j\u0002\b\u0004j\u0002\b\u0005¨\u0006\u0006"}, d2 = {"Lcom/facebook/share/model/ShareMessengerURL...`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:42`
  `public enum WebviewHeightRatio {`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:43`
  `WebviewHeightRatioFull,`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:44`
  `WebviewHeightRatioTall,`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:45`
  `WebviewHeightRatioCompact`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:68`
  `public final WebviewHeightRatio getWebviewHeightRatio() {`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:69`
  `return this.webviewHeightRatio;`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:82`
  `this.webviewHeightRatio = builder.getWebviewHeightRatio();`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:93`
  `this.webviewHeightRatio = (WebviewHeightRatio) parcel.readSerializable();`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:104`
  `dest.writeSerializable(this.webviewHeightRatio);`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:109`
  `@Metadata(d1 = {"\u0000(\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u000b\n\u0002\b\u000b\n\u0002\u0018\u0002\n\u0002\b\r\u0018\u00002\u000e\u0012\u0004\u0012\u00020\u0002\u0012\u0004\u0012\u00020\u00000\u0001B\u0005¢...`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:115`
  `private WebviewHeightRatio webviewHeightRatio;`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:144`
  `/* JADX INFO: renamed from: getWebviewHeightRatio$facebook_common_release, reason: from getter */`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:145`
  `public final WebviewHeightRatio getWebviewHeightRatio() {`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:146`
  `return this.webviewHeightRatio;`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:149`
  `public final void setWebviewHeightRatio$facebook_common_release(WebviewHeightRatio webviewHeightRatio) {`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:150`
  `this.webviewHeightRatio = webviewHeightRatio;`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:177`
  `public final Builder setWebviewHeightRatio(WebviewHeightRatio webviewHeightRatio) {`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:178`
  `this.webviewHeightRatio = webviewHeightRatio;`
- `sources/com/facebook/share/model/ShareMessengerURLActionButton.java:189`
  `return model == null ? this : setUrl(model.getUrl()).setIsMessengerExtensionURL(model.isMessengerExtensionURL()).setFallbackUrl(model.getFallbackUrl()).setWebviewHeightRatio(model.getWebviewHeightRatio()).setShouldHideWebviewShareButton(model.getShouldHideWebviewShareButton());`
- `sources/com/google/android/gms/auth/api/R.java:43`
  `public static int fontWeight = 0x7f040288;`
- `sources/com/google/android/gms/auth/api/R.java:97`
  `public static int compat_notification_large_icon_max_height = 0x7f070073;`
- `sources/com/google/android/gms/auth/api/R.java:104`
  `public static int notification_large_icon_height = 0x7f07035b;`
- `sources/com/google/android/gms/auth/api/R.java:157`
  `public static int notification_template_icon_bg = 0x7f0803c3;`
- `sources/com/google/android/gms/auth/api/R.java:158`
  `public static int notification_template_icon_low_bg = 0x7f0803c4;`
- `sources/com/google/android/gms/auth/api/R.java:206`
  `public static int adjust_height = 0x7f0900a1;`
- `sources/com/google/android/gms/auth/api/R.java:300`
  `public static int notification_template_big_media = 0x7f0c00fa;`
- `sources/com/google/android/gms/auth/api/R.java:301`
  `public static int notification_template_big_media_custom = 0x7f0c00fb;`
- `sources/com/google/android/gms/auth/api/R.java:302`
  `public static int notification_template_big_media_narrow = 0x7f0c00fc;`
- `sources/com/google/android/gms/auth/api/R.java:303`
  `public static int notification_template_big_media_narrow_custom = 0x7f0c00fd;`
- `sources/com/google/android/gms/auth/api/R.java:304`
  `public static int notification_template_custom_big = 0x7f0c00fe;`
- `sources/com/google/android/gms/auth/api/R.java:305`
  `public static int notification_template_icon_group = 0x7f0c00ff;`
- `sources/com/google/android/gms/auth/api/R.java:306`
  `public static int notification_template_lines_media = 0x7f0c0100;`

## BR019

paper_id: B011
paper_title: Locking it down: The privacy and security of mobile medication apps

- `sources/androidx/appcompat/widget/ActivityChooserModel.java:403`
  `map.put(new ComponentName(activityResolveInfo.resolveInfo.activityInfo.packageName, activityResolveInfo.resolveInfo.activityInfo.name), activityResolveInfo);`
- `sources/androidx/constraintlayout/core/state/ConstraintSetParser.java:512`
  `layoutVariables.put(str, layoutVariables.get(cLObject2.get(TypedValues.TransitionType.S_FROM)), layoutVariables.get(cLObject2.get("to")), 1.0f, cLObject2.getStringOrNull("prefix"), cLObject2.getStringOrNull("postfix"));`
- `sources/androidx/constraintlayout/core/state/ConstraintSetParser.java:514`
  `layoutVariables.put(str, layoutVariables.get(cLObject2.get(TypedValues.TransitionType.S_FROM)), layoutVariables.get(cLObject2.get("step")));`
- `sources/androidx/constraintlayout/core/state/helpers/ChainReference.java:49`
  `this.mMapWeights.put(string, Float.valueOf(f));`
- `sources/androidx/constraintlayout/core/state/helpers/ChainReference.java:52`
  `this.mMapPreMargin.put(string, Float.valueOf(f2));`
- `sources/androidx/constraintlayout/core/state/helpers/ChainReference.java:69`
  `this.mMapPostGoneMargin.put(string, Float.valueOf(f5));`
- `sources/androidx/constraintlayout/core/state/helpers/FlowReference.java:71`
  `this.mMapWeights.put(str, Float.valueOf(f));`
- `sources/androidx/constraintlayout/core/state/helpers/FlowReference.java:85`
  `this.mMapPostMargin.put(str, Float.valueOf(f3));`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:906`
  `sparseArray.put(childAt.getId(), this.mFrameArrayList.get(childAt));`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:1467`
  `sparseArray.put(MotionLayout.this.getId(), constraintWidgetContainer);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:664`
  `this.mTempMapIdToWidget.put(0, this.mLayoutWidget);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:665`
  `this.mTempMapIdToWidget.put(getId(), this.mLayoutWidget);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:668`
  `this.mTempMapIdToWidget.put(childAt4.getId(), getViewWidget(childAt4));`
- `sources/androidx/coordinatorlayout/widget/DirectedAcyclicGraph.java:34`
  `this.mGraph.put(t, emptyList);`
- `sources/androidx/core/graphics/TypefaceCompatApi24Impl.java:102`
  `simpleArrayMap.put(uri, byteBufferMmap);`
- `sources/androidx/core/location/LocationManagerCompat.java:116`
  `WeakReference<LocationListenerTransport> weakReferencePut = sLocationListeners.put(locationListenerTransport.getKey(), new WeakReference<>(locationListenerTransport));`
- `sources/androidx/core/location/LocationManagerCompat.java:210`
  `GnssListenersHolder.sGnssMeasurementListeners.put(callback, gnssMeasurementsTransport);`
- `sources/androidx/core/location/LocationManagerCompat.java:942`
  `GnssListenersHolder.sGnssStatusListeners.put(callback, gnssStatusTransport);`
- `sources/androidx/core/location/LocationManagerCompat.java:1045`
  `GnssListenersHolder.sGnssStatusListeners.put(callback, preRGnssStatusTransport);`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/CredentialProviderCreatePublicKeyCredentialController.java:363`
  `String json = response.toJson();`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/CredentialProviderCreatePublicKeyCredentialController.java:364`
  `Intrinsics.checkNotNullExpressionValue(json, "response.toJson()");`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:119`
  `@Metadata(d1 = {"\u0000\u0096\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u000e\n\u0002\bH\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0000\n\u0002\u0010\u0012\n\u0002\b...`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:288`
  `public final void addAuthenticatorAttestationResponse$credentials_play_services_auth_release(byte[] clientDataJSON, byte[] attestationObject, String[] transportArray, JSONObject json) throws JSONException {`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:293`
  `JSONObject jSONObject = new JSONObject();`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:294`
  `jSONObject.put(getJSON_KEY_CLIENT_DATA$credentials_play_services_auth_release(), b64Encode(clientDataJSON));`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:295`
  `jSONObject.put(getJSON_KEY_ATTESTATION_OBJ$credentials_play_services_auth_release(), b64Encode(attestationObject));`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:296`
  `jSONObject.put(getJSON_KEY_TRANSPORTS$credentials_play_services_auth_release(), new JSONArray(transportArray));`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:297`
  `json.put(getJSON_KEY_RESPONSE$credentials_play_services_auth_release(), jSONObject);`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:302`
  `JSONObject jSONObject = new JSONObject();`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:314`
  `String json = publicKeyCredential.toJson();`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:315`
  `Intrinsics.checkNotNullExpressionValue(json, "publicKeyCred.toJson()");`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:322`
  `String string = jSONObject.toString();`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:459`
  `if (jSONObject.has(getJSON_KEY_TRANSPORTS$credentials_play_services_auth_release())) {`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:461`
  `JSONArray jSONArray2 = jSONObject.getJSONArray(getJSON_KEY_TRANSPORTS$credentials_play_services_auth_release());`
- `sources/androidx/credentials/webauthn/AuthenticatorAssertionResponse.java:13`
  `import org.json.JSONObject;`
- `sources/androidx/credentials/webauthn/AuthenticatorAssertionResponse.java:17`
  `@Metadata(d1 = {"\u0000,\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0012\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\u000b\n\u0002\b\r\n\u0002\u0018\u0002\n\u0002\b\u000b\b\u0007\u0018\u00002\u00020\u0001B]\u0012\u0006\u0010\u0002\u001a\u00020\u0...`
- `sources/androidx/credentials/webauthn/AuthenticatorAssertionResponse.java:64`
  `public JSONObject getClientJson() {`
- `sources/androidx/credentials/webauthn/AuthenticatorAssertionResponse.java:69`
  `public void setClientJson(JSONObject jSONObject) {`
- `sources/androidx/credentials/webauthn/AuthenticatorAssertionResponse.java:70`
  `Intrinsics.checkNotNullParameter(jSONObject, "<set-?>");`
- `sources/androidx/credentials/webauthn/AuthenticatorAssertionResponse.java:71`
  `this.clientJson = jSONObject;`

## BR020

paper_id: B012
paper_title: Reviewing the data security and privacy policies of mobile apps for depression

- `sources/androidx/appcompat/widget/SearchView.java:97`
  `CursorAdapter mSuggestionsAdapter;`
- `sources/androidx/core/provider/FontProvider.java:78`
  `Cursor cursorQuery = contentQueryWrapperMake.query(uriBuild, new String[]{"_id", FontsContractCompat.Columns.FILE_ID, FontsContractCompat.Columns.TTC_INDEX, FontsContractCompat.Columns.VARIATION_SETTINGS, FontsContractCompat.Columns.WEIGHT, FontsContractCompat.Columns.ITALIC, FontsContractCompat.Col...`
- `sources/androidx/core/provider/FontProvider.java:79`
  `if (cursorQuery != null) {`
- `sources/androidx/core/provider/FontProvider.java:81`
  `if (cursorQuery.getCount() > 0) {`
- `sources/androidx/core/provider/FontProvider.java:82`
  `int columnIndex = cursorQuery.getColumnIndex(FontsContractCompat.Columns.RESULT_CODE);`
- `sources/androidx/core/provider/FontProvider.java:84`
  `int columnIndex2 = cursorQuery.getColumnIndex("_id");`
- `sources/androidx/core/provider/FontProvider.java:85`
  `int columnIndex3 = cursorQuery.getColumnIndex(FontsContractCompat.Columns.FILE_ID);`
- `sources/androidx/core/provider/FontProvider.java:86`
  `int columnIndex4 = cursorQuery.getColumnIndex(FontsContractCompat.Columns.TTC_INDEX);`
- `sources/androidx/core/provider/FontProvider.java:87`
  `int columnIndex5 = cursorQuery.getColumnIndex(FontsContractCompat.Columns.WEIGHT);`
- `sources/androidx/core/provider/FontProvider.java:88`
  `int columnIndex6 = cursorQuery.getColumnIndex(FontsContractCompat.Columns.ITALIC);`
- `sources/androidx/core/provider/FontProvider.java:89`
  `while (cursorQuery.moveToNext()) {`
- `sources/androidx/core/provider/FontProvider.java:90`
  `int i2 = columnIndex != -1 ? cursorQuery.getInt(columnIndex) : i;`
- `sources/androidx/core/provider/FontProvider.java:91`
  `int i3 = columnIndex4 != -1 ? cursorQuery.getInt(columnIndex4) : i;`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:13`
  `private static final String CREATE_CONTEXTS_SQL_V1 = "CREATE TABLE transport_contexts (_id INTEGER PRIMARY KEY, backend_name TEXT NOT NULL, priority INTEGER NOT NULL, next_request_ms INTEGER NOT NULL)";`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:15`
  `private static final String CREATE_EVENTS_SQL_V1 = "CREATE TABLE events (_id INTEGER PRIMARY KEY, context_id INTEGER NOT NULL, transport_name TEXT NOT NULL, timestamp_ms INTEGER NOT NULL, uptime_ms INTEGER NOT NULL, payload BLOB NOT NULL, code INTEGER, num_attempts INTEGER NOT NULL,FOREIGN KEY (cont...`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:17`
  `private static final String CREATE_EVENT_METADATA_SQL_V1 = "CREATE TABLE event_metadata (_id INTEGER PRIMARY KEY, event_id INTEGER NOT NULL, name TEXT NOT NULL, value TEXT NOT NULL,FOREIGN KEY (event_id) REFERENCES events(_id) ON DELETE CASCADE)";`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:18`
  `private static final String CREATE_GLOBAL_LOG_EVENT_STATE_TABLE = "CREATE TABLE global_log_event_state (last_metrics_upload_ms BIGINT PRIMARY KEY)";`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:19`
  `private static final String CREATE_LOG_EVENT_DROPPED_TABLE = "CREATE TABLE log_event_dropped (log_source VARCHAR(45) NOT NULL,reason INTEGER NOT NULL,events_dropped_count BIGINT NOT NULL,PRIMARY KEY(log_source, reason))";`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:20`
  `private static final String CREATE_PAYLOADS_TABLE_V4 = "CREATE TABLE event_payloads (sequence_num INTEGER NOT NULL, event_id INTEGER NOT NULL, bytes BLOB NOT NULL,FOREIGN KEY (event_id) REFERENCES events(_id) ON DELETE CASCADE,PRIMARY KEY (sequence_num, event_id))";`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:63`
  `sQLiteDatabase.execSQL("ALTER TABLE events ADD COLUMN payload_encoding TEXT");`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:84`
  `sQLiteDatabase.execSQL("ALTER TABLE events ADD COLUMN product_id INTEGER");`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:102`
  `sQLiteDatabase.execSQL(CREATE_EVENT_BACKEND_INDEX_V1);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:103`
  `sQLiteDatabase.execSQL(CREATE_CONTEXT_BACKEND_PRIORITY_INDEX_V1);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:107`
  `sQLiteDatabase.execSQL("ALTER TABLE transport_contexts ADD COLUMN extras BLOB");`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:108`
  `sQLiteDatabase.execSQL("CREATE UNIQUE INDEX contexts_backend_priority_extras on transport_contexts(backend_name, priority, extras)");`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:109`
  `sQLiteDatabase.execSQL("DROP INDEX contexts_backend_priority");`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:113`
  `sQLiteDatabase.execSQL("ALTER TABLE events ADD COLUMN inline BOOLEAN NOT NULL DEFAULT 1");`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:4`
  `import android.database.Cursor;`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:177`
  `return (Long) tryWithCursor(sQLiteDatabase.query("transport_contexts", new String[]{"_id"}, sb.toString(), (String[]) arrayList.toArray(new String[0]), null, null, null), new Function() { // from class: com.google.android.datatransport.runtime.scheduling.persistence.SQLiteEventStore$$ExternalSynthet...`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:180`
  `return SQLiteEventStore.lambda$getTransportContextId$2((Cursor) obj);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:185`
  `static /* synthetic */ Long lambda$getTransportContextId$2(Cursor cursor) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:186`
  `if (cursor.moveToNext()) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:187`
  `return Long.valueOf(cursor.getLong(0));`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:195`
  `final String str = "UPDATE events SET num_attempts = num_attempts + 1 WHERE _id in " + toIdList(iterable);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:209`
  `tryWithCursor(sQLiteDatabase.rawQuery(str2, null), new Function() { // from class: com.google.android.datatransport.runtime.scheduling.persistence.SQLiteEventStore$$ExternalSyntheticLambda27`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:212`
  `return this.f$0.m385x70a49c2a((Cursor) obj);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:220`
  `/* synthetic */ Object m385x70a49c2a(Cursor cursor) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:221`
  `while (cursor.moveToNext()) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:222`
  `recordLogEventDropped(cursor.getInt(0), LogEventDropped.Reason.MAX_RETRIES_REACHED, cursor.getString(1));`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:249`
  `return ((Long) tryWithCursor(getDb().rawQuery("SELECT next_request_ms FROM transport_contexts WHERE backend_name = ? and priority = ?", new String[]{transportContext.getBackendName(), String.valueOf(PriorityMapping.toInt(transportContext.getPriority()))}), new Function() { // from class: com.google....`

## BR021

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `resources/AndroidManifest.xml:253`
  `<provider`
- `resources/AndroidManifest.xml:265`
  `<provider`
- `resources/AndroidManifest.xml:283`
  `<provider`

## BR022

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `resources/res/xml/image_share_filepaths.xml:3`
  `<files-path`

## BR023

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `sources/androidx/startup/InitializationProvider.java:10`
  `public class InitializationProvider extends ContentProvider {`
- `sources/com/facebook/FacebookContentProvider.java:28`
  `public final class FacebookContentProvider extends ContentProvider {`
- `sources/com/facebook/internal/FacebookInitProvider.java:19`
  `public final class FacebookInitProvider extends ContentProvider {`
- `sources/com/google/android/gms/measurement/AppMeasurementContentProvider.java:15`
  `public class AppMeasurementContentProvider extends ContentProvider {`
- `sources/com/google/firebase/provider/FirebaseInitProvider.java:16`
  `public class FirebaseInitProvider extends ContentProvider {`

## BR024

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `sources/androidx/core/content/FileProvider.java:73`
  `if (!providerInfo.grantUriPermissions) {`
- `sources/androidx/core/content/IntentSanitizer.java:121`
  `consumer.accept("Allowing Extra Stream requires also allowing at least  FLAG_GRANT_READ_URI_PERMISSION Flag.");`
- `sources/androidx/core/content/IntentSanitizer.java:123`
  `consumer.accept("Allowing Extra Output requires also allowing FLAG_GRANT_READ_URI_PERMISSION and FLAG_GRANT_WRITE_URI_PERMISSION Flags.");`

## BR025

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:4`
  `import android.database.sqlite.SQLiteDatabase;`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:5`
  `import android.database.sqlite.SQLiteOpenHelper;`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:12`
  `final class SchemaManager extends SQLiteOpenHelper {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:42`
  `void upgrade(SQLiteDatabase sQLiteDatabase);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:48`
  `public final void upgrade(SQLiteDatabase sQLiteDatabase) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:49`
  `SchemaManager.lambda$static$0(sQLiteDatabase);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:55`
  `public final void upgrade(SQLiteDatabase sQLiteDatabase) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:56`
  `SchemaManager.lambda$static$1(sQLiteDatabase);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:62`
  `public final void upgrade(SQLiteDatabase sQLiteDatabase) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:63`
  `sQLiteDatabase.execSQL("ALTER TABLE events ADD COLUMN payload_encoding TEXT");`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:69`
  `public final void upgrade(SQLiteDatabase sQLiteDatabase) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:70`
  `SchemaManager.lambda$static$3(sQLiteDatabase);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:76`
  `public final void upgrade(SQLiteDatabase sQLiteDatabase) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:77`
  `SchemaManager.lambda$static$4(sQLiteDatabase);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:83`
  `public final void upgrade(SQLiteDatabase sQLiteDatabase) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:84`
  `sQLiteDatabase.execSQL("ALTER TABLE events ADD COLUMN product_id INTEGER");`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:90`
  `public final void upgrade(SQLiteDatabase sQLiteDatabase) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:91`
  `SchemaManager.lambda$static$6(sQLiteDatabase);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:99`
  `sQLiteDatabase.execSQL(CREATE_EVENTS_SQL_V1);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:100`
  `sQLiteDatabase.execSQL(CREATE_EVENT_METADATA_SQL_V1);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:101`
  `sQLiteDatabase.execSQL(CREATE_CONTEXTS_SQL_V1);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:102`
  `sQLiteDatabase.execSQL(CREATE_EVENT_BACKEND_INDEX_V1);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:103`
  `sQLiteDatabase.execSQL(CREATE_CONTEXT_BACKEND_PRIORITY_INDEX_V1);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:106`
  `static /* synthetic */ void lambda$static$1(SQLiteDatabase sQLiteDatabase) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:107`
  `sQLiteDatabase.execSQL("ALTER TABLE transport_contexts ADD COLUMN extras BLOB");`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:108`
  `sQLiteDatabase.execSQL("CREATE UNIQUE INDEX contexts_backend_priority_extras on transport_contexts(backend_name, priority, extras)");`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:109`
  `sQLiteDatabase.execSQL("DROP INDEX contexts_backend_priority");`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:112`
  `static /* synthetic */ void lambda$static$3(SQLiteDatabase sQLiteDatabase) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:113`
  `sQLiteDatabase.execSQL("ALTER TABLE events ADD COLUMN inline BOOLEAN NOT NULL DEFAULT 1");`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:114`
  `sQLiteDatabase.execSQL(DROP_PAYLOADS_SQL);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:115`
  `sQLiteDatabase.execSQL(CREATE_PAYLOADS_TABLE_V4);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:5`
  `import android.database.sqlite.SQLiteDatabase;`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:6`
  `import android.database.sqlite.SQLiteDatabaseLockedException;`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:72`
  `SQLiteDatabase getDb() {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:75`
  `return (SQLiteDatabase) retryIfDbLocked(new Producer() { // from class: com.google.android.datatransport.runtime.scheduling.persistence.SQLiteEventStore$$ExternalSyntheticLambda25`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:78`
  `return schemaManager.getWritableDatabase();`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:88`
  `static /* synthetic */ SQLiteDatabase lambda$getDb$0(Throwable th) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:98`
  `return this.f$0.m384x42ac2bf1(eventInternal, transportContext, (SQLiteDatabase) obj);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:108`
  `/* synthetic */ Long m384x42ac2bf1(EventInternal eventInternal, TransportContext transportContext, SQLiteDatabase sQLiteDatabase) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:113`
  `long jEnsureTransportContext = ensureTransportContext(sQLiteDatabase, transportContext);`

## BR026

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/androidx/constraintlayout/core/ArrayRow.java:5`
  `import com.facebook.appevents.UserDataStore;`
- `sources/androidx/constraintlayout/core/ArrayRow.java:276`
  `this.variables.put(linearSystem.createErrorVariable(i, UserDataStore.EMAIL), -1.0f);`
- `sources/androidx/core/text/util/FindAddress.java:3`
  `import com.facebook.appevents.UserDataStore;`
- `sources/androidx/core/text/util/FindAddress.java:73`
  `return lowerCase.equals(i3 % 100 != 11 ? UserDataStore.STATE : "th");`
- `sources/androidx/datastore/core/DataStoreImpl$transformAndWrite$2$newData$1.java:42`
  `jadx.core.utils.exceptions.JadxRuntimeException: Can't change immutable type java.lang.Object to androidx.datastore.core.DataStoreImpl$transformAndWrite$2$newData$1<T> for r3v3 'this'  java.lang.Object`
- `sources/androidx/datastore/core/MulticastFileObserver$Companion$observe$1.java:16`
  `@DebugMetadata(c = "androidx.datastore.core.MulticastFileObserver$Companion$observe$1", f = "MulticastFileObserver.android.kt", i = {0, 0}, l = {84, 85}, m = "invokeSuspend", n = {"$this$channelFlow", "disposeListener"}, s = {"L$0", "L$1"})`
- `sources/androidx/datastore/core/MulticastFileObserver$Companion$observe$1.java:82`
  `androidx.datastore.core.MulticastFileObserver$Companion r4 = androidx.datastore.core.MulticastFileObserver.INSTANCE`
- `sources/androidx/datastore/core/MulticastFileObserver$Companion$observe$1.java:86`
  `kotlinx.coroutines.DisposableHandle r1 = androidx.datastore.core.MulticastFileObserver.Companion.access$observe(r4, r5, r1)`
- `sources/androidx/datastore/core/MulticastFileObserver.java:24`
  `@Metadata(d1 = {"\u0000.\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0002\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010\b\n\u0002\b\u0002\b\u0000\u0018\u0000 \u000f2\u00020\u0001:\u0001\u000fB\u000f\b\...`
- `sources/androidx/datastore/core/MulticastFileObserver.java:57`
  `@Metadata(d1 = {"\u0000>\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0010%\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0...`
- `sources/androidx/datastore/core/MulticastFileObserver.java:63`
  `public static /* synthetic */ void getFileObservers$datastore_core_release$annotations() {`
- `sources/androidx/datastore/core/MulticastFileObserver.java:82`
  `Map<String, MulticastFileObserver> fileObservers$datastore_core_release = MulticastFileObserver.INSTANCE.getFileObservers$datastore_core_release();`
- `sources/androidx/datastore/core/MulticastFileObserver.java:84`
  `MulticastFileObserver multicastFileObserver = fileObservers$datastore_core_release.get(key);`
- `sources/androidx/datastore/core/MulticastFileObserver.java:96`
  `return new DisposableHandle() { // from class: androidx.datastore.core.MulticastFileObserver$Companion$$ExternalSyntheticLambda0`
- `sources/androidx/datastore/core/okio/OkioStorageConnection.java:282`
  `throw new UnsupportedOperationException("Method not decompiled: androidx.datastore.core.okio.OkioStorageConnection.writeScope(kotlin.jvm.functions.Function2, kotlin.coroutines.Continuation):java.lang.Object");`
- `sources/androidx/datastore/core/okio/OkioStorageConnection.java:291`
  `@Override // androidx.datastore.core.Closeable`
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
- `sources/androidx/datastore/preferences/protobuf/ByteString.java:109`
  `UNSIGNED_LEXICOGRAPHICAL_COMPARATOR = new Comparator<ByteString>() { // from class: androidx.datastore.preferences.protobuf.ByteString.2`
- `sources/androidx/datastore/preferences/protobuf/ByteString.java:110`
  `/* JADX WARN: Type inference failed for: r0v0, types: [androidx.datastore.preferences.protobuf.ByteString$ByteIterator] */`
- `sources/androidx/datastore/preferences/protobuf/ByteString.java:111`
  `/* JADX WARN: Type inference failed for: r3v1, types: [androidx.datastore.preferences.protobuf.ByteString$ByteIterator] */`
- `sources/androidx/datastore/preferences/protobuf/DescriptorProtos.java:15473`
  `@Override // androidx.datastore.preferences.protobuf.DescriptorProtos.UninterpretedOptionOrBuilder`
- `sources/androidx/datastore/preferences/protobuf/DescriptorProtos.java:15478`
  `@Override // androidx.datastore.preferences.protobuf.DescriptorProtos.UninterpretedOptionOrBuilder`
- `sources/androidx/datastore/preferences/protobuf/DescriptorProtos.java:15763`
  `@Override // androidx.datastore.preferences.protobuf.DescriptorProtos.UninterpretedOptionOrBuilder`
- `sources/androidx/datastore/preferences/protobuf/DescriptorProtos.java:15768`
  `@Override // androidx.datastore.preferences.protobuf.DescriptorProtos.UninterpretedOptionOrBuilder`
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
- `sources/androidx/datastore/preferences/protobuf/LazyStringArrayList.java:355`
  `@Override // androidx.datastore.preferences.protobuf.LazyStringList`

## BR027

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:120`
  `File file = new File(this.mAppContext.getFilesDir(), BrowserServiceFileProvider.FILE_SUB_DIR);`
- `sources/androidx/core/graphics/drawable/IconCompat.java:342`
  `return new FileInputStream(new File((String) this.mObj1));`
- `sources/androidx/core/util/AtomicFile.java:19`
  `this.mNewName = new File(file.getPath() + ".new");`
- `sources/androidx/core/util/AtomicFile.java:20`
  `this.mLegacyBackupName = new File(file.getPath() + ".bak");`
- `sources/androidx/datastore/migrations/SharedPreferencesMigration.java:387`
  `return new File(new File(context.getApplicationInfo().dataDir, "shared_prefs"), name + ".xml");`
- `sources/androidx/datastore/migrations/SharedPreferencesMigration.java:391`
  `return new File(prefsFile.getPath() + ".bak");`
- `sources/androidx/documentfile/provider/RawDocumentFile.java:30`
  `File file = new File(this.mFile, str2);`
- `sources/androidx/profileinstaller/ProfileInstaller.java:225`
  `String name = new File(applicationInfo.sourceDir).getName();`
- `sources/com/facebook/internal/instrument/InstrumentUtility.java:224`
  `return new JSONObject(Utility.readStreamToString(new FileInputStream(new File(instrumentReportDir, filename))));`
- `sources/com/facebook/internal/instrument/InstrumentUtility.java:241`
  `FileOutputStream fileOutputStream = new FileOutputStream(new File(instrumentReportDir, filename));`
- `sources/com/facebook/internal/instrument/InstrumentUtility.java:256`
  `return new File(instrumentReportDir, filename).delete();`
- `sources/com/facebook/internal/instrument/InstrumentUtility.java:287`
  `File file = new File(FacebookSdk.getApplicationContext().getCacheDir(), INSTRUMENT_DIR);`
- `sources/com/google/android/gms/internal/auth/zzcp.java:42`
  `File file = new File(context.getDir("phenotype_hermetic", 0), "overrides.txt");`
- `sources/com/google/android/gms/internal/measurement/zzjy.java:46`
  `File file = new File(contextCreateDeviceProtectedStorageContext.getDir("phenotype_hermetic", 0), "overrides.txt");`
- `sources/com/google/android/gms/measurement/internal/zzaw.java:30`
  `File file = new File(path);`
- `sources/com/google/android/gms/measurement/internal/zzpf.java:1510`
  `FileChannel channel = new RandomAccessFile(new File(new File(filesDir, "google_app_measurement.db").getPath()), "rw").getChannel();`
- `sources/com/google/common/reflect/ClassPath.java:400`
  `builder.add(new File(str).toURI().toURL());`
- `sources/com/google/common/reflect/ClassPath.java:402`
  `builder.add(new URL(ShareInternalUtility.STAGING_PARAM, (String) null, new File(str).getAbsolutePath()));`
- `sources/com/google/firebase/crashlytics/internal/common/NativeSessionFileGzipper.java:21`
  `gzipInputStream(stream, new File(file, nativeSessionFile.getReportsEndpointFilename()));`
- `sources/com/google/firebase/crashlytics/internal/persistence/FileStore.java:42`
  `File filePrepareBaseDir = prepareBaseDir(new File(filesDir, str));`
- `sources/com/google/firebase/crashlytics/internal/persistence/FileStore.java:44`
  `this.sessionsDir = prepareBaseDir(new File(filePrepareBaseDir, SESSIONS_PATH));`
- `sources/com/google/firebase/crashlytics/internal/persistence/FileStore.java:45`
  `this.reportsDir = prepareBaseDir(new File(filePrepareBaseDir, REPORTS_PATH));`
- `sources/com/google/firebase/crashlytics/internal/persistence/FileStore.java:46`
  `this.priorityReportsDir = prepareBaseDir(new File(filePrepareBaseDir, PRIORITY_REPORTS_PATH));`
- `sources/com/google/firebase/crashlytics/internal/persistence/FileStore.java:47`
  `this.nativeReportsDir = prepareBaseDir(new File(filePrepareBaseDir, NATIVE_REPORTS_PATH));`
- `sources/com/google/firebase/crashlytics/internal/persistence/FileStore.java:64`
  `File file = new File(this.filesDir, str);`
- `sources/com/google/firebase/crashlytics/internal/persistence/FileStore.java:128`
  `return new File(this.reportsDir, str);`
- `sources/com/google/firebase/crashlytics/internal/persistence/FileStore.java:136`
  `return new File(this.priorityReportsDir, str);`
- `sources/com/google/firebase/crashlytics/internal/persistence/FileStore.java:144`
  `return new File(this.nativeReportsDir, str);`
- `sources/com/google/firebase/firestore/local/SQLitePersistence.java:184`
  `File file = new File(path);`
- `sources/com/google/firebase/firestore/local/SQLitePersistence.java:185`
  `File file2 = new File(path + "-journal");`
- `sources/com/google/firebase/firestore/local/SQLitePersistence.java:186`
  `File file3 = new File(str2);`
- `sources/com/lifesense/ble/LsBleManager.java:152`
  `Object objA = l.a(new File(Environment.getExternalStorageDirectory().getPath() + File.separator + LsBleInterface.PERMISSION_OBJECT_FILE_NAME));`
- `sources/com/lifesense/ble/a/c/d.java:166`
  `File file = new File(str);`
- `sources/com/lifesense/ble/a/c/a/j.java:55`
  `File file = new File(iVar.a());`
- `sources/com/lifesense/ble/a/c/a/j.java:131`
  `File file2 = new File(strA2);`

## BR028

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `resources/AndroidManifest.xml:83`
  `android:fullBackupContent="false"`
- `resources/AndroidManifest.xml:86`
  `android:dataExtractionRules="@xml/data_extraction_rules">`
- `resources/res/xml/data_extraction_rules.xml:4`
  `<exclude domain="root"/>`
- `resources/res/xml/data_extraction_rules.xml:5`
  `<exclude domain="file"/>`
- `resources/res/xml/data_extraction_rules.xml:6`
  `<exclude domain="database"/>`
- `resources/res/xml/data_extraction_rules.xml:7`
  `<exclude domain="sharedpref"/>`
- `resources/res/xml/data_extraction_rules.xml:8`
  `<exclude domain="external"/>`
- `resources/res/xml/data_extraction_rules.xml:11`
  `<exclude domain="root"/>`
- `resources/res/xml/data_extraction_rules.xml:12`
  `<exclude domain="file"/>`
- `resources/res/xml/data_extraction_rules.xml:13`
  `<exclude domain="database"/>`
- `resources/res/xml/data_extraction_rules.xml:14`
  `<exclude domain="sharedpref"/>`
- `resources/res/xml/data_extraction_rules.xml:15`
  `<exclude domain="external"/>`

## BR029

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:90`
  `android:exported="true"`
- `resources/AndroidManifest.xml:199`
  `android:exported="true"`

## BR032

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `resources/AndroidManifest.xml:100`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:203`
  `<action android:name="android.intent.action.VIEW"/>`

## BR033

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/androidx/browser/browseractions/BrowserActionsIntent.java:179`
  `return context.getPackageManager().queryIntentActivities(new Intent(ACTION_BROWSER_ACTIONS_OPEN, Uri.parse(TEST_URL)), 131072);`
- `sources/com/facebook/CustomTabActivity.java:29`
  `intent.putExtra(CustomTabMainActivity.EXTRA_URL, getIntent().getDataString());`
- `sources/com/facebook/Profile.java:287`
  `Profile.INSTANCE.setCurrentProfile(new Profile(strOptString, userInfo.optString("first_name"), userInfo.optString(AuthenticationTokenClaims.JSON_KEY_MIDDLE_NAME), userInfo.optString("last_name"), userInfo.optString("name"), strOptString2 != null ? Uri.parse(strOptString2) : null, strOptString3 != nu...`
- `sources/com/facebook/appevents/gps/pa/PACustomAudienceClient.java:242`
  `Uri uri4 = Uri.parse(sb4.append(str4).append("?bidding").toString());`
- `sources/com/facebook/appevents/gps/pa/PACustomAudienceClient.java:243`
  `Intrinsics.checkExpressionValueIsNotNull(uri4, "Uri.parse(this)");`
- `sources/com/facebook/internal/ImageRequest.java:113`
  `Uri.Builder builderBuildUpon = Uri.parse(ServerProtocol.getGraphUrlBase()).buildUpon();`
- `sources/com/facebook/internal/WebDialog.java:638`
  `WebDialog.this.getContext().startActivity(new Intent("android.intent.action.VIEW", Uri.parse(url)));`
- `sources/com/facebook/internal/WebDialog.java:872`
  `Uri uri = Uri.parse(stringArray[i]);`
- `sources/com/facebook/login/CustomTabLoginMethodHandler.java:177`
  `Uri uri = Uri.parse(url);`
- `sources/com/google/firebase/auth/UserProfileChangeRequest.java:77`
  `this.zze = TextUtils.isEmpty(str2) ? null : Uri.parse(str2);`
- `sources/com/google/firebase/auth/internal/zzab.java:35`
  `this.zze = Uri.parse(this.zzd);`
- `sources/com/google/firebase/auth/internal/zzcc.java:100`
  `this.zzg.getApp().getApplicationContext().startActivity(new Intent("android.intent.action.VIEW", Uri.parse(str)).addFlags(268435456));`
- `sources/com/google/firebase/auth/internal/zzcc.java:105`
  `activity.startActivity(new Intent("android.intent.action.VIEW", Uri.parse(str)).addFlags(268435456));`
- `sources/com/viwave/rossmaxconnect/MainAdvActivity.java:1369`
  `Uri data = getIntent().getData();`
- `sources/com/viwave/rossmaxconnect/SplashActivity.java:374`
  `intent.setData(getIntent().getData());`
- `sources/com/viwave/rossmaxconnect/SplashActivity.java:438`
  `splashActivity.startActivity(new Intent("android.intent.action.VIEW", Uri.parse(versionCheckerResponse.getUpdateURL())));`
- `sources/com/viwave/rossmaxconnect/SplashActivity.java:445`
  `splashActivity.startActivity(new Intent("android.intent.action.VIEW", Uri.parse(versionCheckerResponse.getUpdateURL())));`
- `sources/com/viwave/rossmaxconnect/advfragment/WebFragment$initWebView$1$1.java:63`
  `Intent intent = new Intent("android.intent.action.VIEW", Uri.parse(strValueOf));`

## BR034

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/androidx/browser/customtabs/CustomTabsIntent.java:83`
  `ContextCompat.startActivity(context, this.intent, this.startAnimationBundle);`
- `sources/androidx/browser/customtabs/TrustedWebUtils.java:32`
  `context.startActivity(intent);`
- `sources/com/facebook/AccessTokenManager.java:152`
  `this.localBroadcastManager.sendBroadcast(intent);`
- `sources/com/facebook/AuthenticationTokenManager.java:97`
  `this.localBroadcastManager.sendBroadcast(intent);`
- `sources/com/facebook/CustomTabMainActivity.java:88`
  `this.this$0.startActivity(intent2);`
- `sources/com/google/android/gms/measurement/internal/zzhk.java:40`
  `this.zza.doStartService(context, className);`
- `sources/com/viwave/rossmaxconnect/MainAdvActivity.java:306`
  `mainAdvActivity.startActivity(intent);`
- `sources/com/viwave/rossmaxconnect/SplashActivity.java:375`
  `startActivity(intent);`
- `sources/com/viwave/rossmaxconnect/advfragment/caring/QRCodeFragment.java:416`
  `startActivity(Intent.createChooser(intent, null));`

## BR035

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/com/facebook/appevents/AppEventsLoggerImpl.java:1066`
  `webView.addJavascriptInterface(new FacebookSDKJSInterface(context), "fbmq_" + FacebookSdk.getApplicationId());`
- `sources/com/facebook/internal/FacebookWebFallbackDialog.java:79`
  `webView.loadUrl("javascript:(function() {  var event = document.createEvent('Event');  event.initEvent('fbPlatformDialogMustClose',true,true);  document.dispatchEvent(event);})();");`
- `sources/com/facebook/internal/WebDialog.java:531`
  `webView6.loadUrl(str);`
- `sources/com/google/android/recaptcha/internal/zzil.java:100`
  `r7.addJavascriptInterface(r1, r2)`
- `sources/com/viwave/rossmaxconnect/MainAdvActivity.java:349`
  `webView3.loadUrl(mainAdvActivity.getUrl(value, webViewModel2.getError().getValue()));`
- `sources/com/viwave/rossmaxconnect/MainAdvActivity.java:634`
  `webView.loadUrl(getUrl$default(this, null, null, 3, null));`
- `sources/com/viwave/rossmaxconnect/SetRegionActivity.java:319`
  `webView.loadUrl("https://rossmax-care-static-web-page.s3-ap-northeast-1.amazonaws.com/privacy/rossmax.html?region=" + stringExtra + "&language=" + lowerCase + "&editable=" + booleanExtra + "&hint=" + booleanExtra2);`
- `sources/com/viwave/rossmaxconnect/advfragment/WebFragment.java:144`
  `webView.loadUrl(this.strUrl);`

## BR040

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `sources/com/facebook/internal/AttributionIdentifiers.java:107`
  `Method methodQuietly = Utility.getMethodQuietly("com.google.android.gms.ads.identifier.AdvertisingIdClient", "getAdvertisingIdInfo", (Class<?>[]) new Class[]{Context.class});`
- `sources/com/facebook/internal/AttributionIdentifiers.java:148`
  `Intent intent = new Intent("com.google.android.gms.ads.identifier.service.START");`
- `sources/com/facebook/internal/AttributionIdentifiers.java:260`
  `parcelObtain.writeInterfaceToken("com.google.android.gms.ads.identifier.internal.IAdvertisingIdService");`
- `sources/com/facebook/internal/AttributionIdentifiers.java:276`
  `parcelObtain.writeInterfaceToken("com.google.android.gms.ads.identifier.internal.IAdvertisingIdService");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:1`
  `package com.google.android.gms.ads.identifier;`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:229`
  `Intent intent = new Intent("com.google.android.gms.ads.identifier.service.START");`
- `sources/com/google/android/gms/ads/identifier/zza.java:1`
  `package com.google.android.gms.ads.identifier;`
- `sources/com/google/android/gms/ads/identifier/zzb.java:1`
  `package com.google.android.gms.ads.identifier;`
- `sources/com/google/android/gms/ads/identifier/zzc.java:1`
  `package com.google.android.gms.ads.identifier;`
- `sources/com/google/android/gms/ads_identifier/R.java:1`
  `package com.google.android.gms.ads_identifier;`
- `sources/com/google/android/gms/internal/ads_identifier/zza.java:12`
  `private final String zzb = "com.google.android.gms.ads.identifier.internal.IAdvertisingIdService";`
- `sources/com/google/android/gms/internal/ads_identifier/zzd.java:11`
  `super(iBinder, "com.google.android.gms.ads.identifier.internal.IAdvertisingIdService");`
- `sources/com/google/android/gms/internal/ads_identifier/zze.java:13`
  `IInterface iInterfaceQueryLocalInterface = iBinder.queryLocalInterface("com.google.android.gms.ads.identifier.internal.IAdvertisingIdService");`
- `sources/com/google/android/gms/internal/auth/zzby.java:51`
  `BAD_REQUEST("BadRequest"),`
- `sources/com/google/android/gms/measurement/internal/zzhg.java:7`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/measurement/internal/zznm.java:5`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/rpc/BadRequest.java:19`
  `public final class BadRequest extends GeneratedMessageLite<BadRequest, Builder> implements BadRequestOrBuilder {`
- `sources/com/google/rpc/BadRequest.java:20`
  `private static final BadRequest DEFAULT_INSTANCE;`
- `sources/com/google/rpc/BadRequest.java:22`
  `private static volatile Parser<BadRequest> PARSER;`
- `sources/com/google/rpc/BadRequest.java:35`
  `private BadRequest() {`
- `sources/com/google/rpc/BadRequest.java:49`
  `@Override // com.google.rpc.BadRequest.FieldViolationOrBuilder`
- `sources/com/google/rpc/BadRequest.java:54`
  `@Override // com.google.rpc.BadRequest.FieldViolationOrBuilder`
- `sources/com/google/rpc/BadRequest.java:76`
  `@Override // com.google.rpc.BadRequest.FieldViolationOrBuilder`
- `sources/com/google/rpc/BadRequest.java:81`
  `@Override // com.google.rpc.BadRequest.FieldViolationOrBuilder`
- `sources/com/google/rpc/BadRequest.java:168`
  `@Override // com.google.rpc.BadRequest.FieldViolationOrBuilder`
- `sources/com/google/rpc/BadRequest.java:173`
  `@Override // com.google.rpc.BadRequest.FieldViolationOrBuilder`
- `sources/com/google/rpc/BadRequest.java:196`
  `@Override // com.google.rpc.BadRequest.FieldViolationOrBuilder`
- `sources/com/google/rpc/BadRequest.java:201`
  `@Override // com.google.rpc.BadRequest.FieldViolationOrBuilder`
- `sources/com/google/rpc/BadRequest.java:277`
  `/* JADX INFO: renamed from: com.google.rpc.BadRequest$1, reason: invalid class name */`
- `sources/com/google/rpc/BadRequest.java:315`
  `@Override // com.google.rpc.BadRequestOrBuilder`
- `sources/com/google/rpc/BadRequest.java:324`
  `@Override // com.google.rpc.BadRequestOrBuilder`
- `sources/com/google/rpc/BadRequest.java:329`
  `@Override // com.google.rpc.BadRequestOrBuilder`
- `sources/com/google/rpc/BadRequest.java:384`
  `public static BadRequest parseFrom(ByteBuffer byteBuffer) throws InvalidProtocolBufferException {`
- `sources/com/google/rpc/BadRequest.java:385`
  `return (BadRequest) GeneratedMessageLite.parseFrom(DEFAULT_INSTANCE, byteBuffer);`
- `sources/com/google/rpc/BadRequest.java:388`
  `public static BadRequest parseFrom(ByteBuffer byteBuffer, ExtensionRegistryLite extensionRegistryLite) throws InvalidProtocolBufferException {`
- `sources/com/google/rpc/BadRequest.java:389`
  `return (BadRequest) GeneratedMessageLite.parseFrom(DEFAULT_INSTANCE, byteBuffer, extensionRegistryLite);`
- `sources/com/google/rpc/BadRequest.java:392`
  `public static BadRequest parseFrom(ByteString byteString) throws InvalidProtocolBufferException {`
- `sources/com/google/rpc/BadRequest.java:393`
  `return (BadRequest) GeneratedMessageLite.parseFrom(DEFAULT_INSTANCE, byteString);`
- `sources/com/google/rpc/BadRequest.java:396`
  `public static BadRequest parseFrom(ByteString byteString, ExtensionRegistryLite extensionRegistryLite) throws InvalidProtocolBufferException {`
- `sources/com/google/rpc/BadRequest.java:397`
  `return (BadRequest) GeneratedMessageLite.parseFrom(DEFAULT_INSTANCE, byteString, extensionRegistryLite);`
- `sources/com/google/rpc/BadRequest.java:400`
  `public static BadRequest parseFrom(byte[] bArr) throws InvalidProtocolBufferException {`
- `sources/com/google/rpc/BadRequest.java:401`
  `return (BadRequest) GeneratedMessageLite.parseFrom(DEFAULT_INSTANCE, bArr);`
- `sources/com/google/rpc/BadRequest.java:404`
  `public static BadRequest parseFrom(byte[] bArr, ExtensionRegistryLite extensionRegistryLite) throws InvalidProtocolBufferException {`
- `sources/com/google/rpc/BadRequest.java:405`
  `return (BadRequest) GeneratedMessageLite.parseFrom(DEFAULT_INSTANCE, bArr, extensionRegistryLite);`
- `sources/com/google/rpc/BadRequest.java:408`
  `public static BadRequest parseFrom(InputStream inputStream) throws IOException {`
- `sources/com/google/rpc/BadRequest.java:409`
  `return (BadRequest) GeneratedMessageLite.parseFrom(DEFAULT_INSTANCE, inputStream);`
- `sources/com/google/rpc/BadRequest.java:412`
  `public static BadRequest parseFrom(InputStream inputStream, ExtensionRegistryLite extensionRegistryLite) throws IOException {`
- `sources/com/google/rpc/BadRequest.java:413`
  `return (BadRequest) GeneratedMessageLite.parseFrom(DEFAULT_INSTANCE, inputStream, extensionRegistryLite);`
- `sources/com/google/rpc/BadRequest.java:416`
  `public static BadRequest parseDelimitedFrom(InputStream inputStream) throws IOException {`
- `sources/com/google/rpc/BadRequest.java:417`
  `return (BadRequest) parseDelimitedFrom(DEFAULT_INSTANCE, inputStream);`
- `sources/com/google/rpc/BadRequest.java:420`
  `public static BadRequest parseDelimitedFrom(InputStream inputStream, ExtensionRegistryLite extensionRegistryLite) throws IOException {`
- `sources/com/google/rpc/BadRequest.java:421`
  `return (BadRequest) parseDelimitedFrom(DEFAULT_INSTANCE, inputStream, extensionRegistryLite);`
- `sources/com/google/rpc/BadRequest.java:424`
  `public static BadRequest parseFrom(CodedInputStream codedInputStream) throws IOException {`
- `sources/com/google/rpc/BadRequest.java:425`
  `return (BadRequest) GeneratedMessageLite.parseFrom(DEFAULT_INSTANCE, codedInputStream);`
- `sources/com/google/rpc/BadRequest.java:428`
  `public static BadRequest parseFrom(CodedInputStream codedInputStream, ExtensionRegistryLite extensionRegistryLite) throws IOException {`
- `sources/com/google/rpc/BadRequest.java:429`
  `return (BadRequest) GeneratedMessageLite.parseFrom(DEFAULT_INSTANCE, codedInputStream, extensionRegistryLite);`
- `sources/com/google/rpc/BadRequest.java:436`
  `public static Builder newBuilder(BadRequest badRequest) {`
- `sources/com/google/rpc/BadRequest.java:437`
  `return DEFAULT_INSTANCE.createBuilder(badRequest);`
- `sources/com/google/rpc/BadRequest.java:440`
  `public static final class Builder extends GeneratedMessageLite.Builder<BadRequest, Builder> implements BadRequestOrBuilder {`
- `sources/com/google/rpc/BadRequest.java:446`
  `super(BadRequest.DEFAULT_INSTANCE);`
- `sources/com/google/rpc/BadRequest.java:449`
  `@Override // com.google.rpc.BadRequestOrBuilder`
- `sources/com/google/rpc/BadRequest.java:451`
  `return Collections.unmodifiableList(((BadRequest) this.instance).getFieldViolationsList());`
- `sources/com/google/rpc/BadRequest.java:454`
  `@Override // com.google.rpc.BadRequestOrBuilder`
- `sources/com/google/rpc/BadRequest.java:456`
  `return ((BadRequest) this.instance).getFieldViolationsCount();`
- `sources/com/google/rpc/BadRequest.java:459`
  `@Override // com.google.rpc.BadRequestOrBuilder`
- `sources/com/google/rpc/BadRequest.java:461`
  `return ((BadRequest) this.instance).getFieldViolations(i);`
- `sources/com/google/rpc/BadRequest.java:466`
  `((BadRequest) this.instance).setFieldViolations(i, fieldViolation);`
- `sources/com/google/rpc/BadRequest.java:472`
  `((BadRequest) this.instance).setFieldViolations(i, builder.build());`
- `sources/com/google/rpc/BadRequest.java:478`
  `((BadRequest) this.instance).addFieldViolations(fieldViolation);`
- `sources/com/google/rpc/BadRequest.java:484`
  `((BadRequest) this.instance).addFieldViolations(i, fieldViolation);`
- `sources/com/google/rpc/BadRequest.java:490`
  `((BadRequest) this.instance).addFieldViolations(builder.build());`
- `sources/com/google/rpc/BadRequest.java:496`
  `((BadRequest) this.instance).addFieldViolations(i, builder.build());`
- `sources/com/google/rpc/BadRequest.java:502`
  `((BadRequest) this.instance).addAllFieldViolations(iterable);`
- `sources/com/google/rpc/BadRequest.java:508`
  `((BadRequest) this.instance).clearFieldViolations();`
- `sources/com/google/rpc/BadRequest.java:514`
  `((BadRequest) this.instance).removeFieldViolations(i);`
- `sources/com/google/rpc/BadRequest.java:526`
  `return new BadRequest();`
- `sources/com/google/rpc/BadRequest.java:534`
  `Parser<BadRequest> parser = PARSER;`
- `sources/com/google/rpc/BadRequest.java:538`
  `synchronized (BadRequest.class) {`
- `sources/com/google/rpc/BadRequest.java:557`
  `BadRequest badRequest = new BadRequest();`
- `sources/com/google/rpc/BadRequest.java:558`
  `DEFAULT_INSTANCE = badRequest;`

## BR041

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `resources/AndroidManifest.xml:148`
  `android:name="com.google.firebase.components:com.google.firebase.analytics.ktx.FirebaseAnalyticsLegacyRegistrar"`
- `resources/AndroidManifest.xml:175`
  `android:name="com.google.firebase.components:com.google.firebase.analytics.connector.internal.AnalyticsConnectorRegistrar"`
- `sources/androidx/annotation/RequiresOptIn.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/annotation/experimental/Experimental.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/appcompat/app/TwilightManager.java:8`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/appcompat/widget/SuggestionsAdapter.java:27`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/ArraySet.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/ArraySetKt.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/CircularArray.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/CircularIntArray.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/FloatFloatMap.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/FloatIntMap.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/FloatList.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/FloatLongMap.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/FloatObjectMap.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/FloatSet.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/IndexBasedArrayIterator.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/IntFloatMap.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/IntIntMap.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/IntList.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/IntLongMap.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/IntObjectMap.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/IntSet.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/LongFloatMap.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/LongIntMap.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/LongList.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/LongLongMap.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/LongObjectMap.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/LongSet.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/LongSparseArray.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/LongSparseArrayKt.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableFloatFloatMap.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableFloatIntMap.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableFloatList.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableFloatLongMap.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableFloatObjectMap.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableFloatSet.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableIntFloatMap.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableIntIntMap.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableIntList.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableIntLongMap.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableIntObjectMap.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableIntSet.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableLongFloatMap.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableLongIntMap.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableLongList.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableLongLongMap.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableLongObjectMap.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableLongSet.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableMapEntry.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableObjectFloatMap.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableObjectIntMap.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableObjectList.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableObjectLongMap.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableScatterMap.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/MutableScatterSet.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/ObjectFloatMap.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/ObjectIntMap.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/ObjectList.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/ObjectListKt.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/ObjectLongMap.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/ScatterMap.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/ScatterMapKt.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/ScatterSet.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/SimpleArrayMap.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/SparseArrayCompat.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/SparseArrayCompatKt.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/collection/SparseArrayKt.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/content/ContextCompat.java:77`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/content/FileProvider.java:17`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/content/res/TypedArrayApi26ImplKt.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/content/res/TypedArrayKt.java:8`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/database/CursorKt.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/graphics/drawable/IconCompat.java:35`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/provider/FontProvider.java:18`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/util/LongSparseArrayKt.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/util/SparseArrayKt.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/view/MenuKt.java:7`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/view/ViewGroupKt.java:8`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/fragment/app/FragmentContainerView.java:20`
  `import com.google.firebase.analytics.FirebaseAnalytics;`

## BR042

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `resources/AndroidManifest.xml:48`
  `<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>`
- `resources/AndroidManifest.xml:50`
  `<uses-permission android:name="android.permission.ACCESS_ADSERVICES_AD_ID"/>`
- `sources/com/facebook/appevents/cloudbridge/AppEventsConversionsAPITransformer.java:38`
  `private static final Map<AppEventUserAndAppDataField, SectionFieldMapping> topLevelTransformations = MapsKt.mapOf(TuplesKt.to(AppEventUserAndAppDataField.ANON_ID, new SectionFieldMapping(ConversionsAPISection.USER_DATA, ConversionsAPIUserAndAppDataField.ANON_ID)), TuplesKt.to(AppEventUserAndAppDataF...`
- `sources/com/facebook/appevents/cloudbridge/ConversionsAPIUserAndAppDataField.java:8`
  `@Metadata(d1 = {"\u0000\u0012\n\u0002\u0018\u0002\n\u0002\u0010\u0010\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0015\b\u0086\u0001\u0018\u00002\b\u0012\u0004\u0012\u00020\u00000\u0001B\u000f\b\u0002\u0012\u0006\u0010\u0002\u001a\u00020\u0003¢\u0006\u0002\u0010\u0004R\u0011\u0010\u0002\u001a\u00020\u000...`
- `sources/com/facebook/appevents/cloudbridge/ConversionsAPIUserAndAppDataField.java:12`
  `MAD_ID("madid"),`
- `sources/com/facebook/internal/AttributionIdentifiers.java:107`
  `Method methodQuietly = Utility.getMethodQuietly("com.google.android.gms.ads.identifier.AdvertisingIdClient", "getAdvertisingIdInfo", (Class<?>[]) new Class[]{Context.class});`
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
  `Log.i("AdvertisingIdClient", "GMS remote exception ", e2);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:115`
  `throw new IOException("AdvertisingIdClient cannot reconnect.", e3);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:119`
  `advertisingIdClient.zze();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:122`
  `advertisingIdClient.zza();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:141`
  `throw new IOException("AdvertisingIdClient is not connected.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:147`
  `throw new IOException("AdvertisingIdClient cannot reconnect.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:154`
  `Log.i("AdvertisingIdClient", "GMS remote exception ", e2);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:158`
  `throw new IOException("AdvertisingIdClient cannot reconnect.", e3);`
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
- `sources/com/google/android/gms/internal/measurement/zzpa.java:88`
  `zza = zzkfVarZzb.zzc("measurement.ad_id_cache_time", 10000L);`
- `sources/com/google/android/gms/internal/measurement/zzpa.java:89`
  `zzb = zzkfVarZzb.zzc("measurement.app_uninstalled_additional_ad_id_cache_time", 3600000L);`
- `sources/com/google/android/gms/measurement/internal/zzav.java:30`
  `private static final String[] zzd = {"app_version", "ALTER TABLE apps ADD COLUMN app_version TEXT;", "app_store", "ALTER TABLE apps ADD COLUMN app_store TEXT;", "gmp_version", "ALTER TABLE apps ADD COLUMN gmp_version INTEGER;", "dev_cert_hash", "ALTER TABLE apps ADD COLUMN dev_cert_hash INTEGER;", "...`
- `sources/com/google/android/gms/measurement/internal/zzav.java:1820`
  `contentValues.put("unmatched_first_open_without_ad_id", Boolean.valueOf(zzhVar.zzaq()));`
- `sources/com/google/android/gms/measurement/internal/zzhg.java:7`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/measurement/internal/zzhg.java:78`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(true);`
- `sources/com/google/android/gms/measurement/internal/zzhg.java:80`
  `AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(zzibVar.zzaY());`
- `sources/com/google/android/gms/measurement/internal/zzhg.java:91`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(false);`
- `sources/com/google/android/gms/measurement/internal/zznm.java:5`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/measurement/internal/zznm.java:59`
  `AdvertisingIdClient.Info advertisingIdInfo;`
- `sources/com/google/android/gms/measurement/internal/zznm.java:67`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(true);`
- `sources/com/google/android/gms/measurement/internal/zznm.java:71`
  `advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(zzibVar.zzaY());`
- `sources/com/google/android/gms/measurement/internal/zznm.java:88`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(false);`

## BR043

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/com/lifesense/ble/ReceiveDataCallback.java:81`
  `public void onReceiveWifiScanResult(WifiInfo wifiInfo) {`
- `sources/com/lifesense/ble/a/c.java:6`
  `import com.lifesense.ble.bean.BleScanResults;`
- `sources/com/lifesense/ble/a/c.java:34`
  `public void a(BleScanResults bleScanResults) {`
- `sources/com/lifesense/ble/a/d/b.java:7`
  `import com.lifesense.ble.bean.BleScanResults;`
- `sources/com/lifesense/ble/a/d/b.java:51`
  `public void a(BleScanResults bleScanResults) throws Throwable {`
- `sources/com/lifesense/ble/a/d/b.java:52`
  `String strG = g(bleScanResults.getAddress());`
- `sources/com/lifesense/ble/a/d/b.java:53`
  `byte[] scanRecord = bleScanResults.getScanRecord();`
- `sources/com/lifesense/ble/a/d/b.java:58`
  `if (!strG.equalsIgnoreCase(bleScanResults.getAddress())) {`
- `sources/com/lifesense/ble/a/d/b.java:59`
  `if (a(strG, bleScanResults.getAddress(), strB)) {`
- `sources/com/lifesense/ble/a/d/b.java:61`
  `printLogMessage(getAdvancedLogInfo(strG, "sourceMac=(" + strG + "),upgrade mode mac=(" + bleScanResults.getAddress() + ")", com.lifesense.ble.a.c.a.a.Scan_Results, null, true));`
- `sources/com/lifesense/ble/a/d/b.java:63`
  `a(strG, bleScanResults.getAddress(), DeviceUpgradeStatus.CONNECT_UPGRADE_MODE_DEVICE);`
- `sources/com/lifesense/ble/a/d/b.java:76`
  `a(strG, bleScanResults.getAddress(), DeviceUpgradeStatus.CONNECT_DEVICE);`
- `sources/com/lifesense/ble/a/d/c.java:4`
  `import com.lifesense.ble.bean.BleScanResults;`
- `sources/com/lifesense/ble/a/d/c.java:21`
  `public void a(BleScanResults bleScanResults) throws Throwable {`
- `sources/com/lifesense/ble/a/d/c.java:22`
  `if (bleScanResults == null || bleScanResults.getAddress() == null) {`
- `sources/com/lifesense/ble/a/d/c.java:25`
  `this.f740a.a(bleScanResults);`
- `sources/com/lifesense/ble/a/g/a.java:10`
  `import com.lifesense.ble.bean.BleScanResults;`
- `sources/com/lifesense/ble/a/g/a.java:97`
  `private synchronized com.lifesense.ble.bean.LsDeviceInfo a(com.lifesense.ble.bean.BleScanResults r11, java.lang.String r12, java.lang.String r13, java.util.List r14) {`
- `sources/com/lifesense/ble/a/g/a.java:102`
  `throw new UnsupportedOperationException("Method not decompiled: com.lifesense.ble.a.g.a.a(com.lifesense.ble.bean.BleScanResults, java.lang.String, java.lang.String, java.util.List):com.lifesense.ble.bean.LsDeviceInfo");`
- `sources/com/lifesense/ble/a/g/a.java:149`
  `public synchronized void a(BleScanResults bleScanResults) {`
- `sources/com/lifesense/ble/a/g/a.java:150`
  `if (b(bleScanResults)) {`
- `sources/com/lifesense/ble/a/g/a.java:151`
  `byte[] scanRecord = bleScanResults.getScanRecord();`
- `sources/com/lifesense/ble/a/g/a.java:152`
  `String address = bleScanResults.getAddress();`
- `sources/com/lifesense/ble/a/g/a.java:157`
  `LsDeviceInfo lsDeviceInfoA = a(bleScanResults, strB, strA, listA);`
- `sources/com/lifesense/ble/a/g/a.java:233`
  `private synchronized boolean b(BleScanResults bleScanResults) {`
- `sources/com/lifesense/ble/a/g/a.java:234`
  `if (bleScanResults == null) {`
- `sources/com/lifesense/ble/a/g/a.java:237`
  `if (bleScanResults.getAddress() != null && bleScanResults.getAddress().length() != 0) {`
- `sources/com/lifesense/ble/a/g/a.java:238`
  `if (bleScanResults.getScanRecord() != null && bleScanResults.getScanRecord().length != 0) {`
- `sources/com/lifesense/ble/a/g/a.java:248`
  `String upperCase2 = bleScanResults.getAddress().replace(com.lifesense.ble.b.b.a.a.SEPARATOR_TIME_COLON, "").toUpperCase();`
- `sources/com/lifesense/ble/a/g/a.java:250`
  `if (a(str, bleScanResults.getName())) {`
- `sources/com/lifesense/ble/a/g/b.java:4`
  `import com.lifesense.ble.bean.BleScanResults;`
- `sources/com/lifesense/ble/a/g/b.java:26`
  `public void a(BleScanResults bleScanResults) {`
- `sources/com/lifesense/ble/a/g/b.java:27`
  `if (bleScanResults == null) {`
- `sources/com/lifesense/ble/a/g/b.java:32`
  `messageObtainMessage.obj = bleScanResults;`
- `sources/com/lifesense/ble/a/g/f.java:6`
  `import com.lifesense.ble.bean.BleScanResults;`
- `sources/com/lifesense/ble/a/g/f.java:51`
  `BleScanResults bleScanResults = (BleScanResults) message.obj;`
- `sources/com/lifesense/ble/a/g/f.java:52`
  `if (bleScanResults.getDevice() == null || bleScanResults.getDevice().getAddress() == null) {`
- `sources/com/lifesense/ble/a/g/f.java:55`
  `bleScanResults.setName(bleScanResults.getDevice().getName());`
- `sources/com/lifesense/ble/a/g/f.java:56`
  `bleScanResults.setAddress(bleScanResults.getDevice().getAddress());`
- `sources/com/lifesense/ble/a/g/f.java:59`
  `this.f796a.o.a(bleScanResults);`
- `sources/com/lifesense/ble/a/g/f.java:64`
  `if (this.f796a.B != null && !this.f796a.B.contains(bleScanResults.getAddress())) {`
- `sources/com/lifesense/ble/a/g/f.java:65`
  `this.f796a.B.add(bleScanResults.getAddress());`
- `sources/com/lifesense/ble/a/g/f.java:67`
  `this.f796a.a(bleScanResults);`
- `sources/com/lifesense/ble/b/e/c/f.java:87`
  `com.lifesense.ble.a.h.a.a().b().onReceiveWifiScanResult(wifiInfo);`
- `sources/com/lifesense/ble/bean/BleScanResults.java:7`
  `public class BleScanResults {`
- `sources/com/lifesense/ble/bean/BleScanResults.java:55`
  `return "BleScanResults [device=" + this.device + ", name=" + this.name + ", address=" + this.address + ", scanRecord=" + Arrays.toString(this.scanRecord) + ", rssi=" + this.rssi + "]";`
- `sources/com/lifesense/ble/c/a.java:3`
  `import com.lifesense.ble.bean.BleScanResults;`
- `sources/com/lifesense/ble/c/a.java:10`
  `public void a(BleScanResults bleScanResults) {`
- `sources/com/lifesense/ble/c/b.java:17`
  `import com.lifesense.ble.bean.BleScanResults;`
- `sources/com/lifesense/ble/c/b.java:336`
  `zStartLeScan = this.g.startLeScan(this);`
- `sources/com/lifesense/ble/c/b.java:699`
  `BleScanResults bleScanResults = new BleScanResults();`
- `sources/com/lifesense/ble/c/b.java:700`
  `bleScanResults.setDevice(bluetoothDevice);`
- `sources/com/lifesense/ble/c/b.java:701`
  `bleScanResults.setRssi(i);`
- `sources/com/lifesense/ble/c/b.java:702`
  `bleScanResults.setScanRecord(bArr);`
- `sources/com/lifesense/ble/c/b.java:703`
  `this.i.a(bleScanResults);`
- `sources/com/viwave/rossmaxconnect/advfragment/measure/delegate/MeasureDelegate$mScanCallback$1.java:13`
  `@Metadata(d1 = {"\u0000\u001b\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u0002\n\u0002\b\u0002*\u0001\u0000\b\n\u0018\u00002\u00020\u0001J\u0012\u0010\b\u001a\u00020\t2\b\u0010\n\u001a\u0004\u0018\u00010\u0003H\u0016R\u001c\u0010\u0002\u001a\u0004\u0018\u00...`
- `sources/com/viwave/rossmaxconnect/advfragment/measure/delegate/MeasureDelegate$mScanCallback$1.java:31`
  `public void onScanResult(VUBleDevice p0) {`
- `sources/com/viwave/rossmaxconnect/advfragment/measure/delegate/MeasureDelegate$mScanCallback$1.java:33`
  `super.onScanResult(p0);`
- `sources/com/viwave/rossmaxconnect/advfragment/measure/delegate/MeasureDelegate.java:353`
  `VUBleManager.getInstance().startScan(generateScanFilter(), 0);`
- `sources/com/viwave/rossmaxconnect/fragment/device/DeviceScanFragment.java:539`
  `VUBleManager.getInstance().startScan(listGenerateRossmaxPulseOximeterSA300ScanFilterList, 5);`
- `sources/com/viwave/rossmaxconnect/fragment/device/DeviceScanFragment.java:636`
  `@Metadata(d1 = {"\u0000\u001a\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\b\u0082\u0004\u0018\u00002\u00020\u0001B\u0007¢\u0006\u0004\b\u0002\u0010\u0003J\u0010\u0010\u0004\u001a\u00020\u00052\u0006\u0010\u0006\u001a\u00020\...`
- `sources/com/viwave/rossmaxconnect/fragment/device/DeviceScanFragment.java:642`
  `public void onScanResult(VUBleDevice device) {`
- `sources/com/viwaveulife/vuioht/VUBleManager.java:78`
  `import no.nordicsemi.android.support.v18.scanner.BluetoothLeScannerCompat;`
- `sources/com/viwaveulife/vuioht/VUBleManager.java:81`
  `import no.nordicsemi.android.support.v18.scanner.ScanResult;`
- `sources/com/viwaveulife/vuioht/VUBleManager.java:582`
  `public void onScanResult(int i, ScanResult scanResult) {`
- `sources/com/viwaveulife/vuioht/VUBleManager.java:583`
  `BluetoothDevice device = scanResult.getDevice();`
- `sources/com/viwaveulife/vuioht/VUBleManager.java:590`
  `if (VUBleManager.this.o != null && VUBleManager.this.a(device, scanResult.getScanRecord().getServiceUuids())) {`
- `sources/com/viwaveulife/vuioht/VUBleManager.java:594`
  `vUBleDevice.setRssi(scanResult.getRssi());`
- `sources/com/viwaveulife/vuioht/VUBleManager.java:596`
  `ScanRecord scanRecord = scanResult.getScanRecord();`
- `sources/com/viwaveulife/vuioht/VUBleManager.java:602`
  `VUBleManager.this.o.onScanResult(vUBleDevice);`
- `sources/com/viwaveulife/vuioht/VUBleManager.java:634`
  `public void onScanResult(int i, ScanResult scanResult) {`
- `sources/com/viwaveulife/vuioht/VUBleManager.java:635`
  `BluetoothDevice device = scanResult.getDevice();`
- `sources/com/viwaveulife/vuioht/VUBleManager.java:641`
  `BluetoothLeScannerCompat.getScanner().stopScan(this);`
- `sources/com/viwaveulife/vuioht/VUBleManager.java:745`
  `BluetoothLeScannerCompat scanner = BluetoothLeScannerCompat.getScanner();`
- `sources/com/viwaveulife/vuioht/VUBleManager.java:806`
  `BluetoothLeScannerCompat scanner = BluetoothLeScannerCompat.getScanner();`
- `sources/com/viwaveulife/vuioht/VUBleManager.java:1025`
  `public void startScan(List<VUBleScanFilter> list, int i2) {`
- `sources/com/viwaveulife/vuioht/VUBleManager.java:1081`
  `BluetoothLeScannerCompat.getScanner().stopScan(hVar);`
- `sources/com/viwaveulife/vuioht/VUBleManager.java:1093`
  `BluetoothLeScannerCompat.getScanner().stopScan(this.n);`
- `sources/com/viwaveulife/vuioht/VUBleManager.java:1377`
  `BluetoothLeScannerCompat scanner = BluetoothLeScannerCompat.getScanner();`
- `sources/com/viwaveulife/vuioht/VUBleManager.java:1381`
  `scanner.startScan(null, scanSettingsBuild, hVar);`

## BR044

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/androidx/core/content/ContextCompat.java:43`
  `import android.net.wifi.WifiManager;`
- `sources/androidx/core/content/ContextCompat.java:317`
  `map.put(WifiManager.class, "wifi");`

## BR047

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/a/a.java:66`
  `Log.v(Utility.DEBUG_TAG, "onCharacteristicChanged " + bluetoothGattCharacteristic.getUuid().toString());`
- `sources/a/a.java:95`
  `Log.v(Utility.DEBUG_TAG, "onCharacteristicRead " + bluetoothGattCharacteristic.getUuid().toString() + p.SPACE + i);`
- `sources/a/a.java:112`
  `Log.v(Utility.DEBUG_TAG, "onCharacteristicWrite " + bluetoothGattCharacteristic.getUuid().toString() + p.SPACE + i);`
- `sources/a/a.java:132`
  `Log.v(Utility.DEBUG_TAG, "onConnectionStateChange status:" + i + " newState:" + i2);`
- `sources/a/a.java:135`
  `Log.e(Utility.DEBUG_TAG, "ConnectionStateChange, can't get vuBleDevice");`
- `sources/a/a.java:140`
  `Log.v(Utility.DEBUG_TAG, macAddress + " device disconnected " + i);`
- `sources/a/a.java:148`
  `Log.v(Utility.DEBUG_TAG, macAddress + " device connected");`
- `sources/a/a.java:162`
  `Log.v(Utility.DEBUG_TAG, "attempting to start service discovery:" + a.this.f.discoverServices());`
- `sources/a/a.java:167`
  `Log.v(Utility.DEBUG_TAG, "on Descriptor read " + bluetoothGattDescriptor.getUuid() + ", value: " + Utility.byte2Hex(bluetoothGattDescriptor.getValue()));`
- `sources/a/a.java:187`
  `Log.v(Utility.DEBUG_TAG, "onDescriptorWrite " + bluetoothGattDescriptor.getUuid().toString() + p.SPACE + i);`
- `sources/a/a.java:208`
  `Log.v(Utility.DEBUG_TAG, "onMtuChanged -> " + i);`
- `sources/a/a.java:210`
  `Log.v(Utility.DEBUG_TAG, "attempting to start service discovery:" + a.this.f.discoverServices());`
- `sources/a/a.java:252`
  `Log.w(Utility.DEBUG_TAG, "connect timeout expired, device unknown");`
- `sources/a/a.java:254`
  `Log.v(Utility.DEBUG_TAG, a.this.f8d.getMacAddress() + " timeout expired");`
- `sources/a/a.java:272`
  `Log.i(Utility.DEBUG_TAG, "Bond state changed for: " + bluetoothDevice.getName() + " new state: " + intExtra + " previous: " + intExtra2);`
- `sources/a/a.java:274`
  `Log.v(Utility.DEBUG_TAG, "BOND_BONDING " + a.this.f7c);`
- `sources/a/a.java:559`
  `Log.v(Utility.DEBUG_TAG, "starting pairing");`
- `sources/a/a.java:599`
  `Log.w(Utility.DEBUG_TAG, "BluetoothAdapter not initialized");`
- `sources/a/a.java:604`
  `Log.w(Utility.DEBUG_TAG, "BluetoothGatt not initialized");`
- `sources/a/a.java:609`
  `Log.v(Utility.DEBUG_TAG, "\tdevice NOT connected, call onDisconnect");`
- `sources/a/a.java:627`
  `Log.e(Utility.DEBUG_TAG, "Unable to initialize BluetoothManager.");`
- `sources/a/a.java:634`
  `Log.e(Utility.DEBUG_TAG, "Unable to obtain a BluetoothAdapter.");`
- `sources/a/a.java:646`
  `Log.v(Utility.DEBUG_TAG, "read Characteristic " + bluetoothGattCharacteristic.getUuid());`
- `sources/a/a.java:649`
  `Log.w(Utility.DEBUG_TAG, "BluetoothAdapter not initialized");`
- `sources/a/a.java:807`
  `Log.v(Utility.DEBUG_TAG, "Write Descriptor " + bluetoothGattDescriptor.getUuid());`
- `sources/a/a.java:850`
  `Log.w(Utility.DEBUG_TAG, "BluetoothAdapter not initialized");`
- `sources/a/a.java:855`
  `Log.w(Utility.DEBUG_TAG, macAddress + " is not a valid Bluetooth address.");`
- `sources/a/a.java:859`
  `Log.v(Utility.DEBUG_TAG, "Can't connect, Connecting State " + this.g);`
- `sources/a/a.java:865`
  `Log.w(Utility.DEBUG_TAG, "Device not found.  Unable to connect.");`
- `sources/a/a.java:868`
  `Log.d(Utility.DEBUG_TAG, vUBleDevice.getMacAddress() + " create a new connection.");`
- `sources/a/a.java:892`
  `Log.v(Utility.DEBUG_TAG, "write Characteristic " + bluetoothGattCharacteristic.getUuid() + p.SPACE + Utility.byte2Hex(bArr));`
- `sources/a/a.java:895`
  `Log.w(Utility.DEBUG_TAG, "BluetoothAdapter not initialized");`
- `sources/a/a.java:907`
  `Log.v(Utility.DEBUG_TAG, "Read Descriptor " + bluetoothGattDescriptor.getUuid());`
- `sources/android/support/v4/media/MediaBrowserCompat.java:649`
  `Log.d(MediaBrowserCompat.TAG, "addSubscription failed with RemoteException parentId=" + str);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:743`
  `Log.i(MediaBrowserCompat.TAG, "Remote error sending a custom action: action=" + str + ", extras=" + bundle, e2);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:759`
  `Log.w(MediaBrowserCompat.TAG, "onConnect from service while mState=" + getStateLabel(this.mState) + "... ignoring");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:881`
  `Log.d(MediaBrowserCompat.TAG, "  mServiceBinderWrapper=" + this.mServiceBinderWrapper);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:882`
  `Log.d(MediaBrowserCompat.TAG, "  mCallbacksMessenger=" + this.mCallbacksMessenger);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:883`
  `Log.d(MediaBrowserCompat.TAG, "  mRootId=" + this.mRootId);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:884`
  `Log.d(MediaBrowserCompat.TAG, "  mMediaSessionToken=" + this.mMediaSessionToken);`

## BR050

paper_id: B021
paper_title: Metadata-Based Privacy Assessment for Mobile mHealth

- `rossmax_audit_report_zh.md:116`
  `- 'SetRegionActivity'：同样开启 JS 和 popup，加载 S3 privacy 页面，见 'sources/com/viwave/rossmaxconnect/SetRegionActivity.java:240-319'。`
- `rossmax_audit_report_zh.md:166`
  `- 'BuildConfig.BASE_URL'、'API_URL'、S3 privacy URL，见 'sources/com/viwave/rossmaxconnect/BuildConfig.java:5-11'。`
- `rossmax_audit_report_zh.md:168`
  `### R057 / P015 / Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android`
- `rossmax_audit_report_zh.md:348`
  `- R037-R040 / P010、R061/R063/R067/R088：需要隐私政策全文、商店 Data Safety/label、动态流量和 SDK 配置对照。当前只有 privacy URL，没有本地政策正文。`
- `rossmax_audit_report_zh.md:358`
  `3. WebView region 链路：本地 Activity 加载 S3 privacy/region 页 -> JS prompt 'message=region' -> native 保存 'regionShortCode' -> 用户同意 -> Firestore profile region 写入。风险集中在 origin 未校验。`
- `rossmax_audit_report_zh.md:360`
  `5. 第三方 SDK/consent 链路：Manifest providers 自动初始化 Firebase/Facebook -> App 后续展示 privacy/region 页面 -> 未看到显式 Facebook privacy toggles。当前缺少启动抓包。`
- `rossmax_audit_report_zh.md:365`
  `2. 用 mitmproxy/PCAP 抓冷启动、拒绝/同意 privacy、登录、测量、云同步、删除账号流程：验证 R041/R043/R044/R064/R065/R085-R087。`
- `rossmax_evidence_chains_zh.md:192`
  `1. 加载 S3 privacy/region 页面：`
- `rossmax_evidence_chains_zh.md:193`
  `- 'https://rossmax-care-static-web-page.s3-ap-northeast-1.amazonaws.com/privacy/rossmax.html?...'`
- `rossmax_rule_mapping_zh.md:29`
  `| R023 | P006 | Why Eve and Mallory Love Android: An Analysis of Android SSL (in)Security | 'not_supported' | 核心 API、Cloud Functions、S3 privacy URL 均为 HTTPS；零散 'http://' 来自第三方元数据/文档样式，不是业务 sink。 |`
- `rossmax_rule_mapping_zh.md:43`
  `| R037 | P010 | PolicyLint: Investigating Internal Privacy Policy Contradictions on Google Play | 'not_testable' | 无本地隐私政策正文，只有 URL；不能检查政策内部矛盾。 |`
- `rossmax_rule_mapping_zh.md:44`
  `| R038 | P010 | PolicyLint: Investigating Internal Privacy Policy Contradictions on Google Play | 'not_testable' | 需要政策正文和流量/SDK 接收方对照。 |`
- `rossmax_rule_mapping_zh.md:45`
  `| R039 | P010 | PolicyLint: Investigating Internal Privacy Policy Contradictions on Google Play | 'not_testable' | 需要 consent/opt-out 声明与运行行为对照。 |`
- `rossmax_rule_mapping_zh.md:46`
  `| R040 | P010 | PolicyLint: Investigating Internal Privacy Policy Contradictions on Google Play | 'not_testable' | 需要政策正文和技术能力/实际流量对照。 |`
- `rossmax_rule_mapping_zh.md:59`
  `| R053 | P014 | Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment | 'not_testable' | 当前无法判断 App 是否 accredited。 |`
- `rossmax_rule_mapping_zh.md:60`
  `| R054 | P014 | Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment | 'not_supported' | 未发现健康测量值本地明文 cache；只见私有 prefs 保存设备状态/设置。 |`
- `resources/res/values/strings.xml:425`
  `<string name="login_agreement">TERMS OF USE AND PRIVACY POLICY</string>`
- `resources/res/values-it-rIT/strings.xml:261`
  `<string name="login_agreement">TERMINI DI UTILIZZO E PRIVACY</string>`

## BR051

paper_id: B013
paper_title: Availability and quality of mobile health app privacy policies

- `rossmax_audit_report_zh.md:36`
  `- 原论文快照已用于校准证据门槛，尤其是 BLE 应用层安全（P019/P020/P021）、Facebook SDK privacy settings（P022）、Deep Link（P007）、WebView DCV（P008/P009）、mHealth 安全（P013/P018）。`
- `rossmax_audit_report_zh.md:141`
  `- P022 快照说明 Facebook SDK privacy settings/defaults 是评估对象，见 'C:\wujiangliang\app\xiangshan\database\snapshots\P022-popets-facebook-sdk-settings.html:61-62'。`
- `rossmax_audit_report_zh.md:166`
  `- 'BuildConfig.BASE_URL'、'API_URL'、S3 privacy URL，见 'sources/com/viwave/rossmaxconnect/BuildConfig.java:5-11'。`
- `rossmax_audit_report_zh.md:187`
  `### R060 / P015 / Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android`
- `rossmax_audit_report_zh.md:195`
  `### R062 / P016 / Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation`
- `rossmax_audit_report_zh.md:203`
  `### R064 / P016 / Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation`
- `rossmax_audit_report_zh.md:211`
  `### R065 / P017 / Mobile health and privacy: cross sectional study`
- `rossmax_audit_report_zh.md:304`
  `### R085 / P022 / Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs`
- `rossmax_audit_report_zh.md:308`
  `Facebook SDK 配置存在，未看到一方代码显式设置更保守的 privacy toggles。P022 关注 Facebook SDK 默认隐私设置和开发者是否修改设置。无运行期 SDK 配置/流量，不能确认实际默认行为。`
- `rossmax_audit_report_zh.md:312`
  `### R086 / P022 / Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs`
- `rossmax_audit_report_zh.md:320`
  `### R087 / P022 / Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs`
- `rossmax_audit_report_zh.md:324`
  `'FacebookInitProvider' 在 Manifest 中声明，通常会早于用户进入 privacy/region consent 页面初始化。由于没有启动抓包或 SDK 日志，不能确认是否在同意前发送数据。`
- `rossmax_audit_report_zh.md:348`
  `- R037-R040 / P010、R061/R063/R067/R088：需要隐私政策全文、商店 Data Safety/label、动态流量和 SDK 配置对照。当前只有 privacy URL，没有本地政策正文。`
- `rossmax_audit_report_zh.md:358`
  `3. WebView region 链路：本地 Activity 加载 S3 privacy/region 页 -> JS prompt 'message=region' -> native 保存 'regionShortCode' -> 用户同意 -> Firestore profile region 写入。风险集中在 origin 未校验。`
- `rossmax_audit_report_zh.md:360`
  `5. 第三方 SDK/consent 链路：Manifest providers 自动初始化 Firebase/Facebook -> App 后续展示 privacy/region 页面 -> 未看到显式 Facebook privacy toggles。当前缺少启动抓包。`
- `rossmax_audit_report_zh.md:365`
  `2. 用 mitmproxy/PCAP 抓冷启动、拒绝/同意 privacy、登录、测量、云同步、删除账号流程：验证 R041/R043/R044/R064/R065/R085-R087。`
- `rossmax_rule_mapping_zh.md:29`
  `| R023 | P006 | Why Eve and Mallory Love Android: An Analysis of Android SSL (in)Security | 'not_supported' | 核心 API、Cloud Functions、S3 privacy URL 均为 HTTPS；零散 'http://' 来自第三方元数据/文档样式，不是业务 sink。 |`
- `rossmax_rule_mapping_zh.md:43`
  `| R037 | P010 | PolicyLint: Investigating Internal Privacy Policy Contradictions on Google Play | 'not_testable' | 无本地隐私政策正文，只有 URL；不能检查政策内部矛盾。 |`
- `rossmax_rule_mapping_zh.md:44`
  `| R038 | P010 | PolicyLint: Investigating Internal Privacy Policy Contradictions on Google Play | 'not_testable' | 需要政策正文和流量/SDK 接收方对照。 |`
- `rossmax_rule_mapping_zh.md:45`
  `| R039 | P010 | PolicyLint: Investigating Internal Privacy Policy Contradictions on Google Play | 'not_testable' | 需要 consent/opt-out 声明与运行行为对照。 |`
- `rossmax_rule_mapping_zh.md:46`
  `| R040 | P010 | PolicyLint: Investigating Internal Privacy Policy Contradictions on Google Play | 'not_testable' | 需要政策正文和技术能力/实际流量对照。 |`
- `rossmax_rule_mapping_zh.md:59`
  `| R053 | P014 | Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment | 'not_testable' | 当前无法判断 App 是否 accredited。 |`
- `rossmax_rule_mapping_zh.md:60`
  `| R054 | P014 | Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment | 'not_supported' | 未发现健康测量值本地明文 cache；只见私有 prefs 保存设备状态/设置。 |`
- `rossmax_rule_mapping_zh.md:61`
  `| R055 | P014 | Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment | 'not_testable' | 需要设备取证或 app data dump。 |`
- `rossmax_rule_mapping_zh.md:62`
  `| R056 | P014 | Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment | 'not_testable' | 需要商店页面、认证/信任标识、隐私材料。 |`
- `rossmax_rule_mapping_zh.md:63`
  `| R057 | P015 | Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android | 'supported_hypothesis' | 高敏健康数据 + 日志暴露面 + 云同步 + BLE 应用层保护不明；无动态确认。 |`
- `rossmax_rule_mapping_zh.md:64`
  `| R058 | P015 | Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android | 'not_supported' | App 目的和数据类别总体一致：健康设备连接、测量、护理分享。 |`
- `rossmax_rule_mapping_zh.md:65`
  `| R059 | P015 | Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android | 'supported_hypothesis' | 健康数据同步 Firestore，护理 dashboard 查询最近测量；证据 'FirebaseVitalStore.java:186'、'DataManager.java:387-390'。 |`
- `rossmax_rule_mapping_zh.md:66`
  `| R060 | P015 | Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android | 'supported_hypothesis' | 'uid' 路径、deviceSKU/deviceRecKey、测量时间、健康数值组合具备再识别风险；无实际外泄证据。 |`
- `rossmax_rule_mapping_zh.md:67`
  `| R061 | P016 | Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation | 'not_testable' | 需要隐私政策正文与第三方分享行为对照。 |`
- `rossmax_rule_mapping_zh.md:68`
  `| R062 | P016 | Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation | 'supported_hypothesis' | Firebase Analytics 'vital_unit' 上报 bp/bg/wt/tp 有无和单位；证据 'FireAnalytics.java:55-64'。 |`
- `rossmax_rule_mapping_zh.md:69`
  `| R063 | P016 | Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation | 'not_testable' | 需要政策和观测流量。 |`
- `rossmax_rule_mapping_zh.md:70`
  `| R064 | P016 | Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation | 'supported_hypothesis' | Firebase Analytics 收到健康上下文事件；缺抓包确认稳定标识组合。 |`
- `rossmax_rule_mapping_zh.md:71`
  `| R065 | P017 | Mobile health and privacy: cross sectional study | 'supported_hypothesis' | mHealth App 嵌入 Firebase Analytics/Facebook SDK；证据 'AndroidManifest.xml:265-282'、'FireAnalytics.java:34-64'。 |`
- `rossmax_rule_mapping_zh.md:72`
  `| R066 | P017 | Mobile health and privacy: cross sectional study | 'not_supported' | 静态端点为 HTTPS，未见弱 TLS；无 pcap 不能确认所有运行期路径。 |`
- `rossmax_rule_mapping_zh.md:73`
  `| R067 | P017 | Mobile health and privacy: cross sectional study | 'not_testable' | 需要政策正文和观测到的第三方分享。 |`
- `rossmax_rule_mapping_zh.md:74`
  `| R068 | P017 | Mobile health and privacy: cross sectional study | 'not_supported' | 危险权限大多与 BLE/QR/网络功能一致；未见证书弱处理。 |`
- `rossmax_rule_mapping_zh.md:91`
  `| R085 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | 'supported_hypothesis' | Facebook SDK 配置存在，未见显式关闭/保守 privacy settings；无运行期 SDK state。 |`
- `rossmax_rule_mapping_zh.md:92`
  `| R086 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | 'supported_hypothesis' | 未发现 'setAutoLogAppEventsEnabled'、'setAdvertiserIDCollectionEnabled'、'setDataProcessingOptions'。 |`
- `rossmax_rule_mapping_zh.md:93`
  `| R087 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | 'supported_hypothesis' | 'FacebookInitProvider' 自动初始化可能早于 consent；无启动抓包确认外发。 |`
- `rossmax_rule_mapping_zh.md:94`
  `| R088 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | 'not_testable' | 需要披露材料/隐私标签与实际 SDK 配置对照。 |`
- `rossmax_rule_mapping_zh.md:95`
  `| R089 | P023 | Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android | 'not_supported' | BLE scanning 是功能性设备连接；未发现无线扫描 profiling SDK。 |`
- `rossmax_rule_mapping_zh.md:96`
  `| R090 | P023 | Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android | 'not_supported' | 未见 scan data 与稳定标识发送给 profiling 服务。 |`
- `rossmax_rule_mapping_zh.md:97`
  `| R091 | P023 | Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android | 'not_supported' | 'BLUETOOTH_SCAN' 标记 'neverForLocation'，BLE/location 用于设备连接；无 location surrogate profiling 证据。 |`
- `rossmax_rule_mapping_zh.md:98`
  `| R092 | P023 | Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android | 'not_supported' | 无 profiling SDK 和远程扫描流量证据。 |`

## BR052

paper_id: B013
paper_title: Availability and quality of mobile health app privacy policies

- `rossmax_audit_report_zh.md:36`
  `- 原论文快照已用于校准证据门槛，尤其是 BLE 应用层安全（P019/P020/P021）、Facebook SDK privacy settings（P022）、Deep Link（P007）、WebView DCV（P008/P009）、mHealth 安全（P013/P018）。`
- `rossmax_audit_report_zh.md:116`
  `- 'SetRegionActivity'：同样开启 JS 和 popup，加载 S3 privacy 页面，见 'sources/com/viwave/rossmaxconnect/SetRegionActivity.java:240-319'。`
- `rossmax_audit_report_zh.md:141`
  `- P022 快照说明 Facebook SDK privacy settings/defaults 是评估对象，见 'C:\wujiangliang\app\xiangshan\database\snapshots\P022-popets-facebook-sdk-settings.html:61-62'。`
- `rossmax_audit_report_zh.md:166`
  `- 'BuildConfig.BASE_URL'、'API_URL'、S3 privacy URL，见 'sources/com/viwave/rossmaxconnect/BuildConfig.java:5-11'。`
- `rossmax_audit_report_zh.md:168`
  `### R057 / P015 / Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android`
- `rossmax_audit_report_zh.md:176`
  `### R059 / P015 / Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android`
- `rossmax_audit_report_zh.md:187`
  `### R060 / P015 / Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android`
- `rossmax_audit_report_zh.md:195`
  `### R062 / P016 / Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation`
- `rossmax_audit_report_zh.md:203`
  `### R064 / P016 / Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation`
- `rossmax_audit_report_zh.md:211`
  `### R065 / P017 / Mobile health and privacy: cross sectional study`
- `rossmax_audit_report_zh.md:358`
  `3. WebView region 链路：本地 Activity 加载 S3 privacy/region 页 -> JS prompt 'message=region' -> native 保存 'regionShortCode' -> 用户同意 -> Firestore profile region 写入。风险集中在 origin 未校验。`
- `rossmax_audit_report_zh.md:360`
  `5. 第三方 SDK/consent 链路：Manifest providers 自动初始化 Firebase/Facebook -> App 后续展示 privacy/region 页面 -> 未看到显式 Facebook privacy toggles。当前缺少启动抓包。`
- `rossmax_audit_report_zh.md:365`
  `2. 用 mitmproxy/PCAP 抓冷启动、拒绝/同意 privacy、登录、测量、云同步、删除账号流程：验证 R041/R043/R044/R064/R065/R085-R087。`
- `rossmax_evidence_chains_zh.md:192`
  `1. 加载 S3 privacy/region 页面：`
- `rossmax_evidence_chains_zh.md:193`
  `- 'https://rossmax-care-static-web-page.s3-ap-northeast-1.amazonaws.com/privacy/rossmax.html?...'`
- `rossmax_rule_mapping_zh.md:59`
  `| R053 | P014 | Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment | 'not_testable' | 当前无法判断 App 是否 accredited。 |`
- `rossmax_rule_mapping_zh.md:60`
  `| R054 | P014 | Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment | 'not_supported' | 未发现健康测量值本地明文 cache；只见私有 prefs 保存设备状态/设置。 |`
- `rossmax_rule_mapping_zh.md:61`
  `| R055 | P014 | Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment | 'not_testable' | 需要设备取证或 app data dump。 |`
- `rossmax_rule_mapping_zh.md:62`
  `| R056 | P014 | Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment | 'not_testable' | 需要商店页面、认证/信任标识、隐私材料。 |`
- `rossmax_rule_mapping_zh.md:63`
  `| R057 | P015 | Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android | 'supported_hypothesis' | 高敏健康数据 + 日志暴露面 + 云同步 + BLE 应用层保护不明；无动态确认。 |`
- `rossmax_rule_mapping_zh.md:64`
  `| R058 | P015 | Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android | 'not_supported' | App 目的和数据类别总体一致：健康设备连接、测量、护理分享。 |`
- `rossmax_rule_mapping_zh.md:65`
  `| R059 | P015 | Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android | 'supported_hypothesis' | 健康数据同步 Firestore，护理 dashboard 查询最近测量；证据 'FirebaseVitalStore.java:186'、'DataManager.java:387-390'。 |`
- `rossmax_rule_mapping_zh.md:66`
  `| R060 | P015 | Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android | 'supported_hypothesis' | 'uid' 路径、deviceSKU/deviceRecKey、测量时间、健康数值组合具备再识别风险；无实际外泄证据。 |`
- `rossmax_rule_mapping_zh.md:67`
  `| R061 | P016 | Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation | 'not_testable' | 需要隐私政策正文与第三方分享行为对照。 |`
- `rossmax_rule_mapping_zh.md:68`
  `| R062 | P016 | Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation | 'supported_hypothesis' | Firebase Analytics 'vital_unit' 上报 bp/bg/wt/tp 有无和单位；证据 'FireAnalytics.java:55-64'。 |`
- `rossmax_rule_mapping_zh.md:69`
  `| R063 | P016 | Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation | 'not_testable' | 需要政策和观测流量。 |`
- `rossmax_rule_mapping_zh.md:70`
  `| R064 | P016 | Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation | 'supported_hypothesis' | Firebase Analytics 收到健康上下文事件；缺抓包确认稳定标识组合。 |`
- `rossmax_rule_mapping_zh.md:71`
  `| R065 | P017 | Mobile health and privacy: cross sectional study | 'supported_hypothesis' | mHealth App 嵌入 Firebase Analytics/Facebook SDK；证据 'AndroidManifest.xml:265-282'、'FireAnalytics.java:34-64'。 |`
- `rossmax_rule_mapping_zh.md:72`
  `| R066 | P017 | Mobile health and privacy: cross sectional study | 'not_supported' | 静态端点为 HTTPS，未见弱 TLS；无 pcap 不能确认所有运行期路径。 |`
- `rossmax_rule_mapping_zh.md:73`
  `| R067 | P017 | Mobile health and privacy: cross sectional study | 'not_testable' | 需要政策正文和观测到的第三方分享。 |`
- `rossmax_rule_mapping_zh.md:74`
  `| R068 | P017 | Mobile health and privacy: cross sectional study | 'not_supported' | 危险权限大多与 BLE/QR/网络功能一致；未见证书弱处理。 |`
- `rossmax_rule_mapping_zh.md:91`
  `| R085 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | 'supported_hypothesis' | Facebook SDK 配置存在，未见显式关闭/保守 privacy settings；无运行期 SDK state。 |`
- `rossmax_rule_mapping_zh.md:92`
  `| R086 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | 'supported_hypothesis' | 未发现 'setAutoLogAppEventsEnabled'、'setAdvertiserIDCollectionEnabled'、'setDataProcessingOptions'。 |`
- `rossmax_rule_mapping_zh.md:93`
  `| R087 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | 'supported_hypothesis' | 'FacebookInitProvider' 自动初始化可能早于 consent；无启动抓包确认外发。 |`
- `rossmax_rule_mapping_zh.md:94`
  `| R088 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | 'not_testable' | 需要披露材料/隐私标签与实际 SDK 配置对照。 |`
- `rossmax_rule_mapping_zh.md:95`
  `| R089 | P023 | Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android | 'not_supported' | BLE scanning 是功能性设备连接；未发现无线扫描 profiling SDK。 |`
- `rossmax_rule_mapping_zh.md:96`
  `| R090 | P023 | Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android | 'not_supported' | 未见 scan data 与稳定标识发送给 profiling 服务。 |`
- `rossmax_rule_mapping_zh.md:97`
  `| R091 | P023 | Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android | 'not_supported' | 'BLUETOOTH_SCAN' 标记 'neverForLocation'，BLE/location 用于设备连接；无 location surrogate profiling 证据。 |`
- `rossmax_rule_mapping_zh.md:98`
  `| R092 | P023 | Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android | 'not_supported' | 无 profiling SDK 和远程扫描流量证据。 |`
- `resources/res/values/public.xml:6712`
  `<public type="string" name="about_terms_and_privacy" id="0x7f130021" />`
- `resources/res/values/strings.xml:36`
  `<string name="about_terms_and_privacy">Terms and Privacy</string>`
- `resources/res/values/strings.xml:300`
  `<string name="dlg_no_region_code_message">You have not yet selected your current region. Please select your current region and accept the terms of use and privacy policy to continue.</string>`
- `resources/res/values/strings.xml:425`
  `<string name="login_agreement">TERMS OF USE AND PRIVACY POLICY</string>`
- `resources/res/values-ar/strings.xml:36`
  `<string name="about_terms_and_privacy">البنود والخصوصية</string>`
- `resources/res/values-de-rDE/strings.xml:9`
  `<string name="about_terms_and_privacy">Bedingungen und Datenschutz</string>`
- `resources/res/values-fr-rFR/strings.xml:9`
  `<string name="about_terms_and_privacy">Conditions et confidentialité</string>`
- `resources/res/values-it-rIT/strings.xml:9`
  `<string name="about_terms_and_privacy">Termini e Privacy</string>`
- `resources/res/values-it-rIT/strings.xml:178`
  `<string name="dlg_no_region_code_message">Non è ancora stata selezionata regione attuale. Selezionare la regione attuale e accettare i termini di utilizzo e l\'informativa sulla privacy per continuare.</string>`
- `resources/res/values-it-rIT/strings.xml:261`
  `<string name="login_agreement">TERMINI DI UTILIZZO E PRIVACY</string>`
- `resources/res/values-ms/strings.xml:36`
  `<string name="about_terms_and_privacy">Terma dan Privasi</string>`
- `resources/res/values-th-rTH/strings.xml:9`
  `<string name="about_terms_and_privacy">ข้อกำหนดและความเป็นส่วนตัว</string>`
- `resources/res/values-zh-rTW/strings.xml:36`
  `<string name="about_terms_and_privacy">使用條款與政策</string>`

## BR055

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `sources/androidx/core/util/PatternsCompat.java:15`
  `static final String IANA_TOP_LEVEL_DOMAINS = "(?:(?:aaa|aarp|abb|abbott|abbvie|abc|able|abogado|abudhabi|academy|accenture|accountant|accountants|aco|actor|ads|adult|aeg|aero|aetna|afl|africa|agakhan|agency|aig|airbus|airforce|airtel|akdn|alibaba|alipay|allfinanz|allstate|ally|alsace|alstom|amazon|a...`
- `sources/androidx/core/util/PatternsCompat.java:25`
  `private static final String STRICT_HOST_NAME = "(?:(?:[a-zA-Z0-9[ -\ud7ff豈-﷏ﷰ-\uffef𐀀-\u1fffd𠀀-\u2fffd𰀀-\u3fffd\u40000-\u4fffd\u50000-\u5fffd\u60000-\u6fffd\u70000-\u7fffd\u80000-\u8fffd\u90000-\u9fffd\ua0000-\uafffd\ub0000-\ubfffd\uc0000-\ucfffd\ud0000-\udfffd\ue1000-\uefffd&&[^ [\u2000-\u200a]\u20...`
- `sources/androidx/core/util/PatternsCompat.java:26`
  `private static final String STRICT_TLD = "(?:(?:(?:aaa|aarp|abb|abbott|abbvie|abc|able|abogado|abudhabi|academy|accenture|accountant|accountants|aco|actor|ads|adult|aeg|aero|aetna|afl|africa|agakhan|agency|aig|airbus|airforce|airtel|akdn|alibaba|alipay|allfinanz|allstate|ally|alsace|alstom|amazon|am...`
- `sources/androidx/core/util/PatternsCompat.java:42`
  `Pattern patternCompile3 = Pattern.compile("(?:(?:(?:[a-zA-Z0-9[ -\ud7ff豈-﷏ﷰ-\uffef𐀀-\u1fffd𠀀-\u2fffd𰀀-\u3fffd\u40000-\u4fffd\u50000-\u5fffd\u60000-\u6fffd\u70000-\u7fffd\u80000-\u8fffd\u90000-\u9fffd\ua0000-\uafffd\ub0000-\ubfffd\uc0000-\ucfffd\ud0000-\udfffd\ue1000-\uefffd&&[^ [\u2000-\u200a]\u2028...`

## BR058

paper_id: B022
paper_title: A Study of Android Application Security

- `rossmax_audit_report_zh.md:130`
  `### R041 / P011 / A Fait Accompli? An Empirical Study into the Absence of Consent to Third-Party Tracking in Android Apps`
- `rossmax_audit_report_zh.md:304`
  `### R085 / P022 / Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs`
- `rossmax_audit_report_zh.md:312`
  `### R086 / P022 / Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs`
- `rossmax_audit_report_zh.md:320`
  `### R087 / P022 / Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs`
- `rossmax_evidence_chains_zh.md:261`
  `## 5. Third-party SDK / consent 链路`
- `rossmax_rule_mapping_zh.md:47`
  `| R041 | P011 | A Fait Accompli? An Empirical Study into the Absence of Consent to Third-Party Tracking in Android Apps | 'supported_hypothesis' | FacebookInitProvider 自动初始化，未见一方隐私开关；无启动抓包，不能确认外发。证据 'AndroidManifest.xml:265-269'。 |`
- `rossmax_rule_mapping_zh.md:48`
  `| R042 | P011 | A Fait Accompli? An Empirical Study into the Absence of Consent to Third-Party Tracking in Android Apps | 'not_testable' | 需要拒绝/同意前后动态流量，当前无抓包。 |`
- `rossmax_rule_mapping_zh.md:49`
  `| R043 | P011 | A Fait Accompli? An Empirical Study into the Absence of Consent to Third-Party Tracking in Android Apps | 'not_testable' | SDK 可能初始化早于隐私页面，但缺少运行期标识采集证据。 |`
- `rossmax_rule_mapping_zh.md:50`
  `| R044 | P011 | A Fait Accompli? An Empirical Study into the Absence of Consent to Third-Party Tracking in Android Apps | 'not_testable' | 需要 decline 后抓包和 SDK state。 |`
- `rossmax_rule_mapping_zh.md:91`
  `| R085 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | 'supported_hypothesis' | Facebook SDK 配置存在，未见显式关闭/保守 privacy settings；无运行期 SDK state。 |`
- `rossmax_rule_mapping_zh.md:92`
  `| R086 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | 'supported_hypothesis' | 未发现 'setAutoLogAppEventsEnabled'、'setAdvertiserIDCollectionEnabled'、'setDataProcessingOptions'。 |`
- `rossmax_rule_mapping_zh.md:93`
  `| R087 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | 'supported_hypothesis' | 'FacebookInitProvider' 自动初始化可能早于 consent；无启动抓包确认外发。 |`
- `rossmax_rule_mapping_zh.md:94`
  `| R088 | P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | 'not_testable' | 需要披露材料/隐私标签与实际 SDK 配置对照。 |`
- `resources/META-INF/androidx/annotation/annotation/LICENSE.txt:116`
  `wherever such third-party notices normally appear. The contents`
- `resources/META-INF/androidx/constraintlayout/constraintlayout-core/LICENSE.txt:116`
  `wherever such third-party notices normally appear. The contents`
- `resources/META-INF/androidx/lifecycle/lifecycle-common/LICENSE.txt:116`
  `wherever such third-party notices normally appear. The contents`
- `sources/androidx/navigation/serialization/NavTypeConverterKt.java:204`
  `throw new IllegalStateException(("Cannot find KSerializer for [" + serialDescriptor.getSerialName() + "]. If applicable, custom KSerializers for custom and third-party KType is currently not supported when declared directly on a class field via @Serializable(with = ...). Please use @Serializable or ...`

## BR059

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/AndroidManifest.xml:95`
  `<intent-filter>`
- `resources/AndroidManifest.xml:99`
  `<intent-filter android:autoVerify="true">`
- `resources/AndroidManifest.xml:202`
  `<intent-filter>`

## BR060

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzyq.java:16`
  `return zzzd.zza.zza("AES/ECB/NOPADDING");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzzw.java:16`
  `return zzzd.zza.zza("AES/ECB/NoPadding");`
- `sources/com/viwaveulife/vuioht/BuildConfig.java:6`
  `public static final String CIPHER_TRANSFORMATION = "AES/CBC/PKCS5Padding";`

## BR061

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/a/a.java:891`
  `bluetoothGattCharacteristic.setValue(bArr);`
- `sources/a/a.java:893`
  `return this.f.writeCharacteristic(bluetoothGattCharacteristic);`
- `sources/androidx/constraintlayout/core/motion/Motion.java:1340`
  `public boolean setValue(int i, float f) {`
- `sources/androidx/constraintlayout/core/state/WidgetFrame.java:422`
  `public boolean setValue(String str, CLElement cLElement) throws CLParsingException {`
- `sources/androidx/constraintlayout/motion/widget/KeyAttributes.java:303`
  `public void setValue(String str, Object obj) {`
- `sources/androidx/constraintlayout/motion/widget/KeyCycle.java:524`
  `public void setValue(String str, Object obj) {`
- `sources/androidx/constraintlayout/motion/widget/KeyTimeCycle.java:289`
  `public void setValue(String str, Object obj) {`
- `sources/androidx/constraintlayout/motion/widget/KeyTrigger.java:84`
  `public void setValue(String str, Object obj) {`
- `sources/androidx/core/view/inputmethod/EditorInfoCompat.java:24`
  `static int getProtocol(EditorInfo editorInfo) {`
- `sources/androidx/datastore/preferences/protobuf/Any.java:53`
  `public void setValue(ByteString value) {`
- `sources/androidx/datastore/preferences/protobuf/Any.java:161`
  `public Builder setValue(ByteString value) {`
- `sources/androidx/datastore/preferences/protobuf/Any.java:163`
  `((Any) this.instance).setValue(value);`
- `sources/androidx/datastore/preferences/protobuf/BytesValue.java:24`
  `public void setValue(ByteString value) {`
- `sources/androidx/datastore/preferences/protobuf/BytesValue.java:104`
  `public Builder setValue(ByteString value) {`
- `sources/androidx/datastore/preferences/protobuf/BytesValue.java:106`
  `((BytesValue) this.instance).setValue(value);`
- `sources/androidx/datastore/preferences/protobuf/BytesValue.java:203`
  `return newBuilder().setValue(value).build();`
- `sources/androidx/datastore/preferences/protobuf/DescriptorProtos.java:11312`
  `public void setValue(String value) {`
- `sources/androidx/datastore/preferences/protobuf/DescriptorProtos.java:11432`
  `public Builder setValue(String value) {`
- `sources/androidx/datastore/preferences/protobuf/DescriptorProtos.java:11434`
  `((EditionDefault) this.instance).setValue(value);`
- `sources/androidx/datastore/preferences/protobuf/LazyFieldLite.java:85`
  `public MessageLite setValue(MessageLite value) {`
- `sources/androidx/datastore/preferences/protobuf/LazyFieldLite.java:111`
  `setValue(mergeValueAndBytes(other.value, this.delayedBytes, this.extensionRegistry));`
- `sources/androidx/datastore/preferences/protobuf/LazyFieldLite.java:113`
  `setValue(mergeValueAndBytes(this.value, other.delayedBytes, other.extensionRegistry));`
- `sources/androidx/datastore/preferences/protobuf/LazyFieldLite.java:115`
  `setValue(this.value.toBuilder().mergeFrom(other.value).build());`
- `sources/androidx/datastore/preferences/protobuf/LazyFieldLite.java:132`
  `setValue(this.value.toBuilder().mergeFrom(input, extensionRegistry).build());`
- `sources/androidx/datastore/preferences/protobuf/StringValue.java:29`
  `public void setValue(String value) {`
- `sources/androidx/datastore/preferences/protobuf/StringValue.java:120`
  `public Builder setValue(String value) {`
- `sources/androidx/datastore/preferences/protobuf/StringValue.java:122`
  `((StringValue) this.instance).setValue(value);`
- `sources/androidx/lifecycle/LiveData.java:43`
  `LiveData.this.setValue(obj);`
- `sources/androidx/lifecycle/LiveData.java:65`
  `LiveData.this.setValue(obj2);`
- `sources/androidx/navigation/NavigatorState.java:65`
  `this._backStack.setValue(CollectionsKt.plus((Collection<? extends NavBackStackEntry>) this._backStack.getValue(), backStackEntry));`
- `sources/androidx/navigation/NavigatorState.java:98`
  `mutableStateFlow2.setValue(SetsKt.plus(mutableStateFlow2.getValue(), backStackEntry));`
- `sources/androidx/preference/SeekBarPreference.java:228`
  `public void setValue(int i) {`
- `sources/c/b.java:407`
  `bluetoothGattCharacteristicD.setValue(new byte[7]);`
- `sources/c/b.java:408`
  `bluetoothGattCharacteristicD.setValue(i, 18, 0);`
- `sources/c/b.java:409`
  `bluetoothGattCharacteristicD.setValue(i2, 17, 2);`
- `sources/c/b.java:410`
  `bluetoothGattCharacteristicD.setValue(i3, 17, 3);`
- `sources/c/b.java:411`
  `bluetoothGattCharacteristicD.setValue(i4, 17, 4);`
- `sources/c/b.java:412`
  `bluetoothGattCharacteristicD.setValue(i5, 17, 5);`
- `sources/c/b.java:413`
  `bluetoothGattCharacteristicD.setValue(i6, 17, 6);`
- `sources/c/b.java:483`
  `bluetoothGattCharacteristic.setValue(new byte[(numArr.length > 0 ? 1 : 0) + 2 + (numArr.length * 2)]);`

## BR062

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/com/viwave/rossmaxconnect/advfragment/measure/vulistener/BGMeasureListener.java:21`
  `@Metadata(d1 = {"\u0000r\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0010\u0006\n\u0000...`
- `sources/com/viwave/rossmaxconnect/advfragment/measure/vulistener/BGMeasureListener.java:36`
  `public void onCharacteristicReadError(VUBleDevice p0, BluetoothGattCharacteristic p1, int p2) {`
- `sources/com/viwave/rossmaxconnect/advfragment/measure/vulistener/BPMeasureListener.java:21`
  `@Metadata(d1 = {"\u0000n\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0010\u0006\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u...`
- `sources/com/viwave/rossmaxconnect/advfragment/measure/vulistener/BPMeasureListener.java:28`
  `public void onCharacteristicReadError(VUBleDevice p0, BluetoothGattCharacteristic p1, int p2) {`
- `sources/com/viwave/rossmaxconnect/advfragment/measure/vulistener/HistoryDataListener.java:20`
  `@Metadata(d1 = {"\u0000b\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002...`
- `sources/com/viwave/rossmaxconnect/advfragment/measure/vulistener/HistoryDataListener.java:35`
  `public void onCharacteristicReadError(VUBleDevice p0, BluetoothGattCharacteristic p1, int p2) {`
- `sources/com/viwave/rossmaxconnect/advfragment/measure/vulistener/SPO2MeasureListener.java:20`
  `@Metadata(d1 = {"\u0000h\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002...`
- `sources/com/viwave/rossmaxconnect/advfragment/measure/vulistener/SPO2MeasureListener.java:35`
  `public void onCharacteristicReadError(VUBleDevice p0, BluetoothGattCharacteristic p1, int p2) {`
- `sources/com/viwave/rossmaxconnect/advfragment/measure/vulistener/TPMeasureListener.java:21`
  `@Metadata(d1 = {"\u0000r\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002...`
- `sources/com/viwave/rossmaxconnect/advfragment/measure/vulistener/TPMeasureListener.java:36`
  `public void onCharacteristicReadError(VUBleDevice p0, BluetoothGattCharacteristic p1, int p2) {`
- `sources/com/viwave/rossmaxconnect/advfragment/measure/vulistener/WTMeasureListener.java:21`
  `@Metadata(d1 = {"\u0000r\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002...`
- `sources/com/viwave/rossmaxconnect/advfragment/measure/vulistener/WTMeasureListener.java:36`
  `public void onCharacteristicReadError(VUBleDevice p0, BluetoothGattCharacteristic p1, int p2) {`
- `sources/com/viwaveulife/vuioht/VUBleManager.java:172`
  `void onCharacteristicReadError(VUBleDevice vUBleDevice, BluetoothGattCharacteristic bluetoothGattCharacteristic, int i);`

## BR063

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/android/support/v4/media/session/MediaControllerCompat.java:37`
  `public static final String COMMAND_ADD_QUEUE_ITEM = "android.support.v4.media.session.command.ADD_QUEUE_ITEM";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:38`
  `public static final String COMMAND_ADD_QUEUE_ITEM_AT = "android.support.v4.media.session.command.ADD_QUEUE_ITEM_AT";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:39`
  `public static final String COMMAND_ARGUMENT_INDEX = "android.support.v4.media.session.command.ARGUMENT_INDEX";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:40`
  `public static final String COMMAND_ARGUMENT_MEDIA_DESCRIPTION = "android.support.v4.media.session.command.ARGUMENT_MEDIA_DESCRIPTION";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:41`
  `public static final String COMMAND_GET_EXTRA_BINDER = "android.support.v4.media.session.command.GET_EXTRA_BINDER";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:42`
  `public static final String COMMAND_REMOVE_QUEUE_ITEM = "android.support.v4.media.session.command.REMOVE_QUEUE_ITEM";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:43`
  `public static final String COMMAND_REMOVE_QUEUE_ITEM_AT = "android.support.v4.media.session.command.REMOVE_QUEUE_ITEM_AT";`
- `sources/androidx/credentials/webauthn/Cbor.java:353`
  `return new byte[]{(byte) ((i | i2) & 255)};`
- `sources/androidx/credentials/webauthn/Cbor.java:356`
  `return new byte[]{(byte) ((i | 24) & 255), (byte) (i2 & 255)};`
- `sources/androidx/credentials/webauthn/Cbor.java:359`
  `return new byte[]{(byte) ((i | 25) & 255), (byte) ((i2 >> 8) & 255), (byte) (i2 & 255)};`
- `sources/androidx/credentials/webauthn/Cbor.java:362`
  `return new byte[]{(byte) ((i | 26) & 255), (byte) ((i2 >> 24) & 255), (byte) ((i2 >> 16) & 255), (byte) ((i2 >> 8) & 255), (byte) (i2 & 255)};`
- `sources/androidx/datastore/preferences/core/MutablePreferences.java:87`
  `byte[] bArr = (byte[]) value;`
- `sources/androidx/datastore/preferences/core/MutablePreferences.java:88`
  `byte[] bArrCopyOf = Arrays.copyOf(bArr, bArr.length);`
- `sources/androidx/datastore/preferences/protobuf/BinaryWriter.java:1489`
  `byte[] bArr4 = this.buffer;`
- `sources/androidx/datastore/preferences/protobuf/CodedInputStream.java:2313`
  `byte[] bArr = this.buffer;`
- `sources/androidx/datastore/preferences/protobuf/CodedOutputStream.java:488`
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
- `sources/com/dd/plist/Base64.java:44`
  `private static final byte[] _STANDARD_ALPHABET = {c.DOWNLOAD_INFORMATION_DISPLAY_AND_FUNCTION_COMMAND, c.DOWNLOAD_INFORMATION_ALARM_CLOCK_COMMAND, c.DOWNLOAD_INFORMATION_DRINKING_REMINDER_COMMAND, c.DOWNLOAD_INFORMATION_EXERCISE_REMINDER_COMMAND, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, c.DOWNLOA...`
- `sources/com/dd/plist/Base64.java:46`
  `private static final byte[] _STANDARD_DECODABET = {-9, -9, -9, -9, -9, -9, -9, -9, -9, WHITE_SPACE_ENC, WHITE_SPACE_ENC, -9, -9, WHITE_SPACE_ENC, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, WHITE_SPACE_ENC, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, 62, -9, -9, -9, Utf8.REPL...`
- `sources/com/dd/plist/Base64.java:47`
  `private static final byte[] _URL_SAFE_ALPHABET = {c.DOWNLOAD_INFORMATION_DISPLAY_AND_FUNCTION_COMMAND, c.DOWNLOAD_INFORMATION_ALARM_CLOCK_COMMAND, c.DOWNLOAD_INFORMATION_DRINKING_REMINDER_COMMAND, c.DOWNLOAD_INFORMATION_EXERCISE_REMINDER_COMMAND, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, c.DOWNLOA...`
- `sources/com/dd/plist/Base64.java:48`
  `private static final byte[] _URL_SAFE_DECODABET = {-9, -9, -9, -9, -9, -9, -9, -9, -9, WHITE_SPACE_ENC, WHITE_SPACE_ENC, -9, -9, WHITE_SPACE_ENC, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, WHITE_SPACE_ENC, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, 62, -9, -9, 52, 5...`
- `sources/com/dd/plist/Base64.java:49`
  `private static final byte[] _ORDERED_ALPHABET = {45, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, c.DOWNLOAD_INFORMATION_DISPLAY_AND_FUNCTION_COMMAND, c.DOWNLOAD_INFORMATION_ALARM_CLOCK_COMMAND, c.DOWNLOAD_INFORMATION_DRINKING_REMINDER_COMMAND, c.DOWNLOAD_INFORMATION_EXERCISE_REMINDER_COMMAND, 69, 70, 71...`
- `sources/com/dd/plist/Base64.java:50`
  `private static final byte[] _ORDERED_DECODABET = {-9, -9, -9, -9, -9, -9, -9, -9, -9, WHITE_SPACE_ENC, WHITE_SPACE_ENC, -9, -9, WHITE_SPACE_ENC, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, WHITE_SPACE_ENC, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9, 0, -9, -9, 1, 2, 3...`
- `sources/com/dd/plist/NSString.java:128`
  `byte[] bArr = new byte[byteBufferEncode.remaining()];`
- `sources/com/dd/plist/NSString.java:173`
  `byte[] bArr = new byte[byteBufferEncode.remaining()];`
- `sources/com/facebook/appevents/suggestedevents/FeatureExtractor.java:71`
  `byte[] bArr = new byte[fileInputStream.available()];`
- `sources/com/facebook/internal/security/OidcSecurityUtil.java:131`
  `byte[] bArrDecode = Base64.decode(StringsKt.replace$default(StringsKt.replace$default(StringsKt.replace$default(key, "\n", "", false, 4, (Object) null), "-----BEGIN PUBLIC KEY-----", "", false, 4, (Object) null), "-----END PUBLIC KEY-----", "", false, 4, (Object) null), 0);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:115`
  `byte[] bytes = eventInternal.getEncodedPayload().getBytes();`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:126`
  `contentValues.put("payload", z ? bytes : new byte[0]);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:135`
  `byte[] bArrCopyOfRange = Arrays.copyOfRange(bytes, (i - 1) * maxBlobByteSizePerRow, Math.min(i * maxBlobByteSizePerRow, bytes.length));`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:478`
  `byte[] blob = cursor.getBlob(0);`

## BR064

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/a/a.java:269`
  `if (a.this.f == null || !bluetoothDevice.getAddress().equals(a.this.f.getDevice().getAddress())) {`
- `sources/a/a.java:272`
  `Log.i(Utility.DEBUG_TAG, "Bond state changed for: " + bluetoothDevice.getName() + " new state: " + intExtra + " previous: " + intExtra2);`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:191`
  `String name = xml.getName();`
- `sources/androidx/browser/customtabs/PostMessageServiceConnection.java:40`
  `intent.setClassName(str, PostMessageService.class.getName());`
- `sources/androidx/core/app/NotificationCompat.java:1418`
  `if (TextUtils.isEmpty(person.getName())) {`
- `sources/androidx/core/app/NotificationCompat.java:1426`
  `return this.mUser.getName();`
- `sources/androidx/core/app/NotificationCompat.java:1557`
  `CharSequence name = message.getPerson() == null ? "" : message.getPerson().getName();`
- `sources/androidx/core/app/NotificationCompat.java:1561`
  `name = this.mUser.getName();`
- `sources/androidx/core/app/NotificationCompat.java:1580`
  `bundle.putCharSequence(NotificationCompat.EXTRA_SELF_DISPLAY_NAME, this.mUser.getName());`
- `sources/androidx/core/content/FileProvider.java:217`
  `String name = fileProviderPathsMetaData.getName();`
- `sources/androidx/core/graphics/WeightTypefaceApi14.java:25`
  `Log.e(TAG, e2.getClass().getName(), e2);`
- `sources/androidx/core/util/DebugUtils.java:14`
  `if ((simpleName == null || simpleName.length() <= 0) && (iLastIndexOf = (simpleName = obj.getClass().getName()).lastIndexOf(46)) > 0) {`
- `sources/androidx/credentials/webauthn/PublicKeyCredentialUserEntity.java:32`
  `public final String getName() {`
- `sources/androidx/lifecycle/serialization/SavedStateHandleDelegate.java:72`
  `return (thisRef != null ? Reflection.getOrCreateKotlinClass(thisRef.getClass()).getQualifiedName() + '.' : "") + property.getName();`
- `sources/androidx/navigation/NavInflater.java:305`
  `if (next == 2 && depth <= depth2 && Intrinsics.areEqual(TAG_ARGUMENT, parser.getName())) {`
- `sources/androidx/navigation/NavType.java:258`
  `throw new IllegalArgumentException("Object of type " + value.getClass().getName() + " is not supported for navigation arguments.");`
- `sources/androidx/navigation/NavType.java:399`
  `public String getName() {`
- `sources/androidx/navigation/NavType.java:400`
  `String name = this.type.getName();`
- `sources/androidx/navigation/NavType.java:510`
  `throw new IllegalArgumentException("Enum value " + value + " not found for type " + this.type.getName() + '.');`
- `sources/androidx/navigation/SavedStateHandleKt__SavedStateHandleKt.java:53`
  `linkedHashMap.put(namedNavArgument.getName(), namedNavArgument.getArgument().getType());`
- `sources/androidx/navigation/internal/NavDestinationImpl.java:253`
  `throw new IllegalArgumentException(("Wrong argument type for '" + key + "' in argument savedState. " + value.getType().getName() + " expected.").toString());`
- `sources/androidx/navigation/serialization/InternalNavType.java:65`
  `public String getName() {`
- `sources/androidx/navigation/serialization/InternalNavType.java:136`
  `public String getName() {`
- `sources/androidx/navigation/serialization/InternalNavType.java:175`
  `public String getName() {`
- `sources/androidx/navigation/serialization/InternalNavType.java:214`
  `public String getName() {`
- `sources/androidx/privacysandbox/ads/adservices/customaudience/CustomAudienceManagerImplCommon.java:78`
  `CustomAudience.Builder trustedBiddingData = new CustomAudience.Builder().setActivationTime(request.getActivationTime()).setAds(convertAds(request.getAds())).setBiddingLogicUri(request.getBiddingLogicUri()).setBuyer(request.getBuyer().convertToAdServices$ads_adservices_release()).setDailyUpdateUri(re...`
- `sources/androidx/recyclerview/widget/GridLayoutManager.java:113`
  `accessibilityNodeInfoCompat.setClassName(GridView.class.getName());`
- `sources/androidx/savedstate/SavedStateRegistry.java:73`
  `String name = clazz.getName();`
- `sources/androidx/savedstate/serialization/SavedStateRegistryOwnerDelegate.java:68`
  `return (thisRef != null ? Reflection.getOrCreateKotlinClass(thisRef.getClass()).getQualifiedName() + '.' : "") + property.getName();`
- `sources/androidx/versionedparcelable/VersionedParcel.java:990`
  `Method method = this.mWriteCache.get(cls.getName());`
- `sources/androidx/versionedparcelable/VersionedParcel.java:997`
  `this.mWriteCache.put(cls.getName(), declaredMethod);`
- `sources/androidx/versionedparcelable/VersionedParcel.java:1002`
  `Class cls2 = this.mParcelizerCache.get(cls.getName());`
- `sources/androidx/versionedparcelable/VersionedParcel.java:1006`
  `Class<?> cls3 = Class.forName(String.format("%s.%sParcelizer", cls.getPackage().getName(), cls.getSimpleName()), false, cls.getClassLoader());`
- `sources/androidx/versionedparcelable/VersionedParcel.java:1007`
  `this.mParcelizerCache.put(cls.getName(), cls3);`
- `sources/c/i.java:84`
  `return Constant.DEVICE_SKU_FAT_SCALE_WG260.equals(this.f33b.f().getName());`
- `sources/com/facebook/FacebookActivity.java:30`
  `private static final String TAG = FacebookActivity.class.getName();`
- `sources/com/facebook/UserSettingsManager.java:40`
  `private static final String TAG = UserSettingsManager.class.getName();`
- `sources/com/facebook/appevents/AppEventDiskStore.java:26`
  `private static final String TAG = AppEventDiskStore.class.getName();`
- `sources/com/facebook/appevents/AppEventQueue.java:44`
  `private static final String TAG = AppEventQueue.class.getName();`
- `sources/com/facebook/appevents/AppEventStore.java:15`
  `private static final String TAG = AppEventStore.class.getName();`
- `sources/com/facebook/appevents/aam/MetadataViewObserver.java:217`
  `companion.putUserData(map, metadataRule.getName(), strPreNormalize);`
- `sources/com/facebook/appevents/aam/MetadataViewObserver.java:220`
  `companion.putUserData(map, metadataRule.getName(), strPreNormalize);`
- `sources/com/facebook/appevents/ondeviceprocessing/OnDeviceProcessingManager.java:128`
  `return !event.isImplicit() || (event.isImplicit() && ALLOWED_IMPLICIT_EVENTS.contains(event.getName()));`
- `sources/com/facebook/internal/FetchedAppGateKeepersManager.java:214`
  `map2.put(gateKeeper.getName(), Boolean.valueOf(gateKeeper.getValue()));`
- `sources/com/facebook/internal/FetchedAppGateKeepersManager.java:265`
  `if ((gateKeeperRuntimeCache2 != null ? gateKeeperRuntimeCache2.getGateKeeper(applicationId, gateKeeper.getName()) : null) != null) {`
- `sources/com/facebook/internal/FileLruCache.java:154`
  `companion.log(loggingBehavior, TAG2, "Setting lastModified to " + Long.valueOf(time) + " for " + file.getName());`
- `sources/com/facebook/internal/FileLruCache.java:274`
  `return "{FileLruCache: tag:" + this.tag + " file:" + this.directory.getName() + ASCIIPropertyListParser.DICTIONARY_END_TOKEN;`
- `sources/com/facebook/internal/FileLruCache.java:334`
  `companion2.log(loggingBehavior2, TAG3, "  trim considering time=" + Long.valueOf(modifiedFile.getModified()) + " name=" + modifiedFile.getFile().getName());`
- `sources/com/facebook/internal/FileLruCache.java:361`
  `companion3.log(loggingBehavior3, TAG4, "  trim removing " + file2.getName());`
- `sources/com/facebook/internal/gatekeeper/GateKeeperRuntimeCache.java:31`
  `concurrentHashMap.put(gateKeeper.getName(), gateKeeper);`
- `sources/com/facebook/internal/gatekeeper/GateKeeperRuntimeCache.java:117`
  `concurrentHashMap.put(gateKeeper.getName(), gateKeeper);`
- `sources/com/facebook/internal/instrument/threadcheck/ThreadCheckHandler.java:49`
  `String str = String.format(Locale.US, "%s annotation violation detected in %s.%s%s. Current looper is %s and main looper is %s.", Arrays.copyOf(new Object[]{annotation, clazz.getName(), methodName, methodDesc, Looper.myLooper(), Looper.getMainLooper()}, 6));`
- `sources/com/google/android/gms/internal/common/zzab.java:32`
  `String str2 = obj.getClass().getName() + "@" + Integer.toHexString(System.identityHashCode(obj));`
- `sources/com/google/android/gms/internal/common/zzab.java:34`
  `string = "<" + str2 + " threw " + e2.getClass().getName() + ">";`
- `sources/com/google/android/gms/internal/fido/zzaq.java:30`
  `String str2 = obj.getClass().getName() + "@" + Integer.toHexString(System.identityHashCode(obj));`
- `sources/com/google/android/gms/internal/fido/zzaq.java:32`
  `string = "<" + str2 + " threw " + e2.getClass().getName() + ">";`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzae.java:53`
  `String str = obj.getClass().getName() + "@" + Integer.toHexString(System.identityHashCode(obj));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzae.java:55`
  `return "<" + str + " threw " + e2.getClass().getName() + ">";`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zznt.java:49`
  `throw new GeneralSecurityException(String.format("typeUrl (%s) is already registered with %s, cannot be re-registered with %s", strZzb, zzblVar2.getClass().getName(), zzblVar.getClass().getName()));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzuw.java:41`
  `sb.append(getClass().getName()).append('@').append(Integer.toHexString(System.identityHashCode(this)));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzvn.java:45`
  `sb.append(getClass().getName()).append('@').append(Integer.toHexString(System.identityHashCode(this)));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzvt.java:49`
  `sb.append(getClass().getName()).append('@').append(Integer.toHexString(System.identityHashCode(this)));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzwb.java:41`
  `sb.append(getClass().getName()).append('@').append(Integer.toHexString(System.identityHashCode(this)));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzwd.java:45`
  `sb.append(getClass().getName()).append('@').append(Integer.toHexString(System.identityHashCode(this)));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzwe.java:41`
  `sb.append(getClass().getName()).append('@').append(Integer.toHexString(System.identityHashCode(this)));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzws.java:131`
  `sb.append(getClass().getName()).append('@').append(Integer.toHexString(System.identityHashCode(this)));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzwt.java:41`
  `sb.append(getClass().getName()).append('@').append(Integer.toHexString(System.identityHashCode(this)));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzxu.java:49`
  `sb.append(getClass().getName()).append('@').append(Integer.toHexString(System.identityHashCode(this)));`
- `sources/com/google/android/material/animation/MotionSpec.java:138`
  `return "\n" + getClass().getName() + ASCIIPropertyListParser.DICTIONARY_BEGIN_TOKEN + Integer.toHexString(System.identityHashCode(this)) + " timings: " + this.timings + "}\n";`
- `sources/com/google/android/material/animation/MotionTiming.java:104`
  `return "\n" + getClass().getName() + ASCIIPropertyListParser.DICTIONARY_BEGIN_TOKEN + Integer.toHexString(System.identityHashCode(this)) + " delay: " + getDelay() + " duration: " + getDuration() + " interpolator: " + getInterpolator().getClass() + " repeatCount: " + getRepeatCount() + " repeatMode: ...`
- `sources/com/google/android/recaptcha/internal/zzbm.java:43`
  `if (StringsKt.startsWith$default(file.getName(), this.zzb, false, 2, (Object) null)) {`
- `sources/com/google/android/recaptcha/internal/zzfx.java:21`
  `if (Intrinsics.areEqual(method.getName(), InAppPurchaseConstants.METHOD_TO_STRING) && method.getParameterTypes().length == 0) {`
- `sources/com/google/android/recaptcha/internal/zzfx.java:24`
  `if (Intrinsics.areEqual(method.getName(), "hashCode") && method.getParameterTypes().length == 0) {`
- `sources/com/google/android/recaptcha/internal/zzfx.java:27`
  `if (Intrinsics.areEqual(method.getName(), "equals") && method.getParameterTypes().length != 0) {`
- `sources/com/google/android/recaptcha/internal/zzji.java:30`
  `String str2 = obj.getClass().getName() + "@" + Integer.toHexString(System.identityHashCode(obj));`
- `sources/com/google/android/recaptcha/internal/zzji.java:32`
  `string = "<" + str2 + " threw " + e2.getClass().getName() + ">";`
- `sources/com/google/common/base/Strings.java:148`
  `String str = o.getClass().getName() + '@' + Integer.toHexString(System.identityHashCode(o));`
- `sources/com/google/common/base/Strings.java:150`
  `return "<" + str + " threw " + e2.getClass().getName() + ">";`
- `sources/com/google/common/cache/CacheBuilder.java:99`
  `static final Logger logger = Logger.getLogger(CacheBuilder.class.getName());`
- `sources/com/google/common/cache/LocalCache.java:94`
  `static final Logger logger = Logger.getLogger(LocalCache.class.getName());`

## BR065

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/a/a.java:214`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/a/a.java:220`
  `Log.w(Utility.DEBUG_TAG, "onServicesDiscovered received: " + i);`
- `sources/c/i.java:242`
  `Log.d("LSFunctionProcessor", "onServicesDiscovered");`
- `sources/com/lifesense/ble/c/c/c.java:307`
  `public synchronized void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`

## BR066

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/a/a.java:67`
  `BluetoothGattDescriptor descriptor = bluetoothGattCharacteristic.getDescriptor(UUID.fromString("00002902-0000-1000-8000-00805f9b34fb"));`
- `sources/a/a.java:582`
  `BluetoothGattDescriptor descriptor = bluetoothGattCharacteristic.getDescriptor(UUID.fromString("00002902-0000-1000-8000-00805f9b34fb"));`
- `sources/a/a.java:773`
  `BluetoothGattDescriptor descriptor = bluetoothGattCharacteristic.getDescriptor(UUID.fromString("00002902-0000-1000-8000-00805f9b34fb"));`
- `sources/c/a.java:77`
  `return new BluetoothGattCharacteristic(UUID.fromString("00000001-0000-1000-8000-00805f9b34fb"), 8, 16);`
- `sources/c/c.java:19`
  `private static final UUID m = UUID.fromString("00001810-0000-1000-8000-00805f9b34fb");`
- `sources/c/c.java:20`
  `private static final UUID n = UUID.fromString("00002A35-0000-1000-8000-00805f9b34fb");`
- `sources/c/c.java:21`
  `private static final UUID o = UUID.fromString("00002A36-0000-1000-8000-00805f9b34fb");`
- `sources/c/e.java:15`
  `private static final UUID p = UUID.fromString("0000180A-0000-1000-8000-00805f9b34fb");`
- `sources/c/e.java:16`
  `private static final UUID q = UUID.fromString("00002a29-0000-1000-8000-00805f9b34fb");`
- `sources/c/e.java:17`
  `private static final UUID r = UUID.fromString("00002a24-0000-1000-8000-00805f9b34fb");`
- `sources/c/e.java:18`
  `private static final UUID s = UUID.fromString("00002a25-0000-1000-8000-00805f9b34fb");`
- `sources/c/f.java:20`
  `private static final UUID k = UUID.fromString("0000FC00-0000-1000-8000-00805f9b34fb");`
- `sources/c/f.java:21`
  `private static final UUID l = UUID.fromString("0000FCA1-0000-1000-8000-00805f9b34fb");`
- `sources/c/f.java:22`
  `private static final UUID m = UUID.fromString("0000FCA0-0000-1000-8000-00805f9b34fb");`
- `sources/c/g.java:17`
  `private static final UUID j = UUID.fromString("00005970-6d75-4753-5053-676e6f6c7553");`
- `sources/c/g.java:18`
  `private static final UUID k = UUID.fromString("02005970-6d75-4753-5053-676e6f6c7553");`
- `sources/c/h.java:20`
  `private static final UUID m = UUID.fromString("000078a2-0000-1000-8000-00805f9b34fb");`
- `sources/c/h.java:22`
  `private static final UUID n = UUID.fromString(k);`
- `sources/c/h.java:24`
  `private static final UUID o = UUID.fromString(l);`
- `sources/c/h.java:122`
  `this.i = bluetoothGattService.getCharacteristic(UUID.fromString(l));`
- `sources/c/h.java:123`
  `this.j = bluetoothGattService.getCharacteristic(UUID.fromString(k));`
- `sources/c/j.java:26`
  `private static final UUID o = UUID.fromString("0000fff0-0000-1000-8000-00805f9b34fb");`
- `sources/c/j.java:27`
  `private static final UUID p = UUID.fromString("0000FFF1-0000-1000-8000-00805f9b34fb");`
- `sources/c/n.java:16`
  `private static final UUID j = UUID.fromString("0000f680-0000-1000-8000-00805f9b34fb");`
- `sources/c/n.java:17`
  `private static final UUID k = UUID.fromString("0000f682-0000-1000-8000-00805f9b34fb");`
- `sources/c/o.java:17`
  `private static final UUID j = UUID.fromString("6e40f680-b5a3-f393-e0a9-e50e24dcca9e");`
- `sources/c/o.java:18`
  `private static final UUID k = UUID.fromString("6e40f682-b5a3-f393-e0a9-e50e24dcca9e");`
- `sources/c/p.java:19`
  `private static final UUID k = UUID.fromString("6e40f680-b5a3-f393-e0a9-e50e24dcca9e");`
- `sources/c/p.java:20`
  `private static final UUID l = UUID.fromString("6e40f682-b5a3-f393-e0a9-e50e24dcca9e");`
- `sources/c/q.java:44`
  `private static final UUID z = UUID.fromString("00001810-0000-1000-8000-00805f9b34fb");`
- `sources/c/q.java:45`
  `private static final UUID A = UUID.fromString("00002A35-0000-1000-8000-00805f9b34fb");`
- `sources/c/q.java:46`
  `private static final UUID B = UUID.fromString("00002A36-0000-1000-8000-00805f9b34fb");`
- `sources/c/q.java:47`
  `private static final UUID C = UUID.fromString("00001210-0000-1000-8000-00805f9b34fb");`
- `sources/c/r.java:35`
  `private static final UUID v = UUID.fromString("00001810-0000-1000-8000-00805f9b34fb");`
- `sources/c/r.java:36`
  `private static final UUID w = UUID.fromString("00002A35-0000-1000-8000-00805f9b34fb");`
- `sources/c/r.java:37`
  `private static final UUID x = UUID.fromString("00002A36-0000-1000-8000-00805f9b34fb");`
- `sources/c/r.java:38`
  `private static final UUID y = UUID.fromString("00001210-0000-1000-8000-00805f9b34fb");`
- `sources/c/r.java:39`
  `private static final UUID z = UUID.fromString("00001211-0000-1000-8000-00805f9b34fb");`
- `sources/com/lifesense/ble/b/a.java:97`
  `public static final Map marshalServiceUuid;`
- `sources/com/lifesense/ble/b/a.java:102`
  `public static final Map unmarshalServiceUuid;`

## BR067

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/a/a.java:560`
  `boolean zCreateBond = this.f9e.createBond();`
- `sources/a/a.java:561`
  `if (!zCreateBond) {`
- `sources/a/a.java:564`
  `return zCreateBond;`
- `sources/c/b.java:242`
  `Log.e("BloodGlucoseProcessor", "CreateBond Fail");`
- `sources/c/i.java:237`
  `Log.d("LSFunctionProcessor", "onCreateBond");`
- `sources/com/github/mikephil/charting/charts/BarLineChartBase.java:866`
  `public void setPinchZoom(boolean z) {`
- `sources/com/lifesense/ble/c/b.java:238`
  `bluetoothDevice.getClass().getMethod("removeBond", null).invoke(bluetoothDevice, null);`
- `sources/okhttp3/OkHttpClient.java:579`
  `@Metadata(d1 = {"\u0000\u0086\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010!\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010...`
- `sources/okhttp3/internal/http2/Http2Connection.java:651`
  `@Metadata(d1 = {"\u0000^\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000b\n\u0000\n\u0002\u0018\u0002\n\u0002\b\t\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u000e\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u...`

## BR068

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:86`
  `private static final String JSON_KEY_CHALLENGE = ClientData.KEY_CHALLENGE;`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:119`
  `@Metadata(d1 = {"\u0000\u0096\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u000e\n\u0002\bH\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0000\n\u0002\u0010\u0012\n\u0002\b...`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:343`
  `BeginSignInRequest.PasskeysRequestOptions passkeysRequestOptionsBuild = new BeginSignInRequest.PasskeysRequestOptions.Builder().setSupported(true).setRpId(rpId).setChallenge(getChallenge(jSONObject)).build();`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:348`
  `private final byte[] getChallenge(JSONObject json) throws JSONException {`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:349`
  `String challengeB64 = json.optString(getJSON_KEY_CHALLENGE$credentials_play_services_auth_release(), "");`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:350`
  `Intrinsics.checkNotNullExpressionValue(challengeB64, "challengeB64");`
- `sources/androidx/credentials/playservices/controllers/CreatePublicKeyCredential/PublicKeyCredentialControllerUtility.java:351`
  `if (challengeB64.length() == 0) {`
- `sources/androidx/credentials/webauthn/AuthenticatorAssertionResponse.java:51`
  `getClientJson().put(ClientData.KEY_CHALLENGE, WebAuthnUtils.INSTANCE.b64Encode(requestOptions.getChallenge()));`
- `sources/androidx/credentials/webauthn/PublicKeyCredentialCreationOptions.java:18`
  `@Metadata(d1 = {"\u0000V\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u0012\n\u0002\b\u0003\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0...`
- `sources/androidx/credentials/webauthn/PublicKeyCredentialCreationOptions.java:22`
  `private final byte[] challenge;`
- `sources/androidx/credentials/webauthn/PublicKeyCredentialRequestOptions.java:13`
  `@Metadata(d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0002\n\u0002\u0010\u0012\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0010\t\n\u0002\b\u0005\b\u0007\u0018\u00002\u00020\u0001B\r\u0012\u0006\u0010\u0002\u001a\u00020\u0003¢\u0006\...`
- `sources/androidx/credentials/webauthn/PublicKeyCredentialRequestOptions.java:15`
  `private final byte[] challenge;`
- `sources/com/facebook/internal/NativeProtocol.java:39`
  `@Metadata(d1 = {"\u0000 \u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b;\n\u0002\u0010\u0011\n\u0002\u0010\b\n\u0002\b;\n\u0002\u0010$\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\b\u00...`
- `sources/com/facebook/internal/NativeProtocol.java:318`
  `private final Intent createNativeAppIntent(NativeAppInfo appInfo, String applicationId, Collection<String> permissions, String e2e, boolean isForPublish, DefaultAudience defaultAudience, String clientState, String authType, boolean ignoreAppSwitchToLoggedOut, String messengerPageId, boolean resetMes...`
- `sources/com/facebook/internal/NativeProtocol.java:376`
  `public static final List<Intent> createProxyAuthIntents(Context context, String applicationId, Collection<String> permissions, String e2e, boolean isRerequest, boolean isForPublish, DefaultAudience defaultAudience, String clientState, String authType, boolean ignoreAppSwitchToLoggedOut, String messe...`
- `sources/com/facebook/internal/ServerProtocol.java:20`
  `@Metadata(d1 = {"\u0000,\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b:\n\u0002\u0010\u001e\n\u0002\b\t\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\bÆ\u0002\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002J\b\u0010;\u00...`
- `sources/com/facebook/login/CodeChallengeMethod.java:7`
  `/* JADX INFO: compiled from: CodeChallengeMethod.kt */`
- `sources/com/facebook/login/CodeChallengeMethod.java:9`
  `@Metadata(d1 = {"\u0000\u0012\n\u0002\u0018\u0002\n\u0002\u0010\u0010\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0004\b\u0086\u0001\u0018\u00002\b\u0012\u0004\u0012\u00020\u00000\u0001B\u0011\b\u0002\u0012\b\b\u0002\u0010\u0002\u001a\u00020\u0003¢\u0006\u0002\u0010\u0004j\u0002\b\u0005j\u0002\b\u0006¨\u...`
- `sources/com/facebook/login/CodeChallengeMethod.java:10`
  `public enum CodeChallengeMethod {`
- `sources/com/facebook/login/CodeChallengeMethod.java:14`
  `CodeChallengeMethod(String str) {`
- `sources/com/facebook/login/CodeChallengeMethod.java:17`
  `/* synthetic */ CodeChallengeMethod(String str, int i, DefaultConstructorMarker defaultConstructorMarker) {`
- `sources/com/facebook/login/CustomTabLoginMethodHandler.java:38`
  `@Metadata(d1 = {"\u0000'\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\t\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010\b\n\u0002\b\u0003\n\u0002\u0010\u000b\n\u0002\b\u0003\n\u0002\u0018\u0002...`
- `sources/com/facebook/login/CustomTabLoginMethodHandler.java:41`
  `private static final int CHALLENGE_LENGTH = 20;`
- `sources/com/facebook/login/CustomTabLoginMethodHandler.java:46`
  `private String expectedChallenge;`
- `sources/com/facebook/login/CustomTabLoginMethodHandler.java:266`
  `this.expectedChallenge = source.readString();`
- `sources/com/facebook/login/CustomTabLoginMethodHandler.java:274`
  `dest.writeString(this.expectedChallenge);`
- `sources/com/facebook/login/CustomTabLoginMethodHandler.java:278`
  `@Metadata(d1 = {"\u0000,\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\u000b\n\u0000\b\u0086\u0003\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u...`
- `sources/com/facebook/login/LoginClient.java:531`
  `@Metadata(d1 = {"\u0000R\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\"\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0015\n\u0002\u00...`
- `sources/com/facebook/login/LoginClient.java:536`
  `private final String codeChallenge;`
- `sources/com/facebook/login/LoginClient.java:537`
  `private final CodeChallengeMethod codeChallengeMethod;`
- `sources/com/facebook/login/LoginClient.java:726`
  `public final String getCodeChallenge() {`
- `sources/com/facebook/login/LoginClient.java:727`
  `return this.codeChallenge;`
- `sources/com/facebook/login/LoginClient.java:730`
  `public final CodeChallengeMethod getCodeChallengeMethod() {`
- `sources/com/facebook/login/LoginClient.java:731`
  `return this.codeChallengeMethod;`
- `sources/com/facebook/login/LoginClient.java:742`
  `public /* synthetic */ Request(com.facebook.login.LoginBehavior r15, java.util.Set r16, com.facebook.login.DefaultAudience r17, java.lang.String r18, java.lang.String r19, java.lang.String r20, com.facebook.login.LoginTargetApp r21, java.lang.String r22, java.lang.String r23, java.lang.String r24, c...`
- `sources/com/facebook/login/LoginClient.java:884`
  `this.codeChallenge = parcel.readString();`
- `sources/com/facebook/login/LoginClient.java:886`
  `this.codeChallengeMethod = string3 != null ? CodeChallengeMethod.valueOf(string3) : null;`
- `sources/com/facebook/login/LoginClient.java:908`
  `dest.writeString(this.codeChallenge);`
- `sources/com/facebook/login/LoginClient.java:909`
  `CodeChallengeMethod codeChallengeMethod = this.codeChallengeMethod;`
- `sources/com/facebook/login/LoginClient.java:910`
  `dest.writeString(codeChallengeMethod != null ? codeChallengeMethod.name() : null);`
- `sources/com/facebook/login/LoginLogger.java:488`
  `@Metadata(d1 = {"\u0000$\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b$\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\b\u0086\u0003\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002J\u0012\u0010+\u001a\u00020,2\b\u0010...`
- `sources/com/facebook/login/LoginMethodHandler.java:43`
  `@Metadata(d1 = {"\u0000b\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010%\n\u0002\u0010\u000e\n\u0002\b\b\n\u0002\u0010\u0002\n\u0002\b\u0002\n\u0002\u0010\u0000\n\u0002\b\u0007\n\u0002\u0010\u000b\n\u0002\b\u0002\...`
- `sources/com/facebook/login/PKCEUtil.java:29`
  `@Metadata(d1 = {"\u0000(\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0000\bÀ\u0002\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002J \u0010\u0003\u0...`
- `sources/com/facebook/login/WebLoginMethodHandler.java:103`
  `parameters.putString(ServerProtocol.DIALOG_PARAM_CODE_CHALLENGE, request.getCodeChallenge());`
- `sources/com/facebook/login/WebLoginMethodHandler.java:104`
  `CodeChallengeMethod codeChallengeMethod = request.getCodeChallengeMethod();`
- `sources/com/facebook/login/WebLoginMethodHandler.java:105`
  `parameters.putString(ServerProtocol.DIALOG_PARAM_CODE_CHALLENGE_METHOD, codeChallengeMethod != null ? codeChallengeMethod.name() : null);`
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
- `sources/com/google/android/gms/auth/api/identity/BeginSignInRequest.java:393`
  `SafeParcelWriter.writeByteArray(parcel, 2, getChallenge(), false);`
- `sources/com/google/android/gms/fido/fido2/api/common/PublicKeyCredentialCreationOptions.java:220`
  `SafeParcelWriter.writeByteArray(parcel, 4, getChallenge(), false);`
- `sources/com/google/android/gms/fido/fido2/api/common/PublicKeyCredentialRequestOptions.java:179`
  `SafeParcelWriter.writeByteArray(parcel, 2, getChallenge(), false);`
- `sources/com/google/android/gms/fido/fido2/api/common/RequestOptions.java:11`
  `public abstract byte[] getChallenge();`
- `sources/com/google/android/gms/fido/u2f/api/common/RegisteredKey.java:124`
  `SafeParcelWriter.writeString(parcel, 3, getChallengeValue(), false);`
- `sources/com/google/android/gms/fido/u2f/api/common/RegisterRequest.java:20`
  `public static final int U2F_V1_CHALLENGE_BYTE_LENGTH = 65;`
- `sources/com/google/android/gms/fido/u2f/api/common/RegisterRequest.java:117`
  `SafeParcelWriter.writeByteArray(parcel, 3, getChallengeValue(), false);`
- `sources/com/google/android/gms/fido/u2f/api/common/SignRequestParams.java:54`
  `public Builder setDefaultSignChallenge(byte[] bArr) {`
- `sources/com/google/android/gms/fido/u2f/api/common/SignRequestParams.java:132`
  `public byte[] getDefaultSignChallenge() {`
- `sources/com/google/android/gms/fido/u2f/api/common/SignRequestParams.java:166`
  `SafeParcelWriter.writeByteArray(parcel, 5, getDefaultSignChallenge(), false);`
- `sources/com/google/android/gms/internal/auth/zzby.java:30`
  `CHALLENGE_REQUIRED("ChallengeRequired"),`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzaei.java:121`
  `sparseArray.put(17078, new Pair<>("ERROR_SECOND_FACTOR_REQUIRED", "Please complete a second factor challenge to finish signing into this account."));`
- `sources/com/lifesense/ble/b/c/a.java:54`
  `dp.a(new String[]{"\n\u0017BluetoothProtobuf.proto\u0012 com.lifesense.bpmonitor.protobuf\"\r\n\u000bBaseRequest\"/\n\fBaseResponse\u0012\u000f\n\u0007ErrCode\u0018\u0001 \u0002(\u0005\u0012\u000e\n\u0006ErrMsg\u0018\u0002 \u0001(\t\"\n\n\bBasePush\"ù\u0001\n\u000bAuthRequest\u0012B\n\u000bBaseReque...`
- `sources/com/lifesense/ble/b/c/b.java:26`
  `ep unused11 = a.j = new ep(a.i, new String[]{"BaseResponse", "AesSessionKey"});`
- `sources/com/lifesense/ble/b/c/b.java:28`
  `ep unused13 = a.l = new ep(a.k, new String[]{"BaseRequest", "RespFieldFilter", "Challenge"});`
- `sources/okhttp3/Challenge.java:18`
  `/* JADX INFO: compiled from: Challenge.kt */`
- `sources/okhttp3/Challenge.java:20`
  `@Metadata(d1 = {"\u00000\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010$\n\u0002\b\u0007\n\u0002\u0018\u0002\n\u0002\b\u0007\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\u0018\u00002\u00020\u0001B%\u0012\u0006\u0010\u0002\u001a\u00020...`
- `sources/okhttp3/Challenge.java:21`
  `public final class Challenge {`
- `sources/okhttp3/Challenge.java:25`
  `public Challenge(String scheme, Map<String, String> authParams) {`
- `sources/okhttp3/Challenge.java:83`
  `public final Challenge withCharset(Charset charset) {`
- `sources/okhttp3/Challenge.java:87`
  `return new Challenge(this.scheme, (Map<String, String>) mutableMap);`
- `sources/okhttp3/Response.java:26`
  `@Metadata(d1 = {"\u0000|\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010\t\n\u0002\b\u...`
- `sources/okhttp3/internal/http/HttpHeaders.java:26`
  `@Metadata(d1 = {"\u0000T\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010!\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010\u0005\n\u0002\b\u00...`
- `sources/okhttp3/internal/http/HttpHeaders.java:31`
  `public static final List<Challenge> parseChallenges(Headers headers, String headerName) {`
- `sources/okhttp3/internal/http/HttpHeaders.java:39`
  `readChallengeHeader(new Buffer().writeUtf8(headers.value(i)), arrayList);`
- `sources/okhttp3/internal/http/HttpHeaders.java:41`
  `Platform.INSTANCE.get().log("Unable to parse challenge", 5, e2);`
- `sources/okhttp3/internal/http/HttpHeaders.java:61`
  `private static final void readChallengeHeader(okio.Buffer r7, java.util.List<okhttp3.Challenge> r8) throws java.io.EOFException {`
- `sources/okhttp3/internal/http/HttpHeaders.java:66`
  `throw new UnsupportedOperationException("Method not decompiled: okhttp3.internal.http.HttpHeaders.readChallengeHeader(okio.Buffer, java.util.List):void");`

## BR069

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/com/google/api/BackendRule.java:483`
  `public String getAddress() {`
- `sources/com/google/api/BackendRule.java:484`
  `return ((BackendRule) this.instance).getAddress();`
- `sources/com/lifesense/ble/a/f/g.java:42`
  `bundle.putString("mac", str);`
- `sources/com/lifesense/ble/a/f/g.java:54`
  `bundle.putString("mac", str);`
- `sources/com/lifesense/ble/a/f/g.java:67`
  `bundle.putString("mac", str);`
- `sources/com/lifesense/ble/a/f/g.java:79`
  `bundle.putString("mac", str);`
- `sources/com/viwaveulife/vuioht/VUBleManager.java:5`
  `import android.bluetooth.BluetoothDevice;`
- `sources/no/nordicsemi/android/support/v18/scanner/BluetoothLeScannerImplJB.java:47`
  `public final void onLeScan(BluetoothDevice bluetoothDevice, int i, byte[] bArr) {`
- `sources/no/nordicsemi/android/support/v18/scanner/BluetoothLeScannerImplJB.java:48`
  `this.f$0.m2672xf6688aa4(bluetoothDevice, i, bArr);`
- `sources/no/nordicsemi/android/support/v18/scanner/BluetoothLeScannerImplJB.java:183`
  `/* synthetic */ void m2672xf6688aa4(BluetoothDevice bluetoothDevice, int i, byte[] bArr) {`
- `sources/no/nordicsemi/android/support/v18/scanner/BluetoothLeScannerImplJB.java:184`
  `final ScanResult scanResult = new ScanResult(bluetoothDevice, ScanRecord.parseFromBytes(bArr), i, SystemClock.elapsedRealtimeNanos());`
- `sources/okio/HashingSink.java:100`
  `Intrinsics.checkNotNull(mac);`
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

- `sources/com/google/android/gms/internal/measurement/zzpa.java:126`
  `zzH = zzkfVarZzb.zzc("measurement.service_client.reconnect_millis", 1000L);`
- `sources/com/google/android/gms/measurement/internal/zzfx.java:183`
  `zzZ = zza("measurement.service_client.reconnect_millis", 1000L, 1000L, zzdj.zza, false);`
- `sources/com/lifesense/ble/b/e/c/aa.java:67`
  `zVar.printLogMessage(zVar.getGeneralLogInfo(zVar.y, str2, com.lifesense.ble.a.c.a.a.Cancel_Reconnect, null, true));`
- `sources/com/lifesense/ble/b/e/c/ac.java:163`
  `printLogMessage(getSupperLogInfo(this.y, "failed to reconnect device,bluetooth status error..", com.lifesense.ble.a.c.a.a.Reconnect_Message, null, false));`
- `sources/com/lifesense/ble/b/e/c/ac.java:167`
  `printLogMessage(getGeneralLogInfo(this.y, "resume scan device[" + this.y + "] ;lastCacheTime:" + o(), com.lifesense.ble.a.c.a.a.Cancel_Reconnect, null, true));`
- `sources/com/lifesense/ble/b/e/c/ac.java:175`
  `String str = "reconnect syncing device=" + this.B.getBroadcastID() + " ; count=" + this.k;`
- `sources/com/lifesense/ble/b/e/c/ad.java:72`
  `acVar.printLogMessage(acVar.getGeneralLogInfo(acVar.y, str2, com.lifesense.ble.a.c.a.a.Cancel_Reconnect, null, true));`
- `sources/com/lifesense/ble/b/e/c/q.java:88`
  `printLogMessage(getGeneralLogInfo(this.y, "resume scanning=" + this.k + "; lastCacheTime:" + o() + "; from[" + this.y + "]", com.lifesense.ble.a.c.a.a.Cancel_Reconnect, null, true));`
- `sources/com/lifesense/ble/b/e/c/q.java:640`
  `q qVar2 = "no permission to reconnect device,upgrade status error >> ";`
- `sources/com/lifesense/ble/b/e/c/q.java:647`
  `qVar.printLogMessage(qVar.getGeneralLogInfo(qVar.y, "resume scanning=" + qVar.k + " ;lastCacheTime:" + qVar.o() + "; from[" + qVar.y + "]", com.lifesense.ble.a.c.a.a.Cancel_Reconnect, null, true));`
- `sources/com/lifesense/ble/b/e/c/z.java:170`
  `printLogMessage(getSupperLogInfo(this.y, "failed to reconnect device,bluetooth status error..", com.lifesense.ble.a.c.a.a.Reconnect_Message, null, false));`
- `sources/com/lifesense/ble/b/e/c/z.java:174`
  `printLogMessage(getGeneralLogInfo(this.y, "resume scan device[" + this.y + "] ;lastCacheTime:" + o(), com.lifesense.ble.a.c.a.a.Cancel_Reconnect, null, true));`
- `sources/com/lifesense/ble/b/e/c/z.java:182`
  `String str = "reconnect syncing device=" + this.B.getBroadcastID() + " ; count=" + this.k;`
- `sources/kotlinx/coroutines/flow/FlowKt__MigrationKt.java:373`
  `@Deprecated(level = DeprecationLevel.ERROR, message = "Flow analogue of 'replay(bufferSize)' is 'shareIn' with the specified replay parameter. \nreplay().connect() is the default strategy (no extra call is needed), \nreplay().autoConnect() translates to 'started = SharingStared.Lazily' argument, \nr...`
- `sources/okhttp3/EventListener.java:15`
  `@Metadata(d1 = {"\u0000\u008a\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0002\n...`
- `sources/okhttp3/logging/LoggingEventListener.java:27`
  `@Metadata(d1 = {"\u0000\u0082\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\t\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\u0002\n\u00...`

## BR072

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/com/lifesense/ble/message/a/c.java:85`
  `return (str == null || str.length() == 0) ? MessageType.UNKNOWN : "com.tencent.mm".equalsIgnoreCase(str) ? MessageType.WECHAT : "jp.naver.line.android".equalsIgnoreCase(str) ? MessageType.LINE : "com.google.android.gm".equalsIgnoreCase(str) ? MessageType.GMAIL : "com.whatsapp".equalsIgnoreCase(str) ...`

## BR073

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:694`
  `public void restoreToolbarHierarchyState(SparseArray<Parcelable> sparseArray) {`
- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:696`
  `this.mDecorToolbar.restoreHierarchyState(sparseArray);`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:22`
  `import org.xmlpull.v1.XmlPullParserException;`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:442`
  `if (!TAG_HISTORICAL_RECORD.equals(xmlPullParserNewPullParser.getName())) {`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:443`
  `throw new XmlPullParserException("Share records file not well-formed.");`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:445`
  `list.add(new HistoricalRecord(xmlPullParserNewPullParser.getAttributeValue(null, ATTRIBUTE_ACTIVITY), Long.parseLong(xmlPullParserNewPullParser.getAttributeValue(null, ATTRIBUTE_TIME)), Float.parseFloat(xmlPullParserNewPullParser.getAttributeValue(null, ATTRIBUTE_WEIGHT))));`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:448`
  `} catch (XmlPullParserException e2) {`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:166`
  `TextViewCompat.setCompoundDrawableTintMode(this.mView, DrawableUtils.parseTintMode(tintTypedArrayObtainStyledAttributes4.getInt(R.styleable.AppCompatTextView_drawableTintMode, -1), null));`
- `sources/androidx/browser/trusted/TokenContents.java:42`
  `parseIfNeeded();`
- `sources/androidx/browser/trusted/TokenContents.java:51`
  `parseIfNeeded();`
- `sources/androidx/browser/trusted/TokenContents.java:60`
  `parseIfNeeded();`
- `sources/androidx/browser/trusted/TokenContents.java:130`
  `private void parseIfNeeded() throws IOException {`
- `sources/androidx/collection/LongSparseArrayKt.java:21`
  `/* JADX INFO: compiled from: LongSparseArray.kt */`
- `sources/androidx/collection/LongSparseArrayKt.java:23`
  `@Metadata(d1 = {"\u0000X\n\u0000\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u0002\n\u0002\b\u0002\n\u0002\u0010\t\n\u0002\b\u0004\n\u0002\u0010\u000b\n\u0002\b\u001d\n\u0002\u0010\u000e\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\u0018\u0002...`
- `sources/androidx/collection/LongSparseArrayKt.java:24`
  `public final class LongSparseArrayKt {`
- `sources/androidx/collection/LongSparseArrayKt.java:27`
  `public static /* synthetic */ void getSize$annotations(LongSparseArray longSparseArray) {`
- `sources/androidx/collection/LongSparseArrayKt.java:458`
  `Intrinsics.checkNotNullParameter(longSparseArray, "<this>");`
- `sources/androidx/collection/LongSparseArrayKt.java:460`
  `T t = longSparseArray.get(j);`
- `sources/androidx/collection/LongSparseArrayKt.java:464`
  `public static final <T> boolean isNotEmpty(LongSparseArray<T> longSparseArray) {`
- `sources/androidx/collection/LongSparseArrayKt.java:465`
  `Intrinsics.checkNotNullParameter(longSparseArray, "<this>");`
- `sources/androidx/collection/LongSparseArrayKt.java:466`
  `return !longSparseArray.isEmpty();`
- `sources/androidx/collection/LongSparseArrayKt.java:470`
  `public static final /* synthetic */ boolean remove(LongSparseArray longSparseArray, long j, Object obj) {`
- `sources/androidx/collection/SparseArrayKt.java:17`
  `/* JADX INFO: compiled from: SparseArray.kt */`
- `sources/androidx/collection/SparseArrayKt.java:19`
  `@Metadata(d1 = {"\u0000@\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0007\n\u0002\u0010(\...`
- `sources/androidx/collection/SparseArrayKt.java:20`
  `public final class SparseArrayKt {`
- `sources/androidx/collection/SparseArrayKt.java:21`
  `public static final <T> int getSize(SparseArrayCompat<T> sparseArrayCompat) {`
- `sources/androidx/collection/SparseArrayKt.java:22`
  `Intrinsics.checkNotNullParameter(sparseArrayCompat, "<this>");`
- `sources/androidx/collection/SparseArrayKt.java:23`
  `return sparseArrayCompat.size();`
- `sources/androidx/collection/SparseArrayKt.java:51`
  `Intrinsics.checkNotNullParameter(sparseArrayCompat, "<this>");`
- `sources/androidx/collection/SparseArrayKt.java:53`
  `T t = sparseArrayCompat.get(i);`
- `sources/androidx/collection/SparseArrayKt.java:57`
  `public static final <T> boolean isNotEmpty(SparseArrayCompat<T> sparseArrayCompat) {`
- `sources/androidx/collection/SparseArrayKt.java:58`
  `Intrinsics.checkNotNullParameter(sparseArrayCompat, "<this>");`
- `sources/androidx/collection/SparseArrayKt.java:59`
  `return !sparseArrayCompat.isEmpty();`
- `sources/androidx/collection/SparseArrayKt.java:63`
  `public static final /* synthetic */ boolean remove(SparseArrayCompat sparseArrayCompat, int i, Object obj) {`
- `sources/androidx/constraintlayout/core/state/ConstraintSetParser.java:927`
  `static void parseWidget(State state, LayoutVariables layoutVariables, String str, CLObject cLObject) throws CLParsingException {`
- `sources/androidx/constraintlayout/core/state/ConstraintSetParser.java:928`
  `parseWidget(state, layoutVariables, state.constraints(str), cLObject);`
- `sources/androidx/constraintlayout/core/state/ConstraintSetParser.java:1059`
  `constraintReference.setHeight(parseDimension(cLObject, str, state, state.getDpToPixel()));`
- `sources/androidx/constraintlayout/core/state/ConstraintSetParser.java:1062`
  `parseMotionProperties(cLObject.get(str), constraintReference);`
- `sources/androidx/constraintlayout/core/state/ConstraintSetParser.java:1096`
  `constraintReference.setWidth(parseDimension(cLObject, str, state, state.getDpToPixel()));`
- `sources/androidx/constraintlayout/core/state/ConstraintSetParser.java:1134`
  `static void parseWidget(State state, LayoutVariables layoutVariables, ConstraintReference constraintReference, CLObject cLObject) throws CLParsingException {`
- `sources/androidx/constraintlayout/core/utils/GridCore.java:340`
  `private float[] parseWeights(int i, String str) {`
- `sources/androidx/constraintlayout/core/utils/GridCore.java:426`
  `float[] weights = parseWeights(this.mColumns, this.mColumnWeights);`
- `sources/androidx/constraintlayout/core/utils/GridCore.java:472`
  `float[] weights = parseWeights(this.mRows, this.mRowWeights);`
- `sources/androidx/constraintlayout/helper/widget/Grid.java:189`
  `private float[] parseWeights(int i, String str) {`
- `sources/androidx/constraintlayout/helper/widget/Grid.java:374`
  `float[] weights = parseWeights(this.mColumns, this.mStrColumnWeights);`
- `sources/androidx/constraintlayout/helper/widget/Grid.java:424`
  `float[] weights = parseWeights(this.mRows, this.mStrRowWeights);`
- `sources/androidx/constraintlayout/motion/utils/ViewSpline.java:24`
  `return new CustomSet(str, sparseArray);`
- `sources/androidx/constraintlayout/motion/utils/ViewSpline.java:250`
  `SparseArray<ConstraintAttribute> mConstraintAttributeList;`
- `sources/androidx/constraintlayout/motion/utils/ViewSpline.java:253`
  `public CustomSet(String str, SparseArray<ConstraintAttribute> sparseArray) {`
- `sources/androidx/constraintlayout/motion/utils/ViewSpline.java:255`
  `this.mConstraintAttributeList = sparseArray;`
- `sources/androidx/constraintlayout/motion/utils/ViewTimeCycle.java:285`
  `SparseArray<ConstraintAttribute> mConstraintAttributeList;`
- `sources/androidx/constraintlayout/motion/utils/ViewTimeCycle.java:287`
  `SparseArray<float[]> mWaveProperties = new SparseArray<>();`
- `sources/androidx/constraintlayout/motion/utils/ViewTimeCycle.java:289`
  `public CustomSet(String str, SparseArray<ConstraintAttribute> sparseArray) {`
- `sources/androidx/constraintlayout/motion/utils/ViewTimeCycle.java:291`
  `this.mConstraintAttributeList = sparseArray;`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:906`
  `sparseArray.put(childAt.getId(), this.mFrameArrayList.get(childAt));`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:959`
  `if (!sparseBooleanArray.get(childAt2.getId()) && motionController6 != null) {`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:1465`
  `sparseArray.clear();`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:1466`
  `sparseArray.put(0, constraintWidgetContainer);`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:1467`
  `sparseArray.put(MotionLayout.this.getId(), constraintWidgetContainer);`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:1474`
  `sparseArray.put(((View) constraintWidget.getCompanionWidget()).getId(), constraintWidget);`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:1482`
  `constraintSet.applyToHelper((ConstraintHelper) view, constraintWidget2, layoutParams, sparseArray);`
- `sources/androidx/constraintlayout/motion/widget/TouchResponse.java:15`
  `import org.xmlpull.v1.XmlPullParser;`
- `sources/androidx/constraintlayout/motion/widget/TouchResponse.java:76`
  `TouchResponse(Context context, MotionLayout motionLayout, XmlPullParser xmlPullParser) {`
- `sources/androidx/constraintlayout/motion/widget/TouchResponse.java:107`
  `fillFromAttributeList(context, Xml.asAttributeSet(xmlPullParser));`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:39`
  `SparseArray<View> mChildrenByIds;`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:63`
  `private SparseArray<ConstraintWidget> mTempMapIdToWidget;`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:107`
  `public ConstraintLayout(Context context) throws XmlPullParserException, IOException {`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:109`
  `this.mChildrenByIds = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:128`
  `this.mTempMapIdToWidget = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:135`
  `public ConstraintLayout(Context context, AttributeSet attributeSet) throws XmlPullParserException, IOException {`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:137`
  `this.mChildrenByIds = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:156`
  `this.mTempMapIdToWidget = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:163`
  `public ConstraintLayout(Context context, AttributeSet attributeSet, int i) throws XmlPullParserException, IOException {`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:165`
  `this.mChildrenByIds = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:184`
  `this.mTempMapIdToWidget = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:191`
  `public ConstraintLayout(Context context, AttributeSet attributeSet, int i, int i2) throws XmlPullParserException, IOException {`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:193`
  `this.mChildrenByIds = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:212`
  `this.mTempMapIdToWidget = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1068`
  `int i3 = Integer.parseInt(strArrSplit[0]);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1069`
  `int i4 = Integer.parseInt(strArrSplit[1]);`

## BR074

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/android/support/v4/media/session/MediaControllerCompat.java:1490`
  `synchronized (mediaControllerImplApi21.mLock) {`
- `sources/android/support/v4/os/ResultReceiver.java:93`
  `synchronized (this) {`
- `sources/androidx/activity/ComponentActivity.java:73`
  `public class ComponentActivity extends androidx.core.app.ComponentActivity implements ContextAware, LifecycleOwner, ViewModelStoreOwner, HasDefaultViewModelProviderFactory, SavedStateRegistryOwner, OnBackPressedDispatcherOwner, ActivityResultRegistryOwner, ActivityResultCaller, OnConfigurationChange...`
- `sources/androidx/activity/ComponentActivity.java:81`
  `final FullyDrawnReporter mFullyDrawnReporter;`
- `sources/androidx/activity/ComponentActivity.java:147`
  `final ActivityResultContract.SynchronousResult<O> synchronousResult = activityResultContract.getSynchronousResult(componentActivity, i2);`
- `sources/androidx/activity/ComponentActivity.java:148`
  `if (synchronousResult != null) {`
- `sources/androidx/activity/ComponentActivity.java:152`
  `dispatchResult(i, synchronousResult.getValue());`
- `sources/androidx/activity/ComponentActivity.java:243`
  `savedStateRegistryControllerCreate.performAttach();`
- `sources/androidx/activity/ComponentActivity.java:244`
  `SavedStateHandleSupport.enableSavedStateHandles(this);`
- `sources/androidx/activity/ComponentActivity.java:245`
  `getSavedStateRegistry().registerSavedStateProvider(ACTIVITY_RESULT_TAG, new SavedStateRegistry.SavedStateProvider() { // from class: androidx.activity.ComponentActivity$$ExternalSyntheticLambda2`
- `sources/androidx/activity/ComponentActivity.java:246`
  `@Override // androidx.savedstate.SavedStateRegistry.SavedStateProvider`
- `sources/androidx/activity/ComponentActivity.java:247`
  `public final Bundle saveState() {`
- `sources/androidx/activity/ComponentActivity.java:262`
  `this.mActivityResultRegistry.onSaveInstanceState(bundle);`
- `sources/androidx/activity/ComponentActivity.java:268`
  `Bundle bundleConsumeRestoredStateForKey = getSavedStateRegistry().consumeRestoredStateForKey(ACTIVITY_RESULT_TAG);`
- `sources/androidx/activity/ComponentActivity.java:503`
  `if (!TextUtils.equals(e2.getMessage(), "Can not perform this action after onSaveInstanceState")) {`
- `sources/androidx/activity/ComponentActivity.java:532`
  `public FullyDrawnReporter getFullyDrawnReporter() {`
- `sources/androidx/activity/ComponentActivity.java:533`
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
- `sources/androidx/activity/result/ActivityResultRegistry.java:162`
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
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:89`
  `@Metadata(d1 = {"\u0000>\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0011\n\u0002\u0010\u000e\n\u0002\u0010$\n\u0002\u0010\u000b\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:124`
  `public ActivityResultContract.SynchronousResult<Map<String, Boolean>> getSynchronousResult(Context context, String[] input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:128`
  `return new ActivityResultContract.SynchronousResult<>(MapsKt.emptyMap());`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:140`
  `return new ActivityResultContract.SynchronousResult<>(linkedHashMap);`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:165`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\u0018\u00002\u000e\u0012\u0004\u0012\u00020\u00...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:200`
  `public ActivityResultContract.SynchronousResult<Boolean> getSynchronousResult(Context context, String input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:204`
  `return new ActivityResultContract.SynchronousResult<>(true);`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:211`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0016\u0018\u00002\u0012\u0012\u0006\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:214`
  `public final ActivityResultContract.SynchronousResult<Bitmap> getSynchronousResult(Context context, Void input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:239`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\b\u0016\u0018\u00002\u000e\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:242`
  `public final ActivityResultContract.SynchronousResult<Boolean> getSynchronousResult(Context context, Uri input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:265`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0017\u0018\u00002\u0010\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:269`
  `public final ActivityResultContract.SynchronousResult<Bitmap> getSynchronousResult(Context context, Uri input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:298`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\b\u0016\u0018\u00002\u000e\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:301`
  `public final ActivityResultContract.SynchronousResult<Boolean> getSynchronousResult(Context context, Uri input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:348`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0016\u0018\u00002\u0010\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:351`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(Context context, String input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:380`
  `@Metadata(d1 = {"\u0000:\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\b\u0017\u001...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:387`
  `public final ActivityResultContract.SynchronousResult<List<Uri>> getSynchronousResult(Context context, String input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:447`
  `@Metadata(d1 = {"\u00006\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0011\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\b\u0002\b\u0017\u0018\u00002\u0016\...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:450`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(Context context, String[] input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:479`
  `@Metadata(d1 = {"\u0000>\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0011\n\u0002\u0010\u000e\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:482`
  `public final ActivityResultContract.SynchronousResult<List<Uri>> getSynchronousResult(Context context, String[] input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:508`
  `@Metadata(d1 = {"\u0000.\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0017\u0018\u00002\u0012\u0012\u0006\u0012\u0004\u0018\u00010\u00...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:511`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(Context context, Uri input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:540`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0017\u0018\u00002\u0010\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:545`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(Context context, String input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:584`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\b\b\u0017\u0018\u0000 \u00102\u0010\u0012\u0004\u0012...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:611`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(Context context, PickVisualMediaRequest input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:793`
  `@Metadata(d1 = {"\u00008\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\b\u0017\u0018\u0000 ...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:805`
  `public final ActivityResultContract.SynchronousResult<List<Uri>> getSynchronousResult(Context context, PickVisualMediaRequest input) {`
- `sources/androidx/appcompat/R.java:678`
  `public static int submit_area = 0x7f090544;`
- `sources/androidx/appcompat/R.java:1558`
  `public static int[] SearchView = {android.R.attr.textAppearance, android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.text, android.R.attr.hint, android.R.attr.inputType, android.R.attr.imeOptions, com.viwave.RossmaxConnect.R.attr.animateMenuItems, com.viwave.RossmaxConnect.R.attr.anima...`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2612`
  `return Api21Impl.isPowerSaveMode(this.mPowerManager) ? 2 : 1;`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2745`
  `static boolean isPowerSaveMode(PowerManager powerManager) {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2746`
  `return powerManager.isPowerSaveMode();`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:196`
  `canvas.save();`
- `sources/androidx/appcompat/widget/ActionMenuPresenter.java:493`
  `public Parcelable onSaveInstanceState() {`
- `sources/androidx/appcompat/widget/ActionMenuPresenter.java:494`
  `SavedState savedState = new SavedState();`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:161`
  `synchronized (this.mInstanceLock) {`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:177`
  `synchronized (this.mInstanceLock) {`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:194`
  `new PersistHistoryAsyncTask().executeOnExecutor(AsyncTask.THREAD_POOL_EXECUTOR, new ArrayList(this.mHistoricalRecords), this.mHistoryFileName);`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:199`
  `synchronized (this.mInstanceLock) {`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:211`
  `synchronized (this.mInstanceLock) {`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:233`
  `synchronized (this.mInstanceLock) {`
- `sources/androidx/appcompat/widget/AppCompatRatingBar.java:31`
  `protected synchronized void onMeasure(int i, int i2) {`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:138`
  `int iSave = canvas.save();`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:144`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:32`
  `private boolean mAsyncFontPending;`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:233`
  `AppCompatTextHelper.this.onAsyncTypefaceReceived(weakReference, typeface);`

## BR075

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/androidx/appcompat/R.java:1205`
  `public static int AppCompatTextView_autoSizePresetSizes = 0x00000003;`
- `sources/androidx/appcompat/R.java:1543`
  `public static int[] AppCompatTextView = {android.R.attr.textAppearance, com.viwave.RossmaxConnect.R.attr.autoSizeMaxTextSize, com.viwave.RossmaxConnect.R.attr.autoSizeMinTextSize, com.viwave.RossmaxConnect.R.attr.autoSizePresetSizes, com.viwave.RossmaxConnect.R.attr.autoSizeStepGranularity, com.viwa...`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:244`
  `resetGroup();`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:247`
  `public void resetGroup() {`
- `sources/androidx/appcompat/view/menu/MenuItemImpl.java:611`
  `actionProvider2.reset();`
- `sources/androidx/appcompat/widget/AppCompatButton.java:242`
  `public void setAutoSizeTextTypeUniformWithPresetSizes(int[] iArr, int i) throws IllegalArgumentException {`
- `sources/androidx/appcompat/widget/AppCompatButton.java:244`
  `super.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatButton.java:249`
  `appCompatTextHelper.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:145`
  `Api26Impl.setAutoSizeTextTypeUniformWithPresetSizes(this.mView, autoSizeTextAvailableSizes, 0);`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:57`
  `void setAutoSizeTextTypeUniformWithPresetSizes(int[] iArr, int i);`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:302`
  `public void setAutoSizeTextTypeUniformWithPresetSizes(int[] iArr, int i) throws IllegalArgumentException {`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:304`
  `getSuperCaller().setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:309`
  `appCompatTextHelper.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:45`
  `private boolean mHasPresetAutoSizeValues = false;`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:101`
  `if (typedArrayObtainStyledAttributes.hasValue(R.styleable.AppCompatTextView_autoSizePresetSizes) && (resourceId = typedArrayObtainStyledAttributes.getResourceId(R.styleable.AppCompatTextView_autoSizePresetSizes, 0)) > 0) {`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:103`
  `setupAutoSizeUniformPresetSizes(typedArrayObtainTypedArray);`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:109`
  `if (!this.mHasPresetAutoSizeValues) {`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:205`
  `private void setupAutoSizeUniformPresetSizes(TypedArray typedArray) {`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:276`
  `this.mAutoSizeTextSizesInPx = cleanupAutoSizePresetSizes(iArr);`
- `sources/androidx/constraintlayout/core/ArrayRow.java:84`
  `public void reset() {`
- `sources/androidx/constraintlayout/core/LinearSystem.java:135`
  `public void reset() {`
- `sources/androidx/constraintlayout/core/LinearSystem.java:139`
  `solverVariable.reset();`
- `sources/androidx/constraintlayout/core/LinearSystem.java:179`
  `constraintAnchor.resetSolverVariable(this.mCache);`
- `sources/androidx/constraintlayout/core/LinearSystem.java:186`
  `solverVariable.reset();`
- `sources/androidx/constraintlayout/core/LinearSystem.java:214`
  `arrayRowAcquire.reset();`
- `sources/androidx/constraintlayout/core/LinearSystem.java:306`
  `solverVariableAcquire.reset();`
- `sources/androidx/constraintlayout/core/Metrics.java:59`
  `public void reset() {`
- `sources/androidx/constraintlayout/core/PriorityGoalRow.java:113`
  `public void reset() {`
- `sources/androidx/constraintlayout/core/PriorityGoalRow.java:204`
  `this.mAccessor.reset();`
- `sources/androidx/constraintlayout/core/SolverVariable.java:240`
  `public void reset() {`
- `sources/androidx/constraintlayout/core/utils/GridCore.java:564`
  `constraintWidget.mBottom.reset();`
- `sources/androidx/constraintlayout/core/utils/GridCore.java:565`
  `constraintWidget.mBaseline.reset();`
- `sources/androidx/constraintlayout/core/utils/GridCore.java:570`
  `constraintWidget.mLeft.reset();`
- `sources/androidx/constraintlayout/core/utils/GridCore.java:571`
  `constraintWidget.mRight.reset();`
- `sources/androidx/constraintlayout/core/widgets/ConstraintAnchor.java:125`
  `public void resetSolverVariable(Cache cache) {`
- `sources/androidx/constraintlayout/core/widgets/ConstraintAnchor.java:130`
  `solverVariable.reset();`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:868`
  `public void resetSolverVariables(Cache cache) {`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:869`
  `this.mLeft.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:870`
  `this.mTop.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:871`
  `this.mRight.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:872`
  `this.mBottom.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:873`
  `this.mBaseline.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:874`
  `this.mCenter.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:875`
  `this.mCenterX.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:876`
  `this.mCenterY.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/WidgetContainer.java:90`
  `public void resetSolverVariables(Cache cache) {`
- `sources/androidx/constraintlayout/core/widgets/WidgetContainer.java:91`
  `super.resetSolverVariables(cache);`
- `sources/androidx/constraintlayout/core/widgets/WidgetContainer.java:94`
  `this.mChildren.get(i).resetSolverVariables(cache);`
- `sources/androidx/constraintlayout/core/widgets/analyzer/BasicMeasure.java:262`
  `boolean zDirectMeasureSetup = constraintWidgetContainer2.directMeasureSetup(zEnabled);`
- `sources/androidx/constraintlayout/core/widgets/analyzer/BasicMeasure.java:264`
  `zDirectMeasureSetup &= constraintWidgetContainer2.directMeasureWithOrientation(zEnabled, 0);`
- `sources/androidx/constraintlayout/core/widgets/analyzer/BasicMeasure.java:270`
  `zDirectMeasureWithOrientation = constraintWidgetContainer2.directMeasureWithOrientation(zEnabled, 1) & zDirectMeasureSetup;`
- `sources/androidx/constraintlayout/core/widgets/analyzer/BasicMeasure.java:273`
  `zDirectMeasureWithOrientation = zDirectMeasureSetup;`
- `sources/androidx/constraintlayout/core/widgets/analyzer/WidgetGroup.java:118`
  `linearSystem.reset();`
- `sources/androidx/constraintlayout/core/widgets/analyzer/WidgetGroup.java:141`
  `linearSystem.reset();`
- `sources/androidx/constraintlayout/core/widgets/analyzer/WidgetGroup.java:145`
  `linearSystem.reset();`
- `sources/androidx/constraintlayout/helper/widget/MotionEffect.java:131`
  `public void onPreSetup(androidx.constraintlayout.motion.widget.MotionLayout r23, java.util.HashMap<android.view.View, androidx.constraintlayout.motion.widget.MotionController> r24) {`
- `sources/androidx/constraintlayout/helper/widget/MotionEffect.java:136`
  `throw new UnsupportedOperationException("Method not decompiled: androidx.constraintlayout.helper.widget.MotionEffect.onPreSetup(androidx.constraintlayout.motion.widget.MotionLayout, java.util.HashMap):void");`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:2125`
  `this.mPath.reset();`
- `sources/androidx/constraintlayout/utils/widget/ImageFilterButton.java:251`
  `matrix.reset();`
- `sources/androidx/constraintlayout/utils/widget/ImageFilterView.java:303`
  `matrix.reset();`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:319`
  `((LayoutParams) getChildAt(i2).getLayoutParams()).resetTouchBehaviorTracking();`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:322`
  `this.mDisallowInterceptReset = false;`
- `sources/androidx/core/app/NotificationCompat.java:2915`
  `private int mCustomSizePreset;`
- `sources/androidx/core/app/NotificationCompat.java:2929`
  `this.mCustomSizePreset = 0;`
- `sources/androidx/core/app/NotificationCompat.java:2939`
  `this.mCustomSizePreset = 0;`
- `sources/androidx/core/app/NotificationCompat.java:2963`
  `this.mCustomSizePreset = bundle.getInt(KEY_CUSTOM_SIZE_PRESET, 0);`
- `sources/androidx/core/app/NotificationCompat.java:3074`
  `wearableExtender.mCustomSizePreset = this.mCustomSizePreset;`
- `sources/androidx/core/app/NotificationCompat.java:3190`
  `public WearableExtender setCustomSizePreset(int i) {`
- `sources/androidx/core/app/NotificationCompat.java:3191`
  `this.mCustomSizePreset = i;`
- `sources/androidx/core/app/NotificationCompat.java:3196`
  `public int getCustomSizePreset() {`
- `sources/androidx/core/app/NotificationCompat.java:3197`
  `return this.mCustomSizePreset;`
- `sources/androidx/core/text/BidiFormatter.java:163`
  `if (getStereoReset() && z) {`
- `sources/androidx/core/util/PatternsCompat.java:15`
  `static final String IANA_TOP_LEVEL_DOMAINS = "(?:(?:aaa|aarp|abb|abbott|abbvie|abc|able|abogado|abudhabi|academy|accenture|accountant|accountants|aco|actor|ads|adult|aeg|aero|aetna|afl|africa|agakhan|agency|aig|airbus|airforce|airtel|akdn|alibaba|alipay|allfinanz|allstate|ally|alsace|alstom|amazon|a...`
- `sources/androidx/core/util/PatternsCompat.java:25`
  `private static final String STRICT_HOST_NAME = "(?:(?:[a-zA-Z0-9[ -\ud7ff豈-﷏ﷰ-\uffef𐀀-\u1fffd𠀀-\u2fffd𰀀-\u3fffd\u40000-\u4fffd\u50000-\u5fffd\u60000-\u6fffd\u70000-\u7fffd\u80000-\u8fffd\u90000-\u9fffd\ua0000-\uafffd\ub0000-\ubfffd\uc0000-\ucfffd\ud0000-\udfffd\ue1000-\uefffd&&[^ [\u2000-\u200a]\u20...`
- `sources/androidx/core/util/PatternsCompat.java:26`
  `private static final String STRICT_TLD = "(?:(?:(?:aaa|aarp|abb|abbott|abbvie|abc|able|abogado|abudhabi|academy|accenture|accountant|accountants|aco|actor|ads|adult|aeg|aero|aetna|afl|africa|agakhan|agency|aig|airbus|airforce|airtel|akdn|alibaba|alipay|allfinanz|allstate|ally|alsace|alstom|amazon|am...`
- `sources/androidx/core/util/PatternsCompat.java:42`
  `Pattern patternCompile3 = Pattern.compile("(?:(?:(?:[a-zA-Z0-9[ -\ud7ff豈-﷏ﷰ-\uffef𐀀-\u1fffd𠀀-\u2fffd𰀀-\u3fffd\u40000-\u4fffd\u50000-\u5fffd\u60000-\u6fffd\u70000-\u7fffd\u80000-\u8fffd\u90000-\u9fffd\ua0000-\uafffd\ub0000-\ubfffd\uc0000-\ucfffd\ud0000-\udfffd\ue1000-\uefffd&&[^ [\u2000-\u200a]\u2028...`
- `sources/androidx/core/widget/AutoScrollHelper.java:41`
  `boolean mNeedsReset;`
- `sources/androidx/core/widget/AutoScrollHelper.java:239`
  `this.mNeedsReset = true;`
- `sources/androidx/core/widget/AutoScrollHelper.java:249`
  `if (this.mNeedsReset) {`
- `sources/androidx/core/widget/AutoScrollHelper.java:320`
  `if (AutoScrollHelper.this.mNeedsReset) {`

## BR076

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `resources/META-INF/androidx/annotation/annotation/LICENSE.txt:116`
  `wherever such third-party notices normally appear. The contents`
- `resources/META-INF/androidx/annotation/annotation/LICENSE.txt:140`
  `names, trademarks, service marks, or product names of the Licensor,`
- `resources/META-INF/androidx/constraintlayout/constraintlayout-core/LICENSE.txt:116`
  `wherever such third-party notices normally appear. The contents`
- `resources/META-INF/androidx/constraintlayout/constraintlayout-core/LICENSE.txt:140`
  `names, trademarks, service marks, or product names of the Licensor,`
- `resources/META-INF/androidx/lifecycle/lifecycle-common/LICENSE.txt:116`
  `wherever such third-party notices normally appear. The contents`
- `resources/META-INF/androidx/lifecycle/lifecycle-common/LICENSE.txt:140`
  `names, trademarks, service marks, or product names of the Licensor,`
- `resources/res/values/strings.xml:133`
  `<string name="caring_hint_add_button">Add your first caring friend</string>`
- `resources/res/values/strings.xml:134`
  `<string name="caring_hint_add_content">You can add „Caring Friends“ with a couple of easy steps. Press the button below to start the process. You can either add the User ID you want to follow or scan the QR Code. Please make sure your „Caring Friends“ accept your request after you finished with addi...`
- `resources/res/values/strings.xml:141`
  `<string name="caring_hint_req_content">Congratulations! You have caring friends request. If you accept the invitation, your family-member / friend can browse your health data. If you want to manage your „Caring Friends“ in the feature, please click „Check“ button now.</string>`
- `resources/res/values/strings.xml:142`
  `<string name="caring_hint_req_title">CARING FRIENDS REQUEST</string>`
- `resources/res/values/strings.xml:145`
  `<string name="caring_sending_request">Sending Request…</string>`
- `resources/res/values/strings.xml:182`
  `<string name="com_facebook_internet_permission_error_message">WebView login requires INTERNET permission</string>`
- `resources/res/values/strings.xml:201`
  `<string name="com_facebook_smart_login_confirmation_title">Confirm Login</string>`
- `resources/res/values/strings.xml:314`
  `<string name="drawer_third_party">Third-party collaboration</string>`
- `resources/res/values/strings.xml:424`
  `<string name="login">SIGN IN</string>`
- `resources/res/values/strings.xml:486`
  `<string name="meal_before">Before meal</string>`
- `resources/res/values/strings.xml:637`
  `<string name="qr_share_content" formatted="false">Inviting you to join in follow %s health status. This invitation link is valid for 24 hours.%s\nAfter clicking the link, you will directly open the Rossmax HealthStyle APP and can easily join the follow.\n\nThe steps are as follows:\n1.Click the link...`
- `sources/androidx/activity/ComponentActivity.java:210`
  `throw new IllegalStateException("getLifecycle() returned null in ComponentActivity's constructor. Please make sure you are lazily constructing your Lifecycle in the first call to getLifecycle() rather than relying on field initialization.");`
- `sources/androidx/activity/ComponentActivity.java:448`
  `throw new IllegalStateException("Your activity is not yet attached to the Application instance. You can't request ViewModel before onCreate call.");`
- `sources/androidx/activity/result/ActivityResultRegistry.java:38`
  `throw new IllegalStateException("LifecycleOwner " + lifecycleOwner + " is attempting to register while current state is " + lifecycle.getCurrentState() + ". LifecycleOwners must call register before they are STARTED.");`
- `sources/androidx/activity/result/ActivityResultRegistry.java:73`
  `public void launch(I i, ActivityOptionsCompat activityOptionsCompat) throws Exception {`
- `sources/androidx/activity/result/ActivityResultRegistry.java:76`
  `throw new IllegalStateException("Attempting to launch an unregistered ActivityResultLauncher with contract " + activityResultContract + " and input " + i + ". You must ensure the ActivityResultLauncher is registered before calling launch().");`
- `sources/androidx/activity/result/ActivityResultRegistry.java:115`
  `public void launch(I i, ActivityOptionsCompat activityOptionsCompat) throws Exception {`
- `sources/androidx/activity/result/ActivityResultRegistry.java:118`
  `throw new IllegalStateException("Attempting to launch an unregistered ActivityResultLauncher with contract " + activityResultContract + " and input " + i + ". You must ensure the ActivityResultLauncher is registered before calling launch().");`
- `sources/androidx/activity/result/ActivityResultRegistry.java:148`
  `Log.w(LOG_TAG, "Dropping pending result for request " + str + ": " + this.mParsedPendingResults.get(str));`
- `sources/androidx/activity/result/ActivityResultRegistry.java:152`
  `Log.w(LOG_TAG, "Dropping pending result for request " + str + ": " + this.mPendingResults.getParcelable(str));`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:419`
  `throw new IllegalStateException("This Activity already has an action bar supplied by the window decor. Do not request Window.FEATURE_SUPPORT_ACTION_BAR and set windowActionBar to false in your theme to use a Toolbar instead.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1801`
  `throw new AndroidRuntimeException("Window feature must be requested before adding content");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1807`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1813`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR_OVERLAY id when requesting this feature.");`
- `sources/androidx/collection/FloatList.java:19`
  `@Metadata(d1 = {"\u0000d\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0010\u0014\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0010\u000b\n\u0000\n\u0002\u0018\u0002\n\u0002\u0010\u0007\n\u0002\u0018\u0002\n\u0002\b\u0011\n\u0002\u0018\u0002\n\u...`
- `sources/androidx/collection/FloatList.java:98`
  `public final float first() {`
- `sources/androidx/collection/FloatList.java:326`
  `int first = intRangeUntil.getFirst();`
- `sources/androidx/collection/FloatList.java:328`
  `if (first > last) {`
- `sources/androidx/collection/FloatList.java:331`
  `while (fArr[first] == fArr2[first]) {`
- `sources/androidx/collection/FloatList.java:332`
  `if (first == last) {`
- `sources/androidx/collection/FloatList.java:335`
  `first++;`
- `sources/androidx/collection/FloatList.java:384`
  `int first = intRangeUntil.getFirst();`
- `sources/androidx/collection/FloatList.java:386`
  `if (first > last) {`
- `sources/androidx/collection/FloatList.java:389`
  `while (contains(elements.get(first))) {`
- `sources/androidx/collection/FloatList.java:390`
  `if (first == last) {`
- `sources/androidx/collection/FloatList.java:393`
  `first++;`
- `sources/androidx/collection/FloatList.java:411`
  `public final float first(Function1<? super Float, Boolean> predicate) {`
- `sources/androidx/collection/FloatList.java:421`
  `throw new NoSuchElementException("FloatList contains no element matching the predicate.");`
- `sources/androidx/collection/FloatList.java:515`
  `throw new NoSuchElementException("FloatList contains no element matching the predicate.");`
- `sources/androidx/collection/IntList.java:19`
  `@Metadata(d1 = {"\u0000'\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0010\u0015\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0010\u000b\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0011\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002...`
- `sources/androidx/collection/IntList.java:98`
  `public final int first() {`
- `sources/androidx/collection/IntList.java:326`
  `int first = intRangeUntil.getFirst();`
- `sources/androidx/collection/IntList.java:328`
  `if (first > last) {`
- `sources/androidx/collection/IntList.java:331`
  `while (iArr[first] == iArr2[first]) {`
- `sources/androidx/collection/IntList.java:332`
  `if (first == last) {`
- `sources/androidx/collection/IntList.java:335`
  `first++;`
- `sources/androidx/collection/IntList.java:384`
  `int first = intRangeUntil.getFirst();`
- `sources/androidx/collection/IntList.java:386`
  `if (first > last) {`
- `sources/androidx/collection/IntList.java:389`
  `while (contains(elements.get(first))) {`
- `sources/androidx/collection/IntList.java:390`
  `if (first == last) {`
- `sources/androidx/collection/IntList.java:393`
  `first++;`
- `sources/androidx/collection/IntList.java:411`
  `public final int first(Function1<? super Integer, Boolean> predicate) {`
- `sources/androidx/collection/IntList.java:421`
  `throw new NoSuchElementException("IntList contains no element matching the predicate.");`
- `sources/androidx/collection/IntList.java:515`
  `throw new NoSuchElementException("IntList contains no element matching the predicate.");`
- `sources/androidx/collection/LongList.java:19`
  `@Metadata(d1 = {"\u0000d\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0010\u0016\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0010\u000b\n\u0000\n\u0002\u0018\u0002\n\u0002\u0010\t\n\u0002\u0018\u0002\n\u0002\b\u0011\n\u0002\u0018\u0002\n\u0002...`
- `sources/androidx/collection/LongList.java:98`
  `public final long first() {`
- `sources/androidx/collection/LongList.java:326`
  `int first = intRangeUntil.getFirst();`
- `sources/androidx/collection/LongList.java:328`
  `if (first > last) {`
- `sources/androidx/collection/LongList.java:331`
  `while (jArr[first] == jArr2[first]) {`
- `sources/androidx/collection/LongList.java:332`
  `if (first == last) {`
- `sources/androidx/collection/LongList.java:335`
  `first++;`
- `sources/androidx/collection/LongList.java:384`
  `int first = intRangeUntil.getFirst();`
- `sources/androidx/collection/LongList.java:386`
  `if (first > last) {`
- `sources/androidx/collection/LongList.java:389`
  `while (contains(elements.get(first))) {`
- `sources/androidx/collection/LongList.java:390`
  `if (first == last) {`
- `sources/androidx/collection/LongList.java:393`
  `first++;`
- `sources/androidx/collection/LongList.java:411`
  `public final long first(Function1<? super Long, Boolean> predicate) {`
- `sources/androidx/collection/LongList.java:421`
  `throw new NoSuchElementException("LongList contains no element matching the predicate.");`
- `sources/androidx/collection/LongList.java:515`
  `throw new NoSuchElementException("LongList contains no element matching the predicate.");`
- `sources/androidx/collection/ObjectList.java:21`
  `@Metadata(d1 = {"\u0000r\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0010\u0011\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0010\u000b\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010 \n\u0002\b\u0005\n\u0...`
- `sources/androidx/collection/ObjectList.java:135`
  `public final E first() {`
- `sources/androidx/collection/ObjectList.java:307`
  `int first = intRangeUntil.getFirst();`
- `sources/androidx/collection/ObjectList.java:309`
  `if (first > last) {`
- `sources/androidx/collection/ObjectList.java:312`
  `while (Intrinsics.areEqual(objArr[first], objArr2[first])) {`

## BR077

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `sources/io/grpc/okhttp/OkHttpChannelBuilder.java:438`
  `SSLContext sSLContext = SSLContext.getInstance("TLS", Platform.get().getProvider());`
- `sources/io/grpc/okhttp/OkHttpChannelBuilder.java:439`
  `sSLContext.init(keyManagerArrCreateKeyManager, trustManagerArrCreateTrustManager, null);`
- `sources/io/grpc/okhttp/OkHttpChannelBuilder.java:440`
  `return SslSocketFactoryResult.factory(sSLContext.getSocketFactory());`
- `sources/io/grpc/okhttp/OkHttpServerBuilder.java:278`
  `SSLContext sSLContext = SSLContext.getInstance("TLS", Platform.get().getProvider());`
- `sources/io/grpc/okhttp/OkHttpServerBuilder.java:279`
  `sSLContext.init(keyManagerArrCreateKeyManager, trustManagerArrCreateTrustManager, null);`
- `sources/io/grpc/okhttp/OkHttpServerBuilder.java:280`
  `SSLSocketFactory socketFactory = sSLContext.getSocketFactory();`
- `sources/io/grpc/okhttp/internal/Platform.java:119`
  `Provider provider = SSLContext.getDefault().getProvider();`
- `sources/io/grpc/okhttp/internal/Platform.java:122`
  `SSLContext sSLContext = SSLContext.getInstance("TLS", provider);`
- `sources/io/grpc/okhttp/internal/Platform.java:123`
  `sSLContext.init(null, null, null);`
- `sources/io/grpc/okhttp/internal/Platform.java:129`
  `})).invoke(sSLContext.createSSLEngine(), new Object[0]);`
- `sources/okhttp3/OkHttpClient.java:579`
  `@Metadata(d1 = {"\u0000\u0086\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010!\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010...`
- `sources/okhttp3/OkHttpClient.java:792`
  `/* JADX INFO: renamed from: getSslSocketFactoryOrNull$okhttp, reason: from getter */`
- `sources/okhttp3/OkHttpClient.java:793`
  `public final SSLSocketFactory getSslSocketFactoryOrNull() {`
- `sources/okhttp3/OkHttpClient.java:794`
  `return this.sslSocketFactoryOrNull;`
- `sources/okhttp3/OkHttpClient.java:797`
  `public final void setSslSocketFactoryOrNull$okhttp(SSLSocketFactory sSLSocketFactory) {`
- `sources/okhttp3/OkHttpClient.java:798`
  `this.sslSocketFactoryOrNull = sSLSocketFactory;`
- `sources/okhttp3/internal/platform/Platform.java:88`
  `Intrinsics.checkNotNullExpressionValue(sSLContext, "getInstance(...)");`
- `sources/okhttp3/internal/platform/Platform.java:89`
  `return sSLContext;`
- `sources/okhttp3/internal/platform/Platform.java:205`
  `public SSLSocketFactory newSslSocketFactory(X509TrustManager trustManager) {`
- `sources/okhttp3/internal/platform/Platform.java:208`
  `SSLContext sSLContextNewSSLContext = newSSLContext();`
- `sources/okhttp3/internal/platform/Platform.java:210`
  `SSLSocketFactory socketFactory = sSLContextNewSSLContext.getSocketFactory();`

## BR078

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/io/grpc/okhttp/OkHttpChannelBuilder.java:54`
  `import javax.net.ssl.HostnameVerifier;`
- `sources/okhttp3/MultipartBody.java:96`
  `@Override // okhttp3.RequestBody`
- `sources/okhttp3/OkHttpClient.java:21`
  `import javax.net.ssl.HostnameVerifier;`
- `sources/okhttp3/OkHttpClient.java:43`
  `import okhttp3.internal.tls.CertificateChainCleaner;`
- `sources/okhttp3/OkHttpClient.java:44`
  `import okhttp3.internal.tls.OkHostnameVerifier;`
- `sources/okhttp3/OkHttpClient.java:45`
  `import okhttp3.internal.ws.RealWebSocket;`
- `sources/okhttp3/OkHttpClient.java:47`
  `/* JADX INFO: compiled from: OkHttpClient.kt */`
- `sources/okhttp3/OkHttpClient.java:49`
  `@Metadata(d1 = {"\u0000ú\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0002\b\u0003\n\u000...`
- `sources/okhttp3/OkHttpClient.java:50`
  `public class OkHttpClient implements Call.Factory, WebSocket.Factory {`
- `sources/okhttp3/OkHttpClient.java:578`
  `/* JADX INFO: compiled from: OkHttpClient.kt */`
- `sources/okhttp3/OkHttpClient.java:579`
  `@Metadata(d1 = {"\u0000\u0086\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010!\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010...`
- `sources/okhttp3/OkHttpClient.java:954`
  `this.dns = okHttpClient.dns();`
- `sources/okhttp3/OkHttpClient.java:955`
  `this.proxy = okHttpClient.proxy();`
- `sources/okhttp3/OkHttpClient.java:956`
  `this.proxySelector = okHttpClient.proxySelector();`
- `sources/okhttp3/OkHttpClient.java:957`
  `this.proxyAuthenticator = okHttpClient.proxyAuthenticator();`
- `sources/okhttp3/OkHttpClient.java:958`
  `this.socketFactory = okHttpClient.socketFactory();`
- `sources/okhttp3/OkHttpClient.java:959`
  `this.sslSocketFactoryOrNull = okHttpClient.sslSocketFactoryOrNull;`
- `sources/okhttp3/OkHttpClient.java:960`
  `this.x509TrustManagerOrNull = okHttpClient.getX509TrustManager();`
- `sources/okhttp3/OkHttpClient.java:961`
  `this.connectionSpecs = okHttpClient.connectionSpecs();`
- `sources/okhttp3/OkHttpClient.java:962`
  `this.protocols = okHttpClient.protocols();`
- `sources/okhttp3/OkHttpClient.java:963`
  `this.hostnameVerifier = okHttpClient.hostnameVerifier();`
- `sources/okhttp3/OkHttpClient.java:964`
  `this.certificatePinner = okHttpClient.certificatePinner();`
- `sources/okhttp3/OkHttpClient.java:965`
  `this.certificateChainCleaner = okHttpClient.getCertificateChainCleaner();`
- `sources/okhttp3/OkHttpClient.java:966`
  `this.callTimeout = okHttpClient.callTimeoutMillis();`
- `sources/okhttp3/RequestBody.java:237`
  `return new RequestBody() { // from class: okhttp3.RequestBody$Companion$toRequestBody$2`
- `sources/okhttp3/RequestBody.java:238`
  `@Override // okhttp3.RequestBody`
- `sources/okhttp3/RequestBody.java:243`
  `@Override // okhttp3.RequestBody`
- `sources/okhttp3/internal/connection/RealConnection.java:218`
  `if (this.http2Connection == null || routes == null || !routeMatchesAny(routes) || address.hostnameVerifier() != OkHostnameVerifier.INSTANCE || !supportsUrl(address.url())) {`
- `sources/okhttp3/internal/connection/RealConnection.java:268`
  `OkHostnameVerifier okHostnameVerifier = OkHostnameVerifier.INSTANCE;`
- `sources/okhttp3/internal/connection/RealConnection.java:272`
  `if (okHostnameVerifier.verify(strHost, (X509Certificate) certificate)) {`
- `sources/okhttp3/internal/connection/RealConnection.java:279`
  `public final ExchangeCodec newCodec$okhttp(OkHttpClient client, RealInterceptorChain chain) throws SocketException {`
- `sources/okhttp3/internal/connection/RealRoutePlanner.java:226`
  `@Override // okhttp3.internal.connection.RoutePlanner`
- `sources/okhttp3/internal/http/CallServerInterceptor.java:27`
  `@Metadata(d1 = {"\u0000,\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0000\u0018\u00002\u00020\u0001B\u000f\u0012\u0006\u0010\u0002\u001a\u00020\u0003...`
- `sources/okhttp3/internal/http2/PushObserver.java:36`
  `@Metadata(d1 = {"\u00008\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\b\u0002\u0018\u00002\u00...`
- `sources/okhttp3/internal/http2/PushObserver.java:38`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:44`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:50`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:55`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/platform/Android10Platform.java:21`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/Android10Platform.java:22`
  `import okhttp3.internal.platform.android.Android10SocketAdapter;`
- `sources/okhttp3/internal/platform/Android10Platform.java:28`
  `import okhttp3.internal.platform.android.SocketAdapter;`
- `sources/okhttp3/internal/platform/Android10Platform.java:29`
  `import okhttp3.internal.tls.CertificateChainCleaner;`
- `sources/okhttp3/internal/platform/Android10Platform.java:30`
  `import okhttp3.internal.tls.TrustRootIndex;`
- `sources/okhttp3/internal/platform/Android10Platform.java:34`
  `@Metadata(d1 = {"\u0000j\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\...`
- `sources/okhttp3/internal/platform/Android10Platform.java:59`
  `@Override // okhttp3.internal.platform.ContextAwarePlatform`
- `sources/okhttp3/internal/platform/Android10Platform.java:64`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Android10Platform.java:86`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Android10Platform.java:92`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Android10Platform.java:99`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Android10Platform.java:172`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Android10Platform.java:180`
  `@Metadata(d1 = {"\u0000\u001a\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\b\u0086\u0003\u0018\u00002\u00020\u0001B\t\b\u0002¢\u0006\u0004\b\u0002\u0010\u0003J\b\u0010\u0007\u001a\u0004\u0018\u00010\bR\u0011\u0010\u0004\u001a...`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:31`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:32`
  `import okhttp3.internal.platform.android.AndroidCertificateChainCleaner;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:38`
  `import okhttp3.internal.platform.android.StandardAndroidSocketAdapter;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:39`
  `import okhttp3.internal.tls.CertificateChainCleaner;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:40`
  `import okhttp3.internal.tls.TrustRootIndex;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:44`
  `@Metadata(d1 = {"\u0000\u0082\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0000\n...`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:88`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:110`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:161`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:168`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:182`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:199`
  `@Metadata(d1 = {"\u00008\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u000e\n\u0000\b\u0080\b\u0018\u00...`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:256`
  `@Override // okhttp3.internal.tls.TrustRootIndex`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:15`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:19`
  `@Metadata(d1 = {"\u0000B\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\...`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:51`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:57`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Platform.java:37`
  `import okhttp3.OkHttpClient;`
- `sources/okhttp3/internal/platform/Platform.java:42`
  `import okhttp3.internal.tls.CertificateChainCleaner;`
- `sources/okhttp3/internal/platform/Platform.java:43`
  `import okhttp3.internal.tls.TrustRootIndex;`
- `sources/okhttp3/internal/platform/Platform.java:48`
  `@Metadata(d1 = {"\u0000t\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\...`
- `sources/okhttp3/internal/platform/Platform.java:189`
  `message = message + " To see where this was allocated, set the OkHttpClient logger level to FINE: Logger.getLogger(OkHttpClient.class.getName()).setLevel(Level.FINE);";`
- `sources/okhttp3/internal/platform/PlatformRegistry.java:11`
  `@Metadata(d1 = {"\u0000\"\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0006\bÆ\u0002\u0018\u00002\u00020\u0001B\t\b\u0002¢\u0006\u0004\b\u0002\u0010\u0003J\u0006\u0010\u0004\u001a\u00020\u0005R\...`
- `sources/okhttp3/internal/platform/android/Android10SocketAdapter.java:14`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/android/Android10SocketAdapter.java:15`
  `import okhttp3.internal.platform.Platform;`
- `sources/okhttp3/internal/platform/android/Android10SocketAdapter.java:25`
  `@Override // okhttp3.internal.platform.android.SocketAdapter`
- `sources/okhttp3/internal/platform/android/Android10SocketAdapter.java:30`
  `@Override // okhttp3.internal.platform.android.SocketAdapter`
- `sources/okhttp3/internal/platform/android/Android10SocketAdapter.java:35`
  `@Override // okhttp3.internal.platform.android.SocketAdapter`
- `sources/okhttp3/internal/platform/android/AndroidCertificateChainCleaner.java:1`
  `package okhttp3.internal.platform.android;`

## BR079

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/com/facebook/internal/WebDialog.java:523`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/google/android/recaptcha/internal/zzil.java:87`
  `r7.setJavaScriptEnabled(r5)`
- `sources/com/viwave/rossmaxconnect/MainAdvActivity.java:490`
  `webView.getSettings().setJavaScriptEnabled(true);`
- `sources/com/viwave/rossmaxconnect/SetRegionActivity.java:246`
  `webView.getSettings().setJavaScriptEnabled(true);`
- `sources/com/viwave/rossmaxconnect/advfragment/WebFragment.java:114`
  `webView.getSettings().setJavaScriptEnabled(true);`

## BR080

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/a/a.java:66`
  `Log.v(Utility.DEBUG_TAG, "onCharacteristicChanged " + bluetoothGattCharacteristic.getUuid().toString());`
- `sources/a/a.java:95`
  `Log.v(Utility.DEBUG_TAG, "onCharacteristicRead " + bluetoothGattCharacteristic.getUuid().toString() + p.SPACE + i);`
- `sources/a/a.java:112`
  `Log.v(Utility.DEBUG_TAG, "onCharacteristicWrite " + bluetoothGattCharacteristic.getUuid().toString() + p.SPACE + i);`
- `sources/a/a.java:132`
  `Log.v(Utility.DEBUG_TAG, "onConnectionStateChange status:" + i + " newState:" + i2);`
- `sources/a/a.java:140`
  `Log.v(Utility.DEBUG_TAG, macAddress + " device disconnected " + i);`
- `sources/a/a.java:148`
  `Log.v(Utility.DEBUG_TAG, macAddress + " device connected");`
- `sources/a/a.java:162`
  `Log.v(Utility.DEBUG_TAG, "attempting to start service discovery:" + a.this.f.discoverServices());`
- `sources/a/a.java:167`
  `Log.v(Utility.DEBUG_TAG, "on Descriptor read " + bluetoothGattDescriptor.getUuid() + ", value: " + Utility.byte2Hex(bluetoothGattDescriptor.getValue()));`
- `sources/a/a.java:187`
  `Log.v(Utility.DEBUG_TAG, "onDescriptorWrite " + bluetoothGattDescriptor.getUuid().toString() + p.SPACE + i);`
- `sources/a/a.java:208`
  `Log.v(Utility.DEBUG_TAG, "onMtuChanged -> " + i);`
- `sources/a/a.java:210`
  `Log.v(Utility.DEBUG_TAG, "attempting to start service discovery:" + a.this.f.discoverServices());`
- `sources/a/a.java:254`
  `Log.v(Utility.DEBUG_TAG, a.this.f8d.getMacAddress() + " timeout expired");`
- `sources/a/a.java:274`
  `Log.v(Utility.DEBUG_TAG, "BOND_BONDING " + a.this.f7c);`
- `sources/a/a.java:559`
  `Log.v(Utility.DEBUG_TAG, "starting pairing");`
- `sources/a/a.java:609`
  `Log.v(Utility.DEBUG_TAG, "\tdevice NOT connected, call onDisconnect");`
- `sources/a/a.java:646`
  `Log.v(Utility.DEBUG_TAG, "read Characteristic " + bluetoothGattCharacteristic.getUuid());`
- `sources/a/a.java:807`
  `Log.v(Utility.DEBUG_TAG, "Write Descriptor " + bluetoothGattDescriptor.getUuid());`
- `sources/a/a.java:859`
  `Log.v(Utility.DEBUG_TAG, "Can't connect, Connecting State " + this.g);`
- `sources/a/a.java:868`
  `Log.d(Utility.DEBUG_TAG, vUBleDevice.getMacAddress() + " create a new connection.");`
- `sources/a/a.java:892`
  `Log.v(Utility.DEBUG_TAG, "write Characteristic " + bluetoothGattCharacteristic.getUuid() + p.SPACE + Utility.byte2Hex(bArr));`
- `sources/a/a.java:907`
  `Log.v(Utility.DEBUG_TAG, "Read Descriptor " + bluetoothGattDescriptor.getUuid());`
- `sources/android/support/v4/media/MediaBrowserCompat.java:649`
  `Log.d(MediaBrowserCompat.TAG, "addSubscription failed with RemoteException parentId=" + str);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:767`
  `Log.d(MediaBrowserCompat.TAG, "ServiceCallbacks.onConnect...");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:782`
  `Log.d(MediaBrowserCompat.TAG, "addSubscription failed with RemoteException.");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:880`
  `Log.d(MediaBrowserCompat.TAG, "  mServiceConnection=" + this.mServiceConnection);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:881`
  `Log.d(MediaBrowserCompat.TAG, "  mServiceBinderWrapper=" + this.mServiceBinderWrapper);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:882`
  `Log.d(MediaBrowserCompat.TAG, "  mCallbacksMessenger=" + this.mCallbacksMessenger);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:883`
  `Log.d(MediaBrowserCompat.TAG, "  mRootId=" + this.mRootId);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:884`
  `Log.d(MediaBrowserCompat.TAG, "  mMediaSessionToken=" + this.mMediaSessionToken);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2059`
  `Log.d("AppCompatDelegate", "Exception while getting ActivityInfo", e2);`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:1569`
  `Log.v(MotionLayout.TAG, str2 + " done. ");`
- `sources/androidx/fragment/app/DefaultSpecialEffectsController.java:266`
  `Log.v(FragmentManager.TAG, "Animation from operation " + operation + " has been cancelled.");`
- `sources/androidx/fragment/app/FragmentLayoutInflaterFactory.java:70`
  `Log.v("FragmentManager", "Fragment " + fragmentFindFragmentById + " has been inflated via the <fragment> tag: id=0x" + Integer.toHexString(resourceId));`
- `sources/androidx/fragment/app/FragmentLayoutInflaterFactory.java:82`
  `Log.v("FragmentManager", "Retained Fragment " + fragmentFindFragmentById + " has been re-attached via the <fragment> tag: id=0x" + Integer.toHexString(resourceId));`
- `sources/androidx/fragment/app/FragmentManager.java:1669`
  `Log.v(TAG, "Discarding retained Fragment " + fragment2 + " that was not found in the set of active Fragments " + fragmentManagerState.mActive);`
- `sources/androidx/fragment/app/FragmentStateManager.java:468`
  `Log.d("FragmentManager", "moveto ACTIVITY_CREATED: " + this.mFragment);`
- `sources/androidx/fragment/app/FragmentStore.java:125`
  `Log.v("FragmentManager", "Removed fragment from active set " + fragment);`
- `sources/androidx/fragment/app/SpecialEffectsController.java:287`
  `Log.v(FragmentManager.TAG, "SpecialEffectsController: Finished executing pending operations");`
- `sources/androidx/localbroadcastmanager/content/LocalBroadcastManager.java:151`
  `Log.v(TAG, "Resolving type " + strResolveTypeIfNeeded + " scheme " + scheme + " of intent " + intent);`
- `sources/androidx/localbroadcastmanager/content/LocalBroadcastManager.java:156`
  `Log.v(TAG, "Action list: " + arrayList2);`

## BR081

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzmy.java:114`
  `throw new IllegalArgumentException("cannot call withMasterKeyUri() after calling doNotUseKeystore()");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zznc.java:16`
  `KeyStore keyStore = KeyStore.getInstance("AndroidKeyStore");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zznd.java:3`
  `import android.security.keystore.KeyGenParameterSpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zznd.java:64`
  `KeyGenParameterSpec keyGenParameterSpecBuild = new KeyGenParameterSpec.Builder(strZza, 3).setKeySize(256).setBlockModes(CodePackage.GCM).setEncryptionPaddings("NoPadding").build();`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zznd.java:65`
  `KeyGenerator keyGenerator = KeyGenerator.getInstance("AES", "AndroidKeyStore");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zznd.java:66`
  `keyGenerator.init(keyGenParameterSpecBuild);`
- `sources/io/grpc/okhttp/OkHttpChannelBuilder.java:481`
  `KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());`
- `sources/io/grpc/okhttp/OkHttpChannelBuilder.java:501`
  `KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:98`
  `KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());`

## BR082

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:15`
  `import androidx.core.content.FileProvider;`
- `sources/androidx/browser/customtabs/TrustedWebUtils.java:10`
  `import androidx.core.content.FileProvider;`
- `sources/androidx/browser/customtabs/TrustedWebUtils.java:44`
  `Uri uriForFile = FileProvider.getUriForFile(context, str, file);`
- `sources/androidx/core/content/FileProvider.java:271`
  `@Override // androidx.core.content.FileProvider.PathStrategy`
- `sources/androidx/core/content/FileProvider.java:298`
  `@Override // androidx.core.content.FileProvider.PathStrategy`

## BR083

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:99`
  `<intent-filter android:autoVerify="true">`

## BR084

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/androidx/credentials/CredentialManagerImpl.java:95`
  `PendingIntent activity = PendingIntent.getActivity(this.context, 0, intent, AccessibilityEventCompat.TYPE_VIEW_TARGETED_BY_SCROLL);`

## BR086

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/androidx/activity/result/contract/ActivityResultContracts.java:232`
  `return (Bitmap) intent.getParcelableExtra(ShareConstants.WEB_DIALOG_PARAM_DATA);`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:291`
  `return (Bitmap) intent.getParcelableExtra(ShareConstants.WEB_DIALOG_PARAM_DATA);`
- `sources/androidx/annotation/ChecksSdkIntAtLeast.java:22`
  `@Metadata(d1 = {"\u0000\u0018\n\u0002\u0018\u0002\n\u0002\u0010\u001b\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0006\b\u0087\u0002\u0018\u00002\u00020\u0001B2\u0012\b\b\u0002\u0010\u0002\u001a\u00020\u0003\u0012\b\b\u0002\u0010\u0004\u001a\u00020\u0005\u0012\b\b\u0002\u0010\u000...`
- `sources/androidx/annotation/DeprecatedSinceApi.java:22`
  `@Metadata(d1 = {"\u0000\u0018\n\u0002\u0018\u0002\n\u0002\u0010\u001b\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0003\b\u0087\u0002\u0018\u00002\u00020\u0001B\u0012\u0012\u0006\u0010\u0002\u001a\u00020\u0003\u0012\b\b\u0002\u0010\u0004\u001a\u00020\u0005R\u000f\u0010\u0002\u001a\...`
- `sources/androidx/annotation/Discouraged.java:16`
  `@Metadata(d1 = {"\u0000\u0012\n\u0002\u0018\u0002\n\u0002\u0010\u001b\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0002\b\u0087\u0002\u0018\u00002\u00020\u0001B\b\u0012\u0006\u0010\u0002\u001a\u00020\u0003R\u000f\u0010\u0002\u001a\u00020\u0003¢\u0006\u0006\u001a\u0004\b\u0002\u0010\u0004¨\u0006\u0005"}, d...`
- `sources/androidx/annotation/RequiresExtension.java:5`
  `import com.facebook.share.internal.ShareConstants;`
- `sources/androidx/annotation/RequiresExtension.java:25`
  `@Metadata(d1 = {"\u0000\u0012\n\u0002\u0018\u0002\n\u0002\u0010\u001b\n\u0000\n\u0002\u0010\b\n\u0002\b\u0003\b\u0087\u0002\u0018\u00002\u00020\u0001B\u0014\u0012\b\b\u0001\u0010\u0002\u001a\u00020\u0003\u0012\b\b\u0001\u0010\u0004\u001a\u00020\u0003R\u000f\u0010\u0002\u001a\u00020\u0003¢\u0006\u000...`
- `sources/androidx/appcompat/R.java:63`
  `public static int actionModeShareDrawable = 0x7f04001d;`
- `sources/androidx/appcompat/R.java:517`
  `public static int abc_ab_share_pack_mtrl_alpha = 0x7f080044;`
- `sources/androidx/appcompat/R.java:525`
  `public static int abc_btn_default_mtrl_shape = 0x7f08004c;`
- `sources/androidx/appcompat/R.java:1249`
  `public static int AppCompatTheme_actionModeShareDrawable = 0x0000001b;`
- `sources/androidx/appcompat/R.java:1361`
  `public static int DrawerArrowToggle_arrowShaftLength = 0x00000001;`
- `sources/androidx/appcompat/R.java:1544`
  `public static int[] AppCompatTheme = {android.R.attr.windowIsFloating, android.R.attr.windowAnimationStyle, com.viwave.RossmaxConnect.R.attr.actionBarDivider, com.viwave.RossmaxConnect.R.attr.actionBarItemBackground, com.viwave.RossmaxConnect.R.attr.actionBarPopupTheme, com.viwave.RossmaxConnect.R.a...`
- `sources/androidx/appcompat/R.java:1548`
  `public static int[] DrawerArrowToggle = {com.viwave.RossmaxConnect.R.attr.arrowHeadLength, com.viwave.RossmaxConnect.R.attr.arrowShaftLength, com.viwave.RossmaxConnect.R.attr.barLength, com.viwave.RossmaxConnect.R.attr.color, com.viwave.RossmaxConnect.R.attr.drawableSize, com.viwave.RossmaxConnect.R...`
- `sources/androidx/appcompat/R.java:1561`
  `public static int[] TextAppearance = {android.R.attr.textSize, android.R.attr.typeface, android.R.attr.textStyle, android.R.attr.textColor, android.R.attr.textColorHint, android.R.attr.textColorLink, android.R.attr.shadowColor, android.R.attr.shadowDx, android.R.attr.shadowDy, android.R.attr.shadowR...`
- `sources/androidx/appcompat/app/AppCompatDelegate.java:106`
  `public abstract boolean isHandleNativeActionModesEnabled();`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1110`
  `public boolean isHandleNativeActionModesEnabled() {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2486`
  `if (AppCompatDelegateImpl.this.isHandleNativeActionModesEnabled() && i == 0) {`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:24`
  `private float mArrowShaftLength;`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:67`
  `this.mArrowShaftLength = typedArrayObtainStyledAttributes.getDimension(R.styleable.DrawerArrowToggle_arrowShaftLength, 0.0f);`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:177`
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
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:73`
  `ShapeDrawable shapeDrawable = new ShapeDrawable(getDrawableShape());`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:74`
  `shapeDrawable.getPaint().setShader(new BitmapShader(bitmap, Shader.TileMode.REPEAT, Shader.TileMode.CLAMP));`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:75`
  `shapeDrawable.getPaint().setColorFilter(bitmapDrawable.getPaint().getColorFilter());`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:76`
  `return z ? new ClipDrawable(shapeDrawable, 3, 1) : shapeDrawable;`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:99`
  `private Shape getDrawableShape() {`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:100`
  `return new RoundRectShape(new float[]{5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f}, null, null);`
- `sources/androidx/appcompat/widget/DropDownListView.java:516`
  `private static boolean sHasMethods;`
- `sources/androidx/appcompat/widget/DropDownListView.java:532`
  `sHasMethods = true;`
- `sources/androidx/appcompat/widget/SearchView.java:1105`
  `Api29Impl.refreshAutoCompleteResults(this.mSearchSrcTextView);`
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
- `sources/androidx/browser/browseractions/BrowserActionsFallbackMenuUi.java:63`
  `private PendingIntent buildShareAction() {`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:7`
  `import android.content.SharedPreferences;`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:86`
  `private static boolean shouldCleanUp(SharedPreferences sharedPreferences) {`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:87`
  `return System.currentTimeMillis() > sharedPreferences.getLong(BrowserServiceFileProvider.LAST_CLEANUP_TIME_KEY, System.currentTimeMillis()) + CLEANUP_REQUIRED_TIME_SPAN;`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:33`
  `public static final String EXTRA_DEFAULT_SHARE_MENU_ITEM = "android.support.customtabs.extra.SHARE_MENU_ITEM";`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:99`
  `private int mShareState = 0;`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:170`
  `public Builder addDefaultShareMenuItem() {`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:171`
  `setShareState(1);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:176`
  `public Builder setDefaultShareMenuItemEnabled(boolean z) {`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:178`
  `setShareState(1);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:181`
  `setShareState(2);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:185`
  `public Builder setShareState(int i) {`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:195`
  `this.mIntent.putExtra(CustomTabsIntent.EXTRA_DEFAULT_SHARE_MENU_ITEM, false);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:198`
  `this.mIntent.removeExtra(CustomTabsIntent.EXTRA_DEFAULT_SHARE_MENU_ITEM);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:321`
  `this.mIntent.putExtra(CustomTabsIntent.EXTRA_SHARE_STATE, this.mShareState);`
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
- `sources/androidx/cardview/widget/CardView.java:54`
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

## BR088

paper_id: B004
paper_title: Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation

- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzaei.java:112`
  `sparseArray.put(17057, new Pair<>("ERROR_WEB_CONTEXT_ALREADY_PRESENTED", "A headful operation is already in progress. Please wait for that to finish."));`
- `sources/com/google/firebase/firestore/util/AsyncQueue.java:76`
  `ScheduledFuture scheduledFuture = this.scheduledFuture;`
- `sources/com/google/firebase/firestore/util/AsyncQueue.java:77`
  `if (scheduledFuture != null) {`
- `sources/com/google/firebase/firestore/util/AsyncQueue.java:78`
  `scheduledFuture.cancel(false);`
- `sources/com/google/firebase/firestore/util/AsyncQueue.java:86`
  `if (this.scheduledFuture != null) {`
- `sources/com/google/firebase/firestore/util/AsyncQueue.java:93`
  `Assert.hardAssert(this.scheduledFuture != null, "Caller should have verified scheduledFuture is non-null.", new Object[0]);`
- `sources/com/google/firebase/firestore/util/AsyncQueue.java:94`
  `this.scheduledFuture = null;`
- `sources/com/lifesense/ble/b/a.java:112`
  `public static final UUID DEVICEINFO_SERVICE_FIRMWARE_REVISION_CHARACTERISTIC_UUID = UUID.fromString("00002a26-0000-1000-8000-00805f9b34fb");`
- `sources/com/lifesense/ble/b/d/c.java:60`
  `WRITE_START_DFU_COMMAND,`
- `sources/com/lifesense/ble/b/d/c.java:61`
  `WRITE_INIT_DFU_COMMAND,`
- `sources/com/lifesense/ble/b/d/c.java:63`
  `WRITE_RECEIVE_FIRMWARE_IMAGE_COMMAND,`
- `sources/com/lifesense/ble/b/d/c.java:64`
  `WRITE_VALIDATE_FIRMWARE_COMMAND,`
- `sources/com/lifesense/ble/bean/LsDeviceInfo.java:89`
  `this.firmwareVersion = parcel.readString();`
- `sources/com/lifesense/ble/bean/LsDeviceInfo.java:436`
  `parcel.writeString(this.firmwareVersion);`
- `sources/com/lifesense/ble/d/a.java:91`
  `return "A5OtaFile{fileData=" + Arrays.toString(this.f1101a) + ", fileCrc=" + Arrays.toString(this.f1102b) + ", framesNumber=" + this.f1103c + ", fileSize=" + this.f1104d + ", deviceModel='" + this.f1105e + "', fileName='" + this.f + "', firmwareVersion='" + this.g + "', fileHeader=" + Arrays.toStrin...`
- `sources/com/viwave/rossmaxconnect/BuildConfig.java:6`
  `public static final String API_URL = "https://us-central1-viwave-stork.cloudfunctions.net";`
- `sources/com/viwave/rossmaxconnect/BuildConfig.java:8`
  `public static final String BASE_URL = "https://us-central1-rossmax-care.cloudfunctions.net";`
- `sources/com/viwave/rossmaxconnect/datastore/DataManager.java:61`
  `private static final String BASE_URL = "https://us-central1-rossmax-care.cloudfunctions.net";`
- `sources/com/viwave/rossmaxconnect/datastore/DataManager.java:141`
  `final String str = "https://us-central1-rossmax-care.cloudfunctions.net/cleanUserMeasurements?access_token=" + getTokenResult.getToken();`
- `sources/com/viwave/rossmaxconnect/datastore/DataManager.java:387`
  `HttpUrl.Builder builderNewBuilder = HttpUrl.INSTANCE.get("https://us-central1-rossmax-care.cloudfunctions.net/friendzLastMeasurements").newBuilder();`
- `sources/com/viwave/rossmaxconnect/datastore/DataManager.java:486`
  `StringBuilder sb = new StringBuilder("https://us-central1-rossmax-care.cloudfunctions.net/userRegion/");`
- `sources/com/viwave/rossmaxconnect/datastore/DataManager.java:538`
  `HttpUrl.Builder builderNewBuilder = HttpUrl.INSTANCE.get("https://us-central1-rossmax-care.cloudfunctions.net/userRegion").newBuilder();`
- `sources/com/viwave/rossmaxconnect/func/FunctionHelper.java:35`
  `StringBuilder sb = new StringBuilder("https://us-central1-rossmax-care.cloudfunctions.net/measurementsExportCsv");`
- `sources/com/viwave/rossmaxconnect/func/api/ApiClearAllBabyWeights.java:22`
  `StringBuilder sb = new StringBuilder("https://us-central1-rossmax-care.cloudfunctions.net/babyService/measurements/");`
- `sources/com/viwave/rossmaxconnect/func/api/ApiDeleteBaby.java:23`
  `StringBuilder sb = new StringBuilder("https://us-central1-rossmax-care.cloudfunctions.net/babyService/baby/");`
- `sources/com/viwave/rossmaxconnect/okhttp/ViOkHttpMgr.java:89`
  `HttpUrl.Builder builderNewBuilder = HttpUrl.INSTANCE.get("https://us-central1-viwave-stork.cloudfunctions.netappVersion").newBuilder();`
- `sources/io/grpc/util/AdvancedTlsX509TrustManager.java:179`
  `final ScheduledFuture<?> scheduledFutureScheduleWithFixedDelay = scheduledExecutorService.scheduleWithFixedDelay(new LoadFilePathExecution(file), j, j, timeUnit);`
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

## BR090

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `rossmax_audit_report_zh.md:5`
  `这些问题或风险不是本次数据库中的漏洞类型，因此不作为 'confirmed'/'supported_hypothesis' 的规则结论输出，仅供后续工程排查。`
- `rossmax_audit_report_zh.md:23`
  `## 2. Method and Available Evidence`
- `rossmax_audit_report_zh.md:38`
  `## 3. Confirmed Findings`
- `rossmax_audit_report_zh.md:42`
  `结论：'confirmed'`
- `rossmax_audit_report_zh.md:55`
  `结论：'confirmed'`
- `rossmax_audit_report_zh.md:223`
  `当前只支持“健康 App 嵌入第三方统计/社交 SDK”这一部分；没有发现 malware-like 行为证据。该规则不升级为 confirmed。`
- `rossmax_audit_report_zh.md:352`
  `- 所有 BLE confirmed：R073-R084 若要 confirmed，至少需要真实设备、BLE 抓包、同机恶意 App 或可复现实验脚本。`
- `rossmax_audit_report_zh.md:364`
  `1. 运行 release APK，抓 'adb logcat'：覆盖 Google/Facebook/Email/Phone 登录、删除账号、清除测量、region 设置，验证 R050 是否从 'supported_hypothesis' 升为 'confirmed'。`
- `rossmax_evidence_chains_zh.md:1`
  `# Rossmax evidence chains`
- `rossmax_rule_mapping_zh.md:3`
  `结论值只使用：'confirmed'、'supported_hypothesis'、'not_supported'、'not_testable'。`
- `rossmax_rule_mapping_zh.md:11`
  `| R005 | P002 | SUPOR: Precise and Scalable Sensitive User Input Detection for Android Apps | 'confirmed' | 登录面处理 email/password、phone auth、Google/Facebook token；证据 'LoginPage.java:807,844-850,913-977,1052-1061'。 |`
- `rossmax_rule_mapping_zh.md:12`
  `| R006 | P002 | SUPOR: Precise and Scalable Sensitive User Input Detection for Android Apps | 'confirmed' | 血压/血糖/SpO2/体温/体重健康模型和 BLE 回调明确存在；证据 'Vital.java:245-262'、'VUBleManager.java:170-202'。 |`

## BR091

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/com/viwave/rossmaxconnect/api/ApiInterface.java:17`
  `@DELETE("/deleteUser")`
- `sources/com/viwave/rossmaxconnect/api/ApiInterface.java:20`
  `@GET("/thirdPartyServiceInfoHandler")`

## BR092

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/androidx/activity/ComponentActivity.java:503`
  `if (!TextUtils.equals(e2.getMessage(), "Can not perform this action after onSaveInstanceState")) {`
- `sources/androidx/appcompat/R.java:1558`
  `public static int[] SearchView = {android.R.attr.textAppearance, android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.text, android.R.attr.hint, android.R.attr.inputType, android.R.attr.imeOptions, com.viwave.RossmaxConnect.R.attr.animateMenuItems, com.viwave.RossmaxConnect.R.attr.anima...`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2612`
  `return Api21Impl.isPowerSaveMode(this.mPowerManager) ? 2 : 1;`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2745`
  `static boolean isPowerSaveMode(PowerManager powerManager) {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2746`
  `return powerManager.isPowerSaveMode();`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:196`
  `canvas.save();`
- `sources/androidx/appcompat/widget/ActionMenuPresenter.java:493`
  `public Parcelable onSaveInstanceState() {`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:177`
  `synchronized (this.mInstanceLock) {`
- `sources/androidx/appcompat/widget/AppCompatRatingBar.java:31`
  `protected synchronized void onMeasure(int i, int i2) {`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:138`
  `int iSave = canvas.save();`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:144`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:32`
  `private boolean mAsyncFontPending;`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:233`
  `AppCompatTextHelper.this.onAsyncTypefaceReceived(weakReference, typeface);`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:243`
  `this.mAsyncFontPending = this.mFontTypeface == null;`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:94`
  `ViewCompat.saveAttributeDataForStyleable(textView, textView.getContext(), R.styleable.AppCompatTextView, attributeSet, typedArrayObtainStyledAttributes, i, 0);`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:297`
  `synchronized (rectF) {`
- `sources/androidx/appcompat/widget/SearchView.java:93`
  `private final View mSubmitArea;`
- `sources/androidx/appcompat/widget/SearchView.java:94`
  `private boolean mSubmitButtonEnabled;`
- `sources/androidx/appcompat/widget/SwitchCompat.java:970`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:38`
  `private static class FileCleanupTask extends AsyncTask<Void, Void, Void> {`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:34`
  `int iSave = canvas.save();`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:193`
  `int iSave = canvas.save();`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:211`
  `int iSave3 = canvas2.save();`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:218`
  `canvas2.restoreToCount(iSave3);`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:219`
  `int iSave4 = canvas2.save();`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:226`
  `canvas2.restoreToCount(iSave4);`
- `sources/androidx/constraintlayout/core/motion/utils/TypedValues.java:637`
  `/* JADX WARN: Failed to restore switch over string. Please report as a decompilation issue */`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:1280`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:39:0x0086 -> B:40:0x0087). Please report as a decompilation issue!!! */`
- `sources/androidx/constraintlayout/core/widgets/Flow.java:1094`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:105:0x010d -> B:42:0x0059). Please report as a decompilation issue!!! */`
- `sources/androidx/constraintlayout/core/widgets/Flow.java:1095`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:106:0x010f -> B:42:0x0059). Please report as a decompilation issue!!! */`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:1910`
  `canvas.save();`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:125`
  `sRectPool = new Pools.SynchronizedPool(12);`
- `sources/androidx/core/content/pm/ShortcutManagerCompat.java:150`
  `public static void reportShortcutUsed(Context context, String str) {`
- `sources/androidx/core/content/res/FontResourcesParserCompat.java:21`
  `public static final int FETCH_STRATEGY_ASYNC = 1;`
- `sources/androidx/core/content/res/ResourcesCompat.java:29`
  `synchronized (sColorStateCacheLock) {`
- `sources/androidx/core/graphics/WeightTypefaceApi14.java:42`
  `synchronized (sWeightCacheLock) {`
- `sources/androidx/core/graphics/WeightTypefaceApi21.java:63`
  `synchronized (sWeightCacheLock) {`
- `sources/androidx/core/graphics/WeightTypefaceApi26.java:55`
  `synchronized (sWeightCacheLock) {`
- `sources/androidx/core/location/LocationManagerCompat.java:108`
  `synchronized (sLocationListeners) {`
- `sources/androidx/core/location/LocationManagerCompat.java:137`
  `synchronized (weakHashMap) {`

## BR093

paper_id: B004
paper_title: Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation

- `sources/androidx/navigation/NavBackStackEntry.java:19`
  `import androidx.savedstate.SavedStateRegistryOwner;`
- `sources/androidx/navigation/NavBackStackEntry.java:132`
  `@Metadata(d1 = {"\u0000<\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u...`
- `sources/androidx/navigation/NavBackStackEntry.java:164`
  `return new NavBackStackEntry(context, destination, arguments, hostLifecycleState, viewModelStoreProvider, id, savedState, null);`
- `sources/androidx/navigation/NavInflater.java:281`
  `builder.setPopUpTo(typedArrayObtainStyledAttributes.getResourceId(androidx.navigation.common.R.styleable.NavAction_popUpTo, -1), typedArrayObtainStyledAttributes.getBoolean(androidx.navigation.common.R.styleable.NavAction_popUpToInclusive, false), typedArrayObtainStyledAttributes.getBoolean(androidx...`
- `sources/androidx/navigation/common/R.java:53`
  `public static int[] NavAction = {android.R.attr.id, com.viwave.RossmaxConnect.R.attr.destination, com.viwave.RossmaxConnect.R.attr.enterAnim, com.viwave.RossmaxConnect.R.attr.exitAnim, com.viwave.RossmaxConnect.R.attr.launchSingleTop, com.viwave.RossmaxConnect.R.attr.popEnterAnim, com.viwave.Rossmax...`
- `sources/c/i.java:101`
  `this.k.postDelayed(this.m, 2000L);`
- `sources/c/m.java:58`
  `new Handler(Looper.getMainLooper()).postDelayed(new a(), 100L);`
- `sources/com/facebook/appevents/AppEventsLoggerImpl.java:957`
  `FacebookSdk.publishInstallAsync(application, applicationId);`
- `sources/com/facebook/appevents/internal/SessionInfo.java:167`
  `public final void clearSavedSessionFromDisk() {`
- `sources/com/facebook/internal/AppCall.java:29`
  `public static final synchronized AppCall finishPendingCall(UUID uuid, int i) {`
- `sources/com/facebook/internal/AppCall.java:164`
  `public final synchronized AppCall finishPendingCall(UUID callId, int requestCode) {`
- `sources/com/facebook/internal/NativeProtocol.java:39`
  `@Metadata(d1 = {"\u0000 \u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b;\n\u0002\u0010\u0011\n\u0002\u0010\b\n\u0002\b;\n\u0002\u0010$\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\b\u00...`
- `sources/com/facebook/login/DeviceAuthDialog.java:66`
  `@Metadata(d1 = {"\u0000¬\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b...`
- `sources/com/facebook/login/DeviceAuthDialog.java:178`
  `GraphRequest.INSTANCE.newPostRequestWithBundle(null, DEVICE_LOGIN_ENDPOINT, bundle, new GraphRequest.Callback() { // from class: com.facebook.login.DeviceAuthDialog$$ExternalSyntheticLambda6`
- `sources/com/facebook/share/internal/ShareInternalUtility.java:58`
  `@Metadata(d1 = {"\u0000î\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u00...`
- `sources/com/facebook/share/internal/ShareInternalUtility.java:500`
  `return new GraphRequest(accessToken, MY_STAGING_RESOURCES, bundle, HttpMethod.POST, callback, null, 32, null);`
- `sources/com/google/android/gms/internal/measurement/zzch.java:77`
  `java.lang.String r0 = "UploadAlarm"`
- `sources/com/google/android/gms/measurement/internal/zzav.java:28`
  `static final String[] zza = {"associated_row_id", "ALTER TABLE upload_queue ADD COLUMN associated_row_id INTEGER;", "last_upload_timestamp", "ALTER TABLE upload_queue ADD COLUMN last_upload_timestamp INTEGER;"};`
- `sources/com/google/android/gms/measurement/internal/zzav.java:30`
  `private static final String[] zzd = {"app_version", "ALTER TABLE apps ADD COLUMN app_version TEXT;", "app_store", "ALTER TABLE apps ADD COLUMN app_store TEXT;", "gmp_version", "ALTER TABLE apps ADD COLUMN gmp_version INTEGER;", "dev_cert_hash", "ALTER TABLE apps ADD COLUMN dev_cert_hash INTEGER;", "...`
- `sources/com/google/android/gms/measurement/internal/zzav.java:1806`
  `contentValues.put("adid_reporting_enabled", Boolean.valueOf(zzhVar.zzac()));`
- `sources/com/google/android/gms/measurement/internal/zzfx.java:227`
  `zzaN = zza("measurement.sgtm.client.upload_on_backgrounded.dev", false, false, zzfc.zza, true);`
- `sources/com/google/android/recaptcha/internal/zzcv.java:12`
  `import kotlinx.coroutines.sync.Mutex;`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsController.java:138`
  `CrashlyticsController.this.reportingCoordinator.persistFatalEvent(th, thread, currentSessionId, timestampSeconds);`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsController.java:145`
  `return settingsProvider.getSettingsAsync().onSuccessTask(CrashlyticsController.this.crashlyticsWorkers.common, new SuccessContinuation<Settings, Void>() { // from class: com.google.firebase.crashlytics.internal.common.CrashlyticsController.2.1`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsCore.java:209`
  `this.crashlyticsWorkers.common.submit(new Runnable() { // from class: com.google.firebase.crashlytics.internal.common.CrashlyticsCore$$ExternalSyntheticLambda5`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsReportDataCapture.java:87`
  `return CrashlyticsReport.ApplicationExitInfo.builder().setImportance(applicationExitInfo.getImportance()).setProcessName(applicationExitInfo.getProcessName()).setReasonCode(applicationExitInfo.getReasonCode()).setTimestamp(applicationExitInfo.getTimestamp()).setPid(applicationExitInfo.getPid()).setP...`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsReportDataCapture.java:90`
  `private CrashlyticsReport.Builder buildReportData() {`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsReportDataCapture.java:91`
  `return CrashlyticsReport.builder().setSdkVersion(BuildConfig.VERSION_NAME).setGmpAppId(this.appData.googleAppId).setInstallationUuid(this.idManager.getInstallIds().getCrashlyticsInstallId()).setFirebaseInstallationId(this.idManager.getInstallIds().getFirebaseInstallationId()).setFirebaseAuthenticati...`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsReportDataCapture.java:94`
  `private CrashlyticsReport.Session populateSessionData(String str, long j) {`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsReportDataCapture.java:95`
  `return CrashlyticsReport.Session.builder().setStartedAt(j).setIdentifier(str).setGenerator(GENERATOR).setApp(populateSessionApplicationData()).setOs(populateSessionOperatingSystemData()).setDevice(populateSessionDeviceData()).setGeneratorType(3).build();`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsReportDataCapture.java:98`
  `private CrashlyticsReport.Session.Application populateSessionApplicationData() {`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsReportDataCapture.java:99`
  `return CrashlyticsReport.Session.Application.builder().setIdentifier(this.idManager.getAppIdentifier()).setVersion(this.appData.versionCode).setDisplayVersion(this.appData.versionName).setInstallationUuid(this.idManager.getInstallIds().getCrashlyticsInstallId()).setDevelopmentPlatform(this.appData.d...`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsReportDataCapture.java:102`
  `private CrashlyticsReport.Session.OperatingSystem populateSessionOperatingSystemData() {`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsReportDataCapture.java:103`
  `return CrashlyticsReport.Session.OperatingSystem.builder().setPlatform(3).setVersion(Build.VERSION.RELEASE).setBuildVersion(Build.VERSION.CODENAME).setJailbroken(CommonUtils.isRooted()).build();`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsReportDataCapture.java:215`
  `private List<CrashlyticsReport.Session.Event.Application.Execution.BinaryImage> populateBinaryImagesList() {`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsReportDataCapture.java:219`
  `private CrashlyticsReport.Session.Event.Application.Execution.BinaryImage populateBinaryImageData() {`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsReportDataCapture.java:220`
  `return CrashlyticsReport.Session.Event.Application.Execution.BinaryImage.builder().setBaseAddress(0L).setSize(0L).setName(this.appData.packageName).setUuid(this.appData.buildId).build();`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsReportDataCapture.java:223`
  `private CrashlyticsReport.Session.Event.Application.Execution.Signal populateSignalData() {`
- `sources/com/google/firebase/crashlytics/internal/common/CrashlyticsReportDataCapture.java:224`
  `return CrashlyticsReport.Session.Event.Application.Execution.Signal.builder().setName("0").setCode("0").setAddress(0L).build();`
- `sources/com/google/firebase/crashlytics/internal/common/IdManager.java:125`
  `private synchronized String createAndCacheCrashlyticsInstallId(String str, SharedPreferences sharedPreferences) {`

## BR094

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `sources/android/support/customtabs/ICustomTabsCallback.java:38`
  `public void onPostMessage(String str, Bundle bundle) throws RemoteException {`
- `sources/android/support/customtabs/ICustomTabsCallback.java:54`
  `void onPostMessage(String str, Bundle bundle) throws RemoteException;`
- `sources/android/support/customtabs/ICustomTabsCallback.java:64`
  `static final int TRANSACTION_onPostMessage = 5;`
- `sources/android/support/customtabs/ICustomTabsCallback.java:111`
  `onPostMessage(parcel.readString(), parcel.readInt() != 0 ? (Bundle) Bundle.CREATOR.createFromParcel(parcel) : null);`
- `sources/android/support/customtabs/ICustomTabsService.java:92`
  `boolean requestPostMessageChannelWithExtras(ICustomTabsCallback iCustomTabsCallback, Uri uri, Bundle bundle) throws RemoteException;`
- `sources/android/support/customtabs/ICustomTabsService.java:106`
  `static final int TRANSACTION_postMessage = 8;`
- `sources/android/support/customtabs/ICustomTabsService.java:108`
  `static final int TRANSACTION_requestPostMessageChannel = 7;`
- `sources/android/support/customtabs/ICustomTabsService.java:109`
  `static final int TRANSACTION_requestPostMessageChannelWithExtras = 11;`
- `sources/android/support/customtabs/ICustomTabsService.java:186`
  `parcel2.writeInt(iPostMessage);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1642`
  `synchronized (MediaSessionImplBase.this.mLock) {`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1721`
  `postToHandler(10, uri, bundle);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1726`
  `postToHandler(11, Long.valueOf(j));`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1731`
  `postToHandler(12);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1756`
  `postToHandler(17);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1761`
  `postToHandler(18, Long.valueOf(j));`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1766`
  `postToHandler(19, ratingCompat);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:2140`
  `MediaSessionImplApi18.this.postToHandler(18, -1, -1, Long.valueOf(j), null);`
- `sources/androidx/activity/ComponentActivity.java:787`
  `class ReportFullyDrawnExecutorApi16Impl implements ReportFullyDrawnExecutor, ViewTreeObserver.OnDrawListener, Runnable {`
- `sources/androidx/activity/ComponentActivity.java:792`
  `ReportFullyDrawnExecutorApi16Impl() {`
- `sources/androidx/activity/result/ActivityResultRegistry.java:162`
  `public final void onSaveInstanceState(Bundle bundle) {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:128`
  `boolean mInvalidatePanelMenuPosted;`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:309`
  `syncRequestedAndStoredLocales(context);`
- `sources/androidx/appcompat/app/AppCompatViewInflater.java:53`
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
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:67`
  `public static synchronized ResourceManagerInternal get() {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:76`
  `public synchronized void setHooks(ResourceManagerHooks resourceManagerHooks) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:103`
  `public synchronized void onConfigurationChanged(Context context) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:211`
  `private synchronized Drawable getCachedDrawable(Context context, long j) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:227`
  `private synchronized boolean addDrawableToCache(Context context, long j, Drawable drawable) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:241`
  `synchronized Drawable onDrawableLoadedFromResources(Context context, VectorEnabledTintResources vectorEnabledTintResources, int i) {`
- `sources/androidx/appcompat/widget/SearchView.java:93`
  `private final View mSubmitArea;`
- `sources/androidx/appcompat/widget/SearchView.java:263`
  `ViewCompat.saveAttributeDataForStyleable(this, context, androidx.appcompat.R.styleable.SearchView, attributeSet, tintTypedArrayObtainStyledAttributes.getWrappedTypeArray(), i, 0);`
- `sources/androidx/appcompat/widget/SearchView.java:271`
  `View viewFindViewById2 = findViewById(androidx.appcompat.R.id.submit_area);`
- `sources/androidx/appcompat/widget/SearchView.java:272`
  `this.mSubmitArea = viewFindViewById2;`

## BR095

paper_id: B025
paper_title: Why Eve and Mallory Still Love Android: Revisiting TLS (In)Security in Android Applications

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
- `resources/res/drawable/btn_create_account.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/btn_health_blood_pressure_save.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/btn_ic_device_next_arrow.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android" android:autoMirrored="true">`
- `resources/res/drawable/btn_ic_male_overweight.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/btn_ic_male_underweight.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/btn_ic_profile_edit_button.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android" android:autoMirrored="true">`
- `resources/res/drawable/btn_ic_vital_blood_pressure.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/btn_ic_vital_spo2.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/btn_ic_vital_temperature.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/btn_ic_vital_weight.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/btn_radio_off_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/btn_radio_on_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ccp_ic_arrow_drop_down.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/com_facebook_button_icon.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/com_facebook_favicon_blue.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/design_ic_visibility.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/design_ic_visibility_off.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/guide_baby_measurement_step1.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/guide_baby_measurement_step2.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_add.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_add_manually.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/res/drawable/ic_add_measurement.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_add_pressed.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_afib_off.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_afib_on.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_apple1.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_apple2.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/res/drawable/ic_apple3.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/res/drawable/ic_arrow_back_black_24.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_arrow_down_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_arrow_next.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_arrow_next_pressed.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_arrow_previous.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_arrow_previous_pressed.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_arr_off.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_arr_on.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_baby_record.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_baby_record_pressed.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_backspace_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_back_enable.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_back_pressed.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_bg.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_bp_afib.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_bp_afib_on.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_bp_arr.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_bp_arr_on.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_bp_basic.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_bp_brad.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_bp_brad_on.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_bp_dumbbell.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_bp_ear.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_bp_filter_disable.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_bp_filter_pressed.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_bp_filter_used.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_bp_filter_used_pressed.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_bp_ihb.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_bp_ihb_on.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_bp_pc.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`

## BR096

paper_id: B011
paper_title: Locking it down: The privacy and security of mobile medication apps

- `resources/res/color/design_box_stroke_color.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/ic_login_facebook.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/_mtrl_switch_thumb_checked_unchecked__1_res_0x7f08003e.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/res/drawable/_mtrl_switch_thumb_unchecked_checked__0_res_0x7f080041.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/res/drawable/_mtrl_switch_thumb_unchecked_checked__1_res_0x7f080042.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/res/layout/design_text_input_end_icon.xml:2`
  `<com.google.android.material.internal.CheckableImageButton xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/design_text_input_start_icon.xml:2`
  `<com.google.android.material.internal.CheckableImageButton xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/login_new_multi_part.xml:2`
  `<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto"`
- `resources/res/layout/login_new_page.xml:2`
  `<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto"`
- `resources/res/layout/material_chip_input_combo.xml:2`
  `<com.google.android.material.timepicker.ChipTextInputComboView xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/material_time_input.xml:2`
  `<com.google.android.material.textfield.TextInputLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto"`
- `resources/res/layout/mtrl_picker_text_input_date.xml:2`
  `<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/view_login_title_subtitle.xml:2`
  `<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/menu/health_new.xml:2`
  `<menu xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto">`
- `resources/res/raw/firebase_common_keep.xml:2`
  `<resources xmlns:tools="http://schemas.android.com/tools"`
- `resources/res/values/strings.xml:340`
  `<string name="firebase_database_url">https://rossmax-care.firebaseio.com</string>`
- `sources/androidx/datastore/core/DataStoreImpl.java:50`
  `private static final String BUG_MESSAGE = "This is a bug in DataStore. Please file a bug at: https://issuetracker.google.com/issues/new?component=907884&template=1466542";`
- `sources/com/facebook/GraphRequest.java:1316`
  `Log.w(TAG, "Starting with v13 of the SDK, a client token must be embedded in your client code before making Graph API calls. Visit https://developers.facebook.com/docs/android/getting-started#client-token to learn how to implement this change.");`
- `sources/com/facebook/UserSettingsManager.java:29`
  `private static final String ADVERTISERID_COLLECTION_NOT_SET_WARNING = "You haven't set a value for AdvertiserIDCollectionEnabled. Set the flag to TRUE if you want to collect Advertiser ID for better advertising and analytics results. To request user consent before collecting data, set the flag value...`
- `sources/com/facebook/internal/NativeProtocol.java:1088`
  `Log.w(NativeProtocol.access$getTAG$p(), "Apps that target Android API 30+ (Android 11+) cannot call Facebook native apps unless the package visibility needs are declared. Please follow https://developers.facebook.com/docs/android/troubleshooting/#faq_267321845055988 to make the declaration.");`
- `sources/com/google/android/gms/common/FirstPartyScopes.java:6`
  `public static final String GAMES_1P = "https://www.googleapis.com/auth/games.firstparty";`
- `sources/com/google/android/gms/common/Scopes.java:6`
  `public static final String APP_STATE = "https://www.googleapis.com/auth/appstate";`
- `sources/com/google/android/gms/common/Scopes.java:7`
  `public static final String CLOUD_SAVE = "https://www.googleapis.com/auth/datastoremobile";`
- `sources/com/google/android/gms/common/Scopes.java:8`
  `public static final String DRIVE_APPFOLDER = "https://www.googleapis.com/auth/drive.appdata";`
- `sources/com/google/android/gms/common/Scopes.java:9`
  `public static final String DRIVE_APPS = "https://www.googleapis.com/auth/drive.apps";`
- `sources/com/google/android/gms/common/Scopes.java:10`
  `public static final String DRIVE_FILE = "https://www.googleapis.com/auth/drive.file";`
- `sources/com/google/android/gms/common/Scopes.java:11`
  `public static final String DRIVE_FULL = "https://www.googleapis.com/auth/drive";`
- `sources/com/google/android/gms/common/Scopes.java:13`
  `public static final String GAMES = "https://www.googleapis.com/auth/games";`
- `sources/com/google/android/gms/common/Scopes.java:14`
  `public static final String GAMES_LITE = "https://www.googleapis.com/auth/games_lite";`
- `sources/com/google/android/gms/common/Scopes.java:15`
  `public static final String LEGACY_USERINFO_EMAIL = "https://www.googleapis.com/auth/userinfo.email";`
- `sources/com/google/android/gms/common/Scopes.java:16`
  `public static final String LEGACY_USERINFO_PROFILE = "https://www.googleapis.com/auth/userinfo.profile";`
- `sources/com/google/android/gms/common/Scopes.java:20`
  `public static final String PLUS_LOGIN = "https://www.googleapis.com/auth/plus.login";`
- `sources/com/google/android/gms/common/Scopes.java:21`
  `public static final String PLUS_ME = "https://www.googleapis.com/auth/plus.me";`
- `sources/com/google/android/gms/internal/measurement/zzpa.java:103`
  `zzn = zzkfVarZzb.zzf("measurement.sgtm.google_signal.url", "https://app-measurement.com/s/d");`
- `sources/com/google/android/gms/internal/measurement/zzpa.java:166`
  `zzau = zzkfVarZzb.zzf("measurement.upload.url", "https://app-measurement.com/a");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zznt.java:28`
  `throw new GeneralSecurityException("No key manager found for key type " + str + ", see https://developers.google.com/tink/faq/registration_errors");`
- `sources/com/google/android/gms/measurement/internal/zzfx.java:147`
  `zzq = zza("measurement.upload.url", "https://app-measurement.com/a", "https://app-measurement.com/a", zzca.zza, false);`
- `sources/com/google/android/gms/measurement/internal/zzfx.java:148`
  `zzr = zza("measurement.sgtm.google_signal.url", "https://app-measurement.com/s/d", "https://app-measurement.com/s/d", zzcb.zza, false);`
- `sources/com/google/android/gms/measurement/internal/zzkw.java:43`
  `bundleZzi = zzpoVarZzk.zzi(Uri.parse("https://google.com/search?".concat(String.valueOf(str))));`
- `sources/com/google/android/recaptcha/internal/zzbr.java:12`
  `this("https://www.recaptcha.net/recaptcha/api3");`
- `sources/com/google/android/recaptcha/internal/zzbr.java:16`
  `this.zza = "https://www.recaptcha.net/recaptcha/api3";`
- `sources/com/google/android/recaptcha/internal/zzbr.java:17`
  `this.zzb = "https://www.recaptcha.net/recaptcha/api3".concat("/mri");`
- `sources/com/google/android/recaptcha/internal/zzbr.java:18`
  `this.zzc = "https://www.recaptcha.net/recaptcha/api3".concat("/mlg");`
- `sources/com/google/android/recaptcha/internal/zzbr.java:19`
  `this.zzd = "https://www.recaptcha.net/recaptcha/api3".concat("/mrr");`
- `sources/com/google/android/recaptcha/internal/zzcv.java:31`
  `zzaw[] zzawVarArr = {new zzaw("com.google.android.recaptcha.internal.zzaz".hashCode(), new zzaz(null, 1, null)), new zzaw("com.google.android.recaptcha.internal.zzfu".hashCode(), new zzfu()), new zzaw("com.google.android.recaptcha.internal.zzbe".hashCode(), new zzbe()), new zzaw("com.google.android....`
- `sources/com/google/firebase/analytics/ktx/AnalyticsKt.java:47`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.")`
- `sources/com/google/firebase/analytics/ktx/AnalyticsKt.java:57`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.")`
- `sources/com/google/firebase/analytics/ktx/ConsentBuilder.java:12`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.")`
- `sources/com/google/firebase/analytics/ktx/ParametersBuilder.java:11`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.")`
- `sources/com/google/firebase/analytics/ktx/ParametersBuilder.java:21`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.")`
- `sources/com/google/firebase/analytics/ktx/ParametersBuilder.java:27`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.")`
- `sources/com/google/firebase/analytics/ktx/ParametersBuilder.java:33`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.")`
- `sources/com/google/firebase/analytics/ktx/ParametersBuilder.java:40`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.")`
- `sources/com/google/firebase/analytics/ktx/ParametersBuilder.java:47`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.")`
- `sources/com/google/firebase/auth/ktx/AuthKt.java:21`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.")`
- `sources/com/google/firebase/auth/ktx/AuthKt.java:32`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.")`
- `sources/com/google/firebase/auth/ktx/AuthKt.java:59`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.")`
- `sources/com/google/firebase/auth/ktx/AuthKt.java:71`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.")`
- `sources/com/google/firebase/auth/ktx/AuthKt.java:84`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.")`
- `sources/com/google/firebase/crashlytics/ktx/FirebaseCrashlyticsKt.java:24`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.", replaceWith = @ReplaceWith(expression = "", imports = {}))`
- `sources/com/google/firebase/crashlytics/ktx/FirebaseCrashlyticsKtxRegistrar.java:14`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.", replaceWith = @ReplaceWith(expression = "", imports = {}))`
- `sources/com/google/firebase/firestore/ktx/FirebaseFirestoreKtxRegistrar.java:14`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.", replaceWith = @ReplaceWith(expression = "", imports = {}))`
- `sources/com/google/firebase/firestore/ktx/FirestoreKt.java:82`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.", replaceWith = @ReplaceWith(expression = "", imports = {}))`
- `sources/com/google/firebase/firestore/ktx/FirestoreKt.java:89`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.", replaceWith = @ReplaceWith(expression = "", imports = {}))`
- `sources/com/google/firebase/firestore/ktx/FirestoreKt.java:97`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.", replaceWith = @ReplaceWith(expression = "", imports = {}))`
- `sources/com/google/firebase/firestore/ktx/FirestoreKt.java:105`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.", replaceWith = @ReplaceWith(expression = "", imports = {}))`
- `sources/com/google/firebase/firestore/ktx/FirestoreKt.java:114`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.", replaceWith = @ReplaceWith(expression = "", imports = {}))`
- `sources/com/google/firebase/firestore/ktx/FirestoreKt.java:122`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.", replaceWith = @ReplaceWith(expression = "", imports = {}))`
- `sources/com/google/firebase/firestore/ktx/FirestoreKt.java:131`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.", replaceWith = @ReplaceWith(expression = "", imports = {}))`
- `sources/com/google/firebase/firestore/ktx/FirestoreKt.java:140`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.", replaceWith = @ReplaceWith(expression = "", imports = {}))`
- `sources/com/google/firebase/firestore/ktx/FirestoreKt.java:150`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.", replaceWith = @ReplaceWith(expression = "", imports = {}))`
- `sources/com/google/firebase/firestore/ktx/FirestoreKt.java:159`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.", replaceWith = @ReplaceWith(expression = "", imports = {}))`
- `sources/com/google/firebase/firestore/ktx/FirestoreKt.java:169`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.", replaceWith = @ReplaceWith(expression = "", imports = {}))`
- `sources/com/google/firebase/firestore/ktx/FirestoreKt.java:402`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.", replaceWith = @ReplaceWith(expression = "", imports = {}))`
- `sources/com/google/firebase/firestore/ktx/FirestoreKt.java:420`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.", replaceWith = @ReplaceWith(expression = "", imports = {}))`
- `sources/com/google/firebase/firestore/ktx/FirestoreKt.java:440`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.", replaceWith = @ReplaceWith(expression = "", imports = {}))`
- `sources/com/google/firebase/installations/FirebaseInstallations.java:35`
  `private static final String API_KEY_VALIDATION_MSG = "Please set a valid API key. A Firebase API key is required to communicate with Firebase server APIs: It authenticates your project with Google.Please refer to https://firebase.google.com/support/privacy/init-options.";`
- `sources/com/google/firebase/installations/FirebaseInstallations.java:36`
  `private static final String APP_ID_VALIDATION_MSG = "Please set your Application ID. A valid Firebase App ID is required to communicate with Firebase server APIs: It identifies your application with Firebase.Please refer to https://firebase.google.com/support/privacy/init-options.";`
- `sources/com/google/firebase/installations/FirebaseInstallations.java:43`
  `private static final String PROJECT_ID_VALIDATION_MSG = "Please set your Project ID. A valid Firebase Project ID is required to communicate with Firebase server APIs: It identifies your application with Firebase.Please refer to https://firebase.google.com/support/privacy/init-options.";`
- `sources/com/google/firebase/ktx/FirebaseCommonKtxRegistrar.java:26`
  `@Deprecated(message = "Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.", replaceWith = @ReplaceWith(expression = "", imports = {}))`

## BR098

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/com/viwave/rossmaxconnect/api/ApiInstance.java:67`
  `return new Retrofit.Builder().baseUrl(BuildConfig.BASE_URL).addConverterFactory(GsonConverterFactory.create()).addCallAdapterFactory(RxJava3CallAdapterFactory.create()).client(new OkHttpClient.Builder().addInterceptor(INSTANCE.getLogging()).build()).build();`
