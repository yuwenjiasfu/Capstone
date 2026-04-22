# Rule Search Hits

## BR001

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:28`
  `<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:29`
  `<uses-permission android:name="android.permission.RECORD_AUDIO"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:36`
  `<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:37`
  `<uses-permission android:name="android.permission.CAMERA"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:38`
  `<uses-permission android:name="android.permission.VIBRATE"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:64`
  `<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:65`
  `<uses-permission android:name="android.permission.READ_CALENDAR"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:66`
  `<uses-permission android:name="android.permission.WRITE_CALENDAR"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:67`
  `<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:97`
  `<uses-permission android:name="com.bupa.digitalprimarycare.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:98`
  `<uses-permission android:name="android.permission.READ_PHONE_STATE"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:99`
  `<uses-permission android:name="com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE"/>`

## BR002

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:34`
  `<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:35`
  `<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:36`
  `<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:37`
  `<uses-permission android:name="android.permission.CAMERA"/>`

## BR003

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:55`
  `<uses-permission`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:58`
  `<uses-permission`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:61`
  `<uses-permission android:name="android.permission.BLUETOOTH_SCAN"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:62`
  `<uses-permission android:name="android.permission.BLUETOOTH_CONNECT"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:63`
  `<uses-permission android:name="com.android.vending.CHECK_LICENSE"/>`

## BR004

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:47`
  `<uses-permission android:name="android.permission.FOREGROUND_SERVICE"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:48`
  `<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:49`
  `<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:50`
  `<uses-permission android:name="android.permission.DOWNLOAD_WITHOUT_NOTIFICATION"/>`

## BR005

paper_id: B021
paper_title: Metadata-Based Privacy Assessment for Mobile mHealth

- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:66`
  `<uses-permission android:name="android.permission.WRITE_CALENDAR"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:67`
  `<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>`

## BR006

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:125`
  `android:usesCleartextTraffic="true"`

## BR009

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/com/auth0/android/request/DefaultClient.java:14`
  `import javax.net.ssl.X509TrustManager;`
- `sources/com/auth0/android/request/DefaultClient.java:34`
  `@Metadata(d1 = {"\u0000Z\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0010$\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0...`
- `sources/com/auth0/android/request/DefaultClient.java:71`
  `public DefaultClient(int i2, int i3, @NotNull Map<String, String> defaultHeaders, boolean z2, @Nullable SSLSocketFactory sSLSocketFactory, @Nullable X509TrustManager x509TrustManager) {`
- `sources/com/auth0/android/request/DefaultClient.java:83`
  `if (sSLSocketFactory != null && x509TrustManager != null) {`
- `sources/com/auth0/android/request/DefaultClient.java:84`
  `builder.sslSocketFactory(sSLSocketFactory, x509TrustManager);`
- `sources/com/auth0/android/request/DefaultClient.java:139`
  `this(i2, i3, defaultHeaders, z2, (SSLSocketFactory) null, (X509TrustManager) null);`
- `sources/com/onfido/api/client/OnfidoFetcher.java:24`
  `import javax.net.ssl.X509TrustManager;`
- `sources/com/onfido/api/client/OnfidoFetcher.java:86`
  `if (trustManager instanceof X509TrustManager) {`
- `sources/com/onfido/api/client/OnfidoFetcher.java:87`
  `builderNewBuilder.sslSocketFactory(new OnfidoTLSSocketFactory(), (X509TrustManager) trustManager);`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:15`
  `import javax.net.ssl.X509TrustManager;`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:49`
  `X509TrustManager x509TrustManager = new X509TrustManager() { // from class: com.RNFetchBlob.RNFetchBlobUtils.1`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:50`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:51`
  `public void checkClientTrusted(X509Certificate[] x509CertificateArr, String str) throws CertificateException {`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:54`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:55`
  `public void checkServerTrusted(X509Certificate[] x509CertificateArr, String str) throws CertificateException {`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:58`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:64`
  `sSLContext.init(null, new TrustManager[]{x509TrustManager}, new SecureRandom());`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:67`
  `builderNewBuilder.sslSocketFactory(socketFactory, x509TrustManager);`
- `sources/okhttp3/OkHttpClient.java:18`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/OkHttpClient.java:48`
  `@Metadata(d1 = {"\u0000î\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u001a\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u00...`
- `sources/okhttp3/OkHttpClient.java:121`
  `private final X509TrustManager x509TrustManager;`
- `sources/okhttp3/OkHttpClient.java:134`
  `@Metadata(d1 = {"\u0000ø\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0018...`
- `sources/okhttp3/OkHttpClient.java:207`
  `private X509TrustManager x509TrustManagerOrNull;`
- `sources/okhttp3/OkHttpClient.java:552`
  `/* JADX INFO: renamed from: getX509TrustManagerOrNull$okhttp, reason: from getter */`
- `sources/okhttp3/OkHttpClient.java:553`
  `public final X509TrustManager getX509TrustManagerOrNull() {`
- `sources/okhttp3/OkHttpClient.java:554`
  `return this.x509TrustManagerOrNull;`
- `sources/okhttp3/OkHttpClient.java:782`
  `public final void setX509TrustManagerOrNull$okhttp(@Nullable X509TrustManager x509TrustManager) {`
- `sources/okhttp3/OkHttpClient.java:783`
  `this.x509TrustManagerOrNull = x509TrustManager;`
- `sources/okhttp3/OkHttpClient.java:799`
  `@Deprecated(level = DeprecationLevel.ERROR, message = "Use the sslSocketFactory overload that accepts a X509TrustManager.")`
- `sources/okhttp3/OkHttpClient.java:808`
  `X509TrustManager x509TrustManagerTrustManager = companion.get().trustManager(sslSocketFactory);`
- `sources/okhttp3/OkHttpClient.java:809`
  `if (x509TrustManagerTrustManager != null) {`
- `sources/okhttp3/OkHttpClient.java:810`
  `setX509TrustManagerOrNull$okhttp(x509TrustManagerTrustManager);`
- `sources/okhttp3/OkHttpClient.java:812`
  `X509TrustManager x509TrustManagerOrNull = getX509TrustManagerOrNull();`
- `sources/okhttp3/OkHttpClient.java:813`
  `Intrinsics.checkNotNull(x509TrustManagerOrNull);`
- `sources/okhttp3/OkHttpClient.java:814`
  `setCertificateChainCleaner$okhttp(platform.buildCertificateChainCleaner(x509TrustManagerOrNull));`
- `sources/okhttp3/OkHttpClient.java:868`
  `public final Builder sslSocketFactory(@NotNull SSLSocketFactory sslSocketFactory, @NotNull X509TrustManager trustManager) {`
- `sources/okhttp3/OkHttpClient.java:871`
  `if (!Intrinsics.areEqual(sslSocketFactory, getSslSocketFactoryOrNull()) || !Intrinsics.areEqual(trustManager, getX509TrustManagerOrNull())) {`
- `sources/okhttp3/OkHttpClient.java:876`
  `setX509TrustManagerOrNull$okhttp(trustManager);`
- `sources/okhttp3/OkHttpClient.java:901`
  `this.x509TrustManagerOrNull = okHttpClient.getX509TrustManager();`
- `sources/okhttp3/OkHttpClient.java:993`
  `this.x509TrustManager = null;`
- `sources/okhttp3/OkHttpClient.java:1000`
  `X509TrustManager x509TrustManagerOrNull = builder.getX509TrustManagerOrNull();`
- `sources/okhttp3/OkHttpClient.java:1001`
  `Intrinsics.checkNotNull(x509TrustManagerOrNull);`
- `sources/okhttp3/OkHttpClient.java:1002`
  `this.x509TrustManager = x509TrustManagerOrNull;`
- `sources/okhttp3/OkHttpClient.java:1008`
  `X509TrustManager x509TrustManagerPlatformTrustManager = companion.get().platformTrustManager();`
- `sources/okhttp3/OkHttpClient.java:1009`
  `this.x509TrustManager = x509TrustManagerPlatformTrustManager;`
- `sources/okhttp3/OkHttpClient.java:1011`
  `Intrinsics.checkNotNull(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/OkHttpClient.java:1012`
  `this.sslSocketFactoryOrNull = platform.newSslSocketFactory(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/OkHttpClient.java:1014`
  `Intrinsics.checkNotNull(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/OkHttpClient.java:1015`
  `CertificateChainCleaner certificateChainCleaner2 = companion2.get(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/OkHttpClient.java:1052`
  `if (this.x509TrustManager == null) {`
- `sources/okhttp3/OkHttpClient.java:1053`
  `throw new IllegalStateException("x509TrustManager == null".toString());`
- `sources/okhttp3/OkHttpClient.java:1063`
  `if (!(this.x509TrustManager == null)) {`
- `sources/okhttp3/OkHttpClient.java:1468`
  `@JvmName(name = "x509TrustManager")`
- `sources/okhttp3/OkHttpClient.java:1470`
  `/* JADX INFO: renamed from: x509TrustManager, reason: from getter */`
- `sources/okhttp3/OkHttpClient.java:1471`
  `public final X509TrustManager getX509TrustManager() {`
- `sources/okhttp3/OkHttpClient.java:1472`
  `return this.x509TrustManager;`
- `sources/okhttp3/internal/platform/Android10Platform.java:11`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/platform/Android10Platform.java:32`
  `@Metadata(d1 = {"\u0000J\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\...`
- `sources/okhttp3/internal/platform/Android10Platform.java:83`
  `public CertificateChainCleaner buildCertificateChainCleaner(@NotNull X509TrustManager trustManager) {`
- `sources/okhttp3/internal/platform/Android10Platform.java:145`
  `public X509TrustManager trustManager(@NotNull SSLSocketFactory sslSocketFactory) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:18`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:41`
  `@Metadata(d1 = {"\u0000x\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\...`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:79`
  `@Metadata(d1 = {"\u00008\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u000e\n\u0000\b\u0080\b\u0018\u00...`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:86`
  `private final X509TrustManager trustManager;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:88`
  `public CustomTrustRootIndex(@NotNull X509TrustManager trustManager, @NotNull Method findByIssuerAndSignatureMethod) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:96`
  `private final X509TrustManager getTrustManager() {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:105`
  `public static /* synthetic */ CustomTrustRootIndex copy$default(CustomTrustRootIndex customTrustRootIndex, X509TrustManager x509TrustManager, Method method, int i2, Object obj) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:107`
  `x509TrustManager = customTrustRootIndex.trustManager;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:112`
  `return customTrustRootIndex.copy(x509TrustManager, method);`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:116`
  `public final CustomTrustRootIndex copy(@NotNull X509TrustManager trustManager, @NotNull Method findByIssuerAndSignatureMethod) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:182`
  `public CertificateChainCleaner buildCertificateChainCleaner(@NotNull X509TrustManager trustManager) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:190`
  `public TrustRootIndex buildTrustRootIndex(@NotNull X509TrustManager trustManager) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:294`
  `public X509TrustManager trustManager(@NotNull SSLSocketFactory sslSocketFactory) {`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:15`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:28`
  `@Metadata(d1 = {"\u0000J\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\...`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:125`
  `public X509TrustManager platformTrustManager() throws NoSuchAlgorithmException, KeyStoreException, NoSuchProviderException {`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:130`
  `if (!(trustManagers.length == 1 && (trustManagers[0] instanceof X509TrustManager))) {`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:137`
  `return (X509TrustManager) trustManager;`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:139`
  `throw new NullPointerException("null cannot be cast to non-null type javax.net.ssl.X509TrustManager");`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:144`
  `public X509TrustManager trustManager(@NotNull SSLSocketFactory sslSocketFactory) {`

## BR010

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:68`
  `builderNewBuilder.hostnameVerifier(new HostnameVerifier() { // from class: com.RNFetchBlob.RNFetchBlobUtils.2`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:69`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:70`
  `public boolean verify(String str, SSLSession sSLSession) {`
- `sources/okhttp3/internal/connection/RealConnection.java:518`
  `if (this.http2Connection == null || routes == null || !routeMatchesAny(routes) || address.hostnameVerifier() != OkHostnameVerifier.INSTANCE || !supportsUrl(address.url())) {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:85`
  `public static final DisabledHostnameVerifier INSTANCE = new DisabledHostnameVerifier();`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:87`
  `private DisabledHostnameVerifier() {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:90`
  `public final boolean verify(@Nullable String hostname, @Nullable SSLSession session) {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:94`
  `public boolean verify(@Nullable X509Certificate[] certs, @Nullable String hostname, @Nullable SSLSession session) {`
- `sources/okhttp3/internal/tls/BasicCertificateChainCleaner.java:35`
  `toVerify.verify(signingCert.getPublicKey());`

## BR011

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/com/auth0/android/authentication/storage/CryptoUtil.java:256`
  `} catch (CertificateException e9) {`
- `sources/com/microsoft/appcenter/http/HttpUtils.java:111`
  `return (th instanceof SSLException) && (message = th.getMessage()) != null && CONNECTION_ISSUE_PATTERN.matcher(message.toLowerCase(Locale.US)).find();`
- `sources/okhttp3/internal/connection/ConnectionSpecSelector.java:11`
  `import javax.net.ssl.SSLHandshakeException;`
- `sources/okhttp3/internal/connection/ConnectionSpecSelector.java:89`
  `return (!this.isFallbackPossible || (e2 instanceof ProtocolException) || (e2 instanceof InterruptedIOException) || ((e2 instanceof SSLHandshakeException) && (e2.getCause() instanceof CertificateException)) || (e2 instanceof SSLPeerUnverifiedException) || !(e2 instanceof SSLException)) ? false : true...`
- `sources/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:145`
  `return e2 instanceof InterruptedIOException ? (e2 instanceof SocketTimeoutException) && !requestSendStarted : (((e2 instanceof SSLHandshakeException) && (e2.getCause() instanceof CertificateException)) || (e2 instanceof SSLPeerUnverifiedException)) ? false : true;`

## BR012

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/com/onfido/api/client/OnfidoFetcher.java:25`
  `import okhttp3.CertificatePinner;`
- `sources/com/onfido/api/client/OnfidoFetcher.java:110`
  `CertificatePinner.Builder builder2 = new CertificatePinner.Builder();`
- `sources/com/onfido/api/client/OnfidoFetcher.java:114`
  `builder.certificatePinner(builder2.build());`
- `sources/okhttp3/Address.java:23`
  `@Metadata(d1 = {"\u0000h\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002...`
- `sources/okhttp3/Address.java:27`
  `private final CertificatePinner certificatePinner;`
- `sources/okhttp3/Address.java:59`
  `public Address(@NotNull String uriHost, int i2, @NotNull Dns dns, @NotNull SocketFactory socketFactory, @Nullable SSLSocketFactory sSLSocketFactory, @Nullable HostnameVerifier hostnameVerifier, @Nullable CertificatePinner certificatePinner, @NotNull Authenticator proxyAuthenticator, @Nullable Proxy ...`
- `sources/okhttp3/Address.java:71`
  `this.certificatePinner = certificatePinner;`
- `sources/okhttp3/Address.java:80`
  `@Deprecated(level = DeprecationLevel.ERROR, message = "moved to val", replaceWith = @ReplaceWith(expression = "certificatePinner", imports = {}))`
- `sources/okhttp3/Address.java:81`
  `@JvmName(name = "-deprecated_certificatePinner")`
- `sources/okhttp3/Address.java:83`
  `/* JADX INFO: renamed from: -deprecated_certificatePinner, reason: not valid java name and from getter */`
- `sources/okhttp3/Address.java:84`
  `public final CertificatePinner getCertificatePinner() {`
- `sources/okhttp3/Address.java:85`
  `return this.certificatePinner;`
- `sources/okhttp3/Address.java:168`
  `@JvmName(name = "certificatePinner")`
- `sources/okhttp3/Address.java:170`
  `public final CertificatePinner certificatePinner() {`
- `sources/okhttp3/Address.java:171`
  `return this.certificatePinner;`
- `sources/okhttp3/Address.java:198`
  `return Intrinsics.areEqual(this.dns, that.dns) && Intrinsics.areEqual(this.proxyAuthenticator, that.proxyAuthenticator) && Intrinsics.areEqual(this.protocols, that.protocols) && Intrinsics.areEqual(this.connectionSpecs, that.connectionSpecs) && Intrinsics.areEqual(this.proxySelector, that.proxySelec...`
- `sources/okhttp3/Address.java:202`
  `return ((((((((((((((((((527 + this.url.hashCode()) * 31) + this.dns.hashCode()) * 31) + this.proxyAuthenticator.hashCode()) * 31) + this.protocols.hashCode()) * 31) + this.connectionSpecs.hashCode()) * 31) + this.proxySelector.hashCode()) * 31) + Objects.hashCode(this.proxy)) * 31) + Objects.hashCo...`
- `sources/okhttp3/CertificatePinner.java:36`
  `/* JADX INFO: compiled from: CertificatePinner.kt */`
- `sources/okhttp3/CertificatePinner.java:38`
  `@Metadata(d1 = {"\u0000T\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\"\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0010\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u0011\...`
- `sources/okhttp3/CertificatePinner.java:39`
  `public final class CertificatePinner {`
- `sources/okhttp3/CertificatePinner.java:47`
  `public static final CertificatePinner DEFAULT = new Builder().build();`
- `sources/okhttp3/CertificatePinner.java:55`
  `/* JADX INFO: compiled from: CertificatePinner.kt */`
- `sources/okhttp3/CertificatePinner.java:56`
  `@Metadata(d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010!\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010\u000e\n\u0002\u0010\u0011\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\u0018\u00002\u00020\u0001B\u0005¢\u0006\u0002\u0010\u0002J'\u0010\b\u001a\u00020\u00...`
- `sources/okhttp3/CertificatePinner.java:77`
  `public final CertificatePinner build() {`
- `sources/okhttp3/CertificatePinner.java:78`
  `return new CertificatePinner(CollectionsKt___CollectionsKt.toSet(this.pins), null, 2, 0 == true ? 1 : 0);`
- `sources/okhttp3/CertificatePinner.java:87`
  `/* JADX INFO: compiled from: CertificatePinner.kt */`
- `sources/okhttp3/CertificatePinner.java:88`
  `@Metadata(d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\b\u0086\u0003\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002...`
- `sources/okhttp3/CertificatePinner.java:102`
  `return Intrinsics.stringPlus("sha256/", sha256Hash((X509Certificate) certificate).base64());`
- `sources/okhttp3/CertificatePinner.java:128`
  `/* JADX INFO: compiled from: CertificatePinner.kt */`
- `sources/okhttp3/CertificatePinner.java:129`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0007\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0004\u0018\u00002\u00020\u0001B\u0015\u0012\u0006\u0010\...`
- `sources/okhttp3/CertificatePinner.java:164`
  `if (!StringsKt__StringsJVMKt.startsWith$default(pin, "sha256/", false, 2, null)) {`
- `sources/okhttp3/CertificatePinner.java:165`
  `throw new IllegalArgumentException(Intrinsics.stringPlus("pins must start with 'sha256/' or 'sha1/': ", pin));`
- `sources/okhttp3/CertificatePinner.java:212`
  `return Intrinsics.areEqual(this.hash, CertificatePinner.INSTANCE.sha256Hash(certificate));`
- `sources/okhttp3/CertificatePinner.java:215`
  `return Intrinsics.areEqual(this.hash, CertificatePinner.INSTANCE.sha1Hash(certificate));`
- `sources/okhttp3/CertificatePinner.java:252`
  `public CertificatePinner(@NotNull Set<Pin> pins, @Nullable CertificateChainCleaner certificateChainCleaner) {`
- `sources/okhttp3/CertificatePinner.java:279`
  `check$okhttp(hostname, new Function0<List<? extends X509Certificate>>() { // from class: okhttp3.CertificatePinner.check.1`
- `sources/okhttp3/CertificatePinner.java:289`
  `CertificateChainCleaner certificateChainCleaner = CertificatePinner.this.getCertificateChainCleaner();`
- `sources/okhttp3/CertificatePinner.java:359`
  `if (other instanceof CertificatePinner) {`
- `sources/okhttp3/CertificatePinner.java:360`
  `CertificatePinner certificatePinner = (CertificatePinner) other;`
- `sources/okhttp3/CertificatePinner.java:361`
  `if (Intrinsics.areEqual(certificatePinner.pins, this.pins) && Intrinsics.areEqual(certificatePinner.certificateChainCleaner, this.certificateChainCleaner)) {`
- `sources/okhttp3/CertificatePinner.java:402`
  `public final CertificatePinner withCertificateChainCleaner$okhttp(@NotNull CertificateChainCleaner certificateChainCleaner) {`
- `sources/okhttp3/CertificatePinner.java:404`
  `return Intrinsics.areEqual(this.certificateChainCleaner, certificateChainCleaner) ? this : new CertificatePinner(this.pins, certificateChainCleaner);`
- `sources/okhttp3/CertificatePinner.java:414`
  `public /* synthetic */ CertificatePinner(Set set, CertificateChainCleaner certificateChainCleaner, int i2, DefaultConstructorMarker defaultConstructorMarker) {`
- `sources/okhttp3/OkHttpClient.java:48`
  `@Metadata(d1 = {"\u0000î\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u001a\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u00...`
- `sources/okhttp3/OkHttpClient.java:62`
  `private final CertificatePinner certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:134`
  `@Metadata(d1 = {"\u0000ø\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0018...`
- `sources/okhttp3/OkHttpClient.java:148`
  `private CertificatePinner certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:230`
  `this.certificatePinner = CertificatePinner.DEFAULT;`
- `sources/okhttp3/OkHttpClient.java:307`
  `public final Builder certificatePinner(@NotNull CertificatePinner certificatePinner) {`
- `sources/okhttp3/OkHttpClient.java:308`
  `Intrinsics.checkNotNullParameter(certificatePinner, "certificatePinner");`
- `sources/okhttp3/OkHttpClient.java:309`
  `if (!Intrinsics.areEqual(certificatePinner, getCertificatePinner())) {`
- `sources/okhttp3/OkHttpClient.java:312`
  `setCertificatePinner$okhttp(certificatePinner);`
- `sources/okhttp3/OkHttpClient.java:414`
  `/* JADX INFO: renamed from: getCertificatePinner$okhttp, reason: from getter */`
- `sources/okhttp3/OkHttpClient.java:415`
  `public final CertificatePinner getCertificatePinner() {`
- `sources/okhttp3/OkHttpClient.java:416`
  `return this.certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:679`
  `public final void setCertificatePinner$okhttp(@NotNull CertificatePinner certificatePinner) {`
- `sources/okhttp3/OkHttpClient.java:680`
  `Intrinsics.checkNotNullParameter(certificatePinner, "<set-?>");`
- `sources/okhttp3/OkHttpClient.java:681`
  `this.certificatePinner = certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:905`
  `this.certificatePinner = okHttpClient.certificatePinner();`
- `sources/okhttp3/OkHttpClient.java:994`
  `this.certificatePinner = CertificatePinner.DEFAULT;`
- `sources/okhttp3/OkHttpClient.java:1003`
  `CertificatePinner certificatePinner = builder.getCertificatePinner();`
- `sources/okhttp3/OkHttpClient.java:1005`
  `this.certificatePinner = certificatePinner.withCertificateChainCleaner$okhttp(certificateChainCleaner);`
- `sources/okhttp3/OkHttpClient.java:1017`
  `CertificatePinner certificatePinner2 = builder.getCertificatePinner();`
- `sources/okhttp3/OkHttpClient.java:1019`
  `this.certificatePinner = certificatePinner2.withCertificateChainCleaner$okhttp(certificateChainCleaner2);`
- `sources/okhttp3/OkHttpClient.java:1066`
  `if (!Intrinsics.areEqual(this.certificatePinner, CertificatePinner.DEFAULT)) {`
- `sources/okhttp3/OkHttpClient.java:1094`
  `@Deprecated(level = DeprecationLevel.ERROR, message = "moved to val", replaceWith = @ReplaceWith(expression = "certificatePinner", imports = {}))`
- `sources/okhttp3/OkHttpClient.java:1095`
  `@JvmName(name = "-deprecated_certificatePinner")`
- `sources/okhttp3/OkHttpClient.java:1097`
  `/* JADX INFO: renamed from: -deprecated_certificatePinner, reason: not valid java name and from getter */`
- `sources/okhttp3/OkHttpClient.java:1098`
  `public final CertificatePinner getCertificatePinner() {`
- `sources/okhttp3/OkHttpClient.java:1099`
  `return this.certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:1295`
  `@JvmName(name = "certificatePinner")`
- `sources/okhttp3/OkHttpClient.java:1297`
  `public final CertificatePinner certificatePinner() {`
- `sources/okhttp3/OkHttpClient.java:1298`
  `return this.certificatePinner;`
- `sources/okhttp3/internal/connection/RealCall.java:27`
  `import okhttp3.CertificatePinner;`
- `sources/okhttp3/internal/connection/RealCall.java:305`
  `CertificatePinner certificatePinner;`
- `sources/okhttp3/internal/connection/RealCall.java:310`
  `certificatePinner = this.client.certificatePinner();`
- `sources/okhttp3/internal/connection/RealCall.java:314`
  `certificatePinner = null;`
- `sources/okhttp3/internal/connection/RealCall.java:316`
  `return new Address(url.host(), url.port(), this.client.dns(), this.client.socketFactory(), sSLSocketFactory, hostnameVerifier, certificatePinner, this.client.proxyAuthenticator(), this.client.proxy(), this.client.protocols(), this.client.connectionSpecs(), this.client.proxySelector());`
- `sources/okhttp3/internal/connection/RealConnection.java:35`
  `import okhttp3.CertificatePinner;`
- `sources/okhttp3/internal/connection/RealConnection.java:237`
  `final CertificatePinner certificatePinner = address.certificatePinner();`

## BR013

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `resources/com.bupa.digitalprimarycare.apk/res/color/design_box_stroke_color.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/com.bupa.digitalprimarycare.apk/res/color/zui_input_box_hint_color.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/$avd_hide_password__0.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/$avd_hide_password__1.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/$avd_hide_password__2.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/$avd_show_password__0.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/$avd_show_password__1.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/$avd_show_password__2.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/$zui_avd_typing_indicator__0.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_ab_back_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_arrow_drop_right_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_clear_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_go_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_menu_copy_mtrl_am_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_menu_cut_mtrl_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_menu_overflow_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_menu_paste_mtrl_am_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_menu_selectall_mtrl_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_menu_share_mtrl_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_voice_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_seekbar_tick_mark_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_star_black_48dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_star_half_black_48dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_text_cursor_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_vector_test.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/avd_hide_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_hide_password__0_res_0x7f080000">`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/avd_show_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_show_password__0_res_0x7f080003">`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/bootsplash_cyrus.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android" android:opacity="opaque">`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/bootsplash_us.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android" android:opacity="opaque">`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/btn_checkbox_checked_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/btn_checkbox_unchecked_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/btn_radio_off_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/btn_radio_on_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/bt_ic_vaulted_visa.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/bt_ic_visa.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/design_ic_visibility.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/design_ic_visibility_off.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/gray_circle.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/ic_checked_box.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`

## BR014

paper_id: B022
paper_title: A Study of Android Application Security

- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1506`
  `boolean z3 = KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1;`
- `sources/androidx/appcompat/app/ToolbarActionBar.java:312`
  `menu.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);`
- `sources/androidx/appcompat/app/WindowDecorActionBar.java:953`
  `menu.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);`
- `sources/androidx/core/content/ContextCompat.java:59`
  `import android.telephony.TelephonyManager;`
- `sources/androidx/core/content/ContextCompat.java:311`
  `map.put(TelephonyManager.class, HintConstants.AUTOFILL_HINT_PHONE);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:5`
  `import android.telephony.TelephonyManager;`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:15`
  `public class TelephonyManagerCompat {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:16`
  `private static Method sGetDeviceIdMethod;`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:28`
  `static String a(TelephonyManager telephonyManager, int i2) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:29`
  `return telephonyManager.getDeviceId(i2);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:42`
  `static String a(TelephonyManager telephonyManager) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:43`
  `return telephonyManager.getImei();`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:53`
  `static int a(TelephonyManager telephonyManager) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:54`
  `return telephonyManager.getSubscriptionId();`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:58`
  `private TelephonyManagerCompat() {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:64`
  `public static String getImei(@NonNull TelephonyManager telephonyManager) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:68`
  `return Api26Impl.a(telephonyManager);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:70`
  `if (i2 < 22 || (subscriptionId = getSubscriptionId(telephonyManager)) == Integer.MAX_VALUE || subscriptionId == -1) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:71`
  `return telephonyManager.getDeviceId();`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:75`
  `return Api23Impl.a(telephonyManager, slotIndex);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:78`
  `if (sGetDeviceIdMethod == null) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:79`
  `Method declaredMethod = TelephonyManager.class.getDeclaredMethod("getDeviceId", Integer.TYPE);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:80`
  `sGetDeviceIdMethod = declaredMethod;`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:83`
  `return (String) sGetDeviceIdMethod.invoke(telephonyManager, Integer.valueOf(slotIndex));`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:90`
  `public static int getSubscriptionId(@NonNull TelephonyManager telephonyManager) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:93`
  `return Api30Impl.a(telephonyManager);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:100`
  `Method declaredMethod = TelephonyManager.class.getDeclaredMethod("getSubId", new Class[0]);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:104`
  `Integer num = (Integer) sGetSubIdMethod.invoke(telephonyManager, new Object[0]);`
- `sources/bo/app/q1.java:12`
  `import android.telephony.TelephonyManager;`
- `sources/bo/app/q1.java:140`
  `public String getDeviceId() {`
- `sources/bo/app/q1.java:181`
  `TelephonyManager telephonyManager = (TelephonyManager) this.f5289a.getSystemService(HintConstants.AUTOFILL_HINT_PHONE);`
- `sources/bo/app/q1.java:182`
  `int phoneType = telephonyManager.getPhoneType();`
- `sources/bo/app/q1.java:185`
  `return telephonyManager.getNetworkOperatorName();`
- `sources/bo/app/w1.java:19`
  `String getDeviceId();`
- `sources/bo/app/z.java:172`
  `if (w1Var.getDeviceId() != null) {`
- `sources/bo/app/z.java:173`
  `k3Var.b(w1Var.getDeviceId());`
- `sources/com/appboy/Appboy.java:855`
  `public String getDeviceId() {`
- `sources/com/appboy/Appboy.java:872`
  `return getDeviceId();`
- `sources/com/appboy/IAppboy.java:59`
  `String getDeviceId();`
- `sources/com/appsflyer/internal/AFa1hSDK.java:7`
  `import android.telephony.TelephonyManager;`
- `sources/com/appsflyer/internal/AFa1hSDK.java:35`
  `TelephonyManager telephonyManager;`
- `sources/com/appsflyer/internal/AFa1hSDK.java:58`
  `telephonyManager = (TelephonyManager) context.getSystemService(HintConstants.AUTOFILL_HINT_PHONE);`
- `sources/com/appsflyer/internal/AFa1hSDK.java:59`
  `simOperatorName = telephonyManager.getSimOperatorName();`
- `sources/com/appsflyer/internal/AFa1hSDK.java:65`
  `networkOperatorName = telephonyManager.getNetworkOperatorName();`
- `sources/com/appsflyer/internal/AFa1hSDK.java:67`
  `if (2 == telephonyManager.getPhoneType()) {`
- `sources/com/appsflyer/internal/AFe1nSDK.java:86`
  `android.telephony.TelephonyManager r1 = (android.telephony.TelephonyManager) r1     // Catch: java.lang.Exception -> L55 java.lang.reflect.InvocationTargetException -> L77`
- `sources/com/appsflyer/internal/AFe1nSDK.java:88`
  `java.lang.String r7 = "getDeviceId"`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:5`
  `import android.telephony.TelephonyManager;`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:40`
  `TelephonyManager telephonyManager = (TelephonyManager) context.getSystemService(HintConstants.AUTOFILL_HINT_PHONE);`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:41`
  `if (telephonyManager != null) {`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:42`
  `this.Cardinal = setLinkTextColor.init(telephonyManager.getMmsUAProfUrl());`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:43`
  `this.init = setLinkTextColor.init(telephonyManager.getMmsUserAgent());`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:44`
  `this.configure = telephonyManager.getNetworkType();`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:45`
  `this.CardinalError = setLinkTextColor.init(telephonyManager.getNetworkOperator());`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:46`
  `this.cleanup = setLinkTextColor.init(telephonyManager.getNetworkOperatorName());`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:47`
  `this.valueOf = setLinkTextColor.init(telephonyManager.getSimCountryIso());`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:48`
  `this.CardinalUiType = setLinkTextColor.init(telephonyManager.getSimOperator());`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:49`
  `this.CardinalRenderType = setLinkTextColor.init(telephonyManager.getSimOperatorName());`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:50`
  `this.CardinalActionCode = telephonyManager.getSimState();`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:51`
  `this.CardinalEnvironment = telephonyManager.hasIccCard();`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:54`
  `this.getRequestTimeout = telephonyManager.getPhoneCount();`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:55`
  `this.getWarnings = telephonyManager.isHearingAidCompatibilitySupported();`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:56`
  `this.values = telephonyManager.isTtyModeSupported();`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:57`
  `this.getSDKVersion = telephonyManager.isWorldPhone();`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:59`
  `this.getActionCode = telephonyManager.isNetworkRoaming();`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:60`
  `this.setRequestTimeout = telephonyManager.isSmsCapable();`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:62`
  `this.CardinalConfigurationParameters = telephonyManager.isVoiceCapable();`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:64`
  `this.cca_continue = setLinkTextColor.init(telephonyManager.getNetworkCountryIso());`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:66`
  `int phoneType = telephonyManager.getPhoneType();`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:8`
  `import android.telephony.TelephonyManager;`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:331`
  `private static TelephonyManager getTelephonyManager(Context context) {`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:332`
  `return (TelephonyManager) context.getSystemService(HintConstants.AUTOFILL_HINT_PHONE);`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:350`
  `return eventInternal.toBuilder().addMetadata(KEY_SDK_VERSION, Build.VERSION.SDK_INT).addMetadata("model", Build.MODEL).addMetadata(KEY_HARDWARE, Build.HARDWARE).addMetadata("device", Build.DEVICE).addMetadata(KEY_PRODUCT, Build.PRODUCT).addMetadata(KEY_OS_BUILD, Build.ID).addMetadata("manufacturer",...`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:26`
  `import android.telephony.TelephonyManager;`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:255`
  `TelephonyManager telephonyManager = (TelephonyManager) getReactApplicationContext().getSystemService(HintConstants.AUTOFILL_HINT_PHONE);`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:256`
  `if (telephonyManager != null) {`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:257`
  `return telephonyManager.getNetworkOperatorName();`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:259`
  `System.err.println("Unable to get network operator name. TelephonyManager was null");`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:566`
  `TelephonyManager telephonyManager = (TelephonyManager) getReactApplicationContext().getSystemService(HintConstants.AUTOFILL_HINT_PHONE);`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:567`
  `if (telephonyManager == null) {`

## BR015

paper_id: B022
paper_title: A Study of Android Application Security

- `sources/androidx/biometric/BiometricFragment.java:281`
  `if (context == null || !DeviceUtils.c(context, Build.MODEL)) {`
- `sources/androidx/biometric/BiometricFragment.java:302`
  `return (activity == null || this.f706b.j() == null || !DeviceUtils.d(activity, Build.MANUFACTURER, Build.MODEL)) ? false : true;`
- `sources/androidx/biometric/BiometricFragment.java:434`
  `if (!DeviceUtils.c(applicationContext, Build.MODEL)) {`
- `sources/androidx/biometric/BiometricFragment.java:533`
  `if (context == null || !DeviceUtils.b(context, Build.MODEL)) {`
- `sources/androidx/biometric/BiometricManager.java:114`
  `return DeviceUtils.a(this.mContext, Build.MODEL);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:54`
  `return "HUAWEI".equalsIgnoreCase(Build.BRAND) && "HWANE".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:58`
  `return "OnePlus".equalsIgnoreCase(Build.BRAND) && "OnePlus6".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:62`
  `return "OnePlus".equalsIgnoreCase(Build.BRAND) && "OnePlus6T".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExtraSupportedSurfaceCombinationsQuirk.java:69`
  `String str = Build.DEVICE;`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExtraSupportedSurfaceCombinationsQuirk.java:74`
  `if (!"samsung".equalsIgnoreCase(Build.BRAND)) {`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExtraSupportedSurfaceCombinationsQuirk.java:77`
  `return SUPPORT_EXTRA_FULL_CONFIGURATIONS_SAMSUNG_MODELS.contains(Build.MODEL.toUpperCase(Locale.US));`
- `sources/androidx/camera/camera2/internal/compat/quirk/JpegHalCorruptImageQuirk.java:19`
  `return KNOWN_AFFECTED_DEVICES.contains(Build.DEVICE.toLowerCase(Locale.US));`
- `sources/androidx/camera/camera2/internal/compat/quirk/Nexus4AndroidLTargetAspectRatioQuirk.java:16`
  `return "GOOGLE".equalsIgnoreCase(Build.BRAND) && Build.VERSION.SDK_INT < 23 && DEVICE_MODELS.contains(Build.MODEL.toUpperCase(Locale.US));`
- `sources/androidx/camera/camera2/internal/compat/quirk/PreviewPixelHDRnetQuirk.java:16`
  `return "Google".equals(Build.MANUFACTURER) && SUPPORTED_DEVICES.contains(Build.DEVICE.toLowerCase(Locale.getDefault()));`
- `sources/androidx/camera/core/impl/CameraValidator.java:42`
  `Logger.d(TAG, "Verifying camera lens facing on " + Build.DEVICE + ", lensFacingInteger: " + lensFacing);`
- `sources/androidx/camera/core/impl/DeviceProperties.java:14`
  `return create(Build.MANUFACTURER, Build.MODEL, Build.VERSION.SDK_INT);`
- `sources/androidx/camera/core/impl/utils/ExifData.java:398`
  `return new Builder(ByteOrder.BIG_ENDIAN).setAttribute(ExifInterface.TAG_ORIENTATION, String.valueOf(1)).setAttribute(ExifInterface.TAG_X_RESOLUTION, "72/1").setAttribute(ExifInterface.TAG_Y_RESOLUTION, "72/1").setAttribute(ExifInterface.TAG_RESOLUTION_UNIT, String.valueOf(2)).setAttribute(ExifInterf...`
- `sources/androidx/camera/video/internal/compat/quirk/EncoderNotUsePersistentInputSurfaceQuirk.java:15`
  `return Build.VERSION.SDK_INT <= 22 || DEVICE_MODELS.contains(Build.MODEL.toUpperCase());`
- `sources/androidx/camera/video/internal/compat/quirk/MediaCodecInfoReportIncorrectInfoQuirk.java:17`
  `return "Huawei".equalsIgnoreCase(Build.BRAND) && "mha-l29".equalsIgnoreCase(Build.MODEL);`
- `sources/androidx/camera/video/internal/compat/quirk/ReportedVideoQualityNotSupportedQuirk.java:16`
  `return "Huawei".equalsIgnoreCase(Build.BRAND) && "HMA-L29".equalsIgnoreCase(Build.MODEL);`
- `sources/androidx/camera/view/internal/compat/quirk/SurfaceViewStretchedQuirk.java:21`
  `return OPPO.equalsIgnoreCase(Build.MANUFACTURER) && OPPO_FIND_N.equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/view/internal/compat/quirk/SurfaceViewStretchedQuirk.java:25`
  `if ("SAMSUNG".equalsIgnoreCase(Build.MANUFACTURER)) {`
- `sources/androidx/camera/view/internal/compat/quirk/SurfaceViewStretchedQuirk.java:26`
  `String str = Build.DEVICE;`
- `sources/com/appboy/Appboy.java:184`
  `String str2 = Build.MODEL;`
- `sources/com/appboy/Constants.java:89`
  `public static final Boolean IS_AMAZON = Boolean.valueOf("Amazon".equals(Build.MANUFACTURER));`
- `sources/com/appsflyer/internal/AFb1xSDK.java:1718`
  `String lowerCase = str.toLowerCase(Locale.getDefault());`
- `sources/com/appsflyer/internal/AFb1ySDK.java:237`
  `String lowerCase = AFKeystoreWrapper(mac.doFinal(str.getBytes())).toLowerCase(Locale.getDefault());`
- `sources/com/appsflyer/internal/AFc1kSDK.java:384`
  `map.put(Device.JsonKeys.MODEL, Build.MODEL);`
- `sources/com/appsflyer/internal/AFc1kSDK.java:387`
  `map.put(((String) objArr[0]).intern(), Build.BRAND);`
- `sources/com/appsflyer/internal/AFc1oSDK.java:55`
  `Number number = NumberFormat.getInstance(Locale.getDefault()).parse(str);`
- `sources/com/appsflyer/internal/AFc1qSDK.java:689`
  `Map<String, String> mapMapOf = MapsKt__MapsKt.mapOf(TuplesKt.to(((String) objArr[0]).intern(), Build.BRAND), TuplesKt.to(Device.JsonKeys.MODEL, Build.MODEL), TuplesKt.to("app_id", afDebugLog().AFKeystoreWrapper.AFKeystoreWrapper.getPackageName()), TuplesKt.to("p_ex", new AFb1vSDK().AFKeystoreWrapper...`
- `sources/com/appsflyer/internal/AFd1dSDK.java:103`
  `aFa1sSDK.AFKeystoreWrapper(Device.JsonKeys.MODEL, Build.MODEL);`
- `sources/com/appsflyer/internal/AFd1dSDK.java:106`
  `aFa1sSDK.AFKeystoreWrapper(((String) objArr[0]).intern(), Build.BRAND);`
- `sources/com/appsflyer/internal/AFd1wSDK.java:114`
  `Locale locale = Locale.getDefault();`
- `sources/com/appsflyer/internal/AFe1mSDK.java:46`
  `} else if (afRDLog.contains(strAFInAppEventType.toLowerCase(Locale.getDefault()))) {`
- `sources/com/auth0/android/request/ServerResponse.java:110`
  `Locale locale = Locale.getDefault();`
- `sources/com/braintreepayments/api/DeviceInspector.java:175`
  `String str = Build.PRODUCT;`
- `sources/com/braintreepayments/api/DeviceInspector.java:176`
  `if (StringsKt__StringsJVMKt.equals("google_sdk", str, true) || StringsKt__StringsJVMKt.equals("sdk", str, true) || StringsKt__StringsJVMKt.equals("Genymotion", Build.MANUFACTURER, true)) {`
- `sources/com/braintreepayments/api/DeviceInspector.java:189`
  `return new DeviceMetadata(getAppVersion(context), Build.MANUFACTURER, Build.MODEL, this.uuidHelper.getPersistentUUID(context), getDropInVersion(), str2, isPayPalInstalled(context), isDeviceEmulator(), isVenmoInstalled(context), packageName, appName, getNetworkType(context), "Android", strValueOf, "4...`
- `sources/com/braintreepayments/api/HttpRequest.java:70`
  `this.headers.put(HttpHeaders.ACCEPT_LANGUAGE, Locale.getDefault().getLanguage());`
- `sources/com/bumptech/glide/load/resource/bitmap/HardwareConfigState.java:71`
  `String str = Build.MODEL;`
- `sources/com/cardinalcommerce/a/BCDHPublicKey.java:23`
  `Locale locale = Locale.getDefault();`
- `sources/com/cardinalcommerce/a/CardinalError.java:47`
  `jSONObject.put("UserAgent", Build.BRAND);`
- `sources/com/cardinalcommerce/a/setCompoundDrawablePadding.java:85`
  `String str = Build.BRAND;`
- `sources/com/cardinalcommerce/a/setCompoundDrawablePadding.java:87`
  `this.CardinalError = setLinkTextColor.init(Build.DEVICE);`
- `sources/com/cardinalcommerce/a/setCompoundDrawablePadding.java:90`
  `String str2 = Build.MANUFACTURER;`
- `sources/com/cardinalcommerce/a/setCompoundDrawablePadding.java:92`
  `this.CardinalActionCode = setLinkTextColor.init(Build.PRODUCT);`
- `sources/com/cardinalcommerce/a/setCompoundDrawablesRelative.java:29`
  `private char[] valueOf = setLinkTextColor.init(Locale.getDefault().getDisplayLanguage());`
- `sources/com/cardinalcommerce/a/setTextSelectHandle.java:65`
  `this.getInstance = setLinkTextColor.init(TimeZone.getDefault().getDisplayName());`
- `sources/com/facebook/react/modules/i18nmanager/I18nUtil.java:27`
  `return TextUtilsCompat.getLayoutDirectionFromLocale(Locale.getDefault()) == 1;`
- `sources/com/facebook/react/modules/systeminfo/AndroidInfoHelpers.java:27`
  `return Build.MODEL;`
- `sources/com/facebook/react/modules/systeminfo/AndroidInfoHelpers.java:29`
  `return Build.MODEL + " - " + Build.VERSION.RELEASE + " - API " + Build.VERSION.SDK_INT;`
- `sources/com/facebook/react/views/text/frescosupport/FrescoBasedReactTextInlineImageShadowNode.java:46`
  `return new Uri.Builder().scheme(UriUtil.LOCAL_RESOURCE_SCHEME).path(String.valueOf(context.getResources().getIdentifier(str.toLowerCase(Locale.getDefault()).replace("-", "_"), "drawable", context.getPackageName()))).build();`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:350`
  `return eventInternal.toBuilder().addMetadata(KEY_SDK_VERSION, Build.VERSION.SDK_INT).addMetadata("model", Build.MODEL).addMetadata(KEY_HARDWARE, Build.HARDWARE).addMetadata("device", Build.DEVICE).addMetadata(KEY_PRODUCT, Build.PRODUCT).addMetadata(KEY_OS_BUILD, Build.ID).addMetadata("manufacturer",...`
- `sources/com/google/android/material/datepicker/DaysOfWeekAdapter.java:63`
  `textView.setContentDescription(String.format(viewGroup.getContext().getString(R.string.mtrl_picker_day_of_week_column_header), this.calendar.getDisplayName(7, 2, Locale.getDefault())));`
- `sources/com/google/android/material/internal/ManufacturerUtils.java:22`
  `return Build.MANUFACTURER.toLowerCase(Locale.ENGLISH).equals(LGE);`
- `sources/com/google/android/material/internal/ManufacturerUtils.java:26`
  `return Build.MANUFACTURER.toLowerCase(Locale.ENGLISH).equals(MEIZU);`
- `sources/com/google/android/material/internal/ManufacturerUtils.java:30`
  `return Build.MANUFACTURER.toLowerCase(Locale.ENGLISH).equals(SAMSUNG);`
- `sources/com/google/firebase/FirebaseCommonRegistrar.java:59`
  `arrayList.add(LibraryVersionComponent.create(DEVICE_NAME, safeValue(Build.PRODUCT)));`
- `sources/com/google/firebase/FirebaseCommonRegistrar.java:60`
  `arrayList.add(LibraryVersionComponent.create(DEVICE_MODEL, safeValue(Build.DEVICE)));`
- `sources/com/google/firebase/FirebaseCommonRegistrar.java:61`
  `arrayList.add(LibraryVersionComponent.create(DEVICE_BRAND, safeValue(Build.BRAND)));`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:297`
  `map.put(Device.JsonKeys.BRAND, Build.BRAND);`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:298`
  `map.put(Device.JsonKeys.MODEL, Build.MODEL);`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:333`
  `return Build.DEVICE;`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:606`
  `return Build.PRODUCT;`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:628`
  `return Build.VERSION.SDK_INT >= 26 ? Build.getSerial() : Build.SERIAL;`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:718`
  `return Build.MANUFACTURER;`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:960`
  `String str2 = Build.MODEL;`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:963`
  `if (!str2.toLowerCase(locale).contains("droid4x") && !str2.contains("Emulator") && !str2.contains("Android SDK built for x86") && !Build.MANUFACTURER.contains("Genymotion")) {`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:966`
  `String str4 = Build.PRODUCT;`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:967`
  `if (!str4.contains("sdk") && !str4.contains("google_sdk") && !str4.contains("sdk_google") && !str4.contains("sdk_x86") && !str4.contains("vbox86p") && !str4.contains("emulator") && !str4.contains(Device.JsonKeys.SIMULATOR) && !Build.BOARD.toLowerCase(locale).contains("nox") && !Build.BOOTLOADER.toLo...`
- `sources/com/onfido/android/sdk/capture/antifraud/Brand.java:22`
  `return Build.BRAND;`
- `sources/com/onfido/android/sdk/capture/antifraud/Device.java:21`
  `return Build.DEVICE;`
- `sources/com/onfido/android/sdk/capture/antifraud/Manufacturer.java:22`
  `return Build.MANUFACTURER;`
- `sources/com/onfido/android/sdk/capture/antifraud/Model.java:22`
  `return Build.MODEL;`
- `sources/com/onfido/android/sdk/capture/component/active/video/capture/presentation/capture/util/DeviceUtils.java:15`
  `String manufacturer = Build.MANUFACTURER;`
- `sources/com/onfido/android/sdk/capture/component/active/video/capture/presentation/capture/util/DeviceUtils.java:16`
  `String model = Build.MODEL;`
- `sources/com/onfido/android/sdk/capture/ui/camera/liveness/LivenessConfirmationPresenter.java:503`
  `LiveVideoLanguage[] liveVideoLanguageArr = {new LiveVideoLanguage("sdk", Locale.getDefault().getLanguage())};`
- `sources/com/opentok/android/DefaultAudioDevice.java:672`
  `String str = String.format(Locale.getDefault(), "Audio capture could not be initialized.\nRequested parameters\n  Sampling Rate: %d\n  Number of channels: %d\n  Buffer size: %d\n", Integer.valueOf(this.captureSettings.getSampleRate()), Integer.valueOf(this.captureSettings.getNumChannels()), Integer....`
- `sources/com/opentok/android/DefaultVideoCapturer.java:492`
  `if (-1 != Build.MODEL.toLowerCase().indexOf("samsung")) {`

## BR016

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/res/values/strings.xml:175`
  `<string name="com_appboy_api_key">21116020-c7ac-4015-8de8-f746c0fc8a13</string>`
- `resources/res/values/strings.xml:276`
  `<string name="google_api_key">AIzaSyAMzjyS6YeyfWZDQUorVJdEZm1vx2q1B6w</string>`
- `resources/res/values/strings.xml:278`
  `<string name="google_crash_reporting_api_key">AIzaSyAMzjyS6YeyfWZDQUorVJdEZm1vx2q1B6w</string>`
- `sources/bo/app/e2.java:75`
  `String string = brazeConfigurationProvider.getAppboyApiKey().toString();`
- `sources/com/appboy/Appboy.java:159`
  `public static volatile Boolean sIsApiKeyPresent = null;`
- `sources/com/appboy/configuration/AppboyConfigurationProvider.java:32`
  `public static final String API_KEY = "com_appboy_api_key";`
- `sources/com/appboy/configuration/AppboyConfigurationProvider.java:62`
  `public static final String LOCALE_TO_API_KEY_MAPPING_KEY = "com_appboy_locale_api_key_map";`
- `sources/com/appboy/configuration/AppboyConfigurationProvider.java:63`
  `public static final String LOCALE_TO_API_KEY_MAPPING_SEPARATOR = ",";`
- `sources/com/appsflyer/internal/AFe1lSDK.java:67`
  `strValues = string2.split(AppboyConfigurationProvider.LOCALE_TO_API_KEY_MAPPING_SEPARATOR)[r0.length - 1];`
- `sources/com/appsflyer/internal/AFe1lSDK.java:70`
  `String[] strArrSplit = string.split(AppboyConfigurationProvider.LOCALE_TO_API_KEY_MAPPING_SEPARATOR);`
- `sources/com/auth0/android/authentication/AuthenticationAPIClient.java:38`
  `@Metadata(d1 = {"\u0000\u0080\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0...`
- `sources/com/auth0/android/authentication/AuthenticationAPIClient.java:544`
  `public final Request<UserProfile, AuthenticationException> userInfo(@NotNull String accessToken) {`
- `sources/com/auth0/android/authentication/AuthenticationAPIClient.java:545`
  `Intrinsics.checkNotNullParameter(accessToken, "accessToken");`
- `sources/com/auth0/android/authentication/AuthenticationAPIClient.java:546`
  `return profileRequest().addHeader("Authorization", "Bearer " + accessToken);`
- `sources/com/auth0/android/authentication/AuthenticationException.java:24`
  `@Metadata(d1 = {"\u00006\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0007\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0010$\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0002\b\u001f\n\u0002\u0010\u0002\n\u0002\b\u0002\u0018\u0000 32\u00020\u0001:\u00013B...`
- `sources/com/auth0/android/authentication/AuthenticationException.java:43`
  `private static final String ERROR_OIDC_ACCESS_TOKEN = "OIDC conformant clients cannot use /oauth/access_token";`
- `sources/com/auth0/android/authentication/ParameterBuilder.java:18`
  `@Metadata(d1 = {"\u0000$\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010$\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010%\n\u0002\b\u0016\n\u0002\u0018\u0002\n\u0002\b\u0002\u0018\u0000 \u001e2\u00020\u0001:\u0001\u001eB\u001b\b\u0002\u0012\u0012\u0010\u0002\u001a\u000e\u0012\u0004\u0012\u0...`
- `sources/com/auth0/android/authentication/ParameterBuilder.java:59`
  `public static final String GRANT_TYPE_REFRESH_TOKEN = "refresh_token";`
- `sources/com/auth0/android/authentication/ParameterBuilder.java:68`
  `public static final String REFRESH_TOKEN_KEY = "refresh_token";`
- `sources/com/auth0/android/authentication/ParameterBuilder.java:86`
  `@Metadata(d1 = {"\u0000\"\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0013\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010$\n\u0000\b\u0086\u0003\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002J\b\u0010\u0017\u001a\u00020\u0018H\u0007J\u...`
- `sources/com/auth0/android/authentication/storage/CredentialsManager.java:37`
  `@Metadata(d1 = {"\u0000j\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\b\n\u0002\b\u0002\n\u...`
- `sources/com/auth0/android/authentication/storage/CredentialsManager.java:45`
  `private static final String KEY_ACCESS_TOKEN = "com.auth0.access_token";`
- `sources/com/auth0/android/authentication/storage/CredentialsManager.java:57`
  `private static final String KEY_REFRESH_TOKEN = "com.auth0.refresh_token";`
- `sources/com/auth0/android/authentication/storage/CredentialsManager.java:75`
  `@Metadata(d1 = {"\u0000\u0014\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0007\b\u0082\u0003\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002R\u000e\u0010\u0003\u001a\u00020\u0004X\u0082T¢\u0006\u0002\n\u0000R\u000e\u0010\u0005\u001a\u00020...`
- `sources/com/auth0/android/authentication/storage/SecureCredentialsManager.java:62`
  `private static final String KEY_EXPIRES_AT = "com.auth0.credentials_access_token_expires_at";`
- `sources/com/auth0/android/request/ProfileRequest.java:153`
  `java.lang.String r5 = r8.getAccessToken()`
- `sources/com/auth0/android/request/ProfileRequest.java:203`
  `Request requestAddHeader = ProfileRequest.this.userInfoRequest.addHeader("Authorization", "Bearer " + credentials.getAccessToken());`
- `sources/com/auth0/android/request/ProfileRequest.java:253`
  `return new Authentication(this.userInfoRequest.addHeader("Authorization", "Bearer " + credentialsExecute.getAccessToken()).execute(), credentialsExecute);`
- `sources/com/auth0/android/request/internal/CredentialsDeserializer.java:19`
  `@Metadata(d1 = {"\u0000:\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\t\n\u0002\b\u0004\n\u0002\u0010\u000e\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\b\u0010\u00...`
- `sources/com/auth0/android/result/Credentials.java:15`
  `@Metadata(d1 = {"\u0000*\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\t\n\u0002\b\u000e\n\u0002\u0018\u0002\n\u0002\b\u0003\b\u0016\u0018\u00002\u00020\u0001B9\u0012\u0006\u0010\u0002\u001a\u00020\u0003\u0012\u0...`
- `sources/com/auth0/android/result/Credentials.java:18`
  `@SerializedName("access_token")`
- `sources/com/auth0/android/result/UserIdentity.java:16`
  `@Metadata(d1 = {"\u0000&\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0003\n\u0002\u0010\u000b\n\u0002\b\u0003\n\u0002\u0010$\n\u0002\u0010\u0000\n\u0002\b\n\u0018\u00002\u00020\u0001BO\u0012\u0006\u0010\u0002\u001a\u00020\u0003\u0012\u0006\u0010\u0004\u001a\u00020\...`
- `sources/com/auth0/android/result/UserIdentity.java:19`
  `@SerializedName("access_token")`
- `sources/com/auth0/android/result/UserIdentity.java:21`
  `private final String accessToken;`
- `sources/com/auth0/android/result/UserIdentity.java:23`
  `@SerializedName("access_token_secret")`
- `sources/com/auth0/android/result/UserIdentity.java:25`
  `private final String accessTokenSecret;`
- `sources/com/auth0/react/CredentialsParser.java:14`
  `private static final String ACCESS_TOKEN_KEY = "accessToken";`
- `sources/com/auth0/react/CredentialsParser.java:19`
  `private static final String REFRESH_TOKEN_KEY = "refreshToken";`
- `sources/com/babylon/cyrus/MainApplication.java:35`
  `public static final String DEFAULT_API_KEY = "dev-939a0945-9285-473c-8e4b-f66a47a0e1d8";`
- `sources/com/babylon/cyrus/MainApplication.java:41`
  `public static final String PREFS_API_KEY = "prefs_api_key";`
- `sources/com/babylon/cyrus/R.java:5174`
  `public static final int com_appboy_api_key = 0x7f1100ac;`
- `sources/com/babylon/cyrus/R.java:5275`
  `public static final int google_api_key = 0x7f110111;`
- `sources/com/babylon/cyrus/R.java:5277`
  `public static final int google_crash_reporting_api_key = 0x7f110113;`
- `sources/com/braintreepayments/api/BraintreeApiConfiguration.java:15`
  `private static final String ACCESS_TOKEN_KEY = "accessToken";`
- `sources/com/braintreepayments/api/BraintreeApiConfiguration.java:24`
  `private final String accessToken;`
- `sources/com/braintreepayments/api/Configuration.java:28`
  `private static final String BRAINTREE_API_KEY = "braintreeApi";`
- `sources/com/braintreepayments/api/Configuration.java:359`
  `this.braintreeApiAccessToken = braintreeApiConfiguration.getAccessToken();`
- `sources/com/braintreepayments/api/VenmoActivityResultContract.java:24`
  `Intent intentPutExtra = getVenmoIntent().putExtra("com.braintreepayments.api.MERCHANT_ID", venmoIntentData.c()).putExtra("com.braintreepayments.api.ACCESS_TOKEN", venmoIntentData.a().getVenmoAccessToken()).putExtra("com.braintreepayments.api.ENVIRONMENT", venmoIntentData.a().getVenmoEnvironment());`
- `sources/com/braintreepayments/api/VenmoClient.java:173`
  `Intent intentPutExtra = getVenmoIntent().putExtra("com.braintreepayments.api.MERCHANT_ID", str).putExtra("com.braintreepayments.api.ACCESS_TOKEN", configuration.getVenmoAccessToken()).putExtra("com.braintreepayments.api.ENVIRONMENT", configuration.getVenmoEnvironment());`
- `sources/com/braintreepayments/api/VenmoConfiguration.java:15`
  `private static final String ACCESS_TOKEN_KEY = "accessToken";`
- `sources/com/braintreepayments/api/VenmoConfiguration.java:30`
  `private final String accessToken;`
- `sources/com/braintreepayments/api/VisaCheckoutConfiguration.java:18`
  `private static final String API_KEY = "apikey";`
- `sources/com/braintreepayments/api/VisaCheckoutConfiguration.java:80`
  `public VisaCheckoutConfiguration(@NotNull String apiKey, @NotNull String externalClientId, @NotNull List<String> acceptedCardBrands) {`
- `sources/com/braintreepayments/api/VisaCheckoutConfiguration.java:81`
  `Intrinsics.checkNotNullParameter(apiKey, "apiKey");`
- `sources/com/braintreepayments/api/VisaCheckoutConfiguration.java:84`
  `this.apiKey = apiKey;`
- `sources/com/braintreepayments/api/VisaCheckoutConfiguration.java:120`
  `public final VisaCheckoutConfiguration copy(@NotNull String apiKey, @NotNull String externalClientId, @NotNull List<String> acceptedCardBrands) {`
- `sources/com/braintreepayments/api/VisaCheckoutConfiguration.java:121`
  `Intrinsics.checkNotNullParameter(apiKey, "apiKey");`
- `sources/com/braintreepayments/api/VisaCheckoutConfiguration.java:124`
  `return new VisaCheckoutConfiguration(apiKey, externalClientId, acceptedCardBrands);`
- `sources/com/braze/configuration/BrazeConfig.java:18`
  `public final String mApiKey;`
- `sources/com/bupa/digitalprimarycare/R.java:5022`
  `public static final int com_appboy_api_key = 0x7f1100ac;`
- `sources/com/bupa/digitalprimarycare/R.java:5123`
  `public static final int google_api_key = 0x7f110111;`
- `sources/com/bupa/digitalprimarycare/R.java:5125`
  `public static final int google_crash_reporting_api_key = 0x7f110113;`
- `sources/com/google/android/datatransport/cct/CCTDestination.java:16`
  `private static final String DEFAULT_API_KEY;`
- `sources/com/google/android/datatransport/cct/CCTDestination.java:30`
  `private final String apiKey;`
- `sources/com/google/android/datatransport/cct/CCTDestination.java:41`
  `DEFAULT_API_KEY = strA3;`
- `sources/com/google/android/gms/auth/api/signin/GoogleSignInOptions.java:89`
  `@SafeParcelable.Field(getter = "isForceCodeForRefreshToken", id = 6)`
- `sources/com/google/android/gms/auth/api/signin/GoogleSignInOptions.java:298`
  `return new GoogleSignInOptions(3, new ArrayList(hashSet), !TextUtils.isEmpty(strOptString) ? new Account(strOptString, AccountType.GOOGLE) : null, jSONObject.getBoolean("idTokenRequested"), jSONObject.getBoolean("serverAuthRequested"), jSONObject.getBoolean("forceCodeForRefreshToken"), jSONObject.ha...`
- `sources/com/google/android/gms/auth/api/signin/GoogleSignInOptions.java:496`
  `jSONObject.put("forceCodeForRefreshToken", this.zal);`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:75`
  `public static final Task zai(@NonNull HasApiKey hasApiKey, @NonNull HasApiKey... hasApiKeyArr) {`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:76`
  `Preconditions.checkNotNull(hasApiKey, "Requested API must not be null.");`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:77`
  `for (HasApiKey hasApiKey2 : hasApiKeyArr) {`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:78`
  `Preconditions.checkNotNull(hasApiKey2, "Requested API must not be null.");`
- `sources/com/google/android/gms/common/api/internal/zaae.java:26`
  `public static void zad(Activity activity, GoogleApiManager googleApiManager, ApiKey apiKey) {`
- `sources/com/google/android/gms/common/server/response/SafeParcelResponse.java:131`
  `sb.append(AppboyConfigurationProvider.LOCALE_TO_API_KEY_MAPPING_SEPARATOR);`
- `sources/com/google/android/gms/signin/internal/SignInClientImpl.java:58`
  `bundle.putBoolean("com.google.android.gms.signin.internal.forceCodeForRefreshToken", false);`
- `sources/com/google/android/gms/signin/internal/SignInClientImpl.java:61`
  `bundle.putBoolean("com.google.android.gms.signin.internal.waitForAccessTokenRefresh", false);`
- `sources/com/google/firebase/FirebaseError.java:28`
  `public static final int ERROR_INVALID_API_KEY = 17023;`
- `sources/com/google/firebase/FirebaseOptions.java:15`
  `private static final String API_KEY_RESOURCE_NAME = "google_api_key";`
- `sources/com/google/firebase/FirebaseOptions.java:22`
  `private final String apiKey;`
- `sources/com/google/firebase/FirebaseOptions.java:31`
  `private String apiKey;`

## BR017

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `sources/com/appboy/support/StringUtils.java:88`
  `byte[] bArrDigest = MessageDigest.getInstance("MD5").digest(str.getBytes());`
- `sources/com/appsflyer/internal/AFb1ySDK.java:31`
  `MessageDigest messageDigest = MessageDigest.getInstance("SHA-256");`
- `sources/com/appsflyer/internal/AFb1ySDK.java:32`
  `messageDigest.update(str.getBytes());`
- `sources/com/appsflyer/internal/AFb1ySDK.java:33`
  `strAFKeystoreWrapper = AFKeystoreWrapper(messageDigest.digest());`
- `sources/com/appsflyer/internal/AFb1ySDK.java:56`
  `MessageDigest messageDigest = MessageDigest.getInstance("SHA-1");`
- `sources/com/appsflyer/internal/AFb1ySDK.java:57`
  `messageDigest.reset();`
- `sources/com/appsflyer/internal/AFb1ySDK.java:58`
  `messageDigest.update(str.getBytes("UTF-8"));`
- `sources/com/appsflyer/internal/AFb1ySDK.java:59`
  `strValues = values(messageDigest.digest());`
- `sources/com/appsflyer/internal/AFb1ySDK.java:65`
  `MessageDigest messageDigest2 = MessageDigest.getInstance("SHA-1");`
- `sources/com/appsflyer/internal/AFb1ySDK.java:66`
  `messageDigest2.reset();`
- `sources/com/appsflyer/internal/AFb1ySDK.java:67`
  `messageDigest2.update(str.getBytes("UTF-8"));`
- `sources/com/appsflyer/internal/AFb1ySDK.java:68`
  `String strValues2 = values(messageDigest2.digest());`
- `sources/com/appsflyer/internal/AFb1ySDK.java:103`
  `MessageDigest messageDigest = MessageDigest.getInstance("MD5");`
- `sources/com/appsflyer/internal/AFb1ySDK.java:104`
  `messageDigest.reset();`
- `sources/com/appsflyer/internal/AFb1ySDK.java:105`
  `messageDigest.update(str.getBytes("UTF-8"));`
- `sources/com/appsflyer/internal/AFb1ySDK.java:106`
  `return values(messageDigest.digest());`
- `sources/com/appsflyer/internal/AFb1ySDK.java:108`
  `MessageDigest messageDigest2 = MessageDigest.getInstance("MD5");`
- `sources/com/appsflyer/internal/AFb1ySDK.java:109`
  `messageDigest2.reset();`
- `sources/com/appsflyer/internal/AFb1ySDK.java:110`
  `messageDigest2.update(str.getBytes("UTF-8"));`
- `sources/com/appsflyer/internal/AFb1ySDK.java:111`
  `String strValues = values(messageDigest2.digest());`
- `sources/com/appsflyer/internal/AFb1ySDK.java:235`
  `Mac mac = Mac.getInstance("HmacSHA256");`
- `sources/com/appsflyer/internal/AFb1ySDK.java:236`
  `mac.init(new SecretKeySpec(str2.getBytes(), "HmacSHA256"));`
- `sources/com/appsflyer/internal/AFc1oSDK.java:77`
  `MessageDigest messageDigest = MessageDigest.getInstance("SHA-256");`
- `sources/com/appsflyer/internal/AFc1oSDK.java:80`
  `byte[] bArrDigest = messageDigest.digest(bytes);`
- `sources/com/appsflyer/internal/AFd1wSDK.java:163`
  `MessageDigest messageDigest = MessageDigest.getInstance("SHA-256");`
- `sources/com/appsflyer/internal/AFd1wSDK.java:166`
  `byte[] bArrDigest = messageDigest.digest(bytes);`
- `sources/com/auth0/android/authentication/storage/CryptoUtil.java:37`
  `import javax.crypto.spec.IvParameterSpec;`
- `sources/com/auth0/android/authentication/storage/CryptoUtil.java:38`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/auth0/android/authentication/storage/CryptoUtil.java:44`
  `private static final String AES_TRANSFORMATION = "AES/GCM/NOPADDING";`
- `sources/com/auth0/android/authentication/storage/CryptoUtil.java:45`
  `private static final String ALGORITHM_AES = "AES";`
- `sources/com/auth0/android/authentication/storage/CryptoUtil.java:46`
  `private static final String ALGORITHM_RSA = "RSA";`
- `sources/com/auth0/android/authentication/storage/CryptoUtil.java:49`
  `private static final String RSA_TRANSFORMATION = "RSA/ECB/PKCS1Padding";`
- `sources/com/auth0/android/authentication/storage/CryptoUtil.java:106`
  `Cipher cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding");`
- `sources/com/auth0/android/authentication/storage/CryptoUtil.java:112`
  `throw new CryptoException("The RSA encrypted input is corrupted and cannot be recovered. Please discard it.", e);`
- `sources/com/auth0/android/authentication/storage/CryptoUtil.java:140`
  `Cipher cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding");`
- `sources/com/auth0/android/authentication/storage/CryptoUtil.java:145`
  `Log.e(TAG, "The device can't encrypt input using a RSA Key.", e);`
- `sources/com/auth0/android/provider/AlgorithmHelper.java:7`
  `import java.security.MessageDigest;`
- `sources/com/auth0/android/provider/AlgorithmHelper.java:39`
  `MessageDigest messageDigest = MessageDigest.getInstance(SHA_256);`
- `sources/com/auth0/android/provider/AlgorithmHelper.java:40`
  `messageDigest.update(bArr, 0, bArr.length);`
- `sources/com/bumptech/glide/load/Key.java:5`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/Key.java:16`
  `void updateDiskCacheKey(@NonNull MessageDigest messageDigest);`
- `sources/com/bumptech/glide/load/Option.java:6`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/Option.java:12`
  `public void update(@NonNull byte[] bArr, @NonNull Object obj, @NonNull MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/engine/ResourceCacheKey.java:11`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/engine/cache/SafeKeyGenerator.java:32`
  `final MessageDigest f6941a;`
- `sources/com/bumptech/glide/load/engine/cache/SafeKeyGenerator.java:35`
  `PoolableDigestContainer(MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/engine/prefill/BitmapPreFillRunner.java:51`
  `public void updateDiskCacheKey(@NonNull MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/model/GlideUrl.java:11`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/UnitTransformation.java:7`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/CenterCrop.java:7`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/CenterInside.java:7`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/CircleCrop.java:7`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/FitCenter.java:7`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/GranularRoundedCorners.java:9`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/Rotate.java:9`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/RoundedCorners.java:10`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:22`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:35`
  `public void update(@NonNull byte[] bArr, @NonNull Long l2, @NonNull MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:36`
  `messageDigest.update(bArr);`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:39`
  `messageDigest.update(this.buffer.putLong(l2.longValue()).array());`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:47`
  `public void update(@NonNull byte[] bArr, @NonNull Integer num, @NonNull MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:54`
  `messageDigest.update(this.buffer.putInt(num.intValue()).array());`
- `sources/com/bumptech/glide/signature/EmptySignature.java:5`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/signature/MediaStoreSignature.java:43`
  `public void updateDiskCacheKey(@NonNull MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/signature/MediaStoreSignature.java:44`
  `messageDigest.update(ByteBuffer.allocate(12).putLong(this.dateModified).putInt(this.orientation).array());`
- `sources/com/bumptech/glide/signature/MediaStoreSignature.java:45`
  `messageDigest.update(this.mimeType.getBytes(Key.CHARSET));`
- `sources/com/bumptech/glide/signature/ObjectKey.java:34`
  `public void updateDiskCacheKey(@NonNull MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/signature/ObjectKey.java:35`
  `messageDigest.update(this.object.toString().getBytes(Key.CHARSET));`
- `sources/com/cardinalcommerce/a/ECDH.java:21`
  `private static final String[] getWarnings = {CipherStorageKeystoreAesCbc.ALGORITHM_AES, "ARC4", "ARIA", "Blowfish", "Camellia", "CAST5", "CAST6", "ChaCha", "DES", "DESede", "GOST28147", "Grainv1", "Grain128", "HC128", "HC256", "IDEA", "Noekeon", "RC2", "RC5", "RC6", "Rijndael", "Salsa20", "SEED", "S...`
- `sources/com/cardinalcommerce/a/getErrorMessage.java:7`
  `private static final String[] Cardinal = {"ssh-rsa", "ssh-ed25519", "ssh-dss"};`
- `sources/com/cardinalcommerce/a/KeyAgreementSpi.java:2887`
  `throw new MQVwithSHA512KDFAndSharedInfo("input too large for RSA cipher.");`
- `sources/com/cardinalcommerce/a/KeyAgreementSpi.java:2890`
  `throw new MQVwithSHA512KDFAndSharedInfo("input too large for RSA cipher.");`
- `sources/com/cardinalcommerce/a/KeyAgreementSpi.java:2899`
  `throw new MQVwithSHA512KDFAndSharedInfo("input too large for RSA cipher.");`
- `sources/com/cardinalcommerce/a/PSSSignatureSpi.java:26`
  `throw new IllegalArgumentException("RSA publicExponent is even");`
- `sources/com/cardinalcommerce/a/RSA.java:9`
  `public final class RSA extends isLocationDataConsentGiven implements Payment {`
- `sources/com/cardinalcommerce/a/setImageTintBlendMode.java:9`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/cardinalcommerce/a/setImageTintBlendMode.java:41`
  `byte[] bArrDigest = MessageDigest.getInstance("SHA-".concat(String.valueOf(length))).digest(byteArrayOutputStream.toByteArray());`
- `sources/com/cardinalcommerce/a/setImageTintBlendMode.java:45`
  `return new SecretKeySpec(bArr3, CipherStorageKeystoreAesCbc.ALGORITHM_AES);`
- `sources/com/cardinalcommerce/a/setMaxHeight.java:14`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/cardinalcommerce/a/setMaxHeight.java:69`
  `return new SecretKeySpec(bArr, CipherStorageKeystoreAesCbc.ALGORITHM_AES);`

## BR018

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:159`
  `int columnIndex4 = CursorUtil.getColumnIndex(cursorQuery, "run_attempt_count");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:200`
  `workInfoPojo.runAttemptCount = cursorQuery.getInt(columnIndex4);`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:223`
  `int columnIndex4 = CursorUtil.getColumnIndex(cursorQuery, "run_attempt_count");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:264`
  `workInfoPojo.runAttemptCount = cursorQuery.getInt(columnIndex4);`
- `sources/androidx/work/impl/model/WorkSpec.java:99`
  `@ColumnInfo(name = "run_attempt_count")`
- `sources/androidx/work/impl/model/WorkSpec.java:100`
  `public int runAttemptCount;`
- `sources/androidx/work/impl/model/WorkSpec.java:151`
  `@ColumnInfo(name = "run_attempt_count")`
- `sources/androidx/work/impl/model/WorkSpec.java:152`
  `public int runAttemptCount;`
- `sources/androidx/work/impl/model/WorkSpec.java:168`
  `if (this.runAttemptCount != workInfoPojo.runAttemptCount) {`
- `sources/androidx/work/impl/model/WorkSpec.java:197`
  `int iHashCode3 = (((iHashCode2 + (data != null ? data.hashCode() : 0)) * 31) + this.runAttemptCount) * 31;`
- `sources/androidx/work/impl/model/WorkSpec.java:207`
  `return new WorkInfo(UUID.fromString(this.id), this.state, this.output, this.tags, (list == null || list.isEmpty()) ? Data.EMPTY : this.progress.get(0), this.runAttemptCount);`
- `sources/androidx/work/impl/model/WorkSpec.java:227`
  `return this.periodStartTime + Math.min(WorkRequest.MAX_BACKOFF_MILLIS, this.backoffPolicy == BackoffPolicy.LINEAR ? this.backoffDelayDuration * ((long) this.runAttemptCount) : (long) Math.scalb(this.backoffDelayDuration, this.runAttemptCount - 1));`
- `sources/androidx/work/impl/model/WorkSpec.java:255`
  `if (this.initialDelay != workSpec.initialDelay || this.intervalDuration != workSpec.intervalDuration || this.flexDuration != workSpec.flexDuration || this.runAttemptCount != workSpec.runAttemptCount || this.backoffDelayDuration != workSpec.backoffDelayDuration || this.periodStartTime != workSpec.per...`
- `sources/androidx/work/impl/model/WorkSpec.java:278`
  `int iHashCode3 = (((((((i3 + ((int) (j4 ^ (j4 >>> 32)))) * 31) + this.constraints.hashCode()) * 31) + this.runAttemptCount) * 31) + this.backoffPolicy.hashCode()) * 31;`
- `sources/androidx/work/impl/model/WorkSpec.java:290`
  `return this.state == WorkInfo.State.ENQUEUED && this.runAttemptCount > 0;`
- `sources/androidx/work/impl/model/WorkSpec.java:359`
  `this.runAttemptCount = workSpec.runAttemptCount;`
- `sources/androidx/work/impl/model/WorkSpecDao.java:71`
  `@Query("SELECT id, state, output, run_attempt_count FROM workspec WHERE id=:id")`
- `sources/androidx/work/impl/model/WorkSpecDao.java:73`
  `WorkSpec.WorkInfoPojo getWorkStatusPojoForId(String str);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:75`
  `@Query("SELECT id, state, output, run_attempt_count FROM workspec WHERE id IN (:ids)")`
- `sources/androidx/work/impl/model/WorkSpecDao.java:77`
  `List<WorkSpec.WorkInfoPojo> getWorkStatusPojoForIds(List<String> list);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:79`
  `@Query("SELECT id, state, output, run_attempt_count FROM workspec WHERE id IN (SELECT work_spec_id FROM workname WHERE name=:name)")`
- `sources/androidx/work/impl/model/WorkSpecDao.java:81`
  `List<WorkSpec.WorkInfoPojo> getWorkStatusPojoForName(String str);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:83`
  `@Query("SELECT id, state, output, run_attempt_count FROM workspec WHERE id IN (SELECT work_spec_id FROM worktag WHERE tag=:tag)")`
- `sources/androidx/work/impl/model/WorkSpecDao.java:85`
  `List<WorkSpec.WorkInfoPojo> getWorkStatusPojoForTag(String str);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:87`
  `@Query("SELECT id, state, output, run_attempt_count FROM workspec WHERE id IN (:ids)")`
- `sources/androidx/work/impl/model/WorkSpecDao.java:89`
  `LiveData<List<WorkSpec.WorkInfoPojo>> getWorkStatusPojoLiveDataForIds(List<String> list);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:91`
  `@Query("SELECT id, state, output, run_attempt_count FROM workspec WHERE id IN (SELECT work_spec_id FROM workname WHERE name=:name)")`
- `sources/androidx/work/impl/model/WorkSpecDao.java:93`
  `LiveData<List<WorkSpec.WorkInfoPojo>> getWorkStatusPojoLiveDataForName(String str);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:95`
  `@Query("SELECT id, state, output, run_attempt_count FROM workspec WHERE id IN (SELECT work_spec_id FROM worktag WHERE tag=:tag)")`
- `sources/androidx/work/impl/model/WorkSpecDao.java:97`
  `LiveData<List<WorkSpec.WorkInfoPojo>> getWorkStatusPojoLiveDataForTag(String str);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:102`
  `@Query("UPDATE workspec SET run_attempt_count=run_attempt_count+1 WHERE id=:id")`
- `sources/androidx/work/impl/model/WorkSpecDao.java:103`
  `int incrementWorkSpecRunAttemptCount(String str);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:117`
  `@Query("UPDATE workspec SET run_attempt_count=0 WHERE id=:id")`
- `sources/androidx/work/impl/model/WorkSpecDao.java:118`
  `int resetWorkSpecRunAttemptCount(String str);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:30`
  `private final SharedSQLiteStatement __preparedStmtOfIncrementWorkSpecRunAttemptCount;`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:34`
  `private final SharedSQLiteStatement __preparedStmtOfResetWorkSpecRunAttemptCount;`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:43`
  `return "INSERT OR IGNORE INTO 'WorkSpec' ('id','state','worker_class_name','input_merger_class_name','input','output','initial_delay','interval_duration','flex_duration','run_attempt_count','backoff_policy','backoff_delay_duration','period_start_time','minimum_retention_duration','schedule_requested...`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:82`
  `supportSQLiteStatement.bindLong(10, workSpec.runAttemptCount);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:135`
  `this.__preparedStmtOfIncrementWorkSpecRunAttemptCount = new SharedSQLiteStatement(roomDatabase) { // from class: androidx.work.impl.model.WorkSpecDao_Impl.5`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:138`
  `return "UPDATE workspec SET run_attempt_count=run_attempt_count+1 WHERE id=?";`

## BR019

paper_id: B011
paper_title: Locking it down: The privacy and security of mobile medication apps

- `sources/androidx/appcompat/widget/ActivityChooserModel.java:104`
  `map.put(new ComponentName(activityInfo.packageName, activityInfo.name), activityResolveInfo);`
- `sources/androidx/camera/camera2/internal/SupportedSurfaceCombination.java:396`
  `map.put(new Rational(size.getWidth(), size.getHeight()), new ArrayList(Collections.singleton(size)));`
- `sources/androidx/camera/core/internal/ViewPorts.java:34`
  `map2.put(entry.getKey(), matrix);`
- `sources/androidx/camera/video/VideoCapabilities.java:49`
  `this.mSupportedProfileMap.put(quality, camcorderProfileProxy);`
- `sources/androidx/camera/video/VideoCapabilities.java:50`
  `this.mAreaSortedSizeToQualityMap.put(size, quality);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:475`
  `this.mTempMapIdToWidget.put(0, this.mLayoutWidget);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:476`
  `this.mTempMapIdToWidget.put(getId(), this.mLayoutWidget);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:479`
  `this.mTempMapIdToWidget.put(childAt4.getId(), getViewWidget(childAt4));`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:994`
  `this.mChildrenByIds.put(getId(), this);`
- `sources/androidx/coordinatorlayout/widget/DirectedAcyclicGraph.java:57`
  `this.mGraph.put(t2, emptyList);`
- `sources/androidx/core/graphics/TypefaceCompatApi24Impl.java:138`
  `simpleArrayMap.put(uri, byteBufferMmap);`
- `sources/androidx/core/graphics/WeightTypefaceApi21.java:89`
  `sparseArray.put(i3, typefaceCreate);`
- `sources/androidx/core/location/LocationManagerCompat.java:138`
  `simpleArrayMap.put(callback, preRGnssStatusTransport);`
- `sources/androidx/core/location/LocationManagerCompat.java:211`
  `simpleArrayMap.put(callback, gnssStatusTransport);`
- `sources/androidx/core/location/LocationManagerCompat.java:673`
  `WeakReference<LocationListenerTransport> weakReferencePut = f2725a.put(locationListenerTransport.getKey(), new WeakReference<>(locationListenerTransport));`
- `sources/androidx/transition/ChangeBounds.java:175`
  `transitionValues.values.put(PROPNAME_BOUNDS, new Rect(view.getLeft(), view.getTop(), view.getRight(), view.getBottom()));`
- `sources/androidx/transition/ChangeBounds.java:176`
  `transitionValues.values.put(PROPNAME_PARENT, transitionValues.view.getParent());`
- `sources/androidx/transition/ChangeBounds.java:179`
  `transitionValues.values.put(PROPNAME_WINDOW_X, Integer.valueOf(this.mTempLocation[0]));`
- `sources/androidx/transition/ChangeBounds.java:180`
  `transitionValues.values.put(PROPNAME_WINDOW_Y, Integer.valueOf(this.mTempLocation[1]));`
- `sources/androidx/transition/ChangeBounds.java:183`
  `transitionValues.values.put(PROPNAME_CLIP, ViewCompat.getClipBounds(view));`
- `sources/androidx/transition/ChangeClipBounds.java:31`
  `transitionValues.values.put(PROPNAME_CLIP, clipBounds);`
- `sources/androidx/transition/ChangeClipBounds.java:33`
  `transitionValues.values.put(PROPNAME_BOUNDS, new Rect(0, 0, view.getWidth(), view.getHeight()));`
- `sources/androidx/transition/Explode.java:68`
  `transitionValues.values.put(PROPNAME_SCREEN_BOUNDS, new Rect(i2, i3, view.getWidth() + i2, view.getHeight() + i3));`
- `sources/androidx/transition/VisibilityPropagation.java:34`
  `transitionValues.values.put(PROPNAME_VIEW_CENTER, iArr);`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:86`
  `map2.put("initial_delay", new TableInfo.Column("initial_delay", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:87`
  `map2.put("interval_duration", new TableInfo.Column("interval_duration", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:88`
  `map2.put("flex_duration", new TableInfo.Column("flex_duration", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:89`
  `map2.put("run_attempt_count", new TableInfo.Column("run_attempt_count", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:90`
  `map2.put("backoff_policy", new TableInfo.Column("backoff_policy", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:91`
  `map2.put("backoff_delay_duration", new TableInfo.Column("backoff_delay_duration", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:92`
  `map2.put("period_start_time", new TableInfo.Column("period_start_time", "INTEGER", true, 0, null, 1));`
- `sources/bo/app/g3.java:73`
  `jSONObjectK.put("respond_with", this.f5057q.forJsonPut());`
- `sources/bo/app/g3.java:74`
  `return jSONObjectK;`
- `sources/bo/app/k6.java:215`
  `v4 v4VarB = o6.b(new JSONObject(string), this.f5134b);`
- `sources/bo/app/k6.java:217`
  `map.put(v4VarB.getId(), v4VarB);`
- `sources/bo/app/o6.java:17`
  `public static IInAppMessage a(JSONObject jSONObject, v1 v1Var) {`
- `sources/bo/app/o6.java:19`
  `if (jSONObject == null) {`
- `sources/bo/app/o6.java:23`
  `String string = jSONObject.getString("type");`
- `sources/bo/app/o6.java:25`
  `return p4.a(jSONObject.getJSONObject("data"), v1Var);`
- `sources/bo/app/o6.java:30`
  `AppboyLogger.w(f5252a, "Encountered JSONException processing templated message: " + jSONObject, e2);`

## BR020

paper_id: B012
paper_title: Reviewing the data security and privacy policies of mobile apps for depression

- `sources/androidx/camera/video/Recorder.java:604`
  `throw new AssertionError("Attempted to update event listener with event from incorrect recording [Recording: " + videoRecordEvent.getOutputOptions() + ", Expected: " + l() + "]");`
- `sources/androidx/core/provider/FontProvider.java:98`
  `Cursor cursorA = null;`
- `sources/androidx/core/provider/FontProvider.java:100`
  `cursorA = Api16Impl.a(context.getContentResolver(), uriBuild, new String[]{"_id", FontsContractCompat.Columns.FILE_ID, FontsContractCompat.Columns.TTC_INDEX, FontsContractCompat.Columns.VARIATION_SETTINGS, FontsContractCompat.Columns.WEIGHT, FontsContractCompat.Columns.ITALIC, FontsContractCompat.Co...`
- `sources/androidx/core/provider/FontProvider.java:101`
  `if (cursorA != null && cursorA.getCount() > 0) {`
- `sources/androidx/core/provider/FontProvider.java:102`
  `int columnIndex = cursorA.getColumnIndex(FontsContractCompat.Columns.RESULT_CODE);`
- `sources/androidx/core/provider/FontProvider.java:104`
  `int columnIndex2 = cursorA.getColumnIndex("_id");`
- `sources/androidx/core/provider/FontProvider.java:105`
  `int columnIndex3 = cursorA.getColumnIndex(FontsContractCompat.Columns.FILE_ID);`
- `sources/androidx/core/provider/FontProvider.java:106`
  `int columnIndex4 = cursorA.getColumnIndex(FontsContractCompat.Columns.TTC_INDEX);`
- `sources/androidx/core/provider/FontProvider.java:107`
  `int columnIndex5 = cursorA.getColumnIndex(FontsContractCompat.Columns.WEIGHT);`
- `sources/androidx/core/provider/FontProvider.java:108`
  `int columnIndex6 = cursorA.getColumnIndex(FontsContractCompat.Columns.ITALIC);`
- `sources/androidx/core/provider/FontProvider.java:109`
  `while (cursorA.moveToNext()) {`
- `sources/androidx/core/provider/FontProvider.java:110`
  `int i4 = columnIndex != -1 ? cursorA.getInt(columnIndex) : 0;`
- `sources/androidx/core/provider/FontProvider.java:111`
  `int i5 = columnIndex4 != -1 ? cursorA.getInt(columnIndex4) : 0;`
- `sources/androidx/room/InvalidationTracker.java:326`
  `supportSQLiteDatabase.execSQL("INSERT OR IGNORE INTO room_table_modification_log VALUES(" + i2 + ", 0)");`
- `sources/androidx/room/InvalidationTracker.java:423`
  `supportSQLiteDatabase.execSQL("PRAGMA temp_store = MEMORY;");`
- `sources/androidx/room/InvalidationTracker.java:424`
  `supportSQLiteDatabase.execSQL("PRAGMA recursive_triggers='ON';");`
- `sources/androidx/room/InvalidationTracker.java:425`
  `supportSQLiteDatabase.execSQL(CREATE_TRACKING_TABLE_SQL);`
- `sources/androidx/room/InvalidationTracker.java:427`
  `this.f4142e = supportSQLiteDatabase.compileStatement("UPDATE room_table_modification_log SET invalidated = 0 WHERE invalidated = 1 ");`
- `sources/androidx/room/paging/LimitOffsetDataSource.java:72`
  `Cursor cursorQuery = null;`
- `sources/androidx/room/paging/LimitOffsetDataSource.java:79`
  `cursorQuery = this.mDb.query(sQLiteQuery);`
- `sources/androidx/room/paging/LimitOffsetDataSource.java:80`
  `List<T> listA = a(cursorQuery);`
- `sources/androidx/room/paging/LimitOffsetDataSource.java:87`
  `if (cursorQuery != null) {`
- `sources/androidx/room/paging/LimitOffsetDataSource.java:88`
  `cursorQuery.close();`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:171`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'Dependency' ('work_spec_id' TEXT NOT NULL, 'prerequisite_id' TEXT NOT NULL, PRIMARY KEY('work_spec_id', 'prerequisite_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE , FOREIGN KEY('prerequisi...`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:172`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_Dependency_work_spec_id' ON 'Dependency' ('work_spec_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:173`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_Dependency_prerequisite_id' ON 'Dependency' ('prerequisite_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:174`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'WorkSpec' ('id' TEXT NOT NULL, 'state' INTEGER NOT NULL, 'worker_class_name' TEXT NOT NULL, 'input_merger_class_name' TEXT, 'input' BLOB NOT NULL, 'output' BLOB NOT NULL, 'initial_delay' INTEGER NOT NULL, 'interval_duration' INTEGER NOT NULL...`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:175`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkSpec_schedule_requested_at' ON 'WorkSpec' ('schedule_requested_at')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:176`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkSpec_period_start_time' ON 'WorkSpec' ('period_start_time')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:177`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'WorkTag' ('tag' TEXT NOT NULL, 'work_spec_id' TEXT NOT NULL, PRIMARY KEY('tag', 'work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:178`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkTag_work_spec_id' ON 'WorkTag' ('work_spec_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:179`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'SystemIdInfo' ('work_spec_id' TEXT NOT NULL, 'system_id' INTEGER NOT NULL, PRIMARY KEY('work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:154`
  `Cursor cursorQuery = DBUtil.query(this.__db, supportSQLiteQuery, true, null);`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:156`
  `int columnIndex = CursorUtil.getColumnIndex(cursorQuery, "id");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:157`
  `int columnIndex2 = CursorUtil.getColumnIndex(cursorQuery, "state");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:158`
  `int columnIndex3 = CursorUtil.getColumnIndex(cursorQuery, "output");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:159`
  `int columnIndex4 = CursorUtil.getColumnIndex(cursorQuery, "run_attempt_count");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:162`
  `while (cursorQuery.moveToNext()) {`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:163`
  `if (!cursorQuery.isNull(columnIndex)) {`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:164`
  `String string = cursorQuery.getString(columnIndex);`

## BR021

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:291`
  `<provider`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:300`
  `<provider`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:338`
  `<provider`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:350`
  `<provider`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:362`
  `<provider`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:367`
  `<provider`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:480`
  `<provider`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:525`
  `<provider`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:534`
  `<provider`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:544`
  `<provider`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:648`
  `<provider`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:652`
  `<provider`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:686`
  `<provider`

## BR022

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `resources/com.bupa.digitalprimarycare.apk/res/xml/belvedere_attachment_storage_v2.xml:3`
  `<cache-path`
- `resources/com.bupa.digitalprimarycare.apk/res/xml/file_provider_paths.xml:3`
  `<external-path`
- `resources/com.bupa.digitalprimarycare.apk/res/xml/imagepicker_provider_paths.xml:3`
  `<cache-path`
- `resources/com.bupa.digitalprimarycare.apk/res/xml/image_share_filepaths.xml:3`
  `<files-path`
- `resources/com.bupa.digitalprimarycare.apk/res/xml/provider_paths.xml:3`
  `<external-path`
- `resources/com.bupa.digitalprimarycare.apk/res/xml/provider_paths.xml:6`
  `<files-path`
- `resources/com.bupa.digitalprimarycare.apk/res/xml/provider_paths.xml:7`
  `name="files-path"`
- `resources/com.bupa.digitalprimarycare.apk/res/xml/provider_paths.xml:9`
  `<cache-path`
- `resources/com.bupa.digitalprimarycare.apk/res/xml/provider_paths.xml:10`
  `name="cache-path"`
- `resources/com.bupa.digitalprimarycare.apk/res/xml/share_download_paths.xml:3`
  `<external-path`
- `resources/com.bupa.digitalprimarycare.apk/res/xml/share_download_paths.xml:6`
  `<cache-path`
- `resources/com.bupa.digitalprimarycare.apk/res/xml/share_download_paths.xml:9`
  `<root-path`

## BR023

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `sources/androidx/startup/InitializationProvider.java:12`
  `public class InitializationProvider extends ContentProvider {`
- `sources/com/cardinalcommerce/a/setShowSoftInputOnFocus.java:13`
  `public final class setShowSoftInputOnFocus extends ContentProvider {`
- `sources/com/facebook/react/modules/blob/BlobProvider.java:16`
  `public final class BlobProvider extends ContentProvider {`
- `sources/com/google/firebase/provider/FirebaseInitProvider.java:16`
  `public class FirebaseInitProvider extends ContentProvider {`
- `sources/com/google/mlkit/common/internal/MlKitInitProvider.java:17`
  `public class MlKitInitProvider extends ContentProvider {`
- `sources/com/oblador/performance/StartTimeProvider.java:12`
  `public class StartTimeProvider extends ContentProvider {`
- `sources/io/sentry/android/core/EmptySecureContentProvider.java:14`
  `abstract class EmptySecureContentProvider extends ContentProvider {`

## BR024

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `sources/androidx/core/content/FileProvider.java:258`
  `if (!providerInfo.grantUriPermissions) {`
- `sources/androidx/core/content/IntentSanitizer.java:938`
  `consumer.accept("Allowing Extra Stream requires also allowing at least  FLAG_GRANT_READ_URI_PERMISSION Flag.");`
- `sources/androidx/core/content/IntentSanitizer.java:948`
  `consumer.accept("Allowing Extra Output requires also allowing FLAG_GRANT_READ_URI_PERMISSION and FLAG_GRANT_WRITE_URI_PERMISSION Flags.");`
- `sources/zendesk/belvedere/Storage.java:202`
  `String str = String.format(Locale.US, "=====================\nFileProvider failed to retrieve file uri. There might be an issue with the FileProvider \nPlease make sure that manifest-merger is working, and that you have defined the applicationId (package name) in the build.gradle\nManifest merger: h...`

## BR025

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/androidx/room/InvalidationTracker.java:325`
  `private void startTrackingTable(SupportSQLiteDatabase supportSQLiteDatabase, int i2) {`
- `sources/androidx/room/InvalidationTracker.java:326`
  `supportSQLiteDatabase.execSQL("INSERT OR IGNORE INTO room_table_modification_log VALUES(" + i2 + ", 0)");`
- `sources/androidx/room/InvalidationTracker.java:417`
  `void b(SupportSQLiteDatabase supportSQLiteDatabase) {`
- `sources/androidx/room/InvalidationTracker.java:423`
  `supportSQLiteDatabase.execSQL("PRAGMA temp_store = MEMORY;");`
- `sources/androidx/room/InvalidationTracker.java:424`
  `supportSQLiteDatabase.execSQL("PRAGMA recursive_triggers='ON';");`
- `sources/androidx/room/InvalidationTracker.java:425`
  `supportSQLiteDatabase.execSQL(CREATE_TRACKING_TABLE_SQL);`
- `sources/androidx/room/InvalidationTracker.java:426`
  `f(supportSQLiteDatabase);`
- `sources/androidx/room/InvalidationTracker.java:427`
  `this.f4142e = supportSQLiteDatabase.compileStatement("UPDATE room_table_modification_log SET invalidated = 0 WHERE invalidated = 1 ");`
- `sources/androidx/room/util/TableInfo.java:8`
  `import androidx.sqlite.db.SupportSQLiteDatabase;`
- `sources/androidx/room/util/TableInfo.java:276`
  `private static Set<ForeignKey> readForeignKeys(SupportSQLiteDatabase supportSQLiteDatabase, String str) {`
- `sources/androidx/room/util/TableInfo.java:278`
  `Cursor cursorQuery = supportSQLiteDatabase.query("PRAGMA foreign_key_list('" + str + "')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:170`
  `public void createAllTables(SupportSQLiteDatabase supportSQLiteDatabase) {`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:171`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'Dependency' ('work_spec_id' TEXT NOT NULL, 'prerequisite_id' TEXT NOT NULL, PRIMARY KEY('work_spec_id', 'prerequisite_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE , FOREIGN KEY('prerequisi...`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:172`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_Dependency_work_spec_id' ON 'Dependency' ('work_spec_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:173`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_Dependency_prerequisite_id' ON 'Dependency' ('prerequisite_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:174`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'WorkSpec' ('id' TEXT NOT NULL, 'state' INTEGER NOT NULL, 'worker_class_name' TEXT NOT NULL, 'input_merger_class_name' TEXT, 'input' BLOB NOT NULL, 'output' BLOB NOT NULL, 'initial_delay' INTEGER NOT NULL, 'interval_duration' INTEGER NOT NULL...`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:175`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkSpec_schedule_requested_at' ON 'WorkSpec' ('schedule_requested_at')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:176`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkSpec_period_start_time' ON 'WorkSpec' ('period_start_time')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:177`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'WorkTag' ('tag' TEXT NOT NULL, 'work_spec_id' TEXT NOT NULL, PRIMARY KEY('tag', 'work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:178`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkTag_work_spec_id' ON 'WorkTag' ('work_spec_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:179`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'SystemIdInfo' ('work_spec_id' TEXT NOT NULL, 'system_id' INTEGER NOT NULL, PRIMARY KEY('work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:180`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'WorkName' ('name' TEXT NOT NULL, 'work_spec_id' TEXT NOT NULL, PRIMARY KEY('name', 'work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:181`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkName_work_spec_id' ON 'WorkName' ('work_spec_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:182`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'WorkProgress' ('work_spec_id' TEXT NOT NULL, 'progress' BLOB NOT NULL, PRIMARY KEY('work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:27`
  `private final RoomDatabase __db;`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:38`
  `public WorkSpecDao_Impl(RoomDatabase roomDatabase) {`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:39`
  `this.__db = roomDatabase;`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:40`
  `this.__insertionAdapterOfWorkSpec = new EntityInsertionAdapter<WorkSpec>(roomDatabase) { // from class: androidx.work.impl.model.WorkSpecDao_Impl.1`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:129`
  `this.__preparedStmtOfSetPeriodStartTime = new SharedSQLiteStatement(roomDatabase) { // from class: androidx.work.impl.model.WorkSpecDao_Impl.4`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:135`
  `this.__preparedStmtOfIncrementWorkSpecRunAttemptCount = new SharedSQLiteStatement(roomDatabase) { // from class: androidx.work.impl.model.WorkSpecDao_Impl.5`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:141`
  `this.__preparedStmtOfResetWorkSpecRunAttemptCount = new SharedSQLiteStatement(roomDatabase) { // from class: androidx.work.impl.model.WorkSpecDao_Impl.6`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:147`
  `this.__preparedStmtOfMarkWorkSpecScheduled = new SharedSQLiteStatement(roomDatabase) { // from class: androidx.work.impl.model.WorkSpecDao_Impl.7`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager$$Lambda$1.java:3`
  `import android.database.sqlite.SQLiteDatabase;`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager$$Lambda$1.java:14`
  `public void upgrade(SQLiteDatabase sQLiteDatabase) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager$$Lambda$1.java:15`
  `SchemaManager.a(sQLiteDatabase);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager$$Lambda$2.java:3`
  `import android.database.sqlite.SQLiteDatabase;`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager$$Lambda$2.java:14`
  `public void upgrade(SQLiteDatabase sQLiteDatabase) {`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager$$Lambda$2.java:15`
  `SchemaManager.b(sQLiteDatabase);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager$$Lambda$3.java:3`
  `import android.database.sqlite.SQLiteDatabase;`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager$$Lambda$3.java:14`
  `public void upgrade(SQLiteDatabase sQLiteDatabase) {`

## BR026

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/androidx/core/content/SharedPreferencesKt.java:12`
  `/* JADX INFO: compiled from: SharedPreferences.kt */`
- `sources/androidx/core/content/SharedPreferencesKt.java:14`
  `@Metadata(d1 = {"\u0000 \n\u0000\n\u0002\u0010\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000b\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\u001a3\u0010\u0000\u001a\u00020\u0001*\u00020\u00022\b\b\u0002\u0010\u0003\u001a\u00020\u00042\u0017\u0010\u0005\u001a\u001...`
- `sources/androidx/core/content/SharedPreferencesKt.java:15`
  `public final class SharedPreferencesKt {`
- `sources/androidx/core/content/SharedPreferencesKt.java:17`
  `public static final void edit(@NotNull SharedPreferences sharedPreferences, boolean z2, @NotNull Function1<? super SharedPreferences.Editor, Unit> action) {`
- `sources/androidx/core/content/SharedPreferencesKt.java:18`
  `Intrinsics.checkNotNullParameter(sharedPreferences, "<this>");`
- `sources/androidx/core/content/SharedPreferencesKt.java:20`
  `SharedPreferences.Editor editor = sharedPreferences.edit();`
- `sources/bo/app/b2.java:51`
  `SharedPreferences.Editor editorEdit = this.f4881b.edit();`
- `sources/bo/app/f4.java:18`
  `public final SharedPreferences f5031a;`
- `sources/bo/app/f4.java:21`
  `this.f5031a = context.getSharedPreferences("com.appboy.storage.session_storage" + StringUtils.getCacheFileSuffix(context, str, str2), 0);`
- `sources/bo/app/f4.java:28`
  `SharedPreferences.Editor editorEdit = this.f5031a.edit();`
- `sources/bo/app/f4.java:43`
  `SharedPreferences.Editor editorEdit = this.f5031a.edit();`
- `sources/bo/app/g4.java:112`
  `this.f5063h = context.getSharedPreferences("com.appboy.storage.user_cache.v3" + cacheFileSuffix, 0);`
- `sources/bo/app/g4.java:113`
  `this.f5064i = context.getSharedPreferences("com.appboy.storage.user_cache.push_token_store" + cacheFileSuffix, 0);`
- `sources/bo/app/g4.java:200`
  `SharedPreferences.Editor editorEdit = this.f5063h.edit();`
- `sources/bo/app/g4.java:330`
  `SharedPreferences.Editor editorEdit = this.f5064i.edit();`
- `sources/bo/app/g4.java:354`
  `SharedPreferences.Editor editorEdit2 = this.f5063h.edit();`
- `sources/bo/app/g4.java:359`
  `SharedPreferences.Editor editorEdit22 = this.f5063h.edit();`
- `sources/bo/app/o1.java:33`
  `this.f5215a = context.getSharedPreferences("com.appboy.storage.sessions.messaging_session", 0);`
- `sources/bo/app/q1.java:62`
  `this.f5295g = context.getSharedPreferences("com.appboy.managers.device_data_provider", 0);`
- `sources/bo/app/r1.java:14`
  `public final SharedPreferences f5308a;`
- `sources/bo/app/r1.java:17`
  `this.f5308a = context.getSharedPreferences("com.appboy.device", 0);`
- `sources/bo/app/r1.java:47`
  `SharedPreferences.Editor editorEdit = this.f5308a.edit();`
- `sources/bo/app/v.java:18`
  `this.f5377a = context.getSharedPreferences("com.appboy.offline.storagemap", 0);`
- `sources/bo/app/v.java:38`
  `SharedPreferences.Editor editorEdit = this.f5377a.edit();`
- `sources/bo/app/v3.java:91`
  `this.f5380e = context.getSharedPreferences("com.appboy.storage.device_cache.v3" + StringUtils.getCacheFileSuffix(context, str, str2), 0);`
- `sources/bo/app/v3.java:104`
  `SharedPreferences.Editor editorEdit = this.f5380e.edit();`
- `sources/com/appboy/support/StringUtils.java:65`
  `SharedPreferences sharedPreferences = context.getSharedPreferences(CACHE_SUFFIX_PREFERENCES_FILE_PREFIX, 0);`
- `sources/com/appboy/support/StringUtils.java:66`
  `String string = sharedPreferences.getString(SUFFIX_CACHE_USER_ID_KEY, null);`
- `sources/com/appboy/support/StringUtils.java:68`
  `String string2 = sharedPreferences.getString(SUFFIX_CACHE_USER_ID_HASH_VALUE, null);`
- `sources/com/appboy/support/StringUtils.java:79`
  `SharedPreferences.Editor editorEdit = sharedPreferences.edit();`
- `sources/com/appsflyer/internal/AFb1wSDK.java:4`
  `import android.content.SharedPreferences;`
- `sources/com/appsflyer/internal/AFb1xSDK.java:124`
  `private SharedPreferences onResponseNative;`
- `sources/com/appsflyer/internal/AFb1xSDK.java:2697`
  `map.put("launch_counter", Integer.toString(valueOf(sharedPreferencesAFKeystoreWrapper, false)));`
- `sources/com/appsflyer/internal/AFb1xSDK.java:4298`
  `public static synchronized SharedPreferences AFKeystoreWrapper(Context context) {`
- `sources/com/appsflyer/internal/AFb1xSDK.java:4303`
  `AFInAppEventType().onResponseNative = context.getApplicationContext().getSharedPreferences("appsflyer-data", 0);`
- `sources/com/braintreepayments/api/DropInClient.java:64`
  `if (DropInClient.this.dropInSharedPreferences.b() != DropInPaymentMethod.GOOGLE_PAY) {`
- `sources/com/braintreepayments/api/DropInClient.java:94`
  `return new DropInClientParams().a(fragmentActivity).m(lifecycle).c(dropInRequest).b(braintreeClient).n(new PaymentMethodClient(braintreeClient)).l(new GooglePayClient(braintreeClient)).d(DropInSharedPreferences.a(context.getApplicationContext()));`
- `sources/com/facebook/android/crypto/keychain/SharedPrefsBackedKeyChain.java:22`
  `private final SharedPreferences mSharedPreferences;`
- `sources/com/facebook/android/crypto/keychain/SharedPrefsBackedKeyChain.java:71`
  `SharedPreferences.Editor editorEdit = this.mSharedPreferences.edit();`
- `sources/com/facebook/react/devsupport/DevInternalSettings.java:23`
  `private final SharedPreferences mPreferences;`

## BR027

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:151`
  `File file = new File(this.mAppContext.getFilesDir(), BrowserServiceFileProvider.FILE_SUB_DIR);`
- `sources/androidx/camera/video/Recorder.java:404`
  `String absolutePathFromUri = OutputUtil.getAbsolutePathFromUri(mediaStoreOutputOptions.getContentResolver(), uriInsert, Recorder.MEDIA_COLUMN);`
- `sources/androidx/camera/video/Recorder.java:408`
  `if (!OutputUtil.createParentFolder(new File(absolutePathFromUri))) {`
- `sources/androidx/camera/video/Recorder.java:413`
  `ParcelFileDescriptor parcelFileDescriptorOpenFileDescriptor = mediaStoreOutputOptions.getContentResolver().openFileDescriptor(uriInsert, "rw");`
- `sources/androidx/camera/video/Recorder.java:431`
  `mediaStoreOutputOptions.getContentResolver().update(uri, contentValues, null, null);`
- `sources/androidx/camera/video/Recorder.java:444`
  `public static /* synthetic */ void lambda$initializeRecording$4(MediaStoreOutputOptions mediaStoreOutputOptions, Context context, Uri uri) throws Throwable {`
- `sources/androidx/camera/video/Recorder.java:551`
  `if (outputOptionsL instanceof MediaStoreOutputOptions) {`
- `sources/androidx/camera/video/Recorder.java:552`
  `final MediaStoreOutputOptions mediaStoreOutputOptions = (MediaStoreOutputOptions) outputOptionsL;`
- `sources/androidx/camera/video/internal/compat/quirk/DeviceQuirksLoader.java:42`
  `if (MediaStoreVideoCannotWrite.a()) {`
- `sources/androidx/camera/video/internal/compat/quirk/DeviceQuirksLoader.java:43`
  `arrayList.add(new MediaStoreVideoCannotWrite());`
- `sources/androidx/core/content/FileProvider.java:47`
  `private static final File DEVICE_ROOT = new File("/");`
- `sources/androidx/core/graphics/drawable/IconCompat.java:713`
  `return new FileInputStream(new File((String) this.f2713a));`
- `sources/androidx/core/util/AtomicFile.java:21`
  `this.mNewName = new File(file.getPath() + ".new");`
- `sources/androidx/core/util/AtomicFile.java:22`
  `this.mLegacyBackupName = new File(file.getPath() + ".bak");`
- `sources/androidx/documentfile/provider/RawDocumentFile.java:73`
  `File file = new File(this.mFile, str2);`
- `sources/androidx/sqlite/db/SupportSQLiteOpenHelper.java:35`
  `SQLiteDatabase.deleteDatabase(new File(str));`
- `sources/androidx/sqlite/db/framework/FrameworkSQLiteOpenHelper.java:127`
  `this.mDelegate = new OpenHelper(this.mContext, new File(this.mContext.getNoBackupFilesDir(), this.mName).getAbsolutePath(), frameworkSQLiteDatabaseArr, this.mCallback);`
- `sources/androidx/work/impl/WorkDatabasePathHelper.java:38`
  `return new File(context.getNoBackupFilesDir(), str);`
- `sources/androidx/work/impl/WorkDatabasePathHelper.java:73`
  `map.put(new File(defaultDatabasePath.getPath() + str), new File(databasePath.getPath() + str));`
- `sources/bo/app/j6.java:169`
  `File file = new File(context.getCacheDir(), "ab_triggers");`
- `sources/bo/app/j6.java:265`
  `AppboyFileUtils.deleteFileOrDirectory(new File(str2));`
- `sources/cl/json/RNSharePathUtil.java:10`
  `import android.provider.MediaStore;`
- `sources/cl/json/RNSharePathUtil.java:124`
  `uri2 = MediaStore.Images.Media.EXTERNAL_CONTENT_URI;`
- `sources/cl/json/RNSharePathUtil.java:126`
  `uri2 = MediaStore.Video.Media.EXTERNAL_CONTENT_URI;`
- `sources/cl/json/RNSharePathUtil.java:128`
  `uri2 = MediaStore.Audio.Media.EXTERNAL_CONTENT_URI;`
- `sources/com/afollestad/materialdialogs/folderselector/FileChooserDialog.java:192`
  `this.parentFolder = new File(getArguments().getString("current_path"));`
- `sources/com/afollestad/materialdialogs/folderselector/FolderChooserDialog.java:69`
  `File file = new File(FolderChooserDialog.this.parentFolder, charSequence.toString());`
- `sources/com/afollestad/materialdialogs/folderselector/FolderChooserDialog.java:155`
  `this.parentFolder = new File(getArguments().getString("current_path"));`
- `sources/com/airbnb/android/react/maps/AirMapTileProvider.java:134`
  `if ((System.currentTimeMillis() - new File(strE).lastModified()) / 1000 > this.f5922j) {`
- `sources/com/airbnb/lottie/network/NetworkCache.java:76`
  `File file = new File(parentDir(), filenameForUrl(str, fileExtension, true));`
- `sources/com/airbnb/lottie/network/NetworkCache.java:77`
  `File file2 = new File(file.getAbsolutePath().replace(".temp", ""));`
- `sources/com/airbnb/lottie/network/NetworkCache.java:87`
  `File file = new File(parentDir(), filenameForUrl(str, fileExtension, true));`
- `sources/com/appboy/Appboy.java:692`
  `File file = new File(context.getApplicationInfo().dataDir, "shared_prefs");`
- `sources/com/appboy/lrucache/AppboyLruImageLoader.java:154`
  `File file = new File(context.getCacheDir(), APPBOY_LRU_CACHE_FOLDER);`
- `sources/com/appboy/lrucache/AppboyLruImageLoader.java:164`
  `return new File(context.getCacheDir().getPath() + File.separator + str);`
- `sources/com/appboy/support/AppboyFileUtils.java:31`
  `deleteFileOrDirectory(new File(file, str));`
- `sources/com/appboy/support/AppboyImageUtils.java:150`
  `File file = new File(path);`
- `sources/com/appboy/ui/inappmessage/BackgroundInAppMessagePreparer.java:195`
  `if (!StringUtils.isNullOrBlank(localAssetsDirectoryUrl) && new File(localAssetsDirectoryUrl).exists()) {`
- `sources/com/appboy/ui/inappmessage/views/AppboyInAppMessageBaseView.java:33`
  `if (new File(localImageUrl).exists()) {`
- `sources/com/appsflyer/internal/AFa1bSDK.java:59`
  `File file = new File(fileAFInAppEventType, "6.10.2");`

## BR028

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:124`
  `android:fullBackupContent="@xml/appsflyer_backup_rules"`

## BR029

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:135`
  `android:exported="true"`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:166`
  `android:exported="true"`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:237`
  `android:exported="true"`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:326`
  `android:exported="true">`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:379`
  `android:exported="true"`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:400`
  `android:exported="true"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:428`
  `android:exported="true"`

## BR030

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:567`
  `android:exported="true"`

## BR031

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:492`
  `android:exported="true">`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:642`
  `android:exported="true"`

## BR032

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:70`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:140`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:155`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:172`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:181`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:190`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:199`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:208`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:217`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:226`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:240`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:328`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:382`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:431`
  `<action android:name="android.intent.action.VIEW"/>`

## BR033

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/androidx/browser/browseractions/BrowserActionsIntent.java:110`
  `return context.getPackageManager().queryIntentActivities(new Intent(ACTION_BROWSER_ACTIONS_OPEN, Uri.parse(TEST_URL)), 131072);`
- `sources/cl/json/social/InstagramShare.java:53`
  `Uri uri = Uri.parse(str);`
- `sources/com/appsflyer/internal/AFd1lSDK.java:76`
  `context.startActivity(new Intent("android.intent.action.VIEW", Uri.parse(aFe1oSDK.AFKeystoreWrapper)).setFlags(268435456));`
- `sources/com/auth0/android/provider/LogoutManager.java:57`
  `Uri.Builder builderBuildUpon = Uri.parse(this.account.getLogoutUrl()).buildUpon();`
- `sources/com/auth0/android/provider/RedirectActivity.java:19`
  `intent.setData(getIntent().getData());`
- `sources/com/auth0/react/RedirectActivity.java:16`
  `intent.setData(getIntent().getData());`
- `sources/com/braintreepayments/api/BraintreeClient.java:245`
  `Uri uri = Uri.parse("https://braintreepayments.com");`
- `sources/com/braintreepayments/api/BraintreeHttpClient.java:106`
  `path = Uri.parse(path).buildUpon().appendQueryParameter(AUTHORIZATION_FINGERPRINT_KEY, ((ClientToken) authorization).getBearer()).toString();`
- `sources/com/braintreepayments/api/PaymentMethodClient.java:144`
  `this.braintreeClient.sendGET(Uri.parse(ApiClient.versionedPath(ApiClient.PAYMENT_METHOD_ENDPOINT)).buildUpon().appendQueryParameter("default_first", String.valueOf(z2)).appendQueryParameter("session_id", this.braintreeClient.getSessionId()).build().toString(), new HttpResponseCallback() { // from cl...`
- `sources/com/braintreepayments/api/PayPalClient.java:70`
  `if (!Uri.parse(str).getLastPathSegment().equals(uri.getLastPathSegment())) {`
- `sources/com/braintreepayments/api/PayPalClient.java:73`
  `String queryParameter = Uri.parse(str2).getQueryParameter(str3);`
- `sources/com/braintreepayments/api/PayPalClient.java:170`
  `this.braintreeClient.startBrowserSwitch(fragmentActivity, new BrowserSwitchOptions().requestCode(13591).url(Uri.parse(payPalResponse.c())).returnUrlScheme(this.braintreeClient.getReturnUrlScheme()).launchAsNewTask(this.braintreeClient.launchesBrowserSwitchAsNewTask()).metadata(jSONObject));`
- `sources/com/braintreepayments/api/PayPalInternalClient.java:63`
  `Uri uri = Uri.parse(strB);`
- `sources/com/braintreepayments/api/UnionPayClient.java:64`
  `UnionPayClient.this.braintreeClient.sendGET(Uri.parse(UnionPayClient.UNIONPAY_CAPABILITIES_PATH).buildUpon().appendQueryParameter("creditCard[number]", str).build().toString(), new HttpResponseCallback() { // from class: com.braintreepayments.api.UnionPayClient.1.1`
- `sources/com/braintreepayments/api/VenmoClient.java:302`
  `intent.setData(Uri.parse("https://play.google.com/store/apps/details?id=com.venmo"));`
- `sources/com/cardinalcommerce/a/getWarnings.java:258`
  `Uri uri = Uri.parse(strOptString3);`
- `sources/com/facebook/react/devsupport/DebugOverlayController.java:58`
  `Intent intent = new Intent("android.settings.action.MANAGE_OVERLAY_PERMISSION", Uri.parse("package:" + context.getPackageName()));`
- `sources/com/facebook/react/modules/intent/IntentModule.java:111`
  `intent.setData(Uri.parse("package:" + packageName));`
- `sources/com/proyecto26/inappbrowser/RNInAppBrowser.java:305`
  `intent.putExtra("android.intent.extra.REFERRER", Uri.parse("android-app://" + context.getApplicationContext().getPackageName()));`
- `sources/com/RNFetchBlob/RNFetchBlob.java:87`
  `getReactApplicationContext().startActivity(new Intent("android.intent.action.VIEW").setDataAndType(Uri.parse(WebContentUtils.FILE_URI_SCHEME_PREFIX + str), str2).setFlags(268435456));`
- `sources/io/branch/referral/BranchStrongMatchHelper.java:88`
  `return Uri.parse(str3 + "&sdk=android5.0.3");`
- `sources/io/branch/referral/validators/DeepLinkRoutingValidator.java:118`
  `Intent intent = new Intent("android.intent.action.VIEW", Uri.parse(str).buildUpon().appendQueryParameter(URI_REDIRECT_KEY, "2").build());`
- `sources/io/branch/rnbranch/RNBranchModule.java:911`
  `intent.setData(Uri.parse(str));`
- `sources/lib/android/paypal/com/magnessdk/p/b.java:191`
  `magnesNetworkingCreateHttpClient.setUri(Uri.parse(strG));`
- `sources/zendesk/messaging/ui/UtilsAttachment.java:61`
  `Uri uri = Uri.parse(str);`

## BR034

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/androidx/browser/customtabs/CustomTabsIntent.java:130`
  `ContextCompat.startActivity(context, this.intent, this.startAnimationBundle);`
- `sources/com/auth0/android/provider/CustomTabsController.java:53`
  `context.startActivity(intentC);`
- `sources/com/auth0/android/provider/RedirectActivity.java:21`
  `startActivity(intent);`
- `sources/com/auth0/react/RedirectActivity.java:18`
  `startActivity(intent);`
- `sources/com/braintreepayments/api/VenmoClient.java:303`
  `fragmentActivity.startActivity(intent);`
- `sources/com/facebook/react/modules/intent/IntentModule.java:115`
  `currentActivity.startActivity(intent);`
- `sources/com/google/mlkit/common/sdkinternal/OptionalModuleUtils.java:262`
  `context.sendBroadcast(intent);`
- `sources/com/onfido/android/sdk/capture/common/permissions/PermissionsManagementFragment.java:103`
  `startActivity(intent);`
- `sources/com/zoontek/rnpermissions/RNPermissionsModule.java:290`
  `reactApplicationContext.startActivity(intent);`
- `sources/io/branch/rnbranch/RNBranchModule.java:913`
  `mActivity.startActivity(intent);`
- `sources/zendesk/messaging/ui/UtilsAttachment.java:66`
  `context.startActivity(intent);`
- `sources/zendesk/messaging/ui/UtilsAttachment.java:71`
  `context.startActivity(intent);`

## BR035

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/com/appboy/ui/AppboyWebViewActivity.java:101`
  `webView.loadUrl(string);`
- `sources/com/appboy/ui/inappmessage/InAppMessageWebViewClient.java:66`
  `webView.loadUrl(JAVASCRIPT_PREFIX + assetFileStringContents);`
- `sources/com/appboy/ui/inappmessage/factories/AppboyHtmlFullViewFactory.java:31`
  `@SuppressLint({"AddJavascriptInterface"})`
- `sources/com/appboy/ui/inappmessage/factories/AppboyHtmlFullViewFactory.java:43`
  `appboyInAppMessageHtmlFullView.getMessageWebView().addJavascriptInterface(appboyInAppMessageHtmlJavascriptInterface, AppboyInAppMessageHtmlBaseView.BRAZE_BRIDGE_PREFIX);`
- `sources/com/appboy/ui/inappmessage/factories/AppboyHtmlViewFactory.java:31`
  `@SuppressLint({"AddJavascriptInterface"})`
- `sources/com/appboy/ui/inappmessage/factories/AppboyHtmlViewFactory.java:43`
  `appboyInAppMessageHtmlView.getMessageWebView().addJavascriptInterface(appboyInAppMessageHtmlJavascriptInterface, AppboyInAppMessageHtmlBaseView.BRAZE_BRIDGE_PREFIX);`
- `sources/com/appboy/ui/inappmessage/views/AppboyInAppMessageHtmlBaseView.java:56`
  `webView.loadUrl(FINISHED_WEBVIEW_URL);`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:634`
  `addJavascriptInterface(c(this), RNCWebViewManager.JAVASCRIPT_INTERFACE);`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:1117`
  `webView.loadUrl(string, map);`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:1123`
  `webView.loadUrl(BLANK_URL);`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:1335`
  `webView.loadUrl(readableArray.getString(0));`
- `sources/com/tealium/internal/dispatcher/WebViewDispatcher.java:96`
  `WebViewDispatcher.this.mWebView.loadUrl("javascript:utag.track('kill_visitor_session', { event: 'kill_visitor_session', 'cp.trace_id' : utag.data['cp.trace_id'] });");`
- `sources/com/tealium/internal/dispatcher/WebViewDispatcher.java:97`
  `WebViewDispatcher.this.mWebView.loadUrl("javascript:document.cookie = 'trace_id=; expires=Thu, 01 Jan 1970 00:00:01 GMT; path=/'");`
- `sources/com/tealium/internal/dispatcher/WebViewDispatcher.java:100`
  `WebViewDispatcher.this.mWebView.loadUrl(String.format(Locale.ROOT, "javascript:document.cookie = 'trace_id=%s; expires=0; path=/';", this.f13493b));`
- `sources/com/tealium/internal/dispatcher/WebViewDispatcher.java:161`
  `WebViewDispatcher.this.mWebView.loadUrl(this.f13497a);`
- `sources/com/tealium/internal/dispatcher/WebViewDispatcher.java:181`
  `this.f13500a.loadUrl("javascript:(function(){\n    var payload = {};\n    try {\n        var ts = new RegExp(\"ut[0-9]+\\.[0-9]+\\.[0-9]{12}\").exec(document.childNodes[0].textContent)[0];\n        ts = ts.substring(ts.length - 12, ts.length);\n        var y = ts.substring(0, 4);\n        var mo = t...`
- `sources/com/tealium/internal/dispatcher/WebViewDispatcher.java:422`
  `this.mWebView.loadUrl(str);`
- `sources/io/branch/referral/BranchViewHandler.java:204`
  `webView2.loadUrl(str);`

## BR040

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `sources/com/appsflyer/internal/AFa1eSDK.java:51`
  `parcelObtain.writeInterfaceToken("com.google.android.gms.ads.identifier.internal.IAdvertisingIdService");`
- `sources/com/appsflyer/internal/AFa1eSDK.java:65`
  `parcelObtain.writeInterfaceToken("com.google.android.gms.ads.identifier.internal.IAdvertisingIdService");`
- `sources/com/appsflyer/internal/AFa1eSDK.java:114`
  `Intent intent = new Intent("com.google.android.gms.ads.identifier.service.START");`
- `sources/com/bumptech/glide/ListPreloader.java:33`
  `RequestBuilder<?> getPreloadRequestBuilder(@NonNull U u2);`
- `sources/com/bumptech/glide/ListPreloader.java:162`
  `RequestBuilder<?> preloadRequestBuilder;`
- `sources/com/bumptech/glide/ListPreloader.java:163`
  `if (t2 == null || (preloadSize = this.preloadDimensionProvider.getPreloadSize(t2, i2, i3)) == null || (preloadRequestBuilder = this.preloadModelProvider.getPreloadRequestBuilder(t2)) == null) {`
- `sources/com/bumptech/glide/ListPreloader.java:166`
  `preloadRequestBuilder.into(this.preloadTargetQueue.next(preloadSize[0], preloadSize[1]));`
- `sources/com/dieam/reactnativepushnotification/modules/RNPushNotificationPicturesAggregator.java:34`
  `private void downloadRequest(Context context, Uri uri, BaseBitmapDataSubscriber baseBitmapDataSubscriber) {`
- `sources/com/dieam/reactnativepushnotification/modules/RNPushNotificationPicturesAggregator.java:62`
  `downloadRequest(context, Uri.parse(str), new BaseBitmapDataSubscriber() { // from class: com.dieam.reactnativepushnotification.modules.RNPushNotificationPicturesAggregator.1`
- `sources/com/dieam/reactnativepushnotification/modules/RNPushNotificationPicturesAggregator.java:90`
  `downloadRequest(context, Uri.parse(str), new BaseBitmapDataSubscriber() { // from class: com.dieam.reactnativepushnotification.modules.RNPushNotificationPicturesAggregator.2`
- `sources/com/onfido/android/sdk/capture/network/OnfidoApiService.java:71`
  `@Metadata(d1 = {"\u0000ð\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u00...`
- `sources/com/onfido/android/sdk/capture/network/OnfidoApiService.java:737`
  `private Completable mediaUploadRequestWrapper(Completable request) {`
- `sources/com/onfido/android/sdk/capture/network/OnfidoApiService.java:740`
  `Completable completableIgnoreElement = mediaUploadRequestWrapper(singleDefault).ignoreElement();`
- `sources/com/onfido/android/sdk/capture/network/OnfidoApiService.java:741`
  `Intrinsics.checkNotNullExpressionValue(completableIgnoreElement, "mediaUploadRequestWrappe…lt(Unit)).ignoreElement()");`
- `sources/com/onfido/android/sdk/capture/network/OnfidoApiService.java:745`
  `private <T> Single<T> mediaUploadRequestWrapper(Single<T> single) {`
- `sources/com/onfido/android/sdk/capture/network/OnfidoApiService.java:958`
  `return mediaUploadRequestWrapper(singleUploadDocumentMedia);`
- `sources/com/onfido/android/sdk/capture/network/OnfidoApiService.java:968`
  `return mediaUploadRequestWrapper(completableUploadDocumentVideo);`
- `sources/com/onfido/android/sdk/capture/network/OnfidoApiService.java:981`
  `Observable<LiveVideoUpload> observable = mediaUploadRequestWrapper(singleUploadLiveVideo).toObservable();`
- `sources/com/onfido/android/sdk/capture/network/OnfidoApiService.java:982`
  `Intrinsics.checkNotNullExpressionValue(observable, "mediaUploadRequestWrappe…         ).toObservable()");`
- `sources/com/onfido/android/sdk/capture/network/OnfidoApiService.java:991`
  `return mediaUploadRequestWrapper(singlePoaUpload);`
- `sources/com/onfido/android/sdk/capture/ui/camera/document/liveness/DocumentLivenessService.java:44`
  `@Metadata(d1 = {"\u0000\u0086\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0...`
- `sources/com/onfido/android/sdk/capture/ui/camera/document/liveness/DocumentLivenessService.java:75`
  `private final Single<DocumentMediaUploadResponse> binaryUploadRequest(File imageFile, String fileType, DocumentMediaType mediaType, DocSide docSide, DocumentType docType) {`
- `sources/com/onfido/android/sdk/capture/ui/camera/document/liveness/DocumentLivenessService.java:117`
  `Single<DocumentMediaUploadResponse> singleDoOnSuccess = binaryUploadRequest(fileFindFileByPrefix, "image/*", DocumentMediaType.DOCUMENT_PHOTO, DocSide.FRONT, docType).doOnSuccess(new Consumer() { // from class: com.onfido.android.sdk.capture.ui.camera.document.liveness.c`
- `sources/com/onfido/android/sdk/capture/ui/camera/document/liveness/DocumentLivenessService.java:123`
  `Intrinsics.checkNotNullExpressionValue(singleDoOnSuccess, "binaryUploadRequest(\n   …rontSide = it.mediaId() }");`
- `sources/com/onfido/android/sdk/capture/ui/camera/document/liveness/DocumentLivenessService.java:127`
  `Single<DocumentMediaUploadResponse> singleDoOnSuccess2 = binaryUploadRequest(fileFindFileByPrefix2, "image/*", DocumentMediaType.DOCUMENT_PHOTO, DocSide.BACK, docType).doOnSuccess(new Consumer() { // from class: com.onfido.android.sdk.capture.ui.camera.document.liveness.d`
- `sources/com/onfido/android/sdk/capture/ui/camera/document/liveness/DocumentLivenessService.java:133`
  `Intrinsics.checkNotNullExpressionValue(singleDoOnSuccess2, "binaryUploadRequest(\n   …backSide = it.mediaId() }");`
- `sources/com/onfido/android/sdk/capture/ui/camera/document/liveness/DocumentLivenessService.java:137`
  `Single<DocumentMediaUploadResponse> singleDoOnSuccess3 = binaryUploadRequest(fileFindFileByPrefix3, LivenessConfirmationPresenter.MP4_MIME, DocumentMediaType.DOCUMENT_LIVENESS_VIDEO, null, docType).doOnSuccess(new Consumer() { // from class: com.onfido.android.sdk.capture.ui.camera.document.liveness...`
- `sources/com/onfido/android/sdk/capture/ui/camera/document/liveness/DocumentLivenessService.java:143`
  `Intrinsics.checkNotNullExpressionValue(singleDoOnSuccess3, "binaryUploadRequest(\n   …se.video = it.mediaId() }");`
- `sources/com/onfido/android/sdk/capture/ui/camera/document/liveness/DocumentLivenessService.java:216`
  `private final void onFilesUploadRequestCompleted(DocumentLivenessResponse fileUploadResult) {`
- `sources/com/onfido/android/sdk/capture/ui/camera/document/liveness/DocumentLivenessService.java:223`
  `private final void onFilesUploadRequestFailed(Throwable throwable) {`
- `sources/com/onfido/android/sdk/capture/ui/camera/document/liveness/DocumentLivenessService.java:249`
  `this$0.onFilesUploadRequestCompleted(documentLivenessResponse);`
- `sources/com/onfido/android/sdk/capture/ui/camera/document/liveness/DocumentLivenessService.java:257`
  `this$0.onFilesUploadRequestFailed(it);`
- `sources/com/onfido/android/sdk/capture/ui/camera/liveness/LivenessConfirmationPresenter.java:63`
  `@Metadata(d1 = {"\u0000¨\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u...`
- `sources/com/onfido/android/sdk/capture/ui/camera/liveness/LivenessConfirmationPresenter.java:102`
  `@Metadata(d1 = {"\u0000@\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\u0012\n\u0002\b\u0002\n\u0002\u0010\u0011\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\t\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u001a\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010\b\n\u...`
- `sources/com/onfido/android/sdk/capture/ui/camera/liveness/LivenessConfirmationPresenter.java:103`
  `private static final /* data */ class LiveVideoUploadRequestParams {`
- `sources/com/onfido/android/sdk/capture/ui/camera/liveness/LivenessConfirmationPresenter.java:124`
  `public LiveVideoUploadRequestParams(@NotNull String videoFileName, @NotNull byte[] videoFileBytes, @NotNull String challengesId, @NotNull Challenge[] challenges, long j2, @NotNull LiveVideoLanguage[] sdkLanguages, @NotNull String videoFileType) {`
- `sources/com/onfido/android/sdk/capture/ui/camera/liveness/LivenessConfirmationPresenter.java:140`
  `public /* synthetic */ LiveVideoUploadRequestParams(String str, byte[] bArr, String str2, Challenge[] challengeArr, long j2, LiveVideoLanguage[] liveVideoLanguageArr, String str3, int i2, DefaultConstructorMarker defaultConstructorMarker) {`
- `sources/com/onfido/android/sdk/capture/ui/camera/liveness/LivenessConfirmationPresenter.java:186`
  `public final LiveVideoUploadRequestParams copy(@NotNull String videoFileName, @NotNull byte[] videoFileBytes, @NotNull String challengesId, @NotNull Challenge[] challenges, long endChallengeTimestamp, @NotNull LiveVideoLanguage[] sdkLanguages, @NotNull String videoFileType) {`
- `sources/com/onfido/android/sdk/capture/ui/camera/liveness/LivenessConfirmationPresenter.java:193`
  `return new LiveVideoUploadRequestParams(videoFileName, videoFileBytes, challengesId, challenges, endChallengeTimestamp, sdkLanguages, videoFileType);`
- `sources/com/onfido/android/sdk/capture/ui/camera/liveness/LivenessConfirmationPresenter.java:200`
  `if (!(other instanceof LiveVideoUploadRequestParams)) {`
- `sources/com/onfido/android/sdk/capture/ui/camera/liveness/LivenessConfirmationPresenter.java:203`
  `LiveVideoUploadRequestParams liveVideoUploadRequestParams = (LiveVideoUploadRequestParams) other;`
- `sources/com/onfido/android/sdk/capture/ui/camera/liveness/LivenessConfirmationPresenter.java:204`
  `return Intrinsics.areEqual(this.videoFileName, liveVideoUploadRequestParams.videoFileName) && Intrinsics.areEqual(this.videoFileBytes, liveVideoUploadRequestParams.videoFileBytes) && Intrinsics.areEqual(this.challengesId, liveVideoUploadRequestParams.challengesId) && Intrinsics.areEqual(this.challen...`
- `sources/com/onfido/android/sdk/capture/ui/camera/liveness/LivenessConfirmationPresenter.java:247`
  `return "LiveVideoUploadRequestParams(videoFileName=" + this.videoFileName + ", videoFileBytes=" + Arrays.toString(this.videoFileBytes) + ", challengesId=" + this.challengesId + ", challenges=" + Arrays.toString(this.challenges) + ", endChallengeTimestamp=" + this.endChallengeTimestamp + ", sdkLangua...`
- `sources/com/onfido/android/sdk/capture/ui/camera/liveness/LivenessConfirmationPresenter.java:497`
  `private LiveVideoUploadRequestParams prepareRequestParams(LivenessPerformedChallenges performedChallenges, File videoFile) {`
- `sources/com/onfido/android/sdk/capture/ui/camera/liveness/LivenessConfirmationPresenter.java:505`
  `return new LiveVideoUploadRequestParams(videoFileName, bytes, id, challengeArrMapChallenges, endChallengeTimestamp, liveVideoLanguageArr, null, 64, null);`
- `sources/com/onfido/android/sdk/capture/ui/camera/liveness/LivenessConfirmationPresenter.java:524`
  `private Observable<LiveVideoUpload> videoUploadRequest(LiveVideoUploadRequestParams params) {`
- `sources/com/onfido/android/sdk/capture/ui/camera/liveness/LivenessConfirmationPresenter.java:720`
  `Observable<LiveVideoUpload> observableVideoUploadRequest = videoUploadRequest(prepareRequestParams(performedChallenges, file));`
- `sources/com/onfido/android/sdk/capture/ui/camera/liveness/LivenessConfirmationPresenter.java:722`
  `Disposable disposableSubscribe = observableVideoUploadRequest.subscribeOn(this.schedulersProvider.getIo()).observeOn(this.schedulersProvider.getUi()).subscribe(new Consumer() { // from class: com.onfido.android.sdk.capture.ui.camera.liveness.l`
- `sources/com/onfido/android/sdk/capture/ui/camera/liveness/LivenessConfirmationPresenter.java:733`
  `Intrinsics.checkNotNullExpressionValue(disposableSubscribe, "videoUploadRequest\n     …able) }\n                )");`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:1286`
  `module.setDownloadRequest(request);`
- `sources/com/reactnativecommunity/webview/RNCWebViewModule.java:45`
  `private DownloadManager.Request downloadRequest;`
- `sources/com/reactnativecommunity/webview/RNCWebViewModule.java:344`
  `} else if (RNCWebViewModule.this.downloadRequest != null) {`
- `sources/com/reactnativecommunity/webview/RNCWebViewModule.java:363`
  `((DownloadManager) getCurrentActivity().getBaseContext().getSystemService("download")).enqueue(this.downloadRequest);`
- `sources/com/reactnativecommunity/webview/RNCWebViewModule.java:467`
  `public void setDownloadRequest(DownloadManager.Request request) {`
- `sources/com/reactnativecommunity/webview/RNCWebViewModule.java:468`
  `this.downloadRequest = request;`
- `sources/com/tealium/adidentifier/AdIdentifier.java:5`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/tealium/internal/NetworkRequestBuilder.java:177`
  `public static NetworkRequestBuilder createHeadRequest(String str) {`
- `sources/com/tealium/internal/dispatcher/WebViewDispatcher.java:400`
  `this.mMessageRouter.a(NetworkRequestBuilder.createHeadRequest(this.mUrl).addHeader(HttpHeaders.ACCEPT_ENCODING, ProxyConfig.MATCH_ALL_SCHEMES).addHeader(HttpHeaders.IF_MODIFIED_SINCE, this.mIfModifiedFormat.format(new Date(this.mLastPublishURLLoad))).setListener(createHeadRequestResponseListener(and...`
- `sources/com/tealium/internal/dispatcher/WebViewDispatcher.java:436`
  `private NetworkRequestBuilder.HttpResponseListener createHeadRequestResponseListener(int i2) {`
- `sources/com/tealium/library/g.java:184`
  `this.f13679c.a(NetworkRequestBuilder.createHeadRequest(this.f13678b).setListener(this).addHeader(HttpHeaders.IF_MODIFIED_SINCE, this.f13682f.format(new Date(this.f13686j))).createRunnable());`
- `sources/io/branch/referral/GAdsPrefetchTask.java:29`
  `return Class.forName("com.google.android.gms.ads.identifier.AdvertisingIdClient").getMethod("getAdvertisingIdInfo", Context.class).invoke(null, context);`
- `sources/io/branch/referral/GAdsPrefetchTask.java:31`
  `PrefHelper.Debug("Either class com.google.android.gms.ads.identifier.AdvertisingIdClient or its method, getAdvertisingIdInfo, was not found");`

## BR041

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `sources/com/google/firebase/analytics/connector/AnalyticsConnector.java:1`
  `package com.google.firebase.analytics.connector;`
- `sources/com/google/firebase/analytics/connector/R.java:1`
  `package com.google.firebase.analytics.connector;`
- `sources/com/google/firebase/messaging/MessagingAnalytics.java:20`
  `import com.google.firebase.analytics.connector.AnalyticsConnector;`

## BR042

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:67`
  `<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>`
- `sources/com/onfido/android/sdk/capture/ui/camera/CaptureActivity.java:203`
  `private static final String UPLOAD_ID = "upload_id";`
- `sources/com/tealium/adidentifier/AdIdentifier.java:5`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/io/branch/referral/Defines.java:110`
  `FireAdId("fire_ad_id"),`
- `sources/io/branch/referral/GAdsPrefetchTask.java:29`
  `return Class.forName("com.google.android.gms.ads.identifier.AdvertisingIdClient").getMethod("getAdvertisingIdInfo", Context.class).invoke(null, context);`
- `sources/io/branch/referral/GAdsPrefetchTask.java:31`
  `PrefHelper.Debug("Either class com.google.android.gms.ads.identifier.AdvertisingIdClient or its method, getAdvertisingIdInfo, was not found");`
- `sources/io/branch/referral/GAdsPrefetchTask.java:37`
  `public void setGAIDWithAdvertisingIdClient(@NonNull SystemObserver systemObserver, Object obj) {`
- `sources/io/branch/referral/GAdsPrefetchTask.java:45`
  `public void setGoogleLATWithAdvertisingIdClient(@NonNull SystemObserver systemObserver, Object obj) {`
- `sources/io/branch/referral/GAdsPrefetchTask.java:74`
  `GAdsPrefetchTask.this.setGoogleLATWithAdvertisingIdClient(systemObserverB, adInfoObject);`
- `sources/io/branch/referral/GAdsPrefetchTask.java:78`
  `GAdsPrefetchTask.this.setGAIDWithAdvertisingIdClient(systemObserverB, adInfoObject);`
- `sources/io/branch/referral/HuaweiOAIDFetchTask.java:27`
  `Object objInvoke = Class.forName("com.huawei.hms.ads.identifier.AdvertisingIdClient").getDeclaredMethod("getAdvertisingIdInfo", Context.class).invoke(null, context);`

## BR043

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/lib/android/paypal/com/magnessdk/i.java:17`
  `import android.net.wifi.ScanResult;`
- `sources/lib/android/paypal/com/magnessdk/i.java:225`
  `List<ScanResult> scanResults = wifiManager.getScanResults();`
- `sources/lib/android/paypal/com/magnessdk/i.java:226`
  `if (scanResults != null && scanResults.size() != 0) {`
- `sources/lib/android/paypal/com/magnessdk/i.java:231`
  `for (int i5 = 0; i5 < scanResults.size(); i5++) {`
- `sources/lib/android/paypal/com/magnessdk/i.java:232`
  `if (!bssid.equals(scanResults.get(i5).BSSID) && i3 < (i2 = scanResults.get(i5).level)) {`
- `sources/lib/android/paypal/com/magnessdk/i.java:239`
  `arrayList.add(scanResults.get(i4).BSSID);`

## BR044

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/androidx/core/content/ContextCompat.java:43`
  `import android.net.wifi.WifiManager;`
- `sources/androidx/core/content/ContextCompat.java:318`
  `map.put(WifiManager.class, "wifi");`
- `sources/com/cardinalcommerce/a/setCompoundDrawablesWithIntrinsicBounds.java:5`
  `import android.net.wifi.WifiManager;`
- `sources/com/cardinalcommerce/a/setCompoundDrawablesWithIntrinsicBounds.java:163`
  `WifiManager wifiManager = (WifiManager) context.getApplicationContext().getSystemService("wifi");`
- `sources/com/cardinalcommerce/a/setCompoundDrawablesWithIntrinsicBounds.java:165`
  `if ((wifiManager != null ? 'T' : ' ') == 'T') {`
- `sources/com/cardinalcommerce/a/setCompoundDrawablesWithIntrinsicBounds.java:169`
  `connectionInfo = wifiManager.getConnectionInfo();`
- `sources/com/cardinalcommerce/a/setCompoundDrawablesWithIntrinsicBounds.java:181`
  `this.Cardinal = wifiManager.is5GHzBandSupported();`
- `sources/com/cardinalcommerce/a/setCompoundDrawablesWithIntrinsicBounds.java:182`
  `this.cleanup = wifiManager.isDeviceToApRttSupported();`
- `sources/com/cardinalcommerce/a/setCompoundDrawablesWithIntrinsicBounds.java:183`
  `this.getSDKVersion = wifiManager.isEnhancedPowerReportingSupported();`
- `sources/com/cardinalcommerce/a/setCompoundDrawablesWithIntrinsicBounds.java:184`
  `this.getWarnings = wifiManager.isP2pSupported();`
- `sources/com/cardinalcommerce/a/setCompoundDrawablesWithIntrinsicBounds.java:185`
  `this.CardinalError = wifiManager.isPreferredNetworkOffloadSupported();`
- `sources/com/cardinalcommerce/a/setCompoundDrawablesWithIntrinsicBounds.java:186`
  `this.values = wifiManager.isTdlsSupported();`
- `sources/com/cardinalcommerce/a/setCompoundDrawablesWithIntrinsicBounds.java:187`
  `this.CardinalActionCode = wifiManager.isScanAlwaysAvailable();`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:18`
  `import android.net.wifi.WifiManager;`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:128`
  `WifiManager wifiManager = (WifiManager) getReactApplicationContext().getApplicationContext().getSystemService("wifi");`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:129`
  `if (wifiManager != null) {`
- `sources/com/learnium/RNDeviceInfo/RNDeviceModule.java:130`
  `return wifiManager.getConnectionInfo();`
- `sources/com/reactnativecommunity/netinfo/ConnectivityReceiver.java:5`
  `import android.net.wifi.WifiManager;`
- `sources/com/reactnativecommunity/netinfo/ConnectivityReceiver.java:35`
  `private final WifiManager mWifiManager;`
- `sources/com/reactnativecommunity/netinfo/ConnectivityReceiver.java:48`
  `this.mWifiManager = (WifiManager) reactApplicationContext.getApplicationContext().getSystemService("wifi");`
- `sources/com/reactnativecommunity/netinfo/ConnectivityReceiver.java:56`
  `WifiManager wifiManager;`
- `sources/com/reactnativecommunity/netinfo/ConnectivityReceiver.java:91`
  `if (NetInfoUtils.isAccessWifiStatePermissionGranted(c()) && (wifiManager = this.mWifiManager) != null && (connectionInfo = wifiManager.getConnectionInfo()) != null) {`
- `sources/com/reactnativecommunity/netinfo/ConnectivityReceiver.java:109`
  `writableMapCreateMap.putInt("strength", WifiManager.calculateSignalLevel(connectionInfo.getRssi(), 100));`
- `sources/com/reactnativecommunity/netinfo/ConnectivityReceiver.java:180`
  `WifiManager wifiManager = this.mWifiManager;`
- `sources/com/reactnativecommunity/netinfo/ConnectivityReceiver.java:181`
  `writableMapCreateMap.putBoolean("isWifiEnabled", wifiManager != null ? wifiManager.isWifiEnabled() : false);`
- `sources/lib/android/paypal/com/magnessdk/h.java:14`
  `import android.net.wifi.WifiManager;`
- `sources/lib/android/paypal/com/magnessdk/h.java:611`
  `WifiInfo connectionInfo = n(context, "android.permission.ACCESS_WIFI_STATE") ? ((WifiManager) context.getApplicationContext().getSystemService("wifi")).getConnectionInfo() : null;`
- `sources/lib/android/paypal/com/magnessdk/i.java:19`
  `import android.net.wifi.WifiManager;`
- `sources/lib/android/paypal/com/magnessdk/i.java:84`
  `private WifiManager L2;`
- `sources/lib/android/paypal/com/magnessdk/i.java:219`
  `private ArrayList<String> a(WifiManager wifiManager) {`
- `sources/lib/android/paypal/com/magnessdk/i.java:221`
  `if (wifiManager == null) {`
- `sources/lib/android/paypal/com/magnessdk/i.java:225`
  `List<ScanResult> scanResults = wifiManager.getScanResults();`
- `sources/lib/android/paypal/com/magnessdk/i.java:228`
  `String bssid = wifiManager.getConnectionInfo().getBSSID();`
- `sources/lib/android/paypal/com/magnessdk/i.java:738`
  `this.L2 = (WifiManager) context.getApplicationContext().getSystemService("wifi");`
- `sources/lib/android/paypal/com/magnessdk/i.java:762`
  `WifiManager wifiManager = this.L2;`
- `sources/lib/android/paypal/com/magnessdk/i.java:763`
  `if (wifiManager != null) {`
- `sources/lib/android/paypal/com/magnessdk/i.java:764`
  `this.E2 = this.z2 ? wifiManager.getConnectionInfo() : null;`
- `sources/org/otwebrtc/NetworkMonitorAutoDetect.java:46`
  `private WifiManagerDelegate wifiManagerDelegate;`
- `sources/org/otwebrtc/NetworkMonitorAutoDetect.java:430`
  `static class WifiManagerDelegate {`
- `sources/org/otwebrtc/NetworkMonitorAutoDetect.java:435`
  `WifiManagerDelegate() {`
- `sources/org/otwebrtc/NetworkMonitorAutoDetect.java:439`
  `WifiManagerDelegate(Context context) {`
- `sources/org/otwebrtc/NetworkMonitorAutoDetect.java:456`
  `this.wifiManagerDelegate = new WifiManagerDelegate(context);`
- `sources/org/otwebrtc/NetworkMonitorAutoDetect.java:542`
  `return getConnectionType(networkState) != ConnectionType.CONNECTION_WIFI ? "" : this.wifiManagerDelegate.getWifiSSID();`
- `sources/org/otwebrtc/NetworkMonitorAutoDetect.java:620`
  `void setWifiManagerDelegateForTests(WifiManagerDelegate wifiManagerDelegate) {`
- `sources/org/otwebrtc/NetworkMonitorAutoDetect.java:621`
  `this.wifiManagerDelegate = wifiManagerDelegate;`

## BR047

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/android/support/v4/media/MediaBrowserCompat.java:88`
  `Log.w("MediaBrowserCompat", "Unhandled message: " + message + "\n  Client version: 1\n  Service version: " + message.arg1);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:97`
  `Log.e("MediaBrowserCompat", "Could not unparcel the data.");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:208`
  `Log.w("MediaBrowserCompat", "Unknown result code: " + i2 + " (extras=" + this.mExtras + ", resultData=" + bundle + ")");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:557`
  `Log.i("MediaBrowserCompat", "The connected service doesn't support sendCustomAction.");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:570`
  `Log.i("MediaBrowserCompat", "Remote error sending a custom action: action=" + str + ", extras=" + bundle, e2);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:871`
  `Log.d("MediaBrowserCompat", "  mServiceBinderWrapper=" + this.f52h);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:872`
  `Log.d("MediaBrowserCompat", "  mCallbacksMessenger=" + this.f53i);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:873`
  `Log.d("MediaBrowserCompat", "  mRootId=" + this.mRootId);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:874`
  `Log.d("MediaBrowserCompat", "  mMediaSessionToken=" + this.mMediaSessionToken);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1100`
  `Log.w("MediaBrowserCompat", "onConnect from service while mState=" + getStateLabel(this.f50f) + "... ignoring");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1154`
  `Log.i("MediaBrowserCompat", "Remote error sending a custom action: action=" + str + ", extras=" + bundle, e2);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:828`
  `Log.e("MediaControllerCompat", "Dead object in sendCustomAction.", e2);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:837`
  `Log.e("MediaControllerCompat", "Dead object in setRating.", e2);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:853`
  `Log.w("MediaControllerCompat", "Failed to create MediaControllerImpl.", e2);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:884`
  `Log.e("MediaControllerCompat", "Dead object in getMediaController.", e2);`
- `sources/androidx/activity/result/ActivityResultRegistry.java:128`
  `Log.w(LOG_TAG, "Dropping pending result for request " + str + ": " + this.f220d.get(str));`
- `sources/androidx/activity/result/ActivityResultRegistry.java:132`
  `Log.w(LOG_TAG, "Dropping pending result for request " + str + ": " + this.f221e.getParcelable(str));`
- `sources/androidx/appcompat/app/ActionBarDrawerToggle.java:191`
  `Log.w("ActionBarDrawerToggle", "DrawerToggle may not show up because NavigationIcon is not visible. You may need to call actionbar.setDisplayHomeAsUpEnabled(true);");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1218`
  `Log.d("AppCompatDelegate", "Exception while getting ActivityInfo", e2);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1553`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1559`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR_OVERLAY id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2213`
  `Log.i("AppCompatDelegate", "Failed to instantiate custom view inflater " + string + ". Falling back to default.", th);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2300`
  `Log.i("AppCompatDelegate", "The Activity's LayoutInflater already has a Factory installed so we can not install AppCompat's");`
- `sources/androidx/appcompat/app/ResourcesFlusher.java:188`
  `Log.e(TAG, "Could not retrieve value from ThemedResourceCache#mUnthemedEntries", e4);`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:150`
  `Log.w("SupportMenuInflater", "Cannot instantiate class: " + str, e2);`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:183`
  `Log.w("SupportMenuInflater", "Ignoring attribute 'itemActionViewLayout'. Action view already specified.");`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:264`
  `Log.w("SupportMenuInflater", "Ignoring attribute 'actionProviderClass'. Action view already specified.");`
- `sources/androidx/appcompat/view/menu/MenuItemImpl.java:360`
  `Log.e(TAG, "Can't find activity to handle intent; ignoring", e2);`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:64`
  `Log.e("AsldcInflateDelegate", "Exception while inflating <animated-selector>", e2);`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:79`
  `Log.e("AvdcInflateDelegate", "Exception while inflating <animated-vector>", e2);`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:116`
  `Log.e("DrawableDelegate", "Exception while inflating <drawable>", e2);`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:152`
  `Log.e("VdcInflateDelegate", "Exception while inflating <vector>", e2);`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:366`
  `Log.e(TAG, "Exception while inflating drawable", e2);`
- `sources/androidx/appcompat/widget/SuggestionsAdapter.java:118`
  `Log.w(LOG_TAG, "Invalid icon resource " + iconResource + " for " + componentName.flattenToShortString());`
- `sources/androidx/appcompat/widget/SuggestionsAdapter.java:121`
  `Log.w(LOG_TAG, e2.toString());`
- `sources/androidx/appcompat/widget/SuggestionsAdapter.java:172`
  `Log.w(LOG_TAG, "Icon not found: " + uri + ", " + e3.getMessage());`
- `sources/androidx/appcompat/widget/SuggestionsAdapter.java:175`
  `Log.w(LOG_TAG, "Icon not found: " + uri + ", " + e3.getMessage());`
- `sources/androidx/asynclayoutinflater/view/AsyncLayoutInflater.java:145`
  `Log.w(AsyncLayoutInflater.TAG, "Failed to inflate resource in the background! Retrying on the UI thread", e2);`
- `sources/androidx/asynclayoutinflater/view/AsyncLayoutInflater.java:149`
  `Log.w(AsyncLayoutInflater.TAG, e3);`
- `sources/androidx/biometric/BiometricFragment.java:346`
  `Log.v(TAG, "Error not sent to client. User is confirming their device credential.");`

## BR050

paper_id: B021
paper_title: Metadata-Based Privacy Assessment for Mobile mHealth

- `audit_reports/01_evidence_chain.md:163`
  `## 4. 网络、URL 与 cleartext policy 证据链`
- `audit_reports/02_rule_by_rule_mapping.md:12`
  `| BR005 | supported_hypothesis | B021 / Metadata-Based Privacy Assessment for Android Apps | 论文使用应用元数据与实际权限/数据行为之间的不一致来评估隐私风险。 | 当前项目没有商店元数据全文；从 APK 名称/业务看是健康问诊类 App，权限覆盖相机、麦克风、位置、日历、存储、READ_PHONE_STATE、AD_ID、Bluetooth。由于缺少 store description 与政策全文，只能作为元数据-权限不一致的待验证假设。 |`
- `audit_reports/02_rule_by_rule_mapping.md:13`
  `| BR006 | confirmed | B016 / A privacy and security analysis of Android COVID-19 contact tracing apps | 论文把明文传输/静态安全配置作为 Android 安全问题。 | 'AndroidManifest.xml:125' 设置 'usesCleartextTraffic="true"'，且未发现 NSC。确认 cleartext policy 过宽；不确认敏感 HTTP 传输。 |`
- `audit_reports/02_rule_by_rule_mapping.md:49`
  `| BR050 | not_testable | B005 / Mobile health and privacy: cross sectional study | 隐私政策应披露数据接收方和跟踪。 | APK 中有隐私 URL，但未联网核验当前政策全文，也无抓包接收方列表。 |`
- `audit_reports/02_rule_by_rule_mapping.md:50`
  `| BR051 | not_testable | B012 / Privacy policies of Android apps for depression | 心理健康 App 应清晰披露敏感数据使用。 | 发现心理健康数据表面，但未核验政策全文。 |`
- `audit_reports/02_rule_by_rule_mapping.md:51`
  `| BR052 | not_testable | B013 / Privacy policies of mHealth apps | mHealth 隐私政策可用性/内容需要检查。 | 本地 APK 只提供 URL/文案，未获取当前政策。 |`
- `audit_reports/02_rule_by_rule_mapping.md:52`
  `| BR055 | confirmed | B014 / Privacy Assessment in Mobile Health Apps | mHealth 隐私评估应组织多层证据。 | 本审计按 Manifest、代码、资源、存储、网络、动态缺口、云端假设组织。 |`
- `audit_reports/02_rule_by_rule_mapping.md:53`
  `| BR058 | confirmed | B014 / Privacy Assessment in Mobile Health Apps | 评估应区分一方代码与三方 SDK。 | 报告中将 'com.babylon.cyrus' 与 Branch/AppsFlyer/Braze/Auth0/Braintree/Onfido 等分开。 |`
- `audit_reports/02_rule_by_rule_mapping.md:55`
  `| BR060 | supported_hypothesis | B016 / A privacy and security analysis of Android COVID-19 contact tracing apps | 环境/baseUrl/channel flag 可导致后端切换风险。 | bundle 内含 prod/preprod/dev/local host 和 release config；未证明攻击者可切换。 |`
- `audit_reports/03_final_audit_report.md:40`
  `- confirmed 只用于静态 artifact 自身即可证明的事实，例如 Manifest cleartext policy、exported 组件、硬编码 key 存在、代码级数据流。`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_en_ca.json:1`
  `{"chat-exp.about_your_results_content":"The possible causes are those that the Babylon algorithm suggests as most likely, given the answers you entered. They are listed in the order of their match to your answers and how common the causes are. The order is not an indication of your individual likeli...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_en_ca__partnertelus.json:1`
  `{"account_details.county":"Province","account_details.phn_why_subtitle":"Your Medical ID (Health card number) may be required to facilitate prescriptions, labs, imaging requisitions and specialist referrals. By entering your Medical ID the cost of your appointment could be covered by your provincial...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_en_gb.json:1`
  `{"chat-exp.about_your_results_content":"The possible causes are those that the Babylon algorithm suggests as most likely, given the answers you entered. They are listed in the order of their match to your answers and how common the causes are. The order is not an indication of your individual likeli...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_en_gb__partnerbupa.json:1`
  `{"appointments.checkin.window":"If you can't attend, please cancel as soon as possible to free your slot for another patient.","appointments.referraldetailfaqurl":"https://www.bupa.co.uk/help-and-support/blua/prescriptions-and-referrals/referrals","global.applicationName":"Bupa Blua Health","global....`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_en_us.json:1`
  `{"chat-exp.about_your_results_content":"The possible causes are those that the Babylon algorithm suggests as most likely, given the answers you entered. They are listed in the order of their match to your answers and how common the causes are. The order is not an indication of your individual likeli...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_es_us.json:1`
  `{"chat-exp.about_your_results_content":"Las posibles causas son afecciones que pueden estar relacionadas con los síntomas y factores de riesgo ingresados por el usuario.\n\nLas afecciones presentadas a un usuario se enumeran en el orden en que las afecciones coinciden con los síntomas y los factores...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_fr_ca.json:1`
  `{"chat-exp.about_your_results_content":"Les causes possibles sont celles que l'algorithme de Babylon considère les plus probables d'après les réponses que vous avez fournies. Elles sont répertoriées dans leur ordre de correspondance avec vos réponses et de leur fréquence. Cependant, cet ordre n'est ...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_fr_ca__partnertelus.json:1`
  `{"account_details.county":"Province","account_details.phn_why_subtitle":"Votre identifiant médical (numéro de carte d'assurance maladie) peut être requis pour faciliter les ordonnances, les analyses de laboratoire, les demandes d'imagerie et les références aux spécialistes. En saisissant votre ident...`

## BR051

paper_id: B013
paper_title: Availability and quality of mobile health app privacy policies

- `audit_reports/02_rule_by_rule_mapping.md:12`
  `| BR005 | supported_hypothesis | B021 / Metadata-Based Privacy Assessment for Android Apps | 论文使用应用元数据与实际权限/数据行为之间的不一致来评估隐私风险。 | 当前项目没有商店元数据全文；从 APK 名称/业务看是健康问诊类 App，权限覆盖相机、麦克风、位置、日历、存储、READ_PHONE_STATE、AD_ID、Bluetooth。由于缺少 store description 与政策全文，只能作为元数据-权限不一致的待验证假设。 |`
- `audit_reports/02_rule_by_rule_mapping.md:13`
  `| BR006 | confirmed | B016 / A privacy and security analysis of Android COVID-19 contact tracing apps | 论文把明文传输/静态安全配置作为 Android 安全问题。 | 'AndroidManifest.xml:125' 设置 'usesCleartextTraffic="true"'，且未发现 NSC。确认 cleartext policy 过宽；不确认敏感 HTTP 传输。 |`
- `audit_reports/02_rule_by_rule_mapping.md:26`
  `| BR019 | confirmed | B011 / Locking it down: The privacy and security of mobile medication apps | 药物、处方、提醒等是敏感健康信息。 | bundle/strings 出现 prescription、referral、pharmacy、sick certificate 等医疗文档/药房相关流程。 |`
- `audit_reports/02_rule_by_rule_mapping.md:27`
  `| BR020 | confirmed | B012 / Privacy policies of Android apps for depression | 心理健康数据高度敏感，需要透明处理。 | bundle/strings 含 GAD-7、PHQ-9、anxiety、depression 等心理健康量表/文案。确认数据类型，不确认泄露。 |`
- `audit_reports/02_rule_by_rule_mapping.md:37`
  `| BR030 | not_supported | B016 / A privacy and security analysis of Android COVID-19 contact tracing apps | exported Service 可触发敏感后台行为。 | RingerService/OngoingCallService/PushNotificationInterceptor 均 'exported=false'。 |`
- `audit_reports/02_rule_by_rule_mapping.md:38`
  `| BR031 | not_supported | B016 / A privacy and security analysis of Android COVID-19 contact tracing apps | exported Receiver 可接收外部广播触发敏感行为。 | 未发现无保护 exported receiver 触发敏感模块；Work diagnostics receiver 有 DUMP 权限。 |`
- `audit_reports/02_rule_by_rule_mapping.md:43`
  `| BR040 | confirmed | B007 / Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | 三方 SDK 默认初始化和隐私设置会影响数据收集。 | MainApplication 启动 Braze/Appboy、Branch；JS 启动 Sentry/O11y/native events。确认初始化链。 |`
- `audit_reports/02_rule_by_rule_mapping.md:44`
  `| BR041 | supported_hypothesis | B007 / Privacy Settings of Third-Party Libraries in Android Apps | 默认 tracking/auto logging 若未门控会造成隐私风险。 | AppCenter analytics 'ALWAYS_SEND'，Braze lifecycle true，Branch auto instance；未确认 consent gate 与实际发送。 |`
- `audit_reports/02_rule_by_rule_mapping.md:49`
  `| BR050 | not_testable | B005 / Mobile health and privacy: cross sectional study | 隐私政策应披露数据接收方和跟踪。 | APK 中有隐私 URL，但未联网核验当前政策全文，也无抓包接收方列表。 |`
- `audit_reports/02_rule_by_rule_mapping.md:50`
  `| BR051 | not_testable | B012 / Privacy policies of Android apps for depression | 心理健康 App 应清晰披露敏感数据使用。 | 发现心理健康数据表面，但未核验政策全文。 |`
- `audit_reports/02_rule_by_rule_mapping.md:51`
  `| BR052 | not_testable | B013 / Privacy policies of mHealth apps | mHealth 隐私政策可用性/内容需要检查。 | 本地 APK 只提供 URL/文案，未获取当前政策。 |`
- `audit_reports/02_rule_by_rule_mapping.md:52`
  `| BR055 | confirmed | B014 / Privacy Assessment in Mobile Health Apps | mHealth 隐私评估应组织多层证据。 | 本审计按 Manifest、代码、资源、存储、网络、动态缺口、云端假设组织。 |`
- `audit_reports/02_rule_by_rule_mapping.md:53`
  `| BR058 | confirmed | B014 / Privacy Assessment in Mobile Health Apps | 评估应区分一方代码与三方 SDK。 | 报告中将 'com.babylon.cyrus' 与 Branch/AppsFlyer/Braze/Auth0/Braintree/Onfido 等分开。 |`
- `audit_reports/02_rule_by_rule_mapping.md:55`
  `| BR060 | supported_hypothesis | B016 / A privacy and security analysis of Android COVID-19 contact tracing apps | 环境/baseUrl/channel flag 可导致后端切换风险。 | bundle 内含 prod/preprod/dev/local host 和 release config；未证明攻击者可切换。 |`
- `audit_reports/02_rule_by_rule_mapping.md:71`
  `| BR076 | not_testable | B005 / Mobile health and privacy: cross sectional study | 论文关注第三方数据接收方和跟踪库，动态上要看登录或功能使用前是否已有三方请求。 | 无初装/登录前抓包，不能判断 Branch/Braze/AppsFlyer/Sentry/AppCenter 是否在功能使用前联网。 |`
- `audit_reports/02_rule_by_rule_mapping.md:72`
  `| BR077 | not_testable | B007 / Privacy Settings of Third-Party Libraries in Android Apps | 三方 SDK 默认设置风险需要动态观察 consent screen 前后的流量差异。 | 静态看到 SDK 初始化，但无 consent 前后抓包，因此不能确认 SDK traffic before consent。 |`
- `audit_reports/02_rule_by_rule_mapping.md:76`
  `| BR081 | not_testable | B005 / Mobile health and privacy: cross sectional study | 本地 DB/Prefs 中可读敏感值需运行后提取验证。 | 静态看到持久化设计，但无设备 DB/Prefs/AsyncStorage 文件。 |`
- `audit_reports/02_rule_by_rule_mapping.md:77`
  `| BR082 | not_testable | B002 / Unaddressed privacy risks in accredited health and wellness apps | 登出后本地敏感值残留是本地隐私测试重点。 | 无登录/登出后的本地存储转储，无法判断残留。 |`
- `audit_reports/02_rule_by_rule_mapping.md:78`
  `| BR083 | not_testable | B016 / A privacy and security analysis of Android COVID-19 contact tracing apps | exported component 能否被外部调用并改变状态需 ADB/外部 App 验证。 | 静态链 confirmed，但未运行 'adb shell am start'，所以动态规则 not_testable。 |`
- `audit_reports/02_rule_by_rule_mapping.md:81`
  `| BR088 | not_testable | B004 / Assessment of Data Sharing and Privacy Practices of Smartphone Apps | 论文关注健康/心理/戒烟等敏感流程与第三方请求的同时发生。 | App 有健康/心理/药物数据表面和 SDK，但无流程抓包，不能判断三方请求是否与敏感流程重合。 |`
- `audit_reports/02_rule_by_rule_mapping.md:82`
  `| BR090 | confirmed | B014 / Privacy Assessment in Mobile Health Apps | mHealth 隐私评估应把静态高风险项转为手机端验证计划。 | 总报告第 11 节列出 exported Activity、storage、proxy、deep link、SDK consent 的优先动态验证清单。 |`
- `audit_reports/02_rule_by_rule_mapping.md:84`
  `| BR092 | supported_hypothesis | B005 / Mobile health and privacy: cross sectional study | mHealth App 中 adid/deviceId/userId 发送到第三方域名涉及接收方和披露风险。 | SDK 初始化和 ID 能力存在；无抓包确认 adid/deviceId/userId 到第三方域。 |`
- `audit_reports/02_rule_by_rule_mapping.md:85`
  `| BR093 | not_testable | B004 / Assessment of Data Sharing and Privacy Practices of Smartphone Apps | 需要比较观察到的数据接收方与隐私政策披露。 | 无抓包接收方列表，也未联网核验当前政策全文。 |`
- `audit_reports/02_rule_by_rule_mapping.md:86`
  `| BR094 | supported_hypothesis | B016 / A privacy and security analysis of Android COVID-19 contact tracing apps | 身份、设备、位置、健康上下文在同一 API 中组合会增加隐私风险。 | Auth 参数含设备名/Tealium visitor id；App 有身份/健康/保险数据；无单个 payload 同时包含这些字段的证据。 |`
- `audit_reports/02_rule_by_rule_mapping.md:87`
  `| BR095 | not_supported | B025 / Why Eve and Mallory Still Love Android: Revisiting TLS | 敏感 endpoint 使用弱 TLS/客户端配置会降低保护。 | 未发现一方 TLS 绕过；业务 endpoint 为 HTTPS。cleartext policy 单独归 BR006。 |`
- `audit_reports/02_rule_by_rule_mapping.md:89`
  `| BR097 | not_supported | B019 / Pulse Oximeter App Privacy Policies | 血氧/脉搏设备数据和政策披露需检查。 | 仅见设备同步 provider mock 和健康监测泛化字段，未确认 SpO2/脉搏血氧上传。 |`
- `audit_reports/03_final_audit_report.md:40`
  `- confirmed 只用于静态 artifact 自身即可证明的事实，例如 Manifest cleartext policy、exported 组件、硬编码 key 存在、代码级数据流。`
- `audit_reports/04_mentor_review_and_revisions.md:27`
  `### B005 Mobile health and privacy: cross sectional study`
- `audit_reports/04_mentor_review_and_revisions.md:43`
  `- 可以支持危险权限基线、硬编码 key、cleartext policy、组件暴露等静态检查。`
- `audit_reports/04_mentor_review_and_revisions.md:47`
  `### B007 Privacy Settings of Third-Party Libraries in Android Apps`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_en_ca.json:1`
  `{"chat-exp.about_your_results_content":"The possible causes are those that the Babylon algorithm suggests as most likely, given the answers you entered. They are listed in the order of their match to your answers and how common the causes are. The order is not an indication of your individual likeli...`

## BR052

paper_id: B013
paper_title: Availability and quality of mobile health app privacy policies

- `audit_reports/01_evidence_chain.md:163`
  `## 4. 网络、URL 与 cleartext policy 证据链`
- `audit_reports/01_evidence_chain.md:168`
  `### 4.1 Manifest policy`
- `audit_reports/02_rule_by_rule_mapping.md:12`
  `| BR005 | supported_hypothesis | B021 / Metadata-Based Privacy Assessment for Android Apps | 论文使用应用元数据与实际权限/数据行为之间的不一致来评估隐私风险。 | 当前项目没有商店元数据全文；从 APK 名称/业务看是健康问诊类 App，权限覆盖相机、麦克风、位置、日历、存储、READ_PHONE_STATE、AD_ID、Bluetooth。由于缺少 store description 与政策全文，只能作为元数据-权限不一致的待验证假设。 |`
- `audit_reports/02_rule_by_rule_mapping.md:13`
  `| BR006 | confirmed | B016 / A privacy and security analysis of Android COVID-19 contact tracing apps | 论文把明文传输/静态安全配置作为 Android 安全问题。 | 'AndroidManifest.xml:125' 设置 'usesCleartextTraffic="true"'，且未发现 NSC。确认 cleartext policy 过宽；不确认敏感 HTTP 传输。 |`
- `audit_reports/02_rule_by_rule_mapping.md:26`
  `| BR019 | confirmed | B011 / Locking it down: The privacy and security of mobile medication apps | 药物、处方、提醒等是敏感健康信息。 | bundle/strings 出现 prescription、referral、pharmacy、sick certificate 等医疗文档/药房相关流程。 |`
- `audit_reports/02_rule_by_rule_mapping.md:27`
  `| BR020 | confirmed | B012 / Privacy policies of Android apps for depression | 心理健康数据高度敏感，需要透明处理。 | bundle/strings 含 GAD-7、PHQ-9、anxiety、depression 等心理健康量表/文案。确认数据类型，不确认泄露。 |`
- `audit_reports/02_rule_by_rule_mapping.md:32`
  `| BR025 | supported_hypothesis | B005 / Mobile health and privacy: cross sectional study | mHealth 本地数据、第三方接收方和传输需要一起评估。 | Redux persist 可能保存 session/monitor/userContext，且 key 静态；无真实 DB/storage dump，不能确认某个 DB 明文字段。 |`
- `audit_reports/02_rule_by_rule_mapping.md:33`
  `| BR026 | confirmed | B002 / Unaddressed privacy risks in accredited health and wellness apps | 论文协议测试本地存储和传输，报告过本地存储保护不足。 | session token 字段进入 Redux 持久化白名单，encrypt key 来自 bundle 静态 getKey。确认代码级存储设计风险；未确认设备中真实 token。 |`
- `audit_reports/02_rule_by_rule_mapping.md:34`
  `| BR027 | supported_hypothesis | B002 / Unaddressed privacy risks in accredited health and wellness apps | 本地/外部存储和导出路径是隐私测试范围。 | FileProvider XML 有 external/root 宽路径，RNFetchBlob/RNShare/WebView 下载模块存在；但无敏感文件实际导出证据。 |`
- `audit_reports/02_rule_by_rule_mapping.md:35`
  `| BR028 | not_supported | B014 / Privacy Assessment in Mobile Health Apps | 存储、备份和权限应纳入 mHealth 隐私评估。 | 'allowBackup=false'；虽有 sensitive storage 设计，但 Android 备份风险条件不成立。 |`
- `audit_reports/02_rule_by_rule_mapping.md:36`
  `| BR029 | confirmed | B016 / A privacy and security analysis of Android COVID-19 contact tracing apps | 组件暴露和外部入口属于 Android 静态安全问题。 | exported RNBootSplash/MainActivity 接收/转发 Intent，'setLaunchType' 影响视频问诊状态和服务。确认静态路径。 |`
- `audit_reports/02_rule_by_rule_mapping.md:37`
  `| BR030 | not_supported | B016 / A privacy and security analysis of Android COVID-19 contact tracing apps | exported Service 可触发敏感后台行为。 | RingerService/OngoingCallService/PushNotificationInterceptor 均 'exported=false'。 |`
- `audit_reports/02_rule_by_rule_mapping.md:38`
  `| BR031 | not_supported | B016 / A privacy and security analysis of Android COVID-19 contact tracing apps | exported Receiver 可接收外部广播触发敏感行为。 | 未发现无保护 exported receiver 触发敏感模块；Work diagnostics receiver 有 DUMP 权限。 |`
- `audit_reports/02_rule_by_rule_mapping.md:43`
  `| BR040 | confirmed | B007 / Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | 三方 SDK 默认初始化和隐私设置会影响数据收集。 | MainApplication 启动 Braze/Appboy、Branch；JS 启动 Sentry/O11y/native events。确认初始化链。 |`
- `audit_reports/02_rule_by_rule_mapping.md:44`
  `| BR041 | supported_hypothesis | B007 / Privacy Settings of Third-Party Libraries in Android Apps | 默认 tracking/auto logging 若未门控会造成隐私风险。 | AppCenter analytics 'ALWAYS_SEND'，Braze lifecycle true，Branch auto instance；未确认 consent gate 与实际发送。 |`
- `audit_reports/02_rule_by_rule_mapping.md:49`
  `| BR050 | not_testable | B005 / Mobile health and privacy: cross sectional study | 隐私政策应披露数据接收方和跟踪。 | APK 中有隐私 URL，但未联网核验当前政策全文，也无抓包接收方列表。 |`
- `audit_reports/02_rule_by_rule_mapping.md:50`
  `| BR051 | not_testable | B012 / Privacy policies of Android apps for depression | 心理健康 App 应清晰披露敏感数据使用。 | 发现心理健康数据表面，但未核验政策全文。 |`
- `audit_reports/02_rule_by_rule_mapping.md:51`
  `| BR052 | not_testable | B013 / Privacy policies of mHealth apps | mHealth 隐私政策可用性/内容需要检查。 | 本地 APK 只提供 URL/文案，未获取当前政策。 |`
- `audit_reports/02_rule_by_rule_mapping.md:52`
  `| BR055 | confirmed | B014 / Privacy Assessment in Mobile Health Apps | mHealth 隐私评估应组织多层证据。 | 本审计按 Manifest、代码、资源、存储、网络、动态缺口、云端假设组织。 |`
- `audit_reports/02_rule_by_rule_mapping.md:53`
  `| BR058 | confirmed | B014 / Privacy Assessment in Mobile Health Apps | 评估应区分一方代码与三方 SDK。 | 报告中将 'com.babylon.cyrus' 与 Branch/AppsFlyer/Braze/Auth0/Braintree/Onfido 等分开。 |`
- `audit_reports/02_rule_by_rule_mapping.md:55`
  `| BR060 | supported_hypothesis | B016 / A privacy and security analysis of Android COVID-19 contact tracing apps | 环境/baseUrl/channel flag 可导致后端切换风险。 | bundle 内含 prod/preprod/dev/local host 和 release config；未证明攻击者可切换。 |`
- `audit_reports/02_rule_by_rule_mapping.md:71`
  `| BR076 | not_testable | B005 / Mobile health and privacy: cross sectional study | 论文关注第三方数据接收方和跟踪库，动态上要看登录或功能使用前是否已有三方请求。 | 无初装/登录前抓包，不能判断 Branch/Braze/AppsFlyer/Sentry/AppCenter 是否在功能使用前联网。 |`
- `audit_reports/02_rule_by_rule_mapping.md:72`
  `| BR077 | not_testable | B007 / Privacy Settings of Third-Party Libraries in Android Apps | 三方 SDK 默认设置风险需要动态观察 consent screen 前后的流量差异。 | 静态看到 SDK 初始化，但无 consent 前后抓包，因此不能确认 SDK traffic before consent。 |`
- `audit_reports/02_rule_by_rule_mapping.md:76`
  `| BR081 | not_testable | B005 / Mobile health and privacy: cross sectional study | 本地 DB/Prefs 中可读敏感值需运行后提取验证。 | 静态看到持久化设计，但无设备 DB/Prefs/AsyncStorage 文件。 |`
- `audit_reports/02_rule_by_rule_mapping.md:77`
  `| BR082 | not_testable | B002 / Unaddressed privacy risks in accredited health and wellness apps | 登出后本地敏感值残留是本地隐私测试重点。 | 无登录/登出后的本地存储转储，无法判断残留。 |`
- `audit_reports/02_rule_by_rule_mapping.md:78`
  `| BR083 | not_testable | B016 / A privacy and security analysis of Android COVID-19 contact tracing apps | exported component 能否被外部调用并改变状态需 ADB/外部 App 验证。 | 静态链 confirmed，但未运行 'adb shell am start'，所以动态规则 not_testable。 |`
- `audit_reports/02_rule_by_rule_mapping.md:81`
  `| BR088 | not_testable | B004 / Assessment of Data Sharing and Privacy Practices of Smartphone Apps | 论文关注健康/心理/戒烟等敏感流程与第三方请求的同时发生。 | App 有健康/心理/药物数据表面和 SDK，但无流程抓包，不能判断三方请求是否与敏感流程重合。 |`
- `audit_reports/02_rule_by_rule_mapping.md:82`
  `| BR090 | confirmed | B014 / Privacy Assessment in Mobile Health Apps | mHealth 隐私评估应把静态高风险项转为手机端验证计划。 | 总报告第 11 节列出 exported Activity、storage、proxy、deep link、SDK consent 的优先动态验证清单。 |`
- `audit_reports/02_rule_by_rule_mapping.md:84`
  `| BR092 | supported_hypothesis | B005 / Mobile health and privacy: cross sectional study | mHealth App 中 adid/deviceId/userId 发送到第三方域名涉及接收方和披露风险。 | SDK 初始化和 ID 能力存在；无抓包确认 adid/deviceId/userId 到第三方域。 |`
- `audit_reports/02_rule_by_rule_mapping.md:85`
  `| BR093 | not_testable | B004 / Assessment of Data Sharing and Privacy Practices of Smartphone Apps | 需要比较观察到的数据接收方与隐私政策披露。 | 无抓包接收方列表，也未联网核验当前政策全文。 |`
- `audit_reports/02_rule_by_rule_mapping.md:86`
  `| BR094 | supported_hypothesis | B016 / A privacy and security analysis of Android COVID-19 contact tracing apps | 身份、设备、位置、健康上下文在同一 API 中组合会增加隐私风险。 | Auth 参数含设备名/Tealium visitor id；App 有身份/健康/保险数据；无单个 payload 同时包含这些字段的证据。 |`
- `audit_reports/02_rule_by_rule_mapping.md:87`
  `| BR095 | not_supported | B025 / Why Eve and Mallory Still Love Android: Revisiting TLS | 敏感 endpoint 使用弱 TLS/客户端配置会降低保护。 | 未发现一方 TLS 绕过；业务 endpoint 为 HTTPS。cleartext policy 单独归 BR006。 |`
- `audit_reports/02_rule_by_rule_mapping.md:89`
  `| BR097 | not_supported | B019 / Pulse Oximeter App Privacy Policies | 血氧/脉搏设备数据和政策披露需检查。 | 仅见设备同步 provider mock 和健康监测泛化字段，未确认 SpO2/脉搏血氧上传。 |`
- `audit_reports/04_mentor_review_and_revisions.md:17`
  `### B002 Unaddressed privacy risks in accredited health and wellness apps`
- `audit_reports/04_mentor_review_and_revisions.md:27`
  `### B005 Mobile health and privacy: cross sectional study`
- `audit_reports/04_mentor_review_and_revisions.md:43`
  `- 可以支持危险权限基线、硬编码 key、cleartext policy、组件暴露等静态检查。`
- `audit_reports/04_mentor_review_and_revisions.md:96`
  `### B014 Privacy Assessment in Mobile Health Apps`
- `audit_reports/04_mentor_review_and_revisions.md:106`
  `### B016 A privacy and security analysis of Android COVID-19 contact tracing apps`
- `audit_reports/04_mentor_review_and_revisions.md:116`
  `### B019 Pulse Oximeter App Privacy Policies`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_en_ca.json:1`
  `{"chat-exp.about_your_results_content":"The possible causes are those that the Babylon algorithm suggests as most likely, given the answers you entered. They are listed in the order of their match to your answers and how common the causes are. The order is not an indication of your individual likeli...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_en_ca__partnertelus.json:1`
  `{"account_details.county":"Province","account_details.phn_why_subtitle":"Your Medical ID (Health card number) may be required to facilitate prescriptions, labs, imaging requisitions and specialist referrals. By entering your Medical ID the cost of your appointment could be covered by your provincial...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_en_gb.json:1`
  `{"chat-exp.about_your_results_content":"The possible causes are those that the Babylon algorithm suggests as most likely, given the answers you entered. They are listed in the order of their match to your answers and how common the causes are. The order is not an indication of your individual likeli...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_en_gb__partnerbupa.json:1`
  `{"appointments.checkin.window":"If you can't attend, please cancel as soon as possible to free your slot for another patient.","appointments.referraldetailfaqurl":"https://www.bupa.co.uk/help-and-support/blua/prescriptions-and-referrals/referrals","global.applicationName":"Bupa Blua Health","global....`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_en_us.json:1`
  `{"chat-exp.about_your_results_content":"The possible causes are those that the Babylon algorithm suggests as most likely, given the answers you entered. They are listed in the order of their match to your answers and how common the causes are. The order is not an indication of your individual likeli...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_es_us.json:1`
  `{"chat-exp.about_your_results_content":"Las posibles causas son afecciones que pueden estar relacionadas con los síntomas y factores de riesgo ingresados por el usuario.\n\nLas afecciones presentadas a un usuario se enumeran en el orden en que las afecciones coinciden con los síntomas y los factores...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_fr_ca.json:1`
  `{"chat-exp.about_your_results_content":"Les causes possibles sont celles que l'algorithme de Babylon considère les plus probables d'après les réponses que vous avez fournies. Elles sont répertoriées dans leur ordre de correspondance avec vos réponses et de leur fréquence. Cependant, cet ordre n'est ...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_fr_ca__partnertelus.json:1`
  `{"account_details.county":"Province","account_details.phn_why_subtitle":"Votre identifiant médical (numéro de carte d'assurance maladie) peut être requis pour faciliter les ordonnances, les analyses de laboratoire, les demandes d'imagerie et les références aux spécialistes. En saisissant votre ident...`

## BR055

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `sources/androidx/core/util/PatternsCompat.java:29`
  `private static final String STRICT_HOST_NAME = "(?:(?:[a-zA-Z0-9[ -\ud7ff豈-﷏ﷰ-\uffef𐀀-\u1fffd𠀀-\u2fffd𰀀-\u3fffd\u40000-\u4fffd\u50000-\u5fffd\u60000-\u6fffd\u70000-\u7fffd\u80000-\u8fffd\u90000-\u9fffd\ua0000-\uafffd\ub0000-\ubfffd\uc0000-\ucfffd\ud0000-\udfffd\ue1000-\uefffd&&[^ [\u2000-\u200a]\u20...`
- `sources/androidx/core/util/PatternsCompat.java:30`
  `private static final String STRICT_TLD = "(?:(?:(?:aaa|aarp|abb|abbott|abogado|academy|accenture|accountant|accountants|aco|active|actor|ads|adult|aeg|aero|afl|agency|aig|airforce|airtel|allfinanz|alsace|amica|amsterdam|android|apartments|app|apple|aquarelle|aramco|archi|army|arpa|arte|asia|associat...`
- `sources/androidx/core/util/PatternsCompat.java:46`
  `Pattern patternCompile3 = Pattern.compile("(?:(?:(?:[a-zA-Z0-9[ -\ud7ff豈-﷏ﷰ-\uffef𐀀-\u1fffd𠀀-\u2fffd𰀀-\u3fffd\u40000-\u4fffd\u50000-\u5fffd\u60000-\u6fffd\u70000-\u7fffd\u80000-\u8fffd\u90000-\u9fffd\ua0000-\uafffd\ub0000-\ubfffd\uc0000-\ucfffd\ud0000-\udfffd\ue1000-\uefffd&&[^ [\u2000-\u200a]\u2028...`

## BR058

paper_id: B022
paper_title: A Study of Android Application Security

- `audit_reports/02_rule_by_rule_mapping.md:43`
  `| BR040 | confirmed | B007 / Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | 三方 SDK 默认初始化和隐私设置会影响数据收集。 | MainApplication 启动 Braze/Appboy、Branch；JS 启动 Sentry/O11y/native events。确认初始化链。 |`
- `audit_reports/02_rule_by_rule_mapping.md:44`
  `| BR041 | supported_hypothesis | B007 / Privacy Settings of Third-Party Libraries in Android Apps | 默认 tracking/auto logging 若未门控会造成隐私风险。 | AppCenter analytics 'ALWAYS_SEND'，Braze lifecycle true，Branch auto instance；未确认 consent gate 与实际发送。 |`
- `audit_reports/02_rule_by_rule_mapping.md:72`
  `| BR077 | not_testable | B007 / Privacy Settings of Third-Party Libraries in Android Apps | 三方 SDK 默认设置风险需要动态观察 consent screen 前后的流量差异。 | 静态看到 SDK 初始化，但无 consent 前后抓包，因此不能确认 SDK traffic before consent。 |`
- `audit_reports/04_mentor_review_and_revisions.md:47`
  `### B007 Privacy Settings of Third-Party Libraries in Android Apps`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/onfido_licenses_apache2_0.txt:115`
  `wherever such third-party notices normally appear. The contents`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/onfido_licenses_apache2_0.txt:187`
  `identification within third-party archives.`

## BR059

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:137`
  `<intent-filter`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:149`
  `<intent-filter>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:154`
  `<intent-filter android:autoVerify="true">`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:171`
  `<intent-filter>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:180`
  `<intent-filter>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:189`
  `<intent-filter>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:198`
  `<intent-filter>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:207`
  `<intent-filter>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:216`
  `<intent-filter>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:225`
  `<intent-filter>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:239`
  `<intent-filter>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:327`
  `<intent-filter android:autoVerify="true">`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:381`
  `<intent-filter>`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:430`
  `<intent-filter>`

## BR060

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `sources/com/auth0/android/authentication/storage/CryptoUtil.java:49`
  `private static final String RSA_TRANSFORMATION = "RSA/ECB/PKCS1Padding";`
- `sources/com/auth0/android/authentication/storage/CryptoUtil.java:106`
  `Cipher cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding");`
- `sources/com/auth0/android/authentication/storage/CryptoUtil.java:140`
  `Cipher cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding");`
- `sources/com/cardinalcommerce/a/CardinalActionCode.java:42`
  `throw new com.cardinalcommerce.dependencies.internal.nimbusds.jose.KeyLengthException("Unsupported AES/CBC/PKCS5Padding/HMAC-SHA2 key length, must be 256, 384 or 512 bits");`
- `sources/com/cardinalcommerce/a/CardinalActionCode.java:114`
  `cipher = Cipher.getInstance("RSA/ECB/OAEPWithSHA-1AndMGF1Padding");`
- `sources/com/cardinalcommerce/a/CardinalActionCode.java:116`
  `cipher = Cipher.getInstance("RSA/ECB/OAEPWithSHA-1AndMGF1Padding", provider);`
- `sources/com/cardinalcommerce/a/setBaseline.java:25`
  `Cipher cipher = provider == null ? Cipher.getInstance("RSA/ECB/OAEPWithSHA-256AndMGF1Padding") : Cipher.getInstance("RSA/ECB/OAEPWithSHA-256AndMGF1Padding", provider);`
- `sources/com/cardinalcommerce/dependencies/internal/bouncycastle/jcajce/provider/asymmetric/ElGamal.java:21`
  `asymmetricKeyInfoConverter.getInstance("Alg.Alias.Cipher.ELGAMAL/ECB/PKCS1PADDING", "ELGAMAL/PKCS1");`
- `sources/com/cardinalcommerce/dependencies/internal/nimbusds/jose/crypto/impl/AESCBC.java:89`
  `cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/cardinalcommerce/dependencies/internal/nimbusds/jose/crypto/impl/AESCBC.java:91`
  `cipher = Cipher.getInstance("AES/CBC/PKCS5Padding", provider);`
- `sources/com/microsoft/appcenter/utils/crypto/CryptoRsaHandler.java:60`
  `return "RSA/ECB/PKCS1Padding/2048";`
- `sources/com/nimbusds/jose/crypto/AESCBC.java:29`
  `Cipher cipherHelper = CipherHelper.getInstance("AES/CBC/PKCS5Padding", provider);`
- `sources/com/nimbusds/jose/crypto/CompositeKey.java:30`
  `throw new KeyLengthException("Unsupported AES/CBC/PKCS5Padding/HMAC-SHA2 key length, must be 256, 384 or 512 bits");`
- `sources/com/nimbusds/jose/crypto/RSA_OAEP.java:23`
  `Cipher cipherHelper = CipherHelper.getInstance("RSA/ECB/OAEPWithSHA1AndMGF1Padding", provider);`
- `sources/com/nimbusds/jose/crypto/RSA_OAEP.java:33`
  `Cipher cipherHelper = CipherHelper.getInstance("RSA/ECB/OAEPWithSHA-1AndMGF1Padding", provider);`
- `sources/com/nimbusds/jose/crypto/RSA_OAEP_256.java:28`
  `Cipher cipherHelper = CipherHelper.getInstance("RSA/ECB/OAEPWithSHA-256AndMGF1Padding", provider);`
- `sources/com/nimbusds/jose/crypto/RSA_OAEP_256.java:40`
  `Cipher cipherHelper = CipherHelper.getInstance("RSA/ECB/OAEPWithSHA-256AndMGF1Padding", provider);`
- `sources/com/nimbusds/jose/jca/JCASupport.java:109`
  `str2 = "RSA/ECB/OAEPWithSHA-256AndMGF1Padding";`
- `sources/com/nimbusds/jose/jca/JCASupport.java:113`
  `str2 = "RSA/ECB/OAEPWithSHA-1AndMGF1Padding";`
- `sources/com/nimbusds/jose/jca/JCASupport.java:160`
  `Cipher.getInstance("AES/CBC/PKCS5Padding", provider);`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageKeystoreRsaEcb.java:38`
  `public static final String BLOCK_MODE_ECB = "ECB";`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageKeystoreRsaEcb.java:42`
  `public static final String TRANSFORMATION_RSA_ECB_PKCS1 = "RSA/ECB/PKCS1Padding";`

## BR061

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/constraintlayout/motion/widget/KeyAttributes.java:299`
  `public void setValue(String str, Object obj) {`
- `sources/androidx/constraintlayout/motion/widget/KeyCycle.java:476`
  `public void setValue(String str, Object obj) {`
- `sources/androidx/constraintlayout/motion/widget/KeyTimeCycle.java:300`
  `public void setValue(String str, Object obj) {`
- `sources/androidx/lifecycle/LiveData.java:128`
  `LiveData.this.setValue(obj);`
- `sources/androidx/lifecycle/LiveData.java:323`
  `LiveData.this.setValue(obj2);`
- `sources/bo/app/u.java:28`
  `if (url.getProtocol().equals("https")) {`
- `sources/com/braintreepayments/api/DropInViewModel.java:62`
  `this.vaultedPaymentMethods.setValue(arrayList);`
- `sources/com/braintreepayments/api/DropInViewModel.java:67`
  `this.bottomSheetState.setValue(bottomSheetState);`
- `sources/com/braintreepayments/api/DropInViewModel.java:79`
  `this.supportedCardTypes.setValue(list);`
- `sources/com/braintreepayments/api/DropInViewModel.java:83`
  `this.supportedPaymentMethods.setValue(list);`
- `sources/com/braintreepayments/api/DropInViewModel.java:87`
  `this.userCanceledError.setValue(exc);`
- `sources/com/braintreepayments/api/DropInViewModel.java:91`
  `this.vaultedPaymentMethods.setValue(list);`
- `sources/com/facebook/react/viewmanagers/SliderManagerDelegate.java:121`
  `((SliderManagerInterface) this.mViewManager).setValue(t2, obj != null ? ((Double) obj).doubleValue() : 0.0d);`
- `sources/com/facebook/react/views/slider/ReactSlider.java:74`
  `void setValue(double d2) {`
- `sources/com/google/common/collect/Synchronized.java:495`
  `public V setValue(V v2) {`
- `sources/com/google/common/collect/Synchronized.java:498`
  `value = b().setValue(v2);`
- `sources/com/google/common/reflect/ClassPath.java:223`
  `if (next.getProtocol().equals("file")) {`
- `sources/com/google/common/reflect/ClassPath.java:249`
  `if (urlB.getProtocol().equals("file")) {`
- `sources/com/google/common/reflect/ClassPath.java:345`
  `Preconditions.checkArgument(url.getProtocol().equals("file"));`
- `sources/com/microsoft/appcenter/analytics/AnalyticsTransmissionTarget.java:81`
  `((CommonSchemaLog) log).getExt().getProtocol().setTicketKeys(Collections.singletonList(authenticationProvider.e()));`
- `sources/com/microsoft/appcenter/http/HttpUtils.java:49`
  `if (!"https".equals(url.getProtocol())) {`
- `sources/com/microsoft/appcenter/ingestion/OneCollectorIngestion.java:98`
  `List<String> ticketKeys = ((CommonSchemaLog) it3.next()).getExt().getProtocol().getTicketKeys();`
- `sources/com/microsoft/appcenter/ingestion/models/one/Extensions.java:100`
  `public ProtocolExtension getProtocol() {`
- `sources/com/microsoft/appcenter/ingestion/models/one/Extensions.java:225`
  `if (getProtocol() != null) {`
- `sources/com/microsoft/appcenter/ingestion/models/one/Extensions.java:227`
  `getProtocol().write(jSONStringer);`
- `sources/com/microsoft/appcenter/ingestion/models/one/PartAUtils.java:23`
  `commonSchemaLog.getExt().getProtocol().setDevModel(device.getModel());`
- `sources/com/microsoft/appcenter/ingestion/models/one/PartAUtils.java:24`
  `commonSchemaLog.getExt().getProtocol().setDevMake(device.getOemName());`
- `sources/com/onfido/android/sdk/capture/internal/nfc/JMRTDPassportNfcReader.java:300`
  `companion.i("\n            NFC Logger - Performing PACE with " + pACEKeySpecCreateCANKey + " input\n            NFC Logger - Performing PACE : Security information object ID: " + objectIdentifier + "\n            NFC Logger - Performing PACE : Security Protocol ID: " + pACEInfo.getProtocolOIDString(...`
- `sources/com/onfido/android/sdk/capture/ui/OnfidoActivity.java:440`
  `String[] supportedProtocols = SSLContext.getDefault().getDefaultSSLParameters().getProtocols();`
- `sources/com/opentok/android/Session.java:608`
  `int iA = com.opentok.otc.e.a(this.otc_session, this.apiUrl.getHost(), this.apiUrl.getPath(), this.apiUrl.getPort() == -1 ? this.apiUrl.getDefaultPort() : this.apiUrl.getPort(), Utils.booleanToInt(this.apiUrl.getProtocol().equals("https")), str);`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:1276`
  `request.addRequestHeader("Cookie", CookieManager.getInstance().getCookie(url.getProtocol() + "://" + url.getHost()));`
- `sources/okhttp3/Handshake.java:276`
  `String protocol = sSLSession.getProtocol();`
- `sources/okhttp3/OkHttpClient.java:134`
  `@Metadata(d1 = {"\u0000ø\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0018...`
- `sources/okhttp3/OkHttpClient.java:496`
  `public final List<Protocol> getProtocols$okhttp() {`
- `sources/okhttp3/OkHttpClient.java:611`
  `if (!Intrinsics.areEqual(mutableList, getProtocols$okhttp())) {`
- `sources/okhttp3/OkHttpClient.java:968`
  `this.protocols = builder.getProtocols$okhttp();`
- `sources/okhttp3/Response.java:171`
  `public final Protocol getProtocol() {`
- `sources/okhttp3/Response.java:383`
  `@Metadata(d1 = {"\u0000l\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\t\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u00...`
- `sources/okhttp3/Response.java:553`
  `/* JADX INFO: renamed from: getProtocol$okhttp, reason: from getter */`
- `sources/okhttp3/Response.java:554`
  `public final Protocol getProtocol() {`

## BR063

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/android/support/v4/media/session/MediaControllerCompat.java:51`
  `public static final String COMMAND_ARGUMENT_INDEX = "android.support.v4.media.session.command.ARGUMENT_INDEX";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:54`
  `public static final String COMMAND_ARGUMENT_MEDIA_DESCRIPTION = "android.support.v4.media.session.command.ARGUMENT_MEDIA_DESCRIPTION";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:57`
  `public static final String COMMAND_GET_EXTRA_BINDER = "android.support.v4.media.session.command.GET_EXTRA_BINDER";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:60`
  `public static final String COMMAND_REMOVE_QUEUE_ITEM = "android.support.v4.media.session.command.REMOVE_QUEUE_ITEM";`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:63`
  `public static final String COMMAND_REMOVE_QUEUE_ITEM_AT = "android.support.v4.media.session.command.REMOVE_QUEUE_ITEM_AT";`
- `sources/androidx/activity/ActivityViewModelLazyKt$viewModels$factoryPromise$1.java:9`
  `import org.objectweb.asm.Opcodes;`
- `sources/androidx/activity/ActivityViewModelLazyKt$viewModels$factoryPromise$1.java:13`
  `@Metadata(d1 = {"\u0000\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\u0010\u0000\u001a\u00020\u0001\"\n\b\u0000\u0010\u0002\u0018\u0001*\u00020\u0003H\n¢\u0006\u0002\b\u0004"}, d2 = {"<anonymous>", "Landroidx/lifecycle/ViewModelProvider$Factory;", "VM", "Landroidx/lifecycle/...`
- `sources/androidx/activity/ActivityViewModelLazyKt$viewModels$factoryPromise$2.java:9`
  `import org.objectweb.asm.Opcodes;`
- `sources/androidx/activity/ActivityViewModelLazyKt$viewModels$factoryPromise$2.java:13`
  `@Metadata(d1 = {"\u0000\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\u0010\u0000\u001a\u00020\u0001\"\n\b\u0000\u0010\u0002\u0018\u0001*\u00020\u0003H\n¢\u0006\u0002\b\u0004"}, d2 = {"<anonymous>", "Landroidx/lifecycle/ViewModelProvider$Factory;", "VM", "Landroidx/lifecycle/...`
- `sources/androidx/activity/ActivityViewModelLazyKt.java:18`
  `import org.objectweb.asm.Opcodes;`
- `sources/androidx/activity/ActivityViewModelLazyKt.java:27`
  `@Metadata(d1 = {"\u0000\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\u0010\u0000\u001a\u00020\u0001\"\n\b\u0000\u0010\u0002\u0018\u0001*\u00020\u0003H\n¢\u0006\u0002\b\u0004"}, d2 = {"<anonymous>", "Landroidx/lifecycle/ViewModelStore;", "VM", "Landroidx/lifecycle/ViewModel;"...`
- `sources/androidx/exifinterface/media/ExifInterface.java:1539`
  `byte[] bArr = new byte[5000];`
- `sources/androidx/exifinterface/media/ExifInterface.java:1983`
  `byte[] bArr = f3123g;`
- `sources/androidx/exifinterface/media/ExifInterface.java:1985`
  `byte[] bArr2 = new byte[bArr.length];`
- `sources/androidx/exifinterface/media/ExifInterface.java:1990`
  `byte[] bArr3 = f3123g;`
- `sources/androidx/exifinterface/media/ExifInterface.java:3246`
  `byte[] bArr = this.mThumbnailBytes;`
- `sources/androidx/fragment/app/FragmentViewModelLazyKt.java:24`
  `import org.objectweb.asm.Opcodes;`
- `sources/androidx/fragment/app/FragmentViewModelLazyKt.java:33`
  `@Metadata(d1 = {"\u0000\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\u0010\u0000\u001a\u00020\u0001\"\n\b\u0000\u0010\u0002\u0018\u0001*\u00020\u0003H\n¢\u0006\u0002\b\u0004"}, d2 = {"<anonymous>", "Landroidx/lifecycle/ViewModelStore;", "VM", "Landroidx/lifecycle/ViewModel;"...`
- `sources/androidx/fragment/app/FragmentViewModelLazyKt.java:81`
  `@Metadata(d1 = {"\u0000\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\u0010\u0000\u001a\u00020\u0001\"\n\b\u0000\u0010\u0002\u0018\u0001*\u00020\u0003H\n¢\u0006\u0002\b\u0004"}, d2 = {"<anonymous>", "Landroidx/lifecycle/ViewModelProvider$Factory;", "VM", "Landroidx/lifecycle/...`
- `sources/androidx/fragment/app/FragmentViewModelLazyKt.java:105`
  `@Metadata(d1 = {"\u0000\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\u0010\u0000\u001a\u00020\u0001\"\n\b\u0000\u0010\u0002\u0018\u0001*\u00020\u0003H\n¢\u0006\u0002\b\u0004"}, d2 = {"<anonymous>", "Landroidx/lifecycle/ViewModelStore;", "VM", "Landroidx/lifecycle/ViewModel;"...`
- `sources/androidx/fragment/app/FragmentViewModelLazyKt.java:163`
  `@Metadata(d1 = {"\u0000\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\u0010\u0000\u001a\u00020\u0001\"\n\b\u0000\u0010\u0002\u0018\u0001*\u00020\u0003H\n¢\u0006\u0002\b\u0004"}, d2 = {"<anonymous>", "Landroidx/lifecycle/ViewModelProvider$Factory;", "VM", "Landroidx/lifecycle/...`
- `sources/androidx/fragment/app/FragmentViewModelLazyKt.java:187`
  `@Metadata(d1 = {"\u0000\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\u0010\u0000\u001a\u00020\u0001\"\n\b\u0000\u0010\u0002\u0018\u0001*\u00020\u0003H\n¢\u0006\u0002\b\u0004"}, d2 = {"<anonymous>", "Landroidx/lifecycle/ViewModelStore;", "VM", "Landroidx/lifecycle/ViewModel;"...`
- `sources/androidx/fragment/app/FragmentViewModelLazyKt.java:238`
  `@Metadata(d1 = {"\u0000\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\u0010\u0000\u001a\u00020\u0001\"\n\b\u0000\u0010\u0002\u0018\u0001*\u00020\u0003H\n¢\u0006\u0002\b\u0004"}, d2 = {"<anonymous>", "Landroidx/lifecycle/ViewModelProvider$Factory;", "VM", "Landroidx/lifecycle/...`
- `sources/androidx/fragment/app/FragmentViewModelLazyKt.java:272`
  `@Metadata(d1 = {"\u0000\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\u0010\u0000\u001a\u00020\u0001\"\n\b\u0000\u0010\u0002\u0018\u0001*\u00020\u0003H\n¢\u0006\u0002\b\u0004"}, d2 = {"<anonymous>", "Landroidx/lifecycle/ViewModelStore;", "VM", "Landroidx/lifecycle/ViewModel;"...`
- `sources/androidx/fragment/app/FragmentViewModelLazyKt.java:332`
  `@Metadata(d1 = {"\u0000\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\u0010\u0000\u001a\u00020\u0001\"\n\b\u0000\u0010\u0002\u0018\u0001*\u00020\u0003H\n¢\u0006\u0002\b\u0004"}, d2 = {"<anonymous>", "Landroidx/lifecycle/ViewModelProvider$Factory;", "VM", "Landroidx/lifecycle/...`
- `sources/androidx/room/RoomSQLiteQuery.java:58`
  `this.f4188d = new byte[i3][];`
- `sources/androidx/work/impl/background/systemalarm/ConstraintsCommandHandler.java:49`
  `Logger.get().debug(TAG, String.format("Creating a delay_met command for workSpec with id (%s)", str2), new Throwable[0]);`
- `sources/androidx/work/impl/model/WorkProgressDao_Impl.java:38`
  `byte[] byteArrayInternal = Data.toByteArrayInternal(workProgress.mProgress);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:67`
  `byte[] byteArrayInternal = Data.toByteArrayInternal(workSpec.input);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:73`
  `byte[] byteArrayInternal2 = Data.toByteArrayInternal(workSpec.output);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:109`
  `byte[] bArrContentUriTriggersToByteArray = WorkTypeConverters.contentUriTriggersToByteArray(constraints.getContentUriTriggers());`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:2057`
  `byte[] byteArrayInternal = Data.toByteArrayInternal(data);`
- `sources/com/airbnb/android/react/maps/AirMapTileProvider.java:361`
  `byte[] bArrF3 = f(i9, i6, i7);`
- `sources/com/airbnb/android/react/maps/AirMapTileProvider.java:362`
  `byte[] bArrF4 = f(i9, i8, i7);`
- `sources/com/airbnb/android/react/maps/AirMapTileProvider.java:378`
  `byte[] bArrA = a(bitmapD);`
- `sources/com/airbnb/android/react/maps/AirMapTileProvider.java:503`
  `byte[] bArrF = f(i8, i9, i10);`
- `sources/com/airbnb/android/react/maps/AirMapTileProvider.java:513`
  `byte[] bArrA = a(bitmapD);`
- `sources/com/airbnb/android/react/maps/ImageUtil.java:12`
  `byte[] bArrDecode = Base64.decode(str.substring(str.indexOf(AppboyConfigurationProvider.LOCALE_TO_API_KEY_MAPPING_SEPARATOR) + 1), 0);`
- `sources/com/airbnb/lottie/LottieCompositionFactory.java:34`
  `private static final byte[] MAGIC = {80, 75, 3, 4};`
- `sources/com/airbnb/lottie/manager/ImageAssetManager.java:75`
  `options.inDensity = Opcodes.IF_ICMPNE;`

## BR064

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/android/hardware/biometrics/BiometricPrompt.java:11`
  `import javax.crypto.Mac;`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:355`
  `String name = xml.getName();`
- `sources/androidx/biometric/BiometricPrompt.java:22`
  `import javax.crypto.Mac;`
- `sources/androidx/biometric/BiometricPrompt.java:340`
  `private final Mac mMac;`
- `sources/androidx/biometric/BiometricPrompt.java:364`
  `public Mac getMac() {`
- `sources/androidx/biometric/BiometricPrompt.java:380`
  `public CryptoObject(@NonNull Mac mac) {`
- `sources/androidx/biometric/BiometricPrompt.java:383`
  `this.mMac = mac;`
- `sources/androidx/biometric/CryptoObjectUtils.java:157`
  `Mac macE = Api28Impl.e(cryptoObject);`
- `sources/androidx/biometric/CryptoObjectUtils.java:202`
  `Mac mac = cryptoObject.getMac();`
- `sources/androidx/biometric/CryptoObjectUtils.java:203`
  `if (mac != null) {`
- `sources/androidx/biometric/CryptoObjectUtils.java:204`
  `return Api28Impl.c(mac);`
- `sources/androidx/biometric/CryptoObjectUtils.java:225`
  `Mac mac = cryptoObject.getMac();`
- `sources/androidx/biometric/CryptoObjectUtils.java:226`
  `if (mac != null) {`
- `sources/androidx/biometric/CryptoObjectUtils.java:227`
  `return new FingerprintManagerCompat.CryptoObject(mac);`
- `sources/androidx/browser/customtabs/PostMessageServiceConnection.java:62`
  `intent.setClassName(str, PostMessageService.class.getName());`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:994`
  `return useCase.getName() + useCase.hashCode();`
- `sources/androidx/camera/core/ImageCapture.java:1522`
  `return "ImageCapture:" + getName();`
- `sources/androidx/camera/video/VideoCapture.java:709`
  `return "VideoCapture:" + getName();`
- `sources/androidx/collection/LruCache.java:178`
  `throw new java.lang.IllegalStateException(getClass().getName() + ".sizeOf() is reporting inconsistent results!");`
- `sources/androidx/core/app/NotificationCompat.java:3628`
  `CharSequence name = message.getPerson() == null ? "" : message.getPerson().getName();`
- `sources/androidx/core/app/NotificationCompat.java:3630`
  `name = this.mUser.getName();`
- `sources/androidx/core/app/NotificationCompat.java:3645`
  `bundle.putCharSequence(NotificationCompat.EXTRA_SELF_DISPLAY_NAME, this.mUser.getName());`
- `sources/androidx/core/app/NotificationCompat.java:3690`
  `Notification$MessagingStyle notification$MessagingStyle = i2 >= 28 ? new Notification$MessagingStyle(this.mUser.toAndroidPerson()) : new Notification$MessagingStyle(this.mUser.getName());`
- `sources/androidx/core/app/NotificationCompat.java:3778`
  `return this.mUser.getName();`
- `sources/androidx/core/app/NotificationCompat.java:4018`
  `if (!TextUtils.isEmpty(person.getName())) {`
- `sources/androidx/core/content/FileProvider.java:217`
  `String name = xmlResourceParserA.getName();`
- `sources/androidx/core/graphics/WeightTypefaceApi14.java:32`
  `Log.e(TAG, e2.getClass().getName(), e2);`
- `sources/androidx/core/util/DebugUtils.java:19`
  `if (simpleName.length() <= 0 && (iLastIndexOf = (simpleName = obj.getClass().getName()).lastIndexOf(46)) > 0) {`
- `sources/androidx/core/view/accessibility/AccessibilityNodeInfoCompat.java:258`
  `Log.e(TAG, "Failed to execute command with argument class ViewCommandArgument: " + (cls2 == null ? StringUtils.NULL_USER_ID_SUBSTITUTE_STRING : cls2.getName()), e);`
- `sources/androidx/lifecycle/ClassesInfoCache.java:107`
  `return (this.f3403a * 31) + this.f3404b.getName().hashCode();`
- `sources/androidx/savedstate/SavedStateRegistry.java:203`
  `String name = clazz.getName();`
- `sources/cl/json/social/TargetChosenReceiver.java:28`
  `sTargetChosenReceiveAction = reactContext.getPackageName() + "/" + TargetChosenReceiver.class.getName() + "_ACTION";`
- `sources/com/airbnb/android/react/lottie/LottieAnimationViewManager.java:90`
  `public String getName() {`
- `sources/com/airbnb/lottie/animation/content/GradientFillContent.java:67`
  `this.name = gradientFill.getName();`
- `sources/com/airbnb/lottie/animation/content/GradientStrokeContent.java:44`
  `this.name = gradientStroke.getName();`
- `sources/com/appsflyer/internal/AFc1lSDK.java:144`
  `sb.append(file2.getName());`
- `sources/com/appsflyer/internal/AFc1lSDK.java:147`
  `sb2.append(file2.getName());`
- `sources/com/appsflyer/internal/AFc1lSDK.java:173`
  `sb.append(file2.getName());`
- `sources/com/appsflyer/reactnative/RNAppsFlyerModule.java:322`
  `public String getName() {`
- `sources/com/auth0/android/result/UserProfile.java:125`
  `public final String getName() {`
- `sources/com/braintreepayments/api/AnalyticsClient.java:165`
  `JSONObject jSONObjectPut = new JSONObject().put(KIND_KEY, analyticsEvent.getName()).put("timestamp", analyticsEvent.getTimestamp());`
- `sources/com/bumptech/glide/Glide.java:457`
  `throw new IllegalStateException("Attempting to register a Glide v3 module. If you see this, you or one of your dependencies may be including Glide v3 even though you're using Glide v4. You'll need to find and remove (or update) the offending dependency. The v3 module name is: " + glideModule.getClas...`
- `sources/com/bumptech/glide/load/engine/ResourceCacheKey.java:42`
  `byte[] bytes = this.decodedResourceClass.getName().getBytes(Key.CHARSET);`
- `sources/com/cardinalcommerce/a/CardinalRenderType.java:104`
  `throw new IllegalArgumentException("Invalid value for MAC size: ".concat(String.valueOf(i2)));`
- `sources/com/cardinalcommerce/a/setCompoundDrawablePadding.java:81`
  `this.getWarnings = setLinkTextColor.init(defaultAdapter2.getName());`
- `sources/com/cardinalcommerce/a/setCompoundDrawablePadding.java:124`
  `jSONObject.putOpt("DeviceName", setLinkTextColor.getInstance(this.getWarnings));`
- `sources/com/cardinalcommerce/a/setTypeface.java:31`
  `arrayList.add(setLinkTextColor.init(it.next().getName()));`
- `sources/com/cardinalcommerce/dependencies/internal/bouncycastle/jcajce/provider/asymmetric/ec/KeyAgreementSpi.java:412`
  `String name3 = KeyLengthException.class.getName();`
- `sources/com/facebook/common/references/CloseableReference.java:56`
  `objArr[2] = obj == null ? null : obj.getClass().getName();`
- `sources/com/facebook/common/references/DefaultCloseableReference.java:29`
  `objArr[2] = t2 == null ? null : t2.getClass().getName();`
- `sources/com/facebook/common/references/FinalizerCloseableReference.java:38`
  `objArr[2] = t2 == null ? null : t2.getClass().getName();`
- `sources/com/facebook/imagepipeline/cache/DefaultCacheKeyFactory.java:49`
  `name = postprocessor.getClass().getName();`
- `sources/com/facebook/imagepipeline/core/CloseableReferenceFactory.java:25`
  `FLog.w("Fresco", "Finalized without closing: %x %x (type = %s).\nStack:\n%s", Integer.valueOf(System.identityHashCode(this)), Integer.valueOf(System.identityHashCode(sharedReference)), obj != null ? obj.getClass().getName() : "<value is null>", CloseableReferenceFactory.getStackTraceString(th));`
- `sources/com/facebook/imagepipeline/request/BasePostprocessor.java:45`
  `public String getName() {`
- `sources/com/facebook/imagepipeline/request/Postprocessor.java:13`
  `String getName();`
- `sources/com/facebook/react/CoreModulesPackage.java:113`
  `map.put(reactModule.name(), new ReactModuleInfo(reactModule.name(), cls.getName(), reactModule.canOverrideExistingModule(), reactModule.needsEagerInit(), reactModule.hasConstants(), reactModule.isCxxModule(), TurboModule.class.isAssignableFrom(cls)));`
- `sources/com/facebook/react/ReactInstanceManagerBuilder.java:149`
  `String friendlyDeviceName = AndroidInfoHelpers.getFriendlyDeviceName();`
- `sources/com/facebook/react/ReactInstanceManagerBuilder.java:154`
  `JavaScriptExecutorFactory defaultJSExecutorFactory = javaScriptExecutorFactory == null ? getDefaultJSExecutorFactory(packageName, friendlyDeviceName, application.getApplicationContext()) : javaScriptExecutorFactory;`
- `sources/com/facebook/react/bridge/JavaModuleWrapper.java:59`
  `String name = method.getName();`
- `sources/com/facebook/react/bridge/JavaModuleWrapper.java:61`
  `throw new IllegalArgumentException("Java Module " + getName() + " method name already registered: " + name);`
- `sources/com/facebook/react/bridge/JSCJavaScriptExecutorFactory.java:6`
  `private final String mDeviceName;`
- `sources/com/facebook/react/bridge/JSCJavaScriptExecutorFactory.java:10`
  `this.mDeviceName = str2;`
- `sources/com/facebook/react/bridge/JSCJavaScriptExecutorFactory.java:18`
  `writableNativeMap.putString("DeviceIdentity", this.mDeviceName);`
- `sources/com/facebook/react/bridge/NativeModuleRegistry.java:46`
  `ReactSoftExceptionLogger.logSoftException(this.TAG, new ReactNoCrashSoftException("Registering legacy NativeModule: Cxx NativeModule (name = \"" + entry.getValue().getName() + "\", className = " + entry.getValue().getClassName() + ")."));`
- `sources/com/facebook/react/bridge/NativeModuleRegistry.java:59`
  `ReactSoftExceptionLogger.logSoftException(this.TAG, new ReactNoCrashSoftException("Registering legacy NativeModule: Java NativeModule (name = \"" + entry.getValue().getName() + "\", className = " + entry.getValue().getClassName() + ")."));`
- `sources/com/facebook/react/devsupport/DevServerHelper.java:154`
  `return String.format(Locale.US, "http://%s/inspector/device?name=%s&app=%s", this.mSettings.getPackagerConnectionSettings().getInspectorServerHost(), AndroidInfoHelpers.getFriendlyDeviceName(), this.mPackageName);`
- `sources/com/facebook/react/jscexecutor/JSCExecutorFactory.java:10`
  `private final String mDeviceName;`
- `sources/com/facebook/react/jscexecutor/JSCExecutorFactory.java:14`
  `this.mDeviceName = str2;`
- `sources/com/facebook/react/jscexecutor/JSCExecutorFactory.java:22`
  `writableNativeMap.putString("DeviceIdentity", this.mDeviceName);`
- `sources/com/facebook/react/modules/core/DeviceEventManagerModule.java:54`
  `public String getName() {`
- `sources/com/facebook/react/modules/deviceinfo/DeviceInfoModule.java:61`
  `public String getName() {`
- `sources/com/facebook/react/modules/fresco/FrescoModule.java:69`
  `public String getName() {`
- `sources/com/facebook/react/modules/systeminfo/AndroidInfoHelpers.java:25`
  `public static String getFriendlyDeviceName() {`
- `sources/com/facebook/react/packagerconnection/JSPackagerClient.java:108`
  `builder.scheme("ws").encodedAuthority(packagerConnectionSettings.getDebugServerHost()).appendPath("message").appendQueryParameter("device", AndroidInfoHelpers.getFriendlyDeviceName()).appendQueryParameter(App.TYPE, packagerConnectionSettings.getPackageName()).appendQueryParameter("clientid", str);`
- `sources/com/facebook/react/uimanager/ViewHierarchyDumper.java:17`
  `jSONObject.put(Constants.APPBOY_PUSH_CUSTOM_NOTIFICATION_ID, view.getClass().getName());`
- `sources/com/facebook/react/uimanager/ViewManagerPropertyUpdater.java:81`
  `String name = cls.getName();`
- `sources/com/google/android/gms/internal/common/zzy.java:32`
  `String str2 = obj.getClass().getName() + '@' + Integer.toHexString(System.identityHashCode(obj));`
- `sources/com/google/android/gms/internal/common/zzy.java:34`
  `string = "<" + str2 + " threw " + e2.getClass().getName() + ">";`
- `sources/com/google/android/gms/internal/location/zzbs.java:30`
  `String name = obj.getClass().getName();`
- `sources/com/google/android/gms/internal/mlkit_common/zzad.java:30`
  `String str2 = obj.getClass().getName() + '@' + Integer.toHexString(System.identityHashCode(obj));`

## BR066

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/work/impl/foreground/SystemForegroundDispatcher.java:140`
  `this.mWorkManagerImpl.cancelWorkById(UUID.fromString(stringExtra));`

## BR067

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/androidx/camera/view/CameraController.java:868`
  `public void setPinchToZoomEnabled(boolean z2) {`
- `sources/com/appboy/ui/contentcards/view/BaseContentCardView.java:28`
  `contentCardViewHolder.setPinnedIconVisible(t2.getIsPinned());`
- `sources/com/appboy/ui/contentcards/view/ContentCardViewHolder.java:52`
  `public void setPinnedIconVisible(boolean z2) {`
- `sources/okhttp3/OkHttpClient.java:134`
  `@Metadata(d1 = {"\u0000ø\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0018...`
- `sources/okhttp3/OkHttpClient.java:589`
  `setPingInterval$okhttp(Util.checkDuration("interval", interval, unit));`

## BR068

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/com/auth0/android/authentication/AuthenticationAPIClient.java:17`
  `import com.auth0.android.result.Challenge;`
- `sources/com/auth0/android/authentication/AuthenticationAPIClient.java:38`
  `@Metadata(d1 = {"\u0000\u0080\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0...`
- `sources/com/auth0/android/authentication/AuthenticationAPIClient.java:186`
  `@Metadata(d1 = {"\u0000\u001e\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b!\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\b\u0082\u0003\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002J\u000e\u0010%\u001a\b\u0012\u0004\u0012\u00020'0&H\u000...`
- `sources/com/auth0/android/authentication/AuthenticationAPIClient.java:441`
  `public final Request<Challenge, AuthenticationException> multifactorChallenge(@NotNull String mfaToken, @Nullable String challengeType, @Nullable String authenticatorId) {`
- `sources/com/auth0/android/authentication/AuthenticationAPIClient.java:443`
  `Map<String, String> mapAsDictionary = ParameterBuilder.Companion.newBuilder$default(ParameterBuilder.INSTANCE, null, 1, null).setClientId(getClientId()).set(MFA_TOKEN_KEY, mfaToken).set(CHALLENGE_TYPE_KEY, challengeType).set(AUTHENTICATOR_ID_KEY, authenticatorId).asDictionary();`
- `sources/com/auth0/android/authentication/AuthenticationAPIClient.java:444`
  `HttpUrl httpUrlBuild = HttpUrl.INSTANCE.get(this.auth0.getDomainUrl()).newBuilder().addPathSegment(MFA_PATH).addPathSegment(CHALLENGE_PATH).build();`
- `sources/com/auth0/android/authentication/AuthenticationAPIClient.java:445`
  `return this.factory.post(httpUrlBuild.getUrl(), new GsonAdapter(Challenge.class, this.gson)).addParameters(mapAsDictionary);`
- `sources/com/auth0/android/authentication/storage/SecureCredentialsManager.java:224`
  `callback.onFailure(new CredentialsManagerException("The user didn't pass the authentication challenge.", null, 2, null));`
- `sources/com/auth0/android/provider/PKCE.java:47`
  `this.codeChallenge = algorithmHelper.a(strB);`
- `sources/com/auth0/android/result/Challenge.java:10`
  `/* JADX INFO: compiled from: Challenge.kt */`
- `sources/com/auth0/android/result/Challenge.java:12`
  `@Metadata(d1 = {"\u0000\u0012\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0002\b\b\u0018\u00002\u00020\u0001B!\u0012\u0006\u0010\u0002\u001a\u00020\u0003\u0012\b\u0010\u0004\u001a\u0004\u0018\u00010\u0003\u0012\b\u0010\u0005\u001a\u0004\u0018\u00010\u0003¢\u0006\u0002\u001...`
- `sources/com/auth0/android/result/Challenge.java:13`
  `public final class Challenge {`
- `sources/com/auth0/android/result/Challenge.java:19`
  `@SerializedName("challenge_type")`
- `sources/com/auth0/android/result/Challenge.java:22`
  `private final String challengeType;`
- `sources/com/auth0/android/result/Challenge.java:28`
  `public Challenge(@NotNull String challengeType, @Nullable String str, @Nullable String str2) {`
- `sources/com/auth0/android/result/Challenge.java:29`
  `Intrinsics.checkNotNullParameter(challengeType, "challengeType");`
- `sources/com/auth0/android/result/Challenge.java:30`
  `this.challengeType = challengeType;`
- `sources/com/auth0/android/result/Challenge.java:41`
  `public final String getChallengeType() {`
- `sources/com/auth0/android/result/Challenge.java:42`
  `return this.challengeType;`
- `sources/com/auth0/react/A0Auth0Module.java:82`
  `String generateCodeChallenge(@NonNull String str) {`
- `sources/com/auth0/react/A0Auth0Module.java:168`
  `writableMapCreateMap.putString("code_challenge", generateCodeChallenge(strGenerateRandomValue));`
- `sources/com/auth0/react/A0Auth0Module.java:169`
  `writableMapCreateMap.putString("code_challenge_method", "S256");`
- `sources/com/babylon/cyrus/R.java:4504`
  `public static final int activity_multi_select_challenge_view = 0x7f0c001d;`
- `sources/com/babylon/cyrus/R.java:4505`
  `public static final int activity_oob_challenge_view = 0x7f0c001e;`
- `sources/com/babylon/cyrus/R.java:4506`
  `public static final int activity_otp_challenge_view = 0x7f0c001f;`
- `sources/com/babylon/cyrus/R.java:4507`
  `public static final int activity_single_select_challenge_view = 0x7f0c0020;`
- `sources/com/babylon/cyrus/R.java:4701`
  `public static final int onfido_challenge_digits = 0x7f0c00e2;`
- `sources/com/babylon/cyrus/R.java:4702`
  `public static final int onfido_challenge_movement = 0x7f0c00e3;`
- `sources/com/babylon/cyrus/R.java:4703`
  `public static final int onfido_challenge_review_digits = 0x7f0c00e4;`
- `sources/com/babylon/cyrus/R.java:4704`
  `public static final int onfido_challenge_review_movement = 0x7f0c00e5;`
- `sources/com/babylon/cyrus/R.java:5853`
  `public static final int singe_select_challenge_info = 0x7f110353;`
- `sources/com/babylon/cyrus/R.java:5855`
  `public static final int ss_challengeinfo_lable = 0x7f110355;`
- `sources/com/braintreepayments/api/CardDetailsFragment.java:43`
  `CardFormConfiguration cardFormConfiguration = new CardFormConfiguration(configuration.isCvvChallengePresent(), configuration.isPostalCodeChallengePresent());`
- `sources/com/braintreepayments/api/Configuration.java:109`
  `private final Set<String> challenges;`
- `sources/com/braintreepayments/api/Configuration.java:155`
  `private final boolean isCvvChallengePresent;`
- `sources/com/braintreepayments/api/Configuration.java:171`
  `private final boolean isPostalCodeChallengePresent;`
- `sources/com/braintreepayments/api/Configuration.java:347`
  `this.isCvvChallengePresent = this.challenges.contains("cvv");`
- `sources/com/braintreepayments/api/Configuration.java:350`
  `this.isPostalCodeChallengePresent = this.challenges.contains(PostalAddressParser.POSTAL_CODE_UNDERSCORE_KEY);`
- `sources/com/braintreepayments/api/Configuration.java:586`
  `public boolean isCvvChallengePresent() {`
- `sources/com/braintreepayments/api/Configuration.java:587`
  `return this.isCvvChallengePresent;`
- `sources/com/braintreepayments/api/Configuration.java:624`
  `public boolean isPostalCodeChallengePresent() {`
- `sources/com/braintreepayments/api/Configuration.java:625`
  `return this.isPostalCodeChallengePresent;`
- `sources/com/braintreepayments/api/ThreeDSecureClient.java:169`
  `this.braintreeClient.sendAnalyticsEvent(String.format("three-d-secure.verification-flow.challenge-presented.%b", Boolean.valueOf(z2)));`
- `sources/com/braintreepayments/api/ThreeDSecureClient.java:230`
  `public void initializeChallengeWithLookupResponse(@NonNull FragmentActivity fragmentActivity, @NonNull String str) {`
- `sources/com/braintreepayments/api/ThreeDSecureClient.java:231`
  `initializeChallengeWithLookupResponse(fragmentActivity, str, new ThreeDSecureResultCallback() { // from class: com.braintreepayments.api.ThreeDSecureClient.4`
- `sources/com/braintreepayments/api/ThreeDSecureClient.java:453`
  `public void initializeChallengeWithLookupResponse(@NonNull FragmentActivity fragmentActivity, @Nullable ThreeDSecureRequest threeDSecureRequest, @NonNull String str) {`
- `sources/com/braintreepayments/api/ThreeDSecureClient.java:454`
  `initializeChallengeWithLookupResponse(fragmentActivity, threeDSecureRequest, str, new ThreeDSecureResultCallback() { // from class: com.braintreepayments.api.ThreeDSecureClient.5`
- `sources/com/braintreepayments/api/ThreeDSecureClient.java:472`
  `public void initializeChallengeWithLookupResponse(@NonNull FragmentActivity fragmentActivity, @NonNull String str, @NonNull ThreeDSecureResultCallback threeDSecureResultCallback) {`
- `sources/com/braintreepayments/api/ThreeDSecureClient.java:473`
  `initializeChallengeWithLookupResponse(fragmentActivity, null, str, threeDSecureResultCallback);`
- `sources/com/braintreepayments/api/ThreeDSecureClient.java:488`
  `public void initializeChallengeWithLookupResponse(@NonNull final FragmentActivity fragmentActivity, @Nullable final ThreeDSecureRequest threeDSecureRequest, @NonNull final String str, @NonNull final ThreeDSecureResultCallback threeDSecureResultCallback) {`
- `sources/com/braintreepayments/api/ThreeDSecureRequest.java:198`
  `public Boolean isCardAddChallengeRequested() {`
- `sources/com/braintreepayments/api/ThreeDSecureRequest.java:199`
  `return this.cardAddChallengeRequested;`
- `sources/com/braintreepayments/api/ThreeDSecureRequest.java:202`
  `public boolean isChallengeRequested() {`
- `sources/com/braintreepayments/api/ThreeDSecureRequest.java:203`
  `return this.challengeRequested;`
- `sources/com/braintreepayments/api/ThreeDSecureRequest.java:230`
  `public void setCardAddChallengeRequested(@Nullable Boolean bool) {`
- `sources/com/braintreepayments/api/ThreeDSecureRequest.java:231`
  `this.cardAddChallengeRequested = bool;`
- `sources/com/braintreepayments/api/ThreeDSecureRequest.java:234`
  `public void setChallengeRequested(boolean z2) {`
- `sources/com/braintreepayments/api/ThreeDSecureRequest.java:235`
  `this.challengeRequested = z2;`
- `sources/com/braintreepayments/api/ThreeDSecureRequest.java:296`
  `parcel.writeByte(this.challengeRequested ? (byte) 1 : (byte) 0);`
- `sources/com/braintreepayments/api/ThreeDSecureRequest.java:300`
  `parcel.writeSerializable(this.cardAddChallengeRequested);`
- `sources/com/braintreepayments/api/ThreeDSecureRequest.java:308`
  `this.challengeRequested = false;`
- `sources/com/braintreepayments/api/ThreeDSecureRequest.java:319`
  `this.challengeRequested = parcel.readByte() > 0;`
- `sources/com/braintreepayments/api/ThreeDSecureRequest.java:323`
  `this.cardAddChallengeRequested = (Boolean) parcel.readSerializable();`
- `sources/com/braintreepayments/api/dropin/R.java:2710`
  `public static final int challenge_labelview_cf = 0x7f0c0041;`
- `sources/com/braintreepayments/api/dropin/R.java:2711`
  `public static final int challenge_multiselect_body_view = 0x7f0c0042;`
- `sources/com/braintreepayments/api/dropin/R.java:2712`
  `public static final int challenge_oob_body_view = 0x7f0c0043;`
- `sources/com/braintreepayments/api/dropin/R.java:2713`
  `public static final int challenge_otp_body_view = 0x7f0c0044;`
- `sources/com/braintreepayments/api/dropin/R.java:2714`
  `public static final int challenge_single_selectbody = 0x7f0c0045;`
- `sources/com/braintreepayments/api/dropin/R.java:2715`
  `public static final int challenge_toolbar_cf = 0x7f0c0046;`
- `sources/com/braintreepayments/api/dropin/R.java:3048`
  `public static final int singe_select_challenge_info = 0x7f110353;`
- `sources/com/braintreepayments/api/dropin/R.java:3049`
  `public static final int ss_challengeinfo_lable = 0x7f110355;`
- `sources/com/braintreepayments/api/threedsecure/R.java:1170`
  `public static final int singe_select_challenge_info = 0x7f110353;`
- `sources/com/braintreepayments/api/threedsecure/R.java:1171`
  `public static final int ss_challengeinfo_lable = 0x7f110355;`
- `sources/com/bupa/digitalprimarycare/R.java:4367`
  `public static final int activity_multi_select_challenge_view = 0x7f0c001d;`
- `sources/com/bupa/digitalprimarycare/R.java:4368`
  `public static final int activity_oob_challenge_view = 0x7f0c001e;`
- `sources/com/bupa/digitalprimarycare/R.java:4369`
  `public static final int activity_otp_challenge_view = 0x7f0c001f;`
- `sources/com/bupa/digitalprimarycare/R.java:4370`
  `public static final int activity_single_select_challenge_view = 0x7f0c0020;`
- `sources/com/bupa/digitalprimarycare/R.java:4564`
  `public static final int onfido_challenge_digits = 0x7f0c00e2;`
- `sources/com/bupa/digitalprimarycare/R.java:4565`
  `public static final int onfido_challenge_movement = 0x7f0c00e3;`
- `sources/com/bupa/digitalprimarycare/R.java:4566`
  `public static final int onfido_challenge_review_digits = 0x7f0c00e4;`

## BR069

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/com/nimbusds/jose/crypto/PBKDF2.java:45`
  `private static byte[] extractBlock(byte[] bArr, int i2, int i3, Mac mac) {`
- `sources/okio/HashingSink.java:169`
  `Intrinsics.checkNotNull(mac);`
- `sources/okio/HashingSink.java:170`
  `result = mac.doFinal();`
- `sources/okio/HashingSink.java:189`
  `Mac mac = this.mac;`
- `sources/okio/HashingSink.java:190`
  `Intrinsics.checkNotNull(mac);`
- `sources/okio/HashingSink.java:191`
  `mac.update(segment.data, segment.pos, iMin);`

## BR070

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/okhttp3/EventListener.java:18`
  `@Metadata(d1 = {"\u0000z\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004...`
- `sources/okhttp3/logging/LoggingEventListener.java:29`
  `@Metadata(d1 = {"\u0000z\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\t\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0000\n\u0002\u00...`

## BR072

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:310`
  `android:name="io.sentry.auto-init"`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:649`
  `android:name="io.sentry.android.core.SentryInitProvider"`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:653`
  `android:name="io.sentry.android.core.SentryPerformanceProvider"`
- `sources/androidx/activity/result/PickVisualMediaRequest.java:4`
  `import io.sentry.protocol.OperatingSystem;`
- `sources/androidx/appcompat/app/AppCompatDelegate.java:37`
  `import io.sentry.protocol.Device;`
- `sources/androidx/appcompat/app/AppLocalesStorageHelper.java:7`
  `import io.sentry.protocol.Device;`
- `sources/androidx/camera/video/internal/DebugUtils.java:18`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/camera/view/SurfaceViewImplementation.java:25`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/camera/view/TextureViewImplementation.java:24`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/constraintlayout/motion/widget/KeyAttributes.java:11`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/constraintlayout/motion/widget/KeyCycle.java:12`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/constraintlayout/motion/widget/KeyCycleOscillator.java:11`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/constraintlayout/motion/widget/KeyTimeCycle.java:11`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/constraintlayout/motion/widget/MotionConstrainedPoint.java:13`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/constraintlayout/motion/widget/MotionPaths.java:9`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/constraintlayout/motion/widget/SplineSet.java:11`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/constraintlayout/motion/widget/TimeCycleSplineSet.java:11`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/constraintlayout/solver/LinearSystem.java:7`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/core/app/LocaleManagerCompat.java:16`
  `import io.sentry.protocol.Device;`
- `sources/androidx/core/content/ContextKt.java:9`
  `import io.sentry.Session;`
- `sources/androidx/core/content/IntentCompat.java:12`
  `import io.sentry.protocol.SentryStackFrame;`
- `sources/androidx/core/content/PackageManagerCompat.java:18`
  `import io.sentry.protocol.SentryStackFrame;`
- `sources/androidx/core/graphics/BitmapKt.java:12`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/core/graphics/CanvasKt.java:9`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/core/graphics/ColorKt.java:8`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/core/graphics/drawable/IconCompat.java:47`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/core/location/LocationManagerCompat.java:29`
  `import io.sentry.protocol.OperatingSystem;`
- `sources/androidx/core/text/SpannableStringBuilderKt.java:15`
  `import io.sentry.protocol.SentryTransaction;`
- `sources/androidx/core/util/SizeFCompat.java:7`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/core/view/DisplayCompat.java:16`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/core/view/MenuKt.java:5`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/core/view/ViewGroupKt.java:10`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/dynamicanimation/animation/DynamicAnimation.java:12`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/exifinterface/media/ExifInterface.java:29`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/fragment/app/FragmentContainerView.java:20`
  `import io.sentry.Session;`
- `sources/androidx/fragment/app/FragmentLayoutInflaterFactory.java:14`
  `import io.sentry.protocol.Request;`
- `sources/androidx/fragment/app/FragmentTransactionKt.java:5`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/fragment/app/strictmode/FragmentReuseViolation.java:4`
  `import io.sentry.protocol.Request;`
- `sources/androidx/fragment/app/strictmode/FragmentStrictMode.java:15`
  `import io.sentry.protocol.OperatingSystem;`
- `sources/androidx/fragment/app/strictmode/FragmentStrictMode.java:16`
  `import io.sentry.protocol.Request;`
- `sources/androidx/fragment/app/strictmode/FragmentTagUsageViolation.java:5`
  `import io.sentry.protocol.Request;`
- `sources/androidx/fragment/app/strictmode/GetRetainInstanceUsageViolation.java:4`
  `import io.sentry.protocol.Request;`
- `sources/androidx/fragment/app/strictmode/GetTargetFragmentRequestCodeUsageViolation.java:4`
  `import io.sentry.protocol.Request;`
- `sources/androidx/fragment/app/strictmode/GetTargetFragmentUsageViolation.java:4`
  `import io.sentry.protocol.Request;`
- `sources/androidx/fragment/app/strictmode/RetainInstanceUsageViolation.java:4`
  `import io.sentry.protocol.Request;`
- `sources/androidx/fragment/app/strictmode/SetRetainInstanceUsageViolation.java:4`
  `import io.sentry.protocol.Request;`
- `sources/androidx/fragment/app/strictmode/SetTargetFragmentUsageViolation.java:4`
  `import io.sentry.protocol.Request;`
- `sources/androidx/fragment/app/strictmode/SetUserVisibleHintViolation.java:4`
  `import io.sentry.protocol.Request;`
- `sources/androidx/fragment/app/strictmode/TargetFragmentUsageViolation.java:4`
  `import io.sentry.protocol.Request;`
- `sources/androidx/fragment/app/strictmode/Violation.java:4`
  `import io.sentry.protocol.Request;`
- `sources/androidx/fragment/app/strictmode/WrongFragmentContainerViolation.java:5`
  `import io.sentry.protocol.Request;`
- `sources/androidx/lifecycle/ViewModelProvider.java:13`
  `import io.sentry.protocol.App;`
- `sources/androidx/lifecycle/viewmodel/InitializerViewModelFactoryBuilder.java:6`
  `import io.sentry.protocol.OperatingSystem;`
- `sources/androidx/room/util/TableInfo.java:10`
  `import io.sentry.Session;`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:41`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:29`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/work/impl/model/WorkSpec.java:22`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/androidx/work/impl/model/WorkTag.java:9`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/bo/app/f3.java:7`
  `import io.sentry.TraceContext;`
- `sources/bo/app/g4.java:23`
  `import io.sentry.TraceContext;`
- `sources/bo/app/g4.java:24`
  `import io.sentry.protocol.Device;`
- `sources/bo/app/q1.java:23`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/bo/app/q2.java:6`
  `import io.sentry.TraceContext;`
- `sources/bo/app/q3.java:8`
  `import io.sentry.TraceContext;`
- `sources/bo/app/r2.java:4`
  `import io.sentry.TraceContext;`
- `sources/bo/app/s2.java:15`
  `import io.sentry.TraceContext;`
- `sources/bo/app/w2.java:9`
  `import io.sentry.clientreport.DiscardedEvent;`
- `sources/cl/json/social/ShareIntent.java:25`
  `import io.sentry.SentryLockReason;`
- `sources/com/airbnb/android/react/maps/AirMapManager.java:24`
  `import io.sentry.protocol.Geo;`
- `sources/com/airbnb/android/react/maps/AirMapMarkerManager.java:23`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/com/airbnb/android/react/maps/AirMapModule.java:33`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/com/airbnb/android/react/maps/AirMapView.java:61`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/com/airbnb/android/react/maps/RegionChangeEvent.java:10`
  `import io.sentry.protocol.Geo;`
- `sources/com/airbnb/lottie/parser/AnimatablePathValueParser.java:12`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/com/airbnb/lottie/parser/JsonUtils.java:7`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/com/airbnb/lottie/parser/KeyframeParser.java:16`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/com/airbnb/lottie/parser/PolystarShapeParser.java:9`
  `import io.sentry.protocol.OperatingSystem;`
- `sources/com/airbnb/lottie/value/ScaleXY.java:3`
  `import io.sentry.protocol.ViewHierarchyNode;`
- `sources/com/android/installreferrer/api/InstallReferrerClientImpl.java:14`
  `import io.sentry.SentryLockReason;`
- `sources/com/appboy/enums/DeviceKey.java:5`
  `import io.sentry.protocol.Device;`

## BR073

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/android/graphics/ImageDecoder.java:11`
  `public final /* synthetic */ class ImageDecoder implements AutoCloseable {`
- `sources/android/graphics/ImageDecoder.java:51`
  `public static native /* synthetic */ Bitmap decodeBitmap(@NonNull Source source, @NonNull OnHeaderDecodedListener onHeaderDecodedListener) throws IOException;`
- `sources/android/graphics/ImageDecoder.java:54`
  `public static native /* synthetic */ Drawable decodeDrawable(@NonNull Source source, @NonNull OnHeaderDecodedListener onHeaderDecodedListener) throws IOException;`
- `sources/androidx/appcompat/graphics/drawable/DrawableContainerCompat.java:12`
  `import android.util.SparseArray;`
- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:551`
  `this.mDecorToolbar.saveHierarchyState(sparseArray);`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:340`
  `java.lang.String r5 = r2.getAttributeValue(r6, r5)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:342`
  `java.lang.String r7 = r2.getAttributeValue(r6, r7)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:343`
  `long r7 = java.lang.Long.parseLong(r7)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:345`
  `java.lang.String r6 = r2.getAttributeValue(r6, r9)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:346`
  `float r6 = java.lang.Float.parseFloat(r6)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:347`
  `androidx.appcompat.widget.ActivityChooserModel$HistoricalRecord r9 = new androidx.appcompat.widget.ActivityChooserModel$HistoricalRecord     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:348`
  `r9.<init>(r5, r7, r6)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:349`
  `r3.add(r9)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/browser/trusted/TokenContents.java:86`
  `private void parseIfNeeded() throws IOException {`
- `sources/androidx/browser/trusted/TokenContents.java:116`
  `parseIfNeeded();`
- `sources/androidx/browser/trusted/TokenContents.java:125`
  `parseIfNeeded();`
- `sources/androidx/camera/camera2/internal/Camera2CaptureOptionUnpacker.java:23`
  `@Override // androidx.camera.core.impl.CaptureConfig.OptionUnpacker`
- `sources/androidx/camera/camera2/internal/Camera2CaptureOptionUnpacker.java:25`
  `public void unpack(@NonNull UseCaseConfig<?> useCaseConfig, @NonNull CaptureConfig.Builder builder) {`
- `sources/androidx/camera/camera2/internal/Camera2SessionOptionUnpacker.java:25`
  `@Override // androidx.camera.core.impl.SessionConfig.OptionUnpacker`
- `sources/androidx/camera/camera2/internal/Camera2SessionOptionUnpacker.java:27`
  `public void unpack(@NonNull UseCaseConfig<?> useCaseConfig, @NonNull SessionConfig.Builder builder) {`
- `sources/androidx/camera/camera2/internal/Camera2UseCaseConfigFactory.java:74`
  `mutableOptionsBundleCreate.insertOption(UseCaseConfig.OPTION_SESSION_CONFIG_UNPACKER, Camera2SessionOptionUnpacker.f822a);`
- `sources/androidx/camera/camera2/internal/Camera2UseCaseConfigFactory.java:85`
  `mutableOptionsBundleCreate.insertOption(UseCaseConfig.OPTION_CAPTURE_CONFIG_UNPACKER, captureType == UseCaseConfigFactory.CaptureType.IMAGE_CAPTURE ? ImageCaptureOptionUnpacker.f860b : Camera2CaptureOptionUnpacker.f816a);`
- `sources/androidx/camera/camera2/internal/SupportedSurfaceCombination.java:279`
  `int i2 = Integer.parseInt(this.mCameraId);`
- `sources/androidx/camera/core/ImageCapture.java:573`
  `d(1, "Unable to parse JPEG exif", e2);`
- `sources/androidx/camera/core/VideoCapture.java:897`
  `int r5 = java.lang.Integer.parseInt(r9)     // Catch: java.lang.NumberFormatException -> L3d`
- `sources/androidx/camera/core/impl/utils/Exif.java:16`
  `import java.text.ParseException;`
- `sources/androidx/camera/core/impl/utils/Exif.java:146`
  `private long parseTimestamp(@Nullable String str, @Nullable String str2) {`
- `sources/androidx/camera/core/impl/utils/Exif.java:268`
  `long timestamp = parseTimestamp(this.mExifInterface.getAttribute(ExifInterface.TAG_DATETIME));`
- `sources/androidx/camera/core/impl/utils/Exif.java:496`
  `private long parseTimestamp(@Nullable String str) {`
- `sources/androidx/camera/core/impl/utils/ExifAttribute.java:135`
  `return Double.parseDouble((String) objA);`
- `sources/androidx/camera/core/impl/utils/ExifAttribute.java:172`
  `return Integer.parseInt((String) objA);`
- `sources/androidx/camera/core/impl/utils/ExifData.java:168`
  `long j2 = Long.parseLong(str);`
- `sources/androidx/camera/core/impl/utils/ExifData.java:171`
  `Double.parseDouble(str);`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:97`
  `BitmapRegionDecoder bitmapRegionDecoderNewInstance = BitmapRegionDecoder.newInstance(bArr, 0, bArr.length, false);`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:98`
  `Bitmap bitmapDecodeRegion = bitmapRegionDecoderNewInstance.decodeRegion(rect, new BitmapFactory.Options());`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:99`
  `bitmapRegionDecoderNewInstance.recycle();`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:100`
  `if (bitmapDecodeRegion == null) {`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:101`
  `throw new CodecFailedException("Decode byte array failed.", CodecFailedException.FailureType.DECODE_FAILED);`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:104`
  `if (!bitmapDecodeRegion.compress(Bitmap.CompressFormat.JPEG, i2, byteArrayOutputStream)) {`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:107`
  `bitmapDecodeRegion.recycle();`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:110`
  `throw new CodecFailedException("Decode byte array failed.", CodecFailedException.FailureType.DECODE_FAILED);`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:112`
  `throw new CodecFailedException("Decode byte array failed with illegal argument." + e2, CodecFailedException.FailureType.DECODE_FAILED);`
- `sources/androidx/camera/video/VideoCaptureLegacy.java:836`
  `int r5 = java.lang.Integer.parseInt(r9)     // Catch: java.lang.NumberFormatException -> L3d`
- `sources/androidx/collection/LongSparseArrayKt.java:15`
  `/* JADX INFO: compiled from: LongSparseArray.kt */`
- `sources/androidx/collection/LongSparseArrayKt.java:17`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000D\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\t\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002...`
- `sources/androidx/collection/LongSparseArrayKt.java:18`
  `public final class LongSparseArrayKt {`
- `sources/androidx/collection/LongSparseArrayKt.java:21`
  `/* JADX INFO: renamed from: androidx.collection.LongSparseArrayKt$valueIterator$1, reason: invalid class name and case insensitive filesystem */`
- `sources/androidx/collection/LongSparseArrayKt.java:22`
  `/* JADX INFO: compiled from: LongSparseArray.kt */`
- `sources/androidx/collection/LongSparseArrayKt.java:23`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000\u001b\n\u0000\n\u0002\u0010(\n\u0000\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0010\u000b\n\u0002\b\u0004*\u0001\u0000\b\n\u0018\u00002\b\u0012\u0004\u0012\u00028\u00000\u0001J\t\u0010\b\u001a\u00020\tH\u0096\u0002J\u0016\u0010\n\u001a\n \u000b*\u0004\u0018\u00...`
- `sources/androidx/collection/LongSparseArrayKt.java:87`
  `public static final <T> int getSize(@NotNull LongSparseArray<T> receiver$0) {`
- `sources/androidx/collection/LongSparseArrayKt.java:92`
  `public static final <T> boolean isNotEmpty(@NotNull LongSparseArray<T> receiver$0) {`
- `sources/androidx/collection/LongSparseArrayKt.java:98`
  `public static final <T> LongIterator keyIterator(@NotNull final LongSparseArray<T> receiver$0) {`
- `sources/androidx/collection/SparseArrayKt.java:15`
  `/* JADX INFO: compiled from: SparseArray.kt */`
- `sources/androidx/collection/SparseArrayKt.java:17`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000@\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0007...`
- `sources/androidx/collection/SparseArrayKt.java:18`
  `public final class SparseArrayKt {`
- `sources/androidx/collection/SparseArrayKt.java:21`
  `/* JADX INFO: renamed from: androidx.collection.SparseArrayKt$valueIterator$1, reason: invalid class name and case insensitive filesystem */`
- `sources/androidx/collection/SparseArrayKt.java:22`
  `/* JADX INFO: compiled from: SparseArray.kt */`
- `sources/androidx/collection/SparseArrayKt.java:23`
  `@Metadata(bv = {1, 0, 3}, d1 = {"\u0000\u001b\n\u0000\n\u0002\u0010(\n\u0000\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0010\u000b\n\u0002\b\u0004*\u0001\u0000\b\n\u0018\u00002\b\u0012\u0004\u0012\u00028\u00000\u0001J\t\u0010\b\u001a\u00020\tH\u0096\u0002J\u0016\u0010\n\u001a\n \u000b*\u0004\u0018\u00...`
- `sources/androidx/collection/SparseArrayKt.java:87`
  `public static final <T> int getSize(@NotNull SparseArrayCompat<T> receiver$0) {`
- `sources/androidx/collection/SparseArrayKt.java:92`
  `public static final <T> boolean isNotEmpty(@NotNull SparseArrayCompat<T> receiver$0) {`
- `sources/androidx/collection/SparseArrayKt.java:98`
  `public static final <T> IntIterator keyIterator(@NotNull final SparseArrayCompat<T> receiver$0) {`
- `sources/androidx/constraintlayout/motion/widget/DesignTool.java:96`
  `constraintSet.setVerticalBias(view.getId(), Float.parseFloat(str));`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:799`
  `sparseArray.put(((View) constraintWidget.getCompanionWidget()).getId(), constraintWidget);`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:807`
  `constraintSet.applyToHelper((ConstraintHelper) view, constraintWidget2, layoutParams, sparseArray);`
- `sources/androidx/constraintlayout/motion/widget/SplineSet.java:309`
  `return new CustomSet(str, sparseArray);`
- `sources/androidx/constraintlayout/motion/widget/TouchResponse.java:15`
  `import org.xmlpull.v1.XmlPullParser;`
- `sources/androidx/constraintlayout/motion/widget/TouchResponse.java:58`
  `TouchResponse(Context context, MotionLayout motionLayout, XmlPullParser xmlPullParser) {`
- `sources/androidx/constraintlayout/motion/widget/TouchResponse.java:60`
  `fillFromAttributeList(context, Xml.asAttributeSet(xmlPullParser));`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:63`
  `private SparseArray<ConstraintWidget> mTempMapIdToWidget;`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:320`
  `this.mChildrenByIds = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:339`
  `this.mTempMapIdToWidget = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:717`
  `int i4 = Integer.parseInt(strArrSplit[0]);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:718`
  `int i5 = Integer.parseInt(strArrSplit[1]);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:719`
  `int i6 = Integer.parseInt(strArrSplit[2]);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:728`
  `float f5 = i8 + ((int) ((Integer.parseInt(strArrSplit[3]) / 1920.0f) * height));`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1172`
  `this.mChildrenByIds = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1191`
  `this.mTempMapIdToWidget = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1200`
  `this.mChildrenByIds = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1219`
  `this.mTempMapIdToWidget = new SparseArray<>();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1229`
  `this.mChildrenByIds = new SparseArray<>();`

## BR074

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/android/support/v4/media/session/MediaControllerCompat.java:1483`
  `synchronized (mediaControllerImplApi21.f92b) {`
- `sources/android/support/v4/os/ResultReceiver.java:110`
  `synchronized (this) {`
- `sources/androidx/activity/ComponentActivity.java:79`
  `public class ComponentActivity extends androidx.core.app.ComponentActivity implements ContextAware, ViewModelStoreOwner, HasDefaultViewModelProviderFactory, SavedStateRegistryOwner, OnBackPressedDispatcherOwner, ActivityResultRegistryOwner, ActivityResultCaller, OnConfigurationChangedProvider, OnTri...`
- `sources/androidx/activity/ComponentActivity.java:162`
  `final ActivityResultContract.SynchronousResult<O> synchronousResult = activityResultContract.getSynchronousResult(componentActivity, i3);`
- `sources/androidx/activity/ComponentActivity.java:163`
  `if (synchronousResult != null) {`
- `sources/androidx/activity/ComponentActivity.java:167`
  `dispatchResult(i2, synchronousResult.getValue());`
- `sources/androidx/activity/ComponentActivity.java:251`
  `savedStateRegistryControllerCreate.performAttach();`
- `sources/androidx/activity/ComponentActivity.java:252`
  `SavedStateHandleSupport.enableSavedStateHandles(this);`
- `sources/androidx/activity/ComponentActivity.java:256`
  `getSavedStateRegistry().registerSavedStateProvider(ACTIVITY_RESULT_TAG, new SavedStateRegistry.SavedStateProvider() { // from class: androidx.activity.c`
- `sources/androidx/activity/ComponentActivity.java:257`
  `@Override // androidx.savedstate.SavedStateRegistry.SavedStateProvider`
- `sources/androidx/activity/ComponentActivity.java:258`
  `public final Bundle saveState() {`
- `sources/androidx/activity/ComponentActivity.java:280`
  `this.mActivityResultRegistry.onSaveInstanceState(bundle);`
- `sources/androidx/activity/ComponentActivity.java:286`
  `Bundle bundleConsumeRestoredStateForKey = getSavedStateRegistry().consumeRestoredStateForKey(ACTIVITY_RESULT_TAG);`
- `sources/androidx/activity/result/ActivityResultRegistry.java:179`
  `public final void onSaveInstanceState(@NonNull Bundle bundle) {`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:14`
  `@Metadata(d1 = {"\u0000.\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\b\u0004\b&\u0018\u0000*\u0004\b\u0000\u0010\u0001*\u0004\b\u0001\u0010\u00022\u...`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:18`
  `@Metadata(d1 = {"\u0000\u000e\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0000\n\u0002\b\u0006\u0018\u0000*\u0004\b\u0002\u0010\u00012\u00020\u0002B\r\u0012\u0006\u0010\u0003\u001a\u00028\u0002¢\u0006\u0002\u0010\u0004R\u0013\u0010\u0003\u001a\u00028\u0002¢\u0006\n\n\u0002\u0010\u0007\u001a\u0004\b\u...`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:19`
  `public static final class SynchronousResult<T> {`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:22`
  `public SynchronousResult(T t2) {`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:35`
  `public SynchronousResult<O> getSynchronousResult(@NotNull Context context, I input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:67`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\b\u0016\u0018\u00002\u000e\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:71`
  `public final ActivityResultContract.SynchronousResult<Boolean> getSynchronousResult(@NotNull Context context, @NotNull Uri input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:97`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0017\u0018\u00002\u0010\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:111`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(@NotNull Context context, @NotNull String input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:148`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0016\u0018\u00002\u0010\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:152`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(@NotNull Context context, @NotNull String input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:184`
  `@Metadata(d1 = {"\u0000:\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\b\u0017\u001...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:230`
  `public final ActivityResultContract.SynchronousResult<List<Uri>> getSynchronousResult(@NotNull Context context, @NotNull String input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:259`
  `@Metadata(d1 = {"\u00006\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0011\n\u0002\u0010\u000e\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\b\u0002\b\u0017\u0018\u00002\u0016\...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:264`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(@NotNull Context context, @NotNull String[] input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:296`
  `@Metadata(d1 = {"\u0000.\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0017\u0018\u00002\u0012\u0012\u0006\u0012\u0004\u0018\u00010\u00...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:301`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(@NotNull Context context, @Nullable Uri input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:333`
  `@Metadata(d1 = {"\u0000>\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0011\n\u0002\u0010\u000e\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:338`
  `public final ActivityResultContract.SynchronousResult<List<Uri>> getSynchronousResult(@NotNull Context context, @NotNull String[] input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:393`
  `@Metadata(d1 = {"\u00008\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\b\u0017\u0018\u0000 ...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:430`
  `public final ActivityResultContract.SynchronousResult<List<Uri>> getSynchronousResult(@NotNull Context context, @NotNull PickVisualMediaRequest input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:484`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\b\b\u0016\u0018\u0000 \u00102\u0010\u0012\u0004\u0012...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:591`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(@NotNull Context context, @NotNull PickVisualMediaRequest input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:634`
  `@Metadata(d1 = {"\u0000>\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0011\n\u0002\u0010\u000e\n\u0002\u0010$\n\u0002\u0010\u000b\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:679`
  `public ActivityResultContract.SynchronousResult<Map<String, Boolean>> getSynchronousResult(@NotNull Context context, @NotNull String[] input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:684`
  `return new ActivityResultContract.SynchronousResult<>(MapsKt__MapsKt.emptyMap());`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:706`
  `return new ActivityResultContract.SynchronousResult<>(linkedHashMap);`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:732`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000e\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\u0018\u00002\u000e\u0012\u0004\u0012\u00020\u00...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:744`
  `public ActivityResultContract.SynchronousResult<Boolean> getSynchronousResult(@NotNull Context context, @NotNull String input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:748`
  `return new ActivityResultContract.SynchronousResult<>(Boolean.TRUE);`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:864`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\b\u0016\u0018\u00002\u000e\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:868`
  `public final ActivityResultContract.SynchronousResult<Boolean> getSynchronousResult(@NotNull Context context, @NotNull Uri input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:894`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0016\u0018\u00002\u0012\u0012\u0006\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:898`
  `public final ActivityResultContract.SynchronousResult<Bitmap> getSynchronousResult(@NotNull Context context, @Nullable Void input) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:926`
  `@Metadata(d1 = {"\u00002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0017\u0018\u00002\u0010\u0012\u0004\u0012\u0...`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:931`
  `public final ActivityResultContract.SynchronousResult<Bitmap> getSynchronousResult(@NotNull Context context, @NotNull Uri input) {`
- `sources/androidx/appcompat/R.java:678`
  `public static final int submit_area = 0x7f0903ae;`
- `sources/androidx/appcompat/R.java:1546`
  `public static final int[] SearchView = {android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.inputType, android.R.attr.imeOptions, com.bupa.digitalprimarycare.R.attr.closeIcon, com.bupa.digitalprimarycare.R.attr.commitIcon, com.bupa.digitalprimarycare.R.attr.defaultQueryHint, com.bupa.d...`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:415`
  `return powerManager.isPowerSaveMode();`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:100`
  `canvas.save();`
- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:551`
  `this.mDecorToolbar.saveHierarchyState(sparseArray);`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:254`
  `new PersistHistoryAsyncTask().executeOnExecutor(AsyncTask.THREAD_POOL_EXECUTOR, new ArrayList(this.mHistoricalRecords), this.f531b);`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:410`
  `synchronized (this.mInstanceLock) {`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:481`
  `synchronized (this.mInstanceLock) {`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:509`
  `synchronized (this.mInstanceLock) {`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:520`
  `synchronized (this.mInstanceLock) {`
- `sources/androidx/appcompat/widget/AppCompatRatingBar.java:21`
  `protected synchronized void onMeasure(int i2, int i3) {`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:89`
  `int iSave = canvas.save();`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:95`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/appcompat/widget/AppCompatSpinner.java:676`
  `SavedState savedState = (SavedState) parcelable;`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:32`
  `private boolean mAsyncFontPending;`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:291`
  `this.mAsyncFontPending = this.mFontTypeface == null;`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:387`
  `synchronized (rectF) {`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:455`
  `ViewCompat.saveAttributeDataForStyleable(textView, textView.getContext(), iArr, attributeSet, typedArrayObtainStyledAttributes, i2, 0);`
- `sources/androidx/appcompat/widget/SearchView.java:118`
  `private final View mSubmitArea;`
- `sources/androidx/appcompat/widget/SearchView.java:119`
  `private boolean mSubmitButtonEnabled;`
- `sources/androidx/appcompat/widget/SwitchCompat.java:607`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/appcompat/widget/Toolbar.java:1125`
  `if (!(parcelable instanceof SavedState)) {`
- `sources/androidx/biometric/R.java:1760`
  `public static final int[] SearchView = {android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.inputType, android.R.attr.imeOptions, com.bupa.digitalprimarycare.R.attr.closeIcon, com.bupa.digitalprimarycare.R.attr.commitIcon, com.bupa.digitalprimarycare.R.attr.defaultQueryHint, com.bupa.d...`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:46`
  `private static class FileCleanupTask extends AsyncTask<Void, Void, Void> {`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:102`
  `private static class FileSaveTask extends AsyncTask<String, Void, Void> {`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:109`
  `FileSaveTask(Context context, String str, Bitmap bitmap, Uri uri, ResolvableFuture<Uri> resolvableFuture) {`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:117`
  `private void saveFileBlocking(File file) {`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:150`
  `private void saveFileIfNeededBlocking() {`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:152`
  `synchronized (BrowserServiceFileProvider.f750a) {`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:161`
  `saveFileBlocking(file2);`

## BR075

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/androidx/activity/result/ActivityResultCallerLauncher.java:8`
  `import com.braintreepayments.api.GraphQLConstants;`
- `sources/androidx/activity/result/ActivityResultCallerLauncher.java:9`
  `import com.braintreepayments.api.PaymentMethod;`
- `sources/androidx/activity/result/ActivityResultCallerLauncher.java:21`
  `@Metadata(d1 = {"\u0000$\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0011\n\u0002\u0018\u0002\n\u0002\b\u0003\b\u0000\u0018\u0000*\u0004\b\u0000\u0010\u0001*\u0004\b\u0001\u0010\u00022\b\u0012\u0004\u0012\u00020\u00040\u0...`
- `sources/androidx/activity/result/ActivityResultLauncherKt.java:4`
  `import com.braintreepayments.api.PaymentMethod;`
- `sources/androidx/activity/result/ActivityResultLauncherKt.java:14`
  `@Metadata(d1 = {"\u0000\u0018\n\u0000\n\u0002\u0010\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\u001a\u001e\u0010\u0000\u001a\u00020\u0001*\n\u0012\u0006\u0012\u0004\u0018\u00010\u00030\u00022\n\b\u0002\u0010\u0004\u001a\u0004\u0018\u00010\u0005\u001a#\u...`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:6`
  `import com.braintreepayments.api.GraphQLConstants;`
- `sources/androidx/appcompat/R.java:1205`
  `public static final int AppCompatTextView_autoSizePresetSizes = 0x00000003;`
- `sources/androidx/appcompat/R.java:1531`
  `public static final int[] AppCompatTextView = {android.R.attr.textAppearance, com.bupa.digitalprimarycare.R.attr.autoSizeMaxTextSize, com.bupa.digitalprimarycare.R.attr.autoSizeMinTextSize, com.bupa.digitalprimarycare.R.attr.autoSizePresetSizes, com.bupa.digitalprimarycare.R.attr.autoSizeStepGranula...`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:134`
  `resetGroup();`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:286`
  `public void resetGroup() {`
- `sources/androidx/appcompat/widget/AppCompatButton.java:218`
  `public void setAutoSizeTextTypeUniformWithPresetSizes(@NonNull int[] iArr, int i2) throws IllegalArgumentException {`
- `sources/androidx/appcompat/widget/AppCompatButton.java:220`
  `super.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i2);`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:67`
  `void setAutoSizeTextTypeUniformWithPresetSizes(int[] iArr, int i2);`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:400`
  `public void setAutoSizeTextTypeUniformWithPresetSizes(@NonNull int[] iArr, int i2) throws IllegalArgumentException {`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:402`
  `getSuperCaller().setAutoSizeTextTypeUniformWithPresetSizes(iArr, i2);`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:438`
  `textPaint.reset();`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:466`
  `int i7 = R.styleable.AppCompatTextView_autoSizePresetSizes;`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:469`
  `setupAutoSizeUniformPresetSizes(typedArrayObtainTypedArray);`
- `sources/androidx/biometric/BiometricPrompt.java:250`
  `fragment.getLifecycle().addObserver(new ResetCallbackObserver(biometricViewModel));`
- `sources/androidx/biometric/FingerprintDialogFragment.java:168`
  `Log.w(TAG, "Not resetting the dialog. Context is null.");`
- `sources/androidx/biometric/R.java:1367`
  `public static final int AppCompatTextView_autoSizePresetSizes = 0x00000003;`
- `sources/androidx/biometric/R.java:1739`
  `public static final int[] AppCompatTextView = {android.R.attr.textAppearance, com.bupa.digitalprimarycare.R.attr.autoSizeMaxTextSize, com.bupa.digitalprimarycare.R.attr.autoSizeMinTextSize, com.bupa.digitalprimarycare.R.attr.autoSizePresetSizes, com.bupa.digitalprimarycare.R.attr.autoSizeStepGranula...`
- `sources/androidx/camera/camera2/impl/CameraEventCallback.java:21`
  `public CaptureConfig onPresetSession() {`
- `sources/androidx/camera/camera2/impl/CameraEventCallbacks.java:58`
  `public List<CaptureConfig> onPresetSession() {`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:766`
  `errorListener.onError(sessionConfig, SessionConfig.SessionError.SESSION_ERROR_SURFACE_NEEDS_RESET);`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1033`
  `r("Resetting Capture Session");`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1257`
  `public void onUseCaseReset(@NonNull UseCase useCase) {`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1264`
  `this.f1114a.lambda$onUseCaseReset$8(strV, sessionConfig);`
- `sources/androidx/camera/camera2/internal/ZoomControl.java:183`
  `this.f883a.resetZoom();`
- `sources/androidx/camera/core/CameraX.java:153`
  `updateOrResetMinLogLevel();`
- `sources/androidx/camera/core/CameraX.java:186`
  `updateOrResetMinLogLevel();`
- `sources/androidx/camera/core/VideoCapture.java:1367`
  `this.f1261a.reset();`
- `sources/androidx/camera/core/VideoCapture.java:1400`
  `this.mAudioEncoder.reset();`
- `sources/androidx/camera/core/impl/utils/ExifData.java:169`
  `return (j2 < 0 || j2 > WebSocketProtocol.PAYLOAD_SHORT_MAX) ? j2 < 0 ? new Pair<>(9, -1) : new Pair<>(4, -1) : new Pair<>(3, 4);`
- `sources/androidx/camera/video/Recorder.java:115`
  `private static final Set<State> VALID_NON_PENDING_STATES_WHILE_PENDING = Collections.unmodifiableSet(EnumSet.of(State.INITIALIZING, State.IDLING, State.RESETTING, State.STOPPING, State.ERROR));`
- `sources/androidx/camera/video/Recorder.java:2328`
  `B(State.RESETTING);`
- `sources/androidx/camera/video/Recorder.java:2354`
  `throw new AssertionError("In-progress recording does not match the active recording. Unable to reset encoder.");`
- `sources/androidx/camera/video/Recorder.java:2356`
  `B(State.RESETTING);`
- `sources/androidx/camera/video/Recorder.java:2362`
  `resetInternal();`
- `sources/androidx/camera/video/VideoCaptureLegacy.java:996`
  `this.f1603a.reset();`
- `sources/androidx/camera/video/internal/AudioSource.java:284`
  `resetBufferProvider(null);`
- `sources/androidx/camera/video/internal/AudioSource.java:343`
  `private void resetBufferProvider(@Nullable final BufferProvider<InputBuffer> bufferProvider) {`
- `sources/androidx/camera/video/internal/encoder/EncoderImpl.java:958`
  `reset();`
- `sources/androidx/camera/video/internal/encoder/EncoderImpl.java:971`
  `reset();`
- `sources/androidx/camera/video/internal/encoder/EncoderImpl.java:1316`
  `reset();`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:462`
  `this.f2136d.reset();`
- `sources/androidx/constraintlayout/solver/ArrayRow.java:400`
  `public void reset() {`
- `sources/androidx/constraintlayout/solver/LinearSystem.java:101`
  `solverVariableAcquire.reset();`
- `sources/androidx/constraintlayout/solver/LinearSystem.java:738`
  `constraintAnchor.resetSolverVariable(this.f2232e);`
- `sources/androidx/constraintlayout/solver/LinearSystem.java:744`
  `solverVariable.reset();`
- `sources/androidx/constraintlayout/solver/LinearSystem.java:773`
  `arrayRowAcquire.reset();`
- `sources/androidx/constraintlayout/solver/LinearSystem.java:946`
  `public void reset() {`
- `sources/androidx/constraintlayout/solver/LinearSystem.java:957`
  `solverVariable.reset();`
- `sources/androidx/constraintlayout/solver/Metrics.java:52`
  `public void reset() {`
- `sources/androidx/constraintlayout/solver/PriorityGoalRow.java:216`
  `this.f2234f.reset();`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintAnchor.java:374`
  `public void resetFinalResolution() {`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintAnchor.java:379`
  `public void resetSolverVariable(Cache cache) {`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintAnchor.java:384`
  `solverVariable.reset();`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1175`
  `public void resetFinalResolution() {`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1180`
  `this.f2334f.get(i2).resetFinalResolution();`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1184`
  `public void resetSolverVariables(Cache cache) {`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1185`
  `this.mLeft.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1186`
  `this.mTop.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1187`
  `this.mRight.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1188`
  `this.mBottom.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1189`
  `this.mBaseline.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1190`
  `this.mCenter.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1191`
  `this.f2332d.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1192`
  `this.f2333e.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/WidgetContainer.java:63`
  `public void reset() {`
- `sources/androidx/constraintlayout/solver/widgets/WidgetContainer.java:65`
  `super.reset();`
- `sources/androidx/constraintlayout/solver/widgets/WidgetContainer.java:69`
  `public void resetSolverVariables(Cache cache) {`
- `sources/androidx/constraintlayout/solver/widgets/WidgetContainer.java:70`
  `super.resetSolverVariables(cache);`
- `sources/androidx/constraintlayout/solver/widgets/WidgetContainer.java:73`
  `this.mChildren.get(i2).resetSolverVariables(cache);`
- `sources/androidx/constraintlayout/solver/widgets/analyzer/BasicMeasure.java:263`
  `boolean zDirectMeasureSetup = constraintWidgetContainer.directMeasureSetup(zEnabled);`
- `sources/androidx/constraintlayout/solver/widgets/analyzer/BasicMeasure.java:265`
  `zDirectMeasureSetup &= constraintWidgetContainer.directMeasureWithOrientation(zEnabled, 0);`
- `sources/androidx/constraintlayout/solver/widgets/analyzer/BasicMeasure.java:271`
  `zDirectMeasureWithOrientation = constraintWidgetContainer.directMeasureWithOrientation(zEnabled, 1) & zDirectMeasureSetup;`
- `sources/androidx/constraintlayout/solver/widgets/analyzer/BasicMeasure.java:274`
  `zDirectMeasureWithOrientation = zDirectMeasureSetup;`
- `sources/androidx/constraintlayout/solver/widgets/analyzer/WidgetGroup.java:104`
  `linearSystem.reset();`
- `sources/androidx/constraintlayout/solver/widgets/analyzer/WidgetGroup.java:127`
  `linearSystem.reset();`

## BR076

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `resources/com.bupa.digitalprimarycare.apk/com/cardinalcommerce/dependencies/internal/bouncycastle/x509/CertPathReviewerMessages.properties:143`
  `CertPathReviewer.trustButInvalidCert.text = A trust anchor was found. But it has a different public key, than was used to issue the first certificate of the cert path.`
- `resources/com.bupa.digitalprimarycare.apk/com/cardinalcommerce/dependencies/internal/bouncycastle/x509/CertPathReviewerMessages.properties:144`
  `CertPathReviewer.trustButInvalidCert.summary = A trust anchor was found. But it has a different public key, than was used to issue the first certificate of the cert path.`
- `resources/com.bupa.digitalprimarycare.apk/com/cardinalcommerce/dependencies/internal/bouncycastle/x509/CertPathReviewerMessages.properties:145`
  `CertPathReviewer.trustButInvalidCert.details = A trust anchor was found. But it has a different public key, than was used to issue the first certificate of the cert path.`
- `resources/com.bupa.digitalprimarycare.apk/com/cardinalcommerce/dependencies/internal/bouncycastle/x509/CertPathReviewerMessages.properties:335`
  `# found matching CRL, but not valid`
- `resources/com.bupa.digitalprimarycare.apk/com/cardinalcommerce/dependencies/internal/bouncycastle/x509/CertPathReviewerMessages.properties:339`
  `CertPathReviewer.localInvalidCRL.text = Did not use a matching CRL in a local certstore, because it is outdated. Issued on {0,date}, next update {1,date}.`
- `resources/com.bupa.digitalprimarycare.apk/com/cardinalcommerce/dependencies/internal/bouncycastle/x509/CertPathReviewerMessages.properties:340`
  `CertPathReviewer.localInvalidCRL.summary = Did not use a matching CRL in a local certstore, because it is outdated. Issued on {0,date}, next update {1,date}.`
- `resources/com.bupa.digitalprimarycare.apk/com/cardinalcommerce/dependencies/internal/bouncycastle/x509/CertPathReviewerMessages.properties:341`
  `CertPathReviewer.localInvalidCRL.details = Did not use a matching CRL in a local certstore, because it is outdated. Issued on {0,date}, next update {1,date}.`
- `resources/com.bupa.digitalprimarycare.apk/com/cardinalcommerce/dependencies/internal/bouncycastle/x509/CertPathReviewerMessages.properties:417`
  `# {1} list of crl issuer names that are found in the certstores`
- `resources/com.bupa.digitalprimarycare.apk/com/cardinalcommerce/dependencies/internal/bouncycastle/x509/CertPathReviewerMessages.properties:419`
  `CertPathReviewer.noCrlInCertstore.title = No matching CRL found in local CRL store`
- `resources/com.bupa.digitalprimarycare.apk/com/cardinalcommerce/dependencies/internal/bouncycastle/x509/CertPathReviewerMessages.properties:420`
  `CertPathReviewer.noCrlInCertstore.text = No matching CRL was found in the provided local CRL store.`
- `resources/com.bupa.digitalprimarycare.apk/com/cardinalcommerce/dependencies/internal/bouncycastle/x509/CertPathReviewerMessages.properties:421`
  `CertPathReviewer.noCrlInCertstore.summary = No matching CRL was found in the provided local CRL store.`
- `resources/com.bupa.digitalprimarycare.apk/com/cardinalcommerce/dependencies/internal/bouncycastle/x509/CertPathReviewerMessages.properties:422`
  `CertPathReviewer.noCrlInCertstore.details = No matching CRL was found in the provided local CRL store. \`
- `resources/com.bupa.digitalprimarycare.apk/com/cardinalcommerce/dependencies/internal/bouncycastle/x509/CertPathReviewerMessages.properties:559`
  `CertPathReviewer.QcLimitValueAlpha.details = This certificate has a limitation on the value of transaction for which this certificate can be used to the specified amount, according to the Directive 1999/93/EC of the European Parliament and of the Council of 13 December 1999 on a Community framework ...`
- `resources/com.bupa.digitalprimarycare.apk/com/cardinalcommerce/dependencies/internal/bouncycastle/x509/CertPathReviewerMessages.properties:568`
  `CertPathReviewer.QcLimitValueNum.details = This certificate has a limitation on the value of transaction for which this certificate can be used to the specified amount, according to the Directive 1999/93/EC of the European Parliament and of the Council of 13 December 1999 on a Community framework fo...`
- `resources/com.bupa.digitalprimarycare.apk/com/cardinalcommerce/dependencies/internal/bouncycastle/x509/CertPathReviewerMessages.properties:578`
  `CertPathReviewer.QcEuCompliance.text = This certificate is issued as a Qualified Certificate according Annex I and II of the Directive 1999/93/EC of the European Parliament and of the Council of 13 December 1999 on a Community framework for electronic signatures, as implemented in the law of the cou...`
- `resources/com.bupa.digitalprimarycare.apk/com/cardinalcommerce/dependencies/internal/bouncycastle/x509/CertPathReviewerMessages.properties:579`
  `CertPathReviewer.QcEuCompliance.summary = This certificate is issued as a Qualified Certificate according Annex I and II of the Directive 1999/93/EC of the European Parliament and of the Council of 13 December 1999 on a Community framework for electronic signatures, as implemented in the law of the ...`
- `resources/com.bupa.digitalprimarycare.apk/com/cardinalcommerce/dependencies/internal/bouncycastle/x509/CertPathReviewerMessages.properties:580`
  `CertPathReviewer.QcEuCompliance.details = This certificate is issued as a Qualified Certificate according Annex I and II of the Directive 1999/93/EC of the European Parliament and of the Council of 13 December 1999 on a Community framework for electronic signatures, as implemented in the law of the ...`
- `resources/com.bupa.digitalprimarycare.apk/com/cardinalcommerce/dependencies/internal/bouncycastle/x509/CertPathReviewerMessages_de.properties:335`
  `# found matching CRL, but not valid`
- `resources/com.bupa.digitalprimarycare.apk/com/cardinalcommerce/dependencies/internal/bouncycastle/x509/CertPathReviewerMessages_de.properties:417`
  `# {1} list of crl issuer names that are found in the certstores`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_en_ca.json:1`
  `{"chat-exp.about_your_results_content":"The possible causes are those that the Babylon algorithm suggests as most likely, given the answers you entered. They are listed in the order of their match to your answers and how common the causes are. The order is not an indication of your individual likeli...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_en_gb.json:1`
  `{"chat-exp.about_your_results_content":"The possible causes are those that the Babylon algorithm suggests as most likely, given the answers you entered. They are listed in the order of their match to your answers and how common the causes are. The order is not an indication of your individual likeli...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_en_us.json:1`
  `{"chat-exp.about_your_results_content":"The possible causes are those that the Babylon algorithm suggests as most likely, given the answers you entered. They are listed in the order of their match to your answers and how common the causes are. The order is not an indication of your individual likeli...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_es_us.json:1`
  `{"chat-exp.about_your_results_content":"Las posibles causas son afecciones que pueden estar relacionadas con los síntomas y factores de riesgo ingresados por el usuario.\n\nLas afecciones presentadas a un usuario se enumeran en el orden en que las afecciones coinciden con los síntomas y los factores...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_fr_ca.json:1`
  `{"chat-exp.about_your_results_content":"Les causes possibles sont celles que l'algorithme de Babylon considère les plus probables d'après les réponses que vous avez fournies. Elles sont répertoriées dans leur ordre de correspondance avec vos réponses et de leur fréquence. Cependant, cet ordre n'est ...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_package.json:101`
  `"maestro:ios:uk:login": "maestro test .maestro/login_and_book.yml -e APP_ID='com.babylonpartners.enterprise.CyrusBabylonUK' -e ANDROID='' -e IOS=true",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_package.json:363`
  `"unique-names-generator": "4.3.1",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:85`
  `"comment": "add this property first since it uses as fallback for flexbox, https://msdn.microsoft.com/en-us/library/windows/apps/hh466338.aspx",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:89`
  `"comment": "add this property first since it uses as fallback for flexbox, https://msdn.microsoft.com/en-us/library/windows/apps/hh466348.aspx",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:111`
  `"-webkit-column-break-before": {`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:151`
  `"syntax": "auto | baseline | before-edge | text-before-edge | middle | central | after-edge | text-after-edge | ideographic | alphabetic | hanging | mathematical"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:173`
  `"syntax": "<'cue-before'> <'cue-after'>?"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:179`
  `"cue-before": {`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:203`
  `"syntax": "auto | use-script | no-change | reset-size | ideographic | alphabetic | hanging | mathematical | central | middle | text-after-edge | text-before-edge"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:312`
  `"syntax": "<'pause-before'> <'pause-after'>?"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:318`
  `"pause-before": {`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:324`
  `"syntax": "<'rest-before'> <'rest-after'>?"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:330`
  `"rest-before": {`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:491`
  `"comment": "before a standard it contains 2 extra keywords ('contain' and 'cover') https://www.w3.org/TR/2011/WD-css3-images-20110908/#ltsize",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:511`
  `"syntax": "-moz-ButtonDefault | -moz-ButtonHoverFace | -moz-ButtonHoverText | -moz-CellHighlight | -moz-CellHighlightText | -moz-Combobox | -moz-ComboboxText | -moz-Dialog | -moz-DialogText | -moz-dragtargetzone | -moz-EvenTreeRow | -moz-Field | -moz-FieldText | -moz-html-CellHighlight | -moz-html-C...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:526`
  `"comment": "first Apple proposal gradient syntax https://webkit.org/blog/175/introducing-css-gradients/ - TODO: simplify when after match algorithm improvement ( [, point, radius | , point] -> [, radius]? , point )",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:530`
  `"comment": "first Apple proposal gradient syntax https://webkit.org/blog/175/introducing-css-gradients/",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:534`
  `"comment": "first Apple proposal gradient syntax https://webkit.org/blog/175/introducing-css-gradients/",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:538`
  `"comment": "first Apple proposal gradient syntax https://webkit.org/blog/175/introducing-css-gradients/",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:542`
  `"comment": "first Apple proposal gradient syntax https://webkit.org/blog/175/introducing-css-gradients/",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:596`
  `"syntax": "element( <custom-ident> , [ first | start | last | first-except ]? ) | element( <id-selector> )"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:627`
  `"syntax": "repeat( [ <positive-integer> | auto-fill ], <line-names>+)"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_csstree_data_patch.json:630`
  `"comment": "added non standard color names",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:1133`
  `"syntax": "ignore | normal | select-after | select-before | select-menu | select-same | select-all | none",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:1228`
  `"-webkit-border-before": {`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:1234`
  `"-webkit-border-before-width"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:1252`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-webkit-border-before"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:1254`
  `"-webkit-border-before-color": {`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:1269`
  `"-webkit-border-before-style": {`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:1284`
  `"-webkit-border-before-width": {`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2055`
  `"::first-letter",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2056`
  `"::first-line",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2076`
  `"::first-letter",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2077`
  `"::first-line",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2097`
  `"::first-letter",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2098`
  `"::first-line",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2118`
  `"::first-letter",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2119`
  `"::first-line",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2139`
  `"::first-letter",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2140`
  `"::first-line",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2160`
  `"::first-letter",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2161`
  `"::first-line",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2181`
  `"::first-letter",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2182`
  `"::first-line",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2202`
  `"::first-letter",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2203`
  `"::first-line",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2255`
  `"::first-letter",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2256`
  `"::first-line",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2276`
  `"::first-letter",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2277`
  `"::first-line",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2340`
  `"::first-letter"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2595`
  `"::first-letter"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2614`
  `"::first-letter"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2633`
  `"::first-letter"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2652`
  `"::first-letter"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:2671`
  `"::first-letter"`

## BR077

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `sources/bo/app/s.java:20`
  `public SSLSocketFactory f5318a;`
- `sources/bo/app/s.java:23`
  `SSLContext sSLContext = SSLContext.getInstance("TLS");`
- `sources/bo/app/s.java:24`
  `sSLContext.init(null, null, null);`
- `sources/bo/app/s.java:25`
  `this.f5318a = sSLContext.getSocketFactory();`
- `sources/bo/app/u.java:30`
  `((HttpsURLConnection) uRLConnectionOpenConnection).setSSLSocketFactory(f5361b);`
- `sources/com/braintreepayments/api/SynchronousHttpClient.java:33`
  `if (httpURLConnection instanceof HttpsURLConnection) {`
- `sources/com/braintreepayments/api/SynchronousHttpClient.java:34`
  `SSLSocketFactory sSLSocketFactory = this.socketFactory;`
- `sources/com/braintreepayments/api/SynchronousHttpClient.java:35`
  `if (sSLSocketFactory == null) {`
- `sources/com/braintreepayments/api/SynchronousHttpClient.java:36`
  `throw new SSLException("SSLSocketFactory was not set or failed to initialize");`
- `sources/com/braintreepayments/api/SynchronousHttpClient.java:38`
  `((HttpsURLConnection) httpURLConnection).setSSLSocketFactory(sSLSocketFactory);`
- `sources/com/braintreepayments/api/TLSSocketFactory.java:23`
  `class TLSSocketFactory extends SSLSocketFactory {`
- `sources/com/braintreepayments/api/TLSSocketFactory.java:24`
  `private final SSLSocketFactory internalSSLSocketFactory;`
- `sources/com/braintreepayments/api/TLSSocketFactory.java:28`
  `SSLContext sSLContext = SSLContext.getInstance("TLS");`
- `sources/com/braintreepayments/api/TLSSocketFactory.java:29`
  `sSLContext.init(null, null, null);`
- `sources/com/braintreepayments/api/TLSSocketFactory.java:30`
  `this.internalSSLSocketFactory = sSLContext.getSocketFactory();`
- `sources/com/braintreepayments/api/TLSSocketFactory.java:87`
  `SSLContext sSLContext = SSLContext.getInstance("TLS");`
- `sources/com/braintreepayments/api/TLSSocketFactory.java:88`
  `sSLContext.init(null, trustManagerFactory.getTrustManagers(), null);`
- `sources/com/braintreepayments/api/TLSSocketFactory.java:89`
  `this.internalSSLSocketFactory = sSLContext.getSocketFactory();`
- `sources/com/facebook/react/modules/network/TLSSocketFactory.java:13`
  `public class TLSSocketFactory extends SSLSocketFactory {`
- `sources/com/facebook/react/modules/network/TLSSocketFactory.java:14`
  `private SSLSocketFactory delegate;`
- `sources/com/facebook/react/modules/network/TLSSocketFactory.java:17`
  `SSLContext sSLContext = SSLContext.getInstance("TLS");`
- `sources/com/facebook/react/modules/network/TLSSocketFactory.java:18`
  `sSLContext.init(null, null, null);`
- `sources/com/facebook/react/modules/network/TLSSocketFactory.java:19`
  `this.delegate = sSLContext.getSocketFactory();`
- `sources/com/facebook/react/modules/network/TLSSocketFactory.java:24`
  `((SSLSocket) socket).setEnabledProtocols(new String[]{"TLSv1", "TLSv1.1", "TLSv1.2"});`
- `sources/com/microsoft/appcenter/http/HttpUtils.java:53`
  `if (!(uRLConnectionOpenConnection instanceof HttpsURLConnection)) {`
- `sources/com/microsoft/appcenter/http/HttpUtils.java:56`
  `HttpsURLConnection httpsURLConnection = (HttpsURLConnection) uRLConnectionOpenConnection;`
- `sources/com/microsoft/appcenter/http/HttpUtils.java:58`
  `httpsURLConnection.setSSLSocketFactory(new TLS1_2SocketFactory());`
- `sources/com/microsoft/appcenter/http/HttpUtils.java:60`
  `httpsURLConnection.setConnectTimeout(10000);`
- `sources/com/microsoft/appcenter/http/HttpUtils.java:61`
  `httpsURLConnection.setReadTimeout(10000);`
- `sources/com/microsoft/appcenter/http/HttpUtils.java:62`
  `return httpsURLConnection;`
- `sources/com/microsoft/appcenter/http/TLS1_2SocketFactory.java:20`
  `SSLSocketFactory socketFactory = null;`
- `sources/com/microsoft/appcenter/http/TLS1_2SocketFactory.java:22`
  `SSLContext sSLContext = SSLContext.getInstance(TLS1_2_PROTOCOL);`
- `sources/com/microsoft/appcenter/http/TLS1_2SocketFactory.java:23`
  `sSLContext.init(null, null, null);`
- `sources/com/microsoft/appcenter/http/TLS1_2SocketFactory.java:24`
  `socketFactory = sSLContext.getSocketFactory();`
- `sources/com/microsoft/appcenter/http/TLS1_2SocketFactory.java:27`
  `this.delegate = socketFactory == null ? HttpsURLConnection.getDefaultSSLSocketFactory() : socketFactory;`
- `sources/com/microsoft/codepush/react/TLSSocketFactory.java:13`
  `public class TLSSocketFactory extends SSLSocketFactory {`
- `sources/com/microsoft/codepush/react/TLSSocketFactory.java:14`
  `private SSLSocketFactory delegate;`
- `sources/com/microsoft/codepush/react/TLSSocketFactory.java:17`
  `SSLContext sSLContext = SSLContext.getInstance("TLS");`
- `sources/com/microsoft/codepush/react/TLSSocketFactory.java:18`
  `sSLContext.init(null, null, null);`
- `sources/com/microsoft/codepush/react/TLSSocketFactory.java:19`
  `this.delegate = sSLContext.getSocketFactory();`
- `sources/com/microsoft/codepush/react/TLSSocketFactory.java:24`
  `((SSLSocket) socket).setEnabledProtocols(new String[]{"TLSv1.1", "TLSv1.2"});`
- `sources/com/onfido/api/client/OnfidoTLSSocketFactory.java:13`
  `public class OnfidoTLSSocketFactory extends SSLSocketFactory {`
- `sources/com/onfido/api/client/OnfidoTLSSocketFactory.java:14`
  `private SSLSocketFactory ssLSocketFactory;`
- `sources/com/onfido/api/client/OnfidoTLSSocketFactory.java:17`
  `SSLContext sSLContext = SSLContext.getInstance("TLS");`
- `sources/com/onfido/api/client/OnfidoTLSSocketFactory.java:18`
  `sSLContext.init(null, null, null);`
- `sources/com/onfido/api/client/OnfidoTLSSocketFactory.java:19`
  `this.ssLSocketFactory = sSLContext.getSocketFactory();`
- `sources/com/onfido/api/client/OnfidoTLSSocketFactory.java:24`
  `((SSLSocket) socket).setEnabledProtocols(new String[]{"TLSv1.2"});`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:63`
  `SSLContext sSLContext = SSLContext.getInstance("SSL");`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:64`
  `sSLContext.init(null, new TrustManager[]{x509TrustManager}, new SecureRandom());`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:65`
  `SSLSocketFactory socketFactory = sSLContext.getSocketFactory();`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:67`
  `builderNewBuilder.sslSocketFactory(socketFactory, x509TrustManager);`
- `sources/io/sentry/SentryOptions.java:1203`
  `public void setSslSocketFactory(@Nullable SSLSocketFactory sSLSocketFactory) {`
- `sources/io/sentry/SentryOptions.java:1204`
  `this.sslSocketFactory = sSLSocketFactory;`
- `sources/io/sentry/transport/HttpConnection.java:69`
  `boolean z2 = httpURLConnectionA instanceof HttpsURLConnection;`
- `sources/io/sentry/transport/HttpConnection.java:71`
  `((HttpsURLConnection) httpURLConnectionA).setHostnameVerifier(hostnameVerifier);`
- `sources/io/sentry/transport/HttpConnection.java:73`
  `SSLSocketFactory sslSocketFactory = this.options.getSslSocketFactory();`
- `sources/io/sentry/transport/HttpConnection.java:74`
  `if (z2 && sslSocketFactory != null) {`
- `sources/io/sentry/transport/HttpConnection.java:75`
  `((HttpsURLConnection) httpURLConnectionA).setSSLSocketFactory(sslSocketFactory);`
- `sources/lib/android/paypal/com/magnessdk/network/base/b.java:43`
  `httpsURLConnection = (HttpsURLConnection) new URL(this.f20961d.toString()).openConnection();`
- `sources/lib/android/paypal/com/magnessdk/network/base/b.java:45`
  `httpsURLConnection.setReadTimeout(c.h.a.HTTP_READ_TIMEOUT.a());`
- `sources/lib/android/paypal/com/magnessdk/network/base/b.java:46`
  `httpsURLConnection.setConnectTimeout(c.h.a.HTTP_CONNECT_TIMEOUT.a());`
- `sources/lib/android/paypal/com/magnessdk/network/base/b.java:47`
  `httpsURLConnection.setRequestMethod(c.h.b.POST.toString());`
- `sources/lib/android/paypal/com/magnessdk/network/base/b.java:48`
  `httpsURLConnection.setSSLSocketFactory(this.f20958a);`
- `sources/lib/android/paypal/com/magnessdk/network/base/b.java:49`
  `httpsURLConnection.setDoOutput(true);`
- `sources/lib/android/paypal/com/magnessdk/network/base/b.java:50`
  `httpsURLConnection.setFixedLengthStreamingMode(bArr.length);`
- `sources/lib/android/paypal/com/magnessdk/network/base/b.java:52`
  `httpsURLConnection.setRequestProperty(entry.getKey().toString(), entry.getValue().toString());`
- `sources/lib/android/paypal/com/magnessdk/network/base/b.java:54`
  `outputStream = httpsURLConnection.getOutputStream();`
- `sources/lib/android/paypal/com/magnessdk/network/base/f.java:38`
  `this.f20974c = SSLContext.getInstance(f20972a);`
- `sources/okhttp3/OkHttpClient.java:134`
  `@Metadata(d1 = {"\u0000ø\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0018...`
- `sources/okhttp3/OkHttpClient.java:774`
  `public final void setSslSocketFactoryOrNull$okhttp(@Nullable SSLSocketFactory sSLSocketFactory) {`
- `sources/okhttp3/OkHttpClient.java:775`
  `this.sslSocketFactoryOrNull = sSLSocketFactory;`
- `sources/okhttp3/OkHttpClient.java:801`
  `public final Builder sslSocketFactory(@NotNull SSLSocketFactory sslSocketFactory) {`
- `sources/okhttp3/OkHttpClient.java:802`
  `Intrinsics.checkNotNullParameter(sslSocketFactory, "sslSocketFactory");`
- `sources/okhttp3/OkHttpClient.java:803`
  `if (!Intrinsics.areEqual(sslSocketFactory, getSslSocketFactoryOrNull())) {`
- `sources/okhttp3/OkHttpClient.java:806`
  `setSslSocketFactoryOrNull$okhttp(sslSocketFactory);`
- `sources/okhttp3/OkHttpClient.java:808`
  `X509TrustManager x509TrustManagerTrustManager = companion.get().trustManager(sslSocketFactory);`
- `sources/okhttp3/OkHttpClient.java:868`
  `public final Builder sslSocketFactory(@NotNull SSLSocketFactory sslSocketFactory, @NotNull X509TrustManager trustManager) {`
- `sources/okhttp3/OkHttpClient.java:869`
  `Intrinsics.checkNotNullParameter(sslSocketFactory, "sslSocketFactory");`
- `sources/okhttp3/OkHttpClient.java:871`
  `if (!Intrinsics.areEqual(sslSocketFactory, getSslSocketFactoryOrNull()) || !Intrinsics.areEqual(trustManager, getX509TrustManagerOrNull())) {`
- `sources/okhttp3/OkHttpClient.java:874`
  `setSslSocketFactoryOrNull$okhttp(sslSocketFactory);`

## BR078

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/com/auth0/android/request/DefaultClient.java:19`
  `import okhttp3.Call;`
- `sources/com/auth0/android/request/DefaultClient.java:20`
  `import okhttp3.Headers;`
- `sources/com/auth0/android/request/DefaultClient.java:28`
  `import okhttp3.logging.HttpLoggingInterceptor;`
- `sources/com/auth0/android/request/DefaultClient.java:34`
  `@Metadata(d1 = {"\u0000Z\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0010$\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0...`
- `sources/com/auth0/android/request/DefaultClient.java:75`
  `OkHttpClient.Builder builder = new OkHttpClient.Builder();`
- `sources/com/auth0/android/request/DefaultClient.java:86`
  `this.okHttpClient = builder.build();`
- `sources/com/facebook/react/devsupport/DevServerHelper.java:374`
  `new OkHttpClient().newCall(new Request.Builder().url(DevServerHelper.this.getOpenUrlEndpoint(reactContext)).post(RequestBody.create(MediaType.parse("application/json"), new JSONObject().put("url", str).toString())).build()).execute();`
- `sources/com/onfido/api/client/OnfidoFetcher.java:25`
  `import okhttp3.CertificatePinner;`
- `sources/com/onfido/api/client/OnfidoFetcher.java:26`
  `import okhttp3.HttpUrl;`
- `sources/com/onfido/api/client/OnfidoFetcher.java:27`
  `import okhttp3.Interceptor;`
- `sources/com/onfido/api/client/OnfidoFetcher.java:28`
  `import okhttp3.OkHttpClient;`
- `sources/com/onfido/api/client/OnfidoFetcher.java:29`
  `import okhttp3.Protocol;`
- `sources/com/onfido/api/client/OnfidoFetcher.java:30`
  `import okhttp3.Request;`
- `sources/com/onfido/api/client/OnfidoFetcher.java:64`
  `private OnfidoFetcher(OkHttpClient okHttpClient, TokenProvider tokenProvider, String str, String[] strArr, boolean z2, String str2, String str3, String str4, String str5) {`
- `sources/com/onfido/api/client/OnfidoFetcher.java:68`
  `OkHttpClient.Builder builderNewBuilder = okHttpClient.newBuilder();`
- `sources/com/onfido/api/client/OnfidoFetcher.java:70`
  `OkHttpClient.Builder builderAddInterceptor = builderNewBuilder.addInterceptor(new AuthTokenInterceptor(tokenProvider)).addInterceptor(new SdkHeadersInterceptor(str2, str3, str4, str5)).addInterceptor(httpLoggingInterceptor);`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:10`
  `import javax.net.ssl.HostnameVerifier;`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:16`
  `import okhttp3.OkHttpClient;`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:47`
  `public static OkHttpClient.Builder getUnsafeOkHttpClient(OkHttpClient okHttpClient) {`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:66`
  `OkHttpClient.Builder builderNewBuilder = okHttpClient.newBuilder();`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:68`
  `builderNewBuilder.hostnameVerifier(new HostnameVerifier() { // from class: com.RNFetchBlob.RNFetchBlobUtils.2`
- `sources/com/RNFetchBlob/RNFetchBlobUtils.java:69`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/okhttp3/Cookie.java:258`
  `throw new UnsupportedOperationException("Method not decompiled: okhttp3.Cookie.Companion.dateCharacterOffset(java.lang.String, int, int, boolean):int");`
- `sources/okhttp3/OkHttpClient.java:16`
  `import javax.net.ssl.HostnameVerifier;`
- `sources/okhttp3/OkHttpClient.java:46`
  `/* JADX INFO: compiled from: OkHttpClient.kt */`
- `sources/okhttp3/OkHttpClient.java:48`
  `@Metadata(d1 = {"\u0000î\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u001a\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u00...`
- `sources/okhttp3/OkHttpClient.java:49`
  `public class OkHttpClient implements Cloneable, Call.Factory, WebSocket.Factory {`
- `sources/okhttp3/OkHttpClient.java:133`
  `/* JADX INFO: compiled from: OkHttpClient.kt */`
- `sources/okhttp3/OkHttpClient.java:134`
  `@Metadata(d1 = {"\u0000ø\u0001\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\b\b\n\u0002\u0018...`
- `sources/okhttp3/OkHttpClient.java:558`
  `public final Builder hostnameVerifier(@NotNull HostnameVerifier hostnameVerifier) {`
- `sources/okhttp3/OkHttpClient.java:559`
  `Intrinsics.checkNotNullParameter(hostnameVerifier, "hostnameVerifier");`
- `sources/okhttp3/OkHttpClient.java:560`
  `if (!Intrinsics.areEqual(hostnameVerifier, getHostnameVerifier())) {`
- `sources/okhttp3/OkHttpClient.java:881`
  `public Builder(@NotNull OkHttpClient okHttpClient) {`
- `sources/okhttp3/OkHttpClient.java:895`
  `this.dns = okHttpClient.dns();`
- `sources/okhttp3/OkHttpClient.java:896`
  `this.proxy = okHttpClient.proxy();`
- `sources/okhttp3/OkHttpClient.java:897`
  `this.proxySelector = okHttpClient.proxySelector();`
- `sources/okhttp3/OkHttpClient.java:898`
  `this.proxyAuthenticator = okHttpClient.proxyAuthenticator();`
- `sources/okhttp3/OkHttpClient.java:899`
  `this.socketFactory = okHttpClient.socketFactory();`
- `sources/okhttp3/OkHttpClient.java:900`
  `this.sslSocketFactoryOrNull = okHttpClient.sslSocketFactoryOrNull;`
- `sources/okhttp3/OkHttpClient.java:901`
  `this.x509TrustManagerOrNull = okHttpClient.getX509TrustManager();`
- `sources/okhttp3/OkHttpClient.java:902`
  `this.connectionSpecs = okHttpClient.connectionSpecs();`
- `sources/okhttp3/OkHttpClient.java:903`
  `this.protocols = okHttpClient.protocols();`
- `sources/okhttp3/OkHttpClient.java:904`
  `this.hostnameVerifier = okHttpClient.hostnameVerifier();`
- `sources/okhttp3/OkHttpClient.java:905`
  `this.certificatePinner = okHttpClient.certificatePinner();`
- `sources/okhttp3/OkHttpClient.java:906`
  `this.certificateChainCleaner = okHttpClient.getCertificateChainCleaner();`
- `sources/okhttp3/OkHttpClient.java:907`
  `this.callTimeout = okHttpClient.callTimeoutMillis();`
- `sources/okhttp3/OkHttpClient.java:1475`
  `public OkHttpClient() {`
- `sources/okhttp3/internal/connection/RealConnection.java:518`
  `if (this.http2Connection == null || routes == null || !routeMatchesAny(routes) || address.hostnameVerifier() != OkHostnameVerifier.INSTANCE || !supportsUrl(address.url())) {`
- `sources/okhttp3/internal/http2/PushObserver.java:31`
  `@Metadata(d1 = {"\u00008\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\b\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\b\u0002\u0018\u00002\u00...`
- `sources/okhttp3/internal/http2/PushObserver.java:33`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:40`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:46`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:52`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/platform/Android10Platform.java:16`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/Android10Platform.java:17`
  `import okhttp3.internal.SuppressSignatureCheck;`
- `sources/okhttp3/internal/platform/Android10Platform.java:32`
  `@Metadata(d1 = {"\u0000J\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\...`
- `sources/okhttp3/internal/platform/Android10Platform.java:81`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Android10Platform.java:89`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Android10Platform.java:143`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:23`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:24`
  `import okhttp3.internal.SuppressSignatureCheck;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:41`
  `@Metadata(d1 = {"\u0000x\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\...`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:79`
  `@Metadata(d1 = {"\u00008\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0010\u000b\n\u0000\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0000\n\u0002\u0010\u000e\n\u0000\b\u0080\b\u0018\u00...`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:133`
  `@Override // okhttp3.internal.tls.TrustRootIndex`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:180`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:188`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:202`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:283`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:292`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:19`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:28`
  `@Metadata(d1 = {"\u0000J\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\...`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:123`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/BouncyCastlePlatform.java:142`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:22`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:24`
  `import org.conscrypt.ConscryptHostnameVerifier;`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:30`
  `@Metadata(d1 = {"\u0000H\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\...`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:85`
  `public static final DisabledHostnameVerifier INSTANCE = new DisabledHostnameVerifier();`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:87`
  `private DisabledHostnameVerifier() {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:156`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:167`
  `@Override // okhttp3.internal.platform.Platform`

## BR079

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/androidx/webkit/internal/ServiceWorkerWebSettingsImpl.java:105`
  `public void setAllowFileAccess(boolean z2) {`
- `sources/androidx/webkit/internal/ServiceWorkerWebSettingsImpl.java:108`
  `getFrameworksImpl().setAllowFileAccess(z2);`
- `sources/androidx/webkit/internal/ServiceWorkerWebSettingsImpl.java:113`
  `getBoundaryInterface().setAllowFileAccess(z2);`
- `sources/com/appboy/ui/AppboyWebViewActivity.java:26`
  `@SuppressLint({"SetJavaScriptEnabled"})`
- `sources/com/appboy/ui/AppboyWebViewActivity.java:39`
  `settings.setAllowFileAccess(false);`
- `sources/com/appboy/ui/AppboyWebViewActivity.java:41`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/appboy/ui/inappmessage/views/AppboyInAppMessageHtmlBaseView.java:68`
  `@SuppressLint({"SetJavaScriptEnabled"})`
- `sources/com/appboy/ui/inappmessage/views/AppboyInAppMessageHtmlBaseView.java:90`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/appboy/ui/inappmessage/views/AppboyInAppMessageHtmlBaseView.java:95`
  `settings.setAllowFileAccess(true);`
- `sources/com/cardinalcommerce/a/setTextAppearance.java:346`
  `webView.getSettings().setJavaScriptEnabled(false);`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:735`
  `public void setAllowFileAccess(WebView webView, @Nullable Boolean bool) {`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:736`
  `webView.getSettings().setAllowFileAccess(bool != null && bool.booleanValue());`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:740`
  `public void setAllowFileAccessFromFileURLs(WebView webView, boolean z2) {`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:741`
  `webView.getSettings().setAllowFileAccessFromFileURLs(z2);`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:745`
  `public void setAllowUniversalAccessFromFileURLs(WebView webView, boolean z2) {`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:746`
  `webView.getSettings().setAllowUniversalAccessFromFileURLs(z2);`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:936`
  `public void setJavaScriptEnabled(WebView webView, boolean z2) {`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:937`
  `webView.getSettings().setJavaScriptEnabled(z2);`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:973`
  `public void setMixedContentMode(WebView webView, @Nullable String str) {`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:975`
  `webView.getSettings().setMixedContentMode(1);`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:977`
  `webView.getSettings().setMixedContentMode(0);`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:979`
  `webView.getSettings().setMixedContentMode(2);`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:1259`
  `settings.setAllowFileAccess(false);`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:1261`
  `settings.setAllowFileAccessFromFileURLs(false);`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:1262`
  `setAllowUniversalAccessFromFileURLs(rNCWebViewCreateRNCWebViewInstance, false);`
- `sources/com/reactnativecommunity/webview/RNCWebViewManager.java:1263`
  `setMixedContentMode(rNCWebViewCreateRNCWebViewInstance, ReactScrollViewHelper.OVER_SCROLL_NEVER);`
- `sources/com/tealium/internal/dispatcher/WebViewDispatcher.java:124`
  `settings.setJavaScriptEnabled(true);`
- `sources/io/branch/referral/BranchViewHandler.java:175`
  `webView.getSettings().setJavaScriptEnabled(true);`

## BR080

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/android/support/v4/media/MediaBrowserCompat.java:870`
  `Log.d("MediaBrowserCompat", "  mServiceConnection=" + this.f51g);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:871`
  `Log.d("MediaBrowserCompat", "  mServiceBinderWrapper=" + this.f52h);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:872`
  `Log.d("MediaBrowserCompat", "  mCallbacksMessenger=" + this.f53i);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:873`
  `Log.d("MediaBrowserCompat", "  mRootId=" + this.mRootId);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:874`
  `Log.d("MediaBrowserCompat", "  mMediaSessionToken=" + this.mMediaSessionToken);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1108`
  `Log.d("MediaBrowserCompat", "ServiceCallbacks.onConnect...");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1218`
  `Log.d("AppCompatDelegate", "Exception while getting ActivityInfo", e2);`
- `sources/androidx/constraintlayout/motion/utils/StopLogic.java:202`
  `Log.v(str, str2 + " end stage 2");`
- `sources/androidx/core/view/ViewCompat.java:1411`
  `Log.d(TAG, "Error calling dispatchFinishTemporaryDetach", e2);`
- `sources/androidx/core/view/ViewCompat.java:1447`
  `Log.d(TAG, "Error calling dispatchStartTemporaryDetach", e2);`
- `sources/androidx/exifinterface/media/ExifInterface.java:1931`
  `Log.d(TAG, "Failed to skip " + i9 + " bytes.");`
- `sources/androidx/exifinterface/media/ExifInterface.java:1937`
  `Log.d(TAG, "Failed to read " + i8 + " bytes.");`
- `sources/androidx/exifinterface/media/ExifInterface.java:2495`
  `Log.d(TAG, "readExifSegment: Byte Align MM");`
- `sources/androidx/fragment/app/FragmentLayoutInflaterFactory.java:78`
  `Log.v("FragmentManager", "Fragment " + fragmentFindFragmentById + " has been inflated via the <fragment> tag: id=0x" + Integer.toHexString(resourceId));`
- `sources/androidx/fragment/app/FragmentLayoutInflaterFactory.java:91`
  `Log.v("FragmentManager", "Retained Fragment " + fragmentFindFragmentById + " has been re-attached via the <fragment> tag: id=0x" + Integer.toHexString(resourceId));`
- `sources/androidx/fragment/app/FragmentStateManager.java:118`
  `Log.d("FragmentManager", "moveto ACTIVITY_CREATED: " + this.mFragment);`
- `sources/androidx/fragment/app/FragmentStore.java:285`
  `Log.v("FragmentManager", "Removed fragment from active set " + fragmentK);`
- `sources/androidx/localbroadcastmanager/content/LocalBroadcastManager.java:162`
  `Log.v(TAG, "Resolving type " + strResolveTypeIfNeeded + " scheme " + scheme + " of intent " + intent);`
- `sources/androidx/localbroadcastmanager/content/LocalBroadcastManager.java:167`
  `Log.v(TAG, "Action list: " + arrayList3);`
- `sources/androidx/localbroadcastmanager/content/LocalBroadcastManager.java:194`
  `Log.v(TAG, "  Filter matched!  match=0x" + Integer.toHexString(iMatch));`
- `sources/com/airbnb/android/react/maps/AirMapTileProvider.java:281`
  `Log.d("urlTile: ", workManager.getWorkInfosByTag(strE).get(1L, timeUnit).get(0).toString());`
- `sources/com/auth0/android/authentication/storage/SecureCredentialsManager.java:167`
  `Log.d(TAG, "Credentials have expired. Renewing them now...");`
- `sources/com/auth0/android/authentication/storage/SecureCredentialsManager.java:345`
  `Log.d(TAG, "Trying to encrypt the given data using the private key.");`
- `sources/com/auth0/android/provider/OAuthManager.java:344`
  `Log.d(TAG, "The parsed CallbackURI contains the following parameters: " + mapB.keySet());`
- `sources/com/bumptech/glide/Glide.java:441`
  `Log.d(TAG, "Discovered GlideModule from manifest: " + it2.next().getClass());`
- `sources/com/bumptech/glide/load/engine/bitmap_recycle/LruArrayPool.java:117`
  `Log.v(adapterFromObject.getTag(), "evicted: " + adapterFromObject.getArrayLength(objRemoveLast));`
- `sources/com/bumptech/glide/load/engine/bitmap_recycle/LruArrayPool.java:158`
  `Log.v(adapterFromType.getTag(), "Allocated " + key.f6916a + " bytes");`
- `sources/com/bumptech/glide/load/engine/prefill/BitmapPreFillRunner.java:93`
  `Log.d("PreFillRunner", "allocated [" + preFillTypeRemove.d() + ViewHierarchyNode.JsonKeys.X + preFillTypeRemove.b() + "] " + preFillTypeRemove.a() + " size: " + bitmapByteSize);`
- `sources/com/bumptech/glide/load/resource/ImageDecoderResourceDecoder.java:77`
  `Log.v(ImageDecoderResourceDecoder.TAG, "Resizing from [" + size.getWidth() + ViewHierarchyNode.JsonKeys.X + size.getHeight() + "] to [" + iRound + ViewHierarchyNode.JsonKeys.X + iRound2 + "] scaleFactor: " + scaleFactor);`
- `sources/com/bumptech/glide/load/resource/bitmap/BitmapImageDecoderResourceDecoder.java:24`
  `Log.v(TAG, "Decoded [" + bitmapDecodeBitmap.getWidth() + ViewHierarchyNode.JsonKeys.X + bitmapDecodeBitmap.getHeight() + "] for [" + i2 + ViewHierarchyNode.JsonKeys.X + i3 + "]");`
- `sources/com/bumptech/glide/load/resource/bitmap/DefaultImageHeaderParser.java:255`
  `Log.d(TAG, "Missing jpeg exif preamble");`
- `sources/com/bumptech/glide/load/resource/bitmap/DefaultImageHeaderParser.java:338`
  `Log.d(TAG, "Unknown endianness = " + ((int) sA));`
- `sources/com/bumptech/glide/load/resource/bitmap/DefaultImageHeaderParser.java:356`
  `Log.d(TAG, "Negative tiff component count");`
- `sources/com/bumptech/glide/load/resource/bitmap/DefaultImageHeaderParser.java:360`
  `Log.d(TAG, "Got tagIndex=" + i2 + " tagType=" + ((int) sA3) + " formatCode=" + ((int) sA4) + " componentCount=" + iB2);`
- `sources/com/bumptech/glide/load/resource/bitmap/DefaultImageHeaderParser.java:365`
  `Log.d(TAG, "Got byte count > 4, not orientation, continuing, formatCode=" + ((int) sA4));`
- `sources/com/bumptech/glide/load/resource/bitmap/DefaultImageHeaderParser.java:374`
  `Log.d(TAG, "Illegal number of bytes for TI tag data tagType=" + ((int) sA3));`
- `sources/com/bumptech/glide/load/resource/bitmap/DefaultImageHeaderParser.java:377`
  `Log.d(TAG, "Illegal tagValueOffset=" + i4 + " tagType=" + ((int) sA3));`
- `sources/com/bumptech/glide/load/resource/bitmap/Downsampler.java:405`
  `Log.v("Downsampler", "Decoded " + getBitmapString(bitmap) + " from [" + i2 + ViewHierarchyNode.JsonKeys.X + i3 + "] " + str + " with inBitmap " + getInBitmapString(options) + " for [" + i4 + ViewHierarchyNode.JsonKeys.X + i5 + "], sample size: " + options.inSampleSize + ", density: " + options.inDen...`
- `sources/com/bumptech/glide/load/resource/bitmap/TransformationUtils.java:161`
  `Log.v(TAG, "requested target size too big for input, fit centering instead");`
- `sources/com/bumptech/glide/load/resource/bitmap/TransformationUtils.java:211`
  `Log.v(TAG, "requested target size matches input, returning input");`

## BR081

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/android/security/keystore/KeyGenParameterSpec$Builder.java:10`
  `public final /* synthetic */ class KeyGenParameterSpec$Builder {`
- `sources/android/security/keystore/KeyGenParameterSpec$Builder.java:15`
  `public /* synthetic */ KeyGenParameterSpec$Builder(@NonNull String str, int i2) {`
- `sources/android/security/keystore/KeyGenParameterSpec$Builder.java:19`
  `public native /* synthetic */ KeyGenParameterSpec build();`
- `sources/android/security/keystore/KeyGenParameterSpec$Builder.java:21`
  `public native /* synthetic */ KeyGenParameterSpec$Builder setAlgorithmParameterSpec(@NonNull AlgorithmParameterSpec algorithmParameterSpec);`
- `sources/android/security/keystore/KeyGenParameterSpec$Builder.java:24`
  `public native /* synthetic */ KeyGenParameterSpec$Builder setBlockModes(String... strArr);`
- `sources/android/security/keystore/KeyGenParameterSpec$Builder.java:27`
  `public native /* synthetic */ KeyGenParameterSpec$Builder setCertificateNotAfter(@NonNull Date date);`
- `sources/android/security/keystore/KeyGenParameterSpec$Builder.java:30`
  `public native /* synthetic */ KeyGenParameterSpec$Builder setCertificateNotBefore(@NonNull Date date);`
- `sources/android/security/keystore/KeyGenParameterSpec$Builder.java:33`
  `public native /* synthetic */ KeyGenParameterSpec$Builder setCertificateSerialNumber(@NonNull BigInteger bigInteger);`
- `sources/android/security/keystore/KeyGenParameterSpec$Builder.java:36`
  `public native /* synthetic */ KeyGenParameterSpec$Builder setCertificateSubject(@NonNull X500Principal x500Principal);`
- `sources/android/security/keystore/KeyGenParameterSpec$Builder.java:39`
  `public native /* synthetic */ KeyGenParameterSpec$Builder setDigests(String... strArr);`
- `sources/android/security/keystore/KeyGenParameterSpec$Builder.java:42`
  `public native /* synthetic */ KeyGenParameterSpec$Builder setEncryptionPaddings(String... strArr);`
- `sources/android/security/keystore/KeyGenParameterSpec$Builder.java:45`
  `public native /* synthetic */ KeyGenParameterSpec$Builder setKeySize(int i2);`
- `sources/android/security/keystore/KeyGenParameterSpec$Builder.java:48`
  `public native /* synthetic */ KeyGenParameterSpec$Builder setKeyValidityForOriginationEnd(Date date);`
- `sources/android/security/keystore/KeyGenParameterSpec$Builder.java:51`
  `public native /* synthetic */ KeyGenParameterSpec$Builder setRandomizedEncryptionRequired(boolean z2);`
- `sources/android/security/keystore/KeyGenParameterSpec$Builder.java:54`
  `public native /* synthetic */ KeyGenParameterSpec$Builder setSignaturePaddings(String... strArr);`
- `sources/android/security/keystore/KeyGenParameterSpec$Builder.java:57`
  `public native /* synthetic */ KeyGenParameterSpec$Builder setUserAuthenticationRequired(boolean z2);`
- `sources/android/security/keystore/KeyGenParameterSpec$Builder.java:61`
  `public native /* synthetic */ KeyGenParameterSpec$Builder setUserAuthenticationValidityDurationSeconds(int i2);`
- `sources/androidx/biometric/CryptoObjectUtils.java:6`
  `import android.security.keystore.KeyGenParameterSpec;`
- `sources/androidx/biometric/CryptoObjectUtils.java:7`
  `import android.security.keystore.KeyGenParameterSpec$Builder;`
- `sources/androidx/biometric/CryptoObjectUtils.java:34`
  `private static final String KEYSTORE_INSTANCE = "AndroidKeyStore";`
- `sources/androidx/biometric/CryptoObjectUtils.java:43`
  `static KeyGenParameterSpec a(@NonNull KeyGenParameterSpec$Builder keyGenParameterSpec$Builder) {`
- `sources/androidx/biometric/CryptoObjectUtils.java:44`
  `return keyGenParameterSpec$Builder.build();`
- `sources/androidx/biometric/CryptoObjectUtils.java:48`
  `static KeyGenParameterSpec$Builder b(@NonNull String str, int i2) {`
- `sources/androidx/biometric/CryptoObjectUtils.java:49`
  `return new KeyGenParameterSpec$Builder(str, i2);`
- `sources/androidx/biometric/CryptoObjectUtils.java:52`
  `static void c(@NonNull KeyGenerator keyGenerator, @NonNull KeyGenParameterSpec keyGenParameterSpec) throws InvalidAlgorithmParameterException {`
- `sources/androidx/biometric/CryptoObjectUtils.java:53`
  `keyGenerator.init(keyGenParameterSpec);`
- `sources/androidx/biometric/CryptoObjectUtils.java:56`
  `static void d(@NonNull KeyGenParameterSpec$Builder keyGenParameterSpec$Builder) {`
- `sources/androidx/biometric/CryptoObjectUtils.java:57`
  `keyGenParameterSpec$Builder.setBlockModes(CipherStorageKeystoreAesCbc.BLOCK_MODE_CBC);`
- `sources/androidx/biometric/CryptoObjectUtils.java:60`
  `static void e(@NonNull KeyGenParameterSpec$Builder keyGenParameterSpec$Builder) {`
- `sources/androidx/biometric/CryptoObjectUtils.java:61`
  `keyGenParameterSpec$Builder.setEncryptionPaddings(CipherStorageKeystoreAesCbc.PADDING_PKCS7);`
- `sources/androidx/biometric/CryptoObjectUtils.java:124`
  `KeyStore keyStore = KeyStore.getInstance("AndroidKeyStore");`
- `sources/androidx/biometric/CryptoObjectUtils.java:126`
  `KeyGenParameterSpec$Builder keyGenParameterSpec$BuilderB = Api23Impl.b(FAKE_KEY_NAME, 3);`
- `sources/androidx/biometric/CryptoObjectUtils.java:127`
  `Api23Impl.d(keyGenParameterSpec$BuilderB);`
- `sources/androidx/biometric/CryptoObjectUtils.java:128`
  `Api23Impl.e(keyGenParameterSpec$BuilderB);`
- `sources/androidx/biometric/CryptoObjectUtils.java:129`
  `KeyGenerator keyGenerator = KeyGenerator.getInstance(CipherStorageKeystoreAesCbc.ALGORITHM_AES, "AndroidKeyStore");`
- `sources/androidx/biometric/CryptoObjectUtils.java:130`
  `Api23Impl.c(keyGenerator, Api23Impl.a(keyGenParameterSpec$BuilderB));`
- `sources/com/appsflyer/AFKeystoreWrapper.java:6`
  `import android.security.keystore.KeyGenParameterSpec$Builder;`
- `sources/com/appsflyer/AFKeystoreWrapper.java:34`
  `KeyStore keyStore = KeyStore.getInstance(CipherStorageBase.KEYSTORE_TYPE);`
- `sources/com/appsflyer/AFKeystoreWrapper.java:38`
  `AFLogger.afErrorLog("Couldn't load keystore instance of type: AndroidKeyStore", e2);`
- `sources/com/appsflyer/AFKeystoreWrapper.java:199`
  `algorithmParameterSpecBuild = new KeyGenParameterSpec$Builder(str, 3).setCertificateSubject(new X500Principal("CN=AndroidSDK, O=AppsFlyer")).setCertificateSerialNumber(BigInteger.ONE).setCertificateNotBefore(calendar.getTime()).setCertificateNotAfter(calendar2.getTime()).build();`
- `sources/com/auth0/android/authentication/storage/CryptoUtil.java:8`
  `import android.security.keystore.KeyGenParameterSpec$Builder;`
- `sources/com/auth0/android/authentication/storage/CryptoUtil.java:47`
  `private static final String ANDROID_KEY_STORE = "AndroidKeyStore";`
- `sources/com/auth0/android/authentication/storage/CryptoUtil.java:78`
  `KeyStore keyStore = KeyStore.getInstance("AndroidKeyStore");`
- `sources/com/auth0/android/authentication/storage/CryptoUtil.java:193`
  `KeyStore keyStore = KeyStore.getInstance("AndroidKeyStore");`
- `sources/com/auth0/android/authentication/storage/CryptoUtil.java:209`
  `algorithmParameterSpecBuild = new KeyGenParameterSpec$Builder(this.KEY_ALIAS, 3).setCertificateSubject(x500Principal).setCertificateSerialNumber(BigInteger.ONE).setCertificateNotBefore(calendar.getTime()).setCertificateNotAfter(calendar2.getTime()).setKeySize(2048).setEncryptionPaddings(CipherStorag...`
- `sources/com/auth0/android/authentication/storage/CryptoUtil.java:222`
  `KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA", "AndroidKeyStore");`
- `sources/com/braintreepayments/api/TLSSocketFactory.java:78`
  `KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());`
- `sources/com/cardinalcommerce/dependencies/internal/bouncycastle/jcajce/provider/asymmetric/rsa/KeyPairGeneratorSpi.java:15`
  `import java.security.spec.RSAKeyGenParameterSpec;`
- `sources/com/cardinalcommerce/dependencies/internal/bouncycastle/jcajce/provider/asymmetric/rsa/KeyPairGeneratorSpi.java:46`
  `if (!(algorithmParameterSpec instanceof RSAKeyGenParameterSpec)) {`
- `sources/com/cardinalcommerce/dependencies/internal/bouncycastle/jcajce/provider/asymmetric/rsa/KeyPairGeneratorSpi.java:47`
  `throw new InvalidAlgorithmParameterException("parameter object not a RSAKeyGenParameterSpec");`
- `sources/com/cardinalcommerce/dependencies/internal/bouncycastle/jcajce/provider/asymmetric/rsa/KeyPairGeneratorSpi.java:49`
  `RSAKeyGenParameterSpec rSAKeyGenParameterSpec = (RSAKeyGenParameterSpec) algorithmParameterSpec;`
- `sources/com/cardinalcommerce/dependencies/internal/bouncycastle/jcajce/provider/asymmetric/rsa/KeyPairGeneratorSpi.java:50`
  `PSSSignatureSpi.SHA1withRSA sHA1withRSA = new PSSSignatureSpi.SHA1withRSA(rSAKeyGenParameterSpec.getPublicExponent(), secureRandom, rSAKeyGenParameterSpec.getKeysize(), PrimeCertaintyCalculator.cca_continue(2048));`
- `sources/com/microsoft/appcenter/utils/crypto/CryptoAesAndEtmHandler.java:4`
  `import android.security.keystore.KeyGenParameterSpec$Builder;`
- `sources/com/microsoft/appcenter/utils/crypto/CryptoAesAndEtmHandler.java:118`
  `keyGenerator.init(new KeyGenParameterSpec$Builder(str, 4).setKeyValidityForOriginationEnd(calendar.getTime()).build());`
- `sources/com/microsoft/appcenter/utils/crypto/CryptoAesHandler.java:4`
  `import android.security.keystore.KeyGenParameterSpec$Builder;`
- `sources/com/microsoft/appcenter/utils/crypto/CryptoAesHandler.java:21`
  `CryptoUtils.ICipher cipher = iCryptoFactory.getCipher(CipherStorageKeystoreAesCbc.ENCRYPTION_TRANSFORMATION, "AndroidKeyStoreBCWorkaround");`
- `sources/com/microsoft/appcenter/utils/crypto/CryptoAesHandler.java:29`
  `CryptoUtils.ICipher cipher = iCryptoFactory.getCipher(CipherStorageKeystoreAesCbc.ENCRYPTION_TRANSFORMATION, "AndroidKeyStoreBCWorkaround");`
- `sources/com/microsoft/appcenter/utils/crypto/CryptoAesHandler.java:44`
  `keyGenerator.init(new KeyGenParameterSpec$Builder(str, 3).setBlockModes(CipherStorageKeystoreAesCbc.BLOCK_MODE_CBC).setEncryptionPaddings(CipherStorageKeystoreAesCbc.PADDING_PKCS7).setKeySize(256).setKeyValidityForOriginationEnd(calendar.getTime()).build());`
- `sources/com/microsoft/appcenter/utils/crypto/CryptoRsaHandler.java:25`
  `return iCryptoFactory.getCipher(CipherStorageKeystoreRsaEcb.TRANSFORMATION_RSA_ECB_PKCS1, i2 >= 23 ? "AndroidKeyStoreBCWorkaround" : "AndroidOpenSSL");`
- `sources/com/microsoft/appcenter/utils/crypto/CryptoUtils.java:284`
  `keyStore = KeyStore.getInstance(CipherStorageBase.KEYSTORE_TYPE);`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageBase.java:4`
  `import android.security.keystore.KeyGenParameterSpec;`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageBase.java:5`
  `import android.security.keystore.KeyGenParameterSpec$Builder;`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageBase.java:46`
  `public static final String KEYSTORE_TYPE = "AndroidKeyStore";`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageBase.java:47`
  `public static final String TEST_KEY_ALIAS = "AndroidKeyStore#supportsSecureHardware";`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageBase.java:228`
  `protected abstract Key e(@NonNull KeyGenParameterSpec keyGenParameterSpec) throws GeneralSecurityException;`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageBase.java:239`
  `protected abstract KeyGenParameterSpec$Builder g(@NonNull String str, @NonNull boolean z2) throws GeneralSecurityException;`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageBase.java:309`
  `KeyStore keyStore = KeyStore.getInstance(KEYSTORE_TYPE);`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageFacebookConceal.java:3`
  `import android.security.keystore.KeyGenParameterSpec;`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageFacebookConceal.java:4`
  `import android.security.keystore.KeyGenParameterSpec$Builder;`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageFacebookConceal.java:73`
  `protected Key e(@NonNull KeyGenParameterSpec keyGenParameterSpec) throws GeneralSecurityException {`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageFacebookConceal.java:101`
  `protected KeyGenParameterSpec$Builder g(@NonNull String str, @NonNull boolean z2) throws GeneralSecurityException {`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageKeystoreAesCbc.java:5`
  `import android.security.keystore.KeyGenParameterSpec;`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageKeystoreAesCbc.java:6`
  `import android.security.keystore.KeyGenParameterSpec$Builder;`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageKeystoreAesCbc.java:72`
  `protected Key e(@NonNull KeyGenParameterSpec keyGenParameterSpec) throws GeneralSecurityException {`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageKeystoreAesCbc.java:76`
  `keyGenerator.init(keyGenParameterSpec);`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageKeystoreAesCbc.java:110`
  `protected KeyGenParameterSpec$Builder g(@NonNull String str, @NonNull boolean z2) throws GeneralSecurityException {`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageKeystoreAesCbc.java:113`
  `return new KeyGenParameterSpec$Builder(str, 3).setBlockModes(BLOCK_MODE_CBC).setEncryptionPaddings(PADDING_PKCS7).setRandomizedEncryptionRequired(true).setKeySize(256);`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageKeystoreRsaEcb.java:5`
  `import android.security.keystore.KeyGenParameterSpec;`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageKeystoreRsaEcb.java:6`
  `import android.security.keystore.KeyGenParameterSpec$Builder;`
- `sources/com/oblador/keychain/cipherStorage/CipherStorageKeystoreRsaEcb.java:68`
  `protected Key e(@NonNull KeyGenParameterSpec keyGenParameterSpec) throws GeneralSecurityException {`

## BR082

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:20`
  `import androidx.core.content.FileProvider;`
- `sources/androidx/browser/customtabs/TrustedWebUtils.java:14`
  `import androidx.core.content.FileProvider;`
- `sources/androidx/browser/customtabs/TrustedWebUtils.java:62`
  `Uri uriForFile = FileProvider.getUriForFile(context, str, file);`
- `sources/androidx/core/content/FileProvider.java:88`
  `@Override // androidx.core.content.FileProvider.PathStrategy`
- `sources/androidx/core/content/FileProvider.java:110`
  `@Override // androidx.core.content.FileProvider.PathStrategy`
- `sources/cl/json/RNShareFileProvider.java:3`
  `import androidx.core.content.FileProvider;`
- `sources/cl/json/RNSharePathUtil.java:13`
  `import androidx.core.content.FileProvider;`
- `sources/cl/json/RNSharePathUtil.java:45`
  `uriForFile = FileProvider.getUriForFile(reactContext, arrayList.get(i2), file);`
- `sources/com/imagepicker/ImagePickerProvider.java:3`
  `import androidx.core.content.FileProvider;`
- `sources/com/imagepicker/Utils.java:19`
  `import androidx.core.content.FileProvider;`
- `sources/com/imagepicker/Utils.java:120`
  `return FileProvider.getUriForFile(context, context.getApplicationContext().getPackageName() + ".imagepickerprovider", file);`
- `sources/com/reactnative/ivpusic/imagepicker/PickerModule.java:16`
  `import androidx.core.content.FileProvider;`
- `sources/com/reactnative/ivpusic/imagepicker/PickerModule.java:441`
  `Uri uriForFile = FileProvider.getUriForFile(activity, activity.getApplicationContext().getPackageName() + ".provider", fileCreateImageFile);`
- `sources/com/reactnativecommunity/webview/RNCWebViewFileProvider.java:3`
  `import androidx.core.content.FileProvider;`
- `sources/com/reactnativecommunity/webview/RNCWebViewModule.java:19`
  `import androidx.core.content.FileProvider;`
- `sources/com/reactnativecommunity/webview/RNCWebViewModule.java:251`
  `return FileProvider.getUriForFile(getReactApplicationContext(), packageName + ".fileprovider", file);`
- `sources/com/RNFetchBlob/RNFetchBlob.java:9`
  `import androidx.core.content.FileProvider;`
- `sources/com/RNFetchBlob/RNFetchBlob.java:78`
  `Uri uriForFile = FileProvider.getUriForFile(getCurrentActivity(), getReactApplicationContext().getPackageName() + ".provider", new File(str));`
- `sources/com/RNFetchBlob/Utils/FileProvider.java:4`
  `public class FileProvider extends androidx.core.content.FileProvider {`
- `sources/zendesk/belvedere/BelvedereFileProvider.java:8`
  `import androidx.core.content.FileProvider;`
- `sources/zendesk/belvedere/BelvedereFileProvider.java:25`
  `@Override // androidx.core.content.FileProvider, android.content.ContentProvider`
- `sources/zendesk/belvedere/Storage.java:13`
  `import androidx.core.content.FileProvider;`
- `sources/zendesk/belvedere/Storage.java:197`
  `return FileProvider.getUriForFile(context, strE, file);`

## BR083

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:139`
  `android:autoVerify="true">`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:154`
  `<intent-filter android:autoVerify="true">`
- `resources/com.bupa.digitalprimarycare.apk/AndroidManifest.xml:327`
  `<intent-filter android:autoVerify="true">`

## BR086

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/android/hardware/fingerprint/FingerprintManager.java:61`
  `public native /* synthetic */ boolean isHardwareDetected();`
- `sources/android/os/SharedMemory.java:10`
  `public final /* synthetic */ class SharedMemory implements Parcelable, Closeable {`
- `sources/android/os/SharedMemory.java:16`
  `public static native /* synthetic */ SharedMemory create(@Nullable String str, int i2) throws ErrnoException;`
- `sources/androidx/appcompat/R.java:63`
  `public static final int actionModeShareDrawable = 0x7f04001a;`
- `sources/androidx/appcompat/R.java:517`
  `public static final int abc_ab_share_pack_mtrl_alpha = 0x7f08001f;`
- `sources/androidx/appcompat/R.java:525`
  `public static final int abc_btn_default_mtrl_shape = 0x7f080027;`
- `sources/androidx/appcompat/R.java:1249`
  `public static final int AppCompatTheme_actionModeShareDrawable = 0x0000001b;`
- `sources/androidx/appcompat/R.java:1361`
  `public static final int DrawerArrowToggle_arrowShaftLength = 0x00000001;`
- `sources/androidx/appcompat/R.java:1532`
  `public static final int[] AppCompatTheme = {android.R.attr.windowIsFloating, android.R.attr.windowAnimationStyle, com.bupa.digitalprimarycare.R.attr.actionBarDivider, com.bupa.digitalprimarycare.R.attr.actionBarItemBackground, com.bupa.digitalprimarycare.R.attr.actionBarPopupTheme, com.bupa.digitalp...`
- `sources/androidx/appcompat/R.java:1536`
  `public static final int[] DrawerArrowToggle = {com.bupa.digitalprimarycare.R.attr.arrowHeadLength, com.bupa.digitalprimarycare.R.attr.arrowShaftLength, com.bupa.digitalprimarycare.R.attr.barLength, com.bupa.digitalprimarycare.R.attr.color, com.bupa.digitalprimarycare.R.attr.drawableSize, com.bupa.di...`
- `sources/androidx/appcompat/R.java:1549`
  `public static final int[] TextAppearance = {android.R.attr.textSize, android.R.attr.typeface, android.R.attr.textStyle, android.R.attr.textColor, android.R.attr.textColorHint, android.R.attr.textColorLink, android.R.attr.shadowColor, android.R.attr.shadowDx, android.R.attr.shadowDy, android.R.attr.s...`
- `sources/androidx/appcompat/app/AppCompatDelegate.java:353`
  `public abstract boolean isHandleNativeActionModesEnabled();`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2313`
  `public boolean isHandleNativeActionModesEnabled() {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:3008`
  `return AppCompatDelegateImpl.this.isHandleNativeActionModesEnabled() ? b(callback) : super.onWindowStartingActionMode(callback);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:3014`
  `if (AppCompatDelegateImpl.this.isHandleNativeActionModesEnabled() && i2 == 0) {`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:28`
  `private float mArrowShaftLength;`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:63`
  `this.mArrowShaftLength = typedArrayObtainStyledAttributes.getDimension(R.styleable.DrawerArrowToggle_arrowShaftLength, 0.0f);`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:81`
  `float fLerp2 = lerp(this.mBarLength, this.mArrowShaftLength, this.mProgress);`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:47`
  `private boolean mReadShareHistoryCalled = false;`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:353`
  `java.lang.String r3 = "Share records file not well-formed."`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:358`
  `java.lang.String r3 = "Share records file does not start with historical-records tag."`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:9`
  `import android.graphics.Shader;`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:53`
  `private final int[] COLORFILTER_TINT_COLOR_CONTROL_NORMAL = {R.drawable.abc_textfield_search_default_mtrl_alpha, R.drawable.abc_textfield_default_mtrl_alpha, R.drawable.abc_ab_share_pack_mtrl_alpha};`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:54`
  `private final int[] TINT_COLOR_CONTROL_NORMAL = {R.drawable.abc_ic_commit_search_api_mtrl_alpha, R.drawable.abc_seekbar_tick_mark_material, R.drawable.abc_ic_menu_share_mtrl_alpha, R.drawable.abc_ic_menu_copy_mtrl_am_alpha, R.drawable.abc_ic_menu_cut_mtrl_alpha, R.drawable.abc_ic_menu_selectall_mtrl...`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:128`
  `bitmapDrawable2.setTileModeX(Shader.TileMode.REPEAT);`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:183`
  `if (i2 == R.drawable.abc_btn_default_mtrl_shape) {`
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
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:50`
  `private Shape getDrawableShape() {`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:51`
  `return new RoundRectShape(new float[]{5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f}, null, null);`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:121`
  `ShapeDrawable shapeDrawable = new ShapeDrawable(getDrawableShape());`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:122`
  `shapeDrawable.getPaint().setShader(new BitmapShader(bitmap, Shader.TileMode.REPEAT, Shader.TileMode.CLAMP));`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:123`
  `shapeDrawable.getPaint().setColorFilter(bitmapDrawable.getPaint().getColorFilter());`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:124`
  `return z2 ? new ClipDrawable(shapeDrawable, 3, 1) : shapeDrawable;`
- `sources/androidx/appcompat/widget/DropDownListView.java:63`
  `private static boolean sHasMethods;`
- `sources/androidx/appcompat/widget/DropDownListView.java:81`
  `sHasMethods = true;`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:342`
  `if (charSequence != null && charSequence.toString().endsWith(AppboyFileUtils.SHARED_PREFERENCES_FILENAME_SUFFIX)) {`
- `sources/androidx/appcompat/widget/SearchView.java:139`
  `autoCompleteTextView.refreshAutoCompleteResults();`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:107`
  `this.f636a.getTheme().resolveAttribute(R.attr.actionModeShareDrawable, typedValue, true);`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:110`
  `activityChooserView.setDefaultActionButtonContentDescription(R.string.abc_shareactionprovider_share_with_application);`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:111`
  `activityChooserView.setExpandActivityOverflowButtonContentDescription(R.string.abc_shareactionprovider_share_with);`
- `sources/androidx/biometric/BiometricFragment.java:187`
  `if (fingerprintManagerCompat.isHardwareDetected()) {`
- `sources/androidx/biometric/CryptoObjectUtils.java:14`
  `import com.oblador.keychain.cipherStorage.CipherStorageKeystoreAesCbc;`
- `sources/androidx/biometric/CryptoObjectUtils.java:129`
  `KeyGenerator keyGenerator = KeyGenerator.getInstance(CipherStorageKeystoreAesCbc.ALGORITHM_AES, "AndroidKeyStore");`
- `sources/androidx/biometric/CryptoObjectUtils.java:133`
  `Cipher cipher = Cipher.getInstance(CipherStorageKeystoreAesCbc.ENCRYPTION_TRANSFORMATION);`
- `sources/androidx/biometric/R.java:74`
  `public static final int actionModeShareDrawable = 0x7f04001a;`
- `sources/androidx/biometric/R.java:559`
  `public static final int abc_ab_share_pack_mtrl_alpha = 0x7f08001f;`
- `sources/androidx/biometric/R.java:567`
  `public static final int abc_btn_default_mtrl_shape = 0x7f080027;`
- `sources/androidx/biometric/R.java:911`
  `public static final int abc_shareactionprovider_share_with = 0x7f11001a;`
- `sources/androidx/biometric/R.java:912`
  `public static final int abc_shareactionprovider_share_with_application = 0x7f11001b;`
- `sources/androidx/biometric/R.java:1411`
  `public static final int AppCompatTheme_actionModeShareDrawable = 0x0000001b;`
- `sources/androidx/biometric/R.java:1524`
  `public static final int DrawerArrowToggle_arrowShaftLength = 0x00000001;`
- `sources/androidx/biometric/R.java:1740`
  `public static final int[] AppCompatTheme = {android.R.attr.windowIsFloating, android.R.attr.windowAnimationStyle, com.bupa.digitalprimarycare.R.attr.actionBarDivider, com.bupa.digitalprimarycare.R.attr.actionBarItemBackground, com.bupa.digitalprimarycare.R.attr.actionBarPopupTheme, com.bupa.digitalp...`
- `sources/androidx/biometric/R.java:1744`
  `public static final int[] DrawerArrowToggle = {com.bupa.digitalprimarycare.R.attr.arrowHeadLength, com.bupa.digitalprimarycare.R.attr.arrowShaftLength, com.bupa.digitalprimarycare.R.attr.barLength, com.bupa.digitalprimarycare.R.attr.color, com.bupa.digitalprimarycare.R.attr.drawableSize, com.bupa.di...`
- `sources/androidx/biometric/R.java:1765`
  `public static final int[] TextAppearance = {android.R.attr.textSize, android.R.attr.typeface, android.R.attr.textStyle, android.R.attr.textColor, android.R.attr.textColorHint, android.R.attr.textColorLink, android.R.attr.shadowColor, android.R.attr.shadowDx, android.R.attr.shadowDy, android.R.attr.s...`
- `sources/androidx/browser/R.java:258`
  `public static final int image_share_filepaths = 0x7f140003;`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:7`
  `import android.content.SharedPreferences;`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:38`
  `public static final String EXTRA_DEFAULT_SHARE_MENU_ITEM = "android.support.customtabs.extra.SHARE_MENU_ITEM";`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:67`
  `public static final int SHARE_STATE_DEFAULT = 0;`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:68`
  `private static final int SHARE_STATE_MAX = 2;`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:69`
  `public static final int SHARE_STATE_OFF = 2;`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:70`
  `public static final int SHARE_STATE_ON = 1;`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:87`
  `public @interface ShareState {`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:151`
  `private int mShareState = 0;`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:168`
  `public Builder addDefaultShareMenuItem() {`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:169`
  `setShareState(1);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:227`
  `this.mIntent.putExtra(CustomTabsIntent.EXTRA_SHARE_STATE, this.mShareState);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:285`
  `public Builder setDefaultShareMenuItemEnabled(boolean z2) {`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:287`
  `setShareState(1);`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:289`
  `setShareState(2);`
- `sources/androidx/browser/trusted/PackageIdentityUtils.java:96`
  `return MessageDigest.getInstance("SHA256").digest(signature.toByteArray());`
- `sources/androidx/browser/trusted/TrustedWebActivityIntentBuilder.java:15`
  `import androidx.browser.trusted.sharing.ShareData;`
- `sources/androidx/browser/trusted/TrustedWebActivityIntentBuilder.java:16`
  `import androidx.browser.trusted.sharing.ShareTarget;`
- `sources/androidx/browser/trusted/TrustedWebActivityIntentBuilder.java:28`
  `public static final String EXTRA_SHARE_DATA = "androidx.browser.trusted.extra.SHARE_DATA";`
- `sources/androidx/browser/trusted/TrustedWebActivityIntentBuilder.java:29`
  `public static final String EXTRA_SHARE_TARGET = "androidx.browser.trusted.extra.SHARE_TARGET";`
- `sources/androidx/browser/trusted/TrustedWebActivityIntentBuilder.java:38`
  `private ShareData mShareData;`
- `sources/androidx/browser/trusted/TrustedWebActivityIntentBuilder.java:41`
  `private ShareTarget mShareTarget;`

## BR088

paper_id: B004
paper_title: Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation

- `sources/androidx/exifinterface/media/ExifInterface.java:1754`
  `seekableByteOrderedDataInputStream.readFully(bArr2);`
- `sources/com/onfido/android/sdk/capture/ui/proofOfAddress/documentSubmission/PoaDocumentSubmissionViewModel.java:44`
  `@Metadata(d1 = {"\u0000\u0090\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0...`
- `sources/com/onfido/android/sdk/capture/ui/proofOfAddress/documentSubmission/PoaDocumentSubmissionViewModel.java:367`
  `public final Bitmap loadBitmapFromPdfUri(@NotNull Uri uri, @NotNull ContentResolver contentResolver, int densityDpi) throws FileNotFoundException {`
- `sources/kotlin/jvm/internal/AdaptedFunctionReference.java:9`
  `public class AdaptedFunctionReference implements FunctionBase, Serializable {`
- `sources/kotlin/jvm/internal/AdaptedFunctionReference.java:20`
  `public AdaptedFunctionReference(int i2, Class cls, String str, String str2, int i3) {`
- `sources/kotlin/jvm/internal/AdaptedFunctionReference.java:28`
  `if (!(obj instanceof AdaptedFunctionReference)) {`
- `sources/kotlin/jvm/internal/AdaptedFunctionReference.java:31`
  `AdaptedFunctionReference adaptedFunctionReference = (AdaptedFunctionReference) obj;`
- `sources/kotlin/jvm/internal/AdaptedFunctionReference.java:32`
  `return this.isTopLevel == adaptedFunctionReference.isTopLevel && this.arity == adaptedFunctionReference.arity && this.flags == adaptedFunctionReference.flags && Intrinsics.areEqual(this.f19283a, adaptedFunctionReference.f19283a) && Intrinsics.areEqual(this.owner, adaptedFunctionReference.owner) && t...`
- `sources/kotlin/jvm/internal/AdaptedFunctionReference.java:59`
  `public AdaptedFunctionReference(int i2, Object obj, Class cls, String str, String str2, int i3) {`

## BR090

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `audit_reports/00_independent_findings.md:106`
  `- 不作为 confirmed secret 泄露，只作为清理生产包 mock 数据的工程风险。`
- `audit_reports/01_evidence_chain.md:3`
  `本文档记录可复核证据和数据流。结论边界：没有 ADB、Frida、抓包、真实本地存储和真实 BLE 设备证据，因此动态行为、云端接收方、真实 payload、真实 token 有效性均不得写成 confirmed。`
- `audit_reports/01_evidence_chain.md:102`
  `confirmed 的内容：`
- `audit_reports/01_evidence_chain.md:152`
  `confirmed 的内容：`
- `audit_reports/01_evidence_chain.md:179`
  `- 可以 confirmed 的是生产 Manifest 允许 cleartext traffic。`
- `audit_reports/01_evidence_chain.md:180`
  `- 不能 confirmed 的是敏感数据实际通过 HTTP 发送，因为没有抓包，也没有确认业务生产 HTTP endpoint。`
- `audit_reports/01_evidence_chain.md:195`
  `这些证据支持 App 存在一方业务、认证、GraphQL、观测端点。由于都是 HTTPS，不能支持 BR013 的“敏感 HTTP endpoint” confirmed。`
- `audit_reports/01_evidence_chain.md:217`
  `因此 BR009、BR010、BR011、BR095 不支持 confirmed。`
- `audit_reports/01_evidence_chain.md:237`
  `- confirmed：APK 内嵌多类服务 key/secret-like 标识。`
- `audit_reports/01_evidence_chain.md:282`
  `- confirmed：标识符访问能力和授权参数拼接代码存在。`
- `audit_reports/01_evidence_chain.md:301`
  `- confirmed：App 处理健康/身份/处方/心理健康/保险等敏感数据类型的代码和 UI 表面存在。`
- `audit_reports/01_evidence_chain.md:321`
  `- 宽路径和重复 authority 是独立工程风险，只能写 supported_hypothesis，不能写 confirmed 数据泄露。`
- `audit_reports/01_evidence_chain.md:322`
  `- 'allowBackup=false'，因此 BR028 的 backup 风险不支持 confirmed。`
- `audit_reports/02_rule_by_rule_mapping.md:3`
  `结论只能是 'confirmed'、'supported_hypothesis'、'not_supported'、'not_testable'。`
- `audit_reports/02_rule_by_rule_mapping.md:4`
  `判断标准：静态证据足以证明配置/代码路径存在时写 'confirmed'；已有代码和上下文支持但缺少动态 payload/真实数据时写 'supported_hypothesis'；检索到相反证据或关键条件不存在时写 'not_supported'；必须依赖运行、设备、抓包、账户、BLE 外设、远端响应或本地存储转储时写 'not_testable'。`
- `audit_reports/02_rule_by_rule_mapping.md:10`
  `| BR003 | confirmed | B023 / Android Permissions Demystified | 权限可由库代码触发，应区分一方与三方。 | AppsFlyer/Branch/Braze 等三方 SDK 存在 Advertising ID、TelephonyManager、Settings.Secure 能力；Manifest 有 AD_ID/READ_PHONE_STATE。确认能力，不确认上传。 |`
- `audit_reports/02_rule_by_rule_mapping.md:11`
  `| BR004 | confirmed | B006 / Analyzing security issues of android mobile health and medical applications | mHealth 基线关注危险权限与敏感能力。 | Manifest 明确请求 CAMERA、RECORD_AUDIO、LOCATION、READ/WRITE_EXTERNAL_STORAGE、READ_PHONE_STATE、AD_ID、Bluetooth。确认危险权限基线存在，不等同漏洞。 |`
- `audit_reports/02_rule_by_rule_mapping.md:13`
  `| BR006 | confirmed | B016 / A privacy and security analysis of Android COVID-19 contact tracing apps | 论文把明文传输/静态安全配置作为 Android 安全问题。 | 'AndroidManifest.xml:125' 设置 'usesCleartextTraffic="true"'，且未发现 NSC。确认 cleartext policy 过宽；不确认敏感 HTTP 传输。 |`
- `audit_reports/02_rule_by_rule_mapping.md:21`
  `| BR014 | confirmed | B022 / A Study of Android Application Security | 论文发现手机标识符、地理位置和广告/分析库广泛使用。 | Manifest 有 AD_ID/READ_PHONE_STATE；Branch/AppsFlyer 等 SDK 访问广告 ID/Telephony；Auth 参数包含设备名。确认标识符访问能力。 |`
- `audit_reports/02_rule_by_rule_mapping.md:23`
  `| BR016 | confirmed | B006 / Analyzing security issues of android mobile health and medical applications | 论文将硬编码敏感信息列为 mHealth 静态问题。 | APK 内有 AppCenter app_secret、Braze key、Google API key、Branch key、Sentry DSN、liveChat key、一方 DEFAULT_API_KEY。确认嵌入式 key/secret-like 标识存在，不确认可滥用。 |`
- `audit_reports/02_rule_by_rule_mapping.md:25`
  `| BR018 | confirmed | B001 / Security Concerns in Android mHealth Apps | mHealth App 处理个人健康、测量、咨询等敏感数据。 | bundle/UI/业务含 appointment、consultation、patient、medical history、monitor、metric、health report 等。确认敏感健康数据表面。 |`
- `audit_reports/02_rule_by_rule_mapping.md:26`
  `| BR019 | confirmed | B011 / Locking it down: The privacy and security of mobile medication apps | 药物、处方、提醒等是敏感健康信息。 | bundle/strings 出现 prescription、referral、pharmacy、sick certificate 等医疗文档/药房相关流程。 |`
- `audit_reports/02_rule_by_rule_mapping.md:27`
  `| BR020 | confirmed | B012 / Privacy policies of Android apps for depression | 心理健康数据高度敏感，需要透明处理。 | bundle/strings 含 GAD-7、PHQ-9、anxiety、depression 等心理健康量表/文案。确认数据类型，不确认泄露。 |`
- `audit_reports/02_rule_by_rule_mapping.md:33`
  `| BR026 | confirmed | B002 / Unaddressed privacy risks in accredited health and wellness apps | 论文协议测试本地存储和传输，报告过本地存储保护不足。 | session token 字段进入 Redux 持久化白名单，encrypt key 来自 bundle 静态 getKey。确认代码级存储设计风险；未确认设备中真实 token。 |`
- `audit_reports/02_rule_by_rule_mapping.md:36`
  `| BR029 | confirmed | B016 / A privacy and security analysis of Android COVID-19 contact tracing apps | 组件暴露和外部入口属于 Android 静态安全问题。 | exported RNBootSplash/MainActivity 接收/转发 Intent，'setLaunchType' 影响视频问诊状态和服务。确认静态路径。 |`
- `audit_reports/02_rule_by_rule_mapping.md:39`
  `| BR032 | confirmed | B026 / Measuring Insecurity of Mobile Deep Links of Android | custom scheme deep link 可被外部触发/劫持，BROWSABLE 是 web 可达入口。 | 'com.bupa.digitalprimarycare'、'bupabluahealth'、Braintree scheme 等 BROWSABLE/custom schemes 存在。确认入口面。 |`
- `audit_reports/02_rule_by_rule_mapping.md:43`
  `| BR040 | confirmed | B007 / Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | 三方 SDK 默认初始化和隐私设置会影响数据收集。 | MainApplication 启动 Braze/Appboy、Branch；JS 启动 Sentry/O11y/native events。确认初始化链。 |`
- `audit_reports/02_rule_by_rule_mapping.md:52`
  `| BR055 | confirmed | B014 / Privacy Assessment in Mobile Health Apps | mHealth 隐私评估应组织多层证据。 | 本审计按 Manifest、代码、资源、存储、网络、动态缺口、云端假设组织。 |`
- `audit_reports/02_rule_by_rule_mapping.md:53`
  `| BR058 | confirmed | B014 / Privacy Assessment in Mobile Health Apps | 评估应区分一方代码与三方 SDK。 | 报告中将 'com.babylon.cyrus' 与 Branch/AppsFlyer/Braze/Auth0/Braintree/Onfido 等分开。 |`
- `audit_reports/02_rule_by_rule_mapping.md:54`
  `| BR059 | confirmed | B006 / Analyzing security issues of android mobile health and medical applications | targetSdk/exported/default 行为影响 Android 组件风险。 | targetSdk 33；多个 Activity 显式 exported=true；MainActivity/RNBootSplash 暴露路径影响业务状态。 |`
- `audit_reports/02_rule_by_rule_mapping.md:74`
  `| BR079 | not_testable | B030 / Why Eve and Mallory Love Android | 弱 TrustManager/HostnameVerifier 是否运行时可达需要结合代码路径或 MITM。 | 静态未发现一方弱 TLS path；无运行时路径覆盖，因此写 not_testable 而非 confirmed。 |`
- `audit_reports/02_rule_by_rule_mapping.md:78`
  `| BR083 | not_testable | B016 / A privacy and security analysis of Android COVID-19 contact tracing apps | exported component 能否被外部调用并改变状态需 ADB/外部 App 验证。 | 静态链 confirmed，但未运行 'adb shell am start'，所以动态规则 not_testable。 |`
- `audit_reports/02_rule_by_rule_mapping.md:79`
  `| BR084 | not_testable | B026 / Measuring Insecurity of Mobile Deep Links of Android | crafted URI 是否达到敏感页面/动作需设备和路由验证。 | 静态入口 confirmed；未实测 crafted URI。 |`
- `audit_reports/02_rule_by_rule_mapping.md:82`
  `| BR090 | confirmed | B014 / Privacy Assessment in Mobile Health Apps | mHealth 隐私评估应把静态高风险项转为手机端验证计划。 | 总报告第 11 节列出 exported Activity、storage、proxy、deep link、SDK consent 的优先动态验证清单。 |`
- `audit_reports/03_final_audit_report.md:15`
  `## 2. Available Evidence`
- `audit_reports/03_final_audit_report.md:39`
  `- 单个权限、单个 URL、单个 SDK、单个字符串不直接作为 confirmed。`
- `audit_reports/03_final_audit_report.md:40`
  `- confirmed 只用于静态 artifact 自身即可证明的事实，例如 Manifest cleartext policy、exported 组件、硬编码 key 存在、代码级数据流。`
- `audit_reports/03_final_audit_report.md:41`
  `- 涉及“实际上传”“实际泄露”“真实 token 文件”“BLE 连接”“同意前发送”的结论，必须有动态/抓包/本地存储证据；本次没有，因此不写 confirmed。`
- `audit_reports/03_final_audit_report.md:48`
  `- 结论：'confirmed' for BR029/BR059；'not_testable' for BR083。`
- `audit_reports/03_final_audit_report.md:56`
  `- 结论：'confirmed' for BR026 的代码级存储设计；'confirmed' for BR016 的硬编码 secret-like material；BR076/BR079 为 'not_testable'。`
- `audit_reports/03_final_audit_report.md:63`
  `- 结论：'confirmed' for BR006；BR013 为 'not_supported'。`
- `audit_reports/03_final_audit_report.md:70`
  `- 结论：'confirmed' for BR016。`
- `audit_reports/03_final_audit_report.md:77`
  `- 结论：BR014/BR040 为 'confirmed'；BR041/BR092 为 'supported_hypothesis'；BR077 为 'not_testable'。`
- `audit_reports/03_final_audit_report.md:84`
  `- 结论：BR032 为 'confirmed'；BR033/BR034 为 'supported_hypothesis'；BR035/BR084 为 'not_testable'。`
- `audit_reports/03_final_audit_report.md:98`
  `- 结论：BR018/BR019/BR020 为 'confirmed' 数据类型存在；BR091/BR094/BR096 为 'supported_hypothesis'。`
- `audit_reports/03_final_audit_report.md:117`
  `无 confirmed 动态发现。`
- `audit_reports/03_final_audit_report.md:122`
  `无 confirmed 云端上传发现。`
- `audit_reports/03_final_audit_report.md:129`
  `这些都需要抓包、证书代理或端点日志才能升级为 confirmed。`
- `audit_reports/03_final_audit_report.md:133`
  `没有 cross-layer confirmed finding，因为缺少动态层证据。`
- `audit_reports/04_mentor_review_and_revisions.md:25`
  `- 已修订：BR026 写成“confirmed code-level storage design”，同时明确“未确认真实设备 token 文件”。`
- `audit_reports/04_mentor_review_and_revisions.md:44`
  `- 不能把“危险权限存在”写成漏洞 confirmed；只能确认权限基线存在。`
- `audit_reports/04_mentor_review_and_revisions.md:45`
  `- 已修订：BR004 为 confirmed baseline，而 BR001/BR002 对过度权限写 'supported_hypothesis'。`
- `audit_reports/04_mentor_review_and_revisions.md:54`
  `- 已修订：BR040 confirmed 只写“SDK 初始化链存在”；BR041/BR092 只写 supported_hypothesis，不写“已经违规收集”。`
- `audit_reports/04_mentor_review_and_revisions.md:72`
  `- 'usesCleartextTraffic=true' 是 confirmed 配置风险。`
- `audit_reports/04_mentor_review_and_revisions.md:74`
  `- 已修订：BR006 confirmed；BR013 not_supported；BR080 not_testable。`
- `audit_reports/04_mentor_review_and_revisions.md:84`
  `- 已修订：BR019 confirmed 数据类型；BR096 supported_hypothesis。`
- `audit_reports/04_mentor_review_and_revisions.md:94`
  `- 已修订：BR020 confirmed 数据类型；BR051 not_testable。`
- `audit_reports/04_mentor_review_and_revisions.md:104`
  `- 已修订：BR055/BR058 confirmed 为报告方法层面的合规。`
- `audit_reports/04_mentor_review_and_revisions.md:114`
  `- 已修订：涉及运行时资源/组件触发的动态规则保持 not_testable；BR029/BR059 依据静态代码链 confirmed。`
- `audit_reports/04_mentor_review_and_revisions.md:133`
  `- 已修订：BR014 confirmed 能力；BR015/BR094 supported_hypothesis。`
- `audit_reports/04_mentor_review_and_revisions.md:142`
  `- 已修订：BR001/BR002 supported_hypothesis，而非 confirmed。`
- `audit_reports/04_mentor_review_and_revisions.md:150`
  `- 本 App Provider 多为 'exported=false'，不能写 B024 confirmed。`
- `audit_reports/04_mentor_review_and_revisions.md:170`
  `- Manifest 中 custom scheme/BROWSABLE 能 confirmed 入口面。`
- `audit_reports/04_mentor_review_and_revisions.md:172`
  `- 已修订：BR032 confirmed；BR033/BR034 supported_hypothesis；BR035/BR084 not_testable。`
- `audit_reports/04_mentor_review_and_revisions.md:181`
  `- 已修订：BR061-BR075 不写 confirmed。`
- `audit_reports/04_mentor_review_and_revisions.md:213`
  `导师式审查意见：可以确认设计弱点，但不能确认真实 token 文件。报告已把 BR026 写成 code-level confirmed，并将运行时文件读取列为 follow-up。`
- `audit_reports/04_mentor_review_and_revisions.md:225`
  `导师式审查意见：报告中所有“第三方上传”类结论必须保持 supported_hypothesis/not_testable。已修订，没有写 confirmed 数据外发。`
- `audit_reports/04_mentor_review_and_revisions.md:237`
  `导师式审查意见：这是工程风险，不是 B024 confirmed。报告已分离。`
- `audit_reports/04_mentor_review_and_revisions.md:244`
  `- 将 SDK 数据上传从 confirmed 收敛为 'supported_hypothesis'/'not_testable'。`
- `audit_reports/04_mentor_review_and_revisions.md:247`
  `- 将本地 token 问题明确写成“代码级存储设计 confirmed”，并标注“未确认真实设备 token 文件”。`
- `audit_reports/04_mentor_review_and_revisions.md:248`
  `- 将 exported Activity 发现限定为“外部 Intent 影响本地视频问诊状态和服务调用代码路径 confirmed”，不声称后端状态被改变。`
- `audit_reports/04_mentor_review_and_revisions.md:252`
  `本次报告中最可靠的 confirmed 静态问题是：`
- `audit_reports/04_mentor_review_and_revisions.md:263`
  `- 真实本地 token 泄露、真实网络 payload、SDK 同意前上传、云端接收方、深链认证绕过、BLE 连接/数据上传，都未达到 confirmed 标准。`

## BR091

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/com/onfido/android/sdk/capture/component/active/video/capture/data/remote/ActiveVideoCaptureApi.java:35`
  `@PUT("biometrics/media")`
- `sources/com/onfido/android/sdk/capture/component/active/video/capture/data/remote/ActiveVideoCaptureApi.java:37`
  `@Multipart`
- `sources/com/onfido/android/sdk/capture/component/active/video/capture/data/remote/AVCGuidanceVideoApi.java:13`
  `@GET`
- `sources/com/onfido/android/sdk/capture/document/supported/data/remote/datasource/SupportedDocumentsApi.java:14`
  `@GET("supported_documents")`
- `sources/com/onfido/android/sdk/capture/internal/util/logging/network/OnfidoLoggerApi.java:15`
  `@POST("/sdk/logger")`
- `sources/com/onfido/android/sdk/capture/ui/camera/liveness/intro/LivenessIntroVideoApi.java:15`
  `@GET`
- `sources/com/onfido/android/sdk/capture/ui/camera/liveness/intro/LivenessIntroVideoApi.java:19`
  `@GET`
- `sources/com/onfido/android/sdk/capture/ui/proofOfAddress/network/ProofOfAddressApi.java:14`
  `@GET("/report_types/proof_of_address/supported_countries")`
- `sources/com/onfido/android/sdk/capture/ui/userconsent/network/UserConsentApi.java:18`
  `@PATCH("/applicants/{uuid}/consents")`
- `sources/com/onfido/android/sdk/capture/ui/userconsent/network/UserConsentApi.java:23`
  `@GET("/applicants/{uuid}/consents")`
- `sources/com/onfido/android/sdk/capture/ui/userconsent/network/UserConsentApi.java:28`
  `@PATCH("/applicants/{uuid}/location")`
- `sources/com/onfido/api/client/OnfidoService.java:27`
  `@POST("documents")`
- `sources/com/onfido/api/client/OnfidoService.java:31`
  `@POST("live_video_challenge")`
- `sources/com/onfido/api/client/OnfidoService.java:39`
  `@POST("sdk/configurations")`
- `sources/com/onfido/api/client/OnfidoService.java:43`
  `@POST("documents")`
- `sources/com/onfido/api/client/OnfidoService.java:47`
  `@POST("document_video_media")`
- `sources/com/onfido/api/client/OnfidoService.java:51`
  `@POST("live_photos")`
- `sources/com/onfido/api/client/OnfidoService.java:55`
  `@POST("live_videos")`
- `sources/com/onfido/api/client/OnfidoService.java:59`
  `@POST("documents/media")`
- `sources/com/onfido/api/client/OnfidoService.java:63`
  `@POST("documents")`
- `sources/com/onfido/workflow/internal/network/WorkflowApi.java:21`
  `@POST("workflow_runs/{workflow_run_id}/tasks/{task_id}/complete")`
- `sources/com/onfido/workflow/internal/network/WorkflowApi.java:26`
  `@GET("workflow_runs/{workflow_run_id}/tasks/current")`

## BR092

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/androidx/appcompat/R.java:1546`
  `public static final int[] SearchView = {android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.inputType, android.R.attr.imeOptions, com.bupa.digitalprimarycare.R.attr.closeIcon, com.bupa.digitalprimarycare.R.attr.commitIcon, com.bupa.digitalprimarycare.R.attr.defaultQueryHint, com.bupa.d...`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:415`
  `return powerManager.isPowerSaveMode();`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:100`
  `canvas.save();`
- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:551`
  `this.mDecorToolbar.saveHierarchyState(sparseArray);`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:509`
  `synchronized (this.mInstanceLock) {`
- `sources/androidx/appcompat/widget/AppCompatRatingBar.java:21`
  `protected synchronized void onMeasure(int i2, int i3) {`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:89`
  `int iSave = canvas.save();`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:95`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:32`
  `private boolean mAsyncFontPending;`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:291`
  `this.mAsyncFontPending = this.mFontTypeface == null;`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:387`
  `synchronized (rectF) {`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:455`
  `ViewCompat.saveAttributeDataForStyleable(textView, textView.getContext(), iArr, attributeSet, typedArrayObtainStyledAttributes, i2, 0);`
- `sources/androidx/appcompat/widget/SearchView.java:118`
  `private final View mSubmitArea;`
- `sources/androidx/appcompat/widget/SearchView.java:119`
  `private boolean mSubmitButtonEnabled;`
- `sources/androidx/appcompat/widget/SwitchCompat.java:607`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/biometric/R.java:1760`
  `public static final int[] SearchView = {android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.inputType, android.R.attr.imeOptions, com.bupa.digitalprimarycare.R.attr.closeIcon, com.bupa.digitalprimarycare.R.attr.commitIcon, com.bupa.digitalprimarycare.R.attr.defaultQueryHint, com.bupa.d...`
- `sources/androidx/browser/browseractions/BrowserServiceFileProvider.java:46`
  `private static class FileCleanupTask extends AsyncTask<Void, Void, Void> {`
- `sources/androidx/camera/camera2/internal/Camera2CapturePipeline.java:548`
  `public ListenableFuture<List<Void>> submitStillCaptures(@NonNull List<CaptureConfig> list, int i2, int i3, int i4) {`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:828`
  `Logger.d(TAG, "Attempting to submit CaptureRequest after setting");`
- `sources/androidx/camera/camera2/internal/ZoomControl.java:190`
  `synchronized (this.mCurrentZoomState) {`
- `sources/androidx/camera/core/AndroidImageProxy.java:77`
  `public synchronized int getFormat() {`
- `sources/androidx/camera/core/AndroidImageProxy.java:82`
  `public synchronized int getHeight() {`
- `sources/androidx/camera/core/AndroidImageProxy.java:88`
  `public synchronized Image getImage() {`
- `sources/androidx/camera/core/AndroidImageReaderProxy.java:102`
  `synchronized (this.mLock) {`
- `sources/androidx/camera/core/CameraX.java:262`
  `synchronized (this.mInitializeLock) {`
- `sources/androidx/camera/core/CaptureProcessorPipeline.java:140`
  `synchronized (this.mLock) {`
- `sources/androidx/camera/core/ForwardingImageProxy.java:63`
  `public synchronized int getFormat() {`
- `sources/androidx/camera/core/ForwardingImageProxy.java:68`
  `public synchronized int getHeight() {`
- `sources/androidx/camera/core/ForwardingImageProxy.java:74`
  `public synchronized Image getImage() {`
- `sources/androidx/camera/core/ImageProxyDownsampler.java:43`
  `public synchronized int getHeight() {`
- `sources/androidx/camera/core/ImageProxyDownsampler.java:49`
  `public synchronized ImageProxy.PlaneProxy[] getPlanes() {`
- `sources/androidx/camera/core/ImageSaver.java:26`
  `final class ImageSaver implements Runnable {`
- `sources/androidx/camera/core/ImageSaver.java:30`
  `private static final String TAG = "ImageSaver";`
- `sources/androidx/camera/core/ImageSaver.java:35`
  `private final OnImageSavedCallback mCallback;`
- `sources/androidx/camera/core/ImageSaver.java:91`
  `this.mCallback = onImageSavedCallback;`
- `sources/androidx/camera/core/ImageSaver.java:198`
  `Logger.e(TAG, "Application executor rejected executing OnImageSavedCallback.onImageSaved callback. Skipping.");`
- `sources/androidx/camera/core/ImageSaver.java:203`
  `private File saveImageToTempFile() {`
- `sources/androidx/camera/core/ImageSaver.java:205`
  `SaveError saveError;`
- `sources/androidx/camera/core/ImageSaver.java:210`
  `if (isSaveToFile()) {`
- `sources/androidx/camera/core/ImageSaver.java:234`
  `saveError = SaveError.FILE_IO_FAILED;`

## BR093

paper_id: B004
paper_title: Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation

- `sources/androidx/camera/core/ImageSaver.java:210`
  `if (isSaveToFile()) {`
- `sources/androidx/work/ForegroundUpdater.java:11`
  `ListenableFuture<Void> setForegroundAsync(@NonNull Context context, @NonNull UUID uuid, @NonNull ForegroundInfo foregroundInfo);`
- `sources/androidx/work/ListenableWorker.java:194`
  `settableFutureCreate.setException(new IllegalStateException("Expedited WorkRequests require a ListenableWorker to provide an implementation for 'getForegroundInfoAsync()'"));`
- `sources/androidx/work/impl/utils/WorkForegroundUpdater.java:39`
  `public ListenableFuture<Void> setForegroundAsync(@NonNull final Context context, @NonNull final UUID uuid, @NonNull final ForegroundInfo foregroundInfo) {`
- `sources/androidx/work/impl/utils/WorkForegroundUpdater.java:49`
  `throw new IllegalStateException("Calls to setForegroundAsync() must complete before a ListenableWorker signals completion of work by returning an instance of Result.");`
- `sources/com/appboy/AppboyUser.java:78`
  `synchronized (this.mUserIdLock) {`
- `sources/com/appboy/AppboyUser.java:351`
  `synchronized (this.mUserIdLock) {`
- `sources/com/appboy/models/push/BrazeNotificationPayload.java:49`
  `public String mContentCardSyncData;`
- `sources/com/appboy/models/push/BrazeNotificationPayload.java:52`
  `public String mContentCardSyncUserId;`
- `sources/com/appboy/models/push/BrazeNotificationPayload.java:391`
  `this.mContentCardSyncData = parseString(this.mNotificationExtras, Constants.APPBOY_PUSH_CONTENT_CARD_SYNC_DATA_KEY);`
- `sources/com/appboy/models/push/BrazeNotificationPayload.java:392`
  `this.mContentCardSyncUserId = parseString(this.mNotificationExtras, Constants.APPBOY_PUSH_CONTENT_CARD_SYNC_USER_ID_KEY);`
- `sources/com/appboy/models/push/BrazeNotificationPayload.java:579`
  `public String getContentCardSyncData() {`
- `sources/com/appboy/models/push/BrazeNotificationPayload.java:580`
  `return this.mContentCardSyncData;`
- `sources/com/appboy/models/push/BrazeNotificationPayload.java:584`
  `public String getContentCardSyncUserId() {`
- `sources/com/appboy/models/push/BrazeNotificationPayload.java:585`
  `return this.mContentCardSyncUserId;`
- `sources/com/appboy/models/push/BrazeNotificationPayload.java:715`
  `public void setContentCardSyncData(@Nullable String str) {`
- `sources/com/appboy/models/push/BrazeNotificationPayload.java:716`
  `this.mContentCardSyncData = str;`
- `sources/com/appboy/models/push/BrazeNotificationPayload.java:719`
  `public void setContentCardSyncUserId(@Nullable String str) {`
- `sources/com/appboy/models/push/BrazeNotificationPayload.java:720`
  `this.mContentCardSyncUserId = str;`
- `sources/com/appboy/models/push/BrazeNotificationPayload.java:799`
  `return "\nNotificationExtras=" + this.mNotificationExtras + "\n, AppboyExtras=" + this.mAppboyExtras + "\n, PushDuration=" + this.mPushDuration + "\n, IsPushStory=" + this.mIsPushStory + "\n, PublicNotificationExtras='" + this.mPublicNotificationExtras + "'\n, NotificationChannelId='" + this.mNotifi...`
- `sources/com/appboy/push/AppboyNotificationUtils.java:175`
  `String contentCardSyncData = brazeNotificationPayload.getContentCardSyncData();`
- `sources/com/appboy/push/AppboyNotificationUtils.java:176`
  `String contentCardSyncUserId = brazeNotificationPayload.getContentCardSyncUserId();`
- `sources/com/appboy/push/AppboyNotificationUtils.java:177`
  `if (contentCardSyncData == null || brazeNotificationPayload.getContext() == null) {`
- `sources/com/appboy/push/AppboyNotificationUtils.java:180`
  `AppboyLogger.d(TAG, "Push contains associated Content Cards card. User id: " + contentCardSyncUserId + " Card data: " + contentCardSyncData);`
- `sources/com/appboy/push/AppboyNotificationUtils.java:181`
  `AppboyInternal.addSerializedContentCardToStorage(brazeNotificationPayload.getContext(), contentCardSyncData, contentCardSyncUserId);`
- `sources/com/appboy/support/StringUtils.java:72`
  `AppboyLogger.d(TAG, "The saved user id hash was null or empty.");`
- `sources/com/appsflyer/deeplink/DeepLink.java:37`
  `setKeySet.removeAll(Arrays.asList("install_time", "pid", "c", "af_prt", "af_mp", "clickid", "af_siteid", "af_sub_siteid", "af_click_lookback", "af_viewthrough_lookback", "af_keywords", "af_cost_model", "af_cost_currency", "af_cost_value", "af_r", "af_web_dp", "af_force_deeplink", "af_ref", "is_incen...`
- `sources/com/appsflyer/internal/AFb1lSDK.java:22`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:13:0x0054 -> B:14:0x0064). Please report as a decompilation issue!!! */`
- `sources/com/appsflyer/internal/AFb1xSDK.java:4776`
  `AFLogger.afInfoLog("CustomerUserId not set, reporting is disabled", false);`
- `sources/com/appsflyer/internal/AFb1xSDK.java:4778`
  `AFLogger.afInfoLog("CustomerUserId not set, reporting is disabled", true);`
- `sources/com/appsflyer/share/ShareInviteHelper.java:31`
  `AFLogger.afWarnLog("[Invite] Cannot report App-Invite with null/empty channel");`
- `sources/com/appsflyer/share/ShareInviteHelper.java:35`
  `AFLogger.afInfoLog("CustomerUserId not set, report Invite is disabled", true);`
- `sources/com/appsflyer/share/ShareInviteHelper.java:40`
  `AFLogger.afDebugLog("[Invite] Reporting App-Invite via channel: ".concat(String.valueOf(str)));`
- `sources/com/auth0/android/authentication/storage/BaseCredentialsManager.java:19`
  `@Metadata(bv = {}, d1 = {"\u0000\\\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0010\u00...`
- `sources/com/auth0/android/authentication/storage/SecureCredentialsManager.java:178`
  `this$0.saveCredentials(credentials2);`
- `sources/com/auth0/android/management/UsersAPIClient.java:154`
  `return this.factory.post(httpUrlBuild.getUrl(), GsonAdapter.INSTANCE.forListOf(UserIdentity.class, this.gson)).addParameters(ParameterBuilder.Companion.newBuilder$default(ParameterBuilder.INSTANCE, null, 1, null).set(LINK_WITH_KEY, secondaryToken).asDictionary());`
- `sources/com/braintreepayments/api/AnalyticsClient.java:133`
  `private final UUID scheduleAnalyticsUpload(Configuration configuration, Authorization authorization, String str, String str2) throws Throwable {`
- `sources/com/braintreepayments/api/AnalyticsClient.java:136`
  `OneTimeWorkRequest oneTimeWorkRequestBuild = new OneTimeWorkRequest.Builder(AnalyticsUploadWorker.class).setInitialDelay(30L, TimeUnit.SECONDS).setInputData(dataBuild).build();`
- `sources/com/braintreepayments/api/AnalyticsClient.java:137`
  `Intrinsics.checkNotNullExpressionValue(oneTimeWorkRequestBuild, "Builder(AnalyticsUploadW…ata)\n            .build()");`
- `sources/com/braintreepayments/api/AnalyticsClient.java:139`
  `this.workManager.enqueueUniqueWork(WORK_NAME_ANALYTICS_UPLOAD, ExistingWorkPolicy.KEEP, oneTimeWorkRequest);`

## BR094

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `sources/android/support/customtabs/ICustomTabsCallback.java:38`
  `public void onPostMessage(String str, Bundle bundle) throws RemoteException {`
- `sources/android/support/customtabs/ICustomTabsCallback.java:273`
  `onPostMessage(parcel.readString(), parcel.readInt() != 0 ? (Bundle) Bundle.CREATOR.createFromParcel(parcel) : null);`
- `sources/android/support/customtabs/ICustomTabsCallback.java:306`
  `void onPostMessage(String str, Bundle bundle) throws RemoteException;`
- `sources/android/support/customtabs/ICustomTabsService.java:463`
  `parcel2.writeInt(iPostMessage);`
- `sources/android/support/customtabs/ICustomTabsService.java:509`
  `boolean requestPostMessageChannelWithExtras(ICustomTabsCallback iCustomTabsCallback, Uri uri, Bundle bundle) throws RemoteException;`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:878`
  `synchronized (MediaSessionImplBase.this.f124e) {`
- `sources/androidx/activity/result/ActivityResultRegistry.java:179`
  `public final void onSaveInstanceState(@NonNull Bundle bundle) {`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:14`
  `@Metadata(d1 = {"\u0000.\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\b\u0004\b&\u0018\u0000*\u0004\b\u0000\u0010\u0001*\u0004\b\u0001\u0010\u00022\u...`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:18`
  `@Metadata(d1 = {"\u0000\u000e\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0000\n\u0002\b\u0006\u0018\u0000*\u0004\b\u0002\u0010\u00012\u00020\u0002B\r\u0012\u0006\u0010\u0003\u001a\u00028\u0002¢\u0006\u0002\u0010\u0004R\u0013\u0010\u0003\u001a\u00028\u0002¢\u0006\n\n\u0002\u0010\u0007\u001a\u0004\b\u...`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:19`
  `public static final class SynchronousResult<T> {`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:22`
  `public SynchronousResult(T t2) {`
- `sources/androidx/appcompat/app/AppCompatViewInflater.java:217`
  `/* JADX WARN: Failed to restore switch over string. Please report as a decompilation issue */`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:100`
  `canvas.save();`
- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:551`
  `this.mDecorToolbar.saveHierarchyState(sparseArray);`
- `sources/androidx/appcompat/widget/ActivityChooserView.java:567`
  `ViewCompat.saveAttributeDataForStyleable(this, context, iArr, attributeSet, typedArrayObtainStyledAttributes, i2, 0);`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:89`
  `int iSave = canvas.save();`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:95`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/appcompat/widget/ForwardingListener.java:137`
  `r0.postDelayed(r6, r3)`
- `sources/androidx/appcompat/widget/ForwardingListener.java:147`
  `r0.postDelayed(r6, r3)`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:165`
  `private synchronized boolean addDrawableToCache(@NonNull Context context, long j2, @NonNull Drawable drawable) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:257`
  `public static synchronized ResourceManagerInternal get() {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:266`
  `private synchronized Drawable getCachedDrawable(@NonNull Context context, long j2) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:282`
  `public static synchronized PorterDuffColorFilter getPorterDuffColorFilter(int i2, PorterDuff.Mode mode) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:453`
  `public synchronized Drawable getDrawable(@NonNull Context context, @DrawableRes int i2) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:457`
  `public synchronized void onConfigurationChanged(@NonNull Context context) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:464`
  `public synchronized void setHooks(ResourceManagerHooks resourceManagerHooks) {`
- `sources/androidx/appcompat/widget/SearchView.java:118`
  `private final View mSubmitArea;`
- `sources/androidx/appcompat/widget/SearchView.java:119`
  `private boolean mSubmitButtonEnabled;`
- `sources/androidx/appcompat/widget/SearchView.java:865`
  `Drawable background2 = this.mSubmitArea.getBackground();`
- `sources/androidx/appcompat/widget/SearchView.java:1342`
  `ViewCompat.saveAttributeDataForStyleable(this, context, iArr, attributeSet, tintTypedArrayObtainStyledAttributes.getWrappedTypeArray(), i2, 0);`
- `sources/androidx/appcompat/widget/SearchView.java:1350`
  `View viewFindViewById2 = findViewById(R.id.submit_area);`
- `sources/androidx/appcompat/widget/SearchView.java:1351`
  `this.mSubmitArea = viewFindViewById2;`
- `sources/androidx/appcompat/widget/SwitchCompat.java:607`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/appcompat/widget/TooltipCompatHandler.java:66`
  `this.mAnchor.postDelayed(this.mShowRunnable, ViewConfiguration.getLongPressTimeout());`
- `sources/androidx/appcompat/widget/TooltipCompatHandler.java:158`
  `this.mAnchor.postDelayed(this.mHideRunnable, j3);`
- `sources/androidx/asynclayoutinflater/R.java:1`
  `package androidx.asynclayoutinflater;`
- `sources/androidx/asynclayoutinflater/view/AsyncLayoutInflater.java:1`
  `package androidx.asynclayoutinflater.view;`
- `sources/androidx/asynclayoutinflater/view/AsyncLayoutInflater.java:19`
  `public final class AsyncLayoutInflater {`
- `sources/androidx/asynclayoutinflater/view/AsyncLayoutInflater.java:20`
  `private static final String TAG = "AsyncLayoutInflater";`
- `sources/androidx/asynclayoutinflater/view/AsyncLayoutInflater.java:24`
  `private Handler.Callback mHandlerCallback = new Handler.Callback() { // from class: androidx.asynclayoutinflater.view.AsyncLayoutInflater.1`

## BR095

paper_id: B025
paper_title: Why Eve and Mallory Still Love Android: Revisiting TLS (In)Security in Android Applications

- `resources/com.bupa.digitalprimarycare.apk/res/drawable/$avd_hide_password__0.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/$avd_hide_password__1.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/$avd_hide_password__2.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/$avd_show_password__0.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/$avd_show_password__1.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/$avd_show_password__2.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/$zui_avd_typing_indicator__0.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_ab_back_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_arrow_drop_right_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_clear_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_go_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_menu_copy_mtrl_am_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_menu_cut_mtrl_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_menu_overflow_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_menu_paste_mtrl_am_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_menu_selectall_mtrl_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_menu_share_mtrl_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_ic_voice_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_seekbar_tick_mark_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_star_black_48dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_star_half_black_48dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_text_cursor_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/abc_vector_test.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/avd_hide_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_hide_password__0_res_0x7f080000">`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/avd_show_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_show_password__0_res_0x7f080003">`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/bootsplash_cyrus.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android" android:opacity="opaque">`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/bootsplash_us.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android" android:opacity="opaque">`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/btn_checkbox_checked_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/btn_checkbox_unchecked_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/btn_radio_off_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/btn_radio_on_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/bt_ic_vaulted_visa.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/bt_ic_visa.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/design_ic_visibility.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/design_ic_visibility_off.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/gray_circle.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/ic_checked_box.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/ic_check_circle.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/ic_clock_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/ic_dropdown.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/ic_keyboard_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/ic_launcher_emed_background.xml:3`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/ic_mtrl_checked_circle.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/ic_mtrl_chip_checked_black.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/ic_mtrl_chip_checked_circle.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/ic_mtrl_chip_close_circle.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/ic_radio_button_unchecked.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/ic_uncheck_box.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/material_ic_calendar_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/material_ic_clear_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/material_ic_edit_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/material_ic_keyboard_arrow_left_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/material_ic_keyboard_arrow_right_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/material_ic_menu_arrow_down_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/minus.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/mtrl_ic_arrow_drop_down.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/mtrl_ic_arrow_drop_up.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/mtrl_ic_cancel.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/mtrl_ic_error.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/mtrl_tabs_default_indicator.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/navigation_empty_icon.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/onfido_arrow_forward_white.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/onfido_arrow_right_grey.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/onfido_avc_frame_bottom_left_corner.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/onfido_avc_frame_bottom_rigth_corner.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/onfido_avc_frame_top_left_corner.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/onfido_avc_frame_top_rigth_corner.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/onfido_avc_ic_exclamation.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/onfido_avc_ic_eye.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/onfido_avc_ic_face.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/onfido_avc_ic_mask.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/onfido_avc_ic_sun.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/onfido_avc_ic_tick_green.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/onfido_bg_steps_indicator.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/onfido_check_white.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/onfido_cobrand_logo.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/onfido_driving_licence.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/onfido_error_circle.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/drawable/onfido_error_circle_small.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`

## BR096

paper_id: B011
paper_title: Locking it down: The privacy and security of mobile medication apps

- `resources/com.bupa.digitalprimarycare.apk/res/color/design_box_stroke_color.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/com.bupa.digitalprimarycare.apk/res/color/zui_input_box_hint_color.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/com.bupa.digitalprimarycare.apk/res/layout/design_text_input_end_icon.xml:2`
  `<com.google.android.material.internal.CheckableImageButton xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/layout/design_text_input_start_icon.xml:2`
  `<com.google.android.material.internal.CheckableImageButton xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/layout/material_chip_input_combo.xml:2`
  `<com.google.android.material.timepicker.ChipTextInputComboView xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/layout/material_time_input.xml:2`
  `<com.google.android.material.textfield.TextInputLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto"`
- `resources/com.bupa.digitalprimarycare.apk/res/layout/mtrl_picker_text_input_date.xml:2`
  `<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.bupa.digitalprimarycare.apk/res/layout/zui_view_attachments_indicator.xml:2`
  `<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto"`
- `resources/com.bupa.digitalprimarycare.apk/res/layout/zui_view_input_box.xml:2`
  `<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_en_ca.json:1`
  `{"chat-exp.about_your_results_content":"The possible causes are those that the Babylon algorithm suggests as most likely, given the answers you entered. They are listed in the order of their match to your answers and how common the causes are. The order is not an indication of your individual likeli...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_en_ca__partnertelus.json:1`
  `{"account_details.county":"Province","account_details.phn_why_subtitle":"Your Medical ID (Health card number) may be required to facilitate prescriptions, labs, imaging requisitions and specialist referrals. By entering your Medical ID the cost of your appointment could be covered by your provincial...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_en_gb.json:1`
  `{"chat-exp.about_your_results_content":"The possible causes are those that the Babylon algorithm suggests as most likely, given the answers you entered. They are listed in the order of their match to your answers and how common the causes are. The order is not an indication of your individual likeli...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_en_gb__partnerbupa.json:1`
  `{"appointments.checkin.window":"If you can't attend, please cancel as soon as possible to free your slot for another patient.","appointments.referraldetailfaqurl":"https://www.bupa.co.uk/help-and-support/blua/prescriptions-and-referrals/referrals","global.applicationName":"Bupa Blua Health","global....`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_en_us.json:1`
  `{"chat-exp.about_your_results_content":"The possible causes are those that the Babylon algorithm suggests as most likely, given the answers you entered. They are listed in the order of their match to your answers and how common the causes are. The order is not an indication of your individual likeli...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_es_us.json:1`
  `{"chat-exp.about_your_results_content":"Las posibles causas son afecciones que pueden estar relacionadas con los síntomas y factores de riesgo ingresados por el usuario.\n\nLas afecciones presentadas a un usuario se enumeran en el orden en que las afecciones coinciden con los síntomas y los factores...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_fr_ca.json:1`
  `{"chat-exp.about_your_results_content":"Les causes possibles sont celles que l'algorithme de Babylon considère les plus probables d'après les réponses que vous avez fournies. Elles sont répertoriées dans leur ordre de correspondance avec vos réponses et de leur fréquence. Cependant, cet ordre n'est ...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_app_common_messages_fr_ca__partnertelus.json:1`
  `{"account_details.county":"Province","account_details.phn_why_subtitle":"Votre identifiant médical (numéro de carte d'assurance maladie) peut être requis pour faciliter les ordonnances, les analyses de laboratoire, les demandes d'imagerie et les références aux spécialistes. En saisissant votre ident...`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_package.json:64`
  `"download-gql-schema": "apollo schema:download --endpoint https://services-uk.dev.babylontech.co.uk/consumer-api/graphql/api graphql-schema.json",`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_babyloncyrus_package.json:464`
  `"registry": "https://artifactory.ops.babylontech.co.uk/artifactory/api/npm/babylon-virtual-npm/"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:16`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/--*"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:32`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-accelerator"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:48`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-block-progression"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:64`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-content-zoom-chaining"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:80`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-content-zooming"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:121`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-content-zoom-limit-max"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:137`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-content-zoom-limit-min"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:159`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-content-zoom-snap"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:175`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-content-zoom-snap-points"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:191`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-content-zoom-snap-type"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:207`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-filter"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:223`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-flow-from"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:239`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-flow-into"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:255`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-grid-columns"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:271`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-grid-rows"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:287`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-high-contrast-adjust"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:303`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-hyphenate-limit-chars"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:319`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-hyphenate-limit-lines"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:335`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-hyphenate-limit-zone"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:351`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-ime-align"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:367`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-overflow-style"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:383`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-scrollbar-3dlight-color"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:399`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-scrollbar-arrow-color"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:415`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-scrollbar-base-color"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:431`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-scrollbar-darkshadow-color"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:447`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-scrollbar-face-color"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:463`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-scrollbar-highlight-color"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:479`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-scrollbar-shadow-color"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:495`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-scrollbar-track-color"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:511`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-scroll-chaining"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:553`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-scroll-limit-x-max"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:569`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-scroll-limit-x-min"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:585`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-scroll-limit-y-max"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:601`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-scroll-limit-y-min"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:617`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-scroll-rails"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:633`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-scroll-snap-points-x"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:649`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-scroll-snap-points-y"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:665`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-scroll-snap-type"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:725`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-scroll-translation"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:741`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-text-autospace"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:757`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-touch-select"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:773`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-user-select"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:789`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-wrap-flow"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:805`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-wrap-margin"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:821`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-ms-wrap-through"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:838`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/appearance"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:854`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-moz-binding"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:870`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-moz-border-bottom-colors"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:886`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-moz-border-left-colors"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:902`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-moz-border-right-colors"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:918`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-moz-border-top-colors"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:934`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-moz-context-properties"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:950`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-moz-float-edge"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:966`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-moz-force-broken-image-icon"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:982`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-moz-image-region"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:998`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-moz-orient"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:1050`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-moz-outline-radius-bottomleft"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:1066`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-moz-outline-radius-bottomright"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:1082`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-moz-outline-radius-topleft"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:1098`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-moz-outline-radius-topright"`
- `resources/com.bupa.digitalprimarycare.apk/res/raw/node_modules_mdndata_css_properties.json:1114`
  `"mdn_url": "https://developer.mozilla.org/docs/Web/CSS/-moz-stack-sizing"`

## BR097

paper_id: B019
paper_title: Pulse Oximeter App Privacy Policies During COVID-19: Scoping Assessment

- `sources/com/facebook/react/devsupport/DevServerHelper.java:264`
  `return String.format(Locale.US, "ws://%s/debugger-proxy?role=client", this.mSettings.getPackagerConnectionSettings().getDebugServerHost());`
- `sources/zendesk/chat/ChatVisitorClient.java:17`
  `private static final String BASE_URL = "wss://widget-mediator.zopim.com";`

## BR098

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/com/appsflyer/share/LinkGenerator.java:160`
  `public LinkGenerator setBaseURL(String str, String str2, String str3) {`
- `sources/com/auth0/android/request/DefaultClient.java:75`
  `OkHttpClient.Builder builder = new OkHttpClient.Builder();`
- `sources/com/cardinalcommerce/a/setTextAppearance.java:116`
  `this.init.loadDataWithBaseURL("HTTPS://EMV3DS/challenge", strReplaceAll, "text/html", "UTF-8", null);`
- `sources/com/cardinalcommerce/a/setTextAppearance.java:444`
  `this.init.loadDataWithBaseURL("HTTPS://EMV3DS/challenge/refresh", str2, "text/html", "UTF-8", null);`
- `sources/com/facebook/react/devsupport/PackagerStatusCheck.java:23`
  `OkHttpClient.Builder builder = new OkHttpClient.Builder();`
- `sources/com/onfido/android/sdk/capture/common/di/network/NetworkModule.java:64`
  `OkHttpClient.Builder builder = new OkHttpClient.Builder();`
- `sources/com/onfido/android/sdk/capture/common/di/network/NetworkModule.java:141`
  `OkHttpClient.Builder builderAddInterceptor = okHttpClient.newBuilder().addInterceptor(httpLoggingInterceptor);`
- `sources/com/onfido/android/sdk/capture/common/di/network/NetworkModule.java:143`
  `Retrofit retrofitBuild = new Retrofit.Builder().addCallAdapterFactory(RxJava3CallAdapterFactory.create()).addConverterFactory(GsonConverterFactory.create(new GsonBuilder().setLenient().create())).client(builderAddInterceptor.connectTimeout(5000L, timeUnit).readTimeout(5000L, timeUnit).writeTimeout(5...`
- `sources/com/onfido/api/client/OnfidoFetcher.java:68`
  `OkHttpClient.Builder builderNewBuilder = okHttpClient.newBuilder();`
- `sources/com/onfido/api/client/OnfidoFetcher.java:70`
  `OkHttpClient.Builder builderAddInterceptor = builderNewBuilder.addInterceptor(new AuthTokenInterceptor(tokenProvider)).addInterceptor(new SdkHeadersInterceptor(str2, str3, str4, str5)).addInterceptor(httpLoggingInterceptor);`
- `sources/com/onfido/api/client/OnfidoFetcher.java:91`
  `this.retrofit = new Retrofit.Builder().client(builderNewBuilder.build()).addConverterFactory(buildGsonConverter()).addCallAdapterFactory(RxJava3CallAdapterFactory.create()).baseUrl(makeUrlCompatibleWithRetrofit(str)).build();`
- `sources/com/onfido/api/client/UtilsExtKt.java:15`
  `public static final void moveInterceptorsToTop(@NotNull OkHttpClient.Builder builder, @NotNull List<? extends Interceptor> interceptors) {`
- `sources/io/branch/referral/PrefHelper.java:246`
  `public String getAPIBaseUrl() {`
- `sources/zendesk/chat/BaseModule.java:43`
  `OkHttpClient.Builder builderAddInterceptor = Tls12SocketFactory.enableTls12OnPreLollipop(new OkHttpClient.Builder()).addInterceptor(httpLoggingInterceptor).addInterceptor(userAgentAndClientHeadersInterceptor);`
- `sources/zendesk/chat/BaseModule.java:57`
  `return new Retrofit.Builder().baseUrl(chatConfig.getBaseUrl()).addConverterFactory(GsonConverterFactory.create(gson)).client(okHttpClient).build();`
