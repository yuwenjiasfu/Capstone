# Rule Search Hits

## BR001

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/AndroidManifest.xml:63`
  `<uses-permission android:name="android.permission.READ_PHONE_STATE"/>`
- `resources/AndroidManifest.xml:64`
  `<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>`
- `resources/AndroidManifest.xml:66`
  `<uses-permission android:name="android.permission.INTERNET"/>`
- `resources/AndroidManifest.xml:67`
  `<uses-permission android:name="android.permission.CAMERA"/>`
- `resources/AndroidManifest.xml:73`
  `<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>`
- `resources/AndroidManifest.xml:74`
  `<uses-permission android:name="android.permission.RECORD_AUDIO"/>`
- `resources/AndroidManifest.xml:75`
  `<uses-permission android:name="android.permission.FLASHLIGHT"/>`

## BR002

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/AndroidManifest.xml:50`
  `<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>`
- `resources/AndroidManifest.xml:51`
  `<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>`
- `resources/AndroidManifest.xml:52`
  `<uses-permission`
- `resources/AndroidManifest.xml:118`
  `<uses-permission android:name="com.hihonor.android.launcher.permission.CHANGE_BADGE"/>`
- `resources/AndroidManifest.xml:119`
  `<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION"/>`
- `resources/AndroidManifest.xml:120`
  `<uses-permission android:name="android.permission.GET_TASKS"/>`

## BR003

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/AndroidManifest.xml:52`
  `<uses-permission`
- `resources/AndroidManifest.xml:55`
  `<uses-permission`
- `resources/AndroidManifest.xml:58`
  `<uses-permission android:name="android.permission.BLUETOOTH_CONNECT"/>`
- `resources/AndroidManifest.xml:59`
  `<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS"/>`
- `resources/AndroidManifest.xml:60`
  `<uses-permission`

## BR004

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/AndroidManifest.xml:85`
  `<uses-permission android:name="android.permission.SET_WALLPAPER"/>`
- `resources/AndroidManifest.xml:86`
  `<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>`
- `resources/AndroidManifest.xml:87`
  `<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>`
- `resources/AndroidManifest.xml:88`
  `<uses-permission android:name="android.permission.ACTIVITY_RECOGNITION"/>`
- `resources/AndroidManifest.xml:110`
  `<uses-permission android:name="android.permission.READ_MEDIA_IMAGES"/>`
- `resources/AndroidManifest.xml:111`
  `<uses-permission android:name="android.permission.READ_MEDIA_VIDEO"/>`
- `resources/AndroidManifest.xml:112`
  `<uses-permission android:name="android.permission.READ_MEDIA_VISUAL_USER_SELECTED"/>`

## BR005

paper_id: B021
paper_title: Metadata-Based Privacy Assessment for Mobile mHealth

- `resources/AndroidManifest.xml:102`
  `<uses-permission android:name="com.xs.smartlink.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION"/>`
- `resources/AndroidManifest.xml:103`
  `<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>`

## BR006

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:146`
  `android:usesCleartextTraffic="true"`

## BR009

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/aegon/chrome/net/X509Util.java:11`
  `import android.net.http.X509TrustManagerExtensions;`
- `sources/aegon/chrome/net/X509Util.java:42`
  `import javax.net.ssl.X509TrustManager;`
- `sources/aegon/chrome/net/X509Util.java:56`
  `private static X509TrustManagerImplementation sDefaultTrustManager;`
- `sources/aegon/chrome/net/X509Util.java:63`
  `private static X509TrustManagerImplementation sTestTrustManager;`
- `sources/aegon/chrome/net/X509Util.java:94`
  `public static final class X509TrustManagerIceCreamSandwich implements X509TrustManagerImplementation {`
- `sources/aegon/chrome/net/X509Util.java:95`
  `private final X509TrustManager mTrustManager;`
- `sources/aegon/chrome/net/X509Util.java:97`
  `public X509TrustManagerIceCreamSandwich(X509TrustManager x509TrustManager) {`
- `sources/aegon/chrome/net/X509Util.java:98`
  `this.mTrustManager = x509TrustManager;`
- `sources/aegon/chrome/net/X509Util.java:101`
  `@Override // aegon.chrome.net.X509Util.X509TrustManagerImplementation`
- `sources/aegon/chrome/net/X509Util.java:102`
  `public final List<X509Certificate> checkServerTrusted(X509Certificate[] x509CertificateArr, String str, String str2) throws CertificateException {`
- `sources/aegon/chrome/net/X509Util.java:103`
  `this.mTrustManager.checkServerTrusted(x509CertificateArr, str);`
- `sources/aegon/chrome/net/X509Util.java:108`
  `public interface X509TrustManagerImplementation {`
- `sources/aegon/chrome/net/X509Util.java:109`
  `List<X509Certificate> checkServerTrusted(X509Certificate[] x509CertificateArr, String str, String str2);`
- `sources/aegon/chrome/net/X509Util.java:112`
  `public static final class X509TrustManagerJellyBean implements X509TrustManagerImplementation {`
- `sources/aegon/chrome/net/X509Util.java:113`
  `private final X509TrustManagerExtensions mTrustManagerExtensions;`
- `sources/aegon/chrome/net/X509Util.java:116`
  `public X509TrustManagerJellyBean(X509TrustManager x509TrustManager) {`
- `sources/aegon/chrome/net/X509Util.java:117`
  `this.mTrustManagerExtensions = new X509TrustManagerExtensions(x509TrustManager);`
- `sources/aegon/chrome/net/X509Util.java:120`
  `@Override // aegon.chrome.net.X509Util.X509TrustManagerImplementation`
- `sources/aegon/chrome/net/X509Util.java:122`
  `public final List<X509Certificate> checkServerTrusted(X509Certificate[] x509CertificateArr, String str, String str2) {`
- `sources/aegon/chrome/net/X509Util.java:123`
  `return this.mTrustManagerExtensions.checkServerTrusted(x509CertificateArr, str, str2);`
- `sources/aegon/chrome/net/X509Util.java:152`
  `private static X509TrustManagerImplementation createTrustManager(KeyStore keyStore) throws NoSuchAlgorithmException, KeyStoreException {`
- `sources/aegon/chrome/net/X509Util.java:156`
  `if (trustManager instanceof X509TrustManager) {`
- `sources/aegon/chrome/net/X509Util.java:158`
  `return new X509TrustManagerJellyBean((X509TrustManager) trustManager);`
- `sources/aegon/chrome/net/X509Util.java:304`
  `List<X509Certificate> listCheckServerTrusted;`
- `sources/aegon/chrome/net/X509Util.java:327`
  `X509TrustManagerImplementation x509TrustManagerImplementation = sDefaultTrustManager;`
- `sources/aegon/chrome/net/X509Util.java:328`
  `if (x509TrustManagerImplementation == null) {`
- `sources/aegon/chrome/net/X509Util.java:332`
  `listCheckServerTrusted = x509TrustManagerImplementation.checkServerTrusted(x509CertificateArr, str, str2);`
- `sources/aegon/chrome/net/X509Util.java:335`
  `listCheckServerTrusted = sTestTrustManager.checkServerTrusted(x509CertificateArr, str, str2);`
- `sources/aegon/chrome/net/X509Util.java:341`
  `return new AndroidCertVerifyResult(0, listCheckServerTrusted.size() > 0 ? isKnownRoot(listCheckServerTrusted.get(listCheckServerTrusted.size() - 1)) : false, listCheckServerTrusted);`
- `sources/cn/jiguang/ba/b.java:18`
  `import javax.net.ssl.X509TrustManager;`
- `sources/cn/jiguang/ba/b.java:139`
  `X509TrustManager x509TrustManager = a;`
- `sources/cn/jiguang/ba/b.java:140`
  `if (x509TrustManager != null) {`
- `sources/cn/jiguang/ba/b.java:141`
  `httpRequest.setSslTrustManager(x509TrustManager);`
- `sources/cn/jiguang/net/HttpRequest.java:7`
  `import javax.net.ssl.X509TrustManager;`
- `sources/cn/jiguang/net/HttpRequest.java:24`
  `private X509TrustManager n;`
- `sources/cn/jiguang/net/HttpRequest.java:95`
  `public X509TrustManager getSslTrustManager() {`
- `sources/cn/jiguang/net/HttpRequest.java:193`
  `public void setSslTrustManager(X509TrustManager x509TrustManager) {`
- `sources/cn/jiguang/net/HttpRequest.java:194`
  `this.n = x509TrustManager;`
- `sources/cn/jiguang/net/SSLTrustManager.java:14`
  `import javax.net.ssl.X509TrustManager;`
- `sources/cn/jiguang/net/SSLTrustManager.java:17`
  `public class SSLTrustManager implements X509TrustManager {`
- `sources/cn/jiguang/net/SSLTrustManager.java:18`
  `private X509TrustManager a;`
- `sources/cn/jiguang/net/SSLTrustManager.java:33`
  `if (trustManager instanceof X509TrustManager) {`
- `sources/cn/jiguang/net/SSLTrustManager.java:34`
  `this.a = (X509TrustManager) trustManager;`
- `sources/cn/jiguang/net/SSLTrustManager.java:44`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/cn/jiguang/net/SSLTrustManager.java:45`
  `public void checkClientTrusted(X509Certificate[] x509CertificateArr, String str) {`
- `sources/cn/jiguang/net/SSLTrustManager.java:46`
  `f.c("SSLTrustManager", "checkClientTrusted");`
- `sources/cn/jiguang/net/SSLTrustManager.java:49`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/cn/jiguang/net/SSLTrustManager.java:50`
  `public void checkServerTrusted(X509Certificate[] x509CertificateArr, String str) throws CertificateException {`
- `sources/cn/jiguang/net/SSLTrustManager.java:51`
  `f.c("SSLTrustManager", "checkServerTrusted");`
- `sources/cn/jiguang/net/SSLTrustManager.java:58`
  `StringBuilder sbD0 = a.d0("checkServerTrusted: CertificateExpiredException:");`
- `sources/cn/jiguang/net/SSLTrustManager.java:63`
  `StringBuilder sbD02 = a.d0("checkServerTrusted: CertificateNotYetValidException:");`
- `sources/cn/jiguang/net/SSLTrustManager.java:68`
  `StringBuilder sbD03 = a.d0("checkServerTrusted failed, error");`
- `sources/cn/jiguang/net/SSLTrustManager.java:75`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/com/huawei/hms/framework/network/grs/h/g/a.java:6`
  `import com.huawei.secure.android.common.ssl.SecureX509TrustManager;`
- `sources/com/huawei/hms/framework/network/grs/h/g/a.java:25`
  `return new SecureSSLSocketFactoryNew(new SecureX509TrustManager(context.getAssets().open(GrsApp.getInstance().getBrand(Operators.DIV) + "grs_sp.bks"), ""));`
- `sources/com/huawei/secure/android/common/HiCloudX509TrustManager.java:11`
  `public class HiCloudX509TrustManager extends com.huawei.secure.android.common.ssl.SecureX509TrustManager {`
- `sources/com/huawei/secure/android/common/HiCloudX509TrustManager.java:13`
  `public HiCloudX509TrustManager(InputStream inputStream, String str) throws NoSuchAlgorithmException, IOException, CertificateException, KeyStoreException {`
- `sources/com/huawei/secure/android/common/SecureApacheSSLSocketFactory.java:16`
  `import javax.net.ssl.X509TrustManager;`
- `sources/com/huawei/secure/android/common/SecureApacheSSLSocketFactory.java:64`
  `this.a.init(null, new X509TrustManager[]{new SecureX509TrustManager(this.b)}, null);`
- `sources/com/huawei/secure/android/common/SecureApacheSSLSocketFactory.java:78`
  `this.a.init(null, new X509TrustManager[]{new HiCloudX509TrustManager(inputStream, str)}, null);`
- `sources/com/huawei/secure/android/common/SecureSSLSocketFactory.java:16`
  `import javax.net.ssl.X509TrustManager;`
- `sources/com/huawei/secure/android/common/SecureSSLSocketFactory.java:34`
  `this.a.init(null, new X509TrustManager[]{new SecureX509TrustManager(this.b)}, null);`
- `sources/com/huawei/secure/android/common/SecureSSLSocketFactory.java:93`
  `this.a.init(null, new X509TrustManager[]{new HiCloudX509TrustManager(inputStream, str)}, null);`
- `sources/com/huawei/secure/android/common/SecureX509TrustManager.java:11`
  `public class SecureX509TrustManager extends com.huawei.secure.android.common.ssl.SecureX509TrustManager {`
- `sources/com/huawei/secure/android/common/SecureX509TrustManager.java:13`
  `public SecureX509TrustManager(Context context) throws IllegalAccessException, NoSuchAlgorithmException, IOException, CertificateException, KeyStoreException {`
- `sources/com/huawei/secure/android/common/ssl/c.java:17`
  `import javax.net.ssl.X509TrustManager;`
- `sources/com/huawei/secure/android/common/ssl/c.java:20`
  `public class c implements X509TrustManager {`
- `sources/com/huawei/secure/android/common/ssl/c.java:23`
  `private List<X509TrustManager> b = new ArrayList();`
- `sources/com/huawei/secure/android/common/ssl/c.java:33`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/com/huawei/secure/android/common/ssl/c.java:34`
  `public void checkClientTrusted(X509Certificate[] x509CertificateArr, String str) throws CertificateException {`
- `sources/com/huawei/secure/android/common/ssl/c.java:35`
  `g.c(c, "checkClientTrusted");`
- `sources/com/huawei/secure/android/common/ssl/c.java:37`
  `throw new CertificateException("checkClientTrusted CertificateException");`
- `sources/com/huawei/secure/android/common/ssl/c.java:39`
  `this.b.get(0).checkClientTrusted(x509CertificateArr, str);`
- `sources/com/huawei/secure/android/common/ssl/c.java:42`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/com/huawei/secure/android/common/ssl/c.java:43`
  `public void checkServerTrusted(X509Certificate[] x509CertificateArr, String str) throws CertificateException {`
- `sources/com/huawei/secure/android/common/ssl/c.java:44`
  `g.c(c, "checkServerTrusted");`
- `sources/com/huawei/secure/android/common/ssl/c.java:47`
  `StringBuilder sbE0 = j.a.a.a.a.e0("checkServerTrusted ", i2, " : ");`
- `sources/com/huawei/secure/android/common/ssl/c.java:59`
  `StringBuilder sbD0 = j.a.a.a.a.d0("checkServerTrusted InvalidKeyException: ");`
- `sources/com/huawei/secure/android/common/ssl/c.java:63`
  `StringBuilder sbD02 = j.a.a.a.a.d0("checkServerTrusted NoSuchAlgorithmException: ");`
- `sources/com/huawei/secure/android/common/ssl/c.java:67`
  `StringBuilder sbD03 = j.a.a.a.a.d0("checkServerTrusted NoSuchProviderException: ");`

## BR010

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/com/huawei/secure/android/common/ssl/hostname/BrowserCompatHostnameVerifier.java:11`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/com/huawei/secure/android/common/ssl/hostname/BrowserCompatHostnameVerifier.java:12`
  `public boolean verify(String str, SSLSession sSLSession) {`
- `sources/com/huawei/secure/android/common/ssl/hostname/StrictHostnameVerifier.java:11`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/com/huawei/secure/android/common/ssl/hostname/StrictHostnameVerifier.java:12`
  `public final boolean verify(String str, SSLSession sSLSession) {`
- `sources/com/huawei/secure/android/common/ssl/util/b.java:113`
  `x509Certificate2.verify(x509Certificate.getPublicKey());`
- `sources/com/mobile/auth/x/b.java:259`
  `httpsURLConnection.setHostnameVerifier(new HostnameVerifier() { // from class: com.mobile.auth.x.b.1`
- `sources/com/mobile/auth/x/b.java:260`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/com/mobile/auth/x/b.java:261`
  `public boolean verify(String str3, SSLSession sSLSession) {`
- `sources/com/mobile/auth/x/b.java:263`
  `HostnameVerifier defaultHostnameVerifier = HttpsURLConnection.getDefaultHostnameVerifier();`
- `sources/com/mobile/auth/x/b.java:264`
  `if (defaultHostnameVerifier.verify("wostore.cn", sSLSession)) {`
- `sources/com/mobile/auth/x/b.java:267`
  `return defaultHostnameVerifier.verify("10010.com", sSLSession);`
- `sources/com/umeng/umverify/c/a.java:38`
  `this.a = new HostnameVerifier() { // from class: com.umeng.umverify.c.a.1`
- `sources/com/umeng/umverify/c/a.java:39`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/com/umeng/umverify/c/a.java:40`
  `public final boolean verify(String str3, SSLSession sSLSession) {`
- `sources/com/umeng/umverify/c/a.java:44`
  `return HttpsURLConnection.getDefaultHostnameVerifier().verify("ai.login.umeng.com", sSLSession);`
- `sources/com/umeng/umverify/c/a.java:48`
  `httpsURLConnection2.setHostnameVerifier(this.a);`
- `sources/com/umeng/umverify/utils/d.java:56`
  `httpsURLConnection2.setHostnameVerifier(new HostnameVerifier() { // from class: com.umeng.umverify.utils.d.1`
- `sources/com/umeng/umverify/utils/d.java:57`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/com/umeng/umverify/utils/d.java:58`
  `public final boolean verify(String str2, SSLSession sSLSession) {`
- `sources/com/umeng/umverify/utils/d.java:62`
  `return HttpsURLConnection.getDefaultHostnameVerifier().verify("ai.login.umeng.com", sSLSession);`
- `sources/dc/squareup/okhttp3/internal/connection/RealConnection.java:347`
  `if (this.f4868h == null || route == null || route.b.type() != Proxy.Type.DIRECT || this.c.b.type() != Proxy.Type.DIRECT || !this.c.c.equals(route.c) || route.a.f4809j != OkHostnameVerifier.a || !k(address.a)) {`
- `sources/dc/squareup/okhttp3/internal/connection/RealConnection.java:437`
  `return handshake != null && OkHostnameVerifier.a.c(httpUrl.d, (X509Certificate) handshake.c.get(0));`
- `sources/dc/squareup/okhttp3/internal/tls/BasicCertificateChainCleaner.java:59`
  `x509Certificate.verify(x509Certificate2.getPublicKey());`
- `sources/io/dcloud/common/adapter/util/DCloudTrustManager.java:24`
  `public static X509HostnameVerifier getHostnameVerifier(boolean z) {`
- `sources/io/dcloud/feature/weex/adapter/DCWXHttpAdapter.java:87`
  `public X509HostnameVerifier getHostnameVerifier(boolean z) {`

## BR011

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/dc/squareup/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:27`
  `import java.security.cert.CertificateException;`
- `sources/dc/squareup/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:30`
  `import javax.net.ssl.SSLHandshakeException;`
- `sources/dc/squareup/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:255`
  `if (!(iOException instanceof ProtocolException) && (!(iOException instanceof InterruptedIOException) ? ((iOException instanceof SSLHandshakeException) && (iOException.getCause() instanceof CertificateException)) || (iOException instanceof SSLPeerUnverifiedException) : !((iOException instanceof Socke...`

## BR012

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/dc/squareup/okhttp3/Address.java:41`
  `public final CertificatePinner f4810k;`
- `sources/dc/squareup/okhttp3/Address.java:43`
  `public Address(String str, int i2, Dns dns, SocketFactory socketFactory, @Nullable SSLSocketFactory sSLSocketFactory, @Nullable HostnameVerifier hostnameVerifier, @Nullable CertificatePinner certificatePinner, Authenticator authenticator, @Nullable Proxy proxy, List<Protocol> list, List<ConnectionSp...`
- `sources/dc/squareup/okhttp3/Address.java:80`
  `this.f4810k = certificatePinner;`
- `sources/dc/squareup/okhttp3/Address.java:105`
  `CertificatePinner certificatePinner = this.f4810k;`
- `sources/dc/squareup/okhttp3/Address.java:106`
  `return iHashCode4 + (certificatePinner != null ? certificatePinner.hashCode() : 0);`
- `sources/dc/squareup/okhttp3/CertificatePinner.java:21`
  `public final class CertificatePinner {`
- `sources/dc/squareup/okhttp3/CertificatePinner.java:22`
  `public static final CertificatePinner c = new CertificatePinner(new LinkedHashSet(new Builder().a), null);`
- `sources/dc/squareup/okhttp3/CertificatePinner.java:51`
  `public CertificatePinner(Set<Pin> set, @Nullable CertificateChainCleaner certificateChainCleaner) {`
- `sources/dc/squareup/okhttp3/CertificatePinner.java:60`
  `StringBuilder sbD0 = a.d0("sha256/");`
- `sources/dc/squareup/okhttp3/CertificatePinner.java:111`
  `if (obj instanceof CertificatePinner) {`
- `sources/dc/squareup/okhttp3/CertificatePinner.java:112`
  `CertificatePinner certificatePinner = (CertificatePinner) obj;`
- `sources/dc/squareup/okhttp3/CertificatePinner.java:113`
  `if (Util.l(this.b, certificatePinner.b) && this.a.equals(certificatePinner.a)) {`
- `sources/dc/squareup/okhttp3/OkHttpClient.java:90`
  `public final CertificatePinner p;`
- `sources/dc/squareup/okhttp3/OkHttpClient.java:370`
  `CertificatePinner certificatePinner = builder.p;`
- `sources/dc/squareup/okhttp3/OkHttpClient.java:372`
  `this.p = Util.l(certificatePinner.b, certificateChainCleaner) ? certificatePinner : new CertificatePinner(certificatePinner.a, certificateChainCleaner);`
- `sources/dc/squareup/okhttp3/OkHttpClient.java:434`
  `public CertificatePinner p;`
- `sources/dc/squareup/okhttp3/OkHttpClient.java:461`
  `this.p = CertificatePinner.c;`
- `sources/dc/squareup/okhttp3/internal/connection/RealConnection.java:9`
  `import dc.squareup.okhttp3.CertificatePinner;`
- `sources/dc/squareup/okhttp3/internal/connection/RealConnection.java:316`
  `throw new SSLPeerUnverifiedException("Hostname " + address2.a.d + " not verified:\n    certificate: " + CertificatePinner.b(x509Certificate) + "\n    DN: " + x509Certificate.getSubjectDN().getName() + "\n    subjectAltNames: " + OkHostnameVerifier.a(x509Certificate));`
- `sources/dc/squareup/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:5`
  `import dc.squareup.okhttp3.CertificatePinner;`
- `sources/dc/squareup/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:131`
  `CertificatePinner certificatePinner;`
- `sources/dc/squareup/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:136`
  `certificatePinner = okHttpClient.p;`
- `sources/dc/squareup/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:142`
  `certificatePinner = null;`
- `sources/dc/squareup/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:147`
  `return new Address(str, i2, okHttpClient2.t, okHttpClient2.f4837l, sSLSocketFactory, hostnameVerifier, certificatePinner, okHttpClient2.q, okHttpClient2.b, okHttpClient2.c, okHttpClient2.d, okHttpClient2.f4833h);`

## BR013

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `database/snapshots/P001-usenix-android-application-security.html:304`
  `<param name="movie" value="http://releases.flowplayer.org/swf/flowplayer-3.2.1.swf">`
- `database/snapshots/P002-usenix-supor.html:304`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.nsf.gov" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/nsf_150x60_v2.png" width="150" height="60" alt="" /></a><...`
- `database/snapshots/P002-usenix-supor.html:310`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.symantec.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/symantec_logo_1.png" width="200" height="54" alt="" ...`
- `database/snapshots/P002-usenix-supor.html:322`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://cybersecurity.ieee.org" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/ieee_cybersecurity_150x73.png" width="150" hei...`
- `database/snapshots/P002-usenix-supor.html:328`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.microsoft.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/microsoft_150x60_0.png" width="150" height="60" alt...`
- `database/snapshots/P002-usenix-supor.html:334`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.qualcomm.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/qualcomm_150x22.png" width="150" height="33" alt="" ...`
- `database/snapshots/P002-usenix-supor.html:340`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://sfbay.craigslist.org/about/craigslist_is_hiring" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/craigslist_150x35_1.p...`
- `database/snapshots/P002-usenix-supor.html:346`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.oup.com/us" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/oxford_university_press_150x55.png" width="150" height...`
- `database/snapshots/P002-usenix-supor.html:352`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.infosecnews.org" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/infosecnews_150x38.png" width="150" height="38" a...`
- `database/snapshots/P002-usenix-supor.html:358`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://tci.taborcommunications.com/HPCwireLogo_Usenix" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/hpcwire_150x55_0.png" ...`
- `database/snapshots/P002-usenix-supor.html:364`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.userfriendly.org" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/userfriendly_150x60.png" width="150" height="60"...`
- `database/snapshots/P002-usenix-supor.html:370`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.nostarch.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/nostarch_600x240_0.png" width="200" height="80" alt=...`
- `database/snapshots/P002-usenix-supor.html:376`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.linuxpromagazine.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/linux_pro_150x60.png" width="150" height="60...`
- `database/snapshots/P002-usenix-supor.html:382`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.linuxjournal.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/linux_journal_150x72_2.png" width="150" height="...`
- `database/snapshots/P002-usenix-supor.html:388`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.virusbulletin.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/virus_bulletin_150x60.png" width="150" height="...`
- `database/snapshots/P002-usenix-supor.html:394`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.crcpress.com/" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/crc_press_150x60.png" width="150" height="60" alt="...`
- `database/snapshots/P002-usenix-supor.html:400`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://queue.acm.org" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/acmqueue_150x48_3.png" width="150" height="48" alt="" /...`
- `database/snapshots/P002-usenix-supor.html:406`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.admin-magazine.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/admin_150x60.png" width="150" height="60" alt=...`
- `database/snapshots/P002-usenix-supor.html:412`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.dmtf.org" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/dmtf_600x240.png" width="200" height="80" alt="" /></a><...`
- `database/snapshots/P002-usenix-supor.html:663`
  `<a href="http://www.nsf.gov" target="_blank"></a>`
- `database/snapshots/P002-usenix-supor.html:664`
  `<a href="http://www.nsf.gov" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_interest_color/public/sponsor_images/nsf_150x60_v2.png" width="115" height="46" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:667`
  `<a href="http://www.symantec.com" target="_blank"></a>`
- `database/snapshots/P002-usenix-supor.html:668`
  `<a href="http://www.symantec.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_interest_color/public/sponsor_images/symantec_logo_1.png" width="115" height="31" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:705`
  `<a href="http://cybersecurity.ieee.org" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_interest_color/public/sponsor_images/ieee_cybersecurity_150x73.png" width="115" height="56" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:708`
  `<a href="http://www.microsoft.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_interest_color/public/sponsor_images/microsoft_150x60_0.png" width="115" height="46" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:742`
  `<a href="http://sfbay.craigslist.org/about/craigslist_is_hiring" target="_blank"></a>`
- `database/snapshots/P002-usenix-supor.html:743`
  `<a href="http://sfbay.craigslist.org/about/craigslist_is_hiring" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_interest_color/public/sponsor_images/craigslist_150x35_1.png" width="115" height="27" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:746`
  `<a href="http://www.qualcomm.com" target="_blank"></a>`
- `database/snapshots/P002-usenix-supor.html:747`
  `<a href="http://www.qualcomm.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_interest_color/public/sponsor_images/qualcomm_150x22.png" width="115" height="25" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:781`
  `<a href="http://www.oup.com/us" target="_blank"></a>`
- `database/snapshots/P002-usenix-supor.html:782`
  `<a href="http://www.oup.com/us" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_interest_color/public/sponsor_images/oxford_university_press_150x55.png" width="115" height="42" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:816`
  `<a href="http://queue.acm.org"></a>`
- `database/snapshots/P002-usenix-supor.html:817`
  `<a href="http://queue.acm.org" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_front_color/public/sponsor_images/acmqueue_150x48_3.png" width="90" height="29" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:820`
  `<a href="http://www.admin-magazine.com"></a>`
- `database/snapshots/P002-usenix-supor.html:821`
  `<a href="http://www.admin-magazine.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_front_color/public/sponsor_images/admin_150x60.png" width="90" height="36" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:824`
  `<a href="http://www.crcpress.com/"></a>`
- `database/snapshots/P002-usenix-supor.html:825`
  `<a href="http://www.crcpress.com/" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_front_color/public/sponsor_images/crc_press_150x60.png" width="90" height="36" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:828`
  `<a href="http://www.dmtf.org"></a>`
- `database/snapshots/P002-usenix-supor.html:829`
  `<a href="http://www.dmtf.org" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_front_color/public/sponsor_images/dmtf_600x240.png" width="90" height="36" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:836`
  `<a href="http://tci.taborcommunications.com/HPCwireLogo_Usenix"></a>`

## BR014

paper_id: B022
paper_title: A Study of Android Application Security

- `sources/aegon/chrome/net/AndroidCellularSignalStrength.java:13`
  `import android.telephony.TelephonyManager;`
- `sources/aegon/chrome/net/AndroidCellularSignalStrength.java:23`
  `private final TelephonyManager mTelephonyManager;`
- `sources/aegon/chrome/net/AndroidCellularSignalStrength.java:27`
  `TelephonyManager telephonyManager = (TelephonyManager) ContextUtils.getApplicationContext().getSystemService("phone");`
- `sources/aegon/chrome/net/AndroidCellularSignalStrength.java:28`
  `this.mTelephonyManager = telephonyManager;`
- `sources/aegon/chrome/net/AndroidCellularSignalStrength.java:29`
  `if (telephonyManager.getSimState() != 5) {`
- `sources/aegon/chrome/net/AndroidCellularSignalStrength.java:37`
  `this.mTelephonyManager.listen(this, 256);`
- `sources/aegon/chrome/net/AndroidCellularSignalStrength.java:42`
  `this.mTelephonyManager.listen(this, 0);`
- `sources/aegon/chrome/net/AndroidNetworkLibrary.java:270`
  `return AndroidTelephonyManagerBridge.getInstance().getNetworkCountryIso();`
- `sources/aegon/chrome/net/AndroidNetworkLibrary.java:275`
  `return AndroidTelephonyManagerBridge.getInstance().getNetworkOperator();`
- `sources/aegon/chrome/net/AndroidNetworkLibrary.java:287`
  `return AndroidTelephonyManagerBridge.getInstance().getSimOperator();`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge$$Lambda$1.java:4`
  `public final /* synthetic */ class AndroidTelephonyManagerBridge$$Lambda$1 implements Runnable {`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge$$Lambda$1.java:5`
  `private final AndroidTelephonyManagerBridge arg$1;`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge$$Lambda$1.java:7`
  `private AndroidTelephonyManagerBridge$$Lambda$1(AndroidTelephonyManagerBridge androidTelephonyManagerBridge) {`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge$$Lambda$1.java:8`
  `this.arg$1 = androidTelephonyManagerBridge;`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge$$Lambda$1.java:11`
  `public static Runnable lambdaFactory$(AndroidTelephonyManagerBridge androidTelephonyManagerBridge) {`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge$$Lambda$1.java:12`
  `return new AndroidTelephonyManagerBridge$$Lambda$1(androidTelephonyManagerBridge);`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge$$Lambda$1.java:17`
  `AndroidTelephonyManagerBridge.lambda$create$0(this.arg$1);`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:8`
  `import android.telephony.TelephonyManager;`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:16`
  `public class AndroidTelephonyManagerBridge {`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:17`
  `private static volatile AndroidTelephonyManagerBridge sInstance;`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:42`
  `AndroidTelephonyManagerBridge.this.update(AndroidTelephonyManagerBridge.getTelephonyManager());`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:47`
  `private AndroidTelephonyManagerBridge() {`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:50`
  `private static AndroidTelephonyManagerBridge create() {`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:51`
  `AndroidTelephonyManagerBridge androidTelephonyManagerBridge = new AndroidTelephonyManagerBridge();`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:52`
  `ThreadUtils.runOnUiThread(AndroidTelephonyManagerBridge$$Lambda$1.lambdaFactory$(androidTelephonyManagerBridge));`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:53`
  `return androidTelephonyManagerBridge;`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:56`
  `public static AndroidTelephonyManagerBridge getInstance() {`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:57`
  `AndroidTelephonyManagerBridge androidTelephonyManagerBridgeCreate = sInstance;`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:58`
  `if (androidTelephonyManagerBridgeCreate == null) {`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:59`
  `synchronized (AndroidTelephonyManagerBridge.class) {`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:60`
  `androidTelephonyManagerBridgeCreate = sInstance;`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:61`
  `if (androidTelephonyManagerBridgeCreate == null) {`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:62`
  `androidTelephonyManagerBridgeCreate = create();`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:63`
  `sInstance = androidTelephonyManagerBridgeCreate;`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:67`
  `return androidTelephonyManagerBridgeCreate;`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:72`
  `public static TelephonyManager getTelephonyManager() {`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:73`
  `return (TelephonyManager) ContextUtils.getApplicationContext().getSystemService("phone");`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:76`
  `public static /* synthetic */ void lambda$create$0(AndroidTelephonyManagerBridge androidTelephonyManagerBridge) {`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:77`
  `TelephonyManager telephonyManager = getTelephonyManager();`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:78`
  `if (telephonyManager != null) {`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:79`
  `androidTelephonyManagerBridge.listenTelephonyServiceState(telephonyManager);`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:84`
  `private void listenTelephonyServiceState(TelephonyManager telephonyManager) {`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:88`
  `telephonyManager.listen(listener, 1);`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:92`
  `public void update(@CheckForNull TelephonyManager telephonyManager) {`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:93`
  `if (telephonyManager == null) {`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:96`
  `this.mNetworkCountryIso = telephonyManager.getNetworkCountryIso();`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:97`
  `this.mNetworkOperator = telephonyManager.getNetworkOperator();`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:98`
  `this.mSimOperator = telephonyManager.getSimOperator();`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:103`
  `TelephonyManager telephonyManager = getTelephonyManager();`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:104`
  `if (telephonyManager == null) {`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:107`
  `this.mNetworkCountryIso = telephonyManager.getNetworkCountryIso();`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:114`
  `TelephonyManager telephonyManager = getTelephonyManager();`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:115`
  `if (telephonyManager == null) {`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:118`
  `this.mNetworkOperator = telephonyManager.getNetworkOperator();`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:125`
  `TelephonyManager telephonyManager = getTelephonyManager();`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:126`
  `if (telephonyManager == null) {`
- `sources/aegon/chrome/net/AndroidTelephonyManagerBridge.java:129`
  `this.mSimOperator = telephonyManager.getSimOperator();`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2284`
  `boolean z2 = KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1;`
- `sources/androidx/appcompat/app/ToolbarActionBar.java:310`
  `menuB.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);`
- `sources/androidx/appcompat/app/WindowDecorActionBar.java:886`
  `menu.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);`
- `sources/androidx/core/content/ContextCompat.java:59`
  `import android.telephony.TelephonyManager;`
- `sources/androidx/core/content/ContextCompat.java:272`
  `map.put(TelephonyManager.class, "phone");`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:5`
  `import android.telephony.TelephonyManager;`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:16`
  `public class TelephonyManagerCompat {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:25`
  `public static String a(TelephonyManager telephonyManager, int i2) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:26`
  `return telephonyManager.getDeviceId(i2);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:36`
  `public static String a(TelephonyManager telephonyManager) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:37`
  `return telephonyManager.getImei();`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:44`
  `public static int a(TelephonyManager telephonyManager) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:45`
  `return telephonyManager.getSubscriptionId();`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:52`
  `public static String getImei(@NonNull TelephonyManager telephonyManager) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:54`
  `return Api26Impl.a(telephonyManager);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:56`
  `int subscriptionId = getSubscriptionId(telephonyManager);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:57`
  `return (subscriptionId == Integer.MAX_VALUE || subscriptionId == -1) ? telephonyManager.getDeviceId() : Api23Impl.a(telephonyManager, SubscriptionManagerCompat.getSlotIndex(subscriptionId));`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:61`
  `public static int getSubscriptionId(@NonNull TelephonyManager telephonyManager) {`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:63`
  `return Api30Impl.a(telephonyManager);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:67`
  `Method declaredMethod = TelephonyManager.class.getDeclaredMethod("getSubId", new Class[0]);`
- `sources/androidx/core/telephony/TelephonyManagerCompat.java:71`
  `Integer num = (Integer) a.invoke(telephonyManager, new Object[0]);`
- `sources/cn/jiguang/ag/b.java:28`
  `import android.telephony.TelephonyManager;`
- `sources/cn/jiguang/ag/b.java:40`
  `private final TelephonyManager b;`

## BR015

paper_id: B022
paper_title: A Study of Android Application Security

- `sources/aegon/chrome/base/BuildInfo.java:42`
  `strArr[0] = Build.BRAND;`
- `sources/aegon/chrome/base/BuildInfo.java:43`
  `strArr[1] = Build.DEVICE;`
- `sources/aegon/chrome/base/BuildInfo.java:45`
  `strArr[3] = Build.MANUFACTURER;`
- `sources/aegon/chrome/base/BuildInfo.java:46`
  `strArr[4] = Build.MODEL;`
- `sources/androidx/camera/camera2/internal/compat/quirk/DeviceQuirks.java:42`
  `String str2 = Build.MANUFACTURER;`
- `sources/androidx/camera/camera2/internal/compat/quirk/DeviceQuirks.java:43`
  `if ("Google".equals(str2) && PreviewPixelHDRnetQuirk.a.contains(Build.DEVICE.toLowerCase(Locale.getDefault()))) {`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:18`
  `return "HUAWEI".equalsIgnoreCase(Build.BRAND) && "HWANE".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:22`
  `return "OnePlus".equalsIgnoreCase(Build.BRAND) && "OnePlus6".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:26`
  `return "OnePlus".equalsIgnoreCase(Build.BRAND) && "OnePlus6T".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExtraSupportedSurfaceCombinationsQuirk.java:44`
  `String str = Build.DEVICE;`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExtraSupportedSurfaceCombinationsQuirk.java:49`
  `if (!"samsung".equalsIgnoreCase(Build.BRAND)) {`
- `sources/androidx/camera/core/impl/CameraValidator.java:40`
  `sbD0.append(Build.DEVICE);`
- `sources/androidx/camera/core/impl/DeviceProperties.java:14`
  `return create(Build.MANUFACTURER, Build.MODEL, Build.VERSION.SDK_INT);`
- `sources/androidx/camera/core/impl/utils/ExifData.java:498`
  `return new Builder(ByteOrder.BIG_ENDIAN).setAttribute("Orientation", String.valueOf(1)).setAttribute("XResolution", "72/1").setAttribute("YResolution", "72/1").setAttribute("ResolutionUnit", String.valueOf(2)).setAttribute("YCbCrPositioning", String.valueOf(1)).setAttribute("Make", Build.MANUFACTURE...`
- `sources/androidx/camera/extensions/internal/compat/quirk/ExtensionDisabledQuirk.java:11`
  `return "google".equalsIgnoreCase(Build.BRAND) && "redfin".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/video/internal/compat/quirk/DeviceQuirks.java:47`
  `java.lang.String r2 = android.os.Build.BRAND`
- `sources/androidx/camera/video/internal/compat/quirk/MediaCodecInfoReportIncorrectInfoQuirk.java:13`
  `return "Huawei".equalsIgnoreCase(Build.BRAND) && "mha-l29".equalsIgnoreCase(Build.MODEL);`
- `sources/androidx/camera/video/internal/compat/quirk/MediaCodecInfoReportIncorrectInfoQuirk.java:17`
  `return "motorola".equalsIgnoreCase(Build.BRAND) && "moto c".equalsIgnoreCase(Build.MODEL);`
- `sources/androidx/camera/view/internal/compat/quirk/DeviceQuirks.java:22`
  `java.lang.String r2 = android.os.Build.MANUFACTURER`
- `sources/androidx/camera/view/internal/compat/quirk/DeviceQuirks.java:28`
  `java.lang.String r3 = android.os.Build.DEVICE`
- `sources/cn/jiguang/bk/a.java:95`
  `this.e = a(Build.DEVICE);`
- `sources/com/alibaba/fastjson/JSON.java:61`
  `public static TimeZone defaultTimeZone = TimeZone.getDefault();`
- `sources/com/alibaba/fastjson/JSON.java:62`
  `public static Locale defaultLocale = Locale.getDefault();`
- `sources/com/alibaba/fastjson/serializer/JodaCodec.java:59`
  `public static final DateTimeFormatter t = DateTimeFormat.forPattern("yyyy-MM-dd HH:mm:ss").withZone(DateTimeZone.getDefault());`
- `sources/com/alibaba/fastjson/serializer/JodaCodec.java:167`
  `timeZone = TimeZone.getDefault();`
- `sources/com/efs/sdk/base/core/controller/ControllerCenter.java:161`
  `bVar.a.a("lang", Locale.getDefault().getLanguage());`
- `sources/com/efs/sdk/base/core/controller/ControllerCenter.java:162`
  `bVar.a.a("tzone", TimeZone.getDefault().getID());`
- `sources/com/facebook/imagepipeline/producers/HttpUrlConnectionNetworkFetcher.java:107`
  `throw new IOException(i2 == 0 ? String.format(Locale.getDefault(), "URL %s follows too many redirects", uri.toString()) : String.format(Locale.getDefault(), "URL %s returned %d without a valid redirect", uri.toString(), Integer.valueOf(responseCode)));`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:95`
  `builderJ.c().put("model", Build.MODEL);`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:97`
  `builderJ.c().put("device", Build.DEVICE);`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:98`
  `builderJ.c().put("product", Build.PRODUCT);`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:100`
  `builderJ.c().put("manufacturer", Build.MANUFACTURER);`
- `sources/com/google/android/datatransport/cct/CctTransportBackend.java:103`
  `builderJ.c().put("tz-offset", String.valueOf(TimeZone.getDefault().getOffset(Calendar.getInstance().getTimeInMillis()) / 1000));`
- `sources/com/google/android/material/datepicker/DaysOfWeekAdapter.java:76`
  `textView.setContentDescription(String.format(viewGroup.getContext().getString(R.string.mtrl_picker_day_of_week_column_header), this.a.getDisplayName(7, 2, Locale.getDefault())));`
- `sources/com/google/android/material/datepicker/RangeDateSelector.java:131`
  `pairCreate = calendarI.get(1) == calendarI2.get(1) ? calendarI.get(1) == calendarH.get(1) ? Pair.create(DateStrings.c(l2.longValue(), Locale.getDefault()), DateStrings.c(l3.longValue(), Locale.getDefault())) : Pair.create(DateStrings.c(l2.longValue(), Locale.getDefault()), DateStrings.d(l3.longValue...`
- `sources/com/google/android/material/datepicker/SingleDateSelector.java:63`
  `return l2 == null ? resources.getString(R.string.mtrl_picker_date_header_unselected) : resources.getString(R.string.mtrl_picker_date_header_selected, DateStrings.d(l2.longValue(), Locale.getDefault()));`
- `sources/com/google/firebase/FirebaseCommonRegistrar.java:59`
  `arrayList.add(LibraryVersionComponent.create(DEVICE_NAME, safeValue(Build.PRODUCT)));`
- `sources/com/google/firebase/FirebaseCommonRegistrar.java:60`
  `arrayList.add(LibraryVersionComponent.create(DEVICE_MODEL, safeValue(Build.DEVICE)));`
- `sources/com/google/firebase/FirebaseCommonRegistrar.java:61`
  `arrayList.add(LibraryVersionComponent.create(DEVICE_BRAND, safeValue(Build.BRAND)));`
- `sources/com/huawei/appgallery/serviceverifykit/d/c.java:33`
  `int iIndexOf = str.toUpperCase(Locale.getDefault()).indexOf(str2 + ContainerUtils.KEY_VALUE_DELIMITER);`
- `sources/com/huawei/hms/hatool/u0.java:54`
  `map.put("Device-Type", Build.MODEL);`
- `sources/com/huawei/hms/hatool/y0.java:20`
  `jSONObject.put("_model", Build.MODEL);`
- `sources/com/huawei/hms/hihealth/data/DeviceInfo.java:183`
  `String str = Build.MANUFACTURER;`
- `sources/com/huawei/hms/hihealth/data/DeviceInfo.java:184`
  `String str2 = Build.MODEL;`
- `sources/com/huawei/hms/hihealth/data/DeviceInfo.java:189`
  `sbAab.append(Build.BRAND.length() % 10);`
- `sources/com/huawei/hms/opendevice/n.java:78`
  `jSONObject2.put(bg.M, TimeZone.getDefault().getID());`
- `sources/com/kuaishou/weapon/p0/ad.java:38`
  `if ("nokia".equalsIgnoreCase(Build.MANUFACTURER) && ("Nokia_N1".equalsIgnoreCase(Build.DEVICE) || "N1".equalsIgnoreCase(Build.MODEL))) {`
- `sources/com/kuaishou/weapon/p0/bl.java:196`
  `String str = Build.DEVICE;`
- `sources/com/kwad/components/core/webview/tachikoma/i.java:455`
  `adHttpFormDataBuilder.addFormDataPart("os_build_model", Build.MODEL);`
- `sources/com/kwad/components/core/webview/tachikoma/i.java:457`
  `adHttpFormDataBuilder.addFormDataPart("os_build_brand", Build.BRAND);`
- `sources/com/kwad/sdk/utils/bl.java:151`
  `return Build.MODEL;`
- `sources/com/kwad/sdk/utils/bl.java:181`
  `return Build.BRAND;`
- `sources/com/kwad/sdk/utils/bl.java:214`
  `return Build.MANUFACTURER;`
- `sources/com/kwad/sdk/utils/o.java:40`
  `String str3 = Build.BRAND;`
- `sources/com/kwad/sdk/utils/o.java:44`
  `String str4 = Build.DEVICE;`
- `sources/com/kwad/sdk/utils/o.java:48`
  `String str5 = Build.MODEL;`
- `sources/com/mobile/auth/gatewayauth/manager/d.java:157`
  `String str2 = String.format(Locale.getDefault(), "%s [%s] [%s] :%s", new SimpleDateFormat("yy-MM-dd HH:mm:ss.SSS").format(new Date()), a(i2), Thread.currentThread().toString(), str);`
- `sources/com/mobile/auth/gatewayauth/utils/d.java:16`
  `return Build.BRAND;`
- `sources/com/mobile/auth/y/d.java:24`
  `jSONObject.put(Constants.PHONE_BRAND, Build.BRAND);`
- `sources/com/mobile/auth/y/d.java:25`
  `jSONObject.put("model", Build.MODEL);`
- `sources/com/nirvana/tools/core/AppUtils.java:55`
  `return Build.BRAND + Constants.COLON_SEPARATOR + Build.MODEL;`
- `sources/com/nirvana/tools/core/AppUtils.java:59`
  `String str = Build.MODEL;`
- `sources/com/nirvana/tools/crash/CrashUcSdk.java:235`
  `sb.append(Build.MODEL);`
- `sources/com/nirvana/tools/crash/FileUtils.java:100`
  `sb.append(Build.MODEL);`
- `sources/com/ss/bluetooth/blecore/scans/DeviceClassifier.java:39`
  `String lowerCase = Build.MANUFACTURER.toLowerCase();`
- `sources/com/ss/bluetooth/blecore/scans/DeviceClassifier.java:40`
  `String str = Build.MODEL;`
- `sources/com/ss/bluetooth/blecore/scans/DeviceClassifier.java:42`
  `Log.i(TAG, "getDeviceGrade: model:" + str.toLowerCase(locale) + "  brand:" + Build.BRAND.toLowerCase(locale));`
- `sources/com/ss/bluetooth/blecore/scans/DeviceClassifier.java:51`
  `String str = Build.MODEL;`
- `sources/com/ss/bluetooth/blecore/scans/DeviceClassifier.java:54`
  `String lowerCase2 = Build.BRAND.toLowerCase(locale);`
- `sources/com/taobao/weex/utils/WXDeviceUtils.java:16`
  `return "samsung".equalsIgnoreCase(Build.BRAND) && "SM-F9000".equalsIgnoreCase(Build.MODEL);`
- `sources/com/taobao/weex/utils/WXDeviceUtils.java:20`
  `if ("HUAWEI".equalsIgnoreCase(Build.BRAND)) {`
- `sources/com/taobao/weex/utils/WXDeviceUtils.java:21`
  `String str = Build.DEVICE;`
- `sources/com/umeng/analytics/pro/ak.java:37`
  `ajVar.g(Build.BRAND);`
- `sources/com/umeng/analytics/pro/ak.java:38`
  `ajVar.h(Build.MODEL);`
- `sources/com/umeng/analytics/pro/ak.java:155`
  `jSONObject.put("model", Build.MODEL);`
- `sources/com/umeng/analytics/pro/aw.java:15`
  `String str = Build.BRAND;`
- `sources/com/umeng/analytics/pro/o.java:373`
  `String str2 = new SimpleDateFormat("yyyy-MM-dd", Locale.getDefault()).format(new Date(System.currentTimeMillis()));`
- `sources/com/umeng/analytics/process/UMProcessDBDatasSender.java:202`
  `jSONObject.put(d.f4413m, sharedPreferences.getString("vers_date", new SimpleDateFormat("yyyy-MM-dd", Locale.getDefault()).format(new Date(System.currentTimeMillis()))));`
- `sources/com/umeng/cconfig/b/e.java:103`
  `bVar.t = Build.BRAND;`
- `sources/com/umeng/cconfig/b/e.java:104`
  `bVar.u = Build.MODEL;`

## BR016

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `database_beginner/snapshots/B010-client-focused-mhealth-security.html:1451`
  `<p>The authorization header field can contain one of multiple possible values of interest. It may leak usernames and passwords [<a href="#ref52" class="usa-link" aria-describedby="ref52">52</a>], OAuth2 Bearer tokens [<a href="#ref53" class="usa-link" aria-describedby="ref53">53</a>], or other sensi...`
- `resources/AndroidManifest.xml:226`
  `android:name="dcloud_appkey"`
- `resources/AndroidManifest.xml:229`
  `android:name="UMENG_APPKEY"`
- `resources/AndroidManifest.xml:924`
  `android:name="JPUSH_APPKEY"`
- `resources/AndroidManifest.xml:1013`
  `android:name="com.vivo.push.api_key"`
- `resources/AndroidManifest.xml:1022`
  `android:name="XIAOMI_APPKEY"`
- `resources/assets/apps/__UNI__2574FEC/www/app-service.js:57`
  `*/var painterCtors={},instances$1={};function delInstance(e){delete instances$1[e]}function isDarkMode(e){if(!e)return!1;if("string"==typeof e)return lum(e,1)<DARK_MODE_THRESHOLD;if(e.colorStops){for(var t=e.colorStops,a=0,n=t.length,o=0;o<n;o++)a+=lum(t[o].color,1);return(a/=n)<DARK_MODE_THRESHOLD}...`
- `resources/io/dcloud/all.js:1`
  `if(!window.plus||window.plus&&!window.plus.isReady){var plusType=typeof window.plus;"function"==plusType||"object"==plusType?(window.plus.isReady=!0,navigator.plus=window.__html5plus__=window.plus):window.__html5plus__=window.plus=navigator.plus={isReady:!0}}!function(e){var t=e.tools={__UUID__:0,UN...`
- `resources/io/dcloud/weexUniJs.js:1`
  `var PlusObject=function(plusContext,param){plusContext.__param__=param;var dc_plusobjects={},dc_plusMouldes={};function PlusObject(e,t){for(var n in this.weex=t,this.weex_instance_id=e,this.__HtMl_Id__,this.__io__dc_vue_call_exec_sync="undefined"!=typeof global&&global.__io__dc_vue_call_exec_sync,th...`
- `resources/res/values/strings.xml:360`
  `<string name="dcloud_offline_fail_tips">Appkey is not configured or configured incorrectly</string>`
- `resources/res/values-zh/strings.xml:227`
  `<string name="dcloud_offline_fail_tips">未配置appkey或配置错误</string>`
- `sources/cn/jiguang/ai/f.java:274`
  `httpRequest.setRequestProperty("X-Http-Appkey", strA);`
- `sources/cn/jiguang/an/a.java:193`
  `httpRequest.setRequestProperty("X-Http-Appkey", jSONObject.optString("appkey"));`
- `sources/cn/jiguang/android/BuildConfig.java:7`
  `public static final String CUSTOM_APP_KEY = "";`
- `sources/cn/jiguang/ax/a.java:214`
  `cn.jiguang.ay.f.n("CheckManifestHelper", "errorcode:10001,metadata: JCore appKey - not defined in manifest");`
- `sources/cn/jiguang/ax/a.java:215`
  `cn.jiguang.bv.a.a(context, " 未在manifest中配置AppKey", -1);`
- `sources/cn/jiguang/ax/a.java:221`
  `cn.jiguang.ay.f.n("CheckManifestHelper", "errorcode:1008,Invalid appKey : " + strA + ", Please get your Appkey from JIGUANG web console!");`
- `sources/cn/jiguang/ax/a.java:222`
  `cn.jiguang.bv.a.a(context, " AppKey:" + strA + " 是无效的AppKey,请确认与JIGUANG web端的AppKey一致", -1);`
- `sources/cn/jiguang/ax/h.java:47`
  `cn.jiguang.ay.f.i("JSDKBannedHelper", "request bannedConfig failed because can't get appKey");`
- `sources/cn/jiguang/ax/i.java:41`
  `cn.jiguang.ay.f.i("JSDKDeveloperIdLimitHelper", "request bannedConfig failed because can't get appKey");`
- `sources/cn/jiguang/ax/i.java:53`
  `jSONObject.put("appkey", strA);`
- `sources/cn/jiguang/ax/j.java:97`
  `cn.jiguang.ay.f.i("JSslCertUpdateManager", "appKey is empty, return");`
- `sources/cn/jiguang/ax/j.java:105`
  `jSONObject.put("appkey", strA);`
- `sources/cn/jiguang/ay/b.java:119`
  `httpRequest.setRequestProperty("X-Http-Appkey", strA);`
- `sources/cn/jiguang/bd/c.java:77`
  `cn.jiguang.ay.f.h("ConnectingHelper", "Login with - juid:" + jF + ", appKey:" + strE + ", sdkVersion:" + strF + ", pluginPlatformType:" + ((int) b2));`
- `sources/cn/jiguang/bd/c.java:243`
  `sbD0 = j.a.a.a.a.i0(" AppKey:", strE);`
- `sources/cn/jiguang/bd/c.java:248`
  `str = " 非android AppKey";`
- `sources/cn/jiguang/bl/i.java:221`
  `cn.jiguang.ay.f.i("SentryEntryHelper", "request sentry sample failed because can't get appKey");`
- `sources/cn/jiguang/bv/a.java:447`
  `Notification.Builder when = new Notification.Builder(context.getApplicationContext()).setContentTitle("Jiguang提示：包名和AppKey不匹配").setContentText("请到 Portal 上获取您的包名和AppKey并更新AndroidManifest相应字段").setContentIntent(broadcast).setSmallIcon(i3).setTicker(str).setWhen(jCurrentTimeMillis);`
- `sources/cn/jiguang/e/a.java:255`
  `return new a<>(a, "device_config_appkey_n", "");`
- `sources/cn/jiguang/e/a.java:259`
  `return new a<>(a, "device_config_appkey", "");`
- `sources/cn/jiguang/i/e.java:309`
  `f.i("JActFolderConfManager", "request folder data config failed because can't get appKey");`
- `sources/cn/jiguang/internal/JConstants.java:15`
  `public static String APP_KEY = "";`
- `sources/cn/jiguang/n/c.java:166`
  `f.i("JDataConfigManager", "request data config failed because can't get appKey");`
- `sources/cn/jpush/android/ac/c.java:406`
  `Logger.dd("ThirdPushManager", "[refreshToken] third disabled");`
- `sources/cn/jpush/android/ac/c.java:412`
  `Logger.w("ThirdPushManager", "refreshToken romtype is <= 0");`
- `sources/cn/jpush/android/ac/c.java:415`
  `Logger.dd("ThirdPushManager", "[refreshToken] romType: " + ((int) bByteValue));`
- `sources/cn/jpush/android/api/JPushInterface.java:47`
  `public static final String EXTRA_APP_KEY = "cn.jpush.android.APPKEY";`
- `sources/cn/jpush/android/api/JThirdPlatFormInterface.java:37`
  `public static final String KEY_VENDOR_PUSH_APP_KEY_MISS = "j10000";`
- `sources/cn/jpush/android/h/a.java:42`
  `jSONObject.put("JPUSH_APPKEY", str);`
- `sources/cn/jpush/android/helper/a.java:222`
  `intent.putExtra(JPushInterface.EXTRA_APP_KEY, customMessage.senderId);`
- `sources/cn/jpush/android/l/a.java:620`
  `cn.jpush.android.d.b.a(context2, 2, string6, string4, TextUtils.isEmpty(string5) ? JCoreHelper.getAppKey(context2) : string5, 0L, b);`
- `sources/cn/jpush/android/thirdpush/fcm/a.java:29`
  `public static String b = "fcm_appkey";`
- `sources/cn/jpush/android/thirdpush/vivo/a.java:208`
  `c = bundle.getString("com.vivo.push.api_key");`
- `sources/cn/jpush/android/thirdpush/vivo/a.java:212`
  `Logger.w("VivoPushHelper", "metadata: com.vivo.push.api_key - not defined in manifest");`
- `sources/cn/jpush/android/x/b.java:1123`
  `intent.putExtra(CommonConstant.ReqAccessTokenParam.PACKAGE_NAME, context.getPackageName());`
- `sources/com/google/android/gms/auth/api/signin/GoogleSignInOptions.java:86`
  `@SafeParcelable.Field(getter = "isForceCodeForRefreshToken", id = 6)`
- `sources/com/google/android/gms/auth/api/signin/GoogleSignInOptions.java:285`
  `return new GoogleSignInOptions(3, (ArrayList<Scope>) new ArrayList(hashSet), !TextUtils.isEmpty(strOptString) ? new Account(strOptString, "com.google") : null, jSONObject.getBoolean("idTokenRequested"), jSONObject.getBoolean("serverAuthRequested"), jSONObject.getBoolean("forceCodeForRefreshToken"), ...`
- `sources/com/google/android/gms/auth/api/signin/GoogleSignInOptions.java:481`
  `jSONObject.put("forceCodeForRefreshToken", this.zal);`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:71`
  `public static final Task<Map<ApiKey<?>, String>> zai(@NonNull HasApiKey<?> hasApiKey, @NonNull HasApiKey<?>... hasApiKeyArr) {`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:72`
  `Preconditions.checkNotNull(hasApiKey, "Requested API must not be null.");`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:73`
  `for (HasApiKey<?> hasApiKey2 : hasApiKeyArr) {`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:74`
  `Preconditions.checkNotNull(hasApiKey2, "Requested API must not be null.");`
- `sources/com/google/android/gms/common/api/internal/zaae.java:26`
  `public static void zad(Activity activity, GoogleApiManager googleApiManager, ApiKey<?> apiKey) {`
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
- `sources/com/google/firebase/installations/FirebaseInstallations.java:40`
  `private static final String API_KEY_VALIDATION_MSG = "Please set a valid API key. A Firebase API key is required to communicate with Firebase server APIs: It authenticates your project with Google.Please refer to https://firebase.google.com/support/privacy/init-options.";`
- `sources/com/google/firebase/installations/Utils.java:18`
  `private static final Pattern API_KEY_FORMAT = Pattern.compile("\\AA[\\w-]{38}\\z");`
- `sources/com/google/firebase/installations/local/PersistedInstallation.java:20`
  `private static final String REFRESH_TOKEN_KEY = "RefreshToken";`
- `sources/com/google/firebase/installations/remote/AutoValue_InstallationResponse.java:19`
  `private String refreshToken;`
- `sources/com/google/firebase/installations/remote/FirebaseInstallationServiceClient.java:42`
  `private static final String API_KEY_HEADER = "x-goog-api-key";`
- `sources/com/google/firebase/installations/remote/FirebaseInstallationServiceClient.java:185`
  `httpURLConnection.addRequestProperty(API_KEY_HEADER, str);`
- `sources/com/google/firebase/messaging/AutoProtoEncoderDoNotUseEncoder.java:28`
  `private static final FieldDescriptor PACKAGENAME_DESCRIPTOR = a.p(6, FieldDescriptor.builder(CommonConstant.ReqAccessTokenParam.PACKAGE_NAME));`
- `sources/com/google/firebase/messaging/SyncTask.java:89`
  `public boolean maybeRefreshToken() throws IOException {`
- `sources/com/heytap/mcssdk/constant/b.java:46`
  `public static final String z = "appKey";`
- `sources/com/heytap/msp/push/mode/ErrorCode.java:9`
  `public static final int INVALID_APP_KEY = 14;`
- `sources/com/heytap/msp/push/mode/ErrorCode.java:17`
  `public static final int MISSING_APP_KEY = 15;`
- `sources/com/huawei/agconnect/AGConnectOptionsBuilder.java:19`
  `private static final String API_KEY_PATH = "/client/api_key";`
- `sources/com/huawei/agconnect/AGConnectOptionsBuilder.java:22`
  `private static final String CLIENT_SECRET_PATH = "/client/client_secret";`
- `sources/com/huawei/agconnect/exception/AGCServerException.java:5`
  `public static final int ACCESS_TOKEN_EXPIRED = 205524994;`
- `sources/com/huawei/hms/hwid/af.java:18`
  `jSONObject.put(CommonConstant.ReqAccessTokenParam.PACKAGE_NAME, this.a);`
- `sources/com/huawei/hms/hwid/f.java:46`
  `intent.putExtra("ACCESS_TOKEN", str2);`
- `sources/com/huawei/hms/hwid/f.java:55`
  `jSONObject.put("ACCESS_TOKEN", str2);`
- `sources/com/huawei/hms/support/api/entity/common/CommonConstant.java:22`
  `public static final String ACCESS_TOKEN = "https://www.huawei.com/auth/account/base.profile/accesstoken";`
- `sources/com/huawei/hms/support/api/entity/common/CommonConstant.java:46`
  `public static final int CLEAR_ACCESSTOKEN_FAIL_NOT_MATCH = 2010;`
- `sources/com/huawei/hms/support/api/entity/common/CommonConstant.java:74`
  `public static final String ACCESS_TOKEN = "ACCESSTOKEN";`

## BR017

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `sources/aegon/chrome/net/AndroidKeyStore.java:22`
  `Cipher cipher = Cipher.getInstance(str);`
- `sources/aegon/chrome/net/PrivateKeyType.java:11`
  `public static final int RSA = 0;`
- `sources/androidx/core/content/pm/PackageInfoCompat.java:106`
  `bArr3[i2] = MessageDigest.getInstance("SHA256").digest(signatures.get(i2).toByteArray());`
- `sources/cn/jiguang/aa/a.java:13`
  `import java.security.MessageDigest;`
- `sources/cn/jiguang/aw/c.java:14`
  `import java.security.MessageDigest;`
- `sources/cn/jiguang/aw/c.java:90`
  `messageDigest = MessageDigest.getInstance(i.c);`
- `sources/cn/jiguang/aw/i.java:6`
  `import javax.crypto.spec.IvParameterSpec;`
- `sources/cn/jiguang/aw/i.java:7`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/cn/jiguang/aw/i.java:50`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(b(str, "UTF-8"), a);`
- `sources/cn/jiguang/aw/i.java:51`
  `IvParameterSpec ivParameterSpecA = a(str2.getBytes("UTF-8"));`
- `sources/cn/jiguang/aw/i.java:52`
  `Cipher cipher = Cipher.getInstance(b);`
- `sources/cn/jiguang/aw/i.java:53`
  `cipher.init(z ? 1 : 2, secretKeySpec, ivParameterSpecA);`
- `sources/cn/jiguang/aw/j.java:6`
  `import java.security.MessageDigest;`
- `sources/cn/jiguang/aw/j.java:45`
  `MessageDigest messageDigest = MessageDigest.getInstance(i.c);`
- `sources/cn/jiguang/aw/j.java:46`
  `messageDigest.update(str.getBytes());`
- `sources/cn/jiguang/aw/j.java:47`
  `return a(messageDigest.digest());`
- `sources/cn/jiguang/az/a.java:11`
  `import javax.crypto.spec.IvParameterSpec;`
- `sources/cn/jiguang/az/a.java:12`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/cn/jiguang/az/a.java:31`
  `f.c("CryptoUtils", "doCrypto cipherMode is " + i2 + ", key is " + str + ", IvParameterSpec is " + strSubstring + ", inputFile is " + file.getAbsolutePath() + ", outputFile is " + file2.getAbsolutePath());`
- `sources/cn/jiguang/az/a.java:33`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(str.getBytes(StandardCharsets.UTF_8), c);`
- `sources/cn/jiguang/az/a.java:34`
  `IvParameterSpec ivParameterSpec = new IvParameterSpec(strSubstring.getBytes(StandardCharsets.UTF_8));`
- `sources/cn/jiguang/az/a.java:35`
  `Cipher cipher = Cipher.getInstance(b);`
- `sources/cn/jiguang/az/a.java:36`
  `cipher.init(i2, secretKeySpec, ivParameterSpec);`
- `sources/cn/jiguang/bl/i.java:22`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/cn/jiguang/bl/i.java:71`
  `mac.init(new SecretKeySpec(str.getBytes(StandardCharsets.UTF_8), str3));`
- `sources/cn/jiguang/bv/u.java:11`
  `import javax.crypto.spec.IvParameterSpec;`
- `sources/cn/jiguang/bv/u.java:12`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/cn/jiguang/bv/u.java:82`
  `cn.jiguang.ay.f.i("", "Unexpected - failed to AES encrypt.");`
- `sources/cn/jiguang/bv/u.java:113`
  `cipher = Cipher.getInstance(str2);`
- `sources/cn/jiguang/bv/u.java:122`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(c(str, "UTF-8"), d);`
- `sources/cn/jiguang/bv/u.java:123`
  `IvParameterSpec ivParameterSpecA = a(str2.getBytes("UTF-8"));`
- `sources/cn/jiguang/bv/u.java:124`
  `Cipher cipher = Cipher.getInstance(e);`
- `sources/cn/jiguang/bv/u.java:125`
  `cipher.init(z ? 1 : 2, secretKeySpec, ivParameterSpecA);`
- `sources/cn/jiguang/bv/v.java:125`
  `return MessageDigest.getInstance(u.a).digest(bArr);`
- `sources/cn/jiguang/bv/v.java:133`
  `MessageDigest messageDigest = MessageDigest.getInstance(u.a);`
- `sources/cn/jiguang/bv/v.java:139`
  `byte[] bArrDigest = messageDigest.digest(bArr);`
- `sources/cn/jiguang/bv/v.java:156`
  `byte[] bArrDigest = MessageDigest.getInstance(u.a).digest(str.getBytes("utf-8"));`
- `sources/cn/jiguang/bv/v.java:230`
  `MessageDigest messageDigest = MessageDigest.getInstance(u.a);`
- `sources/cn/jiguang/bv/v.java:231`
  `messageDigest.update(str.getBytes());`
- `sources/cn/jiguang/bv/v.java:232`
  `return a(messageDigest.digest());`
- `sources/cn/jiguang/c/a.java:66`
  `JSONObject jSONObject = new JSONObject(u.b(bundle.getString("aes"), cn.jiguang.a.a.f2212i));`
- `sources/cn/jpush/android/ab/d.java:222`
  `j.a.a.a.a.T0("pros des  failed - error:", th2, "TagAliasOperator");`
- `sources/com/bumptech/glide/load/Key.java:5`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/Key.java:15`
  `void updateDiskCacheKey(@NonNull MessageDigest messageDigest);`
- `sources/com/bumptech/glide/load/Option.java:8`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/Option.java:15`
  `public void a(@NonNull byte[] bArr, @NonNull Object obj, @NonNull MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/Options.java:47`
  `public void updateDiskCacheKey(@NonNull MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/Options.java:55`
  `cacheKeyUpdater.a(optionKeyAt.d, objValueAt, messageDigest);`
- `sources/com/bumptech/glide/load/engine/ResourceCacheKey.java:13`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/engine/ResourceCacheKey.java:92`
  `transformation.updateDiskCacheKey(messageDigest);`
- `sources/com/bumptech/glide/load/engine/ResourceCacheKey.java:94`
  `this.f2728h.updateDiskCacheKey(messageDigest);`
- `sources/com/bumptech/glide/load/engine/ResourceCacheKey.java:101`
  `messageDigest.update(bArrE);`
- `sources/com/bumptech/glide/load/engine/cache/SafeKeyGenerator.java:29`
  `public final MessageDigest a;`
- `sources/com/bumptech/glide/load/engine/cache/SafeKeyGenerator.java:32`
  `public PoolableDigestContainer(MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/engine/cache/SafeKeyGenerator.java:33`
  `this.a = messageDigest;`
- `sources/com/bumptech/glide/load/engine/prefill/BitmapPreFillRunner.java:6`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/engine/prefill/BitmapPreFillRunner.java:19`
  `public void updateDiskCacheKey(@NonNull MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/model/GlideUrl.java:94`
  `public void updateDiskCacheKey(@NonNull MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/model/GlideUrl.java:98`
  `messageDigest.update(this.g);`
- `sources/com/bumptech/glide/load/resource/UnitTransformation.java:7`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/CenterCrop.java:10`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/CenterInside.java:9`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/CircleCrop.java:11`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/FitCenter.java:7`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/GranularRoundedCorners.java:15`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/Rotate.java:10`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/RoundedCorners.java:14`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:22`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:31`
  `public void a(@NonNull byte[] bArr, @NonNull Long l2, @NonNull MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:33`
  `messageDigest.update(bArr);`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:36`
  `messageDigest.update(this.a.putLong(l3.longValue()).array());`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:44`
  `public void a(@NonNull byte[] bArr, @NonNull Integer num, @NonNull MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/resource/bitmap/VideoDecoder.java:52`
  `messageDigest.update(this.a.putInt(num2.intValue()).array());`
- `sources/com/bumptech/glide/signature/EmptySignature.java:5`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/signature/ObjectKey.java:40`
  `public void updateDiskCacheKey(@NonNull MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/signature/ObjectKey.java:41`
  `messageDigest.update(this.b.toString().getBytes(Key.a));`
- `sources/com/cmic/sso/sdk/h/a.java:5`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/cmic/sso/sdk/h/a.java:11`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(str.getBytes(), "AES");`
- `sources/com/cmic/sso/sdk/h/a.java:12`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/cmic/sso/sdk/h/a.java:13`
  `cipher.init(1, secretKeySpec, new IvParameterSpec(new byte[cipher.getBlockSize()]));`

## BR018

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:152`
  `int columnIndex4 = CursorUtil.getColumnIndex(cursorQuery, "run_attempt_count");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:193`
  `workInfoPojo.runAttemptCount = cursorQuery.getInt(columnIndex4);`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:215`
  `int columnIndex4 = CursorUtil.getColumnIndex(cursorQuery, "run_attempt_count");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:256`
  `workInfoPojo.runAttemptCount = cursorQuery.getInt(columnIndex4);`
- `sources/androidx/work/impl/model/WorkSpec.java:84`
  `@ColumnInfo(name = "run_attempt_count")`
- `sources/androidx/work/impl/model/WorkSpec.java:85`
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
- `sources/androidx/work/impl/model/WorkSpec.java:229`
  `long jScalb = this.backoffPolicy == BackoffPolicy.LINEAR ? this.backoffDelayDuration * ((long) this.runAttemptCount) : (long) Math.scalb(this.backoffDelayDuration, this.runAttemptCount - 1);`
- `sources/androidx/work/impl/model/WorkSpec.java:261`
  `if (this.initialDelay != workSpec.initialDelay || this.intervalDuration != workSpec.intervalDuration || this.flexDuration != workSpec.flexDuration || this.runAttemptCount != workSpec.runAttemptCount || this.backoffDelayDuration != workSpec.backoffDelayDuration || this.periodStartTime != workSpec.per...`
- `sources/androidx/work/impl/model/WorkSpec.java:284`
  `int iHashCode3 = (this.backoffPolicy.hashCode() + ((((this.constraints.hashCode() + ((i3 + ((int) (j4 ^ (j4 >>> 32)))) * 31)) * 31) + this.runAttemptCount) * 31)) * 31;`
- `sources/androidx/work/impl/model/WorkSpec.java:296`
  `return this.state == WorkInfo.State.ENQUEUED && this.runAttemptCount > 0;`
- `sources/androidx/work/impl/model/WorkSpec.java:365`
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
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:48`
  `return "INSERT OR IGNORE INTO 'WorkSpec' ('id','state','worker_class_name','input_merger_class_name','input','output','initial_delay','interval_duration','flex_duration','run_attempt_count','backoff_policy','backoff_delay_duration','period_start_time','minimum_retention_duration','schedule_requested...`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:87`
  `supportSQLiteStatement.bindLong(10, workSpec.runAttemptCount);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:143`
  `return "UPDATE workspec SET run_attempt_count=run_attempt_count+1 WHERE id=?";`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:149`
  `return "UPDATE workspec SET run_attempt_count=0 WHERE id=?";`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:324`
  `RoomSQLiteQuery roomSQLiteQueryAcquire = RoomSQLiteQuery.acquire("SELECT 'required_network_type', 'requires_charging', 'requires_device_idle', 'requires_battery_not_low', 'requires_storage_not_low', 'trigger_content_update_delay', 'trigger_max_content_delay', 'content_uri_triggers', 'WorkSpec'.'id' ...`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:352`
  `int columnIndexOrThrow18 = CursorUtil.getColumnIndexOrThrow(cursorQuery, "run_attempt_count");`

## BR019

paper_id: B011
paper_title: Locking it down: The privacy and security of mobile medication apps

- `sources/aegon/chrome/net/urlconnection/CronetHttpURLConnection.java:163`
  `treeMap.put(entry.getKey(), Collections.unmodifiableList(arrayList));`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:113`
  `map.put(new ComponentName(activityInfo.packageName, activityInfo.name), activityResolveInfo);`
- `sources/androidx/camera/core/internal/ViewPorts.java:34`
  `map2.put(entry.getKey(), matrix);`
- `sources/androidx/camera/extensions/internal/sessionprocessor/AdvancedSessionProcessor.java:318`
  `camera2SessionConfigBuilder.b.put(key, camera2SessionConfigImpl.getSessionParameters().get(key));`
- `sources/androidx/camera/extensions/internal/sessionprocessor/SessionProcessorBase.java:130`
  `this.a.put(Integer.valueOf(camera2OutputConfig.getId()), imageReaderNewInstance);`
- `sources/androidx/camera/video/VideoCapabilities.java:46`
  `this.a.put(quality2, camcorderProfileProxy);`
- `sources/androidx/camera/video/VideoCapabilities.java:47`
  `this.b.put(size, quality2);`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:947`
  `sparseArray.put(childAt.getId(), motionLayout2.E.get(childAt));`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:859`
  `this.a.put(getId(), this);`
- `sources/androidx/core/graphics/TypefaceCompatApi24Impl.java:133`
  `simpleArrayMap.put(uri, byteBufferMmap);`
- `sources/androidx/core/location/LocationManagerCompat.java:129`
  `simpleArrayMap.put(callback, preRGnssStatusTransport);`
- `sources/androidx/core/location/LocationManagerCompat.java:196`
  `simpleArrayMap.put(callback, gnssStatusTransport);`
- `sources/androidx/core/location/LocationManagerCompat.java:657`
  `WeakReference<LocationListenerTransport> weakReferencePut = d.put(locationListenerTransport.getKey(), new WeakReference<>(locationListenerTransport));`
- `sources/androidx/transition/ChangeBounds.java:353`
  `transitionValues.values.put("android:changeBounds:bounds", new Rect(view.getLeft(), view.getTop(), view.getRight(), view.getBottom()));`
- `sources/androidx/transition/ChangeClipBounds.java:77`
  `transitionValues.values.put("android:clipBounds:clip", clipBounds);`
- `sources/androidx/transition/ChangeClipBounds.java:79`
  `transitionValues.values.put("android:clipBounds:bounds", new Rect(0, 0, view.getWidth(), view.getHeight()));`
- `sources/androidx/transition/Explode.java:34`
  `transitionValues.values.put("android:explode:screenBounds", new Rect(i2, i3, view.getWidth() + i2, view.getHeight() + i3));`
- `sources/androidx/transition/VisibilityPropagation.java:31`
  `transitionValues.values.put("android:visibilityPropagation:center", iArr);`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:93`
  `map2.put("initial_delay", new TableInfo.Column("initial_delay", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:94`
  `map2.put("interval_duration", new TableInfo.Column("interval_duration", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:95`
  `map2.put("flex_duration", new TableInfo.Column("flex_duration", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:96`
  `map2.put("run_attempt_count", new TableInfo.Column("run_attempt_count", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:97`
  `map2.put("backoff_policy", new TableInfo.Column("backoff_policy", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:98`
  `map2.put("backoff_delay_duration", new TableInfo.Column("backoff_delay_duration", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:99`
  `map2.put("period_start_time", new TableInfo.Column("period_start_time", "INTEGER", true, 0, null, 1));`
- `sources/cn/jiguang/ai/f.java:277`
  `httpRequest.setBody(cn.jiguang.d.a.a(jSONObject.toString()));`
- `sources/cn/jiguang/an/a.java:136`
  `private HttpResponse a(HttpURLConnection httpURLConnection, String str, String str2, JSONObject jSONObject, String str3) {`
- `sources/cn/jiguang/an/a.java:144`
  `a(httpRequest, jSONObject);`
- `sources/cn/jiguang/an/a.java:196`
  `httpRequest.setBody(b(jSONObject.toString()));`
- `sources/cn/jiguang/an/a.java:211`
  `JSONObject jSONObject2 = new JSONObject(strA);`
- `sources/cn/jiguang/an/a.java:212`
  `if (2000 == jSONObject2.optInt("code")) {`
- `sources/cn/jiguang/an/a.java:213`
  `return jSONObject2;`
- `sources/cn/jiguang/an/a.java:335`
  `jSONObjectH.put("channelId", str);`
- `sources/cn/jiguang/an/a.java:336`
  `jSONObjectH.put("core_sdk_ver", cn.jiguang.a.a.b);`
- `sources/cn/jiguang/an/a.java:337`
  `jSONObjectH.put("respBody", responseBody);`
- `sources/cn/jiguang/an/a.java:338`
  `jSONObjectH.put("respHeader", a(httpResponse.getResponseHeaders()));`
- `sources/cn/jiguang/an/a.java:339`
  `f.c("JUaidManager", "start to reportToken paramJson=" + jSONObjectH);`
- `sources/cn/jiguang/an/a.java:340`
  `JSONObject jSONObjectA = a(this.g, jSONObjectH, false);`
- `sources/cn/jiguang/an/a.java:341`
  `f.c("JUaidManager", "reportToken response=" + jSONObjectA);`
- `sources/cn/jiguang/an/a.java:342`
  `if (jSONObjectA == null) {`

## BR020

paper_id: B012
paper_title: Reviewing the data security and privacy policies of mobile apps for depression

- `sources/androidx/camera/video/Recorder.java:696`
  `StringBuilder sbD0 = a.d0("Attempted to update event listener with event from incorrect recording [Recording: ");`
- `sources/androidx/core/provider/FontProvider.java:54`
  `cursorA = Api16Impl.a(context.getContentResolver(), uriBuild, new String[]{bk.d, FontsContractCompat.Columns.FILE_ID, FontsContractCompat.Columns.TTC_INDEX, FontsContractCompat.Columns.VARIATION_SETTINGS, FontsContractCompat.Columns.WEIGHT, FontsContractCompat.Columns.ITALIC, FontsContractCompat.Col...`
- `sources/androidx/core/provider/FontProvider.java:55`
  `if (cursorA != null && cursorA.getCount() > 0) {`
- `sources/androidx/core/provider/FontProvider.java:56`
  `int columnIndex = cursorA.getColumnIndex(FontsContractCompat.Columns.RESULT_CODE);`
- `sources/androidx/core/provider/FontProvider.java:58`
  `int columnIndex2 = cursorA.getColumnIndex(bk.d);`
- `sources/androidx/core/provider/FontProvider.java:59`
  `int columnIndex3 = cursorA.getColumnIndex(FontsContractCompat.Columns.FILE_ID);`
- `sources/androidx/core/provider/FontProvider.java:60`
  `int columnIndex4 = cursorA.getColumnIndex(FontsContractCompat.Columns.TTC_INDEX);`
- `sources/androidx/core/provider/FontProvider.java:61`
  `int columnIndex5 = cursorA.getColumnIndex(FontsContractCompat.Columns.WEIGHT);`
- `sources/androidx/core/provider/FontProvider.java:62`
  `int columnIndex6 = cursorA.getColumnIndex(FontsContractCompat.Columns.ITALIC);`
- `sources/androidx/core/provider/FontProvider.java:63`
  `while (cursorA.moveToNext()) {`
- `sources/androidx/core/provider/FontProvider.java:64`
  `int i2 = columnIndex != -1 ? cursorA.getInt(columnIndex) : 0;`
- `sources/androidx/core/provider/FontProvider.java:65`
  `arrayList.add(new FontsContractCompat.FontInfo(columnIndex3 == -1 ? ContentUris.withAppendedId(uriBuild, cursorA.getLong(columnIndex2)) : ContentUris.withAppendedId(uriBuild2, cursorA.getLong(columnIndex3)), columnIndex4 != -1 ? cursorA.getInt(columnIndex4) : 0, columnIndex5 != -1 ? cursorA.getInt(c...`
- `sources/androidx/room/InvalidationTracker.java:294`
  `supportSQLiteDatabase.execSQL("INSERT OR IGNORE INTO room_table_modification_log VALUES(" + i2 + ", 0)");`
- `sources/androidx/room/InvalidationTracker.java:304`
  `a.e(sb, "' BEGIN UPDATE ", "room_table_modification_log", " SET ", "invalidated");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:178`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'Dependency' ('work_spec_id' TEXT NOT NULL, 'prerequisite_id' TEXT NOT NULL, PRIMARY KEY('work_spec_id', 'prerequisite_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE , FOREIGN KEY('prerequisi...`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:179`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_Dependency_work_spec_id' ON 'Dependency' ('work_spec_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:180`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_Dependency_prerequisite_id' ON 'Dependency' ('prerequisite_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:181`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'WorkSpec' ('id' TEXT NOT NULL, 'state' INTEGER NOT NULL, 'worker_class_name' TEXT NOT NULL, 'input_merger_class_name' TEXT, 'input' BLOB NOT NULL, 'output' BLOB NOT NULL, 'initial_delay' INTEGER NOT NULL, 'interval_duration' INTEGER NOT NULL...`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:182`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkSpec_schedule_requested_at' ON 'WorkSpec' ('schedule_requested_at')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:183`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkSpec_period_start_time' ON 'WorkSpec' ('period_start_time')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:184`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'WorkTag' ('tag' TEXT NOT NULL, 'work_spec_id' TEXT NOT NULL, PRIMARY KEY('tag', 'work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:185`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkTag_work_spec_id' ON 'WorkTag' ('work_spec_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:186`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'SystemIdInfo' ('work_spec_id' TEXT NOT NULL, 'system_id' INTEGER NOT NULL, PRIMARY KEY('work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:226`
  `supportSQLiteDatabase.execSQL("PRAGMA temp_store = MEMORY;");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:227`
  `supportSQLiteDatabase.execSQL("PRAGMA recursive_triggers='ON';");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:228`
  `supportSQLiteDatabase.execSQL("CREATE TEMP TABLE room_table_modification_log(table_id INTEGER PRIMARY KEY, invalidated INTEGER NOT NULL DEFAULT 0)");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:230`
  `invalidationTracker.g = supportSQLiteDatabase.compileStatement("UPDATE room_table_modification_log SET invalidated = 0 WHERE invalidated = 1 ");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:147`
  `Cursor cursorQuery = DBUtil.query(this.a, supportSQLiteQuery, true, null);`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:149`
  `int columnIndex = CursorUtil.getColumnIndex(cursorQuery, "id");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:150`
  `int columnIndex2 = CursorUtil.getColumnIndex(cursorQuery, "state");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:151`
  `int columnIndex3 = CursorUtil.getColumnIndex(cursorQuery, "output");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:152`
  `int columnIndex4 = CursorUtil.getColumnIndex(cursorQuery, "run_attempt_count");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:155`
  `while (cursorQuery.moveToNext()) {`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:156`
  `if (!cursorQuery.isNull(columnIndex)) {`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:157`
  `String string = cursorQuery.getString(columnIndex);`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:190`
  `workInfoPojo.output = Data.fromByteArray(cursorQuery.getBlob(columnIndex3));`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:193`
  `workInfoPojo.runAttemptCount = cursorQuery.getInt(columnIndex4);`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:210`
  `Cursor cursorQuery = DBUtil.query(RawWorkInfoDao_Impl.this.a, supportSQLiteQuery, true, null);`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:212`
  `int columnIndex = CursorUtil.getColumnIndex(cursorQuery, "id");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:213`
  `int columnIndex2 = CursorUtil.getColumnIndex(cursorQuery, "state");`

## BR021

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `resources/AndroidManifest.xml:240`
  `<provider`
- `resources/AndroidManifest.xml:458`
  `<provider`
- `resources/AndroidManifest.xml:549`
  `<provider`
- `resources/AndroidManifest.xml:672`
  `<provider`
- `resources/AndroidManifest.xml:721`
  `<provider`
- `resources/AndroidManifest.xml:749`
  `<provider`
- `resources/AndroidManifest.xml:795`
  `<provider`
- `resources/AndroidManifest.xml:886`
  `<provider`
- `resources/AndroidManifest.xml:891`
  `<provider`
- `resources/AndroidManifest.xml:926`
  `<provider`
- `resources/AndroidManifest.xml:961`
  `<provider`
- `resources/AndroidManifest.xml:1103`
  `<provider`
- `resources/AndroidManifest.xml:1163`
  `<provider`
- `resources/AndroidManifest.xml:1168`
  `<provider`

## BR022

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `resources/res/xml/dcloud_file_provider.xml:3`
  `<external-path`
- `resources/res/xml/dcloud_file_provider.xml:6`
  `<root-path`
- `resources/res/xml/dcloud_file_provider.xml:9`
  `<external-files-path`
- `resources/res/xml/dcloud_file_provider.xml:12`
  `<external-cache-path`
- `resources/res/xml/dcloud_gg_file_provider.xml:3`
  `<external-path`
- `resources/res/xml/dcloud_gg_file_provider.xml:6`
  `<root-path`
- `resources/res/xml/dcloud_gg_file_provider.xml:9`
  `<external-files-path`
- `resources/res/xml/dcloud_gg_file_provider.xml:12`
  `<external-cache-path`
- `resources/res/xml/gdt_file_path.xml:3`
  `<external-cache-path`
- `resources/res/xml/gdt_file_path.xml:6`
  `<cache-path`
- `resources/res/xml/jpush_file_paths.xml:4`
  `<root-path`
- `resources/res/xml/jpush_file_paths.xml:7`
  `<external-path`
- `resources/res/xml/jpush_file_paths.xml:10`
  `<external-files-path`
- `resources/res/xml/jpush_file_paths.xml:13`
  `<files-path`
- `resources/res/xml/jpush_file_paths.xml:16`
  `<cache-path`
- `resources/res/xml/ksad_file_paths.xml:3`
  `<files-path`
- `resources/res/xml/ksad_file_paths.xml:6`
  `<cache-path`
- `resources/res/xml/ksad_file_paths.xml:9`
  `<external-files-path`
- `resources/res/xml/ksad_file_paths.xml:12`
  `<external-cache-path`

## BR023

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `sources/androidx/startup/InitializationProvider.java:20`
  `public final class InitializationProvider extends ContentProvider {`
- `sources/cn/jpush/android/ad/a.java:128`
  `int i2 = Service.class.isAssignableFrom(cls) ? 4 : BroadcastReceiver.class.isAssignableFrom(cls) ? 2 : Activity.class.isAssignableFrom(cls) ? 1 : ContentProvider.class.isAssignableFrom(cls) ? 8 : 0;`
- `sources/cn/jpush/android/service/DataProvider.java:13`
  `public class DataProvider extends ContentProvider {`
- `sources/cn/jpush/android/service/DownloadProvider.java:13`
  `public class DownloadProvider extends ContentProvider {`
- `sources/cn/jpush/android/service/InitProvider.java:21`
  `public class InitProvider extends ContentProvider {`
- `sources/com/google/firebase/provider/FirebaseInitProvider.java:17`
  `public class FirebaseInitProvider extends ContentProvider {`
- `sources/com/huawei/agconnect/core/provider/AGConnectInitializeProvider.java:11`
  `public class AGConnectInitializeProvider extends ContentProvider {`
- `sources/com/huawei/hms/aaid/InitProvider.java:10`
  `public class InitProvider extends ContentProvider {`
- `sources/com/huawei/hms/support/api/push/PushProvider.java:17`
  `public class PushProvider extends ContentProvider {`
- `sources/com/huawei/hms/update/provider/UpdateProvider.java:21`
  `public class UpdateProvider extends ContentProvider {`
- `sources/com/huawei/updatesdk/fileprovider/UpdateSdkFileProvider.java:18`
  `public class UpdateSdkFileProvider extends ContentProvider {`
- `sources/com/xiaomi/mipush/sdk/help/HelpContentProvider.java:11`
  `public class HelpContentProvider extends ContentProvider {`
- `sources/com/xiaomi/push/providers/TrafficProvider.java:13`
  `public class TrafficProvider extends ContentProvider {`

## BR024

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `sources/androidx/core/content/FileProvider.java:263`
  `if (!providerInfo.grantUriPermissions) {`
- `sources/androidx/core/content/IntentSanitizer.java:832`
  `consumer.accept("Allowing Extra Stream requires also allowing at least  FLAG_GRANT_READ_URI_PERMISSION Flag.");`
- `sources/androidx/core/content/IntentSanitizer.java:853`
  `consumer.accept("Allowing Extra Output requires also allowing FLAG_GRANT_READ_URI_PERMISSION and FLAG_GRANT_WRITE_URI_PERMISSION Flags.");`
- `sources/com/huawei/hms/update/provider/UpdateProvider.java:61`
  `if (!providerInfo.grantUriPermissions) {`
- `sources/com/huawei/updatesdk/fileprovider/UpdateSdkFileProvider.java:67`
  `if (!providerInfo.grantUriPermissions) {`
- `sources/com/kwad/sdk/api/core/fragment/FileProvider.java:239`
  `if (!providerInfo.grantUriPermissions) {`
- `sources/com/qq/e/comm/GDTFileProvider.java:198`
  `if (!providerInfo.grantUriPermissions) {`

## BR025

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/androidx/room/InvalidationTracker.java:293`
  `public final void c(SupportSQLiteDatabase supportSQLiteDatabase, int i2) {`
- `sources/androidx/room/InvalidationTracker.java:294`
  `supportSQLiteDatabase.execSQL("INSERT OR IGNORE INTO room_table_modification_log VALUES(" + i2 + ", 0)");`
- `sources/androidx/room/SQLiteCopyOpenHelper.java:80`
  `@Override // androidx.sqlite.db.SupportSQLiteOpenHelper, java.io.Closeable, java.lang.AutoCloseable`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:177`
  `public void createAllTables(SupportSQLiteDatabase supportSQLiteDatabase) {`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:178`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'Dependency' ('work_spec_id' TEXT NOT NULL, 'prerequisite_id' TEXT NOT NULL, PRIMARY KEY('work_spec_id', 'prerequisite_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE , FOREIGN KEY('prerequisi...`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:179`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_Dependency_work_spec_id' ON 'Dependency' ('work_spec_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:180`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_Dependency_prerequisite_id' ON 'Dependency' ('prerequisite_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:181`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'WorkSpec' ('id' TEXT NOT NULL, 'state' INTEGER NOT NULL, 'worker_class_name' TEXT NOT NULL, 'input_merger_class_name' TEXT, 'input' BLOB NOT NULL, 'output' BLOB NOT NULL, 'initial_delay' INTEGER NOT NULL, 'interval_duration' INTEGER NOT NULL...`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:182`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkSpec_schedule_requested_at' ON 'WorkSpec' ('schedule_requested_at')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:183`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkSpec_period_start_time' ON 'WorkSpec' ('period_start_time')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:184`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'WorkTag' ('tag' TEXT NOT NULL, 'work_spec_id' TEXT NOT NULL, PRIMARY KEY('tag', 'work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:185`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkTag_work_spec_id' ON 'WorkTag' ('work_spec_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:186`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'SystemIdInfo' ('work_spec_id' TEXT NOT NULL, 'system_id' INTEGER NOT NULL, PRIMARY KEY('work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:187`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'WorkName' ('name' TEXT NOT NULL, 'work_spec_id' TEXT NOT NULL, PRIMARY KEY('name', 'work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:188`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkName_work_spec_id' ON 'WorkName' ('work_spec_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:189`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'WorkProgress' ('work_spec_id' TEXT NOT NULL, 'progress' BLOB NOT NULL, PRIMARY KEY('work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:219`
  `workDatabase_Impl.a = supportSQLiteDatabase;`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:220`
  `supportSQLiteDatabase.execSQL("PRAGMA foreign_keys = ON");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:226`
  `supportSQLiteDatabase.execSQL("PRAGMA temp_store = MEMORY;");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:227`
  `supportSQLiteDatabase.execSQL("PRAGMA recursive_triggers='ON';");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:228`
  `supportSQLiteDatabase.execSQL("CREATE TEMP TABLE room_table_modification_log(table_id INTEGER PRIMARY KEY, invalidated INTEGER NOT NULL DEFAULT 0)");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:229`
  `invalidationTracker.f(supportSQLiteDatabase);`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:230`
  `invalidationTracker.g = supportSQLiteDatabase.compileStatement("UPDATE room_table_modification_log SET invalidated = 0 WHERE invalidated = 1 ");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:234`
  `List<RoomDatabase.Callback> list = WorkDatabase_Impl.this.f2043h;`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:43`
  `public WorkSpecDao_Impl(RoomDatabase roomDatabase) {`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:44`
  `this.a = roomDatabase;`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:45`
  `this.b = new EntityInsertionAdapter<WorkSpec>(this, roomDatabase) { // from class: androidx.work.impl.model.WorkSpecDao_Impl.1`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:140`
  `this.f = new SharedSQLiteStatement(this, roomDatabase) { // from class: androidx.work.impl.model.WorkSpecDao_Impl.5`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:146`
  `this.g = new SharedSQLiteStatement(this, roomDatabase) { // from class: androidx.work.impl.model.WorkSpecDao_Impl.6`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:152`
  `this.f2198h = new SharedSQLiteStatement(this, roomDatabase) { // from class: androidx.work.impl.model.WorkSpecDao_Impl.7`
- `sources/com/dcloud/android/downloader/db/DefaultDownloadDBController.java:26`
  `public final SQLiteDatabase b;`
- `sources/com/dcloud/android/downloader/db/DefaultDownloadDBController.java:27`
  `public final SQLiteDatabase c;`
- `sources/com/dcloud/android/downloader/db/DefaultDownloadHelper.java:4`
  `import android.database.sqlite.SQLiteDatabase;`
- `sources/com/dcloud/android/downloader/db/DefaultDownloadHelper.java:5`
  `import android.database.sqlite.SQLiteOpenHelper;`
- `sources/com/dcloud/android/downloader/db/DefaultDownloadHelper.java:11`
  `public class DefaultDownloadHelper extends SQLiteOpenHelper {`
- `sources/com/dcloud/android/downloader/db/DefaultDownloadHelper.java:17`
  `super(context, "download_info.db", (SQLiteDatabase.CursorFactory) null, 2);`
- `sources/com/dcloud/zxing2/pdf417/PDF417Common.java:37`
  `1291, 1288, 265, 1302, 1299, 2113, AdEventType.VIDEO_PAUSE, 196, 192, 2042, 1232, 1230, 1224, 214, 1220, AdEventType.VIDEO_READY, 1242, 1239, 1235, DOMException.CODE_RUNTIME_COMPONENTS_MODE_NOT_SUPPORT, 2077, 2075, 151, 148, 1993, IjkMediaMeta.FF_PROFILE_H264_HIGH_444, 1990, 1163, 1162, 1160, 1158, ...`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:4`
  `import android.database.sqlite.SQLiteDatabase;`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:5`
  `import android.database.sqlite.SQLiteOpenHelper;`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SchemaManager.java:50`
  `public final void a(SQLiteDatabase sQLiteDatabase) {`

## BR026

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/cn/jiguang/api/MultiSpHelper.java:4`
  `import android.content.SharedPreferences;`
- `sources/cn/jiguang/api/MultiSpHelper.java:11`
  `private static SharedPreferences sharedPref;`
- `sources/cn/jpush/android/cache/a.java:48`
  `sharedPreferencesReload = q(context);`
- `sources/cn/jpush/android/cache/a.java:50`
  `int i2 = sharedPreferencesReload.getInt("service_stoped", -1);`
- `sources/cn/jpush/android/cache/a.java:54`
  `int i3 = context.getSharedPreferences("cn.jpush.android.user.profile", 0).getInt("service_stoped", 0);`
- `sources/cn/jpush/android/cache/a.java:90`
  `j3 = context.getSharedPreferences("cn.jpush.android.user.profile", 0).getLong("geofence_interval", -1L);`
- `sources/cn/jpush/android/cache/a.java:119`
  `String string2 = context.getSharedPreferences("cn.jpush.android.user.profile", 0).getString("jpush_save_custom_builder" + str, "");`
- `sources/cn/jpush/android/cache/a.java:150`
  `if (i3 == -1 && (i3 = context.getSharedPreferences("cn.jpush.android.user.profile", 0).getInt("geofence_max_num", -1)) != -1) {`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:4`
  `import android.content.SharedPreferences;`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:29`
  `private final SharedPreferences firebaseSharedPreferences;`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:32`
  `this.firebaseSharedPreferences = context.getSharedPreferences(HEARTBEAT_PREFERENCES_NAME + str, 0);`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:36`
  `long j2 = this.firebaseSharedPreferences.getLong(HEART_BEAT_COUNT_TAG, 0L);`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:39`
  `for (Map.Entry<String, ?> entry : this.firebaseSharedPreferences.getAll().entrySet()) {`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:49`
  `HashSet hashSet = new HashSet(this.firebaseSharedPreferences.getStringSet(key, new HashSet()));`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:51`
  `this.firebaseSharedPreferences.edit().putStringSet(key, hashSet).putLong(HEART_BEAT_COUNT_TAG, j2 - 1).commit();`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:62`
  `for (Map.Entry<String, ?> entry : this.firebaseSharedPreferences.getAll().entrySet()) {`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:80`
  `HashSet hashSet = new HashSet(this.firebaseSharedPreferences.getStringSet(storedUserAgentString, new HashSet()));`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:83`
  `this.firebaseSharedPreferences.edit().remove(storedUserAgentString).commit();`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:85`
  `this.firebaseSharedPreferences.edit().putStringSet(storedUserAgentString, hashSet).commit();`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:90`
  `SharedPreferences.Editor editorEdit = this.firebaseSharedPreferences.edit();`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:91`
  `for (Map.Entry<String, ?> entry : this.firebaseSharedPreferences.getAll().entrySet()) {`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:103`
  `for (Map.Entry<String, ?> entry : this.firebaseSharedPreferences.getAll().entrySet()) {`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:115`
  `return (int) this.firebaseSharedPreferences.getLong(HEART_BEAT_COUNT_TAG, 0L);`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:119`
  `return this.firebaseSharedPreferences.getLong(GLOBAL, -1L);`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:128`
  `this.firebaseSharedPreferences.edit().putString(LAST_STORED_DATE, formattedDate).commit();`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:137`
  `if (!this.firebaseSharedPreferences.contains(str)) {`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:138`
  `this.firebaseSharedPreferences.edit().putLong(str, j2).commit();`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:141`
  `if (isSameDateUtc(this.firebaseSharedPreferences.getLong(str, -1L), j2)) {`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:144`
  `this.firebaseSharedPreferences.edit().putLong(str, j2).commit();`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:150`
  `if (this.firebaseSharedPreferences.getString(LAST_STORED_DATE, "").equals(formattedDate)) {`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:153`
  `long j3 = this.firebaseSharedPreferences.getLong(HEART_BEAT_COUNT_TAG, 0L);`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:156`
  `j3 = this.firebaseSharedPreferences.getLong(HEART_BEAT_COUNT_TAG, 0L);`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:158`
  `HashSet hashSet = new HashSet(this.firebaseSharedPreferences.getStringSet(str, new HashSet()));`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:160`
  `this.firebaseSharedPreferences.edit().putStringSet(str, hashSet).putLong(HEART_BEAT_COUNT_TAG, j3 + 1).putString(LAST_STORED_DATE, formattedDate).commit();`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:164`
  `this.firebaseSharedPreferences.edit().putLong(GLOBAL, j2).commit();`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:169`
  `public HeartBeatInfoStorage(SharedPreferences sharedPreferences) {`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:170`
  `this.firebaseSharedPreferences = sharedPreferences;`
- `sources/com/google/firebase/installations/local/IidStore.java:38`
  `private final SharedPreferences iidPrefs;`
- `sources/com/google/firebase/installations/local/IidStore.java:41`
  `this.iidPrefs = firebaseApp.getApplicationContext().getSharedPreferences("com.google.android.gms.appid", 0);`
- `sources/com/google/firebase/internal/DataCollectionConfigStorage.java:24`
  `private final SharedPreferences sharedPreferences;`

## BR027

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/aegon/chrome/base/FileUtils.java:64`
  `File file2 = new File(file.getPath() + bi.f3820k);`
- `sources/aegon/chrome/base/PathUtils.java:69`
  `File[] externalFilesDirs = ContextUtils.getApplicationContext().getExternalFilesDirs(Environment.DIRECTORY_DOWNLOADS);`
- `sources/aegon/chrome/base/PathUtils.java:135`
  `public static String getExternalStorageDirectory() {`
- `sources/aegon/chrome/base/PathUtils.java:136`
  `return Environment.getExternalStorageDirectory().getAbsolutePath();`
- `sources/androidx/camera/video/Recorder.java:497`
  `String absolutePathFromUri = OutputUtil.getAbsolutePathFromUri(mediaStoreOutputOptions.getContentResolver(), uriInsert, "_data");`
- `sources/androidx/camera/video/Recorder.java:501`
  `if (!OutputUtil.createParentFolder(new File(absolutePathFromUri))) {`
- `sources/androidx/camera/video/Recorder.java:506`
  `ParcelFileDescriptor parcelFileDescriptorOpenFileDescriptor = mediaStoreOutputOptions.getContentResolver().openFileDescriptor(uriInsert, "rw");`
- `sources/androidx/camera/video/Recorder.java:607`
  `String absolutePathFromUri = OutputUtil.getAbsolutePathFromUri(mediaStoreOutputOptions.getContentResolver(), uriInsert, "_data");`
- `sources/androidx/camera/video/Recorder.java:611`
  `if (!OutputUtil.createParentFolder(new File(absolutePathFromUri))) {`
- `sources/androidx/camera/video/Recorder.java:616`
  `ParcelFileDescriptor parcelFileDescriptorOpenFileDescriptor = mediaStoreOutputOptions.getContentResolver().openFileDescriptor(uriInsert, "rw");`
- `sources/androidx/camera/video/Recorder.java:648`
  `String absolutePathFromUri = OutputUtil.getAbsolutePathFromUri(mediaStoreOutputOptions2.getContentResolver(), uri, "_data");`
- `sources/androidx/core/content/FileProvider.java:52`
  `private static final File DEVICE_ROOT = new File(Operators.DIV);`
- `sources/androidx/core/graphics/drawable/IconCompat.java:631`
  `return new FileInputStream(new File((String) this.a));`
- `sources/androidx/core/util/AtomicFile.java:21`
  `this.b = new File(file.getPath() + ".new");`
- `sources/androidx/core/util/AtomicFile.java:22`
  `this.c = new File(file.getPath() + ".bak");`
- `sources/androidx/documentfile/provider/RawDocumentFile.java:67`
  `File file = new File(this.b, str2);`
- `sources/androidx/sqlite/db/SupportSQLiteOpenHelper.java:35`
  `SQLiteDatabase.deleteDatabase(new File(str));`
- `sources/androidx/sqlite/db/framework/FrameworkSQLiteOpenHelper.java:143`
  `this.f = new OpenHelper(this.a, new File(this.a.getNoBackupFilesDir(), this.b).getAbsolutePath(), frameworkSQLiteDatabaseArr, this.c);`
- `sources/androidx/work/impl/WorkDatabasePathHelper.java:21`
  `return new File(context.getNoBackupFilesDir(), "androidx.work.workdb");`
- `sources/androidx/work/impl/WorkDatabasePathHelper.java:59`
  `map.put(new File(defaultDatabasePath.getPath() + str), new File(databasePath.getPath() + str));`
- `sources/cn/jiguang/ay/b.java:170`
  `File file = new File(str3);`
- `sources/cn/jiguang/ay/b.java:183`
  `i.b(new File(string));`
- `sources/cn/jiguang/ay/b.java:237`
  `File file = new File(string + e.b);`
- `sources/cn/jiguang/ay/b.java:245`
  `File file2 = new File(string + str2);`
- `sources/cn/jiguang/ba/d.java:216`
  `File[] fileArrA = i.a(new File(file, "nowrap"), i.a.a);`
- `sources/cn/jiguang/ba/d.java:219`
  `File file2 = new File(file, "tmp");`
- `sources/cn/jiguang/bn/b.java:91`
  `return i.c(new File(new File(context.getFilesDir() + "/nes"), str + ".l"));`
- `sources/cn/jiguang/bn/b.java:148`
  `File file = new File(context.getFilesDir() + "/nes");`
- `sources/cn/jiguang/bn/b.java:153`
  `File file2 = new File(file, str + ".l");`
- `sources/cn/jiguang/dy/b.java:159`
  `File file = new File(str6);`
- `sources/cn/jiguang/dy/b.java:236`
  `File fileA2 = cn.jiguang.as.b.a(context, new File(absolutePath), cVar.f2277m, cVar.o, e.d);`
- `sources/cn/jiguang/dy/c.java:154`
  `File file = new File(cn.jiguang.aw.c.a(context), "dy_analysis");`
- `sources/cn/jiguang/dy/c.java:185`
  `file3.renameTo(new File(file3.getParentFile(), name.substring(0, name.length() - 4)));`
- `sources/cn/jpush/android/ad/a.java:268`
  `zEquals = Environment.getExternalStorageState().equals("mounted");`
- `sources/cn/jpush/android/ad/c.java:21`
  `return new File(filesDir, str);`
- `sources/cn/jpush/android/ad/c.java:291`
  `c(new File(a(context, "j_in_app_" + str, 0, false)));`
- `sources/cn/jpush/android/ad/c.java:299`
  `String str2 = (a.a() ? context.getExternalFilesDir(Environment.DIRECTORY_PICTURES) : context.getFilesDir()).getAbsolutePath() + File.separator + str;`
- `sources/cn/jpush/android/ad/c.java:300`
  `if (new File(str2).exists()) {`
- `sources/cn/jpush/android/ad/e.java:79`
  `File file = new File(str);`
- `sources/cn/jpush/android/d/c.java:30`
  `File file = new File(filesDir, str);`

## BR028

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `resources/AndroidManifest.xml:141`
  `android:allowBackup="true"`

## BR029

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:158`
  `android:exported="true"`
- `resources/AndroidManifest.xml:176`
  `android:exported="true"`
- `resources/AndroidManifest.xml:185`
  `android:exported="true"`
- `resources/AndroidManifest.xml:194`
  `android:exported="true"`
- `resources/AndroidManifest.xml:213`
  `android:exported="true">`
- `resources/AndroidManifest.xml:666`
  `android:exported="true"`
- `resources/AndroidManifest.xml:821`
  `android:exported="true">`
- `resources/AndroidManifest.xml:831`
  `android:exported="true"`
- `resources/AndroidManifest.xml:864`
  `android:exported="true"`
- `resources/AndroidManifest.xml:893`
  `android:exported="true"`
- `resources/AndroidManifest.xml:898`
  `android:exported="true"`
- `resources/AndroidManifest.xml:909`
  `android:exported="true"`
- `resources/AndroidManifest.xml:1003`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:1066`
  `android:exported="true"`

## BR030

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:450`
  `android:exported="true">`
- `resources/AndroidManifest.xml:566`
  `android:exported="true"`
- `resources/AndroidManifest.xml:666`
  `android:exported="true"`
- `resources/AndroidManifest.xml:854`
  `android:exported="true">`
- `resources/AndroidManifest.xml:953`
  `android:exported="true"`
- `resources/AndroidManifest.xml:1003`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:1037`
  `android:exported="true"/>`

## BR031

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:522`
  `android:exported="true">`
- `resources/AndroidManifest.xml:641`
  `android:exported="true"`
- `resources/AndroidManifest.xml:933`
  `android:exported="true"`
- `resources/AndroidManifest.xml:943`
  `android:exported="true"`
- `resources/AndroidManifest.xml:1037`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:1051`
  `android:exported="true">`

## BR032

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `resources/AndroidManifest.xml:166`
  `<action android:name="android.intent.action.VIEW"/>`

## BR033

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/cn/jpush/android/ui/a.java:130`
  `intent.setDataAndType(Uri.parse(str), "audio/*");`
- `sources/cn/jpush/android/ui/a.java:136`
  `webView.getContext().startActivity(new Intent(CommonConstant.ACTION.HWID_SCHEME_URL, Uri.parse(str)));`
- `sources/cn/jpush/android/ui/a.java:201`
  `intent4.setDataAndType(Uri.parse(str), "video/*");`
- `sources/com/dmcbig/mediapicker/PickerActivity.java:658`
  `intent2.putExtra("IMAGE_URI", Uri.parse(sbD0.toString()));`
- `sources/com/dmcbig/mediapicker/PreviewActivity.java:179`
  `intent.putExtra("IMAGE_URI", Uri.parse(sbD0.toString()));`
- `sources/com/dmcbig/mediapicker/adapter/FolderAdapter.java:79`
  `requestManagerE.f(Uri.parse(sbD0.toString())).z(viewHolder.a);`
- `sources/com/huawei/hms/health/aaba.java:291`
  `Intent intent = new Intent(CommonConstant.ACTION.HWID_SCHEME_URL, Uri.parse("huaweischeme://healthapp/achievement?module=kit"));`
- `sources/com/huawei/hms/update/ui/ThirdPartyMarketWizard.java:152`
  `safeIntent.setData(Uri.parse("market://details?id=" + this.e));`
- `sources/com/hybirdlib/hybirdlib/SdkPluginUtils.java:572`
  `intent.setData(Uri.parse(str));`
- `sources/com/hybirdlib/hybirdlib/permission/PermissionUtils.java:175`
  `intent.setData(Uri.parse(sbD0.toString()));`
- `sources/com/kwad/components/core/e/d/e.java:37`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/launchWXMiniprogram"), null, null, new String[]{smallAppJumpInfo.mediaSmallAppId, smallAppJumpInfo.originId, smallAppJumpInfo.smallAppJumpUrl, "0", ""}, null);`
- `sources/com/kwad/components/core/page/d.java:62`
  `Intent intent = new Intent("android.settings.MANAGE_UNKNOWN_APP_SOURCES", Uri.parse("package:" + getActivity().getApplicationInfo().packageName));`
- `sources/com/kwad/sdk/core/webview/KsAdWebView.java:47`
  `Intent intent = new Intent(CommonConstant.ACTION.HWID_SCHEME_URL, Uri.parse(str));`
- `sources/com/kwad/sdk/core/webview/a/c.java:195`
  `Intent intent = new Intent(CommonConstant.ACTION.HWID_SCHEME_URL, Uri.parse(str));`
- `sources/com/lxj/xpopup/util/XPermission.java:141`
  `intent.setData(Uri.parse(sbD0.toString()));`
- `sources/com/lxj/xpopup/util/XPermission.java:157`
  `intent2.setData(Uri.parse(sbD02.toString()));`
- `sources/com/lxj/xpopup/util/XPermission.java:211`
  `intent.setData(Uri.parse(sbD0.toString()));`
- `sources/com/lxj/xpopup/util/XPopupUtils.java:107`
  `intent.setData(Uri.parse(DeviceInfo.FILE_PROTOCOL + file2.getAbsolutePath()));`
- `sources/com/taobao/weex/bridge/RequestHandler.java:114`
  `wXRequest.url = wXSDKManager.getURIAdapter().rewrite(sDKInstance, AbsURIAdapter.BUNDLE, Uri.parse(str2)).toString();`
- `sources/com/taobao/weex/utils/WXViewToImageUtil.java:101`
  `context.sendBroadcast(new Intent("android.intent.action.MEDIA_SCANNER_SCAN_FILE", Uri.parse(sbD0.toString())));`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:323`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/finderOpenProfile"), null, null, new String[]{this.appId, ((WXChannelOpenProfile.Req) baseReq).userName}, null);`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:361`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/jumpToOfflinePay"), null, null, new String[]{this.appId}, null);`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:371`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/launchWXMiniprogram"), null, null, new String[]{this.appId, req.userName, req.path, a.T(new StringBuilder(), req.miniprogramType, ""), req.extData}, null);`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:389`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/openTypeWebview"), null, null, new String[]{this.appId, String.valueOf(3), URLEncoder.encode(String.format("url=%s", URLEncoder.encode(((WXNontaxPay.Req) baseReq).url)))}, null);`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:459`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/openTypeWebview"), null, null, new String[]{this.appId, String.valueOf(4), URLEncoder.encode(String.format("url=%s", URLEncoder.encode(((WXPayInsurance.Req) baseReq).url)))}, null);`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:512`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/preloadWXMiniprogram"), null, null, new String[]{this.appId, req.userName, req.path, a.T(new StringBuilder(), req.miniprogramType, ""), req.extData}, null);`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:522`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/QRCodePay"), null, null, new String[]{this.appId, req.codeContent, req.extraMsg}, null);`
- `sources/com/umeng/analytics/pro/ba.java:17`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse(a), null, null, null, null);`
- `sources/com/vivo/push/d/u.java:76`
  `Uri uri2 = Uri.parse(skipContent);`
- `sources/io/dcloud/WebviewActivity.java:230`
  `Intent intent2 = new Intent(CommonConstant.ACTION.HWID_SCHEME_URL, Uri.parse(str));`
- `sources/io/dcloud/WebviewActivity.java:305`
  `strValueOf = PlatformUtil.getFilePathFromContentUri(Uri.parse(strValueOf), WebviewActivity.this.that.getContentResolver());`
- `sources/io/dcloud/WebviewActivity.java:338`
  `intent.setData(Uri.parse(str));`
- `sources/io/dcloud/WebviewActivity.java:357`
  `intent2.setData(Uri.parse(str));`
- `sources/io/dcloud/WebviewActivity.java:650`
  `intent.setData(Uri.parse(this.f4925h.getUrl()));`
- `sources/io/dcloud/common/adapter/ui/webview/SysWebView.java:411`
  `strValueOf = PlatformUtil.getFilePathFromContentUri(Uri.parse(strValueOf), context.getContentResolver());`
- `sources/io/dcloud/common/adapter/ui/webview/SysWebView.java:425`
  `strValueOf2 = PlatformUtil.getFilePathFromContentUri(Uri.parse(strValueOf2), context.getContentResolver());`
- `sources/io/dcloud/common/adapter/ui/webview/SysWebView.java:852`
  `intent.setData(Uri.parse(str));`
- `sources/io/dcloud/common/adapter/ui/webview/SysWebView.java:876`
  `intent2.setData(Uri.parse(str));`
- `sources/io/dcloud/common/adapter/ui/webview/WebJsEvent.java:212`
  `uri = Uri.parse(string);`
- `sources/io/dcloud/common/adapter/ui/webview/WebJsEvent.java:214`
  `uri = Uri.parse((string.startsWith(Operators.DIV) ? DeviceInfo.FILE_PROTOCOL : "file:///") + string);`
- `sources/io/dcloud/common/adapter/ui/webview/WebLoadEvent.java:1255`
  `this.mAdaWebview.getActivity().startActivity(new Intent(CommonConstant.ACTION.HWID_SCHEME_URL, Uri.parse(str)));`
- `sources/io/dcloud/common/adapter/ui/webview/WebLoadEvent.java:1260`
  `Intent intent = new Intent(CommonConstant.ACTION.HWID_SCHEME_URL, Uri.parse("sms:" + strSubstring));`
- `sources/io/dcloud/common/adapter/ui/webview/WebLoadEvent.java:1275`
  `this.mAdaWebview.getActivity().startActivity(new Intent(CommonConstant.ACTION.HWID_SCHEME_URL, Uri.parse(str)));`
- `sources/io/dcloud/common/adapter/util/DownloadUtil.java:86`
  `str = PlatformUtil.getFilePathFromContentUri(Uri.parse(str), context.getContentResolver());`
- `sources/io/dcloud/common/adapter/util/PlatformUtil.java:628`
  `str = getFilePathFromContentUri(Uri.parse(str), context.getContentResolver());`
- `sources/io/dcloud/common/adapter/util/PlatformUtil.java:687`
  `android.net.Uri r4 = android.net.Uri.parse(r2)     // Catch: java.lang.Throwable -> L2e java.lang.Exception -> L30`
- `sources/io/dcloud/common/adapter/util/PlatformUtil.java:745`
  `android.net.Uri r4 = android.net.Uri.parse(r2)     // Catch: java.lang.Throwable -> L2e java.lang.Exception -> L30`
- `sources/io/dcloud/common/ui/a.java:74`
  `intent.setData(Uri.parse(this.c.getURL()));`
- `sources/io/dcloud/common/ui/a.java:95`
  `intent2.setData(Uri.parse(url));`
- `sources/io/dcloud/common/ui/b.java:43`
  `intent.setData(Uri.parse(url));`
- `sources/io/dcloud/common/util/ADUtils.java:208`
  `intent.setData(Uri.parse(str));`
- `sources/io/dcloud/common/util/ADUtils.java:297`
  `intent.setData(Uri.parse(str));`
- `sources/io/dcloud/common/util/AppPermissionUtil.java:55`
  `Intent intent = new Intent("android.settings.APPLICATION_DETAILS_SETTINGS", Uri.parse(sbD0.toString()));`
- `sources/io/dcloud/common/util/AppPermissionUtil.java:340`
  `Intent intent = new Intent("android.settings.APPLICATION_DETAILS_SETTINGS", Uri.parse(sbD0.toString()));`
- `sources/io/dcloud/common/util/ErrorDialogUtil.java:56`
  `intent.setData(Uri.parse(str2));`
- `sources/io/dcloud/common/util/ErrorDialogUtil.java:107`
  `intent.setData(Uri.parse(str2));`
- `sources/io/dcloud/e/b/a.java:169`
  `intent.setData(Uri.parse("https://ask.dcloud.net.cn/article/35627"));`
- `sources/io/dcloud/e/b/a.java:185`
  `intent.setData(Uri.parse("https://ask.dcloud.net.cn/article/35877"));`
- `sources/io/dcloud/e/c/b.java:149`
  `Uri uri = Uri.parse(str);`
- `sources/io/dcloud/feature/device/DeviceFeatureImpl.java:263`
  `iWebview.getActivity().startActivity(new Intent(!z ? "android.intent.action.CALL" : "android.intent.action.DIAL", Uri.parse("tel:" + str)));`
- `sources/io/dcloud/feature/pdr/RuntimeFeatureImpl.java:426`
  `intent.setData(Uri.parse(str));`
- `sources/io/dcloud/feature/weex/adapter/webview/DCWXWebView.java:242`
  `uriForFile = Uri.parse(string);`
- `sources/io/dcloud/feature/weex/adapter/webview/DCWXWebView.java:244`
  `uriForFile = Uri.parse((string.startsWith(Operators.DIV) ? DeviceInfo.FILE_PROTOCOL : "file:///") + string);`
- `sources/io/dcloud/feature/weex/adapter/webview/DCWXWebView.java:489`
  `Intent intent = new Intent(CommonConstant.ACTION.HWID_SCHEME_URL, Uri.parse(str));`
- `sources/io/dcloud/feature/weex/extend/WXEventModule.java:42`
  `Uri uri = Uri.parse(sb.toString());`
- `sources/io/dcloud/feature/weex_barcode/BarcodeView.java:571`
  `path = this.mInstance.rewriteUri(Uri.parse(this.mFilename), "image").getPath();`
- `sources/io/dcloud/h/a/e/b.java:59`
  `intent.setData(Uri.parse(str));`
- `sources/io/dcloud/h/a/e/b.java:98`
  `intent.setData(Uri.parse(str));`
- `sources/io/dcloud/h/c/b/b/b.java:161`
  `intent.setData(Uri.parse(c.this.f5120K));`
- `sources/io/dcloud/js/camera/CameraFeatureImpl.java:262`
  `intent.putExtra("IMAGE_URI", Uri.parse(sbD0.toString()));`
- `sources/io/dcloud/js/gallery/GalleryFeatureImpl.java:166`
  `b.this.c.getContext().sendBroadcast(new Intent("android.intent.action.MEDIA_SCANNER_SCAN_FILE", Uri.parse(DeviceInfo.FILE_PROTOCOL + pathFromUri)));`
- `sources/io/dcloud/js/gallery/GalleryFeatureImpl.java:705`
  `strConvert2WebviewFullPath = FileUtil.getPathFromUri(iApp.getActivity(), Uri.parse(str3));`
- `sources/io/dcloud/net/JsUpload.java:105`
  `Uri uri = Uri.parse(str);`
- `sources/io/dcloud/sdk/activity/WebViewActivity.java:177`
  `Intent intent2 = new Intent(CommonConstant.ACTION.HWID_SCHEME_URL, Uri.parse(str));`
- `sources/io/dcloud/sdk/activity/WebViewActivity.java:463`
  `intent.setData(Uri.parse(this.f5172h.getUrl()));`
- `sources/io/dcloud/sdk/base/entry/AdData.java:428`
  `intent.setData(Uri.parse(this.url));`

## BR034

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/androidx/work/impl/background/systemalarm/SystemAlarmScheduler.java:28`
  `this.a.startService(intent);`
- `sources/cn/jiguang/ae/b.java:43`
  `if (this.a.startService(intent) != null) {`
- `sources/cn/jpush/android/d/b.java:238`
  `context.sendBroadcast(intent, String.format(locale, "%s.permission.JPUSH_MESSAGE", dVar.b));`
- `sources/cn/jpush/android/g/b.java:25`
  `cn.jpush.android.f.c.a.sendBroadcast(intent);`
- `sources/cn/jpush/android/n/a.java:35`
  `context.sendBroadcast(intent);`
- `sources/cn/jpush/android/x/b.java:477`
  `context.sendBroadcast(intent);`
- `sources/cn/jpush/android/x/b.java:1111`
  `context.startActivity(intent);`
- `sources/com/hybirdlib/hybirdlib/SdkPluginUtils.java:575`
  `context.startActivity(intent);`
- `sources/com/hybirdlib/hybirdlib/permission/PermissionUtils.java:176`
  `Utils.getApp().startActivity(intent.addFlags(268435456));`
- `sources/com/lxj/xpopup/util/XPermission.java:213`
  `this.a.startActivity(intent.addFlags(268435456));`
- `sources/com/lxj/xpopup/util/XPopupUtils.java:108`
  `this.b.sendBroadcast(intent);`
- `sources/com/mobile/auth/gatewayauth/c.java:608`
  `activity.startActivity(intent);`
- `sources/com/qq/e/comm/DownloadService.java:39`
  `context.startService(intent);`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothScanBALANCED.java:114`
  `context.sendBroadcast(intent);`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothScanBALANCED.java:224`
  `context.sendBroadcast(intent);`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothScanDefault.java:114`
  `context.sendBroadcast(intent);`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothScanDefault.java:224`
  `context.sendBroadcast(intent);`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothScanNoLimit.java:101`
  `context.sendBroadcast(intent);`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothScanNoLimit.java:189`
  `context.sendBroadcast(intent);`
- `sources/com/taobao/weex/WXSDKInstance.java:1891`
  `this.mContext.sendBroadcast(intent);`
- `sources/com/xiaomi/mipush/sdk/PushMessageHandler.java:198`
  `context.sendBroadcast(intent, d.a(context));`
- `sources/com/xiaomi/push/ez.java:57`
  `if (context.startService(intent) == null) {`
- `sources/com/xiaomi/push/service/XMJobService.java:67`
  `startService(intent);`
- `sources/com/xs/jpush/JPushReceiver.java:44`
  `context.startActivity(launchIntentForPackage);`
- `sources/io/dcloud/WebviewActivity.java:339`
  `WebviewActivity.this.startActivity(intent);`
- `sources/io/dcloud/WebviewActivity.java:358`
  `WebviewActivity.this.startActivity(intent2);`
- `sources/io/dcloud/WebviewActivity.java:651`
  `startActivity(Intent.createChooser(intent, getString(io.dcloud.base.R.string.dcloud_common_open_web)));`
- `sources/io/dcloud/common/adapter/ui/webview/SysWebView.java:853`
  `context.startActivity(intent);`
- `sources/io/dcloud/common/adapter/ui/webview/SysWebView.java:877`
  `this.mAdaWebview.getActivity().startActivity(intent2);`
- `sources/io/dcloud/common/core/ui/l.java:131`
  `this.b.getActivity().sendBroadcast(intent);`
- `sources/io/dcloud/common/ui/a.java:75`
  `a.this.a.startActivity(intent);`
- `sources/io/dcloud/common/ui/a.java:99`
  `a.this.a.startActivity(intent2, ActivityOptionsCompat.makeCustomAnimation(a.this.a, R.anim.dcloud_pop_in, R.anim.dcloud_pop_in_out).toBundle());`
- `sources/io/dcloud/common/ui/b.java:47`
  `b.this.f.startActivity(intent, ActivityOptionsCompat.makeCustomAnimation(b.this.f, R.anim.dcloud_pop_in, R.anim.dcloud_pop_in_out).toBundle());`
- `sources/io/dcloud/common/util/ADUtils.java:211`
  `context.startActivity(intent);`
- `sources/io/dcloud/common/util/ADUtils.java:300`
  `context.startActivity(intent);`
- `sources/io/dcloud/common/util/ErrorDialogUtil.java:57`
  `activity.startActivity(intent);`
- `sources/io/dcloud/common/util/ErrorDialogUtil.java:108`
  `iWebview.getActivity().startActivity(intent);`
- `sources/io/dcloud/common/util/LoadAppUtils.java:389`
  `context.startActivity(intent);`
- `sources/io/dcloud/common/util/RuningAcitvityUtil.java:20`
  `public static void StartActivity(Context context, Intent intent) {`
- `sources/io/dcloud/common/util/RuningAcitvityUtil.java:23`
  `context.startActivity(intent2);`
- `sources/io/dcloud/common/util/ShortCutUtil.java:457`
  `context.sendBroadcast(intent);`
- `sources/io/dcloud/e/b/a.java:170`
  `this.a.startActivity(intent);`
- `sources/io/dcloud/e/b/a.java:186`
  `this.a.startActivity(intent);`
- `sources/io/dcloud/feature/gg/dcloud/ADHandler.java:102`
  `this.mContext.sendBroadcast(intent);`
- `sources/io/dcloud/feature/gg/dcloud/ADHandler.java:660`
  `LocalBroadcastManager.getInstance(context).sendBroadcast(intent);`
- `sources/io/dcloud/feature/pdr/RuntimeFeatureImpl.java:429`
  `iWebview.getContext().startActivity(intent);`
- `sources/io/dcloud/feature/weex/extend/PlusModule.java:567`
  `context.startActivity(intent);`
- `sources/io/dcloud/feature/weex/extend/WXEventModule.java:45`
  `this.mWXSDKInstance.getContext().startActivity(intent);`
- `sources/io/dcloud/h/a/e/b.java:62`
  `context.startActivity(intent);`
- `sources/io/dcloud/h/a/e/b.java:101`
  `context.startActivity(intent);`
- `sources/io/dcloud/h/c/b/b/b.java:163`
  `c.this.getActivity().startActivity(intent);`
- `sources/io/dcloud/sdk/activity/WebViewActivity.java:464`
  `startActivity(Intent.createChooser(intent, "打开网页"));`
- `sources/io/dcloud/sdk/base/entry/AdData.java:431`
  `context.startActivity(intent);`
- `sources/io/dcloud/share/mm/WeiXinApiManager.java:627`
  `activity.startActivity(intent);`

## BR035

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/cn/jpush/android/api/SystemAlertHelper.java:173`
  `SystemAlertHelper.e.loadUrl(str);`
- `sources/cn/jpush/android/u/f.java:107`
  `this.f.loadUrl(str);`
- `sources/cn/jpush/android/ui/c.java:168`
  `this.g.loadUrl(str2);`
- `sources/com/cmic/sso/sdk/widget/a.java:53`
  `a.this.a.loadUrl(str);`
- `sources/com/cmic/sso/sdk/widget/a.java:100`
  `this.a.loadUrl(this.b);`
- `sources/com/huawei/secure/android/common/webview/SafeWebView.java:386`
  `super.loadUrl(str);`
- `sources/com/huawei/secure/android/common/webview/SafeWebView.java:391`
  `super.loadUrl(this.a);`
- `sources/com/huawei/secure/android/common/webview/SafeWebView.java:403`
  `webView.loadUrl(defaultErrorPage);`
- `sources/com/huawei/secure/android/common/webview/SafeWebView.java:502`
  `super.loadUrl(this.a, map);`
- `sources/com/huawei/secure/android/common/webview/SafeWebView.java:513`
  `super.loadUrl(str, map);`
- `sources/com/kwad/components/ad/draw/b/b/c.java:104`
  `this.ew.loadUrl(com.kwad.sdk.core.response.b.b.cH(this.mAdTemplate));`
- `sources/com/kwad/components/ad/draw/b/b/c.java:107`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ad/draw/b/b/c.java:113`
  `this.ew.addJavascriptInterface(this.ey, "KwaiAd");`
- `sources/com/kwad/components/ad/f/e.java:391`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ad/f/e.java:398`
  `this.mAdWebView.addJavascriptInterface(this.ey, "KwaiAd");`
- `sources/com/kwad/components/ad/f/e.java:399`
  `this.mAdWebView.loadUrl(com.kwad.sdk.core.response.b.b.dh(this.mAdTemplate));`
- `sources/com/kwad/components/ad/feed/b/n.java:812`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ad/feed/b/n.java:822`
  `this.mAdWebView.loadUrl(com.kwad.sdk.core.response.b.b.df(this.mAdTemplate));`
- `sources/com/kwad/components/ad/l/b.java:196`
  `this.ew.loadUrl(C(this.mAdTemplate));`
- `sources/com/kwad/components/ad/l/b.java:298`
  `this.ew.loadUrl(strC);`
- `sources/com/kwad/components/ad/reward/n/e.java:53`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ad/reward/n/e.java:64`
  `this.ew.addJavascriptInterface(this.ey, "KwaiAd");`
- `sources/com/kwad/components/ad/reward/n/e.java:65`
  `this.ew.loadUrl(str);`
- `sources/com/kwad/components/ad/reward/page/AdRewardPreviewActivityProxy.java:429`
  `this.mAdWebView.loadUrl(!TextUtils.isEmpty(this.mUrl) ? this.mUrl : com.kwad.sdk.core.response.b.a.aV(com.kwad.sdk.core.response.b.e.ew(this.mAdTemplate)));`
- `sources/com/kwad/components/ad/reward/presenter/platdetail/actionbar/f.java:136`
  `this.ew.loadUrl(this.mUrl);`
- `sources/com/kwad/components/ad/reward/presenter/platdetail/actionbar/f.java:139`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ad/reward/presenter/platdetail/actionbar/f.java:145`
  `this.ew.addJavascriptInterface(this.ey, "KwaiAd");`
- `sources/com/kwad/components/ad/splashscreen/presenter/p.java:340`
  `ksAdWebView.loadUrl(str);`
- `sources/com/kwad/components/ad/splashscreen/presenter/p.java:346`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ad/splashscreen/presenter/p.java:353`
  `webView.addJavascriptInterface(this.ey, "KwaiAd");`
- `sources/com/kwad/components/core/e/c/e.java:89`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/core/e/c/e.java:96`
  `this.ew.addJavascriptInterface(this.ey, "KwaiAd");`
- `sources/com/kwad/components/core/o/b/d/a.java:79`
  `@SuppressLint({"JavascriptInterface", "AddJavascriptInterface"})`
- `sources/com/kwad/components/core/o/b/d/a.java:80`
  `public final void addJavascriptInterface(Object obj, String str) {`
- `sources/com/kwad/components/core/o/b/d/a.java:81`
  `this.Qi.addJavascriptInterface(obj, str);`
- `sources/com/kwad/components/core/o/b/d/a.java:116`
  `this.Qi.loadUrl(str);`
- `sources/com/kwad/components/core/page/c/b.java:45`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/core/page/c/b.java:51`
  `this.mAdWebView.addJavascriptInterface(this.ey, "KwaiAd");`
- `sources/com/kwad/components/core/page/c/b.java:71`
  `this.mAdWebView.loadUrl(com.kwad.sdk.core.response.b.a.aV(com.kwad.sdk.core.response.b.e.ew(this.mAdTemplate)));`
- `sources/com/kwad/components/core/page/c/f.java:45`
  `this.Qr.loadUrl(str);`
- `sources/com/kwad/components/core/page/c/f.java:57`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/core/page/c/f.java:63`
  `this.Qr.addJavascriptInterface(this.ey, "KwaiAd");`
- `sources/com/kwad/components/core/page/c/a/g.java:212`
  `this.mAdWebView.loadUrl(this.Ra.mPageUrl);`
- `sources/com/kwad/components/core/playable/a.java:222`
  `this.Ti.loadUrl(url);`
- `sources/com/kwad/components/core/playable/a.java:241`
  `@SuppressLint({"AddJavascriptInterface"})`
- `sources/com/kwad/components/core/playable/a.java:263`
  `this.Ti.addJavascriptInterface(this.ey, "KwaiAd");`
- `sources/com/kwad/components/core/webview/b.java:285`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/core/webview/b.java:295`
  `ksAdWebView.addJavascriptInterface(this.ey, "KwaiAd");`
- `sources/com/kwad/components/core/webview/b.java:302`
  `ksAdWebView.addJavascriptInterface(aVar, "KwaiAdForThird");`
- `sources/com/kwad/components/ct/c/a.java:61`
  `this.aiR.addJavascriptInterface(this.aKO, "kwadSDK");`
- `sources/com/kwad/components/ct/c/a.java:108`
  `this.aiR.loadUrl(value);`
- `sources/com/kwad/components/ct/c/a.java:126`
  `this.aiR.loadUrl(value);`
- `sources/com/kwad/components/ct/coupon/a.java:106`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ct/coupon/a.java:115`
  `this.ew.addJavascriptInterface(this.ey, "KwaiAd");`
- `sources/com/kwad/components/ct/coupon/a.java:116`
  `this.ew.loadUrl(getUrl());`
- `sources/com/kwad/components/ct/coupon/a/a.java:79`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ct/coupon/a/a.java:86`
  `this.Qr.addJavascriptInterface(this.ey, "KwaiAd");`
- `sources/com/kwad/components/ct/detail/ad/presenter/c.java:185`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ct/detail/ad/presenter/c.java:191`
  `this.aiR.addJavascriptInterface(this.ey, "KwaiAd");`
- `sources/com/kwad/components/ct/detail/ad/presenter/a/b.java:224`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ct/detail/ad/presenter/a/b.java:230`
  `this.aiR.addJavascriptInterface(this.ey, "KwaiAd");`
- `sources/com/kwad/components/ct/detail/photo/a/e.java:110`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ct/detail/photo/a/e.java:116`
  `this.Qr.addJavascriptInterface(this.ey, "KwaiAd");`
- `sources/com/kwad/components/ct/home/a/e.java:328`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ct/home/a/e.java:334`
  `this.Qr.addJavascriptInterface(this.ey, "KwaiAd");`
- `sources/com/kwad/components/ct/horizontal/news/c/e.java:338`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ct/horizontal/news/c/e.java:344`
  `this.aiR.addJavascriptInterface(this.ey, "KwaiAd");`
- `sources/com/kwad/components/ct/horizontal/video/presenter/a.java:113`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ct/horizontal/video/presenter/a.java:119`
  `this.aiR.addJavascriptInterface(this.ey, "KwaiAd");`
- `sources/com/kwad/components/ct/horizontal/video/presenter/b.java:163`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ct/horizontal/video/presenter/b.java:169`
  `this.aiR.addJavascriptInterface(this.ey, "KwaiAd");`
- `sources/com/kwad/components/ct/horizontal/video/presenter/b.java:267`
  `this.aiR.loadUrl(strCC);`
- `sources/com/kwad/sdk/core/webview/KsAdWebView.java:171`
  `super.loadUrl(str);`
- `sources/com/taobao/weex/ui/component/WXEmbed.java:238`
  `webView.loadUrl(((WXEmbed) nestedContainer).src);`
- `sources/com/taobao/weex/ui/component/WXWeb.java:136`
  `getWebView().loadUrl(str);`
- `sources/com/taobao/weex/ui/view/WXWebView.java:82`
  `this.mWebView.loadUrl(str);`
- `sources/com/taobao/weex/ui/view/WXWebView.java:155`
  `webView2.loadUrl(str);`
- `sources/com/taobao/weex/ui/view/WXWebView.java:197`
  `webView.addJavascriptInterface(new Object() { // from class: com.taobao.weex.ui.view.WXWebView.3`
- `sources/com/taobao/weex/ui/view/WXWebView.java:299`
  `getWebView().loadUrl(str);`
- `sources/com/tencent/bugly/crashreport/CrashReport.java:759`
  `webView.loadUrl(str);`

## BR040

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `resources/AndroidManifest.xml:257`
  `android:name="com.qq.e.ads.ADActivity"`
- `resources/AndroidManifest.xml:263`
  `android:name="com.qq.e.ads.PortraitADActivity"`
- `resources/AndroidManifest.xml:270`
  `android:name="com.qq.e.ads.LandscapeADActivity"`
- `resources/AndroidManifest.xml:277`
  `android:name="com.qq.e.ads.RewardvideoPortraitADActivity"`
- `resources/AndroidManifest.xml:287`
  `android:name="com.qq.e.ads.RewardvideoLandscapeADActivity"`
- `resources/AndroidManifest.xml:298`
  `android:name="com.qq.e.ads.DialogActivity"`
- `resources/AndroidManifest.xml:308`
  `android:name="com.kwad.sdk.api.proxy.app.AdWebViewActivity"`
- `resources/AndroidManifest.xml:313`
  `android:name="com.kwad.sdk.api.proxy.app.KsFullScreenVideoActivity"`
- `resources/AndroidManifest.xml:318`
  `android:name="com.kwad.sdk.api.proxy.app.KsFullScreenLandScapeVideoActivity"`
- `resources/AndroidManifest.xml:323`
  `android:name="com.kwad.sdk.api.proxy.app.KsRewardVideoActivity"`
- `resources/AndroidManifest.xml:328`
  `android:name="com.kwad.sdk.api.proxy.app.KSRewardLandScapeVideoActivity"`
- `resources/AndroidManifest.xml:333`
  `android:name="com.kwad.sdk.api.proxy.app.FeedDownloadActivity"`
- `resources/AndroidManifest.xml:338`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.KsTrendsActivity"`
- `resources/AndroidManifest.xml:342`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.ProfileHomeActivity"`
- `resources/AndroidManifest.xml:346`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.GoodsPlayBackActivity"`
- `resources/AndroidManifest.xml:350`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.ProfileVideoDetailActivity"`
- `resources/AndroidManifest.xml:354`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.TubeProfileActivity"`
- `resources/AndroidManifest.xml:358`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.ChannelDetailActivity"`
- `resources/AndroidManifest.xml:362`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.TubeDetailActivity"`
- `resources/AndroidManifest.xml:366`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.EpisodeDetailActivity"`
- `resources/AndroidManifest.xml:371`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.FragmentActivity1"`
- `resources/AndroidManifest.xml:376`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.FragmentActivity2"`
- `resources/AndroidManifest.xml:381`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.FragmentActivity3"`
- `resources/AndroidManifest.xml:385`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.FragmentActivity4"`
- `resources/AndroidManifest.xml:389`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.FragmentActivity5"`
- `resources/AndroidManifest.xml:393`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.FragmentActivity6"`
- `resources/AndroidManifest.xml:397`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.FragmentActivity7"`
- `resources/AndroidManifest.xml:401`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.FragmentActivity8"`
- `resources/AndroidManifest.xml:405`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.FragmentActivity9"`
- `resources/AndroidManifest.xml:409`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.FragmentActivity10"`
- `resources/AndroidManifest.xml:413`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.FragmentActivitySingleTop1"`
- `resources/AndroidManifest.xml:418`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.FragmentActivitySingleTop2"`
- `resources/AndroidManifest.xml:423`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.FragmentActivitySingleInstance1"`
- `resources/AndroidManifest.xml:428`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.FragmentActivitySingleInstance2"`
- `resources/AndroidManifest.xml:434`
  `android:name="com.kwad.sdk.api.proxy.app.BaseFragmentActivity.DeveloperConfigActivity"`
- `resources/AndroidManifest.xml:438`
  `<service android:name="com.kwad.sdk.api.proxy.app.FileDownloadService.SharedMainProcessService"/>`
- `resources/AndroidManifest.xml:439`
  `<service android:name="com.kwad.sdk.api.proxy.app.FileDownloadService.SeparateProcessService"/>`
- `resources/AndroidManifest.xml:441`
  `android:name="com.kwad.sdk.api.proxy.app.DownloadService"`
- `resources/AndroidManifest.xml:444`
  `android:name="com.kwad.sdk.api.proxy.app.ServiceProxyRemote"`
- `resources/AndroidManifest.xml:448`
  `android:name="com.kwad.sdk.api.proxy.VideoWallpaperService"`
- `resources/AndroidManifest.xml:459`
  `android:name="com.kwad.sdk.api.proxy.app.AdSdkFileProvider"`
- `resources/res/layout/ad_gdt_group_pic.xml:2`
  `<com.qq.e.ads.nativ.widget.NativeAdContainer xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/ad_gdt_group_pic.xml:6`
  `</com.qq.e.ads.nativ.widget.NativeAdContainer>`
- `resources/res/layout/ad_gdt_large_pic.xml:2`
  `<com.qq.e.ads.nativ.widget.NativeAdContainer xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/ad_gdt_large_pic.xml:8`
  `</com.qq.e.ads.nativ.widget.NativeAdContainer>`
- `resources/res/layout/ad_gdt_large_video.xml:2`
  `<com.qq.e.ads.nativ.widget.NativeAdContainer xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/ad_gdt_large_video.xml:23`
  `<com.qq.e.ads.nativ.MediaView`
- `resources/res/layout/ad_gdt_large_video.xml:45`
  `</com.qq.e.ads.nativ.widget.NativeAdContainer>`
- `resources/res/layout/ad_gdt_small_pic.xml:2`
  `<com.qq.e.ads.nativ.widget.NativeAdContainer xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/ad_gdt_small_pic.xml:8`
  `</com.qq.e.ads.nativ.widget.NativeAdContainer>`
- `resources/res/layout/dcloud_draw_ad.xml:2`
  `<com.qq.e.ads.nativ.widget.NativeAdContainer xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/dcloud_draw_ad.xml:11`
  `<com.qq.e.ads.nativ.MediaView`
- `resources/res/layout/dcloud_draw_ad.xml:23`
  `</com.qq.e.ads.nativ.widget.NativeAdContainer>`
- `resources/res/layout/ksad_activity_active_webview.xml:44`
  `<com.kwad.sdk.core.webview.KsAdWebView`
- `resources/res/layout/ksad_activity_ad_land_page.xml:2`
  `<com.kwad.sdk.widget.KSRelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/ksad_activity_ad_land_page.xml:13`
  `<com.kwad.sdk.widget.KSRelativeLayout`
- `resources/res/layout/ksad_activity_ad_land_page.xml:18`
  `<com.kwad.components.core.video.DetailVideoView`
- `resources/res/layout/ksad_activity_ad_land_page.xml:32`
  `<com.kwad.components.core.widget.KsLogoView`
- `resources/res/layout/ksad_activity_ad_land_page.xml:40`
  `</com.kwad.sdk.widget.KSRelativeLayout>`
- `resources/res/layout/ksad_activity_ad_land_page.xml:50`
  `<com.kwad.sdk.core.webview.KsAdWebView`
- `resources/res/layout/ksad_activity_ad_land_page.xml:78`
  `</com.kwad.sdk.widget.KSRelativeLayout>`
- `resources/res/layout/ksad_activity_ad_video_webview.xml:27`
  `<com.kwad.sdk.widget.DownloadProgressBar`
- `resources/res/layout/ksad_activity_ad_webview.xml:62`
  `<com.kwad.sdk.core.webview.KsAdWebView`
- `resources/res/layout/ksad_activity_apk_info_landscape.xml:22`
  `<com.kwad.sdk.widget.KSRatingBar`
- `resources/res/layout/ksad_activity_apk_info_landscape.xml:36`
  `<com.kwad.components.ad.widget.KsAppTagsView`
- `resources/res/layout/ksad_activity_feedback.xml:125`
  `<com.kwad.lottie.LottieAnimationView`
- `resources/res/layout/ksad_activity_feed_download.xml:2`
  `<com.kwad.sdk.core.view.KsAdContainer xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/ksad_activity_feed_download.xml:9`
  `<com.kwad.components.ad.widget.tailframe.appbar.TailFrameBarAppPortraitVertical`
- `resources/res/layout/ksad_activity_feed_download.xml:13`
  `</com.kwad.sdk.core.view.KsAdContainer>`
- `resources/res/layout/ksad_activity_fullscreen_native.xml:2`
  `<com.kwad.sdk.core.view.AdBaseFrameLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/ksad_activity_fullscreen_native.xml:26`
  `<com.kwad.components.core.widget.KsLogoView`
- `resources/res/layout/ksad_activity_fullscreen_native.xml:47`
  `<com.kwad.components.ad.reward.widget.actionbar.ActionBarH5`
- `resources/res/layout/ksad_activity_fullscreen_native.xml:53`
  `<com.kwad.sdk.core.webview.KsAdWebView`
- `resources/res/layout/ksad_activity_fullscreen_native.xml:151`
  `<com.kwad.components.core.widget.ComplianceTextView`
- `resources/res/layout/ksad_activity_fullscreen_native.xml:162`
  `</com.kwad.sdk.core.view.AdBaseFrameLayout>`
- `resources/res/layout/ksad_activity_fullscreen_tk.xml:2`
  `<com.kwad.sdk.core.view.AdBaseFrameLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/ksad_activity_fullscreen_tk.xml:6`
  `<com.kwad.sdk.widget.KSFrameLayout`
- `resources/res/layout/ksad_activity_fullscreen_tk.xml:15`
  `<com.kwad.sdk.core.webview.KsAdWebView`
- `resources/res/layout/ksad_activity_fullscreen_tk.xml:20`
  `</com.kwad.sdk.core.view.AdBaseFrameLayout>`
- `resources/res/layout/ksad_activity_fullscreen_video_legacy.xml:2`
  `<com.kwad.sdk.core.view.AdBaseFrameLayout xmlns:android="http://schemas.android.com/apk/res/android"`

## BR041

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `sources/aegon/chrome/base/ApiCompatibilityUtils.java:40`
  `import com.umeng.analytics.pro.as;`
- `sources/aegon/chrome/net/X509Util.java:17`
  `import com.umeng.analytics.pro.cv;`
- `sources/androidx/constraintlayout/core/motion/key/MotionKeyAttributes.java:6`
  `import com.umeng.analytics.pro.cv;`
- `sources/androidx/constraintlayout/core/motion/key/MotionKeyCycle.java:10`
  `import com.umeng.analytics.pro.cv;`
- `sources/androidx/constraintlayout/core/state/WidgetFrame.java:15`
  `import com.umeng.analytics.pro.cv;`
- `sources/androidx/constraintlayout/motion/utils/ViewOscillator.java:9`
  `import com.umeng.analytics.pro.cv;`
- `sources/androidx/constraintlayout/motion/utils/ViewSpline.java:11`
  `import com.umeng.analytics.pro.cv;`
- `sources/androidx/constraintlayout/motion/widget/KeyAttributes.java:11`
  `import com.umeng.analytics.pro.cv;`
- `sources/androidx/constraintlayout/motion/widget/KeyCycle.java:14`
  `import com.umeng.analytics.pro.cv;`
- `sources/androidx/constraintlayout/motion/widget/KeyTimeCycle.java:13`
  `import com.umeng.analytics.pro.cv;`
- `sources/androidx/constraintlayout/motion/widget/MotionConstrainedPoint.java:11`
  `import com.umeng.analytics.pro.cv;`
- `sources/androidx/core/app/NotificationCompat.java:42`
  `import com.umeng.analytics.pro.d;`
- `sources/androidx/core/content/ContextCompat.java:83`
  `import com.umeng.analytics.pro.as;`
- `sources/androidx/core/content/ContextCompat.java:84`
  `import com.umeng.analytics.pro.bg;`
- `sources/androidx/core/net/MailTo.java:72`
  `return this.a.get(com.umeng.ccg.a.a);`
- `sources/androidx/core/provider/FontProvider.java:22`
  `import com.umeng.analytics.pro.bk;`
- `sources/androidx/core/text/BidiFormatter.java:4`
  `import com.umeng.analytics.pro.cv;`
- `sources/androidx/cursoradapter/widget/CursorAdapter.java:16`
  `import com.umeng.analytics.pro.bk;`
- `sources/androidx/dynamicanimation/animation/DynamicAnimation.java:14`
  `import com.umeng.analytics.pro.bg;`
- `sources/androidx/exifinterface/media/ExifInterface.java:21`
  `import com.umeng.analytics.pro.cv;`
- `sources/androidx/exifinterface/media/ExifInterface.java:22`
  `import com.umeng.commonsdk.stateless.b;`
- `sources/cn/jiguang/ag/a.java:14`
  `import com.umeng.analytics.pro.bg;`
- `sources/cn/jiguang/ag/a.java:15`
  `import com.umeng.analytics.pro.i;`
- `sources/cn/jiguang/ag/a.java:115`
  `bundle.putDouble(com.umeng.analytics.pro.d.C, d2);`
- `sources/cn/jiguang/ag/a.java:188`
  `jSONObject4.put(com.umeng.analytics.pro.d.C, bVar.c);`
- `sources/cn/jiguang/ag/a.java:189`
  `jSONObject4.put(com.umeng.analytics.pro.d.D, bVar.d);`
- `sources/cn/jiguang/ag/c.java:16`
  `import com.umeng.analytics.pro.i;`
- `sources/cn/jiguang/ai/f.java:16`
  `import com.umeng.analytics.pro.cv;`
- `sources/cn/jiguang/ai/h.java:14`
  `import com.umeng.analytics.pro.bg;`
- `sources/cn/jiguang/am/a.java:48`
  `jSONObject.put(com.umeng.ccg.a.o, jSONObject2);`
- `sources/cn/jiguang/am/a.java:57`
  `jSONObject.put(com.umeng.ccg.a.o, jSONObject2);`
- `sources/cn/jiguang/an/a.java:31`
  `import com.umeng.analytics.pro.cv;`
- `sources/cn/jiguang/ao/c.java:138`
  `JSONObject jSONObjectA3 = a(com.umeng.analytics.pro.d.M, mapB.get(com.umeng.analytics.pro.d.M).booleanValue());`
- `sources/cn/jiguang/ao/c.java:188`
  `map.put(com.umeng.analytics.pro.d.M, Boolean.valueOf(z));`
- `sources/cn/jiguang/ar/b.java:9`
  `import com.umeng.analytics.pro.cv;`
- `sources/cn/jiguang/ar/c.java:17`
  `import com.umeng.analytics.pro.bg;`
- `sources/cn/jiguang/ar/e.java:9`
  `import com.umeng.analytics.pro.cv;`
- `sources/cn/jiguang/as/a.java:8`
  `import com.umeng.analytics.pro.cv;`
- `sources/cn/jiguang/as/c.java:9`
  `import com.umeng.analytics.pro.cv;`
- `sources/cn/jiguang/at/b.java:6`
  `import com.umeng.analytics.pro.bg;`
- `sources/cn/jiguang/aw/c.java:5`
  `import com.umeng.analytics.pro.cv;`
- `sources/cn/jiguang/aw/e.java:5`
  `import com.umeng.analytics.pro.cv;`
- `sources/cn/jiguang/aw/j.java:4`
  `import com.umeng.analytics.pro.cv;`
- `sources/cn/jiguang/ax/b.java:5`
  `import com.umeng.analytics.pro.bg;`
- `sources/cn/jiguang/ax/h.java:9`
  `import com.umeng.analytics.pro.cv;`
- `sources/cn/jiguang/ax/i.java:11`
  `import com.umeng.analytics.pro.cv;`
- `sources/cn/jiguang/ax/j.java:6`
  `import com.umeng.analytics.pro.cv;`
- `sources/cn/jiguang/ay/b.java:17`
  `import com.umeng.analytics.pro.cv;`
- `sources/cn/jiguang/b/a.java:11`
  `import com.umeng.analytics.pro.d;`
- `sources/cn/jiguang/b/b.java:9`
  `import com.umeng.analytics.pro.bg;`
- `sources/cn/jiguang/ba/a.java:7`
  `import com.umeng.analytics.pro.cv;`
- `sources/cn/jiguang/ba/a.java:91`
  `if (str.equals(com.umeng.analytics.pro.d.L)) {`
- `sources/cn/jiguang/ba/a.java:155`
  `return com.umeng.analytics.pro.d.L;`
- `sources/cn/jiguang/ba/e.java:193`
  `double d4 = bundle.getDouble(com.umeng.analytics.pro.d.C);`
- `sources/cn/jiguang/ba/e.java:206`
  `jSONObject.put(com.umeng.analytics.pro.d.C, d3);`
- `sources/cn/jiguang/ba/e.java:207`
  `jSONObject.put(com.umeng.analytics.pro.d.D, d2);`
- `sources/cn/jiguang/ba/e.java:213`
  `jSONObject.put(com.umeng.analytics.pro.d.C, d3);`
- `sources/cn/jiguang/ba/e.java:214`
  `jSONObject.put(com.umeng.analytics.pro.d.D, d2);`
- `sources/cn/jiguang/ba/f.java:28`
  `import com.umeng.analytics.pro.bg;`
- `sources/cn/jiguang/ba/f.java:29`
  `import com.umeng.analytics.pro.cv;`
- `sources/cn/jiguang/bc/a.java:9`
  `import com.umeng.analytics.pro.cv;`
- `sources/cn/jiguang/bd/c.java:18`
  `import com.umeng.analytics.pro.cv;`
- `sources/cn/jiguang/bd/c.java:89`
  `jSONObject.put(com.umeng.analytics.pro.d.C, bundle.getDouble(com.umeng.analytics.pro.d.C, 200.0d));`
- `sources/cn/jiguang/bd/c.java:90`
  `jSONObject.put(com.umeng.analytics.pro.d.D, bundle.getDouble("lot", 200.0d));`
- `sources/cn/jiguang/bd/k.java:50`
  `d3 = bundle.getDouble(com.umeng.analytics.pro.d.C);`
- `sources/cn/jiguang/bd/k.java:130`
  `mVar.f2301h = bundle.getDouble(com.umeng.analytics.pro.d.C);`
- `sources/cn/jiguang/bd/m.java:45`
  `mVar.f2301h = jSONObject.optDouble(com.umeng.analytics.pro.d.C);`
- `sources/cn/jiguang/bd/m.java:46`
  `mVar.f2302i = jSONObject.optDouble(com.umeng.analytics.pro.d.D);`
- `sources/cn/jiguang/bd/m.java:90`
  `jSONObject.put(com.umeng.analytics.pro.d.C, this.f2301h);`
- `sources/cn/jiguang/bd/m.java:91`
  `jSONObject.put(com.umeng.analytics.pro.d.D, this.f2302i);`
- `sources/cn/jiguang/bd/n.java:68`
  `jSONObject.put(com.umeng.analytics.pro.d.C, this.f);`
- `sources/cn/jiguang/bd/n.java:69`
  `jSONObject.put(com.umeng.analytics.pro.d.D, this.g);`
- `sources/cn/jiguang/be/n.java:3`
  `import com.umeng.analytics.pro.bg;`
- `sources/cn/jiguang/bl/d.java:10`
  `import com.umeng.analytics.pro.as;`
- `sources/cn/jiguang/bl/d.java:151`
  `jSONObject.put(com.umeng.ccg.a.o, cn.jiguang.br.c.a());`
- `sources/cn/jiguang/bl/h.java:41`
  `jSONObject3.put("sentry_envelope_item_header", d.a(com.umeng.analytics.pro.d.aw));`
- `sources/cn/jiguang/bl/h.java:94`
  `jSONObject2.put("sentry_envelope_item_header", d.a(com.umeng.analytics.pro.d.aw));`
- `sources/cn/jiguang/bl/i.java:15`
  `import com.umeng.analytics.pro.cv;`
- `sources/cn/jiguang/bq/k.java:8`
  `import com.umeng.analytics.pro.bg;`
- `sources/cn/jiguang/br/b.java:9`
  `import com.umeng.analytics.pro.cv;`

## BR042

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `resources/AndroidManifest.xml:103`
  `<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>`
- `sources/cn/jiguang/bl/d.java:341`
  `jSONObject.put(CrashHianalyticsData.THREAD_ID, dVar.d());`
- `sources/com/huawei/hms/ads/identifier/AdvertisingIdClient.java:18`
  `public class AdvertisingIdClient {`
- `sources/com/huawei/hms/ads/identifier/AdvertisingIdClient.java:19`
  `private static final String SETTINGS_AD_ID = "pps_oaid";`
- `sources/com/huawei/hms/framework/common/hianalytics/CrashHianalyticsData.java:14`
  `public static final String THREAD_ID = "thread_id";`
- `sources/com/huawei/hms/framework/common/hianalytics/CrashHianalyticsData.java:23`
  `put(THREAD_ID, "" + Process.myTid());`
- `sources/com/kwad/components/ad/splashscreen/SplashPreloadManager.java:87`
  `this.Ei = context.getSharedPreferences("ksadsdk_splash_preload_id_list", 0);`
- `sources/com/kwad/sdk/i.java:13`
  `public static List<String> bjY = Arrays.asList("ksadsdk_pref", "ksadsdk_reward_reflow_config", "ksadsdk_rep", "ksadsdk_seq", "ksadsdk_mplogseq", "ksadsdk_splash_preload_id_list", "ksadsdk_notification_download_complete", "ksadsdk_download_package_md5", "ksadsdk_download_package_length", "ksadsdk_api...`
- `sources/com/kwad/sdk/core/network/idc/b.java:20`
  `return com.kwad.sdk.core.network.idc.a.b.fv(h.Y(context, "ksad_idc.json"));`
- `sources/com/kwad/sdk/utils/y.java:33`
  `if ("ksadsdk_splash_preload_id_list".equals(str) && (sharedPreferencesIv = bi.iv(str)) == null) {`
- `sources/com/kwad/sdk/utils/y.java:61`
  `if ("ksadsdk_splash_preload_id_list".equals(str)) {`
- `sources/io/dcloud/common/adapter/util/DownloadUtil.java:34`
  `sbD0.append(intent.getLongExtra("extra_download_id", 0L));`
- `sources/io/dcloud/h/a/d/b/c.java:29`
  `Method declaredMethod = Class.forName("com.google.android.gms.ads.identifier.AdvertisingIdClient").getDeclaredMethod("getAdvertisingIdInfo", Context.class);`
- `sources/org/mozilla/universalchardet/prober/distributionanalysis/Big5DistributionAnalysis.java:30`
  `public static final int[] e = {1, 1801, 1506, 255, 1431, 198, 9, 82, 6, ErrorCode.IMAGE_LOAD_ERROR, 177, 202, 3681, 1256, 2821, 110, 3814, 33, 3274, 261, 76, 44, 2114, 16, 2946, 2187, 1176, 659, 3971, 26, 3451, 2653, 1198, 3972, 3350, 4202, 410, 2215, 302, 590, 361, 1964, 8, AdEventType.VIDEO_PAUSE,...`

## BR043

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/cn/jiguang/ag/d.java:4`
  `import android.net.wifi.ScanResult;`
- `sources/cn/jiguang/ag/d.java:121`
  `List<ScanResult> scanResults = wifiManager.getScanResults();`
- `sources/cn/jiguang/ag/d.java:122`
  `if (scanResults != null && scanResults.size() != 0) {`
- `sources/cn/jiguang/ag/d.java:123`
  `f.c("JLocationWifi", "scan wifi list success:" + scanResults);`
- `sources/cn/jiguang/ag/d.java:124`
  `ArrayList<ScanResult> arrayList = new ArrayList(scanResults);`
- `sources/cn/jiguang/ag/d.java:125`
  `for (ScanResult scanResult : arrayList) {`
- `sources/cn/jiguang/ag/d.java:126`
  `if ((TextUtils.isEmpty(cVar.b) || !cVar.b.equals(v.b(scanResult.SSID)) || TextUtils.isEmpty(cVar.e) || !cVar.e.equals(scanResult.BSSID)) && scanResult.level >= -200) {`
- `sources/cn/jiguang/ag/d.java:127`
  `for (ScanResult scanResult2 : arrayList) {`
- `sources/cn/jiguang/ag/d.java:128`
  `if (scanResult2 != scanResult && scanResult.SSID.equals(scanResult2.SSID) && scanResult.BSSID.equals(scanResult2.BSSID)) {`
- `sources/cn/jiguang/ag/d.java:129`
  `scanResults.remove(scanResult);`
- `sources/cn/jiguang/ag/d.java:133`
  `scanResults.remove(scanResult);`
- `sources/cn/jiguang/ag/d.java:137`
  `Collections.sort(scanResults, new Comparator<ScanResult>() { // from class: cn.jiguang.ag.d.1`
- `sources/cn/jiguang/ag/d.java:140`
  `public int compare(ScanResult scanResult3, ScanResult scanResult4) {`
- `sources/cn/jiguang/ag/d.java:141`
  `return scanResult4.level - scanResult3.level;`
- `sources/cn/jiguang/ag/d.java:144`
  `for (int i2 = 0; i2 < scanResults.size(); i2++) {`
- `sources/cn/jiguang/ag/d.java:145`
  `ScanResult scanResult3 = scanResults.get(i2);`
- `sources/cn/jiguang/ag/d.java:146`
  `String strB = v.b(scanResult3.SSID);`
- `sources/cn/jiguang/ag/d.java:154`
  `cVar2.d = scanResult3.level;`
- `sources/cn/jiguang/ag/d.java:155`
  `cVar2.e = scanResult3.BSSID;`
- `sources/cn/jiguang/ai/h.java:6`
  `import android.net.wifi.ScanResult;`
- `sources/cn/jiguang/ai/h.java:49`
  `private String a(ScanResult scanResult, boolean z) {`
- `sources/cn/jiguang/ai/h.java:51`
  `long jCurrentTimeMillis = System.currentTimeMillis() - (((SystemClock.elapsedRealtimeNanos() / 1000) / 1000) - ((scanResult != null ? scanResult.timestamp : 0L) / 1000));`
- `sources/cn/jiguang/ai/h.java:53`
  `if (scanResult != null) {`
- `sources/cn/jiguang/ai/h.java:54`
  `String strReplace = scanResult.SSID.replace(HiAnalyticsConstant.REPORT_VAL_SEPARATOR, "").replace("#", "").replace(",", "");`
- `sources/cn/jiguang/ai/h.java:55`
  `String str2 = scanResult.BSSID;`
- `sources/cn/jiguang/ai/h.java:58`
  `sbI0.append(scanResult.BSSID);`
- `sources/cn/jiguang/ai/h.java:60`
  `sbI0.append(scanResult.level);`
- `sources/cn/jiguang/ai/h.java:62`
  `sbI0.append(scanResult.capabilities);`
- `sources/cn/jiguang/ai/h.java:153`
  `private String b(List<ScanResult> list) {`
- `sources/cn/jiguang/ai/h.java:224`
  `public void a(List<ScanResult> list) {`
- `sources/cn/jiguang/ai/j.java:4`
  `import android.net.wifi.ScanResult;`
- `sources/cn/jiguang/ai/j.java:19`
  `private Comparator<ScanResult> d;`
- `sources/cn/jiguang/ai/j.java:22`
  `private List<ScanResult> g;`
- `sources/cn/jiguang/ai/j.java:44`
  `public static class b implements Comparator<ScanResult> {`
- `sources/cn/jiguang/ai/j.java:50`
  `public int compare(ScanResult scanResult, ScanResult scanResult2) {`
- `sources/cn/jiguang/ai/j.java:51`
  `return scanResult2.level - scanResult.level;`
- `sources/cn/jiguang/ai/j.java:60`
  `private void b(List<ScanResult> list) {`
- `sources/cn/jiguang/ai/j.java:68`
  `ScanResult scanResult = list.get(i3);`
- `sources/cn/jiguang/ai/j.java:69`
  `if (scanResult != null) {`
- `sources/cn/jiguang/ai/j.java:70`
  `long j2 = Long.parseLong(scanResult.BSSID.replaceAll(Constants.COLON_SEPARATOR, ""), 16);`
- `sources/cn/jiguang/ai/j.java:71`
  `if (j2 != 0 && scanResult.level > e.f2232h && !arrayList.contains(Long.valueOf(j2))) {`
- `sources/cn/jiguang/ai/j.java:76`
  `this.g.add(scanResult);`
- `sources/cn/jiguang/ai/j.java:128`
  `public Comparator<ScanResult> a() {`
- `sources/cn/jiguang/ai/j.java:184`
  `b(this.f2238h.getScanResults());`
- `sources/com/hybirdlib/hybirdlib/SdkPluginUtils.java:944`
  `int iStartScan = XsBluetoothManager.instance.startScan();`
- `sources/com/hybirdlib/hybirdlib/WifiUtil.java:4`
  `import android.net.wifi.ScanResult;`
- `sources/com/hybirdlib/hybirdlib/WifiUtil.java:30`
  `for (ScanResult scanResult : wifiManager.getScanResults()) {`
- `sources/com/hybirdlib/hybirdlib/WifiUtil.java:31`
  `if (!arrayList.contains(scanResult.SSID)) {`
- `sources/com/hybirdlib/hybirdlib/WifiUtil.java:32`
  `arrayList.add(scanResult.SSID);`
- `sources/com/kwad/sdk/utils/bx.java:4`
  `import android.net.wifi.ScanResult;`
- `sources/com/kwad/sdk/utils/bx.java:62`
  `List<ScanResult> scanResults = wifiManager.getScanResults();`
- `sources/com/kwad/sdk/utils/bx.java:63`
  `if (scanResults != null) {`
- `sources/com/kwad/sdk/utils/bx.java:64`
  `for (ScanResult scanResult : scanResults) {`
- `sources/com/kwad/sdk/utils/bx.java:66`
  `aVar.ceU = scanResult.SSID;`
- `sources/com/kwad/sdk/utils/bx.java:67`
  `aVar.ceV = scanResult.BSSID;`
- `sources/com/kwad/sdk/utils/bx.java:68`
  `aVar.level = scanResult.level;`
- `sources/com/kwad/sdk/utils/bx.java:69`
  `if (connectionInfo.getBSSID() == null || scanResult.BSSID == null || !TextUtils.equals(connectionInfo.getBSSID().replace(JSUtil.QUOTE, ""), scanResult.BSSID.replace(JSUtil.QUOTE, "")) || connectionInfo.getSSID() == null || scanResult.SSID == null || !TextUtils.equals(connectionInfo.getSSID().replace...`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:4`
  `import android.bluetooth.le.ScanResult;`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:47`
  `public DCBluetoothDevice(ScanResult scanResult) {`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:48`
  `setMac(scanResult.getDevice().getAddress());`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:49`
  `setName(PdrUtil.isEmpty(scanResult.getDevice().getName()) ? "" : scanResult.getDevice().getName());`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:50`
  `setRSSI(scanResult.getRssi());`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:51`
  `SparseArray<byte[]> manufacturerSpecificData = scanResult.getScanRecord().getManufacturerSpecificData();`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:55`
  `setLocalName(PdrUtil.isEmpty(scanResult.getScanRecord().getDeviceName()) ? "" : scanResult.getScanRecord().getDeviceName());`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:57`
  `setServiceData(map2Str(scanResult.getScanRecord().getServiceData()));`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:58`
  `setAdvertisServiceUUIDs(list2Str(scanResult.getScanRecord().getServiceUuids()));`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothScanBALANCED.java:5`
  `import android.bluetooth.le.BluetoothLeScanner;`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothScanBALANCED.java:8`
  `import android.bluetooth.le.ScanResult;`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothScanBALANCED.java:36`
  `public BluetoothLeScanner leScanner;`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothScanBALANCED.java:58`
  `public void onScanResult(int i2, ScanResult scanResult) {`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothScanBALANCED.java:59`
  `super.onScanResult(i2, scanResult);`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothScanBALANCED.java:60`
  `BluetoothScanBALANCED.this.mHandler.sendMessage(Message.obtain(BluetoothScanBALANCED.this.mHandler, 0, new BleData(scanResult.getDevice(), scanResult.getRssi(), scanResult.getScanRecord().getBytes())));`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothScanBALANCED.java:106`
  `BluetoothLeScanner bluetoothLeScanner = this.leScanner;`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothScanBALANCED.java:107`
  `if (bluetoothLeScanner != null) {`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothScanBALANCED.java:108`
  `bluetoothLeScanner.startScan((List<ScanFilter>) null, scanSettingsBuild, this.m21ScanCallback);`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothScanBALANCED.java:162`
  `this.leScanner = defaultAdapter.getBluetoothLeScanner();`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothScanBALANCED.java:216`
  `BluetoothLeScanner bluetoothLeScanner = this.leScanner;`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothScanBALANCED.java:217`
  `if (bluetoothLeScanner != null) {`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothScanBALANCED.java:218`
  `bluetoothLeScanner.stopScan(this.m21ScanCallback);`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothScanDefault.java:5`
  `import android.bluetooth.le.BluetoothLeScanner;`

## BR044

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/aegon/chrome/net/AndroidNetworkLibrary.java:21`
  `import android.net.wifi.WifiManager;`
- `sources/aegon/chrome/net/AndroidNetworkLibrary.java:304`
  `if (intentRegisterReceiver != null && (intExtra = intentRegisterReceiver.getIntExtra("newRssi", Integer.MIN_VALUE)) != Integer.MIN_VALUE && (iCalculateSignalLevel = WifiManager.calculateSignalLevel(intExtra, i2)) >= 0 && iCalculateSignalLevel < i2) {`
- `sources/aegon/chrome/net/NetworkChangeNotifierAutoDetect.java:22`
  `import android.net.wifi.WifiManager;`
- `sources/aegon/chrome/net/NetworkChangeNotifierAutoDetect.java:52`
  `private WifiManagerDelegate mWifiManagerDelegate;`
- `sources/aegon/chrome/net/NetworkChangeNotifierAutoDetect.java:410`
  `return this.mConnectivityManagerDelegate.getNetworkState(this.mWifiManagerDelegate);`
- `sources/aegon/chrome/net/NetworkChangeNotifierAutoDetect.java:509`
  `public void setWifiManagerDelegateForTests(WifiManagerDelegate wifiManagerDelegate) {`
- `sources/aegon/chrome/net/NetworkChangeNotifierAutoDetect.java:510`
  `this.mWifiManagerDelegate = wifiManagerDelegate;`
- `sources/aegon/chrome/net/NetworkChangeNotifierAutoDetect.java:617`
  `public aegon.chrome.net.NetworkChangeNotifierAutoDetect.NetworkState getNetworkState(aegon.chrome.net.NetworkChangeNotifierAutoDetect.WifiManagerDelegate r17) {`
- `sources/aegon/chrome/net/NetworkChangeNotifierAutoDetect.java:708`
  `throw new UnsupportedOperationException("Method not decompiled: aegon.chrome.net.NetworkChangeNotifierAutoDetect.ConnectivityManagerDelegate.getNetworkState(aegon.chrome.net.NetworkChangeNotifierAutoDetect$WifiManagerDelegate):aegon.chrome.net.NetworkChangeNotifierAutoDetect$NetworkState");`
- `sources/aegon/chrome/net/NetworkChangeNotifierAutoDetect.java:782`
  `public static class WifiManagerDelegate {`
- `sources/aegon/chrome/net/NetworkChangeNotifierAutoDetect.java:794`
  `private WifiManager mWifiManager;`
- `sources/aegon/chrome/net/NetworkChangeNotifierAutoDetect.java:796`
  `public WifiManagerDelegate(Context context) {`
- `sources/aegon/chrome/net/NetworkChangeNotifierAutoDetect.java:805`
  `return this.mWifiManager.getConnectionInfo();`
- `sources/aegon/chrome/net/NetworkChangeNotifierAutoDetect.java:807`
  `return this.mWifiManager.getConnectionInfo();`
- `sources/aegon/chrome/net/NetworkChangeNotifierAutoDetect.java:815`
  `@SuppressLint({"WifiManagerPotentialLeak"})`
- `sources/aegon/chrome/net/NetworkChangeNotifierAutoDetect.java:822`
  `this.mWifiManager = z ? (WifiManager) this.mContext.getSystemService("wifi") : null;`
- `sources/aegon/chrome/net/NetworkChangeNotifierAutoDetect.java:840`
  `public WifiManagerDelegate() {`
- `sources/androidx/core/content/ContextCompat.java:43`
  `import android.net.wifi.WifiManager;`
- `sources/androidx/core/content/ContextCompat.java:279`
  `map.put(WifiManager.class, "wifi");`
- `sources/cn/jiguang/ag/d.java:6`
  `import android.net.wifi.WifiManager;`
- `sources/cn/jiguang/ag/d.java:27`
  `WifiManager wifiManager;`
- `sources/cn/jiguang/ag/d.java:29`
  `if (Build.VERSION.SDK_INT < 29 || !cn.jiguang.g.a.a().a(1608) || (wifiManager = (WifiManager) context.getApplicationContext().getSystemService("wifi")) == null) {`
- `sources/cn/jiguang/ag/d.java:35`
  `for (WifiConfiguration wifiConfiguration : wifiManager.getConfiguredNetworks()) {`
- `sources/cn/jiguang/ag/d.java:82`
  `WifiManager wifiManager = (WifiManager) context.getApplicationContext().getSystemService("wifi");`
- `sources/cn/jiguang/ag/d.java:83`
  `if (wifiManager == null || !wifiManager.isWifiEnabled()) {`
- `sources/cn/jiguang/ag/d.java:85`
  `f.i("JLocationWifi", "get wifiManager failed");`
- `sources/cn/jiguang/ag/d.java:121`
  `List<ScanResult> scanResults = wifiManager.getScanResults();`
- `sources/cn/jiguang/ai/j.java:5`
  `import android.net.wifi.WifiManager;`
- `sources/cn/jiguang/ai/j.java:25`
  `private WifiManager f2238h;`
- `sources/cn/jiguang/ai/j.java:107`
  `this.f2238h = (WifiManager) this.f2239i.getSystemService("wifi");`
- `sources/cn/jiguang/ai/j.java:184`
  `b(this.f2238h.getScanResults());`
- `sources/cn/jiguang/bv/a.java:29`
  `import android.net.wifi.WifiManager;`
- `sources/cn/jiguang/bv/a.java:154`
  `WifiManager wifiManager = (WifiManager) context.getApplicationContext().getSystemService("wifi");`
- `sources/cn/jiguang/bv/a.java:155`
  `if (wifiManager != null && p.a(context, com.kuaishou.weapon.p0.g.d)) {`
- `sources/cn/jiguang/bv/a.java:156`
  `this.f2375h = wifiManager.getConnectionInfo();`
- `sources/cn/jiguang/j/a.java:5`
  `import android.net.wifi.WifiManager;`
- `sources/cn/jiguang/j/a.java:75`
  `WifiManager wifiManager = (WifiManager) context.getApplicationContext().getSystemService("wifi");`
- `sources/cn/jiguang/j/a.java:76`
  `if (wifiManager == null) {`
- `sources/cn/jiguang/j/a.java:77`
  `f.c("JArp", "collect arp failed because get wifiManager failed");`
- `sources/cn/jiguang/j/a.java:86`
  `this.f = wifiManager.getDhcpInfo();`
- `sources/com/huawei/hms/framework/common/NetworkUtil.java:10`
  `import android.net.wifi.WifiManager;`
- `sources/com/huawei/hms/framework/common/NetworkUtil.java:645`
  `if (!(systemService instanceof WifiManager)) {`
- `sources/com/huawei/hms/framework/common/NetworkUtil.java:649`
  `int i2 = ((WifiManager) systemService).getDhcpInfo().gateway;`
- `sources/com/huawei/hms/framework/common/NetworkUtil.java:666`
  `if (!(systemService instanceof WifiManager)) {`
- `sources/com/huawei/hms/framework/common/NetworkUtil.java:670`
  `WifiInfo connectionInfo = ((WifiManager) systemService).getConnectionInfo();`
- `sources/com/huawei/hms/framework/common/NetworkUtil.java:686`
  `return WifiManager.calculateSignalLevel(getWifiRssi(context), 5);`
- `sources/com/hybirdlib/hybirdlib/ConnectedWifiUtil.java:5`
  `import android.net.wifi.WifiManager;`
- `sources/com/hybirdlib/hybirdlib/ConnectedWifiUtil.java:17`
  `WifiManager wifiManager = (WifiManager) context.getSystemService("wifi");`
- `sources/com/hybirdlib/hybirdlib/ConnectedWifiUtil.java:18`
  `if (wifiManager == null) {`
- `sources/com/hybirdlib/hybirdlib/ConnectedWifiUtil.java:19`
  `Log.e("ConnectedWifiUtil", "WifiManager is null");`
- `sources/com/hybirdlib/hybirdlib/ConnectedWifiUtil.java:26`
  `WifiInfo connectionInfo = wifiManager.getConnectionInfo();`
- `sources/com/hybirdlib/hybirdlib/WifiUtil.java:5`
  `import android.net.wifi.WifiManager;`
- `sources/com/hybirdlib/hybirdlib/WifiUtil.java:18`
  `WifiManager wifiManager = (WifiManager) context.getSystemService("wifi");`
- `sources/com/hybirdlib/hybirdlib/WifiUtil.java:19`
  `if (wifiManager == null) {`
- `sources/com/hybirdlib/hybirdlib/WifiUtil.java:20`
  `Log.e("WifiUtil", "WifiManager is null");`
- `sources/com/hybirdlib/hybirdlib/WifiUtil.java:27`
  `if (!wifiManager.isWifiEnabled()) {`
- `sources/com/hybirdlib/hybirdlib/WifiUtil.java:30`
  `for (ScanResult scanResult : wifiManager.getScanResults()) {`
- `sources/com/kwad/sdk/utils/bl.java:8`
  `import android.net.wifi.WifiManager;`
- `sources/com/kwad/sdk/utils/bl.java:626`
  `WifiInfo connectionInfo = ((WifiManager) context.getApplicationContext().getSystemService("wifi")).getConnectionInfo();`
- `sources/com/kwad/sdk/utils/bx.java:6`
  `import android.net.wifi.WifiManager;`
- `sources/com/kwad/sdk/utils/bx.java:47`
  `WifiManager wifiManager;`
- `sources/com/kwad/sdk/utils/bx.java:58`
  `if (ep(context) || (wifiManager = (WifiManager) context.getApplicationContext().getSystemService("wifi")) == null) {`
- `sources/com/kwad/sdk/utils/bx.java:61`
  `WifiInfo connectionInfo = wifiManager.getConnectionInfo();`
- `sources/com/kwad/sdk/utils/bx.java:62`
  `List<ScanResult> scanResults = wifiManager.getScanResults();`
- `sources/com/kwai/library/ipneigh/c.java:4`
  `import android.net.wifi.WifiManager;`
- `sources/com/kwai/library/ipneigh/c.java:15`
  `String strHj = b.hj(((WifiManager) context.getApplicationContext().getSystemService("wifi")).getDhcpInfo().gateway);`
- `sources/com/kwai/video/ksvodplayerkit/Utils/NetworkUtils.java:8`
  `import android.net.wifi.WifiManager;`
- `sources/com/kwai/video/ksvodplayerkit/Utils/NetworkUtils.java:64`
  `WifiManager wifiManager = (WifiManager) context.getApplicationContext().getSystemService("wifi");`
- `sources/com/kwai/video/ksvodplayerkit/Utils/NetworkUtils.java:65`
  `if (wifiManager == null) {`
- `sources/com/kwai/video/ksvodplayerkit/Utils/NetworkUtils.java:69`
  `return wifiManager.getConnectionInfo();`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:14`
  `import android.net.wifi.WifiManager;`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:904`
  `WifiManager wifiManager = (WifiManager) context.getSystemService("wifi");`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:910`
  `} else if (wifiManager != null) {`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:911`
  `sWifiMac = wifiManager.getConnectionInfo().getMacAddress();`
- `sources/com/umeng/commonsdk/utils/UMUtils.java:17`
  `import android.net.wifi.WifiManager;`
- `sources/com/umeng/commonsdk/utils/UMUtils.java:769`
  `WifiManager wifiManager = (WifiManager) context.getSystemService("wifi");`
- `sources/com/umeng/commonsdk/utils/UMUtils.java:770`
  `if (wifiManager == null) {`
- `sources/com/umeng/commonsdk/utils/UMUtils.java:774`
  `return wifiManager.getConnectionInfo().getMacAddress();`
- `sources/io/dcloud/common/adapter/util/DeviceInfo.java:12`
  `import android.net.wifi.WifiManager;`
- `sources/io/dcloud/common/adapter/util/DeviceInfo.java:684`
  `return ((WifiManager) context.getApplicationContext().getSystemService("wifi")).getWifiState() == 3;`

## BR047

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/aegon/chrome/base/AnimationFrameTimeHistogram.java:60`
  `android.util.Log.w(AnimationFrameTimeHistogram.TAG, "Animation frame time recording reached the maximum number. It's eitherthe animation took too long or recording end is not called.");`
- `sources/aegon/chrome/base/ApkAssets.java:38`
  `android.util.Log.e(LOGTAG, "Error while loading asset " + str + ": " + e3);`
- `sources/aegon/chrome/base/task/AsyncTask.java:44`
  `Log.w(AsyncTask.TAG, e.toString(), new Object[0]);`
- `sources/aegon/chrome/net/X509Util.java:317`
  `Log.w(TAG, "intermediate " + i2 + " failed parsing");`
- `sources/aegon/chrome/net/X509Util.java:337`
  `Log.i(TAG, "Failed to validate the certificate chain, error: " + e.getMessage());`
- `sources/aegon/chrome/net/impl/CronetBidirectionalStream.java:207`
  `Log.i(CronetUrlRequestContext.LOG_TAG, "destroyNativeStreamLocked " + toString(), new Object[0]);`
- `sources/aegon/chrome/net/impl/CronetBidirectionalStream.java:248`
  `Log.e(CronetUrlRequestContext.LOG_TAG, "Exception notifying of failed request", e);`
- `sources/aegon/chrome/net/impl/CronetBidirectionalStream.java:280`
  `Log.e(CronetUrlRequestContext.LOG_TAG, "Exception in onSucceeded method", e);`
- `sources/aegon/chrome/net/impl/CronetBidirectionalStream.java:306`
  `Log.e(CronetUrlRequestContext.LOG_TAG, "Exception in CalledByNative method", exc);`
- `sources/aegon/chrome/net/impl/CronetBidirectionalStream.java:320`
  `Log.e(CronetUrlRequestContext.LOG_TAG, "Exception in onCanceled method", e);`
- `sources/aegon/chrome/net/impl/CronetBidirectionalStream.java:476`
  `Log.e(CronetUrlRequestContext.LOG_TAG, "Exception posting task to executor", e);`
- `sources/aegon/chrome/net/impl/CronetUploadDataStream.java:168`
  `Log.e(TAG, "Failure closing data provider", e);`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:205`
  `Log.e(CronetUrlRequestContext.LOG_TAG, a.x("Unknown error code: ", i2), new Object[0]);`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:226`
  `Log.e(CronetUrlRequestContext.LOG_TAG, "Exception posting task to executor", e);`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:258`
  `Log.e(CronetUrlRequestContext.LOG_TAG, "Exception in CalledByNative method", exc);`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:273`
  `Log.e(CronetUrlRequestContext.LOG_TAG, "Exception in onCanceled method", e);`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:322`
  `Log.e(CronetUrlRequestContext.LOG_TAG, "Exception in onFailed method", e);`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:327`
  `Log.e(CronetUrlRequestContext.LOG_TAG, "Exception posting task to executor", e);`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:422`
  `Log.e(CronetUrlRequestContext.LOG_TAG, "Exception in onSucceeded method", e);`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:433`
  `Log.e(CronetUrlRequestContext.LOG_TAG, "Exception posting task to executor", e);`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:527`
  `Log.e(CronetUrlRequestContext.LOG_TAG, "Exception in upload method", th);`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:110`
  `Log.e(JavaUrlRequest.TAG, "Exception in onCanceled method", e);`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:125`
  `Log.e(JavaUrlRequest.TAG, "Exception in onFailed method", e);`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:183`
  `Log.e(JavaUrlRequest.TAG, "Exception in onSucceeded method", e);`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:622`
  `Log.e(JavaUrlRequest.TAG, "Exception when closing OutputChannel", e);`
- `sources/aegon/chrome/net/impl/UrlRequestBuilderImpl.java:96`
  `Log.w(TAG, "It's not necessary to set Accept-Encoding on requests - cronet will do this automatically for you, and setting it yourself has no effect. See https://crbug.com/581399 for details.", new Exception());`
- `sources/aegon/chrome/net/urlconnection/CronetHttpURLConnection.java:381`
  `Log.d(TAG, "Outputstream is being buffered in memory.");`
- `sources/androidtranscoder/engine/OutputSurface.java:42`
  `Log.e("TextureRender", "Could not create program");`
- `sources/androidtranscoder/engine/QueuedMuxer.java:122`
  `Log.v("QueuedMuxer", "Output format determined, writing " + this.f1049h.size() + " samples / " + this.g.limit() + " bytes to muxer.");`
- `sources/androidtranscoder/engine/TextureRender.java:59`
  `Log.e("TextureRender", "Could not compile shader " + i2 + Constants.COLON_SEPARATOR);`
- `sources/androidx/activity/result/ActivityResultRegistry.java:81`
  `Log.w("ActivityResultRegistry", sbK0.toString());`
- `sources/androidx/activity/result/ActivityResultRegistry.java:87`
  `Log.w("ActivityResultRegistry", sbK02.toString());`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1518`
  `Log.i("AppCompatDelegate", "The Activity's LayoutInflater already has a Factory installed so we can not install AppCompat's");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2297`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2303`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR_OVERLAY id when requesting this feature.");`
- `sources/androidx/appcompat/app/ResourcesFlusher.java:54`
  `Log.e("ResourcesFlusher", "Could not retrieve value from ThemedResourceCache#mUnthemedEntries", e4);`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:134`
  `Log.w("SupportMenuInflater", "Cannot instantiate class: " + str, e);`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:183`
  `Log.w("SupportMenuInflater", "Ignoring attribute 'itemActionViewLayout'. Action view already specified.");`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:254`
  `Log.w("SupportMenuInflater", "Ignoring attribute 'actionProviderClass'. Action view already specified.");`
- `sources/androidx/appcompat/widget/AppCompatEditText.java:120`
  `Log.w("ReceiveContent", "Can't insert content from IME; requestPermission() failed", e);`

## BR050

paper_id: B021
paper_title: Metadata-Based Privacy Assessment for Mobile mHealth

- `database/snapshots/P002-usenix-supor.html:616`
  `<iframe title="YouTube video" class="large-12 medium-12 small-12 columns usenix-schedule-media" width="745" height="420" src="//www.youtube.com/embed/xFMggMuh5Wc?width%3D745%26amp%3Bheight%3D420%26amp%3Btheme%3Ddark%26amp%3Bautoplay%3D0%26amp%3Bvq%3Dhd720%26amp%3Brel%3D0%26amp%3Bshowinfo%3D0%26amp%3...`
- `database/snapshots/P003-ndss-content-leaks.html:434`
  `<p class="has-text-align-center"><a href="https://www.ndss-symposium.org/privacy-policy/">Privacy Policy</a> | <a href="https://www.ndss-symposium.org/terms-of-use/">Terms of Use</a> <span class="hide-on-mobile">|</span> <a href="https://www.ndss-symposium.org/ndss-code-of-conduct/">NDSS Code of Con...`
- `database/snapshots/P004-ndss-execute-this.html:404`
  `<p class="has-text-align-center"><a href="https://www.ndss-symposium.org/privacy-policy/">Privacy Policy</a> | <a href="https://www.ndss-symposium.org/terms-of-use/">Terms of Use</a> <span class="hide-on-mobile">|</span> <a href="https://www.ndss-symposium.org/ndss-code-of-conduct/">NDSS Code of Con...`
- `database/snapshots/P005-ndss-appsealer.html:404`
  `<p class="has-text-align-center"><a href="https://www.ndss-symposium.org/privacy-policy/">Privacy Policy</a> | <a href="https://www.ndss-symposium.org/terms-of-use/">Terms of Use</a> <span class="hide-on-mobile">|</span> <a href="https://www.ndss-symposium.org/ndss-code-of-conduct/">NDSS Code of Con...`
- `database/snapshots/P006-teamusec-android-ssl.html:483`
  `<a class="text-link" href="https://www.uni-hannover.de/en/datenschutzerklaerung/">Privacy Policy</a>`
- `database/snapshots/P007-usenix-deep-links.html:223`
  `<iframe title="YouTube video" class="large-12 medium-12 small-12 columns usenix-schedule-media" width="745" height="420" src="//www.youtube.com/embed/Ndnv7SIgMhY?width%3D745%26amp%3Bheight%3D420%26amp%3Btheme%3Ddark%26amp%3Bautoplay%3D0%26amp%3Bvq%3Dhd720%26amp%3Brel%3D0%26amp%3Bshowinfo%3D0%26amp%3...`
- `database/snapshots/P008-usenix-webview-dcv.html:412`
  `<iframe title="YouTube video" class="large-12 medium-12 small-12 columns usenix-schedule-media" width="745" height="420" src="//www.youtube.com/embed/tgr7Y33jdZY?width%3D745%26amp%3Bheight%3D420%26amp%3Btheme%3Ddark%26amp%3Bautoplay%3D0%26amp%3Bvq%3Dhd720%26amp%3Brel%3D0%26amp%3Bshowinfo%3D0%26amp%3...`
- `database/snapshots/P009-ndss-webview-tracking.html:497`
  `<p class="has-text-align-center"><a href="https://www.ndss-symposium.org/privacy-policy/">Privacy Policy</a> | <a href="https://www.ndss-symposium.org/terms-of-use/">Terms of Use</a> <span class="hide-on-mobile">|</span> <a href="https://www.ndss-symposium.org/ndss-code-of-conduct/">NDSS Code of Con...`
- `database/snapshots/P010-usenix-policylint.html:8`
  `<meta name="citation_title" content="{PolicyLint}: Investigating Internal Privacy Policy Contradictions on Google Play" />`
- `database/snapshots/P010-usenix-policylint.html:39`
  `<title>PolicyLint: Investigating Internal Privacy Policy Contradictions on Google Play | USENIX</title>`
- `database/snapshots/P010-usenix-policylint.html:477`
  `<iframe title="YouTube video" class="large-12 medium-12 small-12 columns usenix-schedule-media" width="745" height="420" src="//www.youtube.com/embed/ORY2YSr1VNI?width%3D745%26amp%3Bheight%3D420%26amp%3Btheme%3Ddark%26amp%3Bautoplay%3D0%26amp%3Bvq%3Dhd720%26amp%3Brel%3D0%26amp%3Bshowinfo%3D0%26amp%3...`
- `database/snapshots/P011-soups-consent-tracking.html:31`
  `<meta name="citation_conference_title" content="Seventeenth Symposium on Usable Privacy and Security (SOUPS 2021)" />`
- `database/snapshots/P011-soups-consent-tracking.html:442`
  `booktitle = {Seventeenth Symposium on Usable Privacy and Security (SOUPS 2021)},<br />`
- `database/snapshots/P011-soups-consent-tracking.html:453`
  `<iframe title="YouTube video" class="large-12 medium-12 small-12 columns usenix-schedule-media" width="745" height="420" src="//www.youtube.com/embed/4vTsPl9BncA?width%3D745%26amp%3Bheight%3D420%26amp%3Btheme%3Ddark%26amp%3Bautoplay%3D0%26amp%3Bvq%3Dhd720%26amp%3Brel%3D0%26amp%3Bshowinfo%3D0%26amp%3...`
- `database/snapshots/P012-ndss-inconpreter.html:496`
  `<p class="has-text-align-center"><a href="https://www.ndss-symposium.org/privacy-policy/">Privacy Policy</a> | <a href="https://www.ndss-symposium.org/terms-of-use/">Terms of Use</a> <span class="hide-on-mobile">|</span> <a href="https://www.ndss-symposium.org/ndss-code-of-conduct/">NDSS Code of Con...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:114`
  `<meta name="description" content="Mobile Health (mHealth) applications lie outside of regulatory protection such as HIPAA, which requires a baseline of privacy and security protections appropriate to sensitive medical data. However, mHealth apps, particularly those in the app stores ...">`
- `database/snapshots/P013-pmc-android-mhealth-security.html:118`
  `<meta name="og:description" content="Mobile Health (mHealth) applications lie outside of regulatory protection such as HIPAA, which requires a baseline of privacy and security protections appropriate to sensitive medical data. However, mHealth apps, particularly those in the app stores ...">`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1389`
  `<p>Mobile Health (mHealth) applications lie outside of regulatory protection such as HIPAA, which requires a baseline of privacy and security protections appropriate to sensitive medical data. However, mHealth apps, particularly those in the app stores for iOS and Android, are increasingly handling ...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1554`
  `<p>When used as intended, a variety of sensitive user data are collected, stored, and transmitted through these Android mHealth apps. <a href="#f6-1969977" class="usa-link">Figure 6</a> shows the distribution of sensitive information in the 22 apps (x axis means the number of appearances of sensitiv...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1561`
  `<p>The increased use of mHealth results in greater risks to health-related information on mobile devices. Developers and healthcare service providers would be wise to make efforts to ensure that mHealth apps facilitate security compliance even if they are not legally required to do so (at the curren...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1564`
  `<p>We observed that many apps may ask users to share their private health information by providing privacy policy agreed by users themselves. In our study, most of the apps do make privacy policies available to users either via an URL link in the app or shown when the app is launched for the first t...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1565`
  `<p>A study of Android mHealth apps reveals common shortcomings in security and privacy when using communications and storage. Steps should be made to encourage mHealth app vendors to assure encrypted network links for communications and the use of third party storage only when adequate security and ...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1573`
  `<span class="label">3.</span><cite>Avancha S, Baxi A, Kotz D. Privacy in mobile technology for personal healthcare. ACM Computing Surveys (CSUR) 2012;45(1):3.</cite> [<a href="https://scholar.google.com/scholar_lookup?journal=ACM%20Computing%20Surveys%20(CSUR)&amp;title=Privacy%20in%20mobile%20techn...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1575`
  `<span class="label">4.</span><cite>Kotz D. A threat taxonomy for mHealth privacy; 2011 Third International Conference on Communication Systems and Networks (COMSNETS); 2011 Jan 4–8; Bangalore. </cite> [<a href="https://scholar.google.com/scholar_lookup?journal=A%20threat%20taxonomy%20for%20mHealth%2...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1581`
  `<span class="label">7.</span><cite>Prasad A, Sorber J, Stablein T, Anthony D, Kotz D. Understanding Sharing Preferences and Behavior for mHealth Devices; Proceedings of the 2012 ACM Workshop on Privacy in the Electronic Society (WPES); October 15; Raleigh, NC. New York, NY: ACM; 2012. pp. 117–128.</...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1636`
  `<span class="label">29.</span><cite>Dixon P.  Medical Identity Theft: The Information Crime that Can Kill You. 2006. May 3,  (World Privacy Forum).</cite> [<a href="https://scholar.google.com/scholar_lookup?title=Medical%20Identity%20Theft:%20The%20Information%20Crime%20that%20Can%20Kill%20You&amp;a...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:2298`
  `<a href="https://www.hhs.gov/vulnerability-disclosure-policy/index.html" class="usa-link usa-link--external usa-link--alt ncbi-footer__link" rel="noreferrer noopener" target='_blank' >`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:98`
  `<meta name="citation_title" content="Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment">`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:118`
  `<meta name="description" content="Poor information privacy practices have been identified in health apps. Medical app accreditation programs offer a mechanism for assuring the quality of apps; however, little is known about their ability to control information privacy risks. We ...">`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:119`
  `<meta name="og:title" content="Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment">`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:122`
  `<meta name="og:description" content="Poor information privacy practices have been identified in health apps. Medical app accreditation programs offer a mechanism for assuring the quality of apps; however, little is known about their ability to control information privacy risks. We ...">`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1363`
  `<hgroup><h1>Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment</h1></hgroup><div class="cg p">`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1432`
  `<p>Poor information privacy practices have been identified in health apps. Medical app accreditation programs offer a mechanism for assuring the quality of apps; however, little is known about their ability to control information privacy risks. We aimed to assess the extent to which already-certifie...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1438`
  `<p>Because users cannot see into the inner workings of apps, or the services they connect to, confidence that personal information is handled appropriately relies mostly on trust. Users must trust in the ethical operation of app services, that developers will comply with privacy regulation and secur...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1439`
  `<p>Medical app accreditation programs, in which apps are subject to formal assessment or peer review, are a recent development that aims to provide clinical assurances about quality and safety, foster trust, and promote app adoption by patients and professionals [<a href="#CR14" class="usa-link" ari...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1440`
  `<p>Launched in March 2013, the NHS Health Apps Library offers a curated list of apps for patient and public use. Apps are intended to be suitable for professional recommendation to patients but are also available for general use without clinical support. Registered apps undergo an appraisal process,...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1441`
  `<p>The purpose of the current study was to assess the extent to which accredited apps adhered to these principles. We reviewed all apps available from the NHS Health Apps Library at a particular point in time, and assessed compliance with recommended practice for information collection, transmission...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1444`
  `<p>Assessment involved a combination of manual testing and policy review. Testing was used to characterize app features, explore data collection and transmission behaviour, and identify adherence to data protection principles concerning information security. Policy review identified the extent to wh...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1445`
  `<p>Apps were subject to a 6-month period of evaluation, from August 2013 to January 2014. Testing incorporated two strategies. To ensure coverage of features relating to information collection and transmission, sequential exploration of all user interface elements was performed for each app. After t...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1454`
  `<p>Potential vulnerabilities in server-side controls were explored through manual testing. To identify potential authorization problems, we reset session state information and replayed intercepted data requests to see if developer or third-party systems would return user data without first requiring...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1455`
  `<p>We systematically assessed the content of privacy policies associated with each app. We searched in-app documentation, app store entries and related websites. All documents that self-identified as a privacy policy were included in analysis. We also located privacy-relevant text forming part of ot...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1456`
  `<p>Assessment proceeded by systematically coding each schema item as either being addressed or absent from extracted policy text. For those principles relating to user rights, such as the ability to opt-out of data collection, policies were additionally coded according to whether a given right was a...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1457`
  `<p>Coding decisions, as well as any relevant policy text annotations, were captured using custom software (see Additional file <a href="#MOESM1" class="usa-link">1</a>: Figure AF5). All decisions were reviewed to reach a consensus agreement on policy coverage. The nature of information actually coll...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1458`
  `<p>Data were compiled into a single dataset for analysis (supplied as Additional file <a href="#MOESM2" class="usa-link">2</a>). We used simple descriptive statistics to summarize aspects of data collection, mobile-device storage and transmission. Unless otherwise stated, the unit of analysis is the...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1459`
  `<p>We hypothesized that the likelihood of an app having a privacy policy should not vary by platform or by the distribution model (free or paid). Although apps for iOS are subject to a quality control process prior to release, and although developers of paid-for apps may have greater resources to in...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2090`
  `<span class="label">6.</span><cite>Kotz D.  Third International Conference on Communication Systems and Networks (COMSNETS), 4–8 January 2011. Bangalore: COMSNETS; 2011. A threat taxonomy for mHealth privacy; pp. 1–6.</cite> [<a href="https://scholar.google.com/scholar_lookup?title=Third%20Internati...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2092`
  `<span class="label">7.</span><cite>Cohn SP.  Privacy and confidentiality in the nationwide health information network. Washington: National Committee on Vital and Health Statistics; 2006. </cite> [<a href="https://scholar.google.com/scholar_lookup?title=Privacy%20and%20confidentiality%20in%20the%20n...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2094`
  `<span class="label">8.</span><cite>Smith HJ, Dinev T, Xu H. Information privacy research: an interdisciplinary review. MIS Q. 2011;35:989–1016.</cite> [<a href="https://scholar.google.com/scholar_lookup?journal=MIS%20Q.&amp;title=Information%20privacy%20research:%20an%20interdisciplinary%20review&am...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2096`
  `<span class="label">9.</span><cite>Njie L. Mobile health and fitness apps: what are the privacy risks? [<a href="https://www.privacyrights.org/mobile-health-and-fitness-apps-what-are-privacy-risks" class="usa-link usa-link--external" data-ga-action="click_feat_suppl" target="_blank" rel="noopener no...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2099`
  `<span class="label">10.</span><cite>Sunyaev A, Dehling T, Taylor PL, Mandl KD. Availability and quality of mobile health app privacy policies. J Am Med Inform Assoc. 2014;22:e28–33. doi: 10.1136/amiajnl-2013-002605.</cite> [<a href="https://doi.org/10.1136/amiajnl-2013-002605" class="usa-link usa-li...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2101`
  `<span class="label">11.</span><cite>Dehling T, Gao F, Schneider S, Sunyaev A. Exploring the far side of mobile health: information security and privacy of mobile health apps on iOS and Android. JMIR Mhealth Uhealth. 2015;3:e8. doi: 10.2196/mhealth.3672.</cite> [<a href="https://doi.org/10.2196/mheal...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2105`
  `<span class="label">13.</span><cite>Adhikari R, Richards D.  25th Australasian Conference on Information Systems, 8–10 December 2014. Auckland: Australasian Conference on Information Systems; 2014. Security and privacy issues related to the use of mobile health apps.</cite> [<a href="https://scholar...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2121`
  `<span class="label">19.</span><cite>LaRose R, Rifon N. Your privacy is assured - of being disturbed: websites with and without privacy seals. New Media &amp; Soc. 2006;8:1009–29. doi: 10.1177/1461444806069652.</cite> [<a href="https://doi.org/10.1177/1461444806069652" class="usa-link usa-link--exter...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2152`
  `<span class="label">30.</span><cite>Information Commissioner’s Office  . Privacy notices code of practice. Wilmslow: Information Commissioner’s Office; 2010. </cite> [<a href="https://scholar.google.com/scholar_lookup?title=Privacy%20notices%20code%20of%20practice&amp;publication_year=2010&amp;" cla...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2154`
  `<span class="label">31.</span><cite>Information Commissioner’s Office. Privacy in mobile apps – guidance for app developers [<a href="http://ico.org.uk/for_organisations/data_protection/topic_guides/online/~/media/documents/library/Data_Protection/Detailed_specialist_guides/privacy-in-mobile-apps-dp...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2166`
  `<span class="label">35.</span><cite>Agaku IT, Adisa AO, Ayo-Yusuf OA, Connolly GN. Concern about security and privacy, and perceived control over collection and use of health information are related to withholding of health information from healthcare providers. J Am Med Inform Assoc. 2014;21:374–8....`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2168`
  `<span class="label">36.</span><cite>King J.  Symposium on Usable Privacy and Security (SOUPS), 11–13 July 2012. Washington: SOUPS; 2012. “How come I’m allowing strangers to go through my phone?” – smartphones and privacy expectations.</cite> [<a href="https://scholar.google.com/scholar_lookup?title=...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2170`
  `<span class="label">37.</span><cite>Boyles JL, Smith A, Madden M. Privacy and data management on mobile devices [<a href="http://www.pewinternet.org/2012/09/05/privacy-and-data-management-on-mobile-devices/" class="usa-link usa-link--external" data-ga-action="click_feat_suppl" target="_blank" rel="n...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2173`
  `<span class="label">38.</span><cite>Shklovski I, Mainwaring SD, Skúladóttir HH, Borgthorsson H.  32nd annual ACM CHI Conference on Human Factors in Computing Systems, 26 April–1 May 2014. Toronto: ACM; 2014. Leakiness and creepiness in app space: perceptions of privacy and mobile app use; pp. 2347–5...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2175`
  `<span class="label">39.</span><cite>Office of the Privacy Commissioner of Canada. Results of the 2014 Global Privacy Enforcement Network sweep [<a href="https://www.priv.gc.ca/media/nr-c/2014/bg_140910_e.asp" class="usa-link usa-link--external" data-ga-action="click_feat_suppl" target="_blank" rel="...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2187`
  `<span class="label">43.</span><cite>Plachkinova M, Andres S, Chatterjee S.  The 48th Hawaii International Conference on System Sciences (HICSS), 5–8 January 2015. Kauai: HICSS; 2015. A taxonomy of mHealth apps – security and privacy concerns; pp. 3187–96.</cite> [<a href="https://scholar.google.com/...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2189`
  `<span class="label">44.</span><cite>Martinez-Perez B, de la Torre-Diez I, Lopez-Coronado M. Privacy and security in mobile health apps: a review and recommendations. J Med Syst. 2014;39:181. doi: 10.1007/s10916-014-0181-3.</cite> [<a href="https://doi.org/10.1007/s10916-014-0181-3" class="usa-link u...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2191`
  `<span class="label">45.</span><cite>Weber RH. Internet of Things – new security and privacy challenges. Comput Law Secur Rev. 2010;26:23–30. doi: 10.1016/j.clsr.2009.11.008.</cite> [<a href="https://doi.org/10.1016/j.clsr.2009.11.008" class="usa-link usa-link--external" data-ga-action="click_feat_su...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2196`
  `<span class="label">47.</span><cite>Federal Trade Commission  . Mobile privacy disclosures – building trust through transparency. USA: Federal Trade Commission; 2013. </cite> [<a href="https://scholar.google.com/scholar_lookup?title=Mobile%20privacy%20disclosures%20%E2%80%93%20building%20trust%20thr...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2198`
  `<span class="label">48.</span><cite>Organisation for Economic Co-operation and Development. The OECD privacy framework 2013 [<a href="http://www.oecd.org/sti/ieconomy/oecd_privacy_framework.pdf" class="usa-link usa-link--external" data-ga-action="click_feat_suppl" target="_blank" rel="noopener noref...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2204`
  `<span class="label">50.</span><cite>Hall JL, McGraw D. For telehealth to succeed, privacy and security risks must be identified and addressed. Health Aff (Millwood) 2014;33:216–21. doi: 10.1377/hlthaff.2013.0997.</cite> [<a href="https://doi.org/10.1377/hlthaff.2013.0997" class="usa-link usa-link--e...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2216`
  `<span class="label">55.</span><cite>Takabi H, Joshi JBD, Gail-Joon A. Security and privacy challenges in cloud computing environments. IEEE Secur Priv. 2010;8:24–31. doi: 10.1109/MSP.2010.186.</cite> [<a href="https://doi.org/10.1109/MSP.2010.186" class="usa-link usa-link--external" data-ga-action="...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2218`
  `<span class="label">56.</span><cite>Abbas A, Khan SU. A review on the state-of-the-art privacy-preserving approaches in the e-Health clouds. IEEE J Biomed Health Inform. 2014;18:1431–41. doi: 10.1109/JBHI.2014.2300846.</cite> [<a href="https://doi.org/10.1109/JBHI.2014.2300846" class="usa-link usa-l...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2886`
  `<a href="https://www.hhs.gov/vulnerability-disclosure-policy/index.html" class="usa-link usa-link--external usa-link--alt ncbi-footer__link" rel="noreferrer noopener" target='_blank' >`
- `database/snapshots/P015-pmc-far-side-mhealth.html:98`
  `<meta name="citation_title" content="Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android">`
- `database/snapshots/P015-pmc-far-side-mhealth.html:115`
  `<meta name="description" content="Mobile health (mHealth) apps aim at providing seamless access to tailored health information technology and have the potential to alleviate global health burdens. Yet, they bear risks to information security and privacy because users need to reveal ...">`
- `database/snapshots/P015-pmc-far-side-mhealth.html:116`
  `<meta name="og:title" content="Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android">`
- `database/snapshots/P015-pmc-far-side-mhealth.html:119`
  `<meta name="og:description" content="Mobile health (mHealth) apps aim at providing seamless access to tailored health information technology and have the potential to alleviate global health burdens. Yet, they bear risks to information security and privacy because users need to reveal ...">`
- `database/snapshots/P015-pmc-far-side-mhealth.html:1343`
  `<hgroup><h1>Exploring the Far Side of Mobile Health: Information Security and Privacy of Mobile Health Apps on iOS and Android</h1></hgroup><div class="cg p">`
- `database/snapshots/P015-pmc-far-side-mhealth.html:1415`
  `<p>Mobile health (mHealth) apps aim at providing seamless access to tailored health information technology and have the potential to alleviate global health burdens. Yet, they bear risks to information security and privacy because users need to reveal private, sensitive medical information to redeem...`
- `database/snapshots/P015-pmc-far-side-mhealth.html:1480`
  `<div class="p text-right font-secondary"><a href="table/table1/" class="usa-link" target="_blank" rel="noopener noreferrer">Open in a new tab</a></div></section><p>Characteristic 1, health specificity of information available to apps, assesses whether the app has access to medical user information, ...`
- `database/snapshots/P015-pmc-far-side-mhealth.html:1481`
  `<p>There were two researchers that assessed all discovered clusters. To maintain a consistent interpretation of clusters during assessment, each rater annotated each cluster with a short description based on connotation and prevalence of tags assigned to the cluster. These descriptions were verified...`
- `database/snapshots/P015-pmc-far-side-mhealth.html:1482`
  `<p>mHealth app archetypes (AT), with respect to information security and privacy are identified by grouping clusters with identical assessments in a final aggregation step. An archetype is “the original pattern or model of which all things of the same type are representations or copies” [<a href="#r...`
- `database/snapshots/P015-pmc-far-side-mhealth.html:2047`
  `<span class="label">16.</span><cite>Bélanger F, Crossler RE. MIS Q. 2011.  [2015-01-12].  Privacy in the digital age: A review of information privacy research in information systems <a href="http://misq.org/cat-articles/privacy-in-the-digital-age-a-review-of-information-privacy-research-in-informati...`
- `database/snapshots/P015-pmc-far-side-mhealth.html:2052`
  `<span class="label">18.</span><cite>Avancha S, Baxi A, Kotz D. Privacy in mobile technology for personal healthcare. ACM Comput. Surv. 2012 Nov 01;45(1):1–54. doi: 10.1145/2379776.2379779.</cite> [<a href="https://doi.org/10.1145/2379776.2379779" class="usa-link usa-link--external" data-ga-action="c...`

## BR051

paper_id: B013
paper_title: Availability and quality of mobile health app privacy policies

- `database/prompts/per_app_audit_prompt.md:86`
  `- SDK presence + privacy policy inconsistency`
- `database/snapshots/P009-ndss-webview-tracking.html:341`
  `<p><p>WebViews are a prevalent method of embedding web-based content in Android apps. While they offer functionality similar to that of browsers and execute in an isolated context, apps can directly interfere with WebViews by dynamically injecting JavaScript code at runtime. While prior work has ext...`
- `database/snapshots/P009-ndss-webview-tracking.html:342`
  `<p>To address this gap, we propose WebViewTracer, a framework designed to dynamically analyze the execution of JavaScript code within WebViews at runtime. Our system combines within-WebView JavaScript execution traces with Java method-call information, to also capture the information exchange occurr...`
- `database/snapshots/P011-soups-consent-tracking.html:31`
  `<meta name="citation_conference_title" content="Seventeenth Symposium on Usable Privacy and Security (SOUPS 2021)" />`
- `database/snapshots/P011-soups-consent-tracking.html:362`
  `<div class="field field-name-field-paper-people-text field-type-text-long field-label-hidden"><div class="field-items field-items"><div class="field-item odd"><p>Konrad Kollnig and Reuben Binns, <em>University of Oxford;</em> Pierre Dewitte, <em>KU Leuven;</em> Max Van Kleek, Ge Wang, Daniel Omeiza,...`
- `database/snapshots/P011-soups-consent-tracking.html:442`
  `booktitle = {Seventeenth Symposium on Usable Privacy and Security (SOUPS 2021)},<br />`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1554`
  `<p>When used as intended, a variety of sensitive user data are collected, stored, and transmitted through these Android mHealth apps. <a href="#f6-1969977" class="usa-link">Figure 6</a> shows the distribution of sensitive information in the 22 apps (x axis means the number of appearances of sensitiv...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1561`
  `<p>The increased use of mHealth results in greater risks to health-related information on mobile devices. Developers and healthcare service providers would be wise to make efforts to ensure that mHealth apps facilitate security compliance even if they are not legally required to do so (at the curren...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1564`
  `<p>We observed that many apps may ask users to share their private health information by providing privacy policy agreed by users themselves. In our study, most of the apps do make privacy policies available to users either via an URL link in the app or shown when the app is launched for the first t...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1565`
  `<p>A study of Android mHealth apps reveals common shortcomings in security and privacy when using communications and storage. Steps should be made to encourage mHealth app vendors to assure encrypted network links for communications and the use of third party storage only when adequate security and ...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1439`
  `<p>Medical app accreditation programs, in which apps are subject to formal assessment or peer review, are a recent development that aims to provide clinical assurances about quality and safety, foster trust, and promote app adoption by patients and professionals [<a href="#CR14" class="usa-link" ari...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1440`
  `<p>Launched in March 2013, the NHS Health Apps Library offers a curated list of apps for patient and public use. Apps are intended to be suitable for professional recommendation to patients but are also available for general use without clinical support. Registered apps undergo an appraisal process,...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1441`
  `<p>The purpose of the current study was to assess the extent to which accredited apps adhered to these principles. We reviewed all apps available from the NHS Health Apps Library at a particular point in time, and assessed compliance with recommended practice for information collection, transmission...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1444`
  `<p>Assessment involved a combination of manual testing and policy review. Testing was used to characterize app features, explore data collection and transmission behaviour, and identify adherence to data protection principles concerning information security. Policy review identified the extent to wh...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1445`
  `<p>Apps were subject to a 6-month period of evaluation, from August 2013 to January 2014. Testing incorporated two strategies. To ensure coverage of features relating to information collection and transmission, sequential exploration of all user interface elements was performed for each app. After t...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1454`
  `<p>Potential vulnerabilities in server-side controls were explored through manual testing. To identify potential authorization problems, we reset session state information and replayed intercepted data requests to see if developer or third-party systems would return user data without first requiring...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1455`
  `<p>We systematically assessed the content of privacy policies associated with each app. We searched in-app documentation, app store entries and related websites. All documents that self-identified as a privacy policy were included in analysis. We also located privacy-relevant text forming part of ot...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1456`
  `<p>Assessment proceeded by systematically coding each schema item as either being addressed or absent from extracted policy text. For those principles relating to user rights, such as the ability to opt-out of data collection, policies were additionally coded according to whether a given right was a...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1457`
  `<p>Coding decisions, as well as any relevant policy text annotations, were captured using custom software (see Additional file <a href="#MOESM1" class="usa-link">1</a>: Figure AF5). All decisions were reviewed to reach a consensus agreement on policy coverage. The nature of information actually coll...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1458`
  `<p>Data were compiled into a single dataset for analysis (supplied as Additional file <a href="#MOESM2" class="usa-link">2</a>). We used simple descriptive statistics to summarize aspects of data collection, mobile-device storage and transmission. Unless otherwise stated, the unit of analysis is the...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1459`
  `<p>We hypothesized that the likelihood of an app having a privacy policy should not vary by platform or by the distribution model (free or paid). Although apps for iOS are subject to a quality control process prior to release, and although developers of paid-for apps may have greater resources to in...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1678`
  `<p>In addition to issues affecting information transmission, risks to confidentiality were identified in software application programming interfaces (APIs) provided by online services to communicate with apps. Of 27 apps with such services, 16 (59 %, n = 16/27) allowed unencrypted access. Two apps h...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1679`
  `<p>Two-thirds (67 %, n = 53/79) of apps had some form of privacy policy (Table <a href="#Tab3" class="usa-link">3</a>). The proportion was higher in apps in which users could record information (71 %, n = 50/70) and those transmitting user-related information (70 %, n = 49/70). The availability of a...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1681`
  `<div class="caption p"><p>Availability of policy disclosures</p></div>`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1733`
  `<td colspan="1" rowspan="1">Advertising policy</td>`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1760`
  `<sup>a</sup>Incorporates strong personal identifiers, health-related information and other sensitive information</p></div></div></section><p>Approximately a third (35 %, n = 28/79) of all apps, and two-fifths (42 %, n = 25/59) of those collecting personal or sensitive data, were linked to some form ...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1761`
  `<p>Policies varied in their coverage of recommended topics (Table <a href="#Tab4" class="usa-link">4</a>). Most apps (87 %, n = 46 of 53 apps with policies) incorporated statements of intended primary uses for recorded or transmitted information, and three-fifths (58 %, n = 31/53) described intended...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1763`
  `<div class="caption p"><p>Coverage of privacy and security-related topics in privacy policies</p></div>`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2016`
  `<sup>a</sup>Incorporates strong personal identifiers, health-related information and other sensitive information; <sup>b</sup>because these topics are only relevant for apps that transmit data, the denominator for calculated percentages is the number of apps with a privacy policy that also transmit ...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2017`
  `<p>Overall, 71 % (n = 50/70) of apps collecting or transmitting information (or both) also had a privacy policy. For a small number (4 %, n = 2/49) information handling was completely consistent with commitments made by the policy. However, while no apps transmitted information where a specific comm...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2020`
  `<p>Medical app stores and accreditation programs are specifically intended to provide a trusted resource for both patients and clinical users. In addition to offering clinical quality assurances, they are well-placed to scrutinize information privacy. Some, including the NHS Health Apps Library, inc...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2021`
  `<p>Apps available through the NHS Health Apps Library exhibited substantial variation in compliance with data protection principles, demonstrated both by the availability and content of privacy policies, and adherence to recommended practices for confidentiality enforcement. Over half included funct...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2022`
  `<p>Two cloud-based apps had critical privacy vulnerabilities; weaknesses of design that could be intentionally exploited to obtain user information. As long as these vulnerabilities persist, the privacy of users of these services is in jeopardy. As recent data thefts from high profile online service...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2023`
  `<p>The findings highlight potential shortcomings of an accreditation approach that, in respect of privacy at least, appears to rely mainly on self-declared compliance. The strategy contrasts with that adopted by AppSaludable, another prominent certification program, which explicitly defines privacy ...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2024`
  `<p>The implications extend beyond the risk of diminished trust in health apps. Precarious privacy practices may create new legal and liability issues, and these may ultimately require regulator involvement. Because health and, in particular, wellness apps are often provided by organizations that are...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2025`
  `<p>By assessing all apps available through an accredited medical app store we were able to sample a wide range of app types including those from health providers and commercial organizations. The frequencies of identified issues reflect the specific population of apps available at the time of assess...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2026`
  `<p>Variation in privacy practices observed in clinically-accredited health apps available through a dedicated medical app store raises concerns about potential risks to users and questions the ability of accreditation processes relying substantially on developer self-certification to ensure adherenc...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2090`
  `<span class="label">6.</span><cite>Kotz D.  Third International Conference on Communication Systems and Networks (COMSNETS), 4–8 January 2011. Bangalore: COMSNETS; 2011. A threat taxonomy for mHealth privacy; pp. 1–6.</cite> [<a href="https://scholar.google.com/scholar_lookup?title=Third%20Internati...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2092`
  `<span class="label">7.</span><cite>Cohn SP.  Privacy and confidentiality in the nationwide health information network. Washington: National Committee on Vital and Health Statistics; 2006. </cite> [<a href="https://scholar.google.com/scholar_lookup?title=Privacy%20and%20confidentiality%20in%20the%20n...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2094`
  `<span class="label">8.</span><cite>Smith HJ, Dinev T, Xu H. Information privacy research: an interdisciplinary review. MIS Q. 2011;35:989–1016.</cite> [<a href="https://scholar.google.com/scholar_lookup?journal=MIS%20Q.&amp;title=Information%20privacy%20research:%20an%20interdisciplinary%20review&am...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2096`
  `<span class="label">9.</span><cite>Njie L. Mobile health and fitness apps: what are the privacy risks? [<a href="https://www.privacyrights.org/mobile-health-and-fitness-apps-what-are-privacy-risks" class="usa-link usa-link--external" data-ga-action="click_feat_suppl" target="_blank" rel="noopener no...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1401`
  `<p><strong>Additional Contributions:</strong> Harini Kolamunna, PhD, UNSW Sydney, reviewed the privacy policies. Dr Kolamunna was compensated for her contribution to the study.</p>`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1419`
  `<p>Do the privacy policies of popular smartphone applications (apps) for depression and smoking cessation describe accurately whether data will be processed by commercial third parties?</p></section><section id="ab-zoi190111-2"><h3 class="pmc_sec_title">Findings</h3>`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1420`
  `<p>In this cross-sectional study of 36 top-ranked apps for depression and smoking cessation available in public app stores, 29 transmitted data to services provided by Facebook or Google, but only 12 accurately disclosed this in a privacy policy.</p></section><section id="ab-zoi190111-3"><h3 class="...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1421`
  `<p>Health care professionals prescribing apps should not rely on disclosures about data sharing in health app privacy policies but should reasonably assume that data will be shared with commercial entities whose own privacy practices have been questioned and, if possible, should consider only apps w...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1422`
  `<p>This cross-sectional study evaluates the data sharing and privacy practices of smartphone applications available in public app stores for depression and smoking cessation.</p></section><section class="abstract" id="abstract3"><h2>Abstract</h2>`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1424`
  `<p>Inadequate privacy disclosures have repeatedly been identified by cross-sectional surveys of health applications (apps), including apps for mental health and behavior change. However, few studies have assessed directly the correspondence between privacy disclosures and how apps handle personal da...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1425`
  `<p>To provide a contemporary assessment of the privacy practices of popular apps for depression and smoking cessation by critically evaluating privacy policy content and, specifically, comparing disclosures regarding third-party data transmission to actual behavior.</p></section><section id="ab-zoi1...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1426`
  `<p>Cross-sectional assessment of 36 top-ranked (by app store search result ordering in January 2018) apps for depression and smoking cessation for Android and iOS in the United States and Australia. Privacy policy content was evaluated with prespecified criteria. Technical assessment of encrypted an...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1428`
  `<p>Twenty-five of 36 apps (69%) incorporated a privacy policy. Twenty-two of 25 apps with a policy (88%) provided information about primary uses of collected data, while only 16 (64%) described secondary uses. While 23 of 25 apps with a privacy policy (92%) stated in a policy that data would be tran...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1429`
  `<p>Data sharing with third parties that includes linkable identifiers is prevalent and focused on services provided by Google and Facebook. Despite this, most apps offer users no way to anticipate that data will be shared in this way. As a result, users are denied an informed choice about whether su...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1430`
  `<p>While the potential of smartphone applications (apps) to improve access to health care resources,<sup><a href="#zoi190111r1" class="usa-link" aria-describedby="zoi190111r1">1</a></sup> real-time monitoring,<sup><a href="#zoi190111r2" class="usa-link" aria-describedby="zoi190111r2">2</a></sup> and...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1431`
  `<p>This tension between personal privacy and data capture by health care apps is largely driven by the business models of these apps. Because many national health payers and insurance companies do not yet cover apps (given their often nascent evidence base), selling either subscriptions or users’ pe...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1432`
  `<p>Responding to the need to ensure health care apps adequately protect users’ privacy and to close loopholes that have created the current culture of nontransparent and insecure apps, organizations around the world are now promoting health care app privacy and security. The US Food and Drug Adminis...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1433`
  `<p>However, the evaluation of the privacy (and security) of health care apps remains a challenge. Inspection of app privacy policies has proven valuable in highlighting potential risks, such as whether users are offered routes to edit, amend, and delete personal data,<sup><a href="#zoi190111r6" clas...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1434`
  `<p>In this study, we aimed to provide a contemporary assessment of the privacy practices of popular mental health apps and, specifically, the correspondence between disclosures made in privacy policies and data actually transmitted to third parties. Following the pattern of previous work<sup><a href...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1436`
  `<p>Privacy policies and related material with the potential to contain privacy-related content, such as terms and conditions, were identified from app store descriptions, app content, and associated websites. We adopted a permissive stance that reviewed all policy material, whether (1) presented wit...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1437`
  `<section class="tw xbox font-sm" id="zoi190111t1"><h3 class="obj_head">Table 1.  Counts and Proportions of Apps Addressing Specific Privacy Criteria in a Policy.</h3>`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1442`
  `<th valign="top" align="left" scope="col" rowspan="1" colspan="1">Privacy Criteria</th>`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1562`
  `<sup><sup>a</sup></sup><p class="display-inline">Percentage of apps with a privacy policy (n = 25), unless otherwise stated.</p>`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1569`
  `<p>More than two-thirds (25 of 36 [69%]) of apps incorporated or linked to a privacy policy. <a href="#zoi190111t1" class="usa-link">Table 1</a> summarizes the extent to which the content of these satisfied predefined privacy policy quality criteria. While 22 of 25 apps with a policy (88%) described...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1570`
  `<p>Of the 23 of 25 apps (92%) that, within policy text, addressed the possibility of transmission of data to any third party, 16 (70%) positively indicated data would be shared with advertisers (of which 6 displayed visible advertisements during testing) and 14 (61%) indicated that data would be sha...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1571`
  `<p>After interception and inspection of internet traffic generated by each app, data transmission to 1 or more third parties was identified for 33 of 36 apps (92%) (compared with 12 of 36 [33%] in which data were transmitted to a destination operated by the developer). <a href="#zoi190111t2" class="...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1572`
  `<section class="tw xbox font-sm" id="zoi190111t2"><h3 class="obj_head">Table 2.  Counts and Proportions of Apps Transmitting Data to a Third Party and Whether This Was Disclosed in a Privacy Policy.</h3>`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1770`
  `</div></section><p>Among the 36 apps, 29 (81%) transmitted data to analytics and advertising or marketing services operated by 2 commercial entities, Google and Facebook, but only 17 of the 29 (59%) disclosed transmission in a policy. Of the 15 apps transmitting data to Google advertising services, ...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1773`
  `<p>Transmission of data to third-party entities was prevalent, occurring in 33 of 36 top-ranked apps (92%) for depression and smoking cessation, but most apps failed to provide transparent disclosure of such practices. Commonly observed issues included the lack of a written privacy policy, the omiss...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1774`
  `<p>Transmissions to third parties were dominated in this sample by just 2 commercial entities offering advertising and analytics services. While both Google and Facebook require developers to name the use of their services to users,<sup><a href="#zoi190111r33" class="usa-link" aria-describedby="zoi1...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1775`
  `<p>While transmission of directly personally identifiable information was not observed, traffic sent to third parties routinely included linkable information. This included fixed device identifiers on Android (despite these being deprecated on privacy grounds<sup><a href="#zoi190111r37" class="usa-l...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1776`
  `<p>Our findings are topical not just because of contemporary concerns about the privacy practices of certain commercial entities,<sup><a href="#zoi190111r7" class="usa-link" aria-describedby="zoi190111r7">7</a></sup> but also in respect to current efforts to establish accreditation programs for ment...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1777`
  `<p>These dynamic aspects of app privacy underline the need for the clinical community to respond with frequent privacy reviews that incorporate both consideration of privacy policies and technical security reviews. While it is appealing to offer health care consumers metrics such as transparency sco...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1779`
  `<p>This study has limitations. As with other studies of health app policy and content, our analysis was conducted using a snapshot of apps and policy documentation captured at a single point. While we recognize that the app marketplaces are a dynamic environment,<sup><a href="#zoi190111r40" class="u...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1783`
  `<p>While smartphone apps hold substantial potential to increase access to mental health care, our results highlight deficits in the disclosure of data transmission practices involving third parties. Mechanisms that potentially enable a small number of dominant online service providers to link inform...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1885`
  `<span class="label">34.</span><cite>Facebook Inc  Facebook for developers: Facebook platform policy. <a href="https://developers.facebook.com/policy" class="usa-link usa-link--external" data-ga-action="click_feat_suppl" target="_blank" rel="noopener noreferrer">https://developers.facebook.com/policy...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1897`
  `<span class="label">38.</span><cite>Cutler K-M. Amid privacy concerns, Apple has started rejecting apps that access UDIDs. <a href="https://techcrunch.com/2012/03/24/apple-udids/" class="usa-link usa-link--external" data-ga-action="click_feat_suppl" target="_blank" rel="noopener noreferrer">https://...`
- `database/snapshots/P016-pmc-depression-smoking-apps.html:1900`
  `<span class="label">39.</span><cite>Google LLC. Advertising policies help: personalized advertising. <a href="https://support.google.com/adwordspolicy/answer/143465?hl=en&amp;ref_topic=1626336" class="usa-link usa-link--external" data-ga-action="click_feat_suppl" target="_blank" rel="noopener norefe...`
- `database/snapshots/P017-pmc-mobile-health-privacy.html:1442`
  `<p>88.0% (n=18 472) of mHealth apps included code that could potentially collect user data. 3.9% (n=616) of apps transmitted user information in their traffic. Most data collection operations in apps code and data transmissions in apps traffic involved external service providers (third parties). The...`
- `database/snapshots/P017-pmc-mobile-health-privacy.html:1443`
  `<p>This analysis found serious problems with privacy and inconsistent privacy practices in mHealth apps. Clinicians should be aware of these and articulate them to patients when determining the benefits and risks of mHealth apps.</p></section></section><section id="sec8"><h2 class="pmc_sec_title">In...`
- `database/snapshots/P017-pmc-mobile-health-privacy.html:1446`
  `<a href="#ref4" class="usa-link" aria-describedby="ref4"><sup>4</sup></a> they pose problems concerning data privacy because of the sensitive information they can access, the use of a business model that is centred on selling subscriptions or sharing user data,<a href="#ref5" class="usa-link" aria-d...`
- `database/snapshots/P017-pmc-mobile-health-privacy.html:1447`
  `<p>In line with the HIPAA, the US Food and Drug Administration released guidance for the postmarket management of cybersecurity in medical devices in 2016.<a href="#ref8" class="usa-link" aria-describedby="ref8"><sup>8</sup></a> The FDA recommended that manufacturers of medical devices (ie, app deve...`
- `database/snapshots/P017-pmc-mobile-health-privacy.html:1449`
  `<p>Because of the inadequate privacy disclosures of top mHealth apps,<a href="#ref4" class="usa-link" aria-describedby="ref4"><sup>4</sup></a>`

## BR052

paper_id: B013
paper_title: Availability and quality of mobile health app privacy policies

- `database/prompts/per_app_audit_prompt.md:86`
  `- SDK presence + privacy policy inconsistency`
- `database/snapshots/P001-usenix-android-application-security.html:373`
  `<ul class="menu-tree menu" data-menu-style="tree" data-clickdown="0" data-collapse="default"><li class="first leaf menu-mlid-2774"><a href="/privacy-policy">Privacy Policy</a></li>`
- `database/snapshots/P002-usenix-supor.html:508`
  `<div class="field field-name-field-paper-people-text field-type-text-long field-label-hidden"><div class="field-items field-items"><div class="field-item odd"><p class="p1">Jianjun Huang, <i>Purdue University;</i> Zhichun Li, Xusheng Xiao, and Zhenyu Wu, <i>NEC Labs America; </i>Kangjie Lu, <i>Georg...`
- `database/snapshots/P002-usenix-supor.html:509`
  `<p>In this paper, we examine the possibility of scalably detecting sensitive user inputs from mobile apps. In particular, we design and implement SUPOR, a novel static analysis tool that automatically examines the UIs to identify sensitive user inputs containing critical user data, such as user cred...`
- `database/snapshots/P002-usenix-supor.html:945`
  `<ul class="menu-tree menu" data-menu-style="tree" data-clickdown="0" data-collapse="default"><li class="first leaf menu-mlid-2774"><a href="/privacy-policy">Privacy Policy</a></li>`
- `database/snapshots/P003-ndss-content-leaks.html:434`
  `<p class="has-text-align-center"><a href="https://www.ndss-symposium.org/privacy-policy/">Privacy Policy</a> | <a href="https://www.ndss-symposium.org/terms-of-use/">Terms of Use</a> <span class="hide-on-mobile">|</span> <a href="https://www.ndss-symposium.org/ndss-code-of-conduct/">NDSS Code of Con...`
- `database/snapshots/P004-ndss-execute-this.html:404`
  `<p class="has-text-align-center"><a href="https://www.ndss-symposium.org/privacy-policy/">Privacy Policy</a> | <a href="https://www.ndss-symposium.org/terms-of-use/">Terms of Use</a> <span class="hide-on-mobile">|</span> <a href="https://www.ndss-symposium.org/ndss-code-of-conduct/">NDSS Code of Con...`
- `database/snapshots/P005-ndss-appsealer.html:404`
  `<p class="has-text-align-center"><a href="https://www.ndss-symposium.org/privacy-policy/">Privacy Policy</a> | <a href="https://www.ndss-symposium.org/terms-of-use/">Terms of Use</a> <span class="hide-on-mobile">|</span> <a href="https://www.ndss-symposium.org/ndss-code-of-conduct/">NDSS Code of Con...`
- `database/snapshots/P006-teamusec-android-ssl.html:483`
  `<a class="text-link" href="https://www.uni-hannover.de/en/datenschutzerklaerung/">Privacy Policy</a>`
- `database/snapshots/P007-usenix-deep-links.html:280`
  `<ul class="menu-tree menu" data-menu-style="tree" data-clickdown="0" data-collapse="default"><li class="first leaf menu-mlid-2774"><a href="/privacy-policy">Privacy Policy</a></li>`
- `database/snapshots/P008-usenix-webview-dcv.html:468`
  `<ul class="menu-tree menu" data-menu-style="tree" data-clickdown="0" data-collapse="default"><li class="first leaf menu-mlid-2774"><a href="/privacy-policy">Privacy Policy</a></li>`
- `database/snapshots/P009-ndss-webview-tracking.html:341`
  `<p><p>WebViews are a prevalent method of embedding web-based content in Android apps. While they offer functionality similar to that of browsers and execute in an isolated context, apps can directly interfere with WebViews by dynamically injecting JavaScript code at runtime. While prior work has ext...`
- `database/snapshots/P009-ndss-webview-tracking.html:342`
  `<p>To address this gap, we propose WebViewTracer, a framework designed to dynamically analyze the execution of JavaScript code within WebViews at runtime. Our system combines within-WebView JavaScript execution traces with Java method-call information, to also capture the information exchange occurr...`
- `database/snapshots/P009-ndss-webview-tracking.html:497`
  `<p class="has-text-align-center"><a href="https://www.ndss-symposium.org/privacy-policy/">Privacy Policy</a> | <a href="https://www.ndss-symposium.org/terms-of-use/">Terms of Use</a> <span class="hide-on-mobile">|</span> <a href="https://www.ndss-symposium.org/ndss-code-of-conduct/">NDSS Code of Con...`
- `database/snapshots/P010-usenix-policylint.html:8`
  `<meta name="citation_title" content="{PolicyLint}: Investigating Internal Privacy Policy Contradictions on Google Play" />`
- `database/snapshots/P010-usenix-policylint.html:375`
  `<div class="field field-name-field-paper-people-text field-type-text-long field-label-hidden"><div class="field-items field-items"><div class="field-item odd"><p>Benjamin Andow and Samin Yaseer Mahmud, <em>North Carolina State University;</em> Wenyu Wang, <em>University of Illinois at Urbana-Champai...`
- `database/snapshots/P010-usenix-policylint.html:533`
  `<ul class="menu-tree menu" data-menu-style="tree" data-clickdown="0" data-collapse="default"><li class="first leaf menu-mlid-2774"><a href="/privacy-policy">Privacy Policy</a></li>`
- `database/snapshots/P011-soups-consent-tracking.html:362`
  `<div class="field field-name-field-paper-people-text field-type-text-long field-label-hidden"><div class="field-items field-items"><div class="field-item odd"><p>Konrad Kollnig and Reuben Binns, <em>University of Oxford;</em> Pierre Dewitte, <em>KU Leuven;</em> Max Van Kleek, Ge Wang, Daniel Omeiza,...`
- `database/snapshots/P011-soups-consent-tracking.html:507`
  `<ul class="menu-tree menu" data-menu-style="tree" data-clickdown="0" data-collapse="default"><li class="first leaf menu-mlid-2774"><a href="/privacy-policy">Privacy Policy</a></li>`
- `database/snapshots/P012-ndss-inconpreter.html:341`
  `<p><p>The widespread use of mobile apps meets user needs but also raises security concerns. Current security analysis methods often fall short in addressing user concerns as they do not parse app behavior from the user's standpoint, leading to users not fully understanding the risks within the apps ...`
- `database/snapshots/P012-ndss-inconpreter.html:496`
  `<p class="has-text-align-center"><a href="https://www.ndss-symposium.org/privacy-policy/">Privacy Policy</a> | <a href="https://www.ndss-symposium.org/terms-of-use/">Terms of Use</a> <span class="hide-on-mobile">|</span> <a href="https://www.ndss-symposium.org/ndss-code-of-conduct/">NDSS Code of Con...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:114`
  `<meta name="description" content="Mobile Health (mHealth) applications lie outside of regulatory protection such as HIPAA, which requires a baseline of privacy and security protections appropriate to sensitive medical data. However, mHealth apps, particularly those in the app stores ...">`
- `database/snapshots/P013-pmc-android-mhealth-security.html:118`
  `<meta name="og:description" content="Mobile Health (mHealth) applications lie outside of regulatory protection such as HIPAA, which requires a baseline of privacy and security protections appropriate to sensitive medical data. However, mHealth apps, particularly those in the app stores ...">`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1389`
  `<p>Mobile Health (mHealth) applications lie outside of regulatory protection such as HIPAA, which requires a baseline of privacy and security protections appropriate to sensitive medical data. However, mHealth apps, particularly those in the app stores for iOS and Android, are increasingly handling ...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1391`
  `<p>Security and privacy of health data could be significantly affected by this trend. Freed from the bonds of HIPAA, mHealth apps are free to handle data using lower assurances than those typically applied to HIPAA entities. However, the data they handle is often as sensitive as the data handled by ...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1392`
  `<p>The goal of this paper is to carry out a three-stage study of the security and privacy status of free mHealth apps offered on Google Play. In the first study, the top 160 free mHealth apps in Google Play are classified and examined to formulate a list of attack surfaces that need attention in thi...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1432`
  `<p>In recent years, we have seen an increased adoption of mobile health applications by patients and physicians as well as the general public<a href="#b1-1969977" class="usa-link" aria-describedby="b1-1969977"><sup>1</sup></a><sup>, </sup><a href="#b2-1969977" class="usa-link" aria-describedby="b2-1...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1434`
  `<p>Recently, researchers have been actively involved in mHealth research. Mosa et al.<a href="#b5-1969977" class="usa-link" aria-describedby="b5-1969977"><sup>5</sup></a> review articles discussing the design, development and evaluation of mHealth apps and discuss the differences between apps for he...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1435`
  `<p>Our work focuses on researching the security and privacy risks on Android platform. Android is an open-source platform supported by Google that has become the most common OS for mobile devices. A report by F-Secure<a href="#b8-1969977" class="usa-link" aria-describedby="b8-1969977"><sup>8</sup></...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1436`
  `<p>This paper investigates the security and privacy risks in Android mHealth apps. More specifically, we will investigate such threats in three studies:</p>`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1554`
  `<p>When used as intended, a variety of sensitive user data are collected, stored, and transmitted through these Android mHealth apps. <a href="#f6-1969977" class="usa-link">Figure 6</a> shows the distribution of sensitive information in the 22 apps (x axis means the number of appearances of sensitiv...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1561`
  `<p>The increased use of mHealth results in greater risks to health-related information on mobile devices. Developers and healthcare service providers would be wise to make efforts to ensure that mHealth apps facilitate security compliance even if they are not legally required to do so (at the curren...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1564`
  `<p>We observed that many apps may ask users to share their private health information by providing privacy policy agreed by users themselves. In our study, most of the apps do make privacy policies available to users either via an URL link in the app or shown when the app is launched for the first t...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1565`
  `<p>A study of Android mHealth apps reveals common shortcomings in security and privacy when using communications and storage. Steps should be made to encourage mHealth app vendors to assure encrypted network links for communications and the use of third party storage only when adequate security and ...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1573`
  `<span class="label">3.</span><cite>Avancha S, Baxi A, Kotz D. Privacy in mobile technology for personal healthcare. ACM Computing Surveys (CSUR) 2012;45(1):3.</cite> [<a href="https://scholar.google.com/scholar_lookup?journal=ACM%20Computing%20Surveys%20(CSUR)&amp;title=Privacy%20in%20mobile%20techn...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1575`
  `<span class="label">4.</span><cite>Kotz D. A threat taxonomy for mHealth privacy; 2011 Third International Conference on Communication Systems and Networks (COMSNETS); 2011 Jan 4–8; Bangalore. </cite> [<a href="https://scholar.google.com/scholar_lookup?journal=A%20threat%20taxonomy%20for%20mHealth%2...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1581`
  `<span class="label">7.</span><cite>Prasad A, Sorber J, Stablein T, Anthony D, Kotz D. Understanding Sharing Preferences and Behavior for mHealth Devices; Proceedings of the 2012 ACM Workshop on Privacy in the Electronic Society (WPES); October 15; Raleigh, NC. New York, NY: ACM; 2012. pp. 117–128.</...`
- `database/snapshots/P013-pmc-android-mhealth-security.html:1636`
  `<span class="label">29.</span><cite>Dixon P.  Medical Identity Theft: The Information Crime that Can Kill You. 2006. May 3,  (World Privacy Forum).</cite> [<a href="https://scholar.google.com/scholar_lookup?title=Medical%20Identity%20Theft:%20The%20Information%20Crime%20that%20Can%20Kill%20You&amp;a...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:68`
  `Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment - PMC`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:98`
  `<meta name="citation_title" content="Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment">`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:118`
  `<meta name="description" content="Poor information privacy practices have been identified in health apps. Medical app accreditation programs offer a mechanism for assuring the quality of apps; however, little is known about their ability to control information privacy risks. We ...">`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:119`
  `<meta name="og:title" content="Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment">`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:122`
  `<meta name="og:description" content="Poor information privacy practices have been identified in health apps. Medical app accreditation programs offer a mechanism for assuring the quality of apps; however, little is known about their ability to control information privacy risks. We ...">`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1363`
  `<hgroup><h1>Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment</h1></hgroup><div class="cg p">`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1432`
  `<p>Poor information privacy practices have been identified in health apps. Medical app accreditation programs offer a mechanism for assuring the quality of apps; however, little is known about their ability to control information privacy risks. We aimed to assess the extent to which already-certifie...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1433`
  `<p>Cross-sectional, systematic, 6-month assessment of 79 apps certified as clinically safe and trustworthy by the UK NHS Health Apps Library. Protocol-based testing was used to characterize personal information collection, local-device storage and information transmission. Observed information handl...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1434`
  `<p>The study revealed that 89 % (n = 70/79) of apps transmitted information to online services. No app encrypted personal information stored locally. Furthermore, 66 % (23/35) of apps sending identifying information over the Internet did not use encryption and 20 % (7/35) did not have a privacy poli...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1436`
  `<p>The online version of this article (doi:10.1186/s12916-015-0444-y) contains supplementary material, which is available to authorized users.</p></section><section id="kwd-group1" lang="en" class="kwd-group"><p><strong>Keywords:</strong> Smartphone, Mobile, Apps, Accreditation, NHS, Privacy, Confid...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1438`
  `<p>Because users cannot see into the inner workings of apps, or the services they connect to, confidence that personal information is handled appropriately relies mostly on trust. Users must trust in the ethical operation of app services, that developers will comply with privacy regulation and secur...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1439`
  `<p>Medical app accreditation programs, in which apps are subject to formal assessment or peer review, are a recent development that aims to provide clinical assurances about quality and safety, foster trust, and promote app adoption by patients and professionals [<a href="#CR14" class="usa-link" ari...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1440`
  `<p>Launched in March 2013, the NHS Health Apps Library offers a curated list of apps for patient and public use. Apps are intended to be suitable for professional recommendation to patients but are also available for general use without clinical support. Registered apps undergo an appraisal process,...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1441`
  `<p>The purpose of the current study was to assess the extent to which accredited apps adhered to these principles. We reviewed all apps available from the NHS Health Apps Library at a particular point in time, and assessed compliance with recommended practice for information collection, transmission...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1444`
  `<p>Assessment involved a combination of manual testing and policy review. Testing was used to characterize app features, explore data collection and transmission behaviour, and identify adherence to data protection principles concerning information security. Policy review identified the extent to wh...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1445`
  `<p>Apps were subject to a 6-month period of evaluation, from August 2013 to January 2014. Testing incorporated two strategies. To ensure coverage of features relating to information collection and transmission, sequential exploration of all user interface elements was performed for each app. After t...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1454`
  `<p>Potential vulnerabilities in server-side controls were explored through manual testing. To identify potential authorization problems, we reset session state information and replayed intercepted data requests to see if developer or third-party systems would return user data without first requiring...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1455`
  `<p>We systematically assessed the content of privacy policies associated with each app. We searched in-app documentation, app store entries and related websites. All documents that self-identified as a privacy policy were included in analysis. We also located privacy-relevant text forming part of ot...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1456`
  `<p>Assessment proceeded by systematically coding each schema item as either being addressed or absent from extracted policy text. For those principles relating to user rights, such as the ability to opt-out of data collection, policies were additionally coded according to whether a given right was a...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1457`
  `<p>Coding decisions, as well as any relevant policy text annotations, were captured using custom software (see Additional file <a href="#MOESM1" class="usa-link">1</a>: Figure AF5). All decisions were reviewed to reach a consensus agreement on policy coverage. The nature of information actually coll...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1458`
  `<p>Data were compiled into a single dataset for analysis (supplied as Additional file <a href="#MOESM2" class="usa-link">2</a>). We used simple descriptive statistics to summarize aspects of data collection, mobile-device storage and transmission. Unless otherwise stated, the unit of analysis is the...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1459`
  `<p>We hypothesized that the likelihood of an app having a privacy policy should not vary by platform or by the distribution model (free or paid). Although apps for iOS are subject to a quality control process prior to release, and although developers of paid-for apps may have greater resources to in...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1678`
  `<p>In addition to issues affecting information transmission, risks to confidentiality were identified in software application programming interfaces (APIs) provided by online services to communicate with apps. Of 27 apps with such services, 16 (59 %, n = 16/27) allowed unencrypted access. Two apps h...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1679`
  `<p>Two-thirds (67 %, n = 53/79) of apps had some form of privacy policy (Table <a href="#Tab3" class="usa-link">3</a>). The proportion was higher in apps in which users could record information (71 %, n = 50/70) and those transmitting user-related information (70 %, n = 49/70). The availability of a...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1681`
  `<div class="caption p"><p>Availability of policy disclosures</p></div>`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1760`
  `<sup>a</sup>Incorporates strong personal identifiers, health-related information and other sensitive information</p></div></div></section><p>Approximately a third (35 %, n = 28/79) of all apps, and two-fifths (42 %, n = 25/59) of those collecting personal or sensitive data, were linked to some form ...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1761`
  `<p>Policies varied in their coverage of recommended topics (Table <a href="#Tab4" class="usa-link">4</a>). Most apps (87 %, n = 46 of 53 apps with policies) incorporated statements of intended primary uses for recorded or transmitted information, and three-fifths (58 %, n = 31/53) described intended...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:1763`
  `<div class="caption p"><p>Coverage of privacy and security-related topics in privacy policies</p></div>`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2016`
  `<sup>a</sup>Incorporates strong personal identifiers, health-related information and other sensitive information; <sup>b</sup>because these topics are only relevant for apps that transmit data, the denominator for calculated percentages is the number of apps with a privacy policy that also transmit ...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2017`
  `<p>Overall, 71 % (n = 50/70) of apps collecting or transmitting information (or both) also had a privacy policy. For a small number (4 %, n = 2/49) information handling was completely consistent with commitments made by the policy. However, while no apps transmitted information where a specific comm...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2020`
  `<p>Medical app stores and accreditation programs are specifically intended to provide a trusted resource for both patients and clinical users. In addition to offering clinical quality assurances, they are well-placed to scrutinize information privacy. Some, including the NHS Health Apps Library, inc...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2021`
  `<p>Apps available through the NHS Health Apps Library exhibited substantial variation in compliance with data protection principles, demonstrated both by the availability and content of privacy policies, and adherence to recommended practices for confidentiality enforcement. Over half included funct...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2022`
  `<p>Two cloud-based apps had critical privacy vulnerabilities; weaknesses of design that could be intentionally exploited to obtain user information. As long as these vulnerabilities persist, the privacy of users of these services is in jeopardy. As recent data thefts from high profile online service...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2023`
  `<p>The findings highlight potential shortcomings of an accreditation approach that, in respect of privacy at least, appears to rely mainly on self-declared compliance. The strategy contrasts with that adopted by AppSaludable, another prominent certification program, which explicitly defines privacy ...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2024`
  `<p>The implications extend beyond the risk of diminished trust in health apps. Precarious privacy practices may create new legal and liability issues, and these may ultimately require regulator involvement. Because health and, in particular, wellness apps are often provided by organizations that are...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2025`
  `<p>By assessing all apps available through an accredited medical app store we were able to sample a wide range of app types including those from health providers and commercial organizations. The frequencies of identified issues reflect the specific population of apps available at the time of assess...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2026`
  `<p>Variation in privacy practices observed in clinically-accredited health apps available through a dedicated medical app store raises concerns about potential risks to users and questions the ability of accreditation processes relying substantially on developer self-certification to ensure adherenc...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2052`
  `<strong>NHS health apps and privacy.</strong>`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2053`
  `<strong>Table AF1</strong>: Data types identified in app data collections and transmissions. <strong>Figure AF2</strong>: How a ‘man-in-the-middle’ attack can be extended to intercept secure network communication. <strong>Figure AF3</strong>: Screenshot of custom software used to review transmitted ...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2057`
  `<strong>NHS health apps and privacy: dataset.</strong> (XLSX 1569 kb)</p>`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2090`
  `<span class="label">6.</span><cite>Kotz D.  Third International Conference on Communication Systems and Networks (COMSNETS), 4–8 January 2011. Bangalore: COMSNETS; 2011. A threat taxonomy for mHealth privacy; pp. 1–6.</cite> [<a href="https://scholar.google.com/scholar_lookup?title=Third%20Internati...`
- `database/snapshots/P014-pmc-accredited-health-app-privacy.html:2092`
  `<span class="label">7.</span><cite>Cohn SP.  Privacy and confidentiality in the nationwide health information network. Washington: National Committee on Vital and Health Statistics; 2006. </cite> [<a href="https://scholar.google.com/scholar_lookup?title=Privacy%20and%20confidentiality%20in%20the%20n...`

## BR055

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `sources/androidx/core/util/PatternsCompat.java:32`
  `Pattern patternCompile3 = Pattern.compile("(?:(?:(?:[a-zA-Z0-9[ -\ud7ff豈-﷏ﷰ-\uffef𐀀-\u1fffd𠀀-\u2fffd𰀀-\u3fffd\u40000-\u4fffd\u50000-\u5fffd\u60000-\u6fffd\u70000-\u7fffd\u80000-\u8fffd\u90000-\u9fffd\ua0000-\uafffd\ub0000-\ubfffd\uc0000-\ucfffd\ud0000-\udfffd\ue1000-\uefffd&&[^ [\u2000-\u200a]\u2028...`

## BR058

paper_id: B022
paper_title: A Study of Android Application Security

- `database/README.md:27`
  `- Distinguish first-party code from third-party SDK behavior.`
- `database/prompts/per_app_audit_prompt.md:49`
  `- Distinguish first-party code from third-party SDK code.`
- `database/prompts/per_app_audit_prompt.md:87`
  `- WebView injection + third-party exfiltration`
- `docs/paper_material_audit.md:40`
  `| P011 | A Fait Accompli? An Empirical Study into the Absence of Consent to Third-Party Tracking in Android Apps | P011-soups-consent-tracking.html | 无 | 摘要页 | 否，仅够核验来源/摘要级信息 | 缺完整正文；未检测到 Abstract、Introduction、Method/Methodology、Evaluation/Experiment、Results、Discussion、Conclusion、References 等主体章节 |`
- `docs/paper_material_audit.md:51`
  `| P022 | Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | P022-popets-facebook-sdk-settings.html | P022-popets-facebook-sdk-settings.pdf | 完整论文 | 是 | snapshot 是摘要页，但 PDF 已包含 Abstract、Introduction、Method/Methodology、Evaluation/Experiment、Results、Discussion、Conclus...`
- `docs/paper_material_audit.md:65`
  `- P022 Privacy Settings of Third-Party Libraries in Android Apps`

## BR059

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/AndroidManifest.xml:161`
  `<intent-filter>`
- `resources/AndroidManifest.xml:165`
  `<intent-filter>`
- `resources/AndroidManifest.xml:214`
  `<intent-filter>`

## BR060

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `sources/com/cmic/sso/sdk/h/a.java:12`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/cmic/sso/sdk/h/a.java:24`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/cmic/sso/sdk/h/a.java:37`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/cmic/sso/sdk/h/a.java:50`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/cmic/sso/sdk/h/e.java:79`
  `Cipher cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding");`
- `sources/com/cmic/sso/sdk/h/e.java:93`
  `Cipher cipher2 = Cipher.getInstance("RSA/ECB/PKCS1Padding");`
- `sources/com/cmic/sso/sdk/h/m.java:47`
  `Cipher cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding");`
- `sources/com/efs/sdk/base/core/util/b/a.java:22`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/efs/sdk/base/core/util/b/a.java:34`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/huawei/agconnect/config/impl/i.java:33`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/huawei/hms/hatool/h0.java:61`
  `Cipher cipher = Cipher.getInstance("RSA/ECB/OAEPWITHSHA-1ANDMGF1PADDING");`
- `sources/com/huawei/secure/android/common/encrypt/aes/AesCbc.java:23`
  `private static final String b = "AES/CBC/PKCS5Padding";`
- `sources/com/huawei/secure/android/common/encrypt/aes/CipherUtil.java:19`
  `private static final String c = "AES/CBC/PKCS5Padding";`
- `sources/com/huawei/secure/android/common/encrypt/keystore/rsa/RSAEncryptKS.java:35`
  `private static final String c = "RSA/ECB/OAEPWithSHA-256AndMGF1Padding";`
- `sources/com/huawei/secure/android/common/encrypt/rsa/RSAEncrypt.java:25`
  `private static final String a = "RSA/ECB/OAEPWithSHA-256AndMGF1Padding";`
- `sources/com/kuaishou/weapon/p0/b.java:16`
  `private static final String d = "AES/CBC/PKCS5Padding";`
- `sources/com/kuaishou/weapon/p0/b.java:77`
  `java.lang.String r1 = "AES/CBC/PKCS5Padding"`
- `sources/com/kwad/sdk/core/a/b.java:20`
  `Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");`
- `sources/com/mobile/auth/b/a.java:18`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/mobile/auth/b/a.java:78`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/mobile/auth/b/d.java:12`
  `private static String b = "RSA/ECB/PKCS1Padding";`
- `sources/com/mobile/auth/gatewayauth/utils/f.java:13`
  `Cipher cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding");`
- `sources/com/uc/crashsdk/a/c.java:57`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/umeng/umverify/utils/e.java:15`
  `private static String a = "RSA/ECB/PKCS1Padding";`
- `sources/com/vivo/push/util/a.java:48`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/vivo/push/util/f.java:22`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/xiaomi/push/h.java:18`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/xiaomi/push/service/bt.java:34`
  `Cipher cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding");`
- `sources/io/dcloud/h/a/d/b/a.java:35`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/io/dcloud/h/a/d/b/a.java:47`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`

## BR061

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/aegon/chrome/net/impl/CronetUrlRequestContext.java:623`
  `String protocol = url.getProtocol();`
- `sources/aegon/chrome/net/urlconnection/CronetHttpURLConnection.java:94`
  `boolean zEquals = url.getProtocol().equals(((HttpURLConnection) CronetHttpURLConnection.this).url.getProtocol());`
- `sources/androidx/constraintlayout/core/state/WidgetFrame.java:297`
  `public boolean setValue(String str, CLElement cLElement) throws CLParsingException {`
- `sources/androidx/constraintlayout/motion/widget/KeyAttributes.java:441`
  `public void setValue(String str, Object obj) {`
- `sources/androidx/constraintlayout/motion/widget/KeyCycle.java:545`
  `public void setValue(String str, Object obj) {`
- `sources/androidx/constraintlayout/motion/widget/KeyTimeCycle.java:439`
  `public void setValue(String str, Object obj) {`
- `sources/androidx/lifecycle/LiveData.java:154`
  `LiveData.this.setValue(obj);`
- `sources/androidx/lifecycle/LiveData.java:316`
  `LiveData.this.setValue(obj2);`
- `sources/cn/jiguang/api/JCoreInterface.java:260`
  `public static void sendData(Context context, String str, int i2, byte[] bArr) {`
- `sources/cn/jiguang/ax/l.java:76`
  `cn.jiguang.ay.f.c("ConfigHandlerManager", "getProtocolVersion - DY not supported");`
- `sources/cn/jiguang/ax/l.java:83`
  `cn.jiguang.ay.f.l("ConfigHandlerManager", "getProtocolVersion failed - DY supported but error: " + th.getMessage());`
- `sources/cn/jiguang/ax/l.java:87`
  `StringBuilder sbD0 = j.a.a.a.a.d0("getProtocolVersion failed - check DY support error: ");`
- `sources/cn/jiguang/bf/g.java:674`
  `cn.jiguang.ay.f.j("JCoreTCPManager", "send hb failed:sendData is null");`
- `sources/cn/jiguang/bi/b.java:348`
  `f.c("NioSSLSocketClient", "sendData failed, send data was null");`
- `sources/cn/jiguang/bi/b.java:355`
  `f.c("NioSSLSocketClient", "sendData failed, data length must less than " + this.p);`
- `sources/cn/jiguang/bi/c.java:96`
  `f.i("NioSocketClient", "sendData failed, send data was null");`
- `sources/cn/jiguang/bi/c.java:103`
  `f.i("NioSocketClient", "sendData failed, data length must less than " + this.f2340j);`
- `sources/cn/jpush/android/d/b.java:67`
  `JCoreHelper.sendData(context, JPushConstants.SDK_TYPE, 4, 3, j3, cn.jpush.android.z.b.a(0, (byte) i2, j2, str));`
- `sources/cn/jpush/android/helper/JCoreHelper.java:164`
  `public static void sendData(Context context, String str, int i2, int i3, long j2, byte[] bArr) {`
- `sources/com/davemorrissey/labs/subscaleview/decoder/SkiaPooledImageRegionDecoder.java:76`
  `entry.setValue(Boolean.TRUE);`
- `sources/com/davemorrissey/labs/subscaleview/decoder/SkiaPooledImageRegionDecoder.java:94`
  `entry.setValue(Boolean.FALSE);`
- `sources/com/efs/sdk/h5pagesdk/UApmJSBridge.java:24`
  `public void sendData(String str) {`
- `sources/com/google/android/gms/auth/api/accounttransfer/AccountTransferClient.java:101`
  `public Task<Void> sendData(String str, byte[] bArr) {`
- `sources/com/huawei/hms/api/HuaweiApiClientImpl.java:162`
  `MessageCodec messageCodecFind = CodecLookup.find(dataBuffer.getProtocol());`
- `sources/com/huawei/hms/api/HuaweiApiClientImpl.java:404`
  `MessageCodec messageCodecFind = CodecLookup.find(dataBuffer.getProtocol());`
- `sources/com/huawei/hms/api/IPCCallback.java:32`
  `MessageCodec messageCodecFind = CodecLookup.find(dataBuffer.getProtocol());`
- `sources/com/huawei/hms/api/IPCTransport.java:36`
  `dataBuffer.addBody(CodecLookup.find(dataBuffer.getProtocol()).encode(this.mEntity, new Bundle()));`
- `sources/com/huawei/hms/api/IPCTransport.java:47`
  `MessageCodec messageCodecFind = CodecLookup.find(dataBuffer2.getProtocol());`
- `sources/com/huawei/hms/core/aidl/DataBuffer.java:55`
  `public int getProtocol() {`
- `sources/com/huawei/hms/hatool/l0.java:58`
  `str = "sendData(): getBytes - Unsupported coding format!!";`
- `sources/com/huawei/secure/android/common/ssl/SASFCompatiableSystemCA.java:102`
  `public String[] getProtocols() {`
- `sources/com/huawei/secure/android/common/ssl/SecureApacheSSLSocketFactory.java:106`
  `public String[] getProtocols() {`
- `sources/com/huawei/secure/android/common/ssl/SecureSSLSocketFactory.java:126`
  `public String[] getProtocols() {`
- `sources/com/huawei/secure/android/common/ssl/SecureSSLSocketFactoryNew.java:132`
  `public String[] getProtocols() {`
- `sources/com/huawei/secure/android/common/ssl/SSFCompatiableSystemCA.java:114`
  `public String[] getProtocols() {`
- `sources/com/kuaishou/weapon/p0/l.java:96`
  `if ("https".equals(url.getProtocol())) {`
- `sources/com/mobile/auth/gatewayauth/AuthUIConfig.java:3162`
  `public String getProtocolAction() {`
- `sources/com/mobile/auth/gatewayauth/AuthUIConfig.java:3171`
  `public int getProtocolColor() {`
- `sources/com/mobile/auth/gatewayauth/AuthUIConfig.java:3180`
  `public int getProtocolGravity() {`
- `sources/com/mobile/auth/gatewayauth/AuthUIConfig.java:3189`
  `public int getProtocolLayoutGravity() {`

## BR062

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/no/nordicsemi/android/dfu/BaseButtonlessDfuImpl.java:22`
  `public void onCharacteristicChanged(BluetoothGatt bluetoothGatt, BluetoothGattCharacteristic bluetoothGattCharacteristic) {`
- `sources/no/nordicsemi/android/dfu/BaseDfuImpl.java:67`
  `public void onCharacteristicRead(BluetoothGatt bluetoothGatt, BluetoothGattCharacteristic bluetoothGattCharacteristic, int i2) {`
- `sources/no/nordicsemi/android/dfu/BaseDfuImpl.java:301`
  `StringBuilder sbD0 = a.d0("gatt.setCharacteristicNotification(");`
- `sources/no/nordicsemi/android/dfu/BaseDfuImpl.java:305`
  `bluetoothGatt.setCharacteristicNotification(bluetoothGattCharacteristic, true);`
- `sources/no/nordicsemi/android/dfu/LegacyDfuImpl.java:61`
  `public void onCharacteristicChanged(BluetoothGatt bluetoothGatt, BluetoothGattCharacteristic bluetoothGattCharacteristic) {`
- `sources/no/nordicsemi/android/dfu/SecureDfuImpl.java:80`
  `public void onCharacteristicChanged(BluetoothGatt bluetoothGatt, BluetoothGattCharacteristic bluetoothGattCharacteristic) {`

## BR063

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/camera/core/internal/utils/ImageUtil.java:219`
  `byte[] bArrJpegImageToJpegByteArray = jpegImageToJpegByteArray(imageProxy);`
- `sources/androidx/exifinterface/media/ExifInterface.java:2237`
  `byte[] bArr = this.n;`
- `sources/androidx/exifinterface/media/ExifInterface.java:3604`
  `byte[] r7 = androidx.exifinterface.media.ExifInterface.p0`
- `sources/androidx/exifinterface/media/ExifInterface.java:3608`
  `byte[] r7 = new byte[r7]`
- `sources/androidx/exifinterface/media/ExifInterface.java:3613`
  `byte[] r4 = androidx.exifinterface.media.ExifInterface.p0`
- `sources/androidx/work/impl/background/systemalarm/CommandHandler.java:74`
  `Logger.get().debug(ConstraintsCommandHandler.e, String.format("Creating a delay_met command for workSpec with id (%s)", str2), new Throwable[0]);`
- `sources/androidx/work/impl/model/WorkProgressDao_Impl.java:39`
  `byte[] byteArrayInternal = Data.toByteArrayInternal(workProgress.mProgress);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:72`
  `byte[] byteArrayInternal = Data.toByteArrayInternal(workSpec.input);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:78`
  `byte[] byteArrayInternal2 = Data.toByteArrayInternal(workSpec.output);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:114`
  `byte[] bArrContentUriTriggersToByteArray = WorkTypeConverters.contentUriTriggersToByteArray(constraints.getContentUriTriggers());`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:2051`
  `byte[] byteArrayInternal = Data.toByteArrayInternal(data);`
- `sources/cn/jiguang/ao/b.java:45`
  `f.c("JWakeCmd", jSONObject == null ? "executeWakeAction: [JWakeCmd] from heartBeat" : "executeWakeAction: [JWakeCmd] from cmd");`
- `sources/cn/jiguang/ax/a.java:196`
  `byte[] bytes = str.getBytes("UTF-8");`
- `sources/cn/jiguang/ba/f.java:153`
  `byte[] bArr = (byte[]) obj;`
- `sources/cn/jiguang/ba/f.java:271`
  `byte[] bytes = str.getBytes("UTF-8");`
- `sources/cn/jiguang/be/o.java:99`
  `ByteBuffer[] byteBufferArr = {ByteBuffer.wrap(new byte[]{(byte) (bArr.length >>> 8), (byte) (bArr.length & 255)}), ByteBuffer.wrap(bArr)};`
- `sources/cn/jiguang/bf/g.java:670`
  `byte[] bArrA = cn.jiguang.bh.b.a(this.p, cn.jiguang.bh.b.a(lValueOf.longValue(), JConstants.tcpSessionId, jF, (short) 1, i2, JConstants.DEFAULT_HEARTBEAT_INTERVAL));`
- `sources/com/alibaba/fastjson/parser/deserializer/ASMDeserializerFactory.java:48`
  `public class ASMDeserializerFactory implements Opcodes {`
- `sources/com/alibaba/fastjson/parser/deserializer/ASMDeserializerFactory.java:917`
  `byte[] bArrF = classWriter2.f();`
- `sources/com/alibaba/fastjson/serializer/ASMSerializerFactory.java:31`
  `public class ASMSerializerFactory implements Opcodes {`
- `sources/com/bumptech/glide/load/resource/bitmap/Downsampler.java:230`
  `byte[] bArr = (byte[]) this.c.b(65536, byte[].class);`
- `sources/com/efs/sdk/base/newsharedpreferences/SharedPreferencesNewImpl.java:411`
  `bArr = new byte[this.mMap.size() * 5][];`
- `sources/com/efs/sdk/base/newsharedpreferences/SharedPreferencesNewImpl.java:432`
  `bArr[i3 + 4] = new byte[]{(byte) getObjectType(value)};`
- `sources/com/efs/sdk/base/newsharedpreferences/SharedPreferencesNewImpl.java:501`
  `byte[] bArr2 = new byte[4];`
- `sources/com/efs/sdk/base/newsharedpreferences/SharedPreferencesNewImpl.java:779`
  `byte[] bArr = new byte[length];`
- `sources/com/efs/sdk/base/newsharedpreferences/SharedPreferencesNewImpl.java:780`
  `byte[] bArrIntToBytes = ByteIntUtils.intToBytes(length);`
- `sources/com/facebook/common/webp/WebpSupportStatus.java:14`
  `public static final byte[] c = a("RIFF");`
- `sources/com/facebook/common/webp/WebpSupportStatus.java:15`
  `public static final byte[] d = a("WEBP");`
- `sources/com/facebook/common/webp/WebpSupportStatus.java:16`
  `public static final byte[] e = a("VP8 ");`
- `sources/com/facebook/common/webp/WebpSupportStatus.java:17`
  `public static final byte[] f = a("VP8L");`
- `sources/com/facebook/common/webp/WebpSupportStatus.java:18`
  `public static final byte[] g = a("VP8X");`
- `sources/com/facebook/imagepipeline/bitmaps/EmptyJpegGenerator.java:11`
  `public static final byte[] b = {-1, -40, -1, -37, 0, 67, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, ...`
- `sources/com/facebook/imagepipeline/bitmaps/EmptyJpegGenerator.java:12`
  `public static final byte[] c = {3, 1, 34, 0, 2, 17, 0, 3, 17, 0, -1, -60, 0, 31, 0, 0, 1, 5, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1, -60, 0, -75, cv.n, 0, 2, 1, 3, 3, 2, 4, 3, 5, 5, 4, 4, 0, 0, 1, 125, 1, 2, 3, 0, 4, 17, 5, 18, 33, 49, 65, 6, 19, 81, 97, 7, 3...`
- `sources/com/facebook/imagepipeline/bitmaps/HoneycombBitmapFactory.java:45`
  `byte[] bArr = EmptyJpegGenerator.b;`
- `sources/com/facebook/imagepipeline/bitmaps/HoneycombBitmapFactory.java:47`
  `byte[] bArr2 = EmptyJpegGenerator.c;`
- `sources/com/facebook/imagepipeline/platform/KitKatPurgeableDecoder.java:36`
  `byte[] bArr = (byte[]) closeableReferenceW.n();`
- `sources/com/facebook/imagepipeline/platform/KitKatPurgeableDecoder.java:52`
  `byte[] bArr = DalvikPurgeableDecoder.f(closeableReference, i2) ? null : DalvikPurgeableDecoder.b;`
- `sources/com/github/faucamp/simplertmp/amf/AmfObject.java:35`
  `byte[] bArr2 = c;`
- `sources/com/github/faucamp/simplertmp/io/RtmpConnection.java:167`
  `rtmpConnection.b((Command) rtmpPacketA);`
- `sources/com/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore.java:236`
  `byte[] blob = cursorQuery.getBlob(0);`

## BR064

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/aegon/chrome/net/X509Util.java:259`
  `Log.e(TAG, "Anchor " + str + " not an X509Certificate: " + certificate.getClass().getName());`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:555`
  `return useCase.getName() + useCase.hashCode();`
- `sources/androidx/collection/LruCache.java:176`
  `throw new java.lang.IllegalStateException(getClass().getName() + ".sizeOf() is reporting inconsistent results!");`
- `sources/androidx/core/app/NotificationCompat.java:3338`
  `bundle.putCharSequence(NotificationCompat.EXTRA_SELF_DISPLAY_NAME, this.g.getName());`
- `sources/androidx/core/app/NotificationCompat.java:3468`
  `return this.g.getName();`
- `sources/androidx/core/app/NotificationCompat.java:3675`
  `if (!TextUtils.isEmpty(person.getName())) {`
- `sources/androidx/core/content/FileProvider.java:212`
  `String name = fileProviderPathsMetaData.getName();`
- `sources/androidx/core/content/res/FontResourcesParserCompat.java:143`
  `if (!xmlPullParser.getName().equals(TypefaceUtil.FONT_CACHE_DIR_NAME)) {`
- `sources/androidx/core/util/DebugUtils.java:16`
  `if (simpleName.length() <= 0 && (iLastIndexOf = (simpleName = obj.getClass().getName()).lastIndexOf(46)) > 0) {`
- `sources/androidx/savedstate/SavedStateRegistry.java:73`
  `savedStateProvider.a.add(cls.getName());`
- `sources/androidx/work/OneTimeWorkRequest.java:15`
  `this.c.inputMergerClassName = OverwritingInputMerger.class.getName();`
- `sources/cn/jiguang/az/b.java:18`
  `sbK0.append(file.getName());`
- `sources/cn/jiguang/bv/a.java:1114`
  `cn.jiguang.ay.f.c("AndroidUtil", "ssid change,so update mac");`
- `sources/cn/jiguang/o/g.java:60`
  `cn.jiguang.ay.f.c("JDeviceMac", "get mac: " + strB);`
- `sources/cn/jiguang/o/g.java:62`
  `cn.jiguang.ay.f.c("JDeviceMac", "l mac is empty");`
- `sources/cn/jiguang/o/g.java:66`
  `cn.jiguang.ay.f.c("JDeviceMac", "last mac is same as l mac, mac: " + strB);`
- `sources/cn/jiguang/o/g.java:123`
  `StringBuilder sbD0 = j.a.a.a.a.d0("it need not report, because no wifi info or mac, mac: ");`
- `sources/cn/jiguang/o/g.java:142`
  `j.a.a.a.a.h(th, j.a.a.a.a.d0("ssid mac report failed, "), "JDeviceMac");`
- `sources/com/alibaba/fastjson/util/ASMClassLoader.java:73`
  `b.put(cls.getName(), cls);`
- `sources/com/alibaba/fastjson/util/JavaBeanInfo.java:279`
  `if (cls.getName().equals("org.springframework.security.web.savedrequest.DefaultSavedRequest")) {`
- `sources/com/alibaba/fastjson/util/TypeUtils.java:402`
  `C.put(cls.getName(), cls);`
- `sources/com/bumptech/glide/Glide.java:388`
  `sbD02.append(glideModule3.getClass().getName());`
- `sources/com/bumptech/glide/load/engine/ResourceCacheKey.java:98`
  `bArrE = this.g.getName().getBytes(Key.a);`
- `sources/com/davemorrissey/labs/subscaleview/decoder/SkiaPooledImageRegionDecoder.java:140`
  `return Pattern.matches("cpu[0-9]+", file.getName());`
- `sources/com/efs/sdk/base/core/b/a.java:49`
  `sb.append(file.getName());`
- `sources/com/efs/sdk/base/core/b/a.java:54`
  `if (!file.getName().startsWith("wa_")) {`
- `sources/com/efs/sdk/base/core/c/d.java:111`
  `Log.w("efs.cache", "file upload error, name is " + file2.getName());`
- `sources/com/facebook/cache/disk/DefaultDiskStorage.java:289`
  `java.lang.String r0 = r9.getName()`
- `sources/com/facebook/common/references/CloseableReference.java:47`
  `objArr[2] = objC == null ? null : objC.getClass().getName();`
- `sources/com/facebook/common/references/DefaultCloseableReference.java:34`
  `objArr[2] = tC == null ? null : tC.getClass().getName();`
- `sources/com/facebook/common/references/FinalizerCloseableReference.java:41`
  `objArr[2] = tC == null ? null : tC.getClass().getName();`
- `sources/com/facebook/imagepipeline/cache/DefaultCacheKeyFactory.java:35`
  `name = postprocessor.getClass().getName();`
- `sources/com/facebook/imagepipeline/core/CloseableReferenceFactory.java:24`
  `String name = objC != null ? objC.getClass().getName() : "<value is null>";`
- `sources/com/facebook/imagepipeline/request/BasePostprocessor.java:48`
  `public String getName() {`
- `sources/com/facebook/imagepipeline/request/Postprocessor.java:13`
  `String getName();`
- `sources/com/google/android/gms/internal/common/zzy.java:32`
  `String name = obj.getClass().getName();`
- `sources/com/google/android/material/animation/MotionSpec.java:113`
  `return '\n' + getClass().getName() + Operators.BLOCK_START + Integer.toHexString(System.identityHashCode(this)) + " timings: " + this.a + "}\n";`
- `sources/com/google/android/material/animation/MotionTiming.java:72`
  `sb.append(getClass().getName());`
- `sources/com/google/firebase/FirebaseApp.java:233`
  `sbD0.append(getName());`
- `sources/com/google/firebase/FirebaseApp.java:239`
  `sbD02.append(getName());`
- `sources/com/google/gson/FieldNamingPolicy.java:12`
  `return field.getName();`
- `sources/com/google/gson/internal/bind/ReflectiveTypeAdapterFactory.java:127`
  `sbD0.append(field.getDeclaringClass().getName());`
- `sources/com/google/gson/internal/bind/ReflectiveTypeAdapterFactory.java:129`
  `sbD0.append(field.getName());`
- `sources/com/google/gson/internal/bind/TypeAdapters.java:339`
  `sbD0.append(cls.getName());`
- `sources/com/huawei/hms/activity/ForegroundIntentBuilder.java:51`
  `Intent intentStartBridgeActivity = BridgeActivity.getIntentStartBridgeActivity(this.a, ForegroundBusDelegate.class.getName());`
- `sources/com/huawei/hms/adapter/AvailableAdapter.java:114`
  `activity.startActivity(BridgeActivity.getIntentStartBridgeActivity(activity, AppSpoofResolution.class.getName()));`
- `sources/com/huawei/hms/adapter/AvailableAdapter.java:136`
  `Intent intentStartBridgeActivity = BridgeActivity.getIntentStartBridgeActivity(activity, UpdateAdapter.class.getName());`
- `sources/com/huawei/hms/adapter/AvailableAdapter.java:171`
  `activity.startActivity(BridgeActivity.getIntentStartBridgeActivity(activity, NotInstalledHmsAdapter.class.getName()));`
- `sources/com/huawei/hms/adapter/BaseAdapter.java:482`
  `Intent intentStartBridgeActivity = BridgeActivity.getIntentStartBridgeActivity(activity, BaseResolutionAdapter.class.getName());`
- `sources/com/huawei/hms/api/HuaweiApiAvailabilityImpl.java:125`
  `Intent intentStartBridgeActivity = BridgeActivity.getIntentStartBridgeActivity(activity, ResolutionDelegate.class.getName());`
- `sources/com/huawei/hms/health/aace.java:234`
  `String name = activityRecord.getName();`
- `sources/com/huawei/hms/hihealth/data/ActivityRecord.java:639`
  `SafeParcelWriter.writeString(parcel, 1, getName(), false);`
- `sources/com/huawei/hms/hihealth/data/DataCollector.java:236`
  `sb.append(this.dataType.getName());`
- `sources/com/huawei/secure/android/common/ssl/hostname/BrowserCompatHostnameVerifier.java:15`
  `g.a("", "verify: certificate is : " + x509Certificate.getSubjectDN().getName());`
- `sources/com/huawei/secure/android/common/ssl/hostname/StrictHostnameVerifier.java:15`
  `g.a("", "verify: certificate is : " + x509Certificate.getSubjectDN().getName());`
- `sources/com/kwad/components/core/c/d.java:87`
  `String name = cVar.getName();`
- `sources/com/kwad/components/core/c/l.java:64`
  `public final String getName() {`
- `sources/com/kwad/library/b/c/a.java:188`
  `String name = contextA != null ? contextA.getClass().getName() : "";`
- `sources/com/kwad/sdk/api/core/fragment/DelegateFragment.java:229`
  `bundle.putString(REAL_BASE_CLASS, this.mBase.getClass().getName());`
- `sources/com/kwad/sdk/api/core/fragment/FileProvider.java:201`
  `String name = xmlResourceParserLoadXmlMetaData.getName();`
- `sources/com/kwad/sdk/api/loader/Wrapper.java:102`
  `String name = context2 != null ? context2.getClass().getName() : "";`
- `sources/com/kwad/sdk/collector/AppStatusRules.java:157`
  `public String getName() {`
- `sources/com/kwad/sdk/core/diskcache/ApkCacheManager.java:147`
  `if (file.getName().endsWith(UpdateConstants.LOCAL_APK_FILE)) {`
- `sources/com/kwad/sdk/core/videocache/a/b.java:27`
  `file2 = new File(file.getParentFile(), file.getName() + ".download");`
- `sources/com/kwad/sdk/core/videocache/a/b.java:37`
  `return file.getName().endsWith(".download");`
- `sources/com/kwad/sdk/core/videocache/a/b.java:75`
  `File file = new File(this.file.getParentFile(), this.file.getName().substring(0, this.file.getName().length() - 9));`
- `sources/com/kwad/sdk/crash/handler/b.java:101`
  `return file.getName().endsWith(".dump");`
- `sources/com/kwad/sdk/crash/report/upload/b.java:37`
  `String name = file.getName();`
- `sources/com/kwad/sdk/crash/report/upload/b.java:56`
  `httpURLConnection2.setRequestProperty("file-type", Operators.DOT_STR + r.getExtension(file.getName()));`
- `sources/com/kwad/sdk/crash/report/upload/d.java:23`
  `map.put("mLogUUID", g.hc(file.getName()));`
- `sources/com/kwad/sdk/crash/report/upload/d.java:25`
  `fVar.bHj = r.getExtension(file.getName());`
- `sources/com/kwad/sdk/crash/utils/g.java:416`
  `exceptionMessage.mThreadName = Thread.currentThread().getName();`
- `sources/com/kwad/sdk/o/i.java:272`
  `String name = context2 != null ? context2.getClass().getName() : "";`
- `sources/com/kwad/sdk/utils/t.java:272`
  `sbJ0.append(declaredMethod.getName());`
- `sources/com/kwai/player/KwaiBluetoothDetector.java:94`
  `kwaiBluetoothDeviceInfo.mName = bluetoothDevice.getName();`
- `sources/com/kwai/player/KwaiBluetoothDetector.java:95`
  `kwaiBluetoothDeviceInfo.mAddress = bluetoothDevice.getAddress();`
- `sources/com/kwai/player/KwaiBluetoothDetector.java:103`
  `kwaiBluetoothDeviceInfo.mName = bluetoothDevice2.getName();`
- `sources/com/kwai/player/KwaiBluetoothDetector.java:104`
  `kwaiBluetoothDeviceInfo.mAddress = bluetoothDevice2.getAddress();`
- `sources/com/lxj/xpopup/util/XPopupUtils.java:113`
  `contentValues.put("_display_name", file2.getName());`
- `sources/com/mobile/auth/gatewayauth/manager/d.java:256`
  `map.put("deviceName", com.mobile.auth.gatewayauth.utils.d.c());`

## BR065

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/com/ss/bluetooth/blecore/scans/BluetoothBaseAdapter.java:218`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i2) {`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothBaseAdapter.java:224`
  `Log.i("status", "onServicesDiscovered");`
- `sources/no/nordicsemi/android/dfu/DfuBaseService.java:355`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i2) {`

## BR066

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/work/impl/foreground/SystemForegroundService.java:147`
  `systemForegroundDispatcher.b.cancelWorkById(UUID.fromString(stringExtra2));`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:21`
  `public static final ParcelUuid BASE_UUID = ParcelUuid.fromString("00000000-0000-1000-8000-00805F9B34FB");`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:41`
  `private JSONArray advertisServiceUUIDs;`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:58`
  `setAdvertisServiceUUIDs(list2Str(scanResult.getScanRecord().getServiceUuids()));`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:60`
  `setAdvertisServiceUUIDs(new JSONArray());`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:116`
  `setAdvertisServiceUUIDs(new org.json.JSONArray());`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:135`
  `private int parseServiceUuid(byte[] bArr, int i2, int i3, int i4, List<ParcelUuid> list) {`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:148`
  `public JSONArray getAdvertisServiceUUIDs() {`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:149`
  `return this.advertisServiceUUIDs;`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:198`
  `public void setAdvertisServiceUUIDs(JSONArray jSONArray) {`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:199`
  `this.advertisServiceUUIDs = jSONArray;`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:229`
  `jSONObject.put("advertisServiceUUIDs", this.advertisServiceUUIDs);`
- `sources/com/ss/bluetooth/blecore/DCBluetoothDevice.java:255`
  `this.advertisServiceUUIDs = jSONArray;`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothBaseAdapter.java:72`
  `this.SERVICE_UUID = UUID.fromString("0000fff0-0000-1000-8000-00805f9b34fb");`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothBaseAdapter.java:73`
  `this.CHARACTERISTIC_WRITE_UUID = UUID.fromString("0000fff2-0000-1000-8000-00805f9b34fb");`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothBaseAdapter.java:74`
  `this.CHARACTERISTIC_NOTIFY_UUID = UUID.fromString("0000fff1-0000-1000-8000-00805f9b34fb");`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothBaseAdapter.java:75`
  `this.TAP_SERVICE_UUID = UUID.fromString("0783b03e-8535-b5a0-7140a-304d2495cb7");`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothBaseAdapter.java:76`
  `this.TAP_CHARACTERISTIC_NOTIFY_WRITE_UUID = UUID.fromString("0783b03e-8535-b5a0-7140-a304d2495cb8");`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothBaseAdapter.java:77`
  `this.SERVICE_UPDATE_UUID = UUID.fromString("0000180A-0000-1000-8000-00805f9b34fb");`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothBaseAdapter.java:78`
  `this.CHARACTERISTIC_UPDATE_UUID = UUID.fromString("00002A28-0000-1000-8000-00805f9b34fb");`
- `sources/com/ss/bluetooth/blecore/scans/BluetoothBaseAdapter.java:129`
  `BluetoothGattDescriptor descriptor = bluetoothGattCharacteristic.getDescriptor(UUID.fromString("00002902-0000-1000-8000-00805f9b34fb"));`
- `sources/no/nordicsemi/android/dfu/BaseCustomDfuImpl.java:52`
  `BluetoothGattCharacteristic characteristic = bluetoothGatt.getService(baseCustomDfuImpl.getDfuServiceUUID()).getCharacteristic(BaseCustomDfuImpl.this.getPacketCharacteristicUUID());`
- `sources/no/nordicsemi/android/dfu/BaseCustomDfuImpl.java:96`
  `} else if (!bluetoothGattCharacteristic.getUuid().equals(BaseCustomDfuImpl.this.getPacketCharacteristicUUID())) {`
- `sources/no/nordicsemi/android/dfu/BaseCustomDfuImpl.java:284`
  `public abstract UUID getControlPointCharacteristicUUID();`
- `sources/no/nordicsemi/android/dfu/BaseCustomDfuImpl.java:286`
  `public abstract UUID getDfuServiceUUID();`
- `sources/no/nordicsemi/android/dfu/BaseCustomDfuImpl.java:288`
  `public abstract UUID getPacketCharacteristicUUID();`
- `sources/no/nordicsemi/android/dfu/LegacyDfuImpl.java:200`
  `public UUID getControlPointCharacteristicUUID() {`
- `sources/no/nordicsemi/android/dfu/LegacyDfuImpl.java:205`
  `public UUID getDfuServiceUUID() {`
- `sources/no/nordicsemi/android/dfu/LegacyDfuImpl.java:210`
  `public UUID getPacketCharacteristicUUID() {`
- `sources/no/nordicsemi/android/dfu/SecureDfuImpl.java:617`
  `public UUID getControlPointCharacteristicUUID() {`
- `sources/no/nordicsemi/android/dfu/SecureDfuImpl.java:622`
  `public UUID getDfuServiceUUID() {`
- `sources/no/nordicsemi/android/dfu/SecureDfuImpl.java:627`
  `public UUID getPacketCharacteristicUUID() {`

## BR067

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/androidx/camera/view/CameraController.java:701`
  `public void setPinchToZoomEnabled(boolean z) {`
- `sources/com/kwai/player/vr/KwaiGestureHelper.java:242`
  `public void setPinchEnabled(boolean z) {`
- `sources/com/kwai/player/vr/KwaiVR.java:46`
  `public Builder setPinchEnabled(boolean z) {`
- `sources/com/kwai/player/vr/KwaiVR.java:91`
  `this.mGestureHelper.setPinchEnabled(this.mPinchEnabled);`
- `sources/com/kwai/player/vr/KwaiVR.java:268`
  `public void setPinchEnabled(boolean z) {`
- `sources/com/kwai/player/vr/KwaiVR.java:270`
  `this.mGestureHelper.setPinchEnabled(z);`
- `sources/com/kwai/video/player/kwai_player/KwaiMediaPlayer.java:1389`
  `KwaiVR kwaiVRBuild = KwaiVR.builder().setInteractive(this.mInteractivemode).setPinchEnabled(true).setContext(this.mContext).setStereoType(this.mStereoType).build();`
- `sources/no/nordicsemi/android/dfu/BaseCustomDfuImpl.java:263`
  `removeBond();`
- `sources/no/nordicsemi/android/dfu/BaseCustomDfuImpl.java:266`
  `if (booleanExtra2 && (this.mFileType & 4) > 0 && !createBond()) {`
- `sources/no/nordicsemi/android/dfu/BaseDfuImpl.java:226`
  `private boolean createBondApi18(@NonNull BluetoothDevice bluetoothDevice) {`
- `sources/no/nordicsemi/android/dfu/BaseDfuImpl.java:228`
  `Method method = bluetoothDevice.getClass().getMethod("createBond", new Class[0]);`
- `sources/no/nordicsemi/android/dfu/BaseDfuImpl.java:229`
  `this.mService.sendLogBroadcast(0, "gatt.getDevice().createBond() (hidden)");`
- `sources/no/nordicsemi/android/dfu/BaseDfuImpl.java:258`
  `public boolean createBond() {`
- `sources/no/nordicsemi/android/dfu/BaseDfuImpl.java:262`
  `this.mService.sendLogBroadcast(0, "gatt.getDevice().createBond()");`
- `sources/no/nordicsemi/android/dfu/BaseDfuImpl.java:263`
  `boolean zCreateBond = device.createBond();`
- `sources/no/nordicsemi/android/dfu/BaseDfuImpl.java:266`
  `while (zCreateBond) {`
- `sources/no/nordicsemi/android/dfu/BaseDfuImpl.java:276`
  `return zCreateBond;`
- `sources/no/nordicsemi/android/dfu/BaseDfuImpl.java:487`
  `public boolean removeBond() {`
- `sources/no/nordicsemi/android/dfu/BaseDfuImpl.java:495`
  `Method method = device.getClass().getMethod("removeBond", new Class[0]);`
- `sources/no/nordicsemi/android/dfu/BaseDfuImpl.java:497`
  `this.mService.sendLogBroadcast(0, "gatt.getDevice().removeBond() (hidden)");`

## BR068

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/com/google/android/gms/auth/api/accounttransfer/AccountTransferStatusCodes.java:7`
  `public static final int CHALLENGE_NOT_ALLOWED = 20503;`
- `sources/com/google/android/gms/auth/api/accounttransfer/AccountTransferStatusCodes.java:24`
  `case CHALLENGE_NOT_ALLOWED /* 20503 */:`
- `sources/com/google/android/gms/auth/api/accounttransfer/AccountTransferStatusCodes.java:25`
  `return "CHALLENGE_NOT_ALLOWED";`
- `sources/com/google/android/gms/auth/api/accounttransfer/DeviceMetaData.java:20`
  `@SafeParcelable.Field(getter = "isChallengeAllowed", id = 4)`
- `sources/com/google/android/gms/auth/api/accounttransfer/DeviceMetaData.java:38`
  `public boolean isChallengeAllowed() {`
- `sources/com/google/android/gms/auth/api/accounttransfer/DeviceMetaData.java:52`
  `SafeParcelWriter.writeBoolean(parcel, 4, isChallengeAllowed());`
- `sources/com/google/android/gms/internal/auth/zzah.java:12`
  `@SafeParcelable.Class(creator = "UserChallengeRequestCreator")`
- `sources/dc/squareup/okhttp3/Challenge.java:7`
  `public final class Challenge {`
- `sources/dc/squareup/okhttp3/Challenge.java:9`
  `if (!(obj instanceof Challenge)) {`
- `sources/dc/squareup/okhttp3/Challenge.java:12`
  `Objects.requireNonNull((Challenge) obj);`

## BR069

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/cn/jiguang/bv/a.java:1114`
  `cn.jiguang.ay.f.c("AndroidUtil", "ssid change,so update mac");`
- `sources/com/alibaba/fastjson/serializer/MiscCodec.java:245`
  `InetAddress address = inetSocketAddress.getAddress();`
- `sources/com/umeng/umzid/d.java:47`
  `editorEdit.putString("mac", strB).commit();`

## BR071

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:141`
  `android:allowBackup="true"`

## BR072

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `resources/AndroidManifest.xml:44`
  `<action android:name="com.huawei.hms.core.aidlservice"/>`
- `resources/AndroidManifest.xml:47`
  `<action android:name="com.huawei.hms.core"/>`
- `resources/AndroidManifest.xml:205`
  `android:name="com.huawei.hms.client.appid"`
- `resources/AndroidManifest.xml:498`
  `<action android:name="cn.jpush.android.intent.REGISTRATION"/>`
- `resources/AndroidManifest.xml:499`
  `<action android:name="cn.jpush.android.intent.MESSAGE_RECEIVED"/>`
- `resources/AndroidManifest.xml:500`
  `<action android:name="cn.jpush.android.intent.NOTIFICATION_RECEIVED"/>`
- `resources/AndroidManifest.xml:501`
  `<action android:name="cn.jpush.android.intent.NOTIFICATION_OPENED"/>`
- `resources/AndroidManifest.xml:502`
  `<action android:name="cn.jpush.android.intent.NOTIFICATION_CLICK_ACTION"/>`
- `resources/AndroidManifest.xml:503`
  `<action android:name="cn.jpush.android.intent.CONNECTION"/>`
- `resources/AndroidManifest.xml:512`
  `<action android:name="cn.jpush.android.intent.RECEIVE_MESSAGE"/>`
- `resources/AndroidManifest.xml:764`
  `android:name="com.huawei.hms.hihealth.activity.HealthKitMainActivity"`
- `resources/AndroidManifest.xml:767`
  `android:name="com.huawei.hms.client.service.name:health"`
- `resources/AndroidManifest.xml:770`
  `android:name="com.huawei.hms.min_api_level:hihealth-base:hihealth"`
- `resources/AndroidManifest.xml:774`
  `android:name="com.mobile.auth.gatewayauth.LoginAuthActivity"`
- `resources/AndroidManifest.xml:780`
  `android:name="com.mobile.auth.gatewayauth.activity.AuthWebVeiwActivity"`
- `resources/AndroidManifest.xml:796`
  `android:name="com.huawei.hms.update.provider.UpdateProvider"`
- `resources/AndroidManifest.xml:820`
  `android:name="cn.jpush.android.ui.PopWinActivity"`
- `resources/AndroidManifest.xml:824`
  `<action android:name="cn.jpush.android.ui.PopWinActivity"/>`
- `resources/AndroidManifest.xml:830`
  `android:name="cn.jpush.android.ui.PushActivity"`
- `resources/AndroidManifest.xml:834`
  `<action android:name="cn.jpush.android.ui.PushActivity"/>`
- `resources/AndroidManifest.xml:840`
  `android:name="cn.jpush.android.service.PushService"`
- `resources/AndroidManifest.xml:845`
  `<action android:name="cn.jpush.android.intent.REGISTER"/>`
- `resources/AndroidManifest.xml:846`
  `<action android:name="cn.jpush.android.intent.REPORT"/>`
- `resources/AndroidManifest.xml:847`
  `<action android:name="cn.jpush.android.intent.PushService"/>`
- `resources/AndroidManifest.xml:848`
  `<action android:name="cn.jpush.android.intent.PUSH_TIME"/>`
- `resources/AndroidManifest.xml:852`
  `android:name="cn.jpush.android.service.DaemonService"`
- `resources/AndroidManifest.xml:856`
  `<action android:name="cn.jpush.android.intent.DaemonService"/>`
- `resources/AndroidManifest.xml:862`
  `android:name="cn.jpush.android.service.DActivity"`
- `resources/AndroidManifest.xml:867`
  `<action android:name="cn.jpush.android.intent.DActivity"/>`
- `resources/AndroidManifest.xml:872`
  `android:name="cn.jpush.android.service.PushReceiver"`
- `resources/AndroidManifest.xml:876`
  `<action android:name="cn.jpush.android.intent.NOTIFICATION_RECEIVED_PROXY"/>`
- `resources/AndroidManifest.xml:881`
  `android:name="cn.jpush.android.service.AlarmReceiver"`
- `resources/AndroidManifest.xml:884`
  `android:name="cn.jpush.android.service.SchedulerReceiver"`
- `resources/AndroidManifest.xml:887`
  `android:name="cn.jpush.android.service.DataProvider"`
- `resources/AndroidManifest.xml:892`
  `android:name="cn.jpush.android.service.DownloadProvider"`
- `resources/AndroidManifest.xml:897`
  `android:name="cn.jpush.android.service.JNotifyActivity"`
- `resources/AndroidManifest.xml:901`
  `<action android:name="cn.jpush.android.intent.JNotifyActivity"/>`
- `resources/AndroidManifest.xml:918`
  `android:name="cn.jpush.android.asus.AsusPushMessageReceiver"`
- `resources/AndroidManifest.xml:927`
  `android:name="cn.jpush.android.service.InitProvider"`
- `resources/AndroidManifest.xml:931`
  `android:name="com.huawei.hms.support.api.push.PushMsgReceiver"`
- `resources/AndroidManifest.xml:941`
  `android:name="com.huawei.hms.support.api.push.PushReceiver"`
- `resources/AndroidManifest.xml:951`
  `android:name="com.huawei.hms.support.api.push.service.HmsMsgService"`
- `resources/AndroidManifest.xml:962`
  `android:name="com.huawei.hms.support.api.push.PushProvider"`
- `resources/AndroidManifest.xml:968`
  `android:name="com.huawei.hms.client.service.name:push"`
- `resources/AndroidManifest.xml:971`
  `android:name="com.huawei.hms.min_api_level:push:push"`
- `resources/AndroidManifest.xml:974`
  `android:name="com.huawei.hms.support.api.push.TransActivity"`
- `resources/AndroidManifest.xml:977`
  `android:name="cn.jpush.android.service.PluginHuaweiPlatformsService"`
- `resources/AndroidManifest.xml:984`
  `android:name="cn.jpush.android.service.PluginFCMMessagingService"`
- `resources/AndroidManifest.xml:991`
  `android:name="cn.jpush.android.service.PluginVivoMessageReceiver"`
- `resources/AndroidManifest.xml:1035`
  `android:name="com.xiaomi.mipush.sdk.PushMessageHandler"`
- `resources/AndroidManifest.xml:1039`
  `android:name="com.xiaomi.mipush.sdk.MessageHandleService"`
- `resources/AndroidManifest.xml:1050`
  `android:name="cn.jpush.android.service.PluginXiaomiPlatformsReceiver"`
- `resources/AndroidManifest.xml:1053`
  `<action android:name="com.xiaomi.mipush.RECEIVE_MESSAGE"/>`
- `resources/AndroidManifest.xml:1056`
  `<action android:name="com.xiaomi.mipush.MESSAGE_ARRIVED"/>`
- `resources/AndroidManifest.xml:1059`
  `<action android:name="com.xiaomi.mipush.ERROR"/>`
- `resources/AndroidManifest.xml:1064`
  `android:name="com.xiaomi.mipush.sdk.NotificationClickedActivity"`
- `resources/AndroidManifest.xml:1074`
  `android:name="cn.jpush.android.service.JHonorService"`
- `resources/AndroidManifest.xml:1085`
  `android:name="com.huawei.hms.hwid.internal.ui.activity.HwIdSignInHubActivity"`
- `resources/AndroidManifest.xml:1091`
  `android:name="com.huawei.hms.account.internal.ui.activity.AccountSignInHubActivity"`
- `resources/AndroidManifest.xml:1095`
  `android:name="com.huawei.hms.client.service.name:hwid"`
- `resources/AndroidManifest.xml:1098`
  `android:name="com.huawei.hms.min_api_level:hwid:hwid"`
- `resources/AndroidManifest.xml:1101`
  `android:name="com.huawei.hms.min_api_level:hwid:account"`
- `resources/AndroidManifest.xml:1104`
  `android:name="com.huawei.hms.aaid.InitProvider"`
- `resources/AndroidManifest.xml:1109`
  `android:name="com.huawei.hms.client.service.name:opendevice"`
- `resources/AndroidManifest.xml:1112`
  `android:name="com.huawei.hms.min_api_level:opendevice:push"`
- `resources/AndroidManifest.xml:1115`
  `android:name="com.huawei.hms.client.service.name:base"`
- `resources/AndroidManifest.xml:1118`
  `android:name="com.huawei.hms.min_api_level:base:hmscore"`
- `resources/AndroidManifest.xml:1125`
  `android:name="com.huawei.hms.activity.BridgeActivity"`
- `resources/AndroidManifest.xml:1136`
  `android:name="com.huawei.hms.activity.EnableServiceActivity"`
- `resources/AndroidManifest.xml:1179`
  `android:name="com.huawei.hms.client.appid"`
- `resources/assets/grs_sdk_global_route_config_opendevicesdk.json:5`
  `"name": "com.huawei.hms.opendevicesdk",`
- `resources/res/layout/hw_cloud_select_dialog_material.xml:16`
  `class="com.huawei.hms.update.ui.HwAlertController$RecycleListView"`
- `resources/res/layout/jpush_banner.xml:10`
  `<cn.jpush.android.ui.ShadowViewCard`
- `resources/res/layout/jpush_banner.xml:18`
  `<cn.jpush.android.ui.RoundedImageView`
- `resources/res/layout/jpush_banner.xml:46`
  `</cn.jpush.android.ui.ShadowViewCard>`
- `resources/res/layout/jpush_banner.xml:47`
  `<cn.jpush.android.ui.RoundedImageView`
- `resources/res/layout/jpush_interstitial.xml:20`
  `<cn.jpush.android.ui.RoundedImageView`
- `resources/res/layout/jpush_interstitial.xml:101`
  `<cn.jpush.android.ui.RoundedImageView`
- `resources/res/layout/jpush_webview_layout.xml:2`
  `<cn.jpush.android.ui.FullScreenView xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/jpush_webview_layout.xml:50`
  `</cn.jpush.android.ui.FullScreenView>`

## BR073

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/aegon/chrome/net/AndroidNetworkLibrary.java:191`
  `throw new RuntimeException("Failed to parse IP addresses", e);`
- `sources/aegon/chrome/net/NetStringUtil.java:7`
  `import java.nio.charset.CharsetDecoder;`
- `sources/aegon/chrome/net/NetStringUtil.java:18`
  `return Charset.forName(str).newDecoder().decode(byteBuffer).toString();`
- `sources/aegon/chrome/net/NetStringUtil.java:36`
  `CharsetDecoder charsetDecoderNewDecoder = Charset.forName(str).newDecoder();`
- `sources/aegon/chrome/net/NetStringUtil.java:37`
  `charsetDecoderNewDecoder.onMalformedInput(CodingErrorAction.REPLACE);`
- `sources/aegon/chrome/net/NetStringUtil.java:38`
  `charsetDecoderNewDecoder.onUnmappableCharacter(CodingErrorAction.REPLACE);`
- `sources/aegon/chrome/net/NetStringUtil.java:39`
  `charsetDecoderNewDecoder.replaceWith("�");`
- `sources/aegon/chrome/net/NetStringUtil.java:40`
  `return charsetDecoderNewDecoder.decode(byteBuffer).toString();`
- `sources/aegon/chrome/net/X509Util.java:16`
  `import com.taobao.weex.el.parse.Operators;`
- `sources/androidtranscoder/engine/TextureRender.java:6`
  `import com.taobao.weex.el.parse.Operators;`
- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:536`
  `this.e.saveHierarchyState(sparseArray);`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:317`
  `if (!"historical-record".equals(NewPullParser.getName())) {`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:318`
  `throw new XmlPullParserException("Share records file not well-formed.");`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:320`
  `list.add(new HistoricalRecord(NewPullParser.getAttributeValue(null, "activity"), Long.parseLong(NewPullParser.getAttributeValue(null, "time")), Float.parseFloat(NewPullParser.getAttributeValue(null, "weight"))));`
- `sources/androidx/camera/camera2/internal/Camera2CaptureOptionUnpacker.java:18`
  `@Override // androidx.camera.core.impl.CaptureConfig.OptionUnpacker`
- `sources/androidx/camera/camera2/internal/Camera2CaptureOptionUnpacker.java:20`
  `public void unpack(@NonNull UseCaseConfig<?> useCaseConfig, @NonNull CaptureConfig.Builder builder) {`
- `sources/androidx/camera/camera2/internal/Camera2SessionOptionUnpacker.java:20`
  `@Override // androidx.camera.core.impl.SessionConfig.OptionUnpacker`
- `sources/androidx/camera/camera2/internal/Camera2SessionOptionUnpacker.java:22`
  `public void unpack(@NonNull UseCaseConfig<?> useCaseConfig, @NonNull SessionConfig.Builder builder) {`
- `sources/androidx/camera/camera2/internal/Camera2UseCaseConfigFactory.java:68`
  `mutableOptionsBundleCreate.insertOption(UseCaseConfig.OPTION_SESSION_CONFIG_UNPACKER, Camera2SessionOptionUnpacker.a);`
- `sources/androidx/camera/camera2/internal/Camera2UseCaseConfigFactory.java:79`
  `mutableOptionsBundleCreate.insertOption(UseCaseConfig.OPTION_CAPTURE_CONFIG_UNPACKER, captureType == UseCaseConfigFactory.CaptureType.IMAGE_CAPTURE ? ImageCaptureOptionUnpacker.c : Camera2CaptureOptionUnpacker.a);`
- `sources/androidx/camera/core/ImageCapture.java:65`
  `import com.taobao.weex.el.parse.Operators;`
- `sources/androidx/camera/core/ImageCapture.java:556`
  `b(1, "Unable to parse JPEG exif", e);`
- `sources/androidx/camera/core/VideoCapture.java:1251`
  `if (CamcorderProfile.hasProfile(Integer.parseInt(str), i3)) {`
- `sources/androidx/camera/core/VideoCapture.java:1252`
  `CamcorderProfile camcorderProfile = CamcorderProfile.get(Integer.parseInt(str), i3);`
- `sources/androidx/camera/core/impl/utils/Exif.java:10`
  `import com.taobao.weex.el.parse.Operators;`
- `sources/androidx/camera/core/impl/utils/Exif.java:16`
  `import java.text.ParseException;`
- `sources/androidx/camera/core/impl/utils/ExifAttribute.java:6`
  `import com.taobao.weex.el.parse.Operators;`
- `sources/androidx/camera/core/impl/utils/ExifAttribute.java:129`
  `return Double.parseDouble((String) objA);`
- `sources/androidx/camera/core/impl/utils/ExifAttribute.java:167`
  `return Integer.parseInt((String) objA);`
- `sources/androidx/camera/core/impl/utils/ExifData.java:11`
  `import com.taobao.weex.el.parse.Operators;`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:221`
  `BitmapRegionDecoder bitmapRegionDecoderNewInstance = BitmapRegionDecoder.newInstance(bArrJpegImageToJpegByteArray, 0, bArrJpegImageToJpegByteArray.length, false);`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:222`
  `Bitmap bitmapDecodeRegion = bitmapRegionDecoderNewInstance.decodeRegion(rect, new BitmapFactory.Options());`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:223`
  `bitmapRegionDecoderNewInstance.recycle();`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:224`
  `if (bitmapDecodeRegion != null) {`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:226`
  `if (bitmapDecodeRegion.compress(Bitmap.CompressFormat.JPEG, i2, byteArrayOutputStream)) {`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:227`
  `bitmapDecodeRegion.recycle();`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:232`
  `throw new CodecFailedException("Decode byte array failed.", CodecFailedException.FailureType.DECODE_FAILED);`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:234`
  `throw new CodecFailedException("Decode byte array failed.", CodecFailedException.FailureType.DECODE_FAILED);`
- `sources/androidx/camera/core/internal/utils/ImageUtil.java:236`
  `throw new CodecFailedException("Decode byte array failed with illegal argument." + e, CodecFailedException.FailureType.DECODE_FAILED);`
- `sources/androidx/camera/video/VideoCaptureLegacy.java:1117`
  `if (CamcorderProfile.hasProfile(Integer.parseInt(str), i3)) {`
- `sources/androidx/camera/video/VideoCaptureLegacy.java:1118`
  `CamcorderProfile camcorderProfile = CamcorderProfile.get(Integer.parseInt(str), i3);`
- `sources/androidx/constraintlayout/motion/utils/ViewSpline.java:192`
  `return new CustomSet(str, sparseArray);`
- `sources/androidx/constraintlayout/motion/widget/DesignTool.java:84`
  `constraintSet.setVerticalBias(view.getId(), Float.parseFloat(str));`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:663`
  `sparseArray = sparseArray2;`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:673`
  `sparseArray = sparseArray2;`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:851`
  `sparseArray.put(0, constraintWidgetContainer);`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:852`
  `sparseArray.put(MotionLayout.this.getId(), constraintWidgetContainer);`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:864`
  `sparseArray.put(((View) constraintWidget.getCompanionWidget()).getId(), constraintWidget);`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:872`
  `constraintSet.applyToHelper((ConstraintHelper) view, constraintWidget2, layoutParams, sparseArray);`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:947`
  `sparseArray.put(childAt.getId(), motionLayout2.E.get(childAt));`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:1010`
  `if (!sparseBooleanArray.get(childAt2.getId()) && motionController6 != null) {`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:2553`
  `SparseIntArray sparseIntArray = new SparseIntArray();`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:2554`
  `SparseIntArray sparseIntArray2 = new SparseIntArray();`
- `sources/androidx/constraintlayout/motion/widget/MotionScene.java:224`
  `SparseArray<ConstraintSet> sparseArray = this.f1669h;`
- `sources/androidx/constraintlayout/motion/widget/MotionScene.java:225`
  `return sparseArray.get(sparseArray.keyAt(0));`
- `sources/androidx/constraintlayout/motion/widget/MotionScene.java:1316`
  `} catch (XmlPullParserException e2) {`
- `sources/androidx/constraintlayout/motion/widget/TouchResponse.java:11`
  `import org.xmlpull.v1.XmlPullParser;`
- `sources/androidx/constraintlayout/motion/widget/TouchResponse.java:64`
  `public TouchResponse(Context context, MotionLayout motionLayout, XmlPullParser xmlPullParser) {`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:445`
  `int i4 = Integer.parseInt(strArrSplit[0]);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:446`
  `int i5 = Integer.parseInt(strArrSplit[1]);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:447`
  `int i6 = Integer.parseInt(strArrSplit[2]);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:456`
  `float f4 = i8 + ((int) ((Integer.parseInt(strArrSplit[3]) / 1920.0f) * height));`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1174`
  `public static final SparseIntArray map;`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1177`
  `SparseIntArray sparseIntArray = new SparseIntArray();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1178`
  `map = sparseIntArray;`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1179`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintWidth, 64);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1180`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHeight, 65);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1181`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintLeft_toLeftOf, 8);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1182`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintLeft_toRightOf, 9);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1183`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintRight_toLeftOf, 10);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1184`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintRight_toRightOf, 11);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1185`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintTop_toTopOf, 12);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1186`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintTop_toBottomOf, 13);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1211`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_goneMarginEnd, 26);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1212`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_goneMarginBaseline, 55);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1213`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_marginBaseline, 54);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1214`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHorizontal_bias, 29);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1215`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintVertical_bias, 30);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1216`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintDimensionRatio, 44);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1217`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHorizontal_weight, 45);`

## BR074

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/aegon/chrome/base/AnimationFrameTimeHistogram.java:15`
  `void saveHistogram(String str, long[] jArr, int i2);`
- `sources/aegon/chrome/base/AnimationFrameTimeHistogram.java:107`
  `AnimationFrameTimeHistogramJni.get().saveHistogram(this.mHistogramName, this.mRecorder.getFrameTimesMs(), this.mRecorder.getFrameTimesCount());`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:121`
  `private static void dumpAsyncEvents(List<AsyncEvent> list) {`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:123`
  `for (AsyncEvent asyncEvent : list) {`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:124`
  `if (asyncEvent.mIsStart) {`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:125`
  `nativeRecordEarlyStartAsyncEvent(asyncEvent.mName, asyncEvent.mId, asyncEvent.mTimestampNanos + offsetNanos);`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:127`
  `nativeRecordEarlyFinishAsyncEvent(asyncEvent.mName, asyncEvent.mId, asyncEvent.mTimestampNanos + offsetNanos);`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:141`
  `synchronized (sLock) {`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:261`
  `sPendingAsyncEvents = null;`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:262`
  `sAsyncEvents = null;`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:268`
  `private static native void nativeRecordEarlyFinishAsyncEvent(String str, long j2, long j3);`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:270`
  `private static native void nativeRecordEarlyStartAsyncEvent(String str, long j2, long j3);`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:274`
  `synchronized (sLock) {`
- `sources/aegon/chrome/base/Promise$$Lambda$4.java:15`
  `public static Callback lambdaFactory$(Promise.AsyncFunction asyncFunction, Promise promise) {`
- `sources/aegon/chrome/base/Promise$$Lambda$4.java:16`
  `return new Promise$$Lambda$4(asyncFunction, promise);`
- `sources/aegon/chrome/base/metrics/RecordHistogram.java:15`
  `private static Map<String, Long> sCache = Collections.synchronizedMap(new HashMap());`
- `sources/aegon/chrome/base/task/AsyncTask.java:23`
  `public abstract class AsyncTask<Result> {`
- `sources/aegon/chrome/base/task/AsyncTask.java:24`
  `private static final String TAG = "AsyncTask";`
- `sources/aegon/chrome/base/task/AsyncTask.java:27`
  `public static final Executor THREAD_POOL_EXECUTOR = AsyncTask$$Lambda$2.instance;`
- `sources/aegon/chrome/base/task/AsyncTask.java:42`
  `AsyncTask.this.postResultIfNotInvoked(get());`
- `sources/aegon/chrome/base/task/AsyncTask.java:44`
  `Log.w(AsyncTask.TAG, e.toString(), new Object[0]);`
- `sources/aegon/chrome/base/task/AsyncTask.java:46`
  `AsyncTask.this.postResultIfNotInvoked(null);`
- `sources/aegon/chrome/base/task/AsyncTask.java:70`
  `AsyncTask.THREAD_POOL_EXECUTOR.execute(runnable);`
- `sources/aegon/chrome/base/task/AsyncTask.java:74`
  `public AsyncTask() {`
- `sources/aegon/chrome/base/task/AsyncTask.java:75`
  `Callable<Result> callable = new Callable<Result>() { // from class: aegon.chrome.base.task.AsyncTask.1`
- `sources/aegon/chrome/base/task/AsyncTask.java:78`
  `AsyncTask.this.mTaskInvoked.set(true);`
- `sources/aegon/chrome/base/task/AsyncTask.java:81`
  `result = (Result) AsyncTask.this.doInBackground();`
- `sources/aegon/chrome/base/task/AsyncTask.java:118`
  `if (this instanceof BackgroundOnlyAsyncTask) {`
- `sources/aegon/chrome/base/task/AsyncTask.java:121`
  `ThreadUtils.postOnUiThread(AsyncTask$$Lambda$1.lambdaFactory$(this, result));`
- `sources/aegon/chrome/base/task/AsyncTask.java:134`
  `ThreadPoolExecutor threadPoolExecutor = (ThreadPoolExecutor) android.os.AsyncTask.THREAD_POOL_EXECUTOR;`
- `sources/aegon/chrome/base/task/AsyncTask.java:148`
  `public final AsyncTask<Result> executeOnExecutor(Executor executor) {`
- `sources/aegon/chrome/base/task/AsyncTask.java:155`
  `public final AsyncTask<Result> executeOnTaskRunner(TaskRunner taskRunner) {`
- `sources/aegon/chrome/base/task/AsyncTask.java:162`
  `public final AsyncTask<Result> executeWithTaskTraits(TaskTraits taskTraits) {`
- `sources/aegon/chrome/base/task/AsyncTask.java:180`
  `TraceEvent traceEventScoped = TraceEvent.scoped(str + "AsyncTask.get");`
- `sources/aegon/chrome/base/task/BackgroundOnlyAsyncTask.java:4`
  `public abstract class BackgroundOnlyAsyncTask<Result> extends AsyncTask<Result> {`
- `sources/aegon/chrome/base/task/BackgroundOnlyAsyncTask.java:7`
  `@Override // aegon.chrome.base.task.AsyncTask`
- `sources/aegon/chrome/net/UrlRequest.java:28`
  `public abstract Builder setUploadDataProvider(UploadDataProvider uploadDataProvider, Executor executor);`
- `sources/aegon/chrome/net/X509Util.java:326`
  `synchronized (sLock) {`
- `sources/aegon/chrome/net/impl/CronetBidirectionalStream.java:348`
  `this.mRequestContext.reportRequestFinished(new RequestFinishedInfoImpl(this.mInitialUrl, this.mRequestAnnotations, cronetMetrics, i2 == 7 ? 0 : i2 == 5 ? 2 : 1, this.mResponseInfo, this.mException));`
- `sources/aegon/chrome/net/impl/CronetBidirectionalStream.java:378`
  `synchronized (CronetBidirectionalStream.this.mNativeStreamLock) {`
- `sources/aegon/chrome/net/impl/CronetBidirectionalStream.java:404`
  `synchronized (CronetBidirectionalStream.this.mNativeStreamLock) {`
- `sources/aegon/chrome/net/impl/CronetBidirectionalStream.java:596`
  `synchronized (this.mNativeStreamLock) {`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:211`
  `public void maybeReportMetrics() {`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:215`
  `this.mRequestContext.reportRequestFinished(requestFinishedInfoImpl);`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:271`
  `CronetUrlRequest.this.maybeReportMetrics();`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:320`
  `CronetUrlRequest.this.maybeReportMetrics();`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:356`
  `synchronized (CronetUrlRequest.this.mUrlRequestAdapterLock) {`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:378`
  `synchronized (CronetUrlRequest.this.mUrlRequestAdapterLock) {`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:411`
  `synchronized (CronetUrlRequest.this.mUrlRequestAdapterLock) {`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:420`
  `CronetUrlRequest.this.maybeReportMetrics();`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:535`
  `synchronized (this.mUrlRequestAdapterLock) {`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:581`
  `synchronized (this.mUrlRequestAdapterLock) {`
- `sources/aegon/chrome/net/impl/CronetUrlRequestContext.java:135`
  `synchronized (obj) {`
- `sources/aegon/chrome/net/impl/CronetUrlRequestContext.java:258`
  `synchronized (this.mNetworkQualityLock) {`
- `sources/aegon/chrome/net/impl/CronetUrlRequestContext.java:446`
  `synchronized (this.mNetworkQualityLock) {`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:6`
  `import aegon.chrome.net.UploadDataProvider;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:7`
  `import aegon.chrome.net.UploadDataSink;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:51`
  `private static final int DEFAULT_UPLOAD_BUFFER_SIZE = 8192;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:57`
  `private final AsyncUrlRequestCallback mCallbackAsync;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:67`
  `private VersionSafeCallbacks.UploadDataProviderWrapper mUploadDataProvider;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:68`
  `private Executor mUploadExecutor;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:74`
  `private final AtomicBoolean mUploadProviderClosed = new AtomicBoolean(false);`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:103`
  `this.mUserExecutor.execute(new Runnable() { // from class: aegon.chrome.net.impl.JavaUrlRequest.AsyncUrlRequestCallback.5`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:107`
  `AsyncUrlRequestCallback asyncUrlRequestCallback = AsyncUrlRequestCallback.this;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:108`
  `asyncUrlRequestCallback.mCallback.onCanceled(JavaUrlRequest.this, urlResponseInfo);`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:118`
  `Runnable runnable = new Runnable() { // from class: aegon.chrome.net.impl.JavaUrlRequest.AsyncUrlRequestCallback.7`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:122`
  `AsyncUrlRequestCallback asyncUrlRequestCallback = AsyncUrlRequestCallback.this;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:123`
  `asyncUrlRequestCallback.mCallback.onFailed(JavaUrlRequest.this, urlResponseInfo, cronetException);`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:140`
  `execute(new CheckedRunnable() { // from class: aegon.chrome.net.impl.JavaUrlRequest.AsyncUrlRequestCallback.4`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:144`
  `AsyncUrlRequestCallback asyncUrlRequestCallback = AsyncUrlRequestCallback.this;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:145`
  `asyncUrlRequestCallback.mCallback.onReadCompleted(JavaUrlRequest.this, urlResponseInfo, byteBuffer);`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:152`
  `execute(new CheckedRunnable() { // from class: aegon.chrome.net.impl.JavaUrlRequest.AsyncUrlRequestCallback.2`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:155`
  `AsyncUrlRequestCallback asyncUrlRequestCallback = AsyncUrlRequestCallback.this;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:156`
  `asyncUrlRequestCallback.mCallback.onRedirectReceived(JavaUrlRequest.this, urlResponseInfo, str);`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:162`
  `execute(new CheckedRunnable() { // from class: aegon.chrome.net.impl.JavaUrlRequest.AsyncUrlRequestCallback.3`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:166`
  `AsyncUrlRequestCallback asyncUrlRequestCallback = AsyncUrlRequestCallback.this;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:167`
  `VersionSafeCallbacks.UrlRequestCallback urlRequestCallback = asyncUrlRequestCallback.mCallback;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:176`
  `this.mUserExecutor.execute(new Runnable() { // from class: aegon.chrome.net.impl.JavaUrlRequest.AsyncUrlRequestCallback.6`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:180`
  `AsyncUrlRequestCallback asyncUrlRequestCallback = AsyncUrlRequestCallback.this;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:181`
  `asyncUrlRequestCallback.mCallback.onSucceeded(JavaUrlRequest.this, urlResponseInfo);`

## BR075

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/aegon/chrome/base/CommandLine.java:223`
  `public static void reset() {`
- `sources/aegon/chrome/base/DiscardableReferencePool.java:18`
  `private T mPayload;`
- `sources/aegon/chrome/base/DiscardableReferencePool.java:22`
  `this.mPayload = null;`
- `sources/aegon/chrome/base/DiscardableReferencePool.java:27`
  `return this.mPayload;`
- `sources/aegon/chrome/base/DiscardableReferencePool.java:31`
  `this.mPayload = t;`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:273`
  `public static void resetForTesting() {`
- `sources/aegon/chrome/base/task/PostTask.java:117`
  `public static void resetPrenativeThreadPoolExecutorForTesting() {`
- `sources/aegon/chrome/net/NetError.java:60`
  `public static final int ERR_CONNECTION_RESET = -101;`
- `sources/aegon/chrome/net/NetError.java:97`
  `public static final int ERR_HTTP2_CLAIMED_PUSHED_STREAM_RESET_BY_SERVER = -374;`
- `sources/aegon/chrome/net/NetworkException.java:8`
  `public static final int ERROR_CONNECTION_RESET = 8;`
- `sources/aegon/chrome/net/impl/UrlRequestError.java:12`
  `public static final int CONNECTION_RESET = 8;`
- `sources/androidx/appcompat/R.java:1328`
  `public static final int AppCompatTextView_autoSizePresetSizes = 0x00000003;`
- `sources/androidx/appcompat/R.java:1699`
  `public static final int[] AppCompatTextView = {android.R.attr.textAppearance, com.xs.smartlink.R.attr.autoSizeMaxTextSize, com.xs.smartlink.R.attr.autoSizeMinTextSize, com.xs.smartlink.R.attr.autoSizePresetSizes, com.xs.smartlink.R.attr.autoSizeStepGranularity, com.xs.smartlink.R.attr.autoSizeTextTy...`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:125`
  `resetGroup();`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:276`
  `public void resetGroup() {`
- `sources/androidx/appcompat/widget/AppCompatButton.java:198`
  `public void setAutoSizeTextTypeUniformWithPresetSizes(@NonNull int[] iArr, int i2) throws IllegalArgumentException {`
- `sources/androidx/appcompat/widget/AppCompatButton.java:200`
  `super.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i2);`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:265`
  `public void setAutoSizeTextTypeUniformWithPresetSizes(@NonNull int[] iArr, int i2) throws IllegalArgumentException {`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:267`
  `super.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i2);`
- `sources/androidx/camera/camera2/impl/CameraEventCallback.java:21`
  `public CaptureConfig onPresetSession() {`
- `sources/androidx/camera/camera2/impl/CameraEventCallbacks.java:58`
  `public List<CaptureConfig> onPresetSession() {`
- `sources/androidx/camera/camera2/internal/Camera2CameraControlImpl.java:501`
  `zoomControl.e.resetZoom();`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1039`
  `errorListener.onError(sessionConfig, SessionConfig.SessionError.SESSION_ERROR_SURFACE_NEEDS_RESET);`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1092`
  `public void onUseCaseReset(@NonNull UseCase useCase) {`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1103`
  `camera2CameraImpl.e("Use case " + str + " RESET", null);`
- `sources/androidx/camera/extensions/internal/BasicVendorExtender.java:113`
  `public CaptureStageImpl onPresetSession() {`
- `sources/androidx/camera/extensions/internal/BasicVendorExtender.java:161`
  `public CaptureStageImpl onPresetSession() {`
- `sources/androidx/camera/extensions/internal/ImageCaptureConfigProvider.java:161`
  `public CaptureConfig onPresetSession() {`
- `sources/androidx/camera/extensions/internal/ImageCaptureConfigProvider.java:162`
  `CaptureStageImpl captureStageImplOnPresetSession;`
- `sources/androidx/camera/extensions/internal/ImageCaptureConfigProvider.java:163`
  `if (!this.c.get() || (captureStageImplOnPresetSession = this.a.onPresetSession()) == null) {`
- `sources/androidx/camera/extensions/internal/ImageCaptureConfigProvider.java:167`
  `return new AdaptingCaptureStage(captureStageImplOnPresetSession).getCaptureConfig();`
- `sources/androidx/camera/extensions/internal/ImageCaptureConfigProvider.java:169`
  `Logger.w("ImageCaptureConfigProvider", "The CaptureRequest parameters returned from onPresetSession() will be passed to the camera device as part of the capture session via SessionConfiguration#setSessionParameters(CaptureRequest) which only supported from API level 28!");`
- `sources/androidx/camera/extensions/internal/PreviewConfigProvider.java:173`
  `public CaptureConfig onPresetSession() {`
- `sources/androidx/camera/extensions/internal/PreviewConfigProvider.java:175`
  `CaptureStageImpl captureStageImplOnPresetSession = this.a.onPresetSession();`
- `sources/androidx/camera/extensions/internal/PreviewConfigProvider.java:176`
  `if (captureStageImplOnPresetSession != null) {`
- `sources/androidx/camera/extensions/internal/PreviewConfigProvider.java:178`
  `return new AdaptingCaptureStage(captureStageImplOnPresetSession).getCaptureConfig();`
- `sources/androidx/camera/extensions/internal/PreviewConfigProvider.java:180`
  `Logger.w("PreviewConfigProvider", "The CaptureRequest parameters returned from onPresetSession() will be passed to the camera device as part of the capture session via SessionConfiguration#setSessionParameters(CaptureRequest) which only supported from API level 28!");`
- `sources/androidx/camera/video/Recorder.java:93`
  `public static final Set<State> Q = Collections.unmodifiableSet(EnumSet.of(State.INITIALIZING, State.IDLING, State.RESETTING, State.STOPPING));`
- `sources/androidx/camera/video/Recorder.java:1203`
  `case RESETTING:`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:144`
  `path.reset();`
- `sources/androidx/constraintlayout/core/ArrayRow.java:344`
  `public void reset() {`
- `sources/androidx/constraintlayout/core/LinearSystem.java:113`
  `solverVariableAcquire.reset();`
- `sources/androidx/constraintlayout/core/LinearSystem.java:392`
  `constraintAnchor.resetSolverVariable(this.f1474j);`
- `sources/androidx/constraintlayout/core/LinearSystem.java:398`
  `solverVariable.reset();`
- `sources/androidx/constraintlayout/core/LinearSystem.java:427`
  `arrayRowAcquire.reset();`
- `sources/androidx/constraintlayout/core/LinearSystem.java:837`
  `public void reset() {`
- `sources/androidx/constraintlayout/core/LinearSystem.java:848`
  `solverVariable.reset();`
- `sources/androidx/constraintlayout/core/Metrics.java:52`
  `public void reset() {`
- `sources/androidx/constraintlayout/core/PriorityGoalRow.java:113`
  `public void reset() {`
- `sources/androidx/constraintlayout/core/PriorityGoalRow.java:145`
  `this.f1479i.reset();`
- `sources/androidx/constraintlayout/core/SolverVariable.java:145`
  `public void reset() {`
- `sources/androidx/constraintlayout/core/widgets/ConstraintAnchor.java:364`
  `public void resetFinalResolution() {`
- `sources/androidx/constraintlayout/core/widgets/ConstraintAnchor.java:369`
  `public void resetSolverVariable(Cache cache) {`
- `sources/androidx/constraintlayout/core/widgets/ConstraintAnchor.java:374`
  `solverVariable.reset();`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:2039`
  `public void reset() {`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:2040`
  `this.mLeft.reset();`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:2041`
  `this.mTop.reset();`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:2042`
  `this.mRight.reset();`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:2043`
  `this.mBottom.reset();`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:2044`
  `this.mBaseline.reset();`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:2045`
  `this.s.reset();`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:2046`
  `this.t.reset();`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:2047`
  `this.mCenter.reset();`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:2179`
  `this.u.get(i2).resetFinalResolution();`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:2183`
  `public void resetSolverVariables(Cache cache) {`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:2184`
  `this.mLeft.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:2185`
  `this.mTop.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:2186`
  `this.mRight.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:2187`
  `this.mBottom.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:2188`
  `this.mBaseline.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:2189`
  `this.mCenter.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:2190`
  `this.s.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:2191`
  `this.t.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/core/widgets/ConstraintWidget.java:2194`
  `public void resetSolvingPassFlag() {`
- `sources/androidx/constraintlayout/core/widgets/WidgetContainer.java:63`
  `public void reset() {`
- `sources/androidx/constraintlayout/core/widgets/WidgetContainer.java:65`
  `super.reset();`
- `sources/androidx/constraintlayout/core/widgets/WidgetContainer.java:69`
  `public void resetSolverVariables(Cache cache) {`
- `sources/androidx/constraintlayout/core/widgets/WidgetContainer.java:70`
  `super.resetSolverVariables(cache);`
- `sources/androidx/constraintlayout/core/widgets/WidgetContainer.java:73`
  `this.mChildren.get(i2).resetSolverVariables(cache);`
- `sources/androidx/constraintlayout/core/widgets/analyzer/WidgetGroup.java:123`
  `linearSystem.reset();`

## BR076

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `resources/org/apache/commons/codec/language/bm/lang.txt:66`
  `field$ english true`
- `resources/org/apache/commons/codec/language/bm/lang.txt:267`
  `v[^aoeiu] german false // in german, "v" can be found before a vowel only`
- `resources/org/apache/commons/codec/language/bm/lang.txt:268`
  `y[^aoeiu] german false  // in german, "y" usually appears only in the last position; sometimes before a vowel`
- `resources/res/values/strings.xml:148`
  `<string name="dcloud_ad_error_code_5008">The ad is unavailable or has expired, please request again</string>`
- `resources/res/values/strings.xml:154`
  `<string name="dcloud_ad_error_code_5016">Please init first</string>`
- `resources/res/values/strings.xml:163`
  `<string name="dcloud_ad_error_load_first">Please load the ad first</string>`
- `resources/res/values/strings.xml:169`
  `<string name="dcloud_ad_error_message_5006">Call load before calling show</string>`
- `resources/res/values/strings.xml:184`
  `<string name="dcloud_audio_timeout">file request timed out</string>`
- `resources/res/values/strings.xml:222`
  `<string name="dcloud_common_not_supported">this feature is not supported</string>`
- `resources/res/values/strings.xml:318`
  `<string name="dcloud_gallery_select_null">You must select at least one file before previewing</string>`
- `resources/res/values/strings.xml:368`
  `<string name="dcloud_permissions_checkbox_close_tips">dont prompt before exit</string>`
- `resources/res/values/strings.xml:424`
  `<string name="dcloud_short_cut_vivo1">to use streaming applications on VIVO mobile phones, you must first make sure to open the desktop shortcut. Please click Go to set permissions-Software Management-Desktop Shortcut Management-</string>`
- `resources/res/values/strings.xml:492`
  `<string name="first_frame_render">first-frame-render</string>`
- `resources/res/values/strings.xml:493`
  `<string name="first_screen_time">first-screen</string>`
- `resources/res/values/strings.xml:499`
  `<string name="hms_bindfaildlg_message">%1$s is unable to use HMS Core. Launch Optimizer (Phone Manager) or go to Settings, enable all permissions for %2$s (including auto-launch and secondary launch), and try again.</string>`
- `resources/res/values/strings.xml:514`
  `<string name="hms_install_message">HMS Core must be installed to use this feature. Install?</string>`
- `resources/res/values/strings.xml:523`
  `<string name="hms_update_message">Update to the latest version of HMS Core to use this feature. Update now?</string>`
- `resources/res/values-en-rGB/strings.xml:57`
  `<string name="hms_bindfaildlg_message">%1$s is unable to use HMS Core. Launch Optimiser (Phone Manager) or go to Settings, enable all permissions for %2$s (including auto-launch and secondary launch), and try again.</string>`
- `resources/res/values-en-rGB/strings.xml:71`
  `<string name="hms_install_message">HMS Core must be installed to use this feature. Install?</string>`
- `resources/res/values-en-rGB/strings.xml:78`
  `<string name="hms_update_message">Update to the latest version of HMS Core to use this feature. Update now?</string>`
- `sources/aegon/chrome/net/impl/CronetBidirectionalStream.java:248`
  `Log.e(CronetUrlRequestContext.LOG_TAG, "Exception notifying of failed request", e);`
- `sources/aegon/chrome/net/impl/CronetBidirectionalStream.java:657`
  `throw new IllegalArgumentException("Empty buffer before end of stream.");`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:538`
  `throw new IllegalStateException(a.x("Request is already started. State is: ", iIntValue));`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:796`
  `throw new IllegalStateException("Can't enter error state before start");`
- `sources/aegon/chrome/net/urlconnection/CronetHttpURLConnection.java:144`
  `if (((String) this.mRequestHeaders.get(i2).first).equalsIgnoreCase(str)) {`
- `sources/aegon/chrome/net/urlconnection/CronetHttpURLConnection.java:231`
  `throw new IllegalStateException("Cannot modify request property after connection is made.");`
- `sources/aegon/chrome/net/urlconnection/CronetHttpURLConnection.java:267`
  `builder.addHeader((String) pair.first, (String) pair.second);`
- `sources/aegon/chrome/net/urlconnection/CronetHttpURLConnection.java:397`
  `throw new IllegalStateException("Cannot access request headers after connection is set.");`
- `sources/aegon/chrome/net/urlconnection/CronetHttpURLConnection.java:401`
  `if (treeMap.containsKey(pair.first)) {`
- `sources/aegon/chrome/net/urlconnection/CronetHttpURLConnection.java:406`
  `treeMap.put((String) pair.first, Collections.unmodifiableList(arrayList));`
- `sources/aegon/chrome/net/urlconnection/CronetHttpURLConnection.java:444`
  `throw new IllegalStateException("Cannot modify traffic stats tag after connection is made.");`
- `sources/aegon/chrome/net/urlconnection/CronetHttpURLConnection.java:452`
  `throw new IllegalStateException("Cannot modify traffic stats UID after connection is made.");`
- `sources/androidx/activity/ComponentActivity.java:143`
  `throw new IllegalStateException("getLifecycle() returned null in ComponentActivity's constructor. Please make sure you are lazily constructing your Lifecycle in the first call to getLifecycle() rather than relying on field initialization.");`
- `sources/androidx/activity/ComponentActivity.java:241`
  `throw new IllegalStateException("Your activity is not yet attached to the Application instance. You can't request ViewModel before onCreate call.");`
- `sources/androidx/activity/ComponentActivity.java:281`
  `throw new IllegalStateException("Your activity is not yet attached to the Application instance. You can't request ViewModel before onCreate call.");`
- `sources/androidx/activity/result/ActivityResultRegistry.java:79`
  `StringBuilder sbK0 = a.k0("Dropping pending result for request ", str, ": ");`
- `sources/androidx/activity/result/ActivityResultRegistry.java:85`
  `StringBuilder sbK02 = a.k0("Dropping pending result for request ", str, ": ");`
- `sources/androidx/activity/result/ActivityResultRegistry.java:161`
  `throw new IllegalStateException("LifecycleOwner " + lifecycleOwner + " is attempting to register while current state is " + lifecycle.getCurrentState() + ". LifecycleOwners must call register before they are STARTED.");`
- `sources/androidx/activity/result/ActivityResultRegistry.java:207`
  `public void launch(I i2, @Nullable ActivityOptionsCompat activityOptionsCompat) {`
- `sources/androidx/activity/result/ActivityResultRegistry.java:261`
  `public void launch(I i2, @Nullable ActivityOptionsCompat activityOptionsCompat) {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:99`
  `import java.lang.reflect.Field;`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:893`
  `throw new AndroidRuntimeException("Window feature must be requested before adding content");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1223`
  `Field declaredField = Resources.class.getDeclaredField("mResourcesImpl");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1227`
  `Log.e("ResourcesFlusher", "Could not retrieve Resources#mResourcesImpl field", e2);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1231`
  `Field field = ResourcesFlusher.g;`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1232`
  `if (field != null) {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1234`
  `obj = field.get(resources);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1242`
  `Field declaredField2 = obj.getClass().getDeclaredField("mDrawableCache");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1246`
  `Log.e("ResourcesFlusher", "Could not retrieve ResourcesImpl#mDrawableCache field", e4);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1250`
  `Field field2 = ResourcesFlusher.a;`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1266`
  `Field declaredField3 = Resources.class.getDeclaredField("mDrawableCache");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1270`
  `Log.e("ResourcesFlusher", "Could not retrieve Resources#mDrawableCache field", e6);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1274`
  `Field field3 = ResourcesFlusher.a;`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2078`
  `throw new IllegalStateException("This Activity already has an action bar supplied by the window decor. Do not request Window.FEATURE_SUPPORT_ACTION_BAR and set windowActionBar to false in your theme to use a Toolbar instead.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2297`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2303`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR_OVERLAY id when requesting this feature.");`
- `sources/androidx/appcompat/widget/SearchView.java:811`
  `Log.e("SearchView", "Failed launch activity: " + intentK, e2);`
- `sources/androidx/appcompat/widget/SearchView.java:1124`
  `/* JADX WARN: Type inference fix 'apply assigned field type' failed`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:243`
  `camera2CameraImpl.e("Issue capture request", null);`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:582`
  `return "Release[request=" + this.n.getAndIncrement() + Operators.ARRAY_END_STR;`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1234`
  `return "Release[request=" + camera2CameraImpl.n.getAndIncrement() + Operators.ARRAY_END_STR;`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1384`
  `e("No cameras available. Waiting for available camera before opening camera.", null);`
- `sources/androidx/camera/camera2/internal/Camera2CameraImpl.java:1394`
  `e("No cameras available. Waiting for available camera before opening camera.", null);`
- `sources/androidx/camera/camera2/internal/Camera2CapturePipeline.java:254`
  `this.a.setException(new ImageCaptureException(3, "Capture request is cancelled because camera is closed", null));`
- `sources/androidx/camera/camera2/internal/Camera2CapturePipeline.java:264`
  `StringBuilder sbD0 = a.d0("Capture request failed with reason ");`
- `sources/androidx/camera/camera2/internal/Camera2CapturePipeline.java:386`
  `Logger.d("Camera2CapturePipeline", "Wait for capture result timeout, current:" + l2 + " first: " + l3);`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:204`
  `Logger.d("CaptureSession", "Attempting to send capture request onConfigured");`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:344`
  `Logger.d("CaptureSession", "Issuing capture request.");`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:348`
  `Logger.d("CaptureSession", "Skipping issuing empty capture request.");`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:358`
  `Logger.d("CaptureSession", "Skipping capture request with invalid surface: " + next);`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:376`
  `Logger.d("CaptureSession", "Skipping issuing request without surface.");`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:394`
  `Logger.d("CaptureSession", "Skipping issuing burst request due to no valid request elements");`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:462`
  `Logger.e("CaptureSession", "Unable to issue the request before close the capture session", e);`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:504`
  `Logger.d("CaptureSession", "Issuing request for session.");`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:511`
  `Logger.d("CaptureSession", "Skipping issuing empty request for session.");`
- `sources/androidx/camera/camera2/internal/CaptureSession.java:577`
  `throw new IllegalStateException("Cannot issue capture request on a closed/released session.");`
- `sources/androidx/camera/camera2/internal/SynchronizedCaptureSessionBaseImpl.java:132`
  `Preconditions.checkNotNull(this.g, "Need to call openCaptureSession before using this API.");`
- `sources/androidx/camera/camera2/internal/SynchronizedCaptureSessionBaseImpl.java:138`
  `Preconditions.checkNotNull(this.g, "Need to call openCaptureSession before using this API.");`
- `sources/androidx/camera/camera2/internal/SynchronizedCaptureSessionBaseImpl.java:144`
  `Preconditions.checkNotNull(this.g, "Need to call openCaptureSession before using this API.");`
- `sources/androidx/camera/camera2/internal/SynchronizedCaptureSessionBaseImpl.java:150`
  `Preconditions.checkNotNull(this.g, "Need to call openCaptureSession before using this API.");`

## BR077

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `sources/cn/jiguang/bi/b.java:499`
  `SSLContext sSLContext = SSLContext.getInstance("SSL");`
- `sources/cn/jiguang/bi/b.java:500`
  `this.f2336j = sSLContext;`
- `sources/cn/jiguang/bi/b.java:501`
  `sSLContext.init(null, new TrustManager[]{new SSLTrustManager(j.a())}, new SecureRandom());`
- `sources/com/cmic/sso/sdk/c.java:26`
  `SSLContext sSLContext = SSLContext.getInstance("SSL");`
- `sources/com/cmic/sso/sdk/c.java:27`
  `this.b = sSLContext;`
- `sources/com/cmic/sso/sdk/c.java:28`
  `sSLContext.init(null, trustManagerFactory.getTrustManagers(), null);`
- `sources/com/cmic/sso/sdk/h/d.java:225`
  `((HttpsURLConnection) httpURLConnection).setSSLSocketFactory(new com.cmic.sso.sdk.c(strA).a().getSocketFactory());`
- `sources/com/dcloud/android/downloader/core/task/GetFileInfoTask.java:37`
  `if (httpURLConnection instanceof HttpsURLConnection) {`
- `sources/com/dcloud/android/downloader/core/task/GetFileInfoTask.java:38`
  `SSLSocketFactory sSLSocketFactory = DCloudTrustManager.getSSLSocketFactory();`
- `sources/com/dcloud/android/downloader/core/task/GetFileInfoTask.java:39`
  `if (sSLSocketFactory != null) {`
- `sources/com/dcloud/android/downloader/core/task/GetFileInfoTask.java:40`
  `((HttpsURLConnection) httpURLConnection).setSSLSocketFactory(sSLSocketFactory);`
- `sources/com/dcloud/android/downloader/core/task/GetFileInfoTask.java:42`
  `((HttpsURLConnection) httpURLConnection).setHostnameVerifier(DCloudTrustManager.getHostnameVerifier(false));`
- `sources/com/dcloud/android/downloader/core/thread/DownloadThread.java:70`
  `if (httpURLConnection3 instanceof HttpsURLConnection) {`
- `sources/com/dcloud/android/downloader/core/thread/DownloadThread.java:71`
  `SSLSocketFactory sSLSocketFactory = DCloudTrustManager.getSSLSocketFactory();`
- `sources/com/dcloud/android/downloader/core/thread/DownloadThread.java:72`
  `if (sSLSocketFactory != null) {`
- `sources/com/dcloud/android/downloader/core/thread/DownloadThread.java:73`
  `((HttpsURLConnection) httpURLConnection3).setSSLSocketFactory(sSLSocketFactory);`
- `sources/com/dcloud/android/downloader/core/thread/DownloadThread.java:75`
  `((HttpsURLConnection) httpURLConnection3).setHostnameVerifier(DCloudTrustManager.getHostnameVerifier(false));`
- `sources/com/huawei/hms/framework/network/grs/h/f/a.java:20`
  `if (!(uRLConnectionOpenConnection instanceof HttpsURLConnection)) {`
- `sources/com/huawei/hms/framework/network/grs/h/f/a.java:21`
  `Logger.w("URLConnectionHelper", "urlConnection is not an instance of HttpsURLConnection");`
- `sources/com/huawei/hms/framework/network/grs/h/f/a.java:24`
  `HttpsURLConnection httpsURLConnection = (HttpsURLConnection) uRLConnectionOpenConnection;`
- `sources/com/huawei/hms/framework/network/grs/h/f/a.java:26`
  `httpsURLConnection.setSSLSocketFactory(com.huawei.hms.framework.network.grs.h.g.a.a(context));`
- `sources/com/huawei/hms/framework/network/grs/h/f/a.java:27`
  `httpsURLConnection.setHostnameVerifier(com.huawei.hms.framework.network.grs.h.g.a.a());`
- `sources/com/huawei/hms/framework/network/grs/h/f/a.java:31`
  `httpsURLConnection.setConnectTimeout(10000);`
- `sources/com/huawei/hms/framework/network/grs/h/f/a.java:32`
  `httpsURLConnection.setReadTimeout(10000);`
- `sources/com/huawei/hms/framework/network/grs/h/f/a.java:33`
  `httpsURLConnection.setDoOutput(true);`
- `sources/com/huawei/hms/hatool/w.java:153`
  `if (secureSSLSocketFactory == null) {`
- `sources/com/huawei/hms/hatool/w.java:156`
  `httpsURLConnection.setSSLSocketFactory(secureSSLSocketFactory);`
- `sources/com/huawei/hms/hatool/w.java:157`
  `httpsURLConnection.setHostnameVerifier(new StrictHostnameVerifier());`
- `sources/com/huawei/hms/opendevice/d.java:381`
  `if (secureSSLSocketFactory != null) {`
- `sources/com/huawei/hms/opendevice/d.java:382`
  `httpsURLConnection.setSSLSocketFactory(secureSSLSocketFactory);`
- `sources/com/huawei/hms/opendevice/d.java:383`
  `httpsURLConnection.setHostnameVerifier(SecureSSLSocketFactory.STRICT_HOSTNAME_VERIFIER);`
- `sources/com/huawei/hms/update/http/HttpRequestHelper.java:40`
  `this.a = (HttpsURLConnection) uRLConnectionOpenConnection;`
- `sources/com/huawei/hms/update/http/HttpRequestHelper.java:42`
  `SecureSSLSocketFactory secureSSLSocketFactory = SecureSSLSocketFactory.getInstance(context);`
- `sources/com/huawei/hms/update/http/HttpRequestHelper.java:43`
  `if (secureSSLSocketFactory != null) {`
- `sources/com/huawei/hms/update/http/HttpRequestHelper.java:44`
  `this.a.setSSLSocketFactory(secureSSLSocketFactory);`
- `sources/com/huawei/hms/update/http/HttpRequestHelper.java:46`
  `this.a.setSSLSocketFactory(secureSSLSocketFactory);`
- `sources/com/huawei/hms/update/http/HttpWiseContentHelper.java:50`
  `HttpsURLConnection httpsURLConnection = (HttpsURLConnection) uRLConnectionOpenConnection;`
- `sources/com/huawei/hms/update/http/HttpWiseContentHelper.java:52`
  `SecureSSLSocketFactory secureSSLSocketFactory = SecureSSLSocketFactory.getInstance(context);`
- `sources/com/huawei/hms/update/http/HttpWiseContentHelper.java:53`
  `if (secureSSLSocketFactory != null) {`
- `sources/com/huawei/hms/update/http/HttpWiseContentHelper.java:54`
  `httpsURLConnection.setSSLSocketFactory(secureSSLSocketFactory);`
- `sources/com/huawei/hms/update/http/HttpWiseContentHelper.java:56`
  `httpsURLConnection.setSSLSocketFactory(secureSSLSocketFactory);`
- `sources/com/huawei/hms/update/http/HttpWiseContentHelper.java:57`
  `httpsURLConnection.setHostnameVerifier(new StrictHostnameVerifier());`
- `sources/com/huawei/hms/update/http/HttpWiseContentHelper.java:58`
  `httpsURLConnection.setConnectTimeout(30000);`
- `sources/com/huawei/hms/update/http/HttpWiseContentHelper.java:59`
  `httpsURLConnection.setReadTimeout(30000);`
- `sources/com/huawei/hms/update/http/HttpWiseContentHelper.java:60`
  `return httpsURLConnection;`
- `sources/com/huawei/secure/android/common/SecureApacheSSLSocketFactory.java:60`
  `private SecureApacheSSLSocketFactory(KeyStore keyStore, Context context) throws IllegalAccessException, NoSuchAlgorithmException, UnrecoverableKeyException, IOException, KeyManagementException, KeyStoreException, CertificateException {`
- `sources/com/huawei/secure/android/common/SecureApacheSSLSocketFactory.java:67`
  `@Override // org.apache.http.conn.ssl.SSLSocketFactory, org.apache.http.conn.scheme.SocketFactory`
- `sources/com/huawei/secure/android/common/SecureApacheSSLSocketFactory.java:75`
  `public SecureApacheSSLSocketFactory(KeyStore keyStore, InputStream inputStream, String str) throws NoSuchAlgorithmException, UnrecoverableKeyException, IOException, KeyManagementException, KeyStoreException, CertificateException {`
- `sources/com/huawei/secure/android/common/SecureSSLSocketFactory.java:30`
  `private SecureSSLSocketFactory(Context context) throws IllegalAccessException, NoSuchAlgorithmException, IOException, KeyManagementException, CertificateException, KeyStoreException {`
- `sources/com/huawei/secure/android/common/SecureSSLSocketFactory.java:90`
  `public SecureSSLSocketFactory(InputStream inputStream, String str) throws NoSuchAlgorithmException, IOException, KeyManagementException, CertificateException, KeyStoreException {`
- `sources/com/huawei/secure/android/common/SecureSSLSocketFactory.java:96`
  `@Override // javax.net.ssl.SSLSocketFactory`
- `sources/com/huawei/secure/android/common/ssl/SASFCompatiableSystemCA.java:169`
  `@Override // org.apache.http.conn.ssl.SSLSocketFactory, org.apache.http.conn.scheme.SocketFactory`
- `sources/com/huawei/secure/android/common/ssl/SecureApacheSSLSocketFactory.java:173`
  `@Override // org.apache.http.conn.ssl.SSLSocketFactory, org.apache.http.conn.scheme.SocketFactory`
- `sources/com/huawei/secure/android/common/ssl/SecureApacheSSLSocketFactory.java:219`
  `public SecureApacheSSLSocketFactory(KeyStore keyStore, InputStream inputStream, String str) throws NoSuchAlgorithmException, UnrecoverableKeyException, IOException, KeyManagementException, KeyStoreException, CertificateException, IllegalArgumentException {`
- `sources/com/huawei/secure/android/common/ssl/SecureApacheSSLSocketFactory.java:228`
  `public SecureApacheSSLSocketFactory(KeyStore keyStore, X509TrustManager x509TrustManager) throws NoSuchAlgorithmException, UnrecoverableKeyException, IOException, KeyManagementException, KeyStoreException, CertificateException, IllegalArgumentException {`
- `sources/com/huawei/secure/android/common/ssl/SecureSSLSocketFactory.java:48`
  `public SecureSSLSocketFactory(InputStream inputStream, String str) throws NoSuchAlgorithmException, IOException, KeyManagementException, CertificateException, KeyStoreException, IllegalArgumentException {`
- `sources/com/huawei/secure/android/common/ssl/SecureSSLSocketFactory.java:251`
  `public SecureSSLSocketFactory(X509TrustManager x509TrustManager) throws NoSuchAlgorithmException, KeyManagementException, IllegalArgumentException {`
- `sources/com/huawei/secure/android/common/ssl/SecureSSLSocketFactoryNew.java:38`
  `public SecureSSLSocketFactoryNew(InputStream inputStream, String str) throws NoSuchAlgorithmException, IOException, KeyManagementException, CertificateException, KeyStoreException, IllegalArgumentException {`
- `sources/com/huawei/secure/android/common/ssl/SecureSSLSocketFactoryNew.java:224`
  `public SecureSSLSocketFactoryNew(X509TrustManager x509TrustManager) throws NoSuchAlgorithmException, KeyManagementException, IllegalArgumentException {`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:169`
  `HttpsURLConnection httpsURLConnection2 = null;`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:176`
  `org.apache.http.conn.ssl.SSLSocketFactory sSLSocketFactory = this.c;`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:177`
  `if (sSLSocketFactory instanceof SecureApacheSSLSocketFactory) {`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:178`
  `((SecureApacheSSLSocketFactory) sSLSocketFactory).setContext(this.f3729h);`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:213`
  `if (httpsURLConnection3 != 0) {`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:216`
  `if (uRLConnectionOpenConnection instanceof HttpsURLConnection) {`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:217`
  `httpsURLConnection = (HttpsURLConnection) uRLConnectionOpenConnection;`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:219`
  `httpsURLConnection.setSSLSocketFactory(this.a);`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:220`
  `httpsURLConnection.setHostnameVerifier(this.b);`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:221`
  `httpsURLConnection.setRequestMethod("GET");`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:222`
  `httpsURLConnection.setConnectTimeout(10000);`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:223`
  `httpsURLConnection.setReadTimeout(20000);`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:224`
  `httpsURLConnection.connect();`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:225`
  `httpsURLConnection2 = httpsURLConnection;`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:285`
  `public void setSslSocketFactory(SSLSocketFactory sSLSocketFactory) {`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:286`
  `this.a = sSLSocketFactory;`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:297`
  `setSslSocketFactory(new SecureSSLSocketFactoryNew(new c(context)));`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:300`
  `setApacheSSLSocketFactory(new SecureApacheSSLSocketFactory((KeyStore) null, new c(context)));`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:332`
  `public WebViewSSLCheckThread(SslErrorHandler sslErrorHandler, String str, SSLSocketFactory sSLSocketFactory, HostnameVerifier hostnameVerifier) {`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:335`
  `setSslSocketFactory(sSLSocketFactory);`
- `sources/com/huawei/secure/android/common/ssl/WebViewSSLCheckThread.java:340`
  `public WebViewSSLCheckThread(SslErrorHandler sslErrorHandler, String str, org.apache.http.conn.ssl.SSLSocketFactory sSLSocketFactory, X509HostnameVerifier x509HostnameVerifier) {`

## BR078

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/cn/jiguang/net/HttpRequest.java:6`
  `import javax.net.ssl.HostnameVerifier;`
- `sources/cn/jiguang/net/HttpRequest.java:26`
  `private HostnameVerifier p;`
- `sources/com/dcloud/android/downloader/core/task/GetFileInfoTask.java:42`
  `((HttpsURLConnection) httpURLConnection).setHostnameVerifier(DCloudTrustManager.getHostnameVerifier(false));`
- `sources/com/dcloud/android/downloader/core/thread/DownloadThread.java:75`
  `((HttpsURLConnection) httpURLConnection3).setHostnameVerifier(DCloudTrustManager.getHostnameVerifier(false));`
- `sources/com/huawei/hms/framework/network/grs/h/g/a.java:7`
  `import com.huawei.secure.android.common.ssl.hostname.StrictHostnameVerifier;`
- `sources/com/huawei/hms/framework/network/grs/h/g/a.java:12`
  `import javax.net.ssl.HostnameVerifier;`
- `sources/com/huawei/hms/framework/network/grs/h/g/a.java:19`
  `public static HostnameVerifier a() {`
- `sources/com/huawei/secure/android/common/SecureApacheSSLSocketFactory.java:17`
  `import org.apache.http.conn.ssl.BrowserCompatHostnameVerifier;`
- `sources/com/huawei/secure/android/common/SecureApacheSSLSocketFactory.java:19`
  `import org.apache.http.conn.ssl.StrictHostnameVerifier;`
- `sources/com/huawei/secure/android/common/SecureApacheSSLSocketFactory.java:20`
  `import org.apache.http.conn.ssl.X509HostnameVerifier;`
- `sources/com/huawei/secure/android/common/SecureSSLSocketFactory.java:17`
  `import org.apache.http.conn.ssl.BrowserCompatHostnameVerifier;`
- `sources/com/huawei/secure/android/common/SecureSSLSocketFactory.java:18`
  `import org.apache.http.conn.ssl.StrictHostnameVerifier;`
- `sources/com/huawei/secure/android/common/SecureSSLSocketFactory.java:19`
  `import org.apache.http.conn.ssl.X509HostnameVerifier;`
- `sources/com/huawei/secure/android/common/ssl/SecureApacheSSLSocketFactory.java:18`
  `import org.apache.http.conn.ssl.BrowserCompatHostnameVerifier;`
- `sources/com/huawei/secure/android/common/ssl/SecureApacheSSLSocketFactory.java:20`
  `import org.apache.http.conn.ssl.StrictHostnameVerifier;`
- `sources/com/huawei/secure/android/common/ssl/SecureApacheSSLSocketFactory.java:21`
  `import org.apache.http.conn.ssl.X509HostnameVerifier;`
- `sources/com/huawei/secure/android/common/ssl/SecureSSLSocketFactory.java:18`
  `import org.apache.http.conn.ssl.BrowserCompatHostnameVerifier;`
- `sources/com/huawei/secure/android/common/ssl/SecureSSLSocketFactory.java:19`
  `import org.apache.http.conn.ssl.StrictHostnameVerifier;`
- `sources/com/huawei/secure/android/common/ssl/SecureSSLSocketFactory.java:20`
  `import org.apache.http.conn.ssl.X509HostnameVerifier;`
- `sources/com/huawei/secure/android/common/ssl/hostname/BrowserCompatHostnameVerifier.java:11`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/com/huawei/secure/android/common/ssl/hostname/StrictHostnameVerifier.java:11`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/com/kwad/components/ad/interstitial/report/InterstitialReportInfo.java:73`
  `Class.forName("okhttp3.OkHttpClient");`
- `sources/com/kwad/sdk/core/videocache/g.java:91`
  `Class.forName("okhttp3.OkHttpClient");`
- `sources/com/mobile/auth/x/b.java:17`
  `import javax.net.ssl.HostnameVerifier;`
- `sources/com/mobile/auth/x/b.java:259`
  `httpsURLConnection.setHostnameVerifier(new HostnameVerifier() { // from class: com.mobile.auth.x.b.1`
- `sources/com/mobile/auth/x/b.java:260`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/com/mobile/auth/x/b.java:263`
  `HostnameVerifier defaultHostnameVerifier = HttpsURLConnection.getDefaultHostnameVerifier();`
- `sources/com/mobile/auth/x/b.java:264`
  `if (defaultHostnameVerifier.verify("wostore.cn", sSLSession)) {`
- `sources/com/mobile/auth/x/b.java:267`
  `return defaultHostnameVerifier.verify("10010.com", sSLSession);`
- `sources/com/nostra13/dcloudimageloader/core/download/BaseImageDownloader.java:113`
  `httpsURLConnection.setHostnameVerifier(DCloudTrustManager.getHostnameVerifier(true));`
- `sources/com/umeng/umverify/c/a.java:38`
  `this.a = new HostnameVerifier() { // from class: com.umeng.umverify.c.a.1`
- `sources/com/umeng/umverify/c/a.java:39`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/com/umeng/umverify/c/a.java:44`
  `return HttpsURLConnection.getDefaultHostnameVerifier().verify("ai.login.umeng.com", sSLSession);`
- `sources/com/umeng/umverify/c/a.java:48`
  `httpsURLConnection2.setHostnameVerifier(this.a);`
- `sources/com/umeng/umverify/utils/d.java:56`
  `httpsURLConnection2.setHostnameVerifier(new HostnameVerifier() { // from class: com.umeng.umverify.utils.d.1`
- `sources/com/umeng/umverify/utils/d.java:57`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/com/umeng/umverify/utils/d.java:62`
  `return HttpsURLConnection.getDefaultHostnameVerifier().verify("ai.login.umeng.com", sSLSession);`
- `sources/dc/squareup/okhttp3/OkHttpClient.java:44`
  `import javax.net.ssl.HostnameVerifier;`
- `sources/dc/squareup/okhttp3/OkHttpClient.java:53`
  `public class OkHttpClient implements Cloneable, Call.Factory, WebSocket.Factory {`
- `sources/dc/squareup/okhttp3/OkHttpClient.java:163`
  `@Override // dc.squareup.okhttp3.internal.Internal`
- `sources/dc/squareup/okhttp3/OkHttpClient.java:174`
  `@Override // dc.squareup.okhttp3.internal.Internal`
- `sources/dc/squareup/okhttp3/internal/connection/RealConnection.java:347`
  `if (this.f4868h == null || route == null || route.b.type() != Proxy.Type.DIRECT || this.c.b.type() != Proxy.Type.DIRECT || !this.c.c.equals(route.c) || route.a.f4809j != OkHostnameVerifier.a || !k(address.a)) {`
- `sources/dc/squareup/okhttp3/internal/connection/RealConnection.java:437`
  `return handshake != null && OkHostnameVerifier.a.c(httpUrl.d, (X509Certificate) handshake.c.get(0));`
- `sources/dc/squareup/okhttp3/internal/http2/PushObserver.java:10`
  `public static final PushObserver a = new PushObserver() { // from class: dc.squareup.okhttp3.internal.http2.PushObserver.1`
- `sources/dc/squareup/okhttp3/internal/http2/PushObserver.java:11`
  `@Override // dc.squareup.okhttp3.internal.http2.PushObserver`
- `sources/dc/squareup/okhttp3/internal/http2/PushObserver.java:17`
  `@Override // dc.squareup.okhttp3.internal.http2.PushObserver`
- `sources/dc/squareup/okhttp3/internal/http2/PushObserver.java:22`
  `@Override // dc.squareup.okhttp3.internal.http2.PushObserver`
- `sources/dc/squareup/okhttp3/internal/http2/PushObserver.java:27`
  `@Override // dc.squareup.okhttp3.internal.http2.PushObserver`
- `sources/dc/squareup/okhttp3/internal/platform/AndroidPlatform.java:81`
  `@Override // dc.squareup.okhttp3.internal.tls.TrustRootIndex`
- `sources/dc/squareup/okhttp3/internal/platform/AndroidPlatform.java:146`
  `@Override // dc.squareup.okhttp3.internal.platform.Platform`
- `sources/dc/squareup/okhttp3/internal/platform/AndroidPlatform.java:156`
  `@Override // dc.squareup.okhttp3.internal.platform.Platform`
- `sources/dc/squareup/okhttp3/internal/platform/AndroidPlatform.java:167`
  `@Override // dc.squareup.okhttp3.internal.platform.Platform`
- `sources/dc/squareup/okhttp3/internal/platform/AndroidPlatform.java:274`
  `@Override // dc.squareup.okhttp3.internal.platform.Platform`
- `sources/dc/squareup/okhttp3/internal/platform/AndroidPlatform.java:319`
  `@Override // dc.squareup.okhttp3.internal.platform.Platform`
- `sources/dc/squareup/okhttp3/internal/platform/Jdk9Platform.java:62`
  `@Override // dc.squareup.okhttp3.internal.platform.Platform`
- `sources/dc/squareup/okhttp3/internal/platform/Platform.java:134`
  `str = a.M(str, " To see where this was allocated, set the OkHttpClient logger level to FINE: Logger.getLogger(OkHttpClient.class.getName()).setLevel(Level.FINE);");`
- `sources/io/dcloud/common/adapter/ui/webview/WebLoadEvent.java:325`
  `((HttpsURLConnection) httpURLConnection).setHostnameVerifier(DCloudTrustManager.getHostnameVerifier(true));`
- `sources/io/dcloud/common/adapter/util/DCloudTrustManager.java:13`
  `import org.apache.http.conn.ssl.X509HostnameVerifier;`
- `sources/io/dcloud/common/util/NetTool.java:43`
  `((HttpsURLConnection) httpURLConnection).setHostnameVerifier(getDefaultHostnameVerifier());`
- `sources/io/dcloud/common/util/NetTool.java:59`
  `public static HostnameVerifier getDefaultHostnameVerifier() {`
- `sources/io/dcloud/common/util/NetTool.java:60`
  `HostnameVerifier hostnameVerifier = sCustomeHostnameVerifier;`
- `sources/io/dcloud/common/util/NetTool.java:61`
  `return hostnameVerifier != null ? hostnameVerifier : DCloudTrustManager.getHostnameVerifier(true);`
- `sources/io/dcloud/common/util/net/NetWork.java:173`
  `((HttpsURLConnection) this.mRequest).setHostnameVerifier(NetTool.getDefaultHostnameVerifier());`
- `sources/io/dcloud/feature/weex/adapter/DefaultWebSocketAdapter.java:12`
  `import dc.squareup.okhttp3.OkHttpClient;`
- `sources/io/dcloud/feature/weex/adapter/DefaultWebSocketAdapter.java:13`
  `import dc.squareup.okhttp3.Request;`
- `sources/io/dcloud/feature/weex/adapter/DefaultWebSocketAdapter.java:14`
  `import dc.squareup.okhttp3.Response;`
- `sources/io/dcloud/feature/weex/adapter/DefaultWebSocketAdapter.java:15`
  `import dc.squareup.okhttp3.WebSocket;`
- `sources/io/dcloud/feature/weex/adapter/DefaultWebSocketAdapter.java:16`
  `import dc.squareup.okhttp3.WebSocketListener;`
- `sources/io/dcloud/feature/weex/adapter/DefaultWebSocketAdapter.java:59`
  `OkHttpClient.Builder builder = new OkHttpClient.Builder();`
- `sources/io/dcloud/feature/weex/adapter/DefaultWebSocketAdapter.java:73`
  `builder.a(DCloudTrustManager.getHostnameVerifier(false));`
- `sources/io/dcloud/feature/weex/adapter/DefaultWebSocketAdapter.java:216`
  `OkHttpClient.Builder builder = new OkHttpClient.Builder();`
- `sources/io/dcloud/feature/weex/adapter/DefaultWebSocketAdapter.java:237`
  `builder.a(DCloudTrustManager.getHostnameVerifier(false));`
- `sources/io/dcloud/net/DownloadNetWork.java:104`
  `((HttpsURLConnection) this.mUrlConn).setHostnameVerifier(DCloudTrustManager.getHostnameVerifier(false));`

## BR079

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/androidx/webkit/internal/ServiceWorkerWebSettingsImpl.java:105`
  `public void setAllowFileAccess(boolean z) {`
- `sources/androidx/webkit/internal/ServiceWorkerWebSettingsImpl.java:108`
  `b().setAllowFileAccess(z);`
- `sources/androidx/webkit/internal/ServiceWorkerWebSettingsImpl.java:113`
  `a().setAllowFileAccess(z);`
- `sources/cn/jpush/android/ad/a.java:220`
  `webSettings.setAllowFileAccess(false);`
- `sources/cn/jpush/android/ad/a.java:232`
  `webView.getSettings().setMixedContentMode(0);`
- `sources/cn/jpush/android/ad/a.java:565`
  `webSettings.setAllowFileAccess(false);`
- `sources/cn/jpush/android/ui/c.java:344`
  `this.g.getSettings().setJavaScriptEnabled(false);`
- `sources/com/cmic/sso/sdk/widget/a.java:94`
  `settings.setAllowFileAccess(false);`
- `sources/com/cmic/sso/sdk/widget/a.java:97`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/huawei/secure/android/common/webview/SafeWebSettings.java:13`
  `webSettings.setAllowFileAccess(false);`
- `sources/com/huawei/secure/android/common/webview/SafeWebSettings.java:14`
  `webSettings.setAllowFileAccessFromFileURLs(false);`
- `sources/com/huawei/secure/android/common/webview/SafeWebSettings.java:15`
  `webSettings.setAllowUniversalAccessFromFileURLs(false);`
- `sources/com/huawei/secure/android/common/webview/SafeWebSettings.java:23`
  `webSettings.setMixedContentMode(1);`
- `sources/com/kwad/components/ad/draw/b/b/c.java:107`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ad/f/e.java:391`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ad/feed/b/n.java:812`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ad/reward/n/e.java:53`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ad/reward/presenter/platdetail/actionbar/f.java:139`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ad/splashscreen/presenter/p.java:346`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ad/splashscreen/presenter/p.java:349`
  `webView.getSettings().setAllowFileAccess(true);`
- `sources/com/kwad/components/core/e/c/e.java:89`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/core/o/b/d/a.java:163`
  `public final void setAllowFileAccess(boolean z) {`
- `sources/com/kwad/components/core/o/b/d/a.java:164`
  `this.Qi.getSettings().setAllowFileAccess(z);`
- `sources/com/kwad/components/core/o/b/d/a.java:168`
  `public final void setAllowFileAccessFromFileURLs(boolean z) {`
- `sources/com/kwad/components/core/o/b/d/a.java:169`
  `this.Qi.getSettings().setAllowFileAccessFromFileURLs(z);`
- `sources/com/kwad/components/core/o/b/d/a.java:173`
  `public final void setAllowUniversalAccessFromFileURLs(boolean z) {`
- `sources/com/kwad/components/core/o/b/d/a.java:174`
  `this.Qi.getSettings().setAllowUniversalAccessFromFileURLs(z);`
- `sources/com/kwad/components/core/o/b/d/a.java:216`
  `public final void setJavaScriptEnabled(boolean z) {`
- `sources/com/kwad/components/core/o/b/d/a.java:217`
  `this.Qi.getSettings().setJavaScriptEnabled(z);`
- `sources/com/kwad/components/core/o/b/d/a.java:221`
  `public final void setMixedContentMode(int i2) {`
- `sources/com/kwad/components/core/o/b/d/a.java:222`
  `this.Qi.getSettings().setMixedContentMode(i2);`
- `sources/com/kwad/components/core/page/c/b.java:45`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/core/page/c/f.java:57`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/core/webview/b.java:285`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/core/webview/b.java:452`
  `webView.getSettings().setAllowFileAccess(true);`
- `sources/com/kwad/components/ct/coupon/a.java:106`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ct/coupon/a/a.java:79`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ct/detail/ad/presenter/c.java:185`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ct/detail/ad/presenter/a/b.java:224`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ct/detail/photo/a/e.java:110`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ct/home/a/e.java:328`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ct/horizontal/news/c/e.java:338`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ct/horizontal/video/presenter/a.java:113`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/components/ct/horizontal/video/presenter/b.java:163`
  `@SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface", "JavascriptInterface"})`
- `sources/com/kwad/sdk/utils/bv.java:12`
  `webView.getSettings().setAllowFileAccess(false);`
- `sources/com/kwad/sdk/utils/bv.java:22`
  `settings.setAllowFileAccess(true);`
- `sources/com/kwad/sdk/utils/bv.java:30`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/kwad/sdk/utils/bv.java:33`
  `settings.setAllowFileAccessFromFileURLs(false);`
- `sources/com/kwad/sdk/utils/bv.java:34`
  `settings.setAllowUniversalAccessFromFileURLs(false);`
- `sources/com/kwad/sdk/utils/bv.java:35`
  `settings.setMixedContentMode(0);`
- `sources/com/mobile/auth/gatewayauth/activity/AuthWebVeiwActivity.java:170`
  `settings.setAllowFileAccess(false);`
- `sources/com/mobile/auth/gatewayauth/activity/AuthWebVeiwActivity.java:171`
  `settings.setJavaScriptEnabled(this.g.isWebSupportedJavascript());`
- `sources/com/taobao/weex/ui/component/WXEmbed.java:229`
  `webView.getSettings().setAllowFileAccess(false);`
- `sources/com/taobao/weex/ui/view/WXWebView.java:101`
  `settings.setAllowFileAccess(false);`
- `sources/com/tencent/bugly/crashreport/CrashReport.java:729`
  `@SuppressLint({"SetJavaScriptEnabled"})`
- `sources/com/tencent/bugly/crashreport/CrashReport.java:736`
  `webView.getSettings().setAllowFileAccess(false);`
- `sources/com/tencent/bugly/crashreport/CrashReport.java:749`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/tencent/bugly/crashreport/CrashReport.java:907`
  `@SuppressLint({"SetJavaScriptEnabled"})`
- `sources/com/xs/smartlink/ui/WebActivity.java:161`
  `settings.setAllowFileAccess(true);`
- `sources/com/xs/smartlink/ui/WebActivity.java:162`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/xs/smartlink/ui/WebActivity.java:165`
  `settings.setMixedContentMode(0);`
- `sources/io/dcloud/WebviewActivity.java:733`
  `settings.setAllowFileAccess(false);`
- `sources/io/dcloud/common/adapter/ui/webview/SysWebView.java:596`
  `this.webSettings.setAllowFileAccess(false);`
- `sources/io/dcloud/common/adapter/ui/webview/SysWebView.java:627`
  `PlatformUtil.invokeMethod("android.webkit.WebSettings", "setMixedContentMode", this.webSettings, new Class[]{Integer.TYPE}, new Object[]{0});`
- `sources/io/dcloud/feature/gg/dcloud/AolWebView.java:44`
  `settings.setAllowFileAccess(false);`
- `sources/io/dcloud/feature/weex/adapter/webview/DCWXWebView.java:380`
  `settings.setAllowFileAccess(false);`
- `sources/io/dcloud/feature/weex/adapter/webview/DCWXWebView.java:384`
  `settings.setMixedContentMode(0);`
- `sources/io/dcloud/sdk/activity/WebViewActivity.java:545`
  `settings.setAllowFileAccess(false);`
- `sources/io/dcloud/sdk/activity/WebViewActivity.java:549`
  `settings.setJavaScriptEnabled(true);`
- `sources/io/dcloud/sdk/base/dcloud/d.java:90`
  `settings.setJavaScriptEnabled(true);`
- `sources/io/dcloud/sdk/base/dcloud/d.java:94`
  `settings.setAllowFileAccess(false);`

## BR080

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/androidtranscoder/engine/QueuedMuxer.java:122`
  `Log.v("QueuedMuxer", "Output format determined, writing " + this.f1049h.size() + " samples / " + this.g.limit() + " bytes to muxer.");`
- `sources/androidtranscoder/format/ExportPreset960x540Strategy.java:40`
  `Log.d("ExportPreset960x540Strategy", StringUtil.format("inputFormat: %dx%d => outputFormat: %dx%d", Integer.valueOf(integer), Integer.valueOf(integer2), Integer.valueOf(mediaFormatCreateVideoFormat.getInteger("width")), Integer.valueOf(mediaFormatCreateVideoFormat.getInteger("height"))));`
- `sources/androidx/constraintlayout/motion/widget/MotionScene.java:1390`
  `Log.v(TypedValues.MotionScene.NAME, " OnSwipe (" + context.getResources().getResourceEntryName(i2) + ".xml:" + xml.getLineNumber() + Operators.BRACKET_END_STR);`
- `sources/androidx/core/view/ViewCompat.java:1370`
  `Log.d("ViewCompat", "Error calling dispatchFinishTemporaryDetach", e2);`
- `sources/androidx/core/view/ViewCompat.java:1406`
  `Log.d("ViewCompat", "Error calling dispatchStartTemporaryDetach", e2);`
- `sources/androidx/exifinterface/media/ExifInterface.java:2753`
  `Log.d("ExifInterface", "getRafAttributes starting with: " + byteOrderedDataInputStream);`
- `sources/androidx/exifinterface/media/ExifInterface.java:3100`
  `Log.d("ExifInterface", "getWebpAttributes starting with: " + byteOrderedDataInputStream);`
- `sources/androidx/fragment/app/FragmentLayoutInflaterFactory.java:83`
  `Log.v("FragmentManager", "Fragment " + fragmentFindFragmentById + " has been inflated via the <fragment> tag: id=0x" + Integer.toHexString(resourceId));`
- `sources/androidx/fragment/app/FragmentLayoutInflaterFactory.java:97`
  `Log.v("FragmentManager", "Retained Fragment " + fragmentFindFragmentById + " has been re-attached via the <fragment> tag: id=0x" + Integer.toHexString(resourceId));`
- `sources/androidx/fragment/app/FragmentStateManager.java:76`
  `Log.d("FragmentManager", sbD0.toString());`
- `sources/androidx/localbroadcastmanager/content/LocalBroadcastManager.java:182`
  `Log.v("LocalBroadcastManager", "  Filter matched!  match=0x" + Integer.toHexString(iMatch));`
- `sources/com/bumptech/glide/load/data/HttpUrlFetcher.java:61`
  `Log.d("HttpUrlFetcher", "Failed to get a response code", e);`
- `sources/com/bumptech/glide/load/engine/bitmap_recycle/LruArrayPool.java:238`
  `Log.v(tag, sbD0.toString());`
- `sources/com/bumptech/glide/load/resource/bitmap/CenterInside.java:20`
  `Log.v("TransformationUtils", "requested target size too big for input, fit centering instead");`
- `sources/com/bumptech/glide/load/resource/bitmap/DefaultImageHeaderParser.java:316`
  `Log.d("DfltImageHeaderParser", "Missing jpeg exif preamble");`
- `sources/com/bumptech/glide/load/resource/bitmap/DefaultImageHeaderParser.java:359`
  `Log.d("DfltImageHeaderParser", "Illegal tagValueOffset=" + i8 + " tagType=" + ((int) sA3));`
- `sources/com/bumptech/glide/load/resource/bitmap/HardwareConfigState.java:205`
  `Log.v("HardwareConfig", "Hardware config disallowed because height is too small");`
- `sources/com/bumptech/glide/load/resource/bitmap/TransformationUtils.java:94`
  `Log.v("TransformationUtils", "requested target size matches input, returning input");`
- `sources/com/bumptech/glide/load/resource/bitmap/TransformationUtils.java:103`
  `Log.v("TransformationUtils", "adjusted target size matches input, returning input");`
- `sources/com/bumptech/glide/load/resource/bitmap/TransformationUtils.java:110`
  `Log.v("TransformationUtils", "request: " + i2 + Constants.Name.X + i3);`
- `sources/com/bumptech/glide/load/resource/bitmap/TransformationUtils.java:111`
  `Log.v("TransformationUtils", "toFit:   " + bitmap.getWidth() + Constants.Name.X + bitmap.getHeight());`
- `sources/com/bumptech/glide/load/resource/bitmap/TransformationUtils.java:112`
  `Log.v("TransformationUtils", "toReuse: " + bitmapC.getWidth() + Constants.Name.X + bitmapC.getHeight());`
- `sources/com/bumptech/glide/load/resource/bitmap/TransformationUtils.java:116`
  `Log.v("TransformationUtils", sb.toString());`
- `sources/com/davemorrissey/labs/subscaleview/decoder/SkiaPooledImageRegionDecoder.java:131`
  `Log.d(TAG, str);`
- `sources/com/dcloud/android/downloader/core/DownloadResponseImpl.java:83`
  `Log.d("DownloadResponseImpl", "progress:" + downloadInfo.getProgress() + ",size:" + downloadInfo.getSize());`
- `sources/com/dcloud/android/downloader/core/thread/DownloadThread.java:127`
  `Log.d("DownloadThread", "downloadInfo:" + this.d.getId() + " thread:" + this.a.getThreadId() + " progress:" + this.a.getProgress() + ",start:" + this.a.getStart() + ",end:" + this.a.getEnd());`
- `sources/com/dcloud/android/v4/view/ViewCompat.java:49`
  `Log.d("ViewCompat", "Error calling dispatchFinishTemporaryDetach", e);`
- `sources/com/dcloud/android/v4/view/ViewCompat.java:66`
  `Log.d("ViewCompat", "Error calling dispatchStartTemporaryDetach", e);`
- `sources/com/efs/sdk/net/OkHttpInterceptor.java:141`
  `Log.d("NetTrace-Interceptor", "begin intercept");`
- `sources/com/efs/sdk/net/OkHttpListener.java:231`
  `Log.d("NetTrace-Listener", "connectEnd");`
- `sources/com/efs/sdk/net/OkHttpListener.java:233`
  `Log.d("NetTrace-Listener", "connectEnd net enable false.");`
- `sources/com/efs/sdk/net/OkHttpListener.java:245`
  `Log.d("NetTrace-Listener", "connectFailed");`
- `sources/com/efs/sdk/net/OkHttpListener.java:247`
  `Log.d("NetTrace-Listener", "connectFailed net enable false.");`
- `sources/com/efs/sdk/net/OkHttpListener.java:260`
  `Log.d("NetTrace-Listener", "connectStart");`
- `sources/com/efs/sdk/net/OkHttpListener.java:262`
  `Log.d("NetTrace-Listener", "connectStart net enable false.");`
- `sources/com/efs/sdk/net/OkHttpListener.java:276`
  `Log.d("NetTrace-Listener", "callStart net enable false.");`
- `sources/com/efs/sdk/net/OkHttpListener.java:299`
  `Log.d("NetTrace-Listener", "dnsEnd");`
- `sources/com/efs/sdk/net/OkHttpListener.java:383`
  `Log.d("NetTrace-Listener", "responseBodyEnd");`
- `sources/com/efs/sdk/net/OkHttpListener.java:385`
  `Log.d("NetTrace-Listener", "responseBodyEnd net enable false.");`
- `sources/com/efs/sdk/net/OkHttpListener.java:397`
  `Log.d("NetTrace-Listener", "responseBodyStart");`

## BR081

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/aegon/chrome/net/AndroidKeyStore.java:16`
  `public class AndroidKeyStore {`
- `sources/aegon/chrome/net/AndroidKeyStore.java:17`
  `private static final String TAG = "AndroidKeyStore";`
- `sources/aegon/chrome/net/X509Util.java:183`
  `KeyStore keyStore = KeyStore.getInstance("AndroidCAStore");`
- `sources/aegon/chrome/net/X509Util.java:198`
  `KeyStore keyStore2 = KeyStore.getInstance(KeyStore.getDefaultType());`
- `sources/cn/jiguang/net/SSLTrustManager.java:27`
  `KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());`
- `sources/com/cmic/sso/sdk/c.java:21`
  `KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());`
- `sources/com/cmic/sso/sdk/h/e.java:4`
  `import android.security.keystore.KeyGenParameterSpec;`
- `sources/com/cmic/sso/sdk/h/e.java:30`
  `KeyStore keyStore = KeyStore.getInstance("AndroidKeyStore");`
- `sources/com/cmic/sso/sdk/h/e.java:36`
  `KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA", "AndroidKeyStore");`
- `sources/com/cmic/sso/sdk/h/e.java:37`
  `keyPairGenerator.initialize(new KeyGenParameterSpec.Builder("CMCC_SDK", 3).setDigests("SHA-256", "SHA-512").setEncryptionPaddings("PKCS1Padding").build());`
- `sources/com/cmic/sso/sdk/h/e.java:71`
  `KeyStore keyStore = KeyStore.getInstance("AndroidKeyStore");`
- `sources/com/huawei/hms/device/a.java:201`
  `keyStore = KeyStore.getInstance(j.e);`
- `sources/com/huawei/secure/android/common/encrypt/keystore/aes/AesCbcKS.java:3`
  `import android.security.keystore.KeyGenParameterSpec;`
- `sources/com/huawei/secure/android/common/encrypt/keystore/aes/AesCbcKS.java:33`
  `private static final String b = "AndroidKeyStore";`
- `sources/com/huawei/secure/android/common/encrypt/keystore/aes/AesCbcKS.java:50`
  `KeyStore keyStore = KeyStore.getInstance(b);`
- `sources/com/huawei/secure/android/common/encrypt/keystore/aes/AesCbcKS.java:56`
  `keyGenerator.init(new KeyGenParameterSpec.Builder(str, 3).setBlockModes("CBC").setEncryptionPaddings("PKCS7Padding").setKeySize(256).build());`
- `sources/com/huawei/secure/android/common/encrypt/keystore/aes/AesGcmKS.java:3`
  `import android.security.keystore.KeyGenParameterSpec;`
- `sources/com/huawei/secure/android/common/encrypt/keystore/aes/AesGcmKS.java:34`
  `private static final String b = "AndroidKeyStore";`
- `sources/com/huawei/secure/android/common/encrypt/keystore/aes/AesGcmKS.java:45`
  `KeyStore keyStore = KeyStore.getInstance(b);`
- `sources/com/huawei/secure/android/common/encrypt/keystore/aes/AesGcmKS.java:53`
  `keyGenerator.init(new KeyGenParameterSpec.Builder(str, 3).setBlockModes(CodePackage.GCM).setEncryptionPaddings("NoPadding").setKeySize(256).build());`
- `sources/com/huawei/secure/android/common/encrypt/keystore/rsa/RSAEncryptKS.java:3`
  `import android.security.keystore.KeyGenParameterSpec;`
- `sources/com/huawei/secure/android/common/encrypt/keystore/rsa/RSAEncryptKS.java:34`
  `private static final String b = "AndroidKeyStore";`
- `sources/com/huawei/secure/android/common/encrypt/keystore/rsa/RSAEncryptKS.java:118`
  `KeyStore keyStore = KeyStore.getInstance(b);`
- `sources/com/huawei/secure/android/common/encrypt/keystore/rsa/RSAEncryptKS.java:290`
  `KeyStore keyStore = KeyStore.getInstance(b);`
- `sources/com/huawei/secure/android/common/encrypt/keystore/rsa/RSAEncryptKS.java:341`
  `keyPairGenerator.initialize(new KeyGenParameterSpec.Builder(str, 2).setDigests("SHA-256", "SHA-512").setEncryptionPaddings("OAEPPadding").setKeySize(2048).build());`
- `sources/com/huawei/secure/android/common/encrypt/keystore/rsa/RSAEncryptKS.java:343`
  `keyPairGenerator.initialize(new KeyGenParameterSpec.Builder(str, 2).setDigests("SHA-256", "SHA-512").setEncryptionPaddings("OAEPPadding").setKeySize(f).build());`
- `sources/com/huawei/secure/android/common/encrypt/keystore/rsa/RSAEncryptKS.java:365`
  `KeyStore keyStore = KeyStore.getInstance(b);`
- `sources/com/huawei/secure/android/common/encrypt/keystore/rsa/RSASignKS.java:3`
  `import android.security.keystore.KeyGenParameterSpec;`
- `sources/com/huawei/secure/android/common/encrypt/keystore/rsa/RSASignKS.java:28`
  `private static final String b = "AndroidKeyStore";`
- `sources/com/huawei/secure/android/common/encrypt/keystore/rsa/RSASignKS.java:83`
  `KeyStore keyStore = KeyStore.getInstance(b);`
- `sources/com/huawei/secure/android/common/encrypt/keystore/rsa/RSASignKS.java:250`
  `keyPairGenerator.initialize(new KeyGenParameterSpec.Builder(str, 12).setDigests("SHA-256", "SHA-512").setSignaturePaddings("PSS").setKeySize(2048).build());`
- `sources/com/huawei/secure/android/common/encrypt/keystore/rsa/RSASignKS.java:252`
  `keyPairGenerator.initialize(new KeyGenParameterSpec.Builder(str, 12).setDigests("SHA-256", "SHA-512").setSignaturePaddings("PSS").setKeySize(f).build());`
- `sources/com/huawei/secure/android/common/encrypt/keystore/rsa/RSASignKS.java:268`
  `KeyStore keyStore = KeyStore.getInstance(b);`
- `sources/com/huawei/secure/android/common/ssl/SecureX509TrustManager.java:45`
  `KeyStore keyStore = KeyStore.getInstance(f3727h);`
- `sources/com/huawei/secure/android/common/ssl/SecureX509TrustManager.java:267`
  `KeyStore keyStore = KeyStore.getInstance("bks");`
- `sources/com/huawei/secure/android/common/ssl/SecureX509TrustManager.java:287`
  `KeyStore keyStore = KeyStore.getInstance("bks");`
- `sources/com/huawei/secure/android/common/ssl/util/CertificateUtil.java:34`
  `KeyStore keyStore = KeyStore.getInstance(j.e);`
- `sources/com/huawei/secure/android/common/ssl/util/j.java:45`
  `keyStore = KeyStore.getInstance(e);`
- `sources/com/kuaishou/weapon/p0/am.java:50`
  `KeyStore keyStore = KeyStore.getInstance("AndroidCAStore");`
- `sources/com/mobile/auth/e/a.java:44`
  `com.cmic.sso.sdk.h.f.b("AuthnHelper", com.cmic.sso.sdk.h.e.a(a.this.c) ? "生成androidkeystore成功" : "生成androidkeystore失败");`
- `sources/com/vivo/push/c/a.java:3`
  `import android.security.keystore.KeyGenParameterSpec;`
- `sources/com/vivo/push/c/a.java:22`
  `KeyStore keyStore = KeyStore.getInstance("AndroidKeyStore");`
- `sources/com/vivo/push/c/a.java:40`
  `KeyGenerator keyGenerator = KeyGenerator.getInstance("AES", "AndroidKeyStore");`
- `sources/com/vivo/push/c/a.java:41`
  `keyGenerator.init(new KeyGenParameterSpec.Builder("AesKeyAlias", 3).setBlockModes(CodePackage.GCM).setEncryptionPaddings("NoPadding").setKeySize(256).build());`
- `sources/com/vivo/push/c/e.java:77`
  `KeyStore keyStore = KeyStore.getInstance("AndroidKeyStore");`
- `sources/com/vivo/push/c/e.java:139`
  `KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA", "AndroidKeyStore");`
- `sources/io/dcloud/feature/weex/config/UserCustomTrustManager.java:41`
  `KeyStore keyStore = KeyStore.getInstance("PKCS12");`
- `sources/io/dcloud/feature/weex/config/UserCustomTrustManager.java:54`
  `KeyStore keyStore2 = KeyStore.getInstance("PKCS12");`
- `sources/io/dcloud/feature/weex/config/UserCustomTrustManager.java:110`
  `KeyStore keyStore = KeyStore.getInstance("PKCS12");`
- `sources/io/dcloud/feature/weex/config/UserCustomTrustManager.java:123`
  `KeyStore keyStore2 = KeyStore.getInstance("PKCS12");`

## BR082

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/androidx/core/content/FileProvider.java:79`
  `@Override // androidx.core.content.FileProvider.PathStrategy`
- `sources/androidx/core/content/FileProvider.java:101`
  `@Override // androidx.core.content.FileProvider.PathStrategy`
- `sources/com/dmcbig/mediapicker/TakePhotoActivity.java:11`
  `import androidx.core.content.FileProvider;`
- `sources/com/dmcbig/mediapicker/TakePhotoActivity.java:53`
  `Uri uriForFile = FileProvider.getUriForFile(this, getPackageName() + ".dmc", this.mTmpFile);`
- `sources/com/huawei/updatesdk/support/pm/PackageInstallerActivity.java:30`
  `uriFromFile = UpdateSdkFileProvider.getUriForFile(context, context.getApplicationContext().getPackageName() + UpdateSdkFileProvider.AUTHORITIES_SUFFIX, new File(str));`
- `sources/com/kwad/sdk/api/proxy/app/AdSdkFileProvider.java:4`
  `import androidx.core.content.FileProvider;`
- `sources/com/kwad/sdk/api/proxy/app/AdSdkFileProvider.java:12`
  `@Override // androidx.core.content.FileProvider, android.content.ContentProvider`
- `sources/com/kwad/sdk/utils/am.java:42`
  `uriFromFile = FileProvider.getUriForFile(context, context.getPackageName() + ".adFileProvider", file);`
- `sources/com/kwad/sdk/utils/an.java:34`
  `return FileProvider.getUriForFile(context, context.getPackageName() + ".adFileProvider", file);`
- `sources/io/dcloud/common/adapter/ui/webview/WebJsEvent.java:31`
  `import androidx.core.content.FileProvider;`
- `sources/io/dcloud/common/adapter/ui/webview/WebJsEvent.java:278`
  `arrayList.add(FileProvider.getUriForFile(WebJsEvent.this.mAdaWebview.getActivity(), WebJsEvent.this.mAdaWebview.getActivity().getPackageName() + ".dc.fileprovider", next));`
- `sources/io/dcloud/common/util/DCloud_FileProvider.java:3`
  `import androidx.core.content.FileProvider;`
- `sources/io/dcloud/common/util/FileUtil.java:17`
  `import androidx.core.content.FileProvider;`
- `sources/io/dcloud/common/util/FileUtil.java:383`
  `dCFileUriData.fileUri = FileProvider.getUriForFile(context, context.getPackageName() + ".dc.fileprovider", file2);`
- `sources/io/dcloud/common/util/FileUtil.java:394`
  `dCFileUriData.fileUri = FileProvider.getUriForFile(context, context.getPackageName() + ".dc.fileprovider", file);`
- `sources/io/dcloud/common/util/LoadAppUtils.java:17`
  `import androidx.core.content.FileProvider;`
- `sources/io/dcloud/common/util/LoadAppUtils.java:243`
  `Uri uriForFile = FileProvider.getUriForFile(context, a.s(context, new StringBuilder(), ".dc.fileprovider"), new File(str));`
- `sources/io/dcloud/feature/weex/adapter/webview/DCWXWebView.java:35`
  `import androidx.core.content.FileProvider;`
- `sources/io/dcloud/feature/weex/adapter/webview/DCWXWebView.java:257`
  `uriForFile = FileProvider.getUriForFile(DCWXWebView.this.mContext, DCWXWebView.this.mContext.getPackageName() + ".dc.fileprovider", file);`
- `sources/io/dcloud/js/camera/CameraFeatureImpl.java:11`
  `import androidx.core.content.FileProvider;`
- `sources/io/dcloud/js/camera/CameraFeatureImpl.java:425`
  `intent.putExtra("output", FileProvider.getUriForFile(this.c.getContext(), this.c.getContext().getPackageName() + ".dc.fileprovider", file));`
- `sources/io/dcloud/sdk/base/service/provider/DCloudAdFileProvider.java:3`
  `import androidx.core.content.FileProvider;`
- `sources/io/dcloud/share/a.java:13`
  `import androidx.core.content.FileProvider;`
- `sources/io/dcloud/share/a.java:255`
  `uriForFile = FileProvider.getUriForFile(context, context.getPackageName() + ".dc.fileprovider", file);`
- `sources/io/dcloud/share/mm/WeiXinApiManager.java:16`
  `import androidx.core.content.FileProvider;`
- `sources/io/dcloud/share/mm/WeiXinApiManager.java:457`
  `Uri uriForFile = FileProvider.getUriForFile(context, context.getPackageName() + ".dc.fileprovider", new File(str3));`

## BR086

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/aegon/chrome/base/ApiCompatibilityUtils.java:49`
  `public static class FinishAndRemoveTaskWithRetry implements Runnable {`
- `sources/aegon/chrome/base/ApiCompatibilityUtils.java:55`
  `public FinishAndRemoveTaskWithRetry(Activity activity) {`
- `sources/aegon/chrome/base/ApiCompatibilityUtils.java:61`
  `this.mActivity.finishAndRemoveTask();`
- `sources/aegon/chrome/base/ApiCompatibilityUtils.java:172`
  `public static void finishAfterTransition(Activity activity) {`
- `sources/aegon/chrome/base/ApiCompatibilityUtils.java:173`
  `activity.finishAfterTransition();`
- `sources/aegon/chrome/base/ApiCompatibilityUtils.java:176`
  `public static void finishAndRemoveTask(Activity activity) {`
- `sources/aegon/chrome/base/ApiCompatibilityUtils.java:177`
  `activity.finishAndRemoveTask();`
- `sources/aegon/chrome/base/ContextUtils.java:8`
  `import android.content.SharedPreferences;`
- `sources/aegon/chrome/base/ContextUtils.java:22`
  `private static SharedPreferences sSharedPreferences = ContextUtils.fetchAppSharedPreferences();`
- `sources/aegon/chrome/base/ContextUtils.java:72`
  `SharedPreferences unused = Holder.sSharedPreferences = fetchAppSharedPreferences();`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:230`
  `if (!ContextUtils.getAppSharedPreferences().getBoolean(BACKGROUND_STARTUP_TRACING_ENABLED_KEY, false)) {`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:268`
  `private static native void nativeRecordEarlyFinishAsyncEvent(String str, long j2, long j3);`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:285`
  `ContextUtils.getAppSharedPreferences().edit().putBoolean(BACKGROUND_STARTUP_TRACING_ENABLED_KEY, z).apply();`
- `sources/aegon/chrome/base/JavaExceptionReporter.java:14`
  `private final boolean mCrashAfterReport;`
- `sources/aegon/chrome/base/JavaExceptionReporter.java:20`
  `this.mCrashAfterReport = z;`
- `sources/aegon/chrome/base/JavaExceptionReporter.java:41`
  `nativeReportJavaException(this.mCrashAfterReport, th);`
- `sources/aegon/chrome/base/TraceEvent.java:192`
  `public static void finishAsync(String str, long j2) {`
- `sources/aegon/chrome/base/TraceEvent.java:193`
  `EarlyTraceEvent.finishAsync(str, j2);`
- `sources/aegon/chrome/base/TraceEvent.java:195`
  `nativeFinishAsync(str, j2);`
- `sources/aegon/chrome/base/TraceEvent.java:222`
  `private static native void nativeFinishAsync(String str, long j2);`
- `sources/aegon/chrome/base/compat/ApiHelperForN.java:50`
  `public static boolean startDragAndDrop(View view, ClipData clipData, View.DragShadowBuilder dragShadowBuilder, Object obj, int i2) {`
- `sources/aegon/chrome/base/compat/ApiHelperForN.java:51`
  `return view.startDragAndDrop(clipData, dragShadowBuilder, obj, i2);`
- `sources/aegon/chrome/net/AndroidNetworkLibrary.java:57`
  `private static Boolean sHaveAccessNetworkState;`
- `sources/aegon/chrome/net/AndroidNetworkLibrary.java:58`
  `private static Boolean sHaveAccessWifiState;`
- `sources/aegon/chrome/net/NetError.java:167`
  `public static final int ERR_QUIC_HANDSHAKE_FAILED = -358;`
- `sources/aegon/chrome/net/NetError.java:195`
  `public static final int ERR_SSL_DECRYPT_ERROR_ALERT = -153;`
- `sources/aegon/chrome/net/NetError.java:196`
  `public static final int ERR_SSL_HANDSHAKE_NOT_COMPLETED = -148;`
- `sources/aegon/chrome/net/UrlRequest.java:57`
  `public static final int SSL_HANDSHAKE = 11;`
- `sources/aegon/chrome/net/impl/LoadState.java:14`
  `public static final int SSL_HANDSHAKE = 12;`
- `sources/androidx/appcompat/R.java:70`
  `public static final int actionModeShareDrawable = 0x7f03001d;`
- `sources/androidx/appcompat/R.java:546`
  `public static final int abc_ab_share_pack_mtrl_alpha = 0x7f070007;`
- `sources/androidx/appcompat/R.java:554`
  `public static final int abc_btn_default_mtrl_shape = 0x7f07000f;`
- `sources/androidx/appcompat/R.java:1371`
  `public static final int AppCompatTheme_actionModeShareDrawable = 0x0000001b;`
- `sources/androidx/appcompat/R.java:1484`
  `public static final int DrawerArrowToggle_arrowShaftLength = 0x00000001;`
- `sources/androidx/appcompat/R.java:1700`
  `public static final int[] AppCompatTheme = {android.R.attr.windowIsFloating, android.R.attr.windowAnimationStyle, com.xs.smartlink.R.attr.actionBarDivider, com.xs.smartlink.R.attr.actionBarItemBackground, com.xs.smartlink.R.attr.actionBarPopupTheme, com.xs.smartlink.R.attr.actionBarSize, com.xs.smar...`
- `sources/androidx/appcompat/R.java:1704`
  `public static final int[] DrawerArrowToggle = {com.xs.smartlink.R.attr.arrowHeadLength, com.xs.smartlink.R.attr.arrowShaftLength, com.xs.smartlink.R.attr.barLength, com.xs.smartlink.R.attr.color, com.xs.smartlink.R.attr.drawableSize, com.xs.smartlink.R.attr.gapBetweenBars, com.xs.smartlink.R.attr.sp...`
- `sources/androidx/appcompat/R.java:1725`
  `public static final int[] TextAppearance = {android.R.attr.textSize, android.R.attr.typeface, android.R.attr.textStyle, android.R.attr.textColor, android.R.attr.textColorHint, android.R.attr.textColorLink, android.R.attr.shadowColor, android.R.attr.shadowDx, android.R.attr.shadowDy, android.R.attr.s...`
- `sources/androidx/appcompat/app/AppCompatDelegate.java:143`
  `public abstract boolean isHandleNativeActionModesEnabled();`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:518`
  `return (AppCompatDelegateImpl.this.isHandleNativeActionModesEnabled() && i2 == 0) ? a(callback) : super.onWindowStartingActionMode(callback, i2);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1531`
  `public boolean isHandleNativeActionModesEnabled() {`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:76`
  `this.d = typedArrayObtainStyledAttributes.getDimension(R.styleable.DrawerArrowToggle_arrowShaftLength, BorderDrawable.DEFAULT_BORDER_WIDTH);`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:9`
  `import android.graphics.Shader;`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:72`
  `public final int[] a = {R.drawable.abc_textfield_search_default_mtrl_alpha, R.drawable.abc_textfield_default_mtrl_alpha, R.drawable.abc_ab_share_pack_mtrl_alpha};`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:73`
  `public final int[] b = {R.drawable.abc_ic_commit_search_api_mtrl_alpha, R.drawable.abc_seekbar_tick_mark_material, R.drawable.abc_ic_menu_share_mtrl_alpha, R.drawable.abc_ic_menu_copy_mtrl_am_alpha, R.drawable.abc_ic_menu_cut_mtrl_alpha, R.drawable.abc_ic_menu_selectall_mtrl_alpha, R.drawable.abc_ic...`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:111`
  `bitmapDrawable2.setTileModeX(Shader.TileMode.REPEAT);`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:164`
  `if (i2 == R.drawable.abc_btn_default_mtrl_shape) {`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:5`
  `import android.graphics.BitmapShader;`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:6`
  `import android.graphics.Shader;`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:12`
  `import android.graphics.drawable.ShapeDrawable;`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:13`
  `import android.graphics.drawable.shapes.RoundRectShape;`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:84`
  `ShapeDrawable shapeDrawable = new ShapeDrawable(new RoundRectShape(new float[]{5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f}, null, null));`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:85`
  `shapeDrawable.getPaint().setShader(new BitmapShader(bitmap, Shader.TileMode.REPEAT, Shader.TileMode.CLAMP));`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:86`
  `shapeDrawable.getPaint().setColorFilter(bitmapDrawable.getPaint().getColorFilter());`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:87`
  `return z ? new ClipDrawable(shapeDrawable, 3, 1) : shapeDrawable;`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:102`
  `this.f.getTheme().resolveAttribute(R.attr.actionModeShareDrawable, typedValue, true);`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:105`
  `activityChooserView.setDefaultActionButtonContentDescription(R.string.abc_shareactionprovider_share_with_application);`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:106`
  `activityChooserView.setExpandActivityOverflowButtonContentDescription(R.string.abc_shareactionprovider_share_with);`
- `sources/androidx/camera/camera2/internal/Camera2CameraControlImpl.java:25`
  `import androidx.camera.camera2.internal.compat.workaround.AutoFlashAEModeDisabler;`
- `sources/androidx/camera/camera2/internal/Camera2CameraControlImpl.java:102`
  `public final AutoFlashAEModeDisabler q;`
- `sources/androidx/camera/camera2/internal/Camera2CameraControlImpl.java:206`
  `this.q = new AutoFlashAEModeDisabler();`
- `sources/androidx/camera/camera2/internal/compat/params/OutputConfigurationCompat.java:25`
  `void enableSurfaceSharing();`
- `sources/androidx/camera/camera2/internal/compat/params/OutputConfigurationCompat.java:27`
  `int getMaxSharedSurfaceCount();`
- `sources/androidx/camera/camera2/internal/compat/params/OutputConfigurationCompat.java:79`
  `public void enableSurfaceSharing() {`
- `sources/androidx/camera/camera2/internal/compat/params/OutputConfigurationCompat.java:80`
  `this.a.enableSurfaceSharing();`
- `sources/androidx/camera/camera2/internal/compat/params/OutputConfigurationCompat.java:90`
  `public int getMaxSharedSurfaceCount() {`
- `sources/androidx/camera/camera2/internal/compat/params/OutputConfigurationCompat.java:91`
  `return this.a.getMaxSharedSurfaceCount();`
- `sources/androidx/camera/camera2/internal/compat/params/OutputConfigurationCompatApi24Impl.java:56`
  `public void enableSurfaceSharing() {`
- `sources/androidx/camera/camera2/internal/compat/params/OutputConfigurationCompatApi26Impl.java:51`
  `throw new AssertionError("isSurfaceSharingEnabled() should not be called on API >= 26");`
- `sources/androidx/camera/camera2/internal/compat/params/OutputConfigurationCompatApi26Impl.java:60`
  `public void enableSurfaceSharing() {`
- `sources/androidx/camera/camera2/internal/compat/params/OutputConfigurationCompatApi26Impl.java:61`
  `((OutputConfiguration) getOutputConfiguration()).enableSurfaceSharing();`
- `sources/androidx/camera/camera2/internal/compat/params/OutputConfigurationCompatApi26Impl.java:65`
  `public int getMaxSharedSurfaceCount() {`
- `sources/androidx/camera/camera2/internal/compat/params/OutputConfigurationCompatApi26Impl.java:71`
  `Logger.e("OutputConfigCompat", "Unable to retrieve max shared surface count.", e);`
- `sources/androidx/camera/camera2/internal/compat/params/OutputConfigurationCompatApi26Impl.java:72`
  `return super.getMaxSharedSurfaceCount();`
- `sources/androidx/camera/camera2/internal/compat/params/OutputConfigurationCompatApi28Impl.java:19`
  `return ((OutputConfiguration) getOutputConfiguration()).getMaxSharedSurfaceCount();`
- `sources/androidx/camera/camera2/internal/compat/params/OutputConfigurationCompatBaseImpl.java:108`
  `throw new IllegalStateException("Cannot have 2 surfaces for a non-sharing configuration");`
- `sources/androidx/camera/camera2/internal/compat/params/OutputConfigurationCompatBaseImpl.java:114`
  `public void enableSurfaceSharing() {`
- `sources/androidx/camera/camera2/internal/compat/params/OutputConfigurationCompatBaseImpl.java:126`
  `public int getMaxSharedSurfaceCount() {`
- `sources/androidx/camera/camera2/internal/compat/workaround/AutoFlashAEModeDisabler.java:4`
  `import androidx.camera.camera2.internal.compat.quirk.CrashWhenTakingPhotoWithAutoFlashAEModeQuirk;`
- `sources/androidx/camera/camera2/internal/compat/workaround/AutoFlashAEModeDisabler.java:9`
  `public class AutoFlashAEModeDisabler {`
- `sources/androidx/camera/camera2/internal/compat/workaround/AutoFlashAEModeDisabler.java:11`
  `if (((CrashWhenTakingPhotoWithAutoFlashAEModeQuirk) DeviceQuirks.get(CrashWhenTakingPhotoWithAutoFlashAEModeQuirk.class)) == null || i2 != 2) {`

## BR088

paper_id: B004
paper_title: Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation

- `sources/androidx/exifinterface/media/ExifInterface.java:61`
  `import no.nordicsemi.android.dfu.DfuBaseService;`
- `sources/androidx/exifinterface/media/ExifInterface.java:850`
  `ExifTag[] exifTagArr = {new ExifTag("NewSubfileType", 254, 4), new ExifTag("SubfileType", 255, 4), new ExifTag("ImageWidth", 256, 3, 4), new ExifTag("ImageLength", 257, 3, 4), new ExifTag("BitsPerSample", 258, 3), new ExifTag("Compression", 259, 3), new ExifTag("PhotometricInterpretation", 262, 3), ...`
- `sources/androidx/exifinterface/media/ExifInterface.java:858`
  `ExifTag[] exifTagArr5 = {new ExifTag("NewSubfileType", 254, 4), new ExifTag("SubfileType", 255, 4), new ExifTag("ThumbnailImageWidth", 256, 3, 4), new ExifTag("ThumbnailImageLength", 257, 3, 4), new ExifTag("BitsPerSample", 258, 3), new ExifTag("Compression", 259, 3), new ExifTag("PhotometricInterpr...`
- `sources/com/dcloud/zxing2/maxicode/decoder/BitMatrixParser.java:12`
  `import no.nordicsemi.android.dfu.DfuBaseService;`
- `sources/com/dcloud/zxing2/maxicode/decoder/BitMatrixParser.java:17`
  `public static final int[][] b = {new int[]{121, 120, 127, 126, 133, 132, 139, 138, 145, IjkMediaMeta.FF_PROFILE_H264_HIGH_444, 151, WeiXinApiManager.THUMB_SIZE, 157, 156, 163, 162, 169, 168, 175, 174, 181, 180, 187, 186, 193, 192, 199, 198, -2, -2}, new int[]{123, 122, 129, 128, 135, 134, 141, 140, ...`
- `sources/com/dcloud/zxing2/pdf417/PDF417Common.java:26`
  `import no.nordicsemi.android.dfu.DfuBaseService;`
- `sources/com/dcloud/zxing2/pdf417/PDF417Common.java:36`
  `2280, 1577, 2295, 2293, 2291, 579, 577, 574, 571, 2298, 582, 581, 1592, 2263, 2262, 2260, 2258, 1545, 2255, 1544, 2252, 1541, 2273, 2271, 2269, 2266, 1550, 535, 532, 2279, 528, 2277, 546, 543, 549, 1575, 1573, 2224, 2222, 2220, 1486, 2217, 1485, 2214, 1482, 1479, 2238, 2236, 2234, 2231, 1496, 2228, ...`
- `sources/com/kwad/components/core/webview/tachikoma/i.java:74`
  `import no.nordicsemi.android.dfu.DfuBaseService;`
- `sources/com/kwad/sdk/core/response/model/AdMatrixInfo.java:321`
  `public boolean endCardFullScreenClick;`
- `sources/com/xs/smartlink/R.java:6708`
  `public static final int dfu_action_abort = 0x7f1101c6;`
- `sources/com/xs/smartlink/R.java:6709`
  `public static final int dfu_channel_description = 0x7f1101c7;`
- `sources/com/xs/smartlink/R.java:6710`
  `public static final int dfu_channel_name = 0x7f1101c8;`
- `sources/com/xs/smartlink/R.java:6711`
  `public static final int dfu_status_aborted = 0x7f1101c9;`
- `sources/com/xs/smartlink/R.java:6712`
  `public static final int dfu_status_aborted_msg = 0x7f1101ca;`
- `sources/com/xs/smartlink/R.java:6713`
  `public static final int dfu_status_aborting = 0x7f1101cb;`
- `sources/com/xs/smartlink/R.java:6714`
  `public static final int dfu_status_completed = 0x7f1101cc;`
- `sources/com/xs/smartlink/R.java:6715`
  `public static final int dfu_status_completed_msg = 0x7f1101cd;`
- `sources/com/xs/smartlink/R.java:6719`
  `public static final int dfu_status_disconnecting_msg = 0x7f1101d1;`
- `sources/com/xs/smartlink/R.java:6720`
  `public static final int dfu_status_error = 0x7f1101d2;`
- `sources/com/xs/smartlink/R.java:6721`
  `public static final int dfu_status_error_msg = 0x7f1101d3;`
- `sources/com/xs/smartlink/R.java:6722`
  `public static final int dfu_status_foreground_content = 0x7f1101d4;`
- `sources/com/xs/smartlink/R.java:6723`
  `public static final int dfu_status_foreground_title = 0x7f1101d5;`
- `sources/com/xs/smartlink/R.java:6724`
  `public static final int dfu_status_initializing = 0x7f1101d6;`
- `sources/com/xs/smartlink/R.java:6725`
  `public static final int dfu_status_starting = 0x7f1101d7;`
- `sources/com/xs/smartlink/R.java:6726`
  `public static final int dfu_status_starting_msg = 0x7f1101d8;`
- `sources/com/xs/smartlink/R.java:6727`
  `public static final int dfu_status_switching_to_dfu = 0x7f1101d9;`
- `sources/com/xs/smartlink/R.java:6728`
  `public static final int dfu_status_switching_to_dfu_msg = 0x7f1101da;`
- `sources/com/xs/smartlink/R.java:6729`
  `public static final int dfu_status_uploading = 0x7f1101db;`
- `sources/com/xs/smartlink/R.java:6730`
  `public static final int dfu_status_uploading_msg = 0x7f1101dc;`
- `sources/com/xs/smartlink/R.java:6731`
  `public static final int dfu_status_uploading_part = 0x7f1101dd;`
- `sources/com/xs/smartlink/R.java:6732`
  `public static final int dfu_status_validating = 0x7f1101de;`
- `sources/com/xs/smartlink/R.java:6733`
  `public static final int dfu_status_validating_msg = 0x7f1101df;`
- `sources/com/xs/smartlink/R.java:6734`
  `public static final int dfu_unknown_name = 0x7f1101e0;`
- `sources/io/dcloud/common/util/BaseInfo.java:125`
  `public static String sDownloadFullPath = null;`
- `sources/io/dcloud/common/util/BaseInfo.java:672`
  `String str = sDownloadFullPath;`
- `sources/io/dcloud/common/util/BaseInfo.java:674`
  `sDownloadFullPath = DeviceInfo.sBaseFsRootPath + REAL_PUBLIC_DOWNLOADS_DIR;`
- `sources/io/dcloud/common/util/BaseInfo.java:676`
  `sDownloadFullPath = PdrUtil.appendByDeviceRootDir(sDownloadFullPath);`
- `sources/io/dcloud/common/util/ExifInterface.java:56`
  `import no.nordicsemi.android.dfu.DfuBaseService;`
- `sources/io/dcloud/common/util/ExifInterface.java:1172`
  `ExifTag[] exifTagArr = {new ExifTag("NewSubfileType", 254, 4), new ExifTag("SubfileType", 255, 4), new ExifTag("ImageWidth", 256, 3, 4), new ExifTag("ImageLength", 257, 3, 4), new ExifTag("BitsPerSample", 258, 3), new ExifTag("Compression", 259, 3), new ExifTag("PhotometricInterpretation", 262, 3), ...`
- `sources/io/dcloud/common/util/ExifInterface.java:1180`
  `ExifTag[] exifTagArr5 = {new ExifTag("NewSubfileType", 254, 4), new ExifTag("SubfileType", 255, 4), new ExifTag("ThumbnailImageWidth", 256, 3, 4), new ExifTag("ThumbnailImageLength", 257, 3, 4), new ExifTag("BitsPerSample", 258, 3), new ExifTag("Compression", 259, 3), new ExifTag("PhotometricInterpr...`
- `sources/io/dcloud/e/b/e.java:777`
  `return BaseInfo.sDownloadFullPath + str2.substring(11);`
- `sources/io/dcloud/e/b/e.java:780`
  `return BaseInfo.sDownloadFullPath + str2.substring(10);`
- `sources/io/dcloud/e/b/e.java:866`
  `int length4 = BaseInfo.sDownloadFullPath.length();`
- `sources/io/dcloud/e/b/e.java:885`
  `} else if (str.startsWith(BaseInfo.sDownloadFullPath)) {`
- `sources/io/dcloud/e/b/e.java:889`
  `if (str.startsWith(BaseInfo.sDownloadFullPath.substring(0, i5))) {`
- `sources/io/dcloud/e/b/e.java:946`
  `sbD03.append(BaseInfo.sDownloadFullPath);`
- `sources/io/dcloud/e/b/e.java:1064`
  `return BaseInfo.sDownloadFullPath;`
- `sources/io/dcloud/net/JsDownload.java:175`
  `this.mParentPath = new File(BaseInfo.sDownloadFullPath).getParent() + Operators.DIV;`
- `sources/io/dcloud/net/JsDownload.java:189`
  `this.mParentPath = new File(BaseInfo.sDownloadFullPath).getParent() + Operators.DIV;`
- `sources/io/dcloud/net/JsDownload.java:192`
  `this.mParentPath = new File(BaseInfo.sDownloadFullPath).getParent() + Operators.DIV;`
- `sources/io/dcloud/net/JsDownload.java:246`
  `sb.append(BaseInfo.sDownloadFullPath);`
- `sources/kotlin/jvm/internal/AdaptedFunctionReference.java:10`
  `public class AdaptedFunctionReference implements FunctionBase, Serializable {`
- `sources/kotlin/jvm/internal/AdaptedFunctionReference.java:19`
  `public AdaptedFunctionReference(int i2, Class cls, String str, String str2, int i3) {`
- `sources/kotlin/jvm/internal/AdaptedFunctionReference.java:27`
  `if (!(obj instanceof AdaptedFunctionReference)) {`
- `sources/kotlin/jvm/internal/AdaptedFunctionReference.java:30`
  `AdaptedFunctionReference adaptedFunctionReference = (AdaptedFunctionReference) obj;`
- `sources/kotlin/jvm/internal/AdaptedFunctionReference.java:31`
  `return this.isTopLevel == adaptedFunctionReference.isTopLevel && this.arity == adaptedFunctionReference.arity && this.flags == adaptedFunctionReference.flags && Intrinsics.a(this.receiver, adaptedFunctionReference.receiver) && Intrinsics.a(this.owner, adaptedFunctionReference.owner) && this.name.equ...`
- `sources/kotlin/jvm/internal/AdaptedFunctionReference.java:62`
  `public AdaptedFunctionReference(int i2, Object obj, Class cls, String str, String str2, int i3) {`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:150`
  `randomAccessFile2.readFully(rawIO.b);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:157`
  `randomAccessFile2.readFully(rawIO.b);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:159`
  `randomAccessFile2.readFully(rawIO.c);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:161`
  `randomAccessFile2.readFully(rawIO.b);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:181`
  `randomAccessFile2.readFully(rawIO2.b);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:188`
  `randomAccessFile2.readFully(rawIO2.c);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:190`
  `randomAccessFile2.readFully(rawIO2.a);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:192`
  `randomAccessFile2.readFully(rawIO2.a);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:194`
  `randomAccessFile2.readFully(rawIO2.b);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:196`
  `randomAccessFile2.readFully(rawIO2.b);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:234`
  `randomAccessFile2.readFully(rawIO3.b);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:244`
  `randomAccessFile2.readFully(rawIO3.a);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:246`
  `randomAccessFile2.readFully(rawIO3.a);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:249`
  `randomAccessFile2.readFully(bArr5);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:388`
  `randomAccessFile2.readFully(rawIO3.b);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:393`
  `randomAccessFile2.readFully(rawIO3.a);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:398`
  `randomAccessFile2.readFully(bArr10);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:419`
  `randomAccessFile.readFully(this.b.b);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:425`
  `randomAccessFile.readFully(this.b.b);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:434`
  `randomAccessFile.readFully(rawIO.a);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:436`
  `randomAccessFile.readFully(rawIO.a);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:438`
  `randomAccessFile.readFully(rawIO.a);`
- `sources/net/lingala/zip4j/headers/HeaderReader.java:440`
  `randomAccessFile.readFully(rawIO.a);`

## BR090

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `app_projects/README.md:33`
  `- 'findings.tsv': normalized rule hits with status and evidence`
- `database/README.md:18`
  `Evidence model:`
- `database/README.md:19`
  `- 'confirmed': direct evidence in the current app sample.`
- `database/README.md:20`
  `- 'supported_hypothesis': strong code or traffic evidence, but not fully proven at runtime.`
- `database/README.md:21`
  `- 'not_supported': the rule was checked and no evidence was found.`
- `database/README.md:25`
  `- Do not call a finding 'confirmed' from a single weak string hit.`
- `database/README.md:26`
  `- Prefer a combination of code artifact, runtime evidence, and sink evidence.`
- `database/prompts/per_app_audit_prompt.md:9`
  `Your job is not to produce a generic security checklist. Your job is to compare this specific app against the local database and produce a precise, evidence-based analysis with strict false-positive control.`
- `database/prompts/per_app_audit_prompt.md:29`
  `- directly observed in runtime evidence, or`
- `database/prompts/per_app_audit_prompt.md:43`
  `- 'confirmed'`
- `database/prompts/per_app_audit_prompt.md:47`
  `- Never mark a rule as 'confirmed' from one weak indicator alone.`
- `database/prompts/per_app_audit_prompt.md:58`
  `- If evidence is incomplete, downgrade to 'supported_hypothesis' or 'not_testable'.`
- `database/prompts/per_app_audit_prompt.md:61`
  `6. Evidence rules:`
- `database/prompts/per_app_audit_prompt.md:66`
  `- the concrete app evidence used`
- `database/prompts/per_app_audit_prompt.md:72`
  `- 'Method and Available Evidence'`
- `database/prompts/per_app_audit_prompt.md:73`
  `- 'Confirmed Findings'`
- `database/prompts/per_app_audit_prompt.md:95`
  `- 'the evidence supports'`
- `database/prompts/per_app_audit_prompt.md:99`
  `- If the evidence is not enough, say that directly.`
- `database/prompts/per_app_audit_prompt.md:109`
  `'Read the local database first, extract the subset of relevant rules for this app, map concrete app evidence to those rules, and produce a conservative report with explicit confidence labels and paper-based citations.'`
- `database/prompts/per_app_audit_prompt_zh.md:36`
  `- 'confirmed'`
- `database/prompts/per_app_audit_prompt_zh.md:40`
  `- 不允许因为单个弱证据就标记为 'confirmed'。`
- `database/prompts/per_app_audit_prompt_zh.md:71`
  `- 'Method and Available Evidence'`
- `database/prompts/per_app_audit_prompt_zh.md:72`
  `- 'Confirmed Findings'`
- `database_beginner/README.md:40`
  `## Evidence Policy`
- `database_beginner/README.md:43`
  `- Do not mark BLE findings as 'confirmed' unless there is runtime evidence.`
- `database_beginner/README.md:45`
  `- Static findings can be 'confirmed' only when the artifact itself is sufficient, such as exported components, cleartext config, hardcoded keys, permissive TrustManager, or policy omissions.`
- `database_beginner/README.md:46`
  `- Dynamic and cloud findings need runtime, storage, or traffic evidence unless clearly described as code-supported hypotheses.`
- `database_beginner/STRUCTURE.md:8`
  `- Short database overview: scope, categories, no-device assumptions, and evidence policy.`
- `database_beginner/prompts/per_app_beginner_audit_prompt_zh.md:42`
  `- 'ble_connection'：只做 BLE 代码层和设计层推断；没有真实设备时不能写 'confirmed'。`
- `database_beginner/prompts/per_app_beginner_audit_prompt_zh.md:72`
  `- 'B028'、'B029'：用于 BLE 连接代码层分析，例如 'BluetoothGatt'、'BluetoothLeScanner'、UUID、Characteristic、payload builder、App 层加密/鉴权、bonded/connected 状态信任。没有物理设备时不能写 'confirmed'。`
- `database_beginner/prompts/per_app_beginner_audit_prompt_zh.md:86`
  `- 'confirmed'`
- `database_beginner/prompts/per_app_beginner_audit_prompt_zh.md:92`
  `- 'confirmed'：证据闭环，至少有一个直接证据和一个上下文佐证。`
- `database_beginner/prompts/per_app_beginner_audit_prompt_zh.md:99`
  `以下单独出现时都不能作为 'confirmed'：`
- `database_beginner/prompts/per_app_beginner_audit_prompt_zh.md:139`
  `没有足够证据时，也要写明：当前样本无法形成 cross-layer confirmed finding。`
- `database_beginner/prompts/per_app_beginner_audit_prompt_zh.md:145`
  `- 'Available Evidence'`

## BR092

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/aegon/chrome/net/UrlRequest.java:28`
  `public abstract Builder setUploadDataProvider(UploadDataProvider uploadDataProvider, Executor executor);`
- `sources/aegon/chrome/net/impl/CronetBidirectionalStream.java:348`
  `this.mRequestContext.reportRequestFinished(new RequestFinishedInfoImpl(this.mInitialUrl, this.mRequestAnnotations, cronetMetrics, i2 == 7 ? 0 : i2 == 5 ? 2 : 1, this.mResponseInfo, this.mException));`
- `sources/aegon/chrome/net/impl/CronetBidirectionalStream.java:378`
  `synchronized (CronetBidirectionalStream.this.mNativeStreamLock) {`
- `sources/aegon/chrome/net/impl/CronetBidirectionalStream.java:404`
  `synchronized (CronetBidirectionalStream.this.mNativeStreamLock) {`
- `sources/aegon/chrome/net/impl/CronetBidirectionalStream.java:596`
  `synchronized (this.mNativeStreamLock) {`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:211`
  `public void maybeReportMetrics() {`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:215`
  `this.mRequestContext.reportRequestFinished(requestFinishedInfoImpl);`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:271`
  `CronetUrlRequest.this.maybeReportMetrics();`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:320`
  `CronetUrlRequest.this.maybeReportMetrics();`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:378`
  `synchronized (CronetUrlRequest.this.mUrlRequestAdapterLock) {`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:411`
  `synchronized (CronetUrlRequest.this.mUrlRequestAdapterLock) {`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:420`
  `CronetUrlRequest.this.maybeReportMetrics();`
- `sources/aegon/chrome/net/impl/CronetUrlRequest.java:535`
  `synchronized (this.mUrlRequestAdapterLock) {`
- `sources/aegon/chrome/net/impl/CronetUrlRequestContext.java:258`
  `synchronized (this.mNetworkQualityLock) {`
- `sources/aegon/chrome/net/impl/CronetUrlRequestContext.java:446`
  `synchronized (this.mNetworkQualityLock) {`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:6`
  `import aegon.chrome.net.UploadDataProvider;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:7`
  `import aegon.chrome.net.UploadDataSink;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:51`
  `private static final int DEFAULT_UPLOAD_BUFFER_SIZE = 8192;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:57`
  `private final AsyncUrlRequestCallback mCallbackAsync;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:67`
  `private VersionSafeCallbacks.UploadDataProviderWrapper mUploadDataProvider;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:68`
  `private Executor mUploadExecutor;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:74`
  `private final AtomicBoolean mUploadProviderClosed = new AtomicBoolean(false);`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:103`
  `this.mUserExecutor.execute(new Runnable() { // from class: aegon.chrome.net.impl.JavaUrlRequest.AsyncUrlRequestCallback.5`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:107`
  `AsyncUrlRequestCallback asyncUrlRequestCallback = AsyncUrlRequestCallback.this;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:108`
  `asyncUrlRequestCallback.mCallback.onCanceled(JavaUrlRequest.this, urlResponseInfo);`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:118`
  `Runnable runnable = new Runnable() { // from class: aegon.chrome.net.impl.JavaUrlRequest.AsyncUrlRequestCallback.7`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:122`
  `AsyncUrlRequestCallback asyncUrlRequestCallback = AsyncUrlRequestCallback.this;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:123`
  `asyncUrlRequestCallback.mCallback.onFailed(JavaUrlRequest.this, urlResponseInfo, cronetException);`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:140`
  `execute(new CheckedRunnable() { // from class: aegon.chrome.net.impl.JavaUrlRequest.AsyncUrlRequestCallback.4`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:144`
  `AsyncUrlRequestCallback asyncUrlRequestCallback = AsyncUrlRequestCallback.this;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:145`
  `asyncUrlRequestCallback.mCallback.onReadCompleted(JavaUrlRequest.this, urlResponseInfo, byteBuffer);`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:152`
  `execute(new CheckedRunnable() { // from class: aegon.chrome.net.impl.JavaUrlRequest.AsyncUrlRequestCallback.2`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:155`
  `AsyncUrlRequestCallback asyncUrlRequestCallback = AsyncUrlRequestCallback.this;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:156`
  `asyncUrlRequestCallback.mCallback.onRedirectReceived(JavaUrlRequest.this, urlResponseInfo, str);`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:162`
  `execute(new CheckedRunnable() { // from class: aegon.chrome.net.impl.JavaUrlRequest.AsyncUrlRequestCallback.3`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:166`
  `AsyncUrlRequestCallback asyncUrlRequestCallback = AsyncUrlRequestCallback.this;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:167`
  `VersionSafeCallbacks.UrlRequestCallback urlRequestCallback = asyncUrlRequestCallback.mCallback;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:176`
  `this.mUserExecutor.execute(new Runnable() { // from class: aegon.chrome.net.impl.JavaUrlRequest.AsyncUrlRequestCallback.6`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:180`
  `AsyncUrlRequestCallback asyncUrlRequestCallback = AsyncUrlRequestCallback.this;`
- `sources/aegon/chrome/net/impl/JavaUrlRequest.java:181`
  `asyncUrlRequestCallback.mCallback.onSucceeded(JavaUrlRequest.this, urlResponseInfo);`

## BR093

paper_id: B004
paper_title: Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation

- `sources/androidx/work/ForegroundUpdater.java:11`
  `ListenableFuture<Void> setForegroundAsync(@NonNull Context context, @NonNull UUID uuid, @NonNull ForegroundInfo foregroundInfo);`
- `sources/androidx/work/ListenableWorker.java:203`
  `settableFutureCreate.setException(new IllegalStateException("Expedited WorkRequests require a ListenableWorker to provide an implementation for 'getForegroundInfoAsync()'"));`
- `sources/androidx/work/impl/utils/WorkForegroundUpdater.java:38`
  `public ListenableFuture<Void> setForegroundAsync(@NonNull final Context context, @NonNull final UUID uuid, @NonNull final ForegroundInfo foregroundInfo) {`
- `sources/androidx/work/impl/utils/WorkForegroundUpdater.java:48`
  `throw new IllegalStateException("Calls to setForegroundAsync() must complete before a ListenableWorker signals completion of work by returning an instance of Result.");`
- `sources/cn/jiguang/ao/c.java:159`
  `cn.jiguang.m.b.h(context, "reportWake");`
- `sources/cn/jiguang/ao/c.java:162`
  `j.a.a.a.a.h(th, j.a.a.a.a.d0("reportWakeComponentsState failed, "), "JWakeLocalState");`
- `sources/cn/jiguang/ax/h.java:89`
  `str = "upload" + jSONObject.toString() + " failed";`
- `sources/cn/jiguang/bd/c.java:240`
  `cn.jiguang.ay.f.f("ConnectingHelper", "IMEI is duplicated reported by server. Give up now. ");`
- `sources/cn/jiguang/bk/c.java:72`
  `f.c("RegKeyInfo", "save reg key info: " + jSONObject);`
- `sources/cn/jiguang/bk/e.java:85`
  `f.c("UDIDUtils", "Action:getSavedUuid");`
- `sources/cn/jiguang/bk/e.java:103`
  `f.f("UDIDUtils", "Got sdcard file saved udid - " + strC);`
- `sources/cn/jiguang/bv/b.java:50`
  `cn.jiguang.ay.f.c("AuthUtils", "reportJSON=" + jSONObject);`
- `sources/cn/jiguang/bv/b.java:54`
  `j.a.a.a.a.Q0("sync status  throwable=", th, "AuthUtils");`
- `sources/cn/jiguang/o/d.java:34`
  `cn.jiguang.ay.f.c("JDeviceIdMap", "report: " + str);`
- `sources/cn/jiguang/o/d.java:36`
  `cn.jiguang.ay.f.c("JDeviceIdMap", "report device id map is not enabled");`
- `sources/cn/jiguang/o/d.java:43`
  `cn.jiguang.ay.f.i("JDeviceIdMap", "bootId and mediaDrmId is empty, skip reporting device id map");`
- `sources/cn/jiguang/o/d.java:49`
  `cn.jiguang.ay.f.c("JDeviceIdMap", "report deviceIdMapJson: " + jSONObject);`
- `sources/cn/jiguang/o/d.java:54`
  `cn.jiguang.ay.f.i("JDeviceIdMap", "report device id map failed: " + e.getMessage());`
- `sources/cn/jiguang/o/e.java:74`
  `cn.jiguang.ay.f.c("JDeviceIds", "ids not changed, need not report");`
- `sources/cn/jiguang/o/e.java:106`
  `cn.jiguang.ay.f.i("JDeviceIds", "there are no data to report");`
- `sources/cn/jiguang/o/e.java:112`
  `StringBuilder sbI0 = j.a.a.a.a.i0(str, "report success, reportData: ");`
- `sources/cn/jiguang/o/g.java:71`
  `cn.jiguang.ay.f.c("JDeviceMac", "it need not report, because wifi info is null");`
- `sources/cn/jiguang/o/g.java:123`
  `StringBuilder sbD0 = j.a.a.a.a.d0("it need not report, because no wifi info or mac, mac: ");`
- `sources/cn/jiguang/o/g.java:142`
  `j.a.a.a.a.h(th, j.a.a.a.a.d0("ssid mac report failed, "), "JDeviceMac");`
- `sources/com/efs/sdk/base/core/c/d.java:127`
  `if (WorkThreadUtil.submit(new e(bVar2, cVar, string)) == null) {`
- `sources/com/efs/sdk/base/core/util/d.java:63`
  `Log.e("efs.base", "save uuid '" + string + "' error", e);`
- `sources/com/efs/sdk/memoryinfo/d.java:141`
  `handler.post(new Runnable() { // from class: com.efs.sdk.memoryinfo.b.2`
- `sources/com/efs/sdk/memoryinfo/d.java:248`
  `handler2.post(new Runnable() { // from class: com.efs.sdk.memoryinfo.b.2`
- `sources/com/google/android/material/internal/CollapsingTextHelper.java:214`
  `ViewCompat.postInvalidateOnAnimation(this.a);`
- `sources/com/google/android/material/internal/CollapsingTextHelper.java:216`
  `ViewCompat.postInvalidateOnAnimation(this.a);`
- `sources/com/google/firebase/installations/Utils.java:44`
  `public long getRandomDelayForSyncPrevention() {`
- `sources/com/huawei/hms/aaid/HmsInstanceIdEx.java:76`
  `this.b.saveString(str, string);`
- `sources/com/huawei/hms/aaid/HmsInstanceIdEx.java:77`
  `this.b.saveLong(a(str), Long.valueOf(System.currentTimeMillis()));`
- `sources/com/huawei/hms/hatool/b.java:47`
  `v.c("hmsSdk", "Builder.setEnableImei(boolean isReportAndroidImei) is execute.");`
- `sources/com/huawei/hms/opendevice/n.java:21`
  `/* JADX INFO: compiled from: ReportAaidToken.java */`
- `sources/com/huawei/hms/opendevice/o.java:40`
  `pushPreferences.saveString("aaid", string);`
- `sources/com/huawei/hms/opendevice/o.java:41`
  `pushPreferences.saveLong("creationTime", Long.valueOf(System.currentTimeMillis()));`
- `sources/com/huawei/hms/support/api/entity/hwid/ShippingAddressInfo.java:40`
  `private String postalCode;`
- `sources/com/hybirdlib/hybirdlib/SdkPluginUtils.java:604`
  `if ("syncHistory".equals(strOptString)) {`
- `sources/com/hybirdlib/hybirdlib/SdkPluginUtils.java:606`
  `babyBLEOperation.syncHistory(jSONObjectOptJSONObject.optString("xsId"), jSONObjectOptJSONObject.optInt("userId"), new ICallback<XsBaseData<XsBabyHistoryTestInfo>>(this) { // from class: com.hybirdlib.hybirdlib.SdkPluginUtils.22`

## BR094

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `sources/aegon/chrome/base/AnimationFrameTimeHistogram.java:15`
  `void saveHistogram(String str, long[] jArr, int i2);`
- `sources/aegon/chrome/base/AnimationFrameTimeHistogramJni.java:21`
  `public final void saveHistogram(String str, long[] jArr, int i2) {`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:59`
  `public static final class AsyncEvent {`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:65`
  `public AsyncEvent(String str, long j2, boolean z) {`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:121`
  `private static void dumpAsyncEvents(List<AsyncEvent> list) {`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:123`
  `for (AsyncEvent asyncEvent : list) {`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:124`
  `if (asyncEvent.mIsStart) {`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:125`
  `nativeRecordEarlyStartAsyncEvent(asyncEvent.mName, asyncEvent.mId, asyncEvent.mTimestampNanos + offsetNanos);`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:127`
  `nativeRecordEarlyFinishAsyncEvent(asyncEvent.mName, asyncEvent.mId, asyncEvent.mTimestampNanos + offsetNanos);`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:175`
  `public static void finishAsync(String str, long j2) {`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:177`
  `AsyncEvent asyncEvent = new AsyncEvent(str, j2, false);`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:178`
  `synchronized (sLock) {`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:180`
  `if (sPendingAsyncEvents.remove(str)) {`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:261`
  `sPendingAsyncEvents = null;`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:262`
  `sAsyncEvents = null;`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:268`
  `private static native void nativeRecordEarlyFinishAsyncEvent(String str, long j2, long j3);`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:270`
  `private static native void nativeRecordEarlyStartAsyncEvent(String str, long j2, long j3);`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:274`
  `synchronized (sLock) {`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:288`
  `public static void startAsync(String str, long j2) {`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:290`
  `AsyncEvent asyncEvent = new AsyncEvent(str, j2, true);`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:291`
  `synchronized (sLock) {`
- `sources/aegon/chrome/base/EarlyTraceEvent.java:293`
  `sAsyncEvents.add(asyncEvent);`
- `sources/aegon/chrome/base/JavaHandlerThread.java:72`
  `new Handler(this.mThread.getLooper()).post(new Runnable() { // from class: aegon.chrome.base.JavaHandlerThread.2`
- `sources/aegon/chrome/base/JavaHandlerThread.java:85`
  `new Handler(this.mThread.getLooper()).post(new Runnable() { // from class: aegon.chrome.base.JavaHandlerThread.1`
- `sources/aegon/chrome/base/NonThreadSafe.java:17`
  `public synchronized boolean calledOnValidThread() {`
- `sources/aegon/chrome/base/NonThreadSafe.java:23`
  `public synchronized void detachFromThread() {`
- `sources/aegon/chrome/base/ThreadUtils.java:66`
  `public static void postOnUiThreadDelayed(Runnable runnable, long j2) {`
- `sources/aegon/chrome/base/ThreadUtils.java:67`
  `getUiThreadHandler().postDelayed(runnable, j2);`
- `sources/aegon/chrome/base/TraceEvent.java:141`
  `syncIdleMonitoring();`
- `sources/aegon/chrome/base/TraceEvent.java:192`
  `public static void finishAsync(String str, long j2) {`
- `sources/aegon/chrome/base/TraceEvent.java:193`
  `EarlyTraceEvent.finishAsync(str, j2);`
- `sources/aegon/chrome/base/TraceEvent.java:195`
  `nativeFinishAsync(str, j2);`
- `sources/aegon/chrome/base/TraceEvent.java:222`
  `private static native void nativeFinishAsync(String str, long j2);`
- `sources/aegon/chrome/base/TraceEvent.java:230`
  `private static native void nativeStartAsync(String str, long j2);`
- `sources/aegon/chrome/base/TraceEvent.java:271`
  `public static void startAsync(String str, long j2) {`
- `sources/aegon/chrome/base/TraceEvent.java:272`
  `EarlyTraceEvent.startAsync(str, j2);`
- `sources/aegon/chrome/base/TraceEvent.java:274`
  `nativeStartAsync(str, j2);`
- `sources/aegon/chrome/base/metrics/RecordHistogram.java:15`
  `private static Map<String, Long> sCache = Collections.synchronizedMap(new HashMap());`
- `sources/aegon/chrome/base/task/AsyncTask.java:27`
  `public static final Executor THREAD_POOL_EXECUTOR = AsyncTask$$Lambda$2.instance;`
- `sources/aegon/chrome/base/task/AsyncTask.java:42`
  `AsyncTask.this.postResultIfNotInvoked(get());`

## BR095

paper_id: B025
paper_title: Why Eve and Mallory Still Love Android: Revisiting TLS (In)Security in Android Applications

- `database/snapshots/P001-usenix-android-application-security.html:304`
  `<param name="movie" value="http://releases.flowplayer.org/swf/flowplayer-3.2.1.swf">`
- `database/snapshots/P002-usenix-supor.html:7`
  `<html  lang="en" dir="ltr" prefix="og: http://ogp.me/ns#" class="no-js">`
- `database/snapshots/P002-usenix-supor.html:304`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.nsf.gov" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/nsf_150x60_v2.png" width="150" height="60" alt="" /></a><...`
- `database/snapshots/P002-usenix-supor.html:310`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.symantec.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/symantec_logo_1.png" width="200" height="54" alt="" ...`
- `database/snapshots/P002-usenix-supor.html:322`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://cybersecurity.ieee.org" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/ieee_cybersecurity_150x73.png" width="150" hei...`
- `database/snapshots/P002-usenix-supor.html:328`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.microsoft.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/microsoft_150x60_0.png" width="150" height="60" alt...`
- `database/snapshots/P002-usenix-supor.html:334`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.qualcomm.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/qualcomm_150x22.png" width="150" height="33" alt="" ...`
- `database/snapshots/P002-usenix-supor.html:340`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://sfbay.craigslist.org/about/craigslist_is_hiring" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/craigslist_150x35_1.p...`
- `database/snapshots/P002-usenix-supor.html:346`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.oup.com/us" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/oxford_university_press_150x55.png" width="150" height...`
- `database/snapshots/P002-usenix-supor.html:352`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.infosecnews.org" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/infosecnews_150x38.png" width="150" height="38" a...`
- `database/snapshots/P002-usenix-supor.html:358`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://tci.taborcommunications.com/HPCwireLogo_Usenix" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/hpcwire_150x55_0.png" ...`
- `database/snapshots/P002-usenix-supor.html:364`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.userfriendly.org" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/userfriendly_150x60.png" width="150" height="60"...`
- `database/snapshots/P002-usenix-supor.html:370`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.nostarch.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/nostarch_600x240_0.png" width="200" height="80" alt=...`
- `database/snapshots/P002-usenix-supor.html:376`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.linuxpromagazine.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/linux_pro_150x60.png" width="150" height="60...`
- `database/snapshots/P002-usenix-supor.html:382`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.linuxjournal.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/linux_journal_150x72_2.png" width="150" height="...`
- `database/snapshots/P002-usenix-supor.html:388`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.virusbulletin.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/virus_bulletin_150x60.png" width="150" height="...`
- `database/snapshots/P002-usenix-supor.html:394`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.crcpress.com/" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/crc_press_150x60.png" width="150" height="60" alt="...`
- `database/snapshots/P002-usenix-supor.html:400`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://queue.acm.org" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/acmqueue_150x48_3.png" width="150" height="48" alt="" /...`
- `database/snapshots/P002-usenix-supor.html:406`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.admin-magazine.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/admin_150x60.png" width="150" height="60" alt=...`
- `database/snapshots/P002-usenix-supor.html:412`
  `<div class="views-field views-field-field-sponsor-image">        <div class="field-content"><a href="http://www.dmtf.org" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_slideshow_front/public/sponsor_images/dmtf_600x240.png" width="200" height="80" alt="" /></a><...`
- `database/snapshots/P002-usenix-supor.html:663`
  `<a href="http://www.nsf.gov" target="_blank"></a>`
- `database/snapshots/P002-usenix-supor.html:664`
  `<a href="http://www.nsf.gov" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_interest_color/public/sponsor_images/nsf_150x60_v2.png" width="115" height="46" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:667`
  `<a href="http://www.symantec.com" target="_blank"></a>`
- `database/snapshots/P002-usenix-supor.html:668`
  `<a href="http://www.symantec.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_interest_color/public/sponsor_images/symantec_logo_1.png" width="115" height="31" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:705`
  `<a href="http://cybersecurity.ieee.org" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_interest_color/public/sponsor_images/ieee_cybersecurity_150x73.png" width="115" height="56" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:708`
  `<a href="http://www.microsoft.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_interest_color/public/sponsor_images/microsoft_150x60_0.png" width="115" height="46" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:742`
  `<a href="http://sfbay.craigslist.org/about/craigslist_is_hiring" target="_blank"></a>`
- `database/snapshots/P002-usenix-supor.html:743`
  `<a href="http://sfbay.craigslist.org/about/craigslist_is_hiring" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_interest_color/public/sponsor_images/craigslist_150x35_1.png" width="115" height="27" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:746`
  `<a href="http://www.qualcomm.com" target="_blank"></a>`
- `database/snapshots/P002-usenix-supor.html:747`
  `<a href="http://www.qualcomm.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_interest_color/public/sponsor_images/qualcomm_150x22.png" width="115" height="25" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:781`
  `<a href="http://www.oup.com/us" target="_blank"></a>`
- `database/snapshots/P002-usenix-supor.html:782`
  `<a href="http://www.oup.com/us" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_interest_color/public/sponsor_images/oxford_university_press_150x55.png" width="115" height="42" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:816`
  `<a href="http://queue.acm.org"></a>`
- `database/snapshots/P002-usenix-supor.html:817`
  `<a href="http://queue.acm.org" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_front_color/public/sponsor_images/acmqueue_150x48_3.png" width="90" height="29" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:820`
  `<a href="http://www.admin-magazine.com"></a>`
- `database/snapshots/P002-usenix-supor.html:821`
  `<a href="http://www.admin-magazine.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_front_color/public/sponsor_images/admin_150x60.png" width="90" height="36" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:824`
  `<a href="http://www.crcpress.com/"></a>`
- `database/snapshots/P002-usenix-supor.html:825`
  `<a href="http://www.crcpress.com/" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_front_color/public/sponsor_images/crc_press_150x60.png" width="90" height="36" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:828`
  `<a href="http://www.dmtf.org"></a>`
- `database/snapshots/P002-usenix-supor.html:829`
  `<a href="http://www.dmtf.org" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_front_color/public/sponsor_images/dmtf_600x240.png" width="90" height="36" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:836`
  `<a href="http://tci.taborcommunications.com/HPCwireLogo_Usenix"></a>`
- `database/snapshots/P002-usenix-supor.html:837`
  `<a href="http://tci.taborcommunications.com/HPCwireLogo_Usenix" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_front_color/public/sponsor_images/hpcwire_150x55_0.png" width="90" height="33" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:840`
  `<a href="http://www.infosecnews.org"></a>`
- `database/snapshots/P002-usenix-supor.html:841`
  `<a href="http://www.infosecnews.org" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_front_color/public/sponsor_images/infosecnews_150x38.png" width="90" height="23" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:844`
  `<a href="http://www.linuxjournal.com"></a>`
- `database/snapshots/P002-usenix-supor.html:845`
  `<a href="http://www.linuxjournal.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_front_color/public/sponsor_images/linux_journal_150x72_2.png" width="90" height="43" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:848`
  `<a href="http://www.linuxpromagazine.com"></a>`
- `database/snapshots/P002-usenix-supor.html:849`
  `<a href="http://www.linuxpromagazine.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_front_color/public/sponsor_images/linux_pro_150x60.png" width="90" height="36" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:852`
  `<a href="http://www.nostarch.com"></a>`
- `database/snapshots/P002-usenix-supor.html:853`
  `<a href="http://www.nostarch.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_front_color/public/sponsor_images/nostarch_600x240_0.png" width="90" height="36" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:856`
  `<a href="http://www.userfriendly.org"></a>`
- `database/snapshots/P002-usenix-supor.html:857`
  `<a href="http://www.userfriendly.org" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_front_color/public/sponsor_images/userfriendly_150x60.png" width="90" height="36" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:860`
  `<a href="http://www.virusbulletin.com"></a>`
- `database/snapshots/P002-usenix-supor.html:861`
  `<a href="http://www.virusbulletin.com" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_front_color/public/sponsor_images/virus_bulletin_150x60.png" width="90" height="36" alt="" /></a>    </div>`
- `database/snapshots/P002-usenix-supor.html:895`
  `<a href="http://peerj.com/"></a>`
- `database/snapshots/P002-usenix-supor.html:896`
  `<a href="http://peerj.com/" target="_blank"><img src="https://www.usenix.org/sites/default/files/styles/sponsor_front_color/public/sponsor_images/peerj_600x240.png" width="90" height="36" alt="" /></a>    </div>`
- `database/snapshots/P003-ndss-content-leaks.html:324`
  `<div class="wp-block-group search-dropdown is-layout-flow wp-block-group-is-layout-flow"><div class="wp-block-group__inner-container"><p><form data-min-no-for-search=1 data-result-box-max-height=400 data-form-id=9240 class="is-search-form is-disable-submit is-form-style is-form-style-3 is-form-id-92...`
- `database/snapshots/P003-ndss-content-leaks.html:360`
  `<p><strong>Associated Event: </strong><a href="http://www.ndss-symposium.org/ndss2013">NDSS Symposium 2013</a></p>`
- `database/snapshots/P003-ndss-content-leaks.html:465`
  `.wp-block-image>a,.wp-block-image>figure>a{display:inline-block}.wp-block-image img{box-sizing:border-box;height:auto;max-width:100%;vertical-align:bottom}@media not (prefers-reduced-motion){.wp-block-image img.hide{visibility:hidden}.wp-block-image img.show{animation:show-content-image .4s}}.wp-blo...`
- `database/snapshots/P004-ndss-execute-this.html:316`
  `<div class="wp-block-group search-dropdown is-layout-flow wp-block-group-is-layout-flow"><div class="wp-block-group__inner-container"><p><form data-min-no-for-search=1 data-result-box-max-height=400 data-form-id=9240 class="is-search-form is-disable-submit is-form-style is-form-style-3 is-form-id-92...`
- `database/snapshots/P004-ndss-execute-this.html:336`
  `<p class="ndss_associated"><strong>Associated Event: </strong><a href="http://www.ndss-symposium.org/ndss2014">NDSS Symposium 2014</a></p>`
- `database/snapshots/P004-ndss-execute-this.html:435`
  `.wp-block-image>a,.wp-block-image>figure>a{display:inline-block}.wp-block-image img{box-sizing:border-box;height:auto;max-width:100%;vertical-align:bottom}@media not (prefers-reduced-motion){.wp-block-image img.hide{visibility:hidden}.wp-block-image img.show{animation:show-content-image .4s}}.wp-blo...`
- `database/snapshots/P005-ndss-appsealer.html:316`
  `<div class="wp-block-group search-dropdown is-layout-flow wp-block-group-is-layout-flow"><div class="wp-block-group__inner-container"><p><form data-min-no-for-search=1 data-result-box-max-height=400 data-form-id=9240 class="is-search-form is-disable-submit is-form-style is-form-style-3 is-form-id-92...`
- `database/snapshots/P005-ndss-appsealer.html:336`
  `<p class="ndss_associated"><strong>Associated Event: </strong><a href="http://www.ndss-symposium.org/ndss2014">NDSS Symposium 2014</a></p>`
- `database/snapshots/P005-ndss-appsealer.html:435`
  `.wp-block-image>a,.wp-block-image>figure>a{display:inline-block}.wp-block-image img{box-sizing:border-box;height:auto;max-width:100%;vertical-align:bottom}@media not (prefers-reduced-motion){.wp-block-image img.hide{visibility:hidden}.wp-block-image img.show{animation:show-content-image .4s}}.wp-blo...`
- `database/snapshots/P006-teamusec-android-ssl.html:163`
  `<a class="text-link " href="https://teamusec.de/"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-house-fill" viewBox="0 0 16 16">`
- `database/snapshots/P006-teamusec-android-ssl.html:229`
  `<a class="text-link " href="https://teamusec.de/"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-house-fill" viewBox="0 0 16 16">`
- `database/snapshots/P006-teamusec-android-ssl.html:312`
  `<span><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-file-earmark-fill" viewBox="0 0 16 16">`
- `database/snapshots/P006-teamusec-android-ssl.html:322`
  `<span><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-file-text" viewBox="0 0 16 16">`
- `database/snapshots/P006-teamusec-android-ssl.html:334`
  `<span><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-tag-fill" viewBox="0 0 16 16">`
- `database/snapshots/P006-teamusec-android-ssl.html:343`
  `<span><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-box-arrow-up-right" viewBox="0 0 16 16">`
- `database/snapshots/P006-teamusec-android-ssl.html:383`
  `<span class="default"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-clipboard" viewBox="0 0 16 16">`
- `database/snapshots/P006-teamusec-android-ssl.html:388`
  `<span class="success" style="display:none;"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-clipboard-check" viewBox="0 0 16 16">`
- `database/snapshots/P006-teamusec-android-ssl.html:394`
  `<span class="failure" style="display:none;"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-clipboard" viewBox="0 0 16 16">`
- `database/snapshots/P007-usenix-deep-links.html:2`
  `<!--[if IE 8]><html class="no-js lt-ie9"  lang="en" dir="ltr" prefix="og: http://ogp.me/ns#"> <![endif]-->`
- `database/snapshots/P007-usenix-deep-links.html:3`
  `<!--[if gt IE 8]><!--> <html class="no-js"  lang="en" dir="ltr" prefix="og: http://ogp.me/ns#"> <!--<![endif]-->`
- `database/snapshots/P008-usenix-webview-dcv.html:2`
  `<!--[if IE 8]><html class="no-js lt-ie9"  lang="en" dir="ltr" prefix="og: http://ogp.me/ns#"> <![endif]-->`
- `database/snapshots/P008-usenix-webview-dcv.html:3`
  `<!--[if gt IE 8]><!--> <html class="no-js"  lang="en" dir="ltr" prefix="og: http://ogp.me/ns#"> <!--<![endif]-->`
- `database/snapshots/P009-ndss-webview-tracking.html:315`
  `<div class="wp-block-group search-dropdown is-layout-flow wp-block-group-is-layout-flow"><div class="wp-block-group__inner-container"><p><form data-min-no-for-search=1 data-result-box-max-height=400 data-form-id=9240 class="is-search-form is-disable-submit is-form-style is-form-style-3 is-form-id-92...`
- `database/snapshots/P009-ndss-webview-tracking.html:528`
  `.wp-block-image>a,.wp-block-image>figure>a{display:inline-block}.wp-block-image img{box-sizing:border-box;height:auto;max-width:100%;vertical-align:bottom}@media not (prefers-reduced-motion){.wp-block-image img.hide{visibility:hidden}.wp-block-image img.show{animation:show-content-image .4s}}.wp-blo...`

## BR096

paper_id: B011
paper_title: Locking it down: The privacy and security of mobile medication apps

- `database/snapshots/P001-usenix-android-application-security.html:300`
  `<video width="640" height="480"  poster="https://www.usenix.org/sites/default/files/styles/video-thumbnail/public/conference/video/enck.jpg" class="video-js vjs-default-skin vjs-big-play-centered" preload="auto" controls>`
- `database/snapshots/P001-usenix-android-application-security.html:301`
  `<source src='https://c59951.ssl.cf2.rackcdn.com/sec11/enck.mp4' type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>`
- `database/snapshots/P001-usenix-android-application-security.html:302`
  `<source src='https://c59951.ssl.cf2.rackcdn.com/sec11/enck.webm' type='video/webm; codecs="vp8.0, vorbis"'>`
- `database/snapshots/P001-usenix-android-application-security.html:303`
  `<object type="application/x-shockwave-flash" data="https://releases.flowplayer.org/swf/flowplayer-3.2.1.swf" width="640" height="480">`
- `database/snapshots/P001-usenix-android-application-security.html:384`
  `<noscript aria-hidden="true"><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WQSPGJT"`
- `database/snapshots/P001-usenix-android-application-security.html:385`
  `height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>      <script defer src="https://static.cloudflareinsights.com/beacon.min.js/v8c78df7c7c0f484497ecbca7046644da1771523124516" integrity="sha512-8DS7rgIrAmghBFwoOTujcf6D9rXvH8xm8JQ1Ja01h9QX8EzXldiszufYa4IFfKdLUKTTrnSFXLDkU...`
- `database/snapshots/P002-usenix-supor.html:12`
  `<link rel="shortcut icon" href="https://www.usenix.org/themes/motherboard/favicon.ico" type="image/vnd.microsoft.icon" />`
- `database/snapshots/P002-usenix-supor.html:57`
  `@import url("https://www.usenix.org/core/misc/normalize.css?td9vs1");`
- `database/snapshots/P002-usenix-supor.html:58`
  `@import url("https://www.usenix.org/core/modules/system/css/system.theme.css?td9vs1");`
- `database/snapshots/P002-usenix-supor.html:109`
  `@import url("https://www.usenix.org/themes/tao/drupal.css?td9vs1");`
- `database/snapshots/P002-usenix-supor.html:113`
  `<script defer="defer" src="https://www.usenix.org/sites/default/files/google_tag/google_tag.script.js?td9vs1"></script>`
- `database/snapshots/P002-usenix-supor.html:114`
  `<script src="https://www.usenix.org/modules/contrib/jquery_update/replace/jquery/1.12/jquery.min.js?td9vs1"></script>`
- `database/snapshots/P002-usenix-supor.html:115`
  `<script src="https://www.usenix.org/core/misc/jquery.once.js?v=1.2.6"></script>`
- `database/snapshots/P002-usenix-supor.html:207`
  `<li class="menu-27916 menu-path-susenixorg-conference-usenixsecurity15-activitieswips  odd last"><a href="https://www.usenix.org/conference/usenixsecurity15/activities#wips" title="">WiPs</a></li>`
- `database/snapshots/P002-usenix-supor.html:956`
  `<noscript aria-hidden="true"><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WQSPGJT"`
- `database/snapshots/P002-usenix-supor.html:957`
  `height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>      <script defer src="https://static.cloudflareinsights.com/beacon.min.js/v8c78df7c7c0f484497ecbca7046644da1771523124516" integrity="sha512-8DS7rgIrAmghBFwoOTujcf6D9rXvH8xm8JQ1Ja01h9QX8EzXldiszufYa4IFfKdLUKTTrnSFXLDkU...`
- `database/snapshots/P003-ndss-content-leaks.html:7`
  `<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.1/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">`
- `database/snapshots/P003-ndss-content-leaks.html:8`
  `<link rel="preconnect" href="https://fonts.googleapis.com">`
- `database/snapshots/P003-ndss-content-leaks.html:9`
  `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>`
- `database/snapshots/P003-ndss-content-leaks.html:10`
  `<link href="https://fonts.googleapis.com/css2?family=Hind:wght@300;400;500;600;700&family=Roboto+Slab:wght@100..900&display=swap" rel="stylesheet">`
- `database/snapshots/P003-ndss-content-leaks.html:13`
  `<!-- This site is optimized with the Yoast SEO plugin v27.1.1 - https://yoast.com/product/yoast-seo-wordpress/ -->`
- `database/snapshots/P003-ndss-content-leaks.html:22`
  `<meta property="article:publisher" content="https://www.facebook.com/NDSSSymposium/" />`
- `database/snapshots/P003-ndss-content-leaks.html:24`
  `<meta property="og:image" content="https://www.ndss-symposium.org/wp-content/uploads/NDSS_Logo_RGB.jpg" />`
- `database/snapshots/P003-ndss-content-leaks.html:30`
  `<script type="application/ld+json" class="yoast-schema-graph">{"@context":"https://schema.org","@graph":[{"@type":"WebPage","@id":"https://www.ndss-symposium.org/ndss2013/ndss-2013-programme/detecting-passive-content-leaks-and-pollution-android-applications/","url":"https://www.ndss-symposium.org/nd...`
- `database/snapshots/P003-ndss-content-leaks.html:35`
  `<link rel="alternate" title="oEmbed (JSON)" type="application/json+oembed" href="https://www.ndss-symposium.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.ndss-symposium.org%2Fndss2013%2Fndss-2013-programme%2Fdetecting-passive-content-leaks-and-pollution-android-applications%2F" />`
- `database/snapshots/P003-ndss-content-leaks.html:36`
  `<link rel="alternate" title="oEmbed (XML)" type="text/xml+oembed" href="https://www.ndss-symposium.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.ndss-symposium.org%2Fndss2013%2Fndss-2013-programme%2Fdetecting-passive-content-leaks-and-pollution-android-applications%2F&#038;format=xml" />`
- `database/snapshots/P003-ndss-content-leaks.html:41`
  `<link rel='stylesheet' id='pt-cv-public-style-css' href='https://www.ndss-symposium.org/wp-content/plugins/content-views-query-and-display-post-page/public/assets/css/cv.css?ver=4.3' type='text/css' media='all' />`
- `database/snapshots/P003-ndss-content-leaks.html:42`
  `<link rel='stylesheet' id='pt-cv-public-pro-style-css' href='https://www.ndss-symposium.org/wp-content/plugins/pt-content-views-pro/public/assets/css/cvpro.min.css?ver=7.3' type='text/css' media='all' />`
- `database/snapshots/P003-ndss-content-leaks.html:43`
  `<link rel='stylesheet' id='jquery.prettyphoto-css' href='https://www.ndss-symposium.org/wp-content/plugins/wp-video-lightbox/css/prettyPhoto.css?ver=6.9.4' type='text/css' media='all' />`
- `database/snapshots/P003-ndss-content-leaks.html:44`
  `<link rel='stylesheet' id='video-lightbox-css' href='https://www.ndss-symposium.org/wp-content/plugins/wp-video-lightbox/wp-video-lightbox.css?ver=6.9.4' type='text/css' media='all' />`
- `database/snapshots/P003-ndss-content-leaks.html:45`
  `<link rel='stylesheet' id='wp-block-library-css' href='https://www.ndss-symposium.org/wp-includes/css/dist/block-library/style.min.css?ver=6.9.4' type='text/css' media='all' />`
- `database/snapshots/P003-ndss-content-leaks.html:46`
  `<link rel='stylesheet' id='ivory-search-styles-css' href='https://www.ndss-symposium.org/wp-content/plugins/add-search-to-menu/public/css/ivory-search.min.css?ver=5.5.14' type='text/css' media='all' />`
- `database/snapshots/P003-ndss-content-leaks.html:47`
  `<link rel='stylesheet' id='sage/main.css-css' href='https://www.ndss-symposium.org/wp-content/themes/ndss2/dist/styles/main_e8b4062a.css' type='text/css' media='all' />`
- `database/snapshots/P003-ndss-content-leaks.html:48`
  `<link rel='stylesheet' id='google-fonts-css' href='https://fonts.googleapis.com/css?family=Yantramanav&#038;ver=6.9.4' type='text/css' media='all' />`
- `database/snapshots/P003-ndss-content-leaks.html:51`
  `/*# sourceURL=https://www.ndss-symposium.org/wp-includes/blocks/paragraph/style.min.css */`
- `database/snapshots/P003-ndss-content-leaks.html:66`
  `<script type="text/javascript" src="https://www.ndss-symposium.org/wp-content/plugins/wp-video-lightbox/js/video-lightbox.js?ver=3.1.6" id="video-lightbox-js"></script>`
- `database/snapshots/P003-ndss-content-leaks.html:67`
  `<link rel="https://api.w.org/" href="https://www.ndss-symposium.org/wp-json/" /><link rel="alternate" title="JSON" type="application/json" href="https://www.ndss-symposium.org/wp-json/wp/v2/pages/2145" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://www.ndss-symposium.org/...`
- `database/snapshots/P003-ndss-content-leaks.html:69`
  `<link rel='shortlink' href='https://www.ndss-symposium.org/?p=2145' />`
- `database/snapshots/P003-ndss-content-leaks.html:91`
  `</script><script async src="https://www.googletagmanager.com/gtag/js?id=G-VM78LT63H3"></script>`
- `database/snapshots/P003-ndss-content-leaks.html:196`
  `}</style><link rel="icon" href="https://www.ndss-symposium.org/wp-content/uploads/cropped-NDSS_512x512-32x32.png" sizes="32x32" />`
- `database/snapshots/P003-ndss-content-leaks.html:197`
  `<link rel="icon" href="https://www.ndss-symposium.org/wp-content/uploads/cropped-NDSS_512x512-192x192.png" sizes="192x192" />`
- `database/snapshots/P003-ndss-content-leaks.html:198`
  `<link rel="apple-touch-icon" href="https://www.ndss-symposium.org/wp-content/uploads/cropped-NDSS_512x512-180x180.png" />`
- `database/snapshots/P003-ndss-content-leaks.html:199`
  `<meta name="msapplication-TileImage" content="https://www.ndss-symposium.org/wp-content/uploads/cropped-NDSS_512x512-270x270.png" />`
- `database/snapshots/P003-ndss-content-leaks.html:285`
  `<li class="nav-item dropdown"><a href="https://www.ndss-symposium.org/ndss2026/" class="nav-link toggle"><span>2026 Symposium</span></a>`
- `database/snapshots/P003-ndss-content-leaks.html:287`
  `<li class="dropdown-item"><a href="https://www.ndss-symposium.org/ndss2026/accepted-papers/" class="nav-link toggle"><span>Accepted Papers</span></a></li>`
- `database/snapshots/P003-ndss-content-leaks.html:288`
  `<li class="dropdown-item"><a href="https://www.ndss-symposium.org/ndss2026/accepted-posters/" class="nav-link toggle"><span>Accepted Posters</span></a></li>`
- `database/snapshots/P003-ndss-content-leaks.html:289`
  `<li class="dropdown-item"><a href="https://www.ndss-symposium.org/ndss2026/program/" class="nav-link toggle"><span>Program</span></a></li>`
- `database/snapshots/P003-ndss-content-leaks.html:290`
  `<li class="dropdown-item"><a href="https://www.ndss-symposium.org/ndss2026/co-located-events/" class="nav-link toggle"><span>Co-located Events</span></a></li>`
- `database/snapshots/P003-ndss-content-leaks.html:291`
  `<li class="dropdown-item"><a href="https://www.ndss-symposium.org/ndss2026/leadership/" class="nav-link toggle"><span>Leadership</span></a></li>`
- `database/snapshots/P003-ndss-content-leaks.html:311`
  `<figure class="wp-block-image size-full search-toggle"><a href="#"><img loading="lazy" decoding="async" width="21" height="21" src="https://www.ndss-symposium.org/wp-content/uploads/search-bar-21px-21px.svg" alt="Search Icon" class="wp-image-9241"></a></figure>`
- `database/snapshots/P003-ndss-content-leaks.html:324`
  `<div class="wp-block-group search-dropdown is-layout-flow wp-block-group-is-layout-flow"><div class="wp-block-group__inner-container"><p><form data-min-no-for-search=1 data-result-box-max-height=400 data-form-id=9240 class="is-search-form is-disable-submit is-form-style is-form-style-3 is-form-id-92...`
- `database/snapshots/P003-ndss-content-leaks.html:382`
  `<li id="menu-item-11369" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-11369"><a href="https://www.ndss-symposium.org/ndss-test-of-time-award/">Test of Time Award</a></li>`
- `database/snapshots/P003-ndss-content-leaks.html:383`
  `<li id="menu-item-10055" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-10055"><a href="https://www.ndss-symposium.org/why-ndss/">Why NDSS Symposium</a></li>`
- `database/snapshots/P003-ndss-content-leaks.html:384`
  `<li id="menu-item-11886" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-11886"><a href="https://www.ndss-symposium.org/sponsorship/">Sponsorship</a></li>`
- `database/snapshots/P003-ndss-content-leaks.html:385`
  `<li id="menu-item-16445" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-16445"><a href="https://www.ndss-symposium.org/news/">News</a></li>`
- `database/snapshots/P003-ndss-content-leaks.html:388`
  `<section class="widget nav_menu-3 widget_nav_menu"><h3>NDSS Symposium 2023</h3><div class="menu-footer-menu-two-container"><ul id="menu-footer-menu-two" class="menu"><li id="menu-item-21362" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-21362"><a href="https://www.ndss-sy...`
- `database/snapshots/P003-ndss-content-leaks.html:389`
  `<li id="menu-item-23890" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-23890"><a href="https://www.ndss-symposium.org/ndss2026/accepted-papers/">Accepted Papers</a></li>`
- `database/snapshots/P003-ndss-content-leaks.html:390`
  `<li id="menu-item-23295" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-23295"><a href="https://www.ndss-symposium.org/ndss2026/program/">Program</a></li>`
- `database/snapshots/P003-ndss-content-leaks.html:391`
  `<li id="menu-item-22514" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-22514"><a href="https://www.ndss-symposium.org/ndss2026/co-located-events/">Co-located Events</a></li>`
- `database/snapshots/P003-ndss-content-leaks.html:392`
  `<li id="menu-item-21439" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-21439"><a href="https://www.ndss-symposium.org/ndss2026/leadership/">Leadership</a></li>`
- `database/snapshots/P003-ndss-content-leaks.html:396`
  `<section class="widget nav_menu-4 widget_nav_menu"><h3>NDSS Symposium 2022</h3><div class="menu-footer-menu-three-container"><ul id="menu-footer-menu-three" class="menu"><li id="menu-item-22123" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-22123"><a href="https://www.nds...`
- `database/snapshots/P003-ndss-content-leaks.html:397`
  `<li id="menu-item-18093" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-18093"><a href="https://www.ndss-symposium.org/ndss2025/accepted-papers/">Accepted Papers</a></li>`
- `database/snapshots/P003-ndss-content-leaks.html:398`
  `<li id="menu-item-22124" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-22124"><a href="https://www.ndss-symposium.org/ndss2025/program/">Program</a></li>`
- `database/snapshots/P003-ndss-content-leaks.html:399`
  `<li id="menu-item-18094" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-18094"><a href="https://www.ndss-symposium.org/ndss2025/co-located-events/">Co-located Events</a></li>`
- `database/snapshots/P003-ndss-content-leaks.html:400`
  `<li id="menu-item-18095" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-18095"><a href="https://www.ndss-symposium.org/ndss2025/leadership/">Leadership</a></li>`
- `database/snapshots/P003-ndss-content-leaks.html:405`
  `<li id="menu-item-9429" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-9429"><a href="https://www.ndss-symposium.org/previous-ndss-symposia/">Previous NDSS Symposia</a></li>`
- `database/snapshots/P003-ndss-content-leaks.html:406`
  `<li id="menu-item-21357" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-21357"><a href="https://www.ndss-symposium.org/previous-co-located-events/">Previous Co-located Events</a></li>`
- `database/snapshots/P003-ndss-content-leaks.html:418`
  `<figure class="wp-block-image size-large"><a href="https://www.facebook.com/NDSSSymposium/" target="_blank" rel=" noreferrer noopener"><img loading="lazy" decoding="async" width="12" height="25" src="https://www.ndss-symposium.org/wp-content/uploads/fb-12px-25px.svg" alt="Facebook" class="wp-image-9...`
- `database/snapshots/P003-ndss-content-leaks.html:422`
  `<figure class="wp-block-image size-full"><a href="https://twitter.com/NDSSSymposium" target="_blank" rel=" noreferrer noopener"><img decoding="async" src="https://www.ndss-symposium.org/wp-content/uploads/logo-white.png" alt="X home" class="wp-image-22046"></a></figure>`
- `database/snapshots/P003-ndss-content-leaks.html:426`
  `<figure class="wp-block-image size-large"><a href="https://www.linkedin.com/company/network-and-distributed-system-symposium-ndss-/" target="_blank" rel=" noreferrer noopener"><img loading="lazy" decoding="async" width="25" height="24" src="https://www.ndss-symposium.org/wp-content/uploads/in-25px-2...`
- `database/snapshots/P003-ndss-content-leaks.html:430`
  `<figure class="wp-block-image size-large"><a href="https://www.youtube.com/ndsssymposium" target="_blank" rel=" noreferrer noopener"><img loading="lazy" decoding="async" width="38" height="26" src="https://www.ndss-symposium.org/wp-content/uploads/yt-38px-26px.svg" alt="Youtube" class="wp-image-9328...`
- `database/snapshots/P003-ndss-content-leaks.html:442`
  `</section><section class="widget block-16 widget_block"><p style="font-size:16px; margin-bottom:20px">The Internet Society has been a proud host and organizer of the NDSS Symposium for over 30 years. <a href="https://www.internetsociety.org/about-internet-society/" target="_blank" style="cursor:poin...`
- `database/snapshots/P003-ndss-content-leaks.html:465`
  `.wp-block-image>a,.wp-block-image>figure>a{display:inline-block}.wp-block-image img{box-sizing:border-box;height:auto;max-width:100%;vertical-align:bottom}@media not (prefers-reduced-motion){.wp-block-image img.hide{visibility:hidden}.wp-block-image img.show{animation:show-content-image .4s}}.wp-blo...`
- `database/snapshots/P003-ndss-content-leaks.html:494`
  `var PT_CV_PUBLIC = {"_prefix":"pt-cv-","page_to_show":"5","_nonce":"8a2ffa9856","is_admin":"","is_mobile":"","ajaxurl":"https://www.ndss-symposium.org/wp-admin/admin-ajax.php","lang":"","loading_image_src":"data:image/gif;base64,R0lGODlhDwAPALMPAMrKygwMDJOTkz09PZWVla+vr3p6euTk5M7OzuXl5TMzMwAAAJmZmWZ...`
- `database/snapshots/P003-ndss-content-leaks.html:499`
  `<script type="text/javascript" src="https://www.ndss-symposium.org/wp-content/plugins/content-views-query-and-display-post-page/public/assets/js/cv.js?ver=4.3" id="pt-cv-content-views-script-js"></script>`
- `database/snapshots/P003-ndss-content-leaks.html:500`
  `<script type="text/javascript" src="https://www.ndss-symposium.org/wp-content/plugins/pt-content-views-pro/public/assets/js/cvpro.min.js?ver=7.3" id="pt-cv-public-pro-script-js"></script>`
- `database/snapshots/P003-ndss-content-leaks.html:501`
  `<script type="text/javascript" src="https://www.ndss-symposium.org/wp-content/themes/ndss2/dist/scripts/main.js" id="sage/main.js-js"></script>`
- `database/snapshots/P004-ndss-execute-this.html:7`
  `<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.1/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">`
- `database/snapshots/P004-ndss-execute-this.html:8`
  `<link rel="preconnect" href="https://fonts.googleapis.com">`
- `database/snapshots/P004-ndss-execute-this.html:9`
  `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>`

## BR098

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/com/kwad/sdk/k.java:66`
  `public static OkHttpClient.Builder Sn() {`
- `sources/com/kwad/sdk/k.java:67`
  `OkHttpClient.Builder builder = new OkHttpClient.Builder();`
- `sources/com/kwad/sdk/k.java:73`
  `public static OkHttpClient.Builder So() {`
- `sources/com/kwad/sdk/k.java:74`
  `OkHttpClient.Builder builder = new OkHttpClient.Builder();`
