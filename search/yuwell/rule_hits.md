# Rule Search Hits

## BR001

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/AndroidManifest.xml:33`
  `<uses-permission android:name="android.permission.CHANGE_WIFI_STATE"/>`
- `resources/AndroidManifest.xml:34`
  `<uses-permission android:name="android.permission.CAMERA"/>`
- `resources/AndroidManifest.xml:37`
  `<uses-permission android:name="android.permission.READ_PHONE_STATE"/>`
- `resources/AndroidManifest.xml:38`
  `<uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW"/>`
- `resources/AndroidManifest.xml:39`
  `<uses-permission android:name="android.permission.READ_CALENDAR"/>`
- `resources/AndroidManifest.xml:40`
  `<uses-permission android:name="android.permission.WRITE_CALENDAR"/>`
- `resources/AndroidManifest.xml:41`
  `<uses-permission android:name="android.permission.VIBRATE"/>`
- `resources/AndroidManifest.xml:69`
  `<uses-permission android:name="com.yuwell.uhealth.permission.MIPUSH_RECEIVE"/>`
- `resources/AndroidManifest.xml:70`
  `<uses-permission android:name="android.permission.CALL_PHONE"/>`
- `resources/AndroidManifest.xml:71`
  `<uses-permission android:name="android.permission.RECORD_AUDIO"/>`
- `resources/AndroidManifest.xml:72`
  `<uses-permission android:name="android.permission.FLAG_GRANT_READ_URI_PERMISSION"/>`

## BR002

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/AndroidManifest.xml:22`
  `<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>`
- `resources/AndroidManifest.xml:23`
  `<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>`
- `resources/AndroidManifest.xml:24`
  `<uses-permission android:name="android.permission.BLUETOOTH_CONNECT"/>`

## BR003

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/AndroidManifest.xml:13`
  `<uses-permission`
- `resources/AndroidManifest.xml:16`
  `<uses-permission`
- `resources/AndroidManifest.xml:23`
  `<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>`
- `resources/AndroidManifest.xml:24`
  `<uses-permission android:name="android.permission.BLUETOOTH_CONNECT"/>`
- `resources/AndroidManifest.xml:25`
  `<uses-permission android:name="android.permission.BLUETOOTH_SCAN"/>`
- `resources/AndroidManifest.xml:26`
  `<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>`

## BR004

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/AndroidManifest.xml:25`
  `<uses-permission android:name="android.permission.BLUETOOTH_SCAN"/>`
- `resources/AndroidManifest.xml:26`
  `<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>`
- `resources/AndroidManifest.xml:27`
  `<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>`
- `resources/AndroidManifest.xml:28`
  `<uses-permission android:name="android.permission.INTERNET"/>`

## BR007

paper_id: B025
paper_title: Why Eve and Mallory Still Love Android: Revisiting TLS (In)Security in Android Applications

- `resources/AndroidManifest.xml:82`
  `android:networkSecurityConfig="@xml/network_security_config"`
- `resources/res/xml/network_security_config.xml:3`
  `<base-config cleartextTrafficPermitted="true"/>`

## BR009

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/cn/jiguang/aa/a.java:6`
  `import javax.net.ssl.X509TrustManager;`
- `sources/cn/jiguang/aa/a.java:16`
  `private X509TrustManager m;`
- `sources/cn/jiguang/aa/a.java:70`
  `public X509TrustManager i() {`
- `sources/cn/jiguang/ay/c.java:14`
  `import javax.net.ssl.X509TrustManager;`
- `sources/cn/jiguang/ay/c.java:49`
  `X509TrustManager x509TrustManager = (X509TrustManager) objArr[3];`
- `sources/cn/jiguang/ay/c.java:68`
  `httpRequest.setSslTrustManager(x509TrustManager);`
- `sources/cn/jiguang/bf/b.java:15`
  `import javax.net.ssl.X509TrustManager;`
- `sources/cn/jiguang/bf/b.java:123`
  `X509TrustManager x509TrustManager = a;`
- `sources/cn/jiguang/bf/b.java:124`
  `if (x509TrustManager != null) {`
- `sources/cn/jiguang/bf/b.java:125`
  `httpRequest.setSslTrustManager(x509TrustManager);`
- `sources/cn/jiguang/net/HttpRequest.java:7`
  `import javax.net.ssl.X509TrustManager;`
- `sources/cn/jiguang/net/HttpRequest.java:17`
  `private X509TrustManager m;`
- `sources/cn/jiguang/net/HttpRequest.java:82`
  `public X509TrustManager getSslTrustManager() {`
- `sources/cn/jiguang/net/HttpRequest.java:176`
  `public void setSslTrustManager(X509TrustManager x509TrustManager) {`
- `sources/cn/jiguang/net/HttpRequest.java:177`
  `this.m = x509TrustManager;`
- `sources/cn/jiguang/net/SSLTrustManager.java:13`
  `import javax.net.ssl.X509TrustManager;`
- `sources/cn/jiguang/net/SSLTrustManager.java:16`
  `public class SSLTrustManager implements X509TrustManager {`
- `sources/cn/jiguang/net/SSLTrustManager.java:17`
  `private X509TrustManager a;`
- `sources/cn/jiguang/net/SSLTrustManager.java:32`
  `if (trustManager instanceof X509TrustManager) {`
- `sources/cn/jiguang/net/SSLTrustManager.java:33`
  `this.a = (X509TrustManager) trustManager;`
- `sources/cn/jiguang/net/SSLTrustManager.java:43`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/cn/jiguang/net/SSLTrustManager.java:44`
  `public void checkClientTrusted(X509Certificate[] x509CertificateArr, String str) {`
- `sources/cn/jiguang/net/SSLTrustManager.java:45`
  `d.c("SSLTrustManager", "checkClientTrusted");`
- `sources/cn/jiguang/net/SSLTrustManager.java:48`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/cn/jiguang/net/SSLTrustManager.java:49`
  `public void checkServerTrusted(X509Certificate[] x509CertificateArr, String str) throws CertificateException {`
- `sources/cn/jiguang/net/SSLTrustManager.java:50`
  `d.c("SSLTrustManager", "checkServerTrusted");`
- `sources/cn/jiguang/net/SSLTrustManager.java:57`
  `d.i("SSLTrustManager", "checkServerTrusted: CertificateExpiredException:" + e.getLocalizedMessage());`
- `sources/cn/jiguang/net/SSLTrustManager.java:60`
  `d.i("SSLTrustManager", "checkServerTrusted: CertificateNotYetValidException:" + e2.getLocalizedMessage());`
- `sources/cn/jiguang/net/SSLTrustManager.java:63`
  `d.i("SSLTrustManager", "checkServerTrusted failed, error" + th.getLocalizedMessage());`
- `sources/cn/jiguang/net/SSLTrustManager.java:68`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/cn/udesk/rich/BaseImageLoader.java:20`
  `import javax.net.ssl.X509TrustManager;`
- `sources/cn/udesk/rich/BaseImageLoader.java:45`
  `static class b implements X509TrustManager {`
- `sources/cn/udesk/rich/BaseImageLoader.java:49`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/cn/udesk/rich/BaseImageLoader.java:50`
  `@SuppressLint({"TrustAllX509TrustManager"})`
- `sources/cn/udesk/rich/BaseImageLoader.java:51`
  `public void checkClientTrusted(X509Certificate[] x509CertificateArr, String str) {`
- `sources/cn/udesk/rich/BaseImageLoader.java:54`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/cn/udesk/rich/BaseImageLoader.java:55`
  `@SuppressLint({"TrustAllX509TrustManager"})`
- `sources/cn/udesk/rich/BaseImageLoader.java:56`
  `public void checkServerTrusted(X509Certificate[] x509CertificateArr, String str) {`
- `sources/cn/udesk/rich/BaseImageLoader.java:59`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/com/lidroid/xutils/util/OtherUtils.java:18`
  `import javax.net.ssl.X509TrustManager;`
- `sources/com/lidroid/xutils/util/OtherUtils.java:29`
  `class a implements X509TrustManager {`
- `sources/com/lidroid/xutils/util/OtherUtils.java:33`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/com/lidroid/xutils/util/OtherUtils.java:34`
  `public void checkClientTrusted(X509Certificate[] x509CertificateArr, String str) {`
- `sources/com/lidroid/xutils/util/OtherUtils.java:37`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/com/lidroid/xutils/util/OtherUtils.java:38`
  `public void checkServerTrusted(X509Certificate[] x509CertificateArr, String str) {`
- `sources/com/lidroid/xutils/util/OtherUtils.java:41`
  `@Override // javax.net.ssl.X509TrustManager`
- `sources/okhttp3/OkHttpClient.java:22`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/OkHttpClient.java:368`
  `public Builder sslSocketFactory(SSLSocketFactory sSLSocketFactory, X509TrustManager x509TrustManager) {`
- `sources/okhttp3/OkHttpClient.java:370`
  `Objects.requireNonNull(x509TrustManager, "trustManager == null");`
- `sources/okhttp3/OkHttpClient.java:372`
  `this.n = CertificateChainCleaner.get(x509TrustManager);`
- `sources/okhttp3/OkHttpClient.java:471`
  `private static SSLSocketFactory b(X509TrustManager x509TrustManager) {`
- `sources/okhttp3/OkHttpClient.java:474`
  `sSLContext.init(null, new TrustManager[]{x509TrustManager}, null);`
- `sources/okhttp3/OkHttpClient.java:632`
  `X509TrustManager x509TrustManagerPlatformTrustManager = Util.platformTrustManager();`
- `sources/okhttp3/OkHttpClient.java:633`
  `this.m = b(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/OkHttpClient.java:634`
  `this.n = CertificateChainCleaner.get(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/internal/Util.java:34`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/Util.java:538`
  `public static X509TrustManager platformTrustManager() {`
- `sources/okhttp3/internal/Util.java:543`
  `if (trustManagers.length == 1 && (trustManagers[0] instanceof X509TrustManager)) {`
- `sources/okhttp3/internal/Util.java:544`
  `return (X509TrustManager) trustManagers[0];`
- `sources/okhttp3/internal/platform/b.java:22`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/platform/b.java:125`
  `private final X509TrustManager a;`
- `sources/okhttp3/internal/platform/b.java:128`
  `c(X509TrustManager x509TrustManager, Method method) {`
- `sources/okhttp3/internal/platform/b.java:130`
  `this.a = x509TrustManager;`
- `sources/okhttp3/internal/platform/b.java:218`
  `public CertificateChainCleaner buildCertificateChainCleaner(X509TrustManager x509TrustManager) {`
- `sources/okhttp3/internal/platform/b.java:220`
  `Class<?> cls = Class.forName("android.net.http.X509TrustManagerExtensions");`
- `sources/okhttp3/internal/platform/b.java:221`
  `return new a(cls.getConstructor(X509TrustManager.class).newInstance(x509TrustManager), cls.getMethod("checkServerTrusted", X509Certificate[].class, String.class, String.class));`
- `sources/okhttp3/internal/platform/b.java:223`
  `return super.buildCertificateChainCleaner(x509TrustManager);`
- `sources/okhttp3/internal/platform/b.java:228`
  `public TrustRootIndex buildTrustRootIndex(X509TrustManager x509TrustManager) {`
- `sources/okhttp3/internal/platform/b.java:230`
  `Method declaredMethod = x509TrustManager.getClass().getDeclaredMethod("findTrustAnchorByIssuerAndSignature", X509Certificate.class);`
- `sources/okhttp3/internal/platform/b.java:232`
  `return new c(x509TrustManager, declaredMethod);`
- `sources/okhttp3/internal/platform/b.java:234`
  `return super.buildTrustRootIndex(x509TrustManager);`
- `sources/okhttp3/internal/platform/b.java:372`
  `protected X509TrustManager trustManager(SSLSocketFactory sSLSocketFactory) {`
- `sources/okhttp3/internal/platform/b.java:381`
  `X509TrustManager x509TrustManager = (X509TrustManager) Platform.e(objE, X509TrustManager.class, "x509TrustManager");`
- `sources/okhttp3/internal/platform/b.java:382`
  `return x509TrustManager != null ? x509TrustManager : (X509TrustManager) Platform.e(objE, X509TrustManager.class, "trustManager");`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:11`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:77`
  `public X509TrustManager trustManager(SSLSocketFactory sSLSocketFactory) {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:84`
  `return (X509TrustManager) Platform.e(objE, X509TrustManager.class, "x509TrustManager");`
- `sources/okhttp3/internal/platform/d.java:10`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/platform/d.java:65`
  `public X509TrustManager trustManager(SSLSocketFactory sSLSocketFactory) {`
- `sources/okhttp3/internal/platform/Platform.java:18`
  `import javax.net.ssl.X509TrustManager;`

## BR010

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/cn/udesk/rich/BaseImageLoader.java:38`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/cn/udesk/rich/BaseImageLoader.java:39`
  `@SuppressLint({"BadHostnameVerifier"})`
- `sources/cn/udesk/rich/BaseImageLoader.java:40`
  `public boolean verify(String str, SSLSession sSLSession) {`
- `sources/com/lidroid/xutils/util/OtherUtils.java:219`
  `HttpsURLConnection.setDefaultHostnameVerifier(org.apache.http.conn.ssl.SSLSocketFactory.ALLOW_ALL_HOSTNAME_VERIFIER);`
- `sources/okhttp3/internal/connection/RealConnection.java:297`
  `if (this.f == null || list == null || !j(list) || address.hostnameVerifier() != OkHostnameVerifier.INSTANCE || !supportsUrl(address.url())) {`
- `sources/okhttp3/internal/connection/RealConnection.java:428`
  `return this.d != null && OkHostnameVerifier.INSTANCE.verify(httpUrl.host(), (X509Certificate) this.d.peerCertificates().get(0));`
- `sources/okhttp3/internal/tls/BasicCertificateChainCleaner.java:25`
  `x509Certificate.verify(x509Certificate2.getPublicKey());`
- `sources/okhttp3/internal/tls/OkHostnameVerifier.java:74`
  `@Override // javax.net.ssl.HostnameVerifier`

## BR011

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/com/alipay/android/phone/mrpc/core/ad.java:5`
  `import javax.net.ssl.SSLException;`
- `sources/com/alipay/android/phone/mrpc/core/ad.java:22`
  `return ((iOException instanceof SocketException) || (iOException instanceof SSLException)) && iOException.getMessage() != null && iOException.getMessage().contains("Broken pipe");`
- `sources/okhttp3/internal/connection/b.java:66`
  `if (((iOException instanceof SSLHandshakeException) && (iOException.getCause() instanceof CertificateException)) || (iOException instanceof SSLPeerUnverifiedException)) {`
- `sources/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:117`
  `return iOException instanceof InterruptedIOException ? (iOException instanceof SocketTimeoutException) && !z : (((iOException instanceof SSLHandshakeException) && (iOException.getCause() instanceof CertificateException)) || (iOException instanceof SSLPeerUnverifiedException)) ? false : true;`

## BR012

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/okhttp3/Address.java:35`
  `final CertificatePinner k;`
- `sources/okhttp3/Address.java:37`
  `public Address(String str, int i, Dns dns, SocketFactory socketFactory, @Nullable SSLSocketFactory sSLSocketFactory, @Nullable HostnameVerifier hostnameVerifier, @Nullable CertificatePinner certificatePinner, Authenticator authenticator, @Nullable Proxy proxy, List<Protocol> list, List<ConnectionSpe...`
- `sources/okhttp3/Address.java:54`
  `this.k = certificatePinner;`
- `sources/okhttp3/Address.java:62`
  `public CertificatePinner certificatePinner() {`
- `sources/okhttp3/CertificatePinner.java:20`
  `public final class CertificatePinner {`
- `sources/okhttp3/CertificatePinner.java:21`
  `public static final CertificatePinner DEFAULT = new Builder().build();`
- `sources/okhttp3/CertificatePinner.java:38`
  `public CertificatePinner build() {`
- `sources/okhttp3/CertificatePinner.java:39`
  `return new CertificatePinner(new LinkedHashSet(this.a), null);`
- `sources/okhttp3/CertificatePinner.java:62`
  `if (!str2.startsWith("sha256/")) {`
- `sources/okhttp3/CertificatePinner.java:63`
  `throw new IllegalArgumentException("pins must start with 'sha256/' or 'sha1/': " + str2);`
- `sources/okhttp3/CertificatePinner.java:65`
  `this.c = "sha256/";`
- `sources/okhttp3/CertificatePinner.java:107`
  `CertificatePinner(Set<a> set, @Nullable CertificateChainCleaner certificateChainCleaner) {`
- `sources/okhttp3/CertificatePinner.java:124`
  `return "sha256/" + c((X509Certificate) certificate).base64();`
- `sources/okhttp3/CertificatePinner.java:157`
  `if (aVar.c.equals("sha256/")) {`
- `sources/okhttp3/CertificatePinner.java:200`
  `CertificatePinner d(@Nullable CertificateChainCleaner certificateChainCleaner) {`
- `sources/okhttp3/CertificatePinner.java:201`
  `return Objects.equals(this.b, certificateChainCleaner) ? this : new CertificatePinner(this.a, certificateChainCleaner);`
- `sources/okhttp3/CertificatePinner.java:208`
  `if (obj instanceof CertificatePinner) {`
- `sources/okhttp3/CertificatePinner.java:209`
  `CertificatePinner certificatePinner = (CertificatePinner) obj;`
- `sources/okhttp3/CertificatePinner.java:210`
  `if (Objects.equals(this.b, certificatePinner.b) && this.a.equals(certificatePinner.a)) {`
- `sources/okhttp3/OkHttpClient.java:67`
  `final CertificatePinner p;`
- `sources/okhttp3/OkHttpClient.java:107`
  `CertificatePinner p;`
- `sources/okhttp3/OkHttpClient.java:134`
  `this.p = CertificatePinner.DEFAULT;`
- `sources/okhttp3/OkHttpClient.java:187`
  `public Builder certificatePinner(CertificatePinner certificatePinner) {`
- `sources/okhttp3/OkHttpClient.java:188`
  `Objects.requireNonNull(certificatePinner, "certificatePinner == null");`
- `sources/okhttp3/OkHttpClient.java:189`
  `this.p = certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:500`
  `public CertificatePinner certificatePinner() {`
- `sources/okhttp3/internal/connection/RealConnection.java:23`
  `import okhttp3.CertificatePinner;`
- `sources/okhttp3/internal/connection/RealConnection.java:130`
  `address.certificatePinner().check(address.url().host(), handshake.peerCertificates());`
- `sources/okhttp3/internal/connection/RealConnection.java:148`
  `throw new SSLPeerUnverifiedException("Hostname " + address.url().host() + " not verified:\n    certificate: " + CertificatePinner.pin(x509Certificate) + "\n    DN: " + x509Certificate.getSubjectDN().getName() + "\n    subjectAltNames: " + OkHostnameVerifier.allSubjectAltNames(x509Certificate));`
- `sources/okhttp3/internal/connection/RealConnection.java:301`
  `address.certificatePinner().check(address.url().host(), handshake().peerCertificates());`
- `sources/okhttp3/internal/connection/Transmitter.java:13`
  `import okhttp3.CertificatePinner;`
- `sources/okhttp3/internal/connection/Transmitter.java:79`
  `CertificatePinner certificatePinner;`
- `sources/okhttp3/internal/connection/Transmitter.java:84`
  `certificatePinner = this.a.certificatePinner();`
- `sources/okhttp3/internal/connection/Transmitter.java:88`
  `certificatePinner = null;`
- `sources/okhttp3/internal/connection/Transmitter.java:90`
  `return new Address(httpUrl.host(), httpUrl.port(), this.a.dns(), this.a.socketFactory(), sSLSocketFactory, hostnameVerifier, certificatePinner, this.a.proxyAuthenticator(), this.a.proxy(), this.a.protocols(), this.a.connectionSpecs(), this.a.proxySelector());`

## BR013

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `resources/assets/js/highcharts.js:9`
  `R=g.navigator&&g.navigator.userAgent||"",y=c&&c.createElementNS&&!!c.createElementNS("http://www.w3.org/2000/svg","svg").createSVGRect,q=/(edge|msie|trident)/i.test(R)&&!g.opera,H=-1!==R.indexOf("Firefox"),D=-1!==R.indexOf("Chrome"),J=H&&4>parseInt(R.split("Firefox/")[1],10);return{product:"Highchar...`
- `resources/assets/js/highcharts.js:10`
  `SVG_NS:"http://www.w3.org/2000/svg",chartCount:0,seriesTypes:{},symbolSizes:{},svg:y,win:g,marginNames:["plotTop","marginRight","marginBottom","plotLeft"],noop:function(){},charts:[],dateFormats:{}}});O(q,"parts/Utilities.js",[q["parts/Globals.js"]],function(g){function c(b,h,e,z){var a=h?"Highchart...`
- `resources/assets/js/highcharts.js:65`
  `z=!0);var l=x.element;(e=a.element.getAttribute("id"))||a.element.setAttribute("id",e=M());if(d)for(a=b.getElementsByTagName("tspan");a.length;)a[0].setAttribute("y",0),f(k.dx)&&a[0].setAttribute("x",-k.dx),l.appendChild(a[0]);z&&x&&x.add({element:this.text?this.text.element:b});l.setAttributeNS("ht...`
- `resources/assets/js/highcharts.js:104`
  `this.width=b;this.height=a;for(this.boxWrapper.animate({width:b,height:a},{step:function(){this.attr({viewBox:"0 0 "+this.attr("width")+" "+this.attr("height")})},duration:m(e,!0)?void 0:0});f--;)h[f].align()};b.prototype.g=function(b){var h=this.createElement("g");return b?h.attr({"class":"highchar...`
- `resources/org.jivesoftware.smackx/smack-experimental-components.xml:2`
  `<scr:component xmlns:scr="http://www.osgi.org/xmlns/scr/v1.2.0"`
- `resources/org.jivesoftware.smackx/smack-extensions-components.xml:2`
  `<scr:component xmlns:scr="http://www.osgi.org/xmlns/scr/v1.2.0"`
- `resources/res/color/design_box_stroke_color.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/abc_ic_ab_back_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_arrow_drop_right_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_clear_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_go_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_menu_overflow_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_voice_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_list_divider_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:tint="?android:attr/colorForeground">`
- `resources/res/drawable/abc_seekbar_tick_mark_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/abc_text_cursor_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/res/drawable/abc_vector_test.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/avd_hide_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_hide_password__0_res_0x7f080000">`
- `resources/res/drawable/avd_show_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_show_password__0_res_0x7f080003">`
- `resources/res/drawable/bg_edit_text.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/btn_checkbox_checked_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/btn_checkbox_unchecked_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/btn_radio_off_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/btn_radio_on_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/button_enable.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/circle_beat.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/circle_blue.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/circle_brown.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/circle_ff6775.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/circle_green.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/circle_grey.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/circle_list_item.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/circle_red.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/circle_white_alpha.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/circle_white_alpha_20.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/circle_yellow.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/coin.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/design_ic_visibility.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/design_ic_visibility_off.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`

## BR014

paper_id: B022
paper_title: A Study of Android Application Security

- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1167`
  `boolean z2 = KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1;`
- `sources/androidx/appcompat/app/d.java:321`
  `menuB.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);`
- `sources/androidx/appcompat/app/WindowDecorActionBar.java:929`
  `menu.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);`
- `sources/androidx/core/content/ContextCompat.java:55`
  `import android.telephony.TelephonyManager;`
- `sources/androidx/core/content/ContextCompat.java:146`
  `map.put(TelephonyManager.class, UdeskConst.StructBtnTypeString.phone);`
- `sources/cn/jiguang/api/JCoreInterface.java:73`
  `public static String getDeviceId(Context context) {`
- `sources/cn/jiguang/aq/a.java:280`
  `cn.jiguang.r.a.f("IdHelper", "google getAdvertisingIdInfo Exception: " + th2.toString());`
- `sources/cn/jiguang/aq/a.java:329`
  `cn.jiguang.r.a.f("IdHelper", "hw getAdvertisingIdInfo Exception: " + th2.toString());`
- `sources/cn/jiguang/aq/a.java:375`
  `cn.jiguang.r.a.f("IdHelper", "zui getAdvertisingIdInfo Exception: " + e2.toString());`
- `sources/cn/jiguang/aq/a.java:443`
  `cn.jiguang.r.a.f("IdHelper", "sumsung getAdvertisingIdInfo Exception: " + e2.toString());`
- `sources/cn/jiguang/aq/a.java:516`
  `cn.jiguang.r.a.f("IdHelper", "oppo getAdvertisingIdInfo Exception: " + e2.toString());`
- `sources/cn/jiguang/aq/a.java:596`
  `cn.jiguang.r.a.f("IdHelper", "asus getAdvertisingIdInfo Exception: " + e2.toString());`
- `sources/cn/jiguang/f/a.java:505`
  `Object objA = cn.jiguang.ay.a.a(context, "getImei", bundle, null);`
- `sources/cn/jiguang/n/a.java:91`
  `if (str.equals("getImei")) {`
- `sources/cn/jiguang/o/b.java:22`
  `import android.telephony.TelephonyManager;`
- `sources/cn/jiguang/o/b.java:33`
  `private final TelephonyManager b;`
- `sources/cn/jiguang/o/b.java:73`
  `this.b = (TelephonyManager) context.getSystemService(UdeskConst.StructBtnTypeString.phone);`
- `sources/cn/jiguang/o/b.java:82`
  `cn.jiguang.r.a.f("JLocationCell", "get telephonyManager failed");`
- `sources/cn/jiguang/w/g.java:6`
  `import android.telephony.TelephonyManager;`
- `sources/cn/jiguang/w/g.java:80`
  `Object objA = e.a((Class<?>) TelephonyManager.class, "getNetworkClass", new Object[]{Integer.valueOf(i)}, new Class[]{Integer.TYPE});`
- `sources/cn/jiguang/w/g.java:153`
  `c = ((TelephonyManager) context.getSystemService(UdeskConst.StructBtnTypeString.phone)).getNetworkType();`
- `sources/cn/jiguang/w/g.java:170`
  `d = ((TelephonyManager) context.getSystemService(UdeskConst.StructBtnTypeString.phone)).getNetworkOperator();`
- `sources/cn/jiguang/w/g.java:186`
  `e = ((TelephonyManager) context.getSystemService(UdeskConst.StructBtnTypeString.phone)).getNetworkOperatorName();`
- `sources/cn/jpush/android/api/JPushInterface.java:272`
  `return JCoreHelper.getDeviceId(context);`
- `sources/cn/jpush/android/helper/JCoreHelper.java:59`
  `public static String getDeviceId(Context context) {`
- `sources/com/alipay/android/app/helper/TidHelper.java:11`
  `public static String getIMEI(Context context) {`
- `sources/com/alipay/android/app/helper/TidHelper.java:12`
  `return com.alipay.sdk.tid.TidHelper.getIMEI(context);`
- `sources/com/alipay/mobile/common/logging/LogContextImpl.java:408`
  `public String getDeviceId() {`
- `sources/com/alipay/mobile/common/logging/api/LogContext.java:144`
  `String getDeviceId();`
- `sources/com/alipay/mobile/common/logging/api/LoggerFactory.java:395`
  `public String getDeviceId() {`
- `sources/com/alipay/mobile/common/logging/render/AntEventRender.java:59`
  `LoggingUtil.appendParam(sb, this.b.getDeviceId());`
- `sources/com/alipay/mobile/common/logging/render/BatteryRender.java:29`
  `LoggingUtil.appendParam(sb, this.b.getDeviceId());`
- `sources/com/alipay/mobile/common/logging/render/BehavorRender.java:79`
  `LoggingUtil.appendParam(sb, this.b.getDeviceId());`
- `sources/com/alipay/mobile/common/logging/render/DataflowRender.java:51`
  `LoggingUtil.appendParam(sb, this.b.getDeviceId());`
- `sources/com/alipay/mobile/common/logging/render/DiagnoseRender.java:51`
  `LoggingUtil.appendParam(sb, this.b.getDeviceId());`
- `sources/com/alipay/mobile/common/logging/render/ExceptionRender.java:112`
  `LoggingUtil.appendParam(sb, this.b.getDeviceId());`
- `sources/com/alipay/mobile/common/logging/render/PerformanceRender.java:86`
  `LoggingUtil.appendParam(sb, this.b.getDeviceId());`
- `sources/com/alipay/mobile/common/logging/strategy/LogStrategyManager.java:184`
  `boolean zIsHitTest = SimplingUtils.isHitTest(getUploadRateByLevel(logStrategyInfo, i), LoggerFactory.getLogContext().getDeviceId());`
- `sources/com/alipay/mobile/common/logging/strategy/StoreFloodManager.java:49`
  `boolean zIsHitStoreFlood = SimplingUtils.isHitStoreFlood(logStrategyInfo.floodRate, LoggerFactory.getLogContext().getDeviceId());`
- `sources/com/alipay/mobile/common/logging/util/config/GrayScaleUtils.java:37`
  `return !TextUtils.isEmpty(strA) ? grayscaleUtdid(LoggerFactory.getLogContext().getDeviceId(), strA) : z;`
- `sources/com/alipay/mobile/common/logging/util/network/NetworkUtils.java:8`
  `import android.telephony.TelephonyManager;`
- `sources/com/alipay/mobile/common/logging/util/network/NetworkUtils.java:120`
  `Integer num = (Integer) TelephonyManager.class.getMethod("getNetworkClass", Integer.TYPE).invoke(TelephonyManager.class, Integer.valueOf(i));`
- `sources/com/alipay/mobile/common/logging/util/network/NetworkUtils.java:129`
  `Log.e(TAG, "TelephonyManager#getNetworkClass exception: " + th.toString());`
- `sources/com/alipay/sdk/tid/TidHelper.java:41`
  `public static String getIMEI(Context context) {`
- `sources/com/alipay/security/mobile/module/b/b.java:18`
  `import android.telephony.TelephonyManager;`
- `sources/com/alipay/security/mobile/module/b/b.java:65`
  `android.telephony.TelephonyManager r2 = (android.telephony.TelephonyManager) r2     // Catch: java.lang.Throwable -> L1c`
- `sources/com/alipay/security/mobile/module/b/b.java:67`
  `java.lang.String r2 = r2.getDeviceId()     // Catch: java.lang.Throwable -> L1c`
- `sources/com/alipay/security/mobile/module/b/b.java:106`
  `android.telephony.TelephonyManager r2 = (android.telephony.TelephonyManager) r2     // Catch: java.lang.Throwable -> L1c`
- `sources/com/alipay/security/mobile/module/b/b.java:108`
  `java.lang.String r2 = r2.getSubscriberId()     // Catch: java.lang.Throwable -> L1c`
- `sources/com/alipay/security/mobile/module/b/b.java:269`
  `android.telephony.TelephonyManager r1 = (android.telephony.TelephonyManager) r1     // Catch: java.lang.Throwable -> L11`
- `sources/com/alipay/security/mobile/module/b/b.java:546`
  `String simSerialNumber = ((TelephonyManager) context.getSystemService(UdeskConst.StructBtnTypeString.phone)).getSimSerialNumber();`
- `sources/com/alipay/security/mobile/module/b/b.java:597`
  `TelephonyManager telephonyManager = (TelephonyManager) context.getSystemService(UdeskConst.StructBtnTypeString.phone);`
- `sources/com/alipay/security/mobile/module/b/b.java:598`
  `return telephonyManager != null ? String.valueOf(telephonyManager.getNetworkType()) : "";`
- `sources/com/alipay/security/mobile/module/b/d.java:48`
  `android.telephony.TelephonyManager r1 = (android.telephony.TelephonyManager) r1     // Catch: java.lang.Exception -> L66`
- `sources/com/alipay/security/mobile/module/b/d.java:50`
  `java.lang.String r1 = r1.getDeviceId()     // Catch: java.lang.Exception -> L66`
- `sources/com/ta/utdid2/a/a/e.java:65`
  `android.telephony.TelephonyManager r1 = (android.telephony.TelephonyManager) r1     // Catch: java.lang.Exception -> L11`
- `sources/com/ta/utdid2/a/a/e.java:67`
  `java.lang.String r1 = r1.getSubscriberId()     // Catch: java.lang.Exception -> L11`
- `sources/com/ta/utdid2/a/a/e.java:101`
  `android.telephony.TelephonyManager r0 = (android.telephony.TelephonyManager) r0     // Catch: java.lang.Exception -> L17`
- `sources/com/ta/utdid2/a/a/e.java:103`
  `java.lang.String r0 = r0.getDeviceId()     // Catch: java.lang.Exception -> L17`
- `sources/com/ta/utdid2/device/a.java:36`
  `public String getDeviceId() {`
- `sources/com/ta/utdid2/device/b.java:16`
  `String str = String.format("%s%s%s%s%s", aVar.f(), aVar.getDeviceId(), Long.valueOf(aVar.a()), aVar.getImsi(), aVar.e());`
- `sources/com/totoro/database/entity/EntityBase.java:44`
  `public String getDeviceId() {`
- `sources/com/umeng/commonsdk/UMConfigure.java:276`
  `strArr[0] = DeviceConfig.getDeviceIdForGeneral(context);`
- `sources/com/umeng/commonsdk/internal/d.java:198`
  `jSONObject.put("a_meid", DeviceConfig.getMeid(applicationContext));`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:15`
  `import android.telephony.TelephonyManager;`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:170`
  `TelephonyManager telephonyManager = (TelephonyManager) context.getSystemService(UdeskConst.StructBtnTypeString.phone);`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:171`
  `if (telephonyManager != null) {`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:174`
  `String deviceId = telephonyManager.getDeviceId();`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:177`
  `MLog.i(LOG_TAG, "getDeviceId, IMEI: " + deviceId);`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:363`
  `public static String getDeviceId(Context context) {`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:364`
  `return AnalyticsConstants.getDeviceType() == 2 ? getDeviceIdForBox(context) : getDeviceIdForGeneral(context);`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:367`
  `public static String getDeviceIdForBox(Context context) {`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:379`
  `MLog.i(LOG_TAG, "getDeviceId, ANDROID_ID: " + androidId);`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:388`
  `MLog.i(LOG_TAG, "getDeviceId, MAC: " + strH);`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:407`
  `MLog.i(LOG_TAG, "getDeviceId, ANDROID_ID: " + androidId);`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:426`
  `MLog.i(LOG_TAG, "getDeviceId, MAC: " + strG);`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:475`
  `MLog.i(LOG_TAG, "getDeviceId: ANDROID_ID: " + androidId);`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:502`
  `MLog.i(LOG_TAG, "getDeviceId, MAC: " + strH3);`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:509`
  `public static String getDeviceIdForGeneral(Context context) {`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:534`
  `MLog.i(LOG_TAG, "getDeviceId, ANDROID_ID: " + strH);`

## BR015

paper_id: B022
paper_title: A Study of Android Application Security

- `sources/cn/jiguang/ab/a.java:91`
  `this.e = a(Build.DEVICE);`
- `sources/cn/jiguang/ab/a.java:92`
  `this.k = a(Build.PRODUCT);`
- `sources/cn/jiguang/ad/d.java:84`
  `jSONObject.put("manufacturer", Build.MANUFACTURER);`
- `sources/cn/jiguang/ad/d.java:87`
  `jSONObject.put(Constants.PHONE_BRAND, Build.BRAND);`
- `sources/cn/jiguang/ad/d.java:91`
  `jSONObject.put("model", Build.MODEL);`
- `sources/cn/jiguang/ad/d.java:123`
  `jSONObject.put("language", Locale.getDefault().toString());`
- `sources/cn/jiguang/ad/d.java:246`
  `return Build.MODEL.split(" ", -1)[0];`
- `sources/cn/jiguang/ad/d.java:266`
  `java.lang.String r2 = android.os.Build.BRAND     // Catch: java.lang.Exception -> L99`
- `sources/cn/jiguang/ad/d.java:269`
  `java.lang.String r2 = android.os.Build.DEVICE     // Catch: java.lang.Exception -> L99`
- `sources/cn/jiguang/am/c.java:184`
  `String str4 = Build.MODEL;`
- `sources/cn/jiguang/an/b.java:99`
  `String str4 = String.format(Locale.ENGLISH, Build.MODEL, new Object[0]);`
- `sources/cn/jiguang/an/b.java:106`
  `String str5 = String.format(Locale.ENGLISH, Build.BRAND, new Object[0]);`
- `sources/cn/jiguang/an/b.java:113`
  `String str6 = String.format(Locale.ENGLISH, Build.PRODUCT, new Object[0]);`
- `sources/cn/jiguang/an/b.java:141`
  `long rawOffset = ((long) TimeZone.getDefault().getRawOffset()) / 3600000;`
- `sources/cn/jiguang/api/JCoreInterface.java:106`
  `return Build.BRAND.equals(DeviceProperty.ALIAS_NUBIA);`
- `sources/cn/jiguang/az/i.java:178`
  `jSONObject.put("jg_brand", Build.BRAND);`
- `sources/cn/jiguang/w/a.java:108`
  `return cn.jiguang.ag.a.a().e(YearClass.CLASS_2008) ? a(Build.MANUFACTURER) : "";`
- `sources/cn/jiguang/z/a.java:157`
  `String str4 = String.format(locale, Build.MODEL, new Object[0]);`
- `sources/cn/jiguang/z/a.java:162`
  `String str5 = String.format(locale, Build.BRAND, new Object[0]);`
- `sources/cn/jiguang/z/a.java:167`
  `String str6 = String.format(locale, Build.PRODUCT, new Object[0]);`
- `sources/cn/jiguang/z/a.java:177`
  `String str7 = String.format(locale, Build.MANUFACTURER, new Object[0]);`
- `sources/cn/jiguang/z/a.java:182`
  `long rawOffset = TimeZone.getDefault().getRawOffset() / 3600000;`
- `sources/cn/jpush/android/ad/a.java:560`
  `if (!Build.MANUFACTURER.equalsIgnoreCase(DeviceProperty.ALIAS_VIVO) && !strC.startsWith("Funtouch")) {`
- `sources/cn/jpush/android/x/b.java:672`
  `String str = Build.MANUFACTURER;`
- `sources/com/alibaba/fastjson/JSON.java:46`
  `public static TimeZone defaultTimeZone = TimeZone.getDefault();`
- `sources/com/alibaba/fastjson/JSON.java:47`
  `public static Locale defaultLocale = Locale.getDefault();`
- `sources/com/alibaba/sdk/android/oss/common/utils/OSSUtils.java:104`
  `sb.append("[INFO]: mobile_model：" + Build.MODEL + "\n");`
- `sources/com/alipay/camera/CameraConfigurationManager.java:423`
  `if (FpsWhiteList.inWhiteList(Build.BRAND, Build.MODEL)) {`
- `sources/com/alipay/camera/CameraConfigurationManager.java:559`
  `String str = Build.MODEL;`
- `sources/com/alipay/camera/CameraConfigurationManager.java:573`
  `return DeviceProperty.ALIAS_XIAOMI.equalsIgnoreCase(Build.BRAND) && Build.VERSION.SDK_INT >= 17 && Settings.Global.getInt(this.b.getContentResolver(), "force_fsg_nav_bar", 0) != 0;`
- `sources/com/alipay/camera/CameraConfigurationManager.java:603`
  `String str = Build.BRAND;`
- `sources/com/alipay/camera/compatible/CompatibleManager.java:44`
  `String str = Build.MANUFACTURER;`
- `sources/com/alipay/camera/util/FpsWhiteList.java:45`
  `String str2 = Build.BRAND + "/" + Build.MODEL;`
- `sources/com/alipay/camera/util/ManufacturerPermissionChecker.java:61`
  `String str = Build.MANUFACTURER;`
- `sources/com/alipay/mobile/bqcscanservice/behavior/BehaviorBury.java:167`
  `behavor.addExtParam(com.xiaomi.mipush.sdk.Constants.PHONE_BRAND, Build.BRAND);`
- `sources/com/alipay/mobile/common/logging/DevicePropertyImpl.java:44`
  `this.mBrandName = Build.BRAND.toLowerCase();`
- `sources/com/alipay/mobile/common/logging/DevicePropertyImpl.java:108`
  `this.mManufacturer = Build.MANUFACTURER.toLowerCase();`
- `sources/com/alipay/mobile/common/logging/ProcessInfoImpl.java:359`
  `return PreferenceManager.getDefaultSharedPreferences(this.a).getBoolean("huawei_preload_launch_models", "PAR-TL00 PAR-LX9 PAR-LX1 PAR-LX1M PAR-AL00 PAR-TL20".contains(Build.MODEL));`
- `sources/com/alipay/mobile/common/logging/render/AntEventRender.java:56`
  `LoggingUtil.appendParam(sb, Build.MODEL);`
- `sources/com/alipay/mobile/common/logging/render/AntEventRender.java:61`
  `LoggingUtil.appendParam(sb, Build.MANUFACTURER);`
- `sources/com/alipay/mobile/common/logging/render/BatteryRender.java:38`
  `LoggingUtil.appendParam(sb, Build.MODEL);`
- `sources/com/alipay/mobile/common/logging/render/BehavorRender.java:103`
  `LoggingUtil.appendParam(sb, Build.MODEL);`
- `sources/com/alipay/mobile/common/logging/render/DataflowRender.java:63`
  `LoggingUtil.appendParam(sb, Build.MODEL);`
- `sources/com/alipay/mobile/common/logging/render/DiagnoseRender.java:28`
  `LoggingUtil.appendParam(sb, Build.MODEL);`
- `sources/com/alipay/mobile/common/logging/render/ExceptionRender.java:107`
  `LoggingUtil.appendParam(sb, Build.MODEL);`
- `sources/com/alipay/mobile/common/logging/render/PerformanceRender.java:83`
  `LoggingUtil.appendParam(sb, Build.MODEL);`
- `sources/com/alipay/mobile/common/logging/util/LowEndDeviceUtil.java:43`
  `sInLowEndDeviceList = hashSet.contains(Build.MODEL);`
- `sources/com/alipay/mobile/common/nativecrash/CrashFilterUtils.java:167`
  `if ("BenWee V5".equals(Build.MODEL)) {`
- `sources/com/alipay/sdk/app/statistic/b.java:122`
  `return new SimpleDateFormat("HH:mm:ss:SSS", Locale.getDefault()).format(new Date());`
- `sources/com/alipay/sdk/packet/e.java:55`
  `map.put(p, Build.MODEL);`
- `sources/com/alipay/sdk/util/l.java:386`
  `String lowerCase = Build.BRAND.toLowerCase();`
- `sources/com/alipay/sdk/util/l.java:387`
  `String lowerCase2 = Build.MANUFACTURER.toLowerCase();`
- `sources/com/alipay/security/mobile/module/b/d.java:111`
  `return Build.BRAND;`
- `sources/com/alipay/security/mobile/module/b/d.java:115`
  `return Build.DEVICE;`
- `sources/com/google/android/material/datepicker/e.java:72`
  `textView.setContentDescription(String.format(viewGroup.getContext().getString(R.string.mtrl_picker_day_of_week_column_header), this.a.getDisplayName(7, 2, Locale.getDefault())));`
- `sources/com/google/android/material/internal/ManufacturerUtils.java:19`
  `return Build.MANUFACTURER.toLowerCase(Locale.ENGLISH).equals("lge");`
- `sources/com/google/android/material/internal/ManufacturerUtils.java:23`
  `return Build.MANUFACTURER.toLowerCase(Locale.ENGLISH).equals(DeviceProperty.ALIAS_MEIZU);`
- `sources/com/google/android/material/internal/ManufacturerUtils.java:27`
  `return Build.MANUFACTURER.toLowerCase(Locale.ENGLISH).equals(DeviceProperty.ALIAS_SAMSUNG);`
- `sources/com/umeng/analytics/pro/ac.java:12`
  `String str = Build.BRAND;`
- `sources/com/umeng/analytics/pro/ac.java:35`
  `if (Build.MANUFACTURER.equalsIgnoreCase("SAMSUNG")) {`
- `sources/com/umeng/analytics/pro/o.java:854`
  `String str2 = new SimpleDateFormat("yyyy-MM-dd", Locale.getDefault()).format(new Date(System.currentTimeMillis()));`
- `sources/com/umeng/analytics/process/UMProcessDBDatasSender.java:218`
  `jSONObject.put(d.m, sharedPreferences.getString("vers_date", new SimpleDateFormat("yyyy-MM-dd", Locale.getDefault()).format(new Date(System.currentTimeMillis()))));`
- `sources/com/umeng/commonsdk/internal/d.java:414`
  `jSONObject.put("a_pr", Build.PRODUCT);`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:1423`
  `java.lang.String r0 = android.os.Build.SERIAL     // Catch: java.lang.Throwable -> L64`
- `sources/com/umeng/commonsdk/statistics/internal/a.java:30`
  `this.a = str.replaceAll("&=", " ").replaceAll("&&", " ").replaceAll("==", "/") + "/Android/" + Build.DISPLAY + "/" + Build.MODEL + "/" + Build.VERSION.RELEASE + " " + HelperUtils.getUmengMD5(UMUtils.getAppkey(c));`
- `sources/com/umeng/commonsdk/utils/UMUtils.java:767`
  `return locale == null ? Locale.getDefault() : locale;`
- `sources/com/vivo/push/util/j.java:130`
  `String str = Build.MANUFACTURER;`
- `sources/com/vivo/push/util/j.java:132`
  `p.d("Device", "Build.MANUFACTURER is null");`
- `sources/com/vivo/push/util/j.java:135`
  `p.d("Device", "Build.MANUFACTURER is " + str);`
- `sources/com/xiaomi/mipush/sdk/MiPushClient.java:545`
  `long rawOffset = ((TimeZone.getTimeZone("GMT+08").getRawOffset() - TimeZone.getDefault().getRawOffset()) / 1000) / 60;`
- `sources/com/xiaomi/push/service/bk.java:39`
  `builderBuildUpon.appendQueryParameter(com.umeng.analytics.pro.am.x, id.a(Build.MODEL + Constants.COLON_SEPARATOR + Build.VERSION.INCREMENTAL));`
- `sources/com/xiaomi/push/service/p.java:204`
  `map.put("model", Build.MODEL);`
- `sources/com/xiaomi/push/service/p.java:224`
  `map2.put("model", Build.MODEL);`
- `sources/com/xiaomi/push/service/u.java:69`
  `aVar2.a(Constants.APPID, str2).a("locale", Locale.getDefault().toString()).a(MainActivity.SYNC, 1);`
- `sources/com/yuwell/uhealth/data/source/local/CalendarProviderManager.java:39`
  `contentValues.put("calendar_timezone", TimeZone.getDefault().getID());`
- `sources/com/yuwell/uhealth/global/utils/Logger.java:30`
  `appendLog("\n>>>>>>>>>>>>>>>> File Header >>>>>>>>>>>>>>>>\nDevice Manufacturer: " + Build.MANUFACTURER + "\nDevice Model       : " + Build.MODEL + "\nAndroid Version    : " + Build.VERSION.RELEASE + "\nAndroid SDK        : " + Build.VERSION.SDK_INT + "\nApp VersionName    : " + BuildConfig.VERSION_...`
- `sources/com/yuwell/uhealth/view/impl/data/ho/HoHomeFragment.java:508`
  `String str = String.format(Locale.getDefault(), "%02d:%02d", Integer.valueOf(patternBody.timeAlarm / 60), Integer.valueOf(patternBody.timeAlarm % 60));`
- `sources/com/yuwell/uhealth/view/impl/data/ho/HoTimeActivity.java:74`
  `this.mHour.setText(String.format(Locale.getDefault(), "%02d", 0));`
- `sources/com/yuwell/uhealth/view/impl/data/ho/HoTimeActivity.java:75`
  `this.mMinutes.setText(String.format(Locale.getDefault(), "%02d", 0));`
- `sources/com/yuwell/uhealth/view/impl/data/ho/HoTimeActivity.java:79`
  `this.mHour.setText(String.format(Locale.getDefault(), "%02d", Integer.valueOf(i)));`

## BR016

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/AndroidManifest.xml:537`
  `android:name="io.fabric.ApiKey"`
- `resources/AndroidManifest.xml:540`
  `android:name="UMENG_APPKEY"`
- `resources/AndroidManifest.xml:543`
  `android:name="com.amap.api.v2.apikey"`
- `resources/AndroidManifest.xml:677`
  `android:name="JPUSH_APPKEY"`
- `resources/AndroidManifest.xml:703`
  `android:name="com.vivo.push.api_key"`
- `resources/AndroidManifest.xml:734`
  `android:name="OPPO_APPKEY"`
- `resources/AndroidManifest.xml:746`
  `android:name="XIAOMI_APPKEY"`
- `resources/AndroidManifest.xml:996`
  `android:name="appkey"`
- `sources/cn/jiguang/am/c.java:156`
  `cn.jiguang.r.a.f("JDataConfigManager", "request data config failed because can't get appKey");`
- `sources/cn/jiguang/android/BuildConfig.java:8`
  `public static final String CUSTOM_APP_KEY = "";`
- `sources/cn/jiguang/ax/a.java:197`
  `cn.jiguang.bd.d.n("CheckManifestHelper", "errorcode:10001,metadata: JCore appKey - not defined in manifest");`
- `sources/cn/jiguang/ax/a.java:198`
  `cn.jiguang.f.a.a(context, " 未在manifest中配置AppKey", -1);`
- `sources/cn/jiguang/ax/a.java:204`
  `cn.jiguang.bd.d.n("CheckManifestHelper", "errorcode:1008,Invalid appKey : " + strA + ", Please get your Appkey from JIGUANG web console!");`
- `sources/cn/jiguang/ax/a.java:205`
  `cn.jiguang.f.a.a(context, " AppKey:" + strA + " 是无效的AppKey,请确认与JIGUANG web端的AppKey一致", -1);`
- `sources/cn/jiguang/ax/i.java:97`
  `cn.jiguang.bd.d.i("JSslCertUpdateManager", "appKey is empty, return");`
- `sources/cn/jiguang/ax/i.java:105`
  `jSONObject.put("appkey", strA);`
- `sources/cn/jiguang/az/i.java:422`
  `jSONObject.put("jg_app_key", f.m(context));`
- `sources/cn/jiguang/bd/a.java:83`
  `httpRequest.setRequestProperty("X-Http-Appkey", strA);`
- `sources/cn/jiguang/bi/c.java:41`
  `cn.jiguang.bd.d.h("ConnectingHelper", "Login with - juid:" + jF + ", appKey:" + strE + ", sdkVersion:" + strF + ", pluginPlatformType:" + ((int) bA));`
- `sources/cn/jiguang/bi/c.java:173`
  `str = " 非android AppKey";`
- `sources/cn/jiguang/bq/i.java:101`
  `httpRequest.setRequestProperty("X-Http-Appkey", strA);`
- `sources/cn/jiguang/bq/i.java:123`
  `cn.jiguang.bd.d.i("SentryEntryHelper", "request sentry sample failed because can't get appKey");`
- `sources/cn/jiguang/f/a.java:249`
  `Notification.Builder when = new Notification.Builder(context.getApplicationContext()).setContentTitle("Jiguang提示：包名和AppKey不匹配").setContentText("请到 Portal 上获取您的包名和AppKey并更新AndroidManifest相应字段").setContentIntent(broadcast).setSmallIcon(i3).setTicker(str).setWhen(jCurrentTimeMillis);`
- `sources/cn/jiguang/f/a.java:262`
  `e.a(notification2, "setLatestEventInfo", new Object[]{context, "Jiguang提示：包名和AppKey不匹配", "请到 Portal 上获取您的包名和AppKey并更新AndroidManifest相应字段", broadcast}, new Class[]{Context.class, CharSequence.class, CharSequence.class, PendingIntent.class});`
- `sources/cn/jiguang/g/a.java:74`
  `return new a<>(b, "device_config_appkey", "");`
- `sources/cn/jiguang/internal/JConstants.java:13`
  `public static String APP_KEY = "";`
- `sources/cn/jpush/android/ac/c.java:392`
  `Logger.dd("ThirdPushManager", "[refreshToken] third disabled");`
- `sources/cn/jpush/android/ac/c.java:398`
  `Logger.w("ThirdPushManager", "refreshToken romtype is <= 0");`
- `sources/cn/jpush/android/ac/c.java:401`
  `Logger.dd("ThirdPushManager", "[refreshToken] romType: " + ((int) bByteValue));`
- `sources/cn/jpush/android/api/JPushInterface.java:48`
  `public static final String EXTRA_APP_KEY = "cn.jpush.android.APPKEY";`
- `sources/cn/jpush/android/api/JThirdPlatFormInterface.java:37`
  `public static final String KEY_VENDOR_PUSH_APP_KEY_MISS = "j10000";`
- `sources/cn/jpush/android/h/a.java:42`
  `jSONObject.put("JPUSH_APPKEY", str);`
- `sources/cn/jpush/android/helper/a.java:223`
  `intent.putExtra(JPushInterface.EXTRA_APP_KEY, customMessage.senderId);`
- `sources/cn/jpush/android/l/a.java:589`
  `cn.jpush.android.d.b.a(context2, 2, string6, string4, TextUtils.isEmpty(string5) ? JCoreHelper.getAppKey(context2) : string5, 0L, b);`
- `sources/cn/jpush/android/thirdpush/vivo/a.java:202`
  `c = bundle.getString("com.vivo.push.api_key");`
- `sources/cn/jpush/android/thirdpush/vivo/a.java:206`
  `Logger.w("VivoPushHelper", "metadata: com.vivo.push.api_key - not defined in manifest");`
- `sources/com/alipay/sdk/cons/b.java:12`
  `public static final String h = "app_key";`
- `sources/com/alipay/sdk/sys/a.java:28`
  `public static final String o = "appkey";`
- `sources/com/alipay/security/mobile/module/http/model/c.java:8`
  `public static final String o = "APPKEY_ERROR";`
- `sources/com/contec/verify/ContecFoetalEncryptUtils.java:11`
  `private native int getAppKey(byte[] bArr, byte[] bArr2, byte[] bArr3);`
- `sources/com/heytap/mcssdk/constant/b.java:34`
  `public static final String z = "appKey";`
- `sources/com/heytap/msp/push/mode/ErrorCode.java:9`
  `public static final int INVALID_APP_KEY = 14;`
- `sources/com/heytap/msp/push/mode/ErrorCode.java:17`
  `public static final int MISSING_APP_KEY = 15;`
- `sources/com/umeng/analytics/pro/am.java:109`
  `public static final String k = "appkey";`
- `sources/com/umeng/analytics/pro/am.java:111`
  `public static final String m = "secret";`
- `sources/com/umeng/analytics/pro/d.java:31`
  `public static final String a = "appkey";`
- `sources/com/umeng/analytics/pro/d.java:59`
  `public static final String c = "secret";`
- `sources/com/umeng/commonsdk/UMConfigure.java:586`
  `Method declaredMethod10 = cls3.getDeclaredMethod("setMessageAppKey", String.class);`
- `sources/com/umeng/commonsdk/UMConfigure.java:589`
  `declaredMethod10.invoke(objInvoke2, sAppkey);`
- `sources/com/umeng/commonsdk/UMConfigure.java:606`
  `Log.i("UMConfigure", "push secret is " + str3);`
- `sources/com/umeng/commonsdk/UMConfigure.java:622`
  `l(clsD3, "APPKEY", sAppkey);`
- `sources/com/umeng/commonsdk/UMConfigure.java:665`
  `declaredMethod14.invoke(null, applicationContext, sAppkey, sChannel, Integer.valueOf(i2), str3);`
- `sources/com/umeng/commonsdk/UMConfigure.java:673`
  `declaredMethod15.invoke(null, applicationContext, sAppkey);`
- `sources/com/umeng/commonsdk/debug/UMLogCommon.java:6`
  `public static final String SC_10004 = "PUSH AppKey设置成功";`
- `sources/com/umeng/commonsdk/debug/UMLogCommon.java:8`
  `public static final String SC_10006 = "Share AppKey设置成功";`
- `sources/com/umeng/commonsdk/debug/UMLogCommon.java:9`
  `public static final String SC_10008 = "AppKey改变!!!";`
- `sources/com/umeng/commonsdk/debug/UMLogCommon.java:12`
  `public static final String SC_10011 = "请注意：您init接口中设置的AppKey是@，manifest中设置的AppKey是#，init接口设置的AppKey会覆盖manifest中设置的AppKey";`
- `sources/com/umeng/commonsdk/debug/UMLogCommon.java:31`
  `public static final String SC_10007 = "AppKey不能为空|您必须正确设置AppKey，如何正确初始化请详见地址：" + UMLogUtils.makeUrl("67292");`
- `sources/com/umeng/commonsdk/internal/c.java:183`
  `jSONObject.put(com.umeng.commonsdk.statistics.b.a("appkey"), UMGlobalContext.getInstance(context).getAppkey());`
- `sources/com/umeng/commonsdk/internal/c.java:207`
  `jSONObject.put(com.umeng.commonsdk.statistics.b.a("appkey"), UMGlobalContext.getInstance(context).getAppkey());`
- `sources/com/umeng/commonsdk/internal/c.java:288`
  `String appkey = UMUtils.getAppkey(context);`
- `sources/com/umeng/commonsdk/internal/c.java:295`
  `declaredMethod.invoke(objInvoke, applicationContext, appkey, null);`
- `sources/com/umeng/commonsdk/statistics/b.java:57`
  `f.put("appkey", "#ak");`
- `sources/com/vivo/push/b/b.java:22`
  `aVar.a("BaseAppCommand.EXTRA_APPKEY", this.b);`
- `sources/com/vivo/push/b/b.java:44`
  `this.b = aVar.a("BaseAppCommand.EXTRA_APPKEY");`
- `sources/com/youzan/androidsdk/account/Token.java:17`
  `public static String getAccessToken() {`
- `sources/com/youzan/androidsdk/account/Token.java:18`
  `return Preference.instance().getString("token.access_token", null);`
- `sources/com/youzan/androidsdk/account/Token.java:42`
  `Preference.instance().setString("token.access_token", str);`
- `sources/com/youzan/spiderman/c/e/d.java:49`
  `map.put("access_token", str2);`
- `sources/com/yuwell/uhealth/data/source/HoDeviceRepository.java:29`
  `return this.a.bindingDevice(PreferenceSource.getAccessToken(), PreferenceSource.getAccessToken(), bindingDeviceReq);`
- `sources/com/yuwell/uhealth/data/source/HoDeviceRepository.java:58`
  `return this.a.setAnion(PreferenceSource.getAccessToken(), str, i);`
- `sources/com/yuwell/uhealth/data/source/HoDeviceRepository.java:75`
  `return this.a.setVoice(PreferenceSource.getAccessToken(), str, i);`
- `sources/com/yuwell/uhealth/data/source/HoDeviceRepository.java:80`
  `return this.a.unBindingDevice(PreferenceSource.getAccessToken(), PreferenceSource.getAccessToken(), unbindingDeviceReq);`
- `sources/com/yuwell/uhealth/data/source/local/PreferenceSource.java:69`
  `String accessToken = getAccessToken();`
- `sources/com/yuwell/uhealth/data/source/local/PreferenceSource.java:70`
  `if (TextUtils.isEmpty(accessToken)) {`
- `sources/com/yuwell/uhealth/data/source/local/PreferenceSource.java:315`
  `public static void setAccessToken(String str) {`
- `sources/com/yuwell/uhealth/data/source/local/PreferenceSource.java:476`
  `public static void setRefreshToken(String str) {`
- `sources/com/yuwell/uhealth/data/source/remote/AccountAPI.java:31`
  `@POST("api/account/refreshtoken")`
- `sources/com/yuwell/uhealth/data/source/remote/AccountAPI.java:32`
  `Call<Ret<RefreshTokenData>> refreshToken(@Header(HttpHeaders.AUTHORIZATION) String str, @Body RefreshTokenRequest refreshTokenRequest);`
- `sources/com/yuwell/uhealth/global/GlobalConstant.java:33`
  `public static String UDESK_APPKEY = "ab703d16e072d145fc913c68d0a0bddc";`

## BR017

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `sources/cn/jiguang/af/b.java:19`
  `cn.jiguang.r.a.f("", "Unexpected - failed to AES encrypt.");`
- `sources/cn/jiguang/af/b.java:45`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(c(str, "UTF-8"), "AES");`
- `sources/cn/jiguang/af/b.java:46`
  `IvParameterSpec ivParameterSpecA = a(str2.getBytes("UTF-8"));`
- `sources/cn/jiguang/af/b.java:47`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/cn/jiguang/af/b.java:48`
  `cipher.init(z ? 1 : 2, secretKeySpec, ivParameterSpecA);`
- `sources/cn/jiguang/af/b.java:56`
  `cn.jiguang.r.a.f("", "Unexpected - failed to AES decrypt.");`
- `sources/cn/jiguang/az/f.java:84`
  `return cn.jiguang.ca.f.b(str, c(), "RSA/ECB/PKCS1Padding");`
- `sources/cn/jiguang/be/a.java:20`
  `d.c("CryptoUtils", "doCrypto cipherMode is " + i + ", key is " + str + ", IvParameterSpec is " + strSubstring + ", inputFile is " + file.getAbsolutePath() + ", outputFile is " + file2.getAbsolutePath());`
- `sources/cn/jiguang/be/a.java:21`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(str.getBytes(), "AES");`
- `sources/cn/jiguang/be/a.java:22`
  `IvParameterSpec ivParameterSpec = new IvParameterSpec(strSubstring.getBytes());`
- `sources/cn/jiguang/be/a.java:23`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/cn/jiguang/be/a.java:24`
  `cipher.init(i, secretKeySpec, ivParameterSpec);`
- `sources/cn/jiguang/c/a.java:61`
  `JSONObject jSONObject = new JSONObject(f.b(bundle.getString("aes"), cn.jiguang.a.a.i));`
- `sources/cn/jiguang/ca/f.java:80`
  `cn.jiguang.bd.d.i("", "Unexpected - failed to AES encrypt.");`
- `sources/cn/jiguang/ca/f.java:104`
  `cipher = Cipher.getInstance(str2);`
- `sources/cn/jiguang/ca/f.java:113`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(c(str, "UTF-8"), "AES");`
- `sources/cn/jiguang/ca/f.java:114`
  `IvParameterSpec ivParameterSpecA = a(str2.getBytes("UTF-8"));`
- `sources/cn/jiguang/ca/f.java:115`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/cn/jiguang/ca/f.java:116`
  `cipher.init(z ? 1 : 2, secretKeySpec, ivParameterSpecA);`
- `sources/cn/jiguang/f/f.java:68`
  `return MessageDigest.getInstance(AppSigning.MD5).digest(bArr);`
- `sources/cn/jiguang/f/f.java:76`
  `MessageDigest messageDigest = MessageDigest.getInstance(AppSigning.MD5);`
- `sources/cn/jiguang/f/f.java:82`
  `byte[] bArrDigest = messageDigest.digest(bArr);`
- `sources/cn/jiguang/f/f.java:99`
  `byte[] bArrDigest = MessageDigest.getInstance(AppSigning.MD5).digest(str.getBytes("utf-8"));`
- `sources/cn/jiguang/f/f.java:160`
  `MessageDigest messageDigest = MessageDigest.getInstance(AppSigning.MD5);`
- `sources/cn/jiguang/f/f.java:161`
  `messageDigest.update(str.getBytes());`
- `sources/cn/jiguang/f/f.java:162`
  `return a(messageDigest.digest());`
- `sources/cn/jiguang/w/f.java:67`
  `MessageDigest messageDigest = MessageDigest.getInstance(AppSigning.MD5);`
- `sources/cn/jiguang/w/f.java:68`
  `messageDigest.update(str.getBytes());`
- `sources/cn/jiguang/w/f.java:69`
  `return a(messageDigest.digest());`
- `sources/cn/jpush/android/ab/d.java:214`
  `Logger.d("TagAliasOperator", "pros des  failed - error:" + th2);`
- `sources/com/alibaba/sdk/android/oss/common/auth/HmacSHA1Signature.java:9`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/alibaba/sdk/android/oss/common/auth/HmacSHA1Signature.java:12`
  `public class HmacSHA1Signature {`
- `sources/com/alibaba/sdk/android/oss/common/utils/BinaryUtil.java:29`
  `MessageDigest messageDigest = MessageDigest.getInstance(AppSigning.MD5);`
- `sources/com/alibaba/sdk/android/oss/common/utils/BinaryUtil.java:36`
  `return messageDigest.digest();`
- `sources/com/alibaba/sdk/android/oss/common/utils/BinaryUtil.java:56`
  `MessageDigest messageDigest = MessageDigest.getInstance("SHA-1");`
- `sources/com/alibaba/sdk/android/oss/common/utils/BinaryUtil.java:61`
  `messageDigest.update(bArr, 0, i);`
- `sources/com/alibaba/sdk/android/oss/common/utils/BinaryUtil.java:148`
  `MessageDigest messageDigest = MessageDigest.getInstance("SHA-1");`
- `sources/com/alibaba/sdk/android/oss/common/utils/BinaryUtil.java:153`
  `messageDigest.update(bArr, 0, i);`
- `sources/com/alibaba/sdk/android/oss/common/utils/BinaryUtil.java:190`
  `MessageDigest messageDigest = MessageDigest.getInstance(AppSigning.MD5);`
- `sources/com/alibaba/sdk/android/oss/common/utils/BinaryUtil.java:196`
  `messageDigest.update(bArr, 0, i);`
- `sources/com/alipay/mobile/common/logging/render/PendingRender.java:136`
  `des = str;`
- `sources/com/alipay/mobile/common/logging/render/PendingRender.java:138`
  `if (strA == null || (length = strA.getBytes().length) <= 16384 || a.contains(des) || !LogLengthConfig.a().b()) {`
- `sources/com/alipay/mobile/common/logging/render/PendingRender.java:143`
  `behavor4.setParam1(des);`
- `sources/com/alipay/mobile/common/logging/util/MD5Util.java:28`
  `MessageDigest messageDigest = MessageDigest.getInstance("md5");`
- `sources/com/alipay/mobile/common/logging/util/MD5Util.java:29`
  `messageDigest.update(str.getBytes("UTF8"));`
- `sources/com/alipay/mobile/common/logging/util/MD5Util.java:30`
  `return a(messageDigest.digest());`
- `sources/com/alipay/mobile/common/logging/util/RSAUtil.java:39`
  `java.lang.String r2 = "RSA"`
- `sources/com/alipay/mobile/common/logging/util/RSAUtil.java:41`
  `java.lang.String r2 = "RSA/ECB/PKCS1Padding"`
- `sources/com/alipay/mobile/common/logging/util/RSAUtil.java:42`
  `javax.crypto.Cipher r2 = javax.crypto.Cipher.getInstance(r2)     // Catch: java.lang.Throwable -> L45 java.lang.Exception -> L47`
- `sources/com/alipay/mobile/common/logging/util/RSAUtil.java:121`
  `java.lang.String r2 = "RSA"`
- `sources/com/alipay/mobile/common/logging/util/RSAUtil.java:123`
  `java.lang.String r2 = "RSA/ECB/PKCS1Padding"`
- `sources/com/alipay/mobile/common/logging/util/RSAUtil.java:124`
  `javax.crypto.Cipher r2 = javax.crypto.Cipher.getInstance(r2)     // Catch: java.lang.Throwable -> L45 java.lang.Exception -> L47`
- `sources/com/alipay/mobile/mascanengine/imagetrace/sec/MD5Util.java:34`
  `MessageDigest messageDigest = MessageDigest.getInstance("md5");`
- `sources/com/alipay/mobile/mascanengine/imagetrace/sec/MD5Util.java:35`
  `messageDigest.update(str.getBytes("UTF8"));`
- `sources/com/alipay/mobile/mascanengine/imagetrace/sec/MD5Util.java:36`
  `return a(messageDigest.digest());`
- `sources/com/alipay/mobile/mascanengine/imagetrace/sec/RSAUtil.java:45`
  `java.lang.String r2 = "RSA"`
- `sources/com/alipay/mobile/mascanengine/imagetrace/sec/RSAUtil.java:47`
  `java.lang.String r2 = "RSA/ECB/PKCS1Padding"`
- `sources/com/alipay/mobile/mascanengine/imagetrace/sec/RSAUtil.java:48`
  `javax.crypto.Cipher r2 = javax.crypto.Cipher.getInstance(r2)     // Catch: java.lang.Throwable -> L45 java.lang.Exception -> L47`
- `sources/com/alipay/mobile/mascanengine/imagetrace/sec/RSAUtil.java:127`
  `java.lang.String r2 = "RSA"`
- `sources/com/alipay/mobile/mascanengine/imagetrace/sec/RSAUtil.java:129`
  `java.lang.String r2 = "RSA/ECB/PKCS1Padding"`
- `sources/com/alipay/mobile/mascanengine/imagetrace/sec/RSAUtil.java:130`
  `javax.crypto.Cipher r2 = javax.crypto.Cipher.getInstance(r2)     // Catch: java.lang.Throwable -> L45 java.lang.Exception -> L47`
- `sources/com/alipay/sdk/encrypt/d.java:9`
  `public static final String a = "RSA";`
- `sources/com/alipay/sdk/encrypt/d.java:20`
  `java.lang.String r1 = "RSA"`
- `sources/com/alipay/sdk/encrypt/d.java:22`
  `java.lang.String r1 = "RSA/ECB/PKCS1Padding"`
- `sources/com/alipay/sdk/encrypt/d.java:23`
  `javax.crypto.Cipher r1 = javax.crypto.Cipher.getInstance(r1)     // Catch: java.lang.Throwable -> L3f java.lang.Exception -> L41`
- `sources/com/alipay/sdk/encrypt/e.java:4`
  `import javax.crypto.spec.IvParameterSpec;`
- `sources/com/alipay/sdk/encrypt/e.java:5`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/alipay/sdk/encrypt/e.java:13`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(str.getBytes(), "DESede");`
- `sources/com/alipay/sdk/encrypt/e.java:14`
  `Cipher cipher = Cipher.getInstance(a);`
- `sources/com/alipay/sdk/encrypt/e.java:15`
  `cipher.init(2, secretKeySpec, new IvParameterSpec(c.a(cipher, str2)));`
- `sources/com/alipay/sdk/encrypt/e.java:24`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(str.getBytes(), "DESede");`
- `sources/com/alipay/sdk/encrypt/e.java:25`
  `Cipher cipher = Cipher.getInstance(a);`
- `sources/com/alipay/sdk/encrypt/e.java:26`
  `cipher.init(1, secretKeySpec, new IvParameterSpec(c.a(cipher, str2)));`
- `sources/com/alipay/sdk/packet/e.java:25`
  `public static final String i = "des-mode";`
- `sources/com/alipay/sdk/util/l.java:603`
  `MessageDigest messageDigest = MessageDigest.getInstance("SHA-256");`
- `sources/com/alipay/sdk/util/l.java:604`
  `messageDigest.update(str.getBytes());`
- `sources/com/alipay/sdk/util/l.java:605`
  `byte[] bArrDigest = messageDigest.digest();`
- `sources/com/alipay/security/mobile/module/a/a.java:83`
  `MessageDigest messageDigest = MessageDigest.getInstance("SHA-1");`
- `sources/com/alipay/security/mobile/module/a/a.java:84`
  `messageDigest.update(str.getBytes("UTF-8"));`
- `sources/com/alipay/security/mobile/module/a/a.java:85`
  `byte[] bArrDigest = messageDigest.digest();`

## BR018

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/cn/jiguang/api/JProtocol.java:130`
  `sb.append(this.isRequest ? "[Request]" : "[Response]");`
- `sources/cn/jiguang/api/JResponse.java:7`
  `public abstract class JResponse extends JProtocol {`
- `sources/cn/jiguang/api/JResponse.java:10`
  `public JResponse(int i, int i2, long j, long j2, int i3, String str) {`
- `sources/cn/jiguang/api/JResponse.java:15`
  `public JResponse(Object obj, ByteBuffer byteBuffer) {`
- `sources/cn/jiguang/api/JResponse.java:19`
  `public JResponse(ByteBuffer byteBuffer, byte[] bArr) {`
- `sources/cn/jiguang/api/JResponse.java:32`
  `return "JResponse{code=" + this.code + '}';`
- `sources/cn/jiguang/api/utils/ByteBufferUtils.java:3`
  `import cn.jiguang.api.JResponse;`
- `sources/cn/jiguang/api/utils/ByteBufferUtils.java:14`
  `private static String generalExtraStr(Throwable th, JResponse jResponse, ByteBuffer byteBuffer) {`
- `sources/cn/jiguang/api/utils/ByteBufferUtils.java:16`
  `if (jResponse != null) {`
- `sources/cn/jiguang/api/utils/ByteBufferUtils.java:17`
  `sb.append(jResponse.toString());`
- `sources/cn/jiguang/api/utils/ByteBufferUtils.java:39`
  `public static java.lang.Byte get(java.nio.ByteBuffer r1, cn.jiguang.api.JResponse r2) {`
- `sources/cn/jiguang/api/utils/ByteBufferUtils.java:64`
  `throw new UnsupportedOperationException("Method not decompiled: cn.jiguang.api.utils.ByteBufferUtils.get(java.nio.ByteBuffer, cn.jiguang.api.JResponse):java.lang.Byte");`
- `sources/cn/jiguang/api/utils/ByteBufferUtils.java:73`
  `public static java.nio.ByteBuffer get(java.nio.ByteBuffer r0, byte[] r1, cn.jiguang.api.JResponse r2) {`
- `sources/cn/jiguang/api/utils/ByteBufferUtils.java:97`
  `throw new UnsupportedOperationException("Method not decompiled: cn.jiguang.api.utils.ByteBufferUtils.get(java.nio.ByteBuffer, byte[], cn.jiguang.api.JResponse):java.nio.ByteBuffer");`
- `sources/cn/jiguang/api/utils/ByteBufferUtils.java:106`
  `public static int getInt(java.nio.ByteBuffer r1, cn.jiguang.api.JResponse r2) {`
- `sources/cn/jiguang/api/utils/ByteBufferUtils.java:130`
  `throw new UnsupportedOperationException("Method not decompiled: cn.jiguang.api.utils.ByteBufferUtils.getInt(java.nio.ByteBuffer, cn.jiguang.api.JResponse):int");`
- `sources/cn/jiguang/api/utils/ByteBufferUtils.java:139`
  `public static long getLong(java.nio.ByteBuffer r1, cn.jiguang.api.JResponse r2) {`
- `sources/cn/jiguang/api/utils/ByteBufferUtils.java:163`
  `throw new UnsupportedOperationException("Method not decompiled: cn.jiguang.api.utils.ByteBufferUtils.getLong(java.nio.ByteBuffer, cn.jiguang.api.JResponse):long");`
- `sources/cn/jiguang/api/utils/ByteBufferUtils.java:172`
  `public static short getShort(java.nio.ByteBuffer r1, cn.jiguang.api.JResponse r2) {`
- `sources/cn/jiguang/api/utils/ByteBufferUtils.java:196`
  `throw new UnsupportedOperationException("Method not decompiled: cn.jiguang.api.utils.ByteBufferUtils.getShort(java.nio.ByteBuffer, cn.jiguang.api.JResponse):short");`
- `sources/cn/jiguang/api/utils/ByteBufferUtils.java:199`
  `private static void onException(Throwable th, JResponse jResponse, ByteBuffer byteBuffer) {`
- `sources/cn/jiguang/api/utils/ByteBufferUtils.java:200`
  `generalExtraStr(th, jResponse, byteBuffer);`
- `sources/cn/jiguang/api/utils/ProtocolUtil.java:3`
  `import cn.jiguang.api.JResponse;`
- `sources/cn/jiguang/api/utils/ProtocolUtil.java:97`
  `public static String getTlv2(ByteBuffer byteBuffer, JResponse jResponse) {`
- `sources/cn/jiguang/api/utils/ProtocolUtil.java:98`
  `int i = ByteBufferUtils.getShort(byteBuffer, jResponse);`
- `sources/cn/jiguang/api/utils/ProtocolUtil.java:104`
  `ByteBufferUtils.get(byteBuffer, bArr, jResponse);`
- `sources/cn/jpush/android/api/SystemAlertHelper.java:40`
  `Logger.d("SystemAlertHelper", "height : " + displayMetrics.heightPixels);`
- `sources/cn/jpush/android/api/SystemAlertHelper.java:56`
  `int i4 = displayMetricsA.heightPixels / 2;`
- `sources/cn/jpush/android/api/SystemAlertHelper.java:70`
  `layoutParams.height = b;`
- `sources/cn/jpush/android/api/SystemAlertHelper.java:77`
  `layoutParams.height = -2;`
- `sources/cn/jpush/android/api/SystemAlertHelper.java:116`
  `public static int getWindowHeight() {`
- `sources/cn/udesk/photoselect/entity/LocalMedia.java:53`
  `public int getHeight() {`
- `sources/cn/udesk/photoselect/entity/LocalMedia.java:85`
  `public void setHeight(int i) {`
- `sources/com/airbnb/lottie/model/layer/BaseLayer.java:373`
  `this.h.set(Camera2ConfigurationUtils.MIN_ZOOM_RATE, Camera2ConfigurationUtils.MIN_ZOOM_RATE, canvas.getWidth(), canvas.getHeight());`
- `sources/com/airbnb/lottie/model/layer/ImageLayer.java:66`
  `this.x.set(0, 0, bitmapR.getWidth(), bitmapR.getHeight());`
- `sources/com/airbnb/lottie/model/layer/ImageLayer.java:67`
  `this.y.set(0, 0, (int) (bitmapR.getWidth() * fDpScale), (int) (bitmapR.getHeight() * fDpScale));`
- `sources/com/airbnb/lottie/model/layer/ImageLayer.java:76`
  `rectF.set(rectF.left, rectF.top, Math.min(rectF.right, r6.getWidth()), Math.min(rectF.bottom, r6.getHeight()));`
- `sources/com/airbnb/lottie/parser/LayerParser.java:30`
  `return new Layer(Collections.emptyList(), lottieComposition, "__container", -1L, Layer.LayerType.PreComp, -1L, null, Collections.emptyList(), new AnimatableTransform(), 0, 0, 0, Camera2ConfigurationUtils.MIN_ZOOM_RATE, Camera2ConfigurationUtils.MIN_ZOOM_RATE, bounds.width(), bounds.height(), null, n...`
- `sources/com/alibaba/sdk/android/oss/model/ListMultipartUploadsResult.java:6`
  `import com.alibaba.sdk.android.oss.internal.ResponseMessage;`
- `sources/com/alibaba/sdk/android/oss/model/ListMultipartUploadsResult.java:77`
  `public ListMultipartUploadsResult parseData(ResponseMessage responseMessage) throws Exception {`

## BR019

paper_id: B011
paper_title: Locking it down: The privacy and security of mobile medication apps

- `sources/androidx/appcompat/widget/ActivityChooserModel.java:140`
  `map.put(new ComponentName(activityInfo.packageName, activityInfo.name), activityResolveInfo);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:718`
  `this.a.put(getId(), this);`
- `sources/androidx/core/graphics/c.java:122`
  `simpleArrayMap.put(uri, byteBufferMmap);`
- `sources/androidx/transition/ChangeBounds.java:307`
  `transitionValues.values.put("android:changeBounds:bounds", new Rect(view.getLeft(), view.getTop(), view.getRight(), view.getBottom()));`
- `sources/androidx/transition/ChangeClipBounds.java:42`
  `transitionValues.values.put("android:clipBounds:clip", clipBounds);`
- `sources/androidx/transition/ChangeClipBounds.java:44`
  `transitionValues.values.put("android:clipBounds:bounds", new Rect(0, 0, view.getWidth(), view.getHeight()));`
- `sources/androidx/transition/Explode.java:32`
  `transitionValues.values.put("android:explode:screenBounds", new Rect(i, i2, view.getWidth() + i, view.getHeight() + i2));`
- `sources/androidx/transition/VisibilityPropagation.java:31`
  `transitionValues.values.put("android:visibilityPropagation:center", iArr);`
- `sources/cn/jiguang/ad/d.java:96`
  `jSONObject.put("battery_level", a(intentF));`
- `sources/cn/jiguang/ad/d.java:97`
  `jSONObject.put("charging", b(intentF));`
- `sources/cn/jiguang/ad/d.java:98`
  `jSONObject.put("battery_temperature", c(intentF));`
- `sources/cn/jiguang/ad/d.java:101`
  `jSONObject.put("online", i != 1 ? i != 2 ? null : Boolean.TRUE : Boolean.FALSE);`
- `sources/cn/jiguang/ad/d.java:110`
  `jSONObject.put("screen_width_pixels", displayMetricsH.widthPixels);`
- `sources/cn/jiguang/ad/d.java:111`
  `jSONObject.put("screen_height_pixels", displayMetricsH.heightPixels);`
- `sources/cn/jiguang/ad/d.java:112`
  `jSONObject.put("screen_density", displayMetricsH.density);`
- `sources/cn/jiguang/ad/d.java:113`
  `jSONObject.put("screen_dpi", displayMetricsH.densityDpi);`
- `sources/cn/jiguang/ae/d.java:64`
  `private static JSONObject a(Bundle bundle) {`
- `sources/cn/jiguang/an/c.java:62`
  `this.b = new JSONObject();`
- `sources/cn/jiguang/an/c.java:65`
  `this.b.put("scale", intExtra2);`
- `sources/cn/jiguang/an/c.java:66`
  `this.b.put("status", intExtra3);`
- `sources/cn/jiguang/an/c.java:67`
  `this.b.put("voltage", intExtra4);`
- `sources/cn/jiguang/an/c.java:68`
  `this.b.put("temperature", intExtra5);`
- `sources/cn/jiguang/an/e.java:69`
  `aVar.a(i.b(jSONObject.toString(), true));`
- `sources/cn/jiguang/an/e.java:122`
  `String strOptString = new JSONObject(strA).optString("ipv6", "");`
- `sources/cn/jiguang/analytics/page/PushSA.java:33`
  `private JSONObject flow_cache = null;`
- `sources/cn/jiguang/ao/a.java:321`
  `jSONObject.put("modelnumber", aVarA.c);`
- `sources/cn/jiguang/ao/a.java:324`
  `jSONObject.put("basebandversion", aVarA.d);`
- `sources/cn/jiguang/ao/a.java:326`
  `jSONObject.put("buildnumber", aVarA.e);`
- `sources/cn/jiguang/ax/g.java:56`
  `cn.jiguang.bf.g gVarA = cn.jiguang.bf.b.a(str2, jSONObject.toString(), context, false, 3, 3);`
- `sources/cn/jiguang/ax/h.java:61`
  `cn.jiguang.bf.g gVarA = cn.jiguang.bf.b.a(str2, jSONObject.toString(), context, false, 3, 3);`
- `sources/cn/jiguang/az/f.java:34`
  `public static String a(Context context, String str, JSONObject jSONObject) {`
- `sources/cn/jiguang/az/f.java:65`
  `return jSONObject2.toString();`
- `sources/cn/jiguang/az/f.java:69`
  `JSONObject jSONObject3 = new JSONObject();`
- `sources/cn/jiguang/az/f.java:71`
  `jSONObject3.put("code", -1);`
- `sources/cn/jiguang/az/f.java:72`
  `jSONObject3.put("msg", httpResponseHttpPost);`
- `sources/cn/jiguang/az/f.java:75`
  `return jSONObject3.toString();`
- `sources/cn/jiguang/az/i.java:433`
  `String[] strArrSplit = jSONObjectA.optString(am.z, "").split("\\*");`
- `sources/cn/jiguang/az/i.java:435`
  `jSONObject.put("jg_screen_width", strArrSplit[0]);`
- `sources/cn/jiguang/az/i.java:436`
  `jSONObject.put("jg_screen_height", strArrSplit[1]);`
- `sources/cn/jiguang/az/i.java:438`
  `jSONObject.put("jg_screen_size", jSONObjectA.optString("screensize", ""));`

## BR020

paper_id: B012
paper_title: Reviewing the data security and privacy policies of mobile apps for depression

- `sources/androidx/core/provider/FontsContractCompat.java:458`
  `Cursor cursorQuery = null;`
- `sources/androidx/core/provider/FontsContractCompat.java:460`
  `cursorQuery = Build.VERSION.SDK_INT > 16 ? context.getContentResolver().query(uriBuild, new String[]{aq.d, Columns.FILE_ID, Columns.TTC_INDEX, Columns.VARIATION_SETTINGS, Columns.WEIGHT, Columns.ITALIC, Columns.RESULT_CODE}, "query = ?", new String[]{fontRequest.getQuery()}, null, cancellationSignal...`
- `sources/androidx/core/provider/FontsContractCompat.java:461`
  `if (cursorQuery != null && cursorQuery.getCount() > 0) {`
- `sources/androidx/core/provider/FontsContractCompat.java:462`
  `int columnIndex = cursorQuery.getColumnIndex(Columns.RESULT_CODE);`
- `sources/androidx/core/provider/FontsContractCompat.java:464`
  `int columnIndex2 = cursorQuery.getColumnIndex(aq.d);`
- `sources/androidx/core/provider/FontsContractCompat.java:465`
  `int columnIndex3 = cursorQuery.getColumnIndex(Columns.FILE_ID);`
- `sources/androidx/core/provider/FontsContractCompat.java:466`
  `int columnIndex4 = cursorQuery.getColumnIndex(Columns.TTC_INDEX);`
- `sources/androidx/core/provider/FontsContractCompat.java:467`
  `int columnIndex5 = cursorQuery.getColumnIndex(Columns.WEIGHT);`
- `sources/androidx/core/provider/FontsContractCompat.java:468`
  `int columnIndex6 = cursorQuery.getColumnIndex(Columns.ITALIC);`
- `sources/androidx/core/provider/FontsContractCompat.java:469`
  `while (cursorQuery.moveToNext()) {`
- `sources/androidx/core/provider/FontsContractCompat.java:470`
  `int i = columnIndex != -1 ? cursorQuery.getInt(columnIndex) : 0;`
- `sources/androidx/core/provider/FontsContractCompat.java:471`
  `arrayList2.add(new FontInfo(columnIndex3 == -1 ? ContentUris.withAppendedId(uriBuild, cursorQuery.getLong(columnIndex2)) : ContentUris.withAppendedId(uriBuild2, cursorQuery.getLong(columnIndex3)), columnIndex4 != -1 ? cursorQuery.getInt(columnIndex4) : 0, columnIndex5 != -1 ? cursorQuery.getInt(colu...`
- `sources/cn/jpush/android/r/c.java:42`
  `Logger.d("InAppTplHelper", "use cache template, templateId: " + strD + ", webPagePath: " + str2 + ", totalTemplateCount: " + linkedHashMapA.values().size() + ", update template file time: " + new File(str2).setLastModified(bVar.c));`
- `sources/cn/udesk/db/UdeskDBHelper.java:78`
  `sQLiteDatabase.execSQL("DROP TABLE IF EXISTS udeskAgentMsg");`
- `sources/cn/udesk/db/UdeskDBHelper.java:79`
  `sQLiteDatabase.execSQL("DROP TABLE IF EXISTS sub_sessionid");`
- `sources/cn/udesk/db/UdeskDBHelper.java:80`
  `sQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS " + UdeskSendIngMsgs + "( MsgID TEXT, SendFlag INTEGER, Time BIGINT, primary key(MsgID))");`
- `sources/cn/udesk/db/UdeskDBHelper.java:81`
  `sQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS " + UdeskAgentMsg + "( Receive_AgentJid TEXT, HeadUrl TEXT, AgentNick TEXT, primary key(Receive_AgentJid))");`
- `sources/cn/udesk/db/UdeskDBHelper.java:82`
  `sQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS " + SubSessionId + "( SUBID TEXT primary key, SEQNUM INTEGER)");`
- `sources/cn/udesk/db/UdeskDBHelper.java:83`
  `sQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS TempMessageInfo(MsgID TEXT primary key,Time BIGINT,MsgContent TEXT,MsgType TEXT, ReadFlag INTEGER,SendFlag INTEGER,PlayedFlag INTEGER,Direction INTEGER,LocalPath Text,Duration INTEGER,Receive_AgentJid TEXT,created_at TEXT,updated_at TEXT,reply_user ...`
- `sources/cn/udesk/db/UdeskDBHelper.java:85`
  `sQLiteDatabase.execSQL(" INSERT INTO TempMessageInfo (MsgID,Time,MsgContent,MsgType,ReadFlag,SendFlag,PlayedFlag,Direction,LocalPath,Duration) SELECT MsgID,Time,MsgContent,MsgType,ReadFlag,SendFlag,PlayedFlag,Direction,LocalPath,Duration  FROM udeskMessageInfo ");`
- `sources/cn/udesk/db/UdeskDBHelper.java:87`
  `sQLiteDatabase.execSQL(" INSERT INTO TempMessageInfo (MsgID,Time,MsgContent,MsgType,ReadFlag,SendFlag,PlayedFlag,Direction,LocalPath,Duration,Receive_AgentJid,created_at,reply_user,reply_userurl) SELECT MsgID,Time,MsgContent,MsgType,ReadFlag,SendFlag,PlayedFlag,Direction,LocalPath,Duration,AgentJid,...`
- `sources/cn/udesk/db/UdeskDBHelper.java:89`
  `sQLiteDatabase.execSQL(" INSERT INTO TempMessageInfo (MsgID,Time,MsgContent,MsgType,ReadFlag,SendFlag,PlayedFlag,Direction,LocalPath,Duration) SELECT MsgID,Time,MsgContent,MsgType,ReadFlag,SendFlag,PlayedFlag,Direction,LocalPath,Duration  FROM udeskMessageInfo ");`
- `sources/cn/udesk/db/UdeskDBHelper.java:91`
  `sQLiteDatabase.execSQL("DROP TABLE udeskMessageInfo");`
- `sources/cn/udesk/db/UdeskDBHelper.java:92`
  `sQLiteDatabase.execSQL("ALTER TABLE TempMessageInfo RENAME TO udeskMessageInfo");`
- `sources/com/example/btconfig/R.java:1350`
  `public static final int material_cursor_inset_bottom = 0x7f0700ec;`
- `sources/com/example/btconfig/R.java:1351`
  `public static final int material_cursor_inset_top = 0x7f0700ed;`
- `sources/com/google/android/material/R.java:1343`
  `public static final int material_cursor_inset_bottom = 0x7f0700ec;`
- `sources/com/google/android/material/R.java:1344`
  `public static final int material_cursor_inset_top = 0x7f0700ed;`
- `sources/com/mpaas/aar/demo/custom/R.java:1370`
  `public static final int material_cursor_inset_bottom = 0x7f0700ec;`
- `sources/com/mpaas/aar/demo/custom/R.java:1371`
  `public static final int material_cursor_inset_top = 0x7f0700ed;`
- `sources/com/mpaas/ocr/biz/api/R.java:101`
  `public static final int AU_CURSOR_WIDTH = com.mpaas.ocr.R.dimen.AU_CURSOR_WIDTH;`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:520`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/openTypeWebview"), null, null, new String[]{this.appId, String.valueOf(1), String.valueOf(req.scene), req.templateID, req.reserved}, null);`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:521`
  `if (cursorQuery != null) {`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:522`
  `cursorQuery.close();`
- `sources/com/theartofdev/edmodo/cropper/BitmapUtils.java:5`
  `import android.database.Cursor;`
- `sources/com/yuwell/uhealth/R.java:2273`
  `public static final int material_cursor_inset_bottom = 0x7f0700ec;`
- `sources/com/yuwell/uhealth/R.java:2274`
  `public static final int material_cursor_inset_top = 0x7f0700ed;`
- `sources/com/yuwell/uhealth/R.java:4698`
  `public static final int ptr_classic_header_rotate_view_header_last_update = 0x7f0903a5;`
- `sources/com/yuwell/uhealth/R.java:5015`
  `public static final int text_update = 0x7f0904e2;`
- `sources/com/yuwell/uhealth/data/model/database/dao/BPMeasurementDAO.java:93`
  `cursorExecQuery.close();`

## BR021

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `resources/AndroidManifest.xml:527`
  `<provider`
- `resources/AndroidManifest.xml:645`
  `<provider`
- `resources/AndroidManifest.xml:679`
  `<provider`
- `resources/AndroidManifest.xml:800`
  `<provider`
- `resources/AndroidManifest.xml:887`
  `<provider`
- `resources/AndroidManifest.xml:896`
  `<provider`
- `resources/AndroidManifest.xml:905`
  `<provider`
- `resources/AndroidManifest.xml:914`
  `<provider`
- `resources/AndroidManifest.xml:923`
  `<provider`

## BR022

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `resources/res/xml/file_paths.xml:3`
  `<cache-path`
- `resources/res/xml/file_paths.xml:6`
  `<external-cache-path`
- `resources/res/xml/file_paths.xml:9`
  `<external-cache-path`
- `resources/res/xml/file_paths.xml:12`
  `<external-path`
- `resources/res/xml/file_paths.xml:15`
  `<external-path`
- `resources/res/xml/file_paths.xml:18`
  `<files-path`
- `resources/res/xml/file_paths.xml:21`
  `<cache-path`
- `resources/res/xml/file_paths.xml:24`
  `<external-files-path`
- `resources/res/xml/file_paths.xml:27`
  `<external-cache-path`
- `resources/res/xml/file_paths.xml:30`
  `<root-path`
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
- `resources/res/xml/udesk_provider_paths_external.xml:3`
  `<external-path name="my_external"/>`
- `resources/res/xml/udesk_provider_paths_external_cache.xml:3`
  `<external-cache-path name="my_external"/>`
- `resources/res/xml/udesk_provider_paths_external_file.xml:3`
  `<external-files-path name="my_external"/>`
- `resources/res/xml/udesk_provider_paths_internal_cache.xml:3`
  `<cache-path name="my_external"/>`
- `resources/res/xml/udesk_provider_paths_internal_file.xml:3`
  `<files-path name="my_external"/>`

## BR023

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `sources/androidx/lifecycle/ProcessLifecycleOwnerInitializer.java:13`
  `public class ProcessLifecycleOwnerInitializer extends ContentProvider {`
- `sources/cn/jpush/android/ad/a.java:121`
  `int i2 = Service.class.isAssignableFrom(cls) ? 4 : BroadcastReceiver.class.isAssignableFrom(cls) ? 2 : Activity.class.isAssignableFrom(cls) ? 1 : ContentProvider.class.isAssignableFrom(cls) ? 8 : 0;`
- `sources/cn/jpush/android/service/DataProvider.java:12`
  `public class DataProvider extends ContentProvider {`
- `sources/cn/jpush/android/service/DownloadProvider.java:13`
  `public class DownloadProvider extends ContentProvider {`
- `sources/cn/jpush/android/service/InitProvider.java:12`
  `public class InitProvider extends ContentProvider {`
- `sources/com/xiaomi/mipush/sdk/help/HelpContentProvider.java:10`
  `public class HelpContentProvider extends ContentProvider {`
- `sources/com/xiaomi/push/providers/TrafficProvider.java:13`
  `public class TrafficProvider extends ContentProvider {`

## BR024

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `sources/androidx/core/content/FileProvider.java:225`
  `if (!providerInfo.grantUriPermissions) {`

## BR025

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/cn/udesk/db/UdeskDBHelper.java:5`
  `import android.database.sqlite.SQLiteDatabase;`
- `sources/cn/udesk/db/UdeskDBHelper.java:6`
  `import android.database.sqlite.SQLiteOpenHelper;`
- `sources/cn/udesk/db/UdeskDBHelper.java:9`
  `public class UdeskDBHelper extends SQLiteOpenHelper {`
- `sources/cn/udesk/db/UdeskDBHelper.java:18`
  `super(context, DATABASE_NAME + str, (SQLiteDatabase.CursorFactory) null, 7);`
- `sources/cn/udesk/db/UdeskDBHelper.java:21`
  `@Override // android.database.sqlite.SQLiteOpenHelper`
- `sources/cn/udesk/db/UdeskDBHelper.java:22`
  `public void onCreate(SQLiteDatabase sQLiteDatabase) {`
- `sources/cn/udesk/db/UdeskDBHelper.java:24`
  `sQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS " + UdeskMessage + "(MsgID TEXT primary key,Time BIGINT,MsgContent TEXT,MsgType TEXT, ReadFlag INTEGER,SendFlag INTEGER,PlayedFlag INTEGER,Direction INTEGER,LocalPath Text,Duration INTEGER,Receive_AgentJid TEXT,created_at TEXT,updated_at TEXT,reply_...`
- `sources/cn/udesk/db/UdeskDBHelper.java:25`
  `sQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS " + UdeskSendIngMsgs + "( MsgID TEXT, SendFlag INTEGER, Time BIGINT, primary key(MsgID))");`
- `sources/cn/udesk/db/UdeskDBHelper.java:26`
  `sQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS " + UdeskAgentMsg + "( Receive_AgentJid TEXT, HeadUrl TEXT, AgentNick TEXT, primary key(Receive_AgentJid))");`
- `sources/cn/udesk/db/UdeskDBHelper.java:27`
  `sQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS " + SubSessionId + "( SUBID TEXT primary key, SEQNUM INTEGER)");`
- `sources/cn/udesk/db/UdeskDBHelper.java:33`
  `@Override // android.database.sqlite.SQLiteOpenHelper`
- `sources/cn/udesk/db/UdeskDBHelper.java:34`
  `public void onUpgrade(SQLiteDatabase sQLiteDatabase, int i, int i2) {`
- `sources/cn/udesk/db/UdeskDBHelper.java:35`
  `sQLiteDatabase.beginTransaction();`
- `sources/cn/udesk/db/UdeskDBHelper.java:71`
  `sQLiteDatabase.execSQL("ALTER TABLE udeskMessageInfo ADD COLUMN  flowId INTEGER ");`
- `sources/cn/udesk/db/UdeskDBHelper.java:72`
  `sQLiteDatabase.execSQL("ALTER TABLE udeskMessageInfo ADD COLUMN  flowTitle TEXT ");`
- `sources/cn/udesk/db/UdeskDBHelper.java:73`
  `sQLiteDatabase.execSQL("ALTER TABLE udeskMessageInfo ADD COLUMN  flowContent TEXT ");`
- `sources/cn/udesk/db/UdeskDBHelper.java:74`
  `sQLiteDatabase.execSQL("ALTER TABLE udeskMessageInfo ADD COLUMN  question_id TEXT ");`
- `sources/cn/udesk/db/UdeskDBHelper.java:77`
  `sQLiteDatabase.execSQL("DROP TABLE IF EXISTS udesksendIngMsgs");`
- `sources/cn/udesk/db/UdeskDBHelper.java:78`
  `sQLiteDatabase.execSQL("DROP TABLE IF EXISTS udeskAgentMsg");`
- `sources/cn/udesk/db/UdeskDBHelper.java:79`
  `sQLiteDatabase.execSQL("DROP TABLE IF EXISTS sub_sessionid");`
- `sources/cn/udesk/db/UdeskDBHelper.java:80`
  `sQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS " + UdeskSendIngMsgs + "( MsgID TEXT, SendFlag INTEGER, Time BIGINT, primary key(MsgID))");`
- `sources/cn/udesk/db/UdeskDBHelper.java:81`
  `sQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS " + UdeskAgentMsg + "( Receive_AgentJid TEXT, HeadUrl TEXT, AgentNick TEXT, primary key(Receive_AgentJid))");`
- `sources/cn/udesk/db/UdeskDBHelper.java:82`
  `sQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS " + SubSessionId + "( SUBID TEXT primary key, SEQNUM INTEGER)");`
- `sources/cn/udesk/db/UdeskDBHelper.java:83`
  `sQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS TempMessageInfo(MsgID TEXT primary key,Time BIGINT,MsgContent TEXT,MsgType TEXT, ReadFlag INTEGER,SendFlag INTEGER,PlayedFlag INTEGER,Direction INTEGER,LocalPath Text,Duration INTEGER,Receive_AgentJid TEXT,created_at TEXT,updated_at TEXT,reply_user ...`
- `sources/cn/udesk/db/UdeskDBHelper.java:85`
  `sQLiteDatabase.execSQL(" INSERT INTO TempMessageInfo (MsgID,Time,MsgContent,MsgType,ReadFlag,SendFlag,PlayedFlag,Direction,LocalPath,Duration) SELECT MsgID,Time,MsgContent,MsgType,ReadFlag,SendFlag,PlayedFlag,Direction,LocalPath,Duration  FROM udeskMessageInfo ");`
- `sources/cn/udesk/db/UdeskDBHelper.java:87`
  `sQLiteDatabase.execSQL(" INSERT INTO TempMessageInfo (MsgID,Time,MsgContent,MsgType,ReadFlag,SendFlag,PlayedFlag,Direction,LocalPath,Duration,Receive_AgentJid,created_at,reply_user,reply_userurl) SELECT MsgID,Time,MsgContent,MsgType,ReadFlag,SendFlag,PlayedFlag,Direction,LocalPath,Duration,AgentJid,...`
- `sources/cn/udesk/db/UdeskDBHelper.java:89`
  `sQLiteDatabase.execSQL(" INSERT INTO TempMessageInfo (MsgID,Time,MsgContent,MsgType,ReadFlag,SendFlag,PlayedFlag,Direction,LocalPath,Duration) SELECT MsgID,Time,MsgContent,MsgType,ReadFlag,SendFlag,PlayedFlag,Direction,LocalPath,Duration  FROM udeskMessageInfo ");`
- `sources/cn/udesk/db/UdeskDBHelper.java:91`
  `sQLiteDatabase.execSQL("DROP TABLE udeskMessageInfo");`
- `sources/cn/udesk/db/UdeskDBHelper.java:92`
  `sQLiteDatabase.execSQL("ALTER TABLE TempMessageInfo RENAME TO udeskMessageInfo");`
- `sources/cn/udesk/db/UdeskDBManager.java:497`
  `if (getSQLiteDatabase() != null && messageInfo != null) {`
- `sources/cn/udesk/db/UdeskDBManager.java:498`
  `getSQLiteDatabase().execSQL("replace into " + UdeskDBHelper.UdeskMessage + "(MsgID ,Time ,MsgContent,MsgType,ReadFlag,SendFlag,PlayedFlag,Direction,LocalPath,Duration,Receive_AgentJid,created_at,updated_at,reply_user,reply_userurl,subsessionid,seqNum,fileName,fileSize,switchStaffType,switchStaffTips...`
- `sources/cn/udesk/db/UdeskDBManager.java:510`
  `if (getSQLiteDatabase() == null) {`
- `sources/cn/udesk/db/UdeskDBManager.java:513`
  `getSQLiteDatabase().execSQL(" replace into " + UdeskDBHelper.SubSessionId + "(SUBID,SEQNUM)  values (?,?)", new Object[]{str, Integer.valueOf(i2)});`
- `sources/cn/udesk/db/UdeskDBManager.java:967`
  `public synchronized SQLiteDatabase getSQLiteDatabase() {`
- `sources/cn/udesk/db/UdeskDBManager.java:983`
  `if (getSQLiteDatabase() == null) {`
- `sources/cn/udesk/db/UdeskDBManager.java:986`
  `cursorRawQuery = getSQLiteDatabase().rawQuery(str2, new String[]{str});`
- `sources/com/umeng/analytics/pro/i.java:1394`
  `android.content.Context r8 = com.umeng.analytics.pro.i.g     // Catch: java.lang.Throwable -> L83 android.database.sqlite.SQLiteDatabaseCorruptException -> L85`
- `sources/com/umeng/analytics/pro/i.java:1395`
  `java.lang.String r8 = com.umeng.commonsdk.utils.UMUtils.getAppVersionCode(r8)     // Catch: java.lang.Throwable -> L83 android.database.sqlite.SQLiteDatabaseCorruptException -> L85`
- `sources/com/umeng/analytics/pro/i.java:1396`
  `r4.put(r7, r8)     // Catch: java.lang.Throwable -> L83 android.database.sqlite.SQLiteDatabaseCorruptException -> L85`
- `sources/com/umeng/analytics/pro/i.java:1398`
  `r3.insert(r7, r2, r4)     // Catch: java.lang.Throwable -> L83 android.database.sqlite.SQLiteDatabaseCorruptException -> L85`

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
  `int i = sharedPreferencesReload.getInt("service_stoped", -1);`
- `sources/cn/jpush/android/cache/a.java:54`
  `int i2 = context.getSharedPreferences("cn.jpush.android.user.profile", 0).getInt("service_stoped", 0);`
- `sources/cn/jpush/android/cache/a.java:90`
  `j2 = context.getSharedPreferences("cn.jpush.android.user.profile", 0).getLong("geofence_interval", -1L);`
- `sources/cn/jpush/android/cache/a.java:119`
  `String string2 = context.getSharedPreferences("cn.jpush.android.user.profile", 0).getString("jpush_save_custom_builder" + str, "");`
- `sources/cn/jpush/android/cache/a.java:150`
  `if (i2 == -1 && (i2 = context.getSharedPreferences("cn.jpush.android.user.profile", 0).getInt("geofence_max_num", -1)) != -1) {`
- `sources/com/alipay/mobile/common/logging/ProcessInfoImpl.java:359`
  `return PreferenceManager.getDefaultSharedPreferences(this.a).getBoolean("huawei_preload_launch_models", "PAR-TL00 PAR-LX9 PAR-LX1 PAR-LX1M PAR-AL00 PAR-TL20".contains(Build.MODEL));`
- `sources/com/alipay/mobile/common/logging/strategy/LogStrategyManager.java:1000`
  `LoggerFactory.getTraceLogger().info(TAG, "isLogWrite, curCrashMinuteCoutCommitResult:".concat(String.valueOf(sharedPreferences.edit().putInt(KEY_CUR_CRASH_MINUTE_COUNT, i3).commit())));`
- `sources/com/alipay/mobile/common/logging/strategy/LogStrategyManager.java:1009`
  `this.positiveDiagnoseTag = this.context.getSharedPreferences(SP_NAME_LOGSTRATEGY_CONFIG, 4).getInt(KEY_POSITIVE_DIAGNOSE, 1);`
- `sources/com/alipay/mobile/common/logging/util/LoggingSPCache.java:40`
  `private SharedPreferences c;`
- `sources/com/alipay/mobile/common/logging/util/perf/Judge.java:4`
  `import android.content.SharedPreferences;`
- `sources/com/alipay/mobile/common/logging/util/perf/Judge.java:5`
  `import android.preference.PreferenceManager;`
- `sources/com/alipay/mobile/common/logging/util/perf/Judge.java:42`
  `SharedPreferences judgeSP = getJudgeSP();`
- `sources/com/umeng/analytics/pro/d0.java:46`
  `SharedPreferences.Editor editorEdit = PreferenceWrapper.getDefault(context).edit();`
- `sources/com/umeng/analytics/pro/o.java:856`
  `jSONObject.put(com.umeng.commonsdk.statistics.b.a(com.umeng.analytics.pro.d.l), sharedPreferences.getString("vers_pre_version", "0"));`
- `sources/com/umeng/analytics/pro/o.java:857`
  `jSONObject.put(com.umeng.commonsdk.statistics.b.a(com.umeng.analytics.pro.d.m), sharedPreferences.getString("vers_date", str2));`
- `sources/com/umeng/analytics/pro/o.java:859`
  `sharedPreferences.edit().putString("pre_version", string).putString("cur_version", DeviceConfig.getAppVersionName(m)).putString("pre_date", str2).remove("vers_name").remove("vers_code").remove("vers_date").remove("vers_pre_version").commit();`
- `sources/com/umeng/analytics/pro/o.java:1564`
  `SharedPreferences sharedPreferences = PreferenceWrapper.getDefault(m);`
- `sources/com/umeng/analytics/pro/o.java:1565`
  `if (sharedPreferences != null) {`
- `sources/com/umeng/analytics/pro/o.java:1566`
  `String string = sharedPreferences.getString("userlevel", "");`
- `sources/com/umeng/analytics/pro/u.java:97`
  `if (sharedPreferences.getLong(e, 0L) == 0) {`
- `sources/com/umeng/analytics/pro/u.java:101`
  `SharedPreferences.Editor editorEdit = sharedPreferences.edit();`
- `sources/com/umeng/analytics/pro/u.java:151`
  `SharedPreferences.Editor editorEdit = sharedPreferences.edit();`
- `sources/com/umeng/analytics/pro/u.java:198`
  `int i2 = sharedPreferences.getInt("versioncode", 0);`
- `sources/com/umeng/analytics/pro/u.java:199`
  `String string2 = sharedPreferences.getString("pre_date", "");`
- `sources/com/umeng/analytics/pro/u.java:200`
  `String string3 = sharedPreferences.getString("pre_version", "");`
- `sources/com/umeng/analytics/pro/u.java:201`
  `String string4 = sharedPreferences.getString(d.az, "");`
- `sources/com/umeng/analytics/pro/u.java:231`
  `h = sharedPreferences.getString("session_id", null);`
- `sources/com/umeng/analytics/pro/y.java:85`
  `SharedPreferences sharedPreferences = PreferenceWrapper.getDefault(appContext);`
- `sources/com/umeng/analytics/pro/y.java:86`
  `long j = sharedPreferences.getLong(u.e, 0L);`
- `sources/com/umeng/analytics/pro/y.java:87`
  `long j2 = sharedPreferences.getLong(u.f, 0L);`
- `sources/com/umeng/analytics/process/UMProcessDBDatasSender.java:143`
  `SharedPreferences sharedPreferences = PreferenceWrapper.getDefault(this.b);`
- `sources/com/umeng/analytics/process/UMProcessDBDatasSender.java:144`
  `if (sharedPreferences != null) {`
- `sources/com/umeng/analytics/process/UMProcessDBDatasSender.java:145`
  `String string = sharedPreferences.getString("userlevel", "");`
- `sources/com/umeng/common/b.java:28`
  `private SharedPreferences e() {`
- `sources/com/umeng/common/b.java:33`
  `return context.getSharedPreferences("mobclick_agent_user_" + b, 0);`
- `sources/com/umeng/common/b.java:37`
  `SharedPreferences sharedPreferencesE = e();`
- `sources/com/umeng/common/b.java:38`
  `if (sharedPreferencesE != null) {`

## BR027

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/androidx/core/content/ContextCompat.java:265`
  `return Build.VERSION.SDK_INT >= 21 ? context.getNoBackupFilesDir() : a(new File(context.getApplicationInfo().dataDir, "no_backup"));`
- `sources/androidx/core/content/FileProvider.java:31`
  `private static final File c = new File("/");`
- `sources/androidx/core/graphics/drawable/IconCompat.java:366`
  `return new FileInputStream(new File((String) this.a));`
- `sources/androidx/core/os/EnvironmentCompat.java:27`
  `return file.getCanonicalPath().startsWith(Environment.getExternalStorageDirectory().getCanonicalPath()) ? Environment.getExternalStorageState() : "unknown";`
- `sources/androidx/documentfile/provider/b.java:74`
  `File file = new File(this.b, str2);`
- `sources/cn/jiguang/bd/a.java:144`
  `File file = new File(string + c.b);`
- `sources/cn/jiguang/bd/a.java:152`
  `File file2 = new File(string + str3);`
- `sources/cn/jiguang/bf/d.java:207`
  `File[] fileArrA = cn.jiguang.f.c.a(new File(file, "nowrap"), c.a.a);`
- `sources/cn/jiguang/bf/d.java:210`
  `File file2 = new File(file, "tmp");`
- `sources/cn/jpush/android/ad/c.java:20`
  `return new File(filesDir, str);`
- `sources/cn/jpush/android/ad/c.java:111`
  `return new File(str).exists();`
- `sources/cn/jpush/android/ad/c.java:256`
  `c(new File(a(context, "j_in_app_" + str, 0, false)));`
- `sources/cn/jpush/android/ad/c.java:266`
  `if (new File(str2).exists()) {`
- `sources/cn/jpush/android/ad/e.java:78`
  `File file = new File(str);`
- `sources/cn/jpush/android/d/c.java:30`
  `File file = new File(filesDir, str);`
- `sources/cn/jpush/android/d/c.java:47`
  `File file = new File(context.getFilesDir(), str);`
- `sources/cn/jpush/android/d/c.java:114`
  `File file = new File(context.getFilesDir(), str);`
- `sources/cn/jpush/android/r/c.java:42`
  `Logger.d("InAppTplHelper", "use cache template, templateId: " + strD + ", webPagePath: " + str2 + ", totalTemplateCount: " + linkedHashMapA.values().size() + ", update template file time: " + new File(str2).setLastModified(bVar.c));`
- `sources/cn/jpush/android/r/c.java:133`
  `Logger.d("InAppTplHelper", "download image resource cache to local success, Uri.fromFile: " + Uri.fromFile(new File(strA)));`
- `sources/cn/jpush/android/r/c.java:281`
  `File file = new File(str);`
- `sources/cn/jpush/android/ui/b.java:117`
  `if (TextUtils.isEmpty(str) || !new File(str.replace("file://", "")).exists()) {`
- `sources/cn/jpush/android/x/b.java:246`
  `if (new File(str).exists()) {`
- `sources/cn/jpush/android/x/b.java:883`
  `if (!new File(str2).exists()) {`
- `sources/cn/udesk/UdeskUtil.java:1309`
  `return ContentUris.withAppendedId(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, Long.valueOf(strArrSplit[1]).longValue()).toString();`
- `sources/cn/udesk/UdeskUtil.java:1312`
  `return ContentUris.withAppendedId(MediaStore.Video.Media.EXTERNAL_CONTENT_URI, Long.valueOf(strArrSplit[1]).longValue()).toString();`
- `sources/cn/udesk/UdeskUtil.java:1315`
  `return ContentUris.withAppendedId(MediaStore.Audio.Media.EXTERNAL_CONTENT_URI, Long.valueOf(strArrSplit[1]).longValue()).toString();`
- `sources/cn/udesk/UdeskUtil.java:1318`
  `return getDataColumn(context, "image".equals(str) ? MediaStore.Images.Media.EXTERNAL_CONTENT_URI : "video".equals(str) ? MediaStore.Video.Media.EXTERNAL_CONTENT_URI : UdeskConst.ChatMsgTypeString.TYPE_AUDIO.equals(str) ? MediaStore.Audio.Media.EXTERNAL_CONTENT_URI : null, "_id=?", new String[]{strAr...`
- `sources/cn/udesk/aac/livedata/FileLiveData.java:517`
  `UdeskHttpFacade.getInstance().downloadFile(new File(UdeskUtil.getDirectoryPath(context, UdeskConst.FileAudio), UdeskUtil.getFileName(context, messageInfo.getMsgContent(), UdeskConst.FileAudio)).getAbsolutePath(), messageInfo.getMsgContent(), UdeskConst.REFERER_VALUE, new h(this));`
- `sources/cn/udesk/photoselect/LocalMedialLoader.java:8`
  `import android.provider.MediaStore;`
- `sources/cn/udesk/voice/AudioRecordButton.java:233`
  `return new File(this.l).length();`
- `sources/cn/udesk/voice/AudioRecordManager.java:85`
  `File file = new File(AudioRecordManager.this.a);`
- `sources/cn/udesk/voice/AudioRecordManager.java:89`
  `AudioRecordManager.this.b = new File(file, UUID.randomUUID().toString() + UdeskConst.AUDIO_SUF_WAV).getAbsolutePath();`
- `sources/cn/udesk/voice/AudioRecordManager.java:169`
  `new File(AudioRecordManager.this.b).delete();`
- `sources/com/alibaba/sdk/android/oss/common/OSSLogToFileUtils.java:120`
  `if (this.a && Environment.getExternalStorageState().equals("mounted") && Build.VERSION.SDK_INT < 29) {`
- `sources/com/alibaba/sdk/android/oss/common/OSSLogToFileUtils.java:124`
  `file = new File(Environment.getExternalStorageDirectory().getPath() + File.separator + "OSSLog");`
- `sources/com/alibaba/sdk/android/oss/common/OSSLogToFileUtils.java:129`
  `file = new File(c.getFilesDir().getPath() + File.separator + "OSSLog");`
- `sources/com/alibaba/sdk/android/oss/common/OSSLogToFileUtils.java:139`
  `file2 = new File(file.getPath() + "/logs.csv");`
- `sources/com/alibaba/sdk/android/oss/common/OSSLogToFileUtils.java:166`
  `StatFs statFs = new StatFs(Environment.getExternalStorageDirectory().getPath());`
- `sources/com/alibaba/sdk/android/oss/common/OSSLogToFileUtils.java:202`
  `File file = new File(e.getParent() + "/logs.csv");`
- `sources/com/alibaba/sdk/android/oss/common/OSSLogToFileUtils.java:211`
  `File file = new File(Environment.getExternalStorageDirectory().getPath() + File.separator + "OSSLog");`

## BR029

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:87`
  `android:exported="true"`
- `resources/AndroidManifest.xml:96`
  `android:exported="true"`
- `resources/AndroidManifest.xml:197`
  `android:exported="true"`
- `resources/AndroidManifest.xml:277`
  `android:exported="true"`
- `resources/AndroidManifest.xml:575`
  `android:exported="true"`
- `resources/AndroidManifest.xml:581`
  `android:exported="true"`
- `resources/AndroidManifest.xml:600`
  `android:exported="true">`
- `resources/AndroidManifest.xml:610`
  `android:exported="true"`
- `resources/AndroidManifest.xml:653`
  `android:exported="true"`
- `resources/AndroidManifest.xml:664`
  `android:exported="true"`
- `resources/AndroidManifest.xml:693`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:790`
  `android:exported="true"`

## BR030

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:693`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:711`
  `android:exported="true">`
- `resources/AndroidManifest.xml:719`
  `android:exported="true">`
- `resources/AndroidManifest.xml:727`
  `android:exported="true">`
- `resources/AndroidManifest.xml:761`
  `android:exported="true"/>`

## BR031

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:761`
  `android:exported="true"/>`
- `resources/AndroidManifest.xml:775`
  `android:exported="true">`
- `resources/AndroidManifest.xml:810`
  `android:exported="true">`

## BR033

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/cn/jpush/android/ui/a.java:127`
  `intent.setDataAndType(Uri.parse(str), "audio/*");`
- `sources/cn/jpush/android/ui/a.java:198`
  `intent4.setDataAndType(Uri.parse(str), "video/*");`
- `sources/cn/udesk/activity/UdeskBaseWebViewActivity.java:45`
  `UdeskBaseWebViewActivity.this.startActivity(new Intent("android.intent.action.VIEW", Uri.parse(str)));`
- `sources/cn/udesk/activity/UdeskBaseWebViewActivity.java:69`
  `Uri uri = Uri.parse(str);`
- `sources/cn/udesk/activity/UdeskChatActivity.java:255`
  `Intent intent = new Intent("android.intent.action.CALL", Uri.parse(this.a));`
- `sources/cn/udesk/activity/UdeskChatActivity.java:2339`
  `Intent intent = new Intent("android.intent.action.CALL", Uri.parse(str));`
- `sources/cn/udesk/itemview/LeftViewHolder.java:796`
  `this.b.startActivity(new Intent("android.intent.action.DIAL", Uri.parse("tel:" + this.a.getValue())));`
- `sources/cn/udesk/itemview/LeftViewHolder.java:1865`
  `this.mContext.startActivity(new Intent("android.intent.action.DIAL", Uri.parse(str)));`
- `sources/com/alipay/ma/analyze/a/a.java:24`
  `return (TextUtils.isEmpty(str) || (uri = Uri.parse(str)) == null || TextUtils.isEmpty(uri.getHost()) || !TextUtils.equals("s.tb.cn", uri.getHost().toLowerCase())) ? false : true;`
- `sources/com/alipay/sdk/app/d.java:28`
  `activity.startActivityForResult(new Intent(str2, Uri.parse(str)), i);`
- `sources/com/alipay/sdk/app/PayResultActivity.java:51`
  `intent.setData(Uri.parse("alipayhk://platformapi/startApp?appId=20000125&schemePaySession=" + URLEncoder.encode(str, "UTF-8") + "&orderSuffix=" + URLEncoder.encode(str2, "UTF-8") + "&packageName=" + URLEncoder.encode(str3, "UTF-8") + "&externalPkgName=" + URLEncoder.encode(str3, "UTF-8")));`
- `sources/com/alipay/sdk/app/PayTask.java:450`
  `Uri uri = Uri.parse(strTrim);`
- `sources/com/alipay/sdk/util/f.java:354`
  `intent.setData(Uri.parse(string));`
- `sources/com/alipay/sdk/util/k.java:14`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse(a), null, null, null, null);`
- `sources/com/alipay/sdk/util/l.java:581`
  `activity.startActivity(new Intent("android.intent.action.VIEW", Uri.parse(str)));`
- `sources/com/alipay/sdk/widget/d.java:510`
  `intent.setData(Uri.parse(str));`
- `sources/com/alipay/sdk/widget/e.java:90`
  `Intent intent = new Intent("android.intent.action.VIEW", Uri.parse(str));`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:315`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/finderOpenProfile"), null, null, new String[]{this.appId, ((WXChannelOpenProfile.Req) baseReq).userName}, null);`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:353`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/jumpToOfflinePay"), null, null, new String[]{this.appId}, null);`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:363`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/launchWXMiniprogram"), null, null, new String[]{this.appId, req.userName, req.path, req.miniprogramType + "", req.extData}, null);`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:381`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/openTypeWebview"), null, null, new String[]{this.appId, String.valueOf(3), URLEncoder.encode(String.format("url=%s", URLEncoder.encode(((WXNontaxPay.Req) baseReq).url)))}, null);`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:451`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/openTypeWebview"), null, null, new String[]{this.appId, String.valueOf(4), URLEncoder.encode(String.format("url=%s", URLEncoder.encode(((WXPayInsurance.Req) baseReq).url)))}, null);`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:500`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/preloadWXMiniprogram"), null, null, new String[]{this.appId, req.userName, req.path, req.miniprogramType + "", req.extData}, null);`
- `sources/com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.java:510`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://com.tencent.mm.sdk.comm.provider/QRCodePay"), null, null, new String[]{this.appId, req.codeContent, req.extraMsg}, null);`
- `sources/com/umeng/analytics/pro/g.java:17`
  `Cursor cursorQuery = context.getContentResolver().query(Uri.parse("content://cn.nubia.provider.deviceid.dataid/oaid"), null, null, null, null);`
- `sources/com/vivo/push/p.java:9`
  `public static final Uri a = Uri.parse("content://com.vivo.push.sdk.service.SystemPushConfig/config");`
- `sources/com/vivo/push/p.java:10`
  `public static final Uri b = Uri.parse("content://com.vivo.push.sdk.service.SystemPushConfig/permission");`
- `sources/com/vivo/push/d/u.java:76`
  `Uri uri2 = Uri.parse(skipContent);`
- `sources/com/xiaomi/push/service/al.java:416`
  `intent.setData(Uri.parse(strTrim));`
- `sources/com/xiaomi/push/service/al.java:508`
  `intent2.setData(Uri.parse(jaVarM541a.f612e));`
- `sources/com/xiaomi/push/service/al.java:846`
  `intent.setData(Uri.parse(strTrim));`
- `sources/com/youzan/androidsdk/tool/WebUtil.java:42`
  `return !TextUtils.isEmpty(str) && SchemeIntent.handleSilently(activity, Uri.parse(str));`
- `sources/com/youzan/spiderman/cache/f.java:21`
  `return new CacheUrl(Uri.parse(str));`
- `sources/com/youzan/spiderman/cache/f.java:27`
  `return new CacheUrl(Uri.parse("https://img.yzcdn.cn" + str));`
- `sources/com/youzan/spiderman/cache/f.java:30`
  `return new CacheUrl(Uri.parse("https://su.yzcdn.cn" + str));`
- `sources/com/youzan/systemweb/event/PreviewImageSubscriber.java:33`
  `intent.setData(Uri.parse("youzan://imagebrowser"));`
- `sources/com/yuwell/uhealth/global/utils/OptimizationUtil.java:79`
  `intent.setData(Uri.parse("package:" + activity.getPackageName()));`
- `sources/com/yuwell/uhealth/global/utils/OptimizationUtil.java:105`
  `intent.setData(Uri.parse("package:" + activity.getPackageName()));`
- `sources/com/yuwell/uhealth/global/utils/OptimizationUtil.java:125`
  `intent.setData(Uri.parse("package:" + context.getPackageName()));`
- `sources/com/yuwell/uhealth/view/base/ToolbarActivity.java:143`
  `startActivityForResult(new Intent("android.settings.action.MANAGE_OVERLAY_PERMISSION", Uri.parse("package:" + getPackageName())), 5);`
- `sources/com/yuwell/uhealth/view/base/web/CommonWebViewClient.java:55`
  `Uri uri = Uri.parse(str);`
- `sources/com/yuwell/uhealth/view/impl/customer/UdeskChatActivity.java:296`
  `Intent intent = new Intent("android.intent.action.CALL", Uri.parse(this.a));`
- `sources/com/yuwell/uhealth/view/impl/customer/UdeskChatActivity.java:2344`
  `Intent intent = new Intent("android.intent.action.CALL", Uri.parse(str));`
- `sources/com/yuwell/uhealth/view/impl/me/ContactUs.java:21`
  `Uri uri = Uri.parse("tel:4008287768");`

## BR034

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/cn/jiguang/l/b.java:43`
  `if (this.a.startService(intent) != null) {`
- `sources/cn/jpush/android/d/b.java:235`
  `context.sendBroadcast(intent, String.format(locale, "%s.permission.JPUSH_MESSAGE", dVar.b));`
- `sources/cn/jpush/android/g/b.java:25`
  `cn.jpush.android.f.c.a.sendBroadcast(intent);`
- `sources/cn/jpush/android/n/a.java:35`
  `context.sendBroadcast(intent);`
- `sources/cn/jpush/android/x/b.java:490`
  `context.sendBroadcast(intent);`
- `sources/cn/jpush/android/x/b.java:1127`
  `context.startActivity(intent);`
- `sources/cn/udesk/activity/UdeskZoomImageActivty.java:247`
  `UdeskZoomImageActivty.this.sendBroadcast(intent);`
- `sources/com/alipay/mobile/common/logging/util/MemoryUtil.java:137`
  `context.sendBroadcast(intent);`
- `sources/com/alipay/mobile/common/logging/util/ToolThreadUtils.java:48`
  `this.c.sendBroadcast(intent);`
- `sources/com/alipay/sdk/util/f.java:358`
  `this.a.startActivity(intent);`
- `sources/com/alipay/sdk/widget/d.java:511`
  `activity.startActivity(intent);`
- `sources/com/mpaas/aar/demo/custom/CustomScanActivity.java:259`
  `startActivity(intent);`
- `sources/com/mpaas/aar/demo/custom/CustomScanActivity.java:261`
  `startActivity(new Intent("android.settings.APPLICATION_SETTINGS"));`
- `sources/com/xiaomi/mipush/sdk/PushMessageHandler.java:245`
  `context.sendBroadcast(intent, d.a(context));`
- `sources/com/xiaomi/push/fk.java:44`
  `if (context.startService(intent) != null) {`
- `sources/com/xiaomi/push/service/XMJobService.java:64`
  `startService(intent);`
- `sources/com/youzan/androidsdk/basic/web/plugin/SaveImageProcessor.java:137`
  `context.sendBroadcast(intent);`
- `sources/com/yuwell/uhealth/data/source/local/CalendarProviderManager.java:304`
  `context.startActivity(data);`
- `sources/com/yuwell/uhealth/data/source/local/CalendarProviderManager.java:312`
  `context.startActivity(intentPutExtra);`
- `sources/com/yuwell/uhealth/data/source/local/CalendarProviderManager.java:320`
  `context.startActivity(data);`
- `sources/com/yuwell/uhealth/global/utils/OptimizationUtil.java:126`
  `context.startActivity(intent);`
- `sources/com/yuwell/uhealth/view/impl/data/bpm/BpTest.java:257`
  `context.startActivity(new Intent(context, (Class<?>) BpTest.class));`
- `sources/com/yuwell/uhealth/view/impl/data/glu/BgTest.java:226`
  `context.startActivity(new Intent(context, (Class<?>) BgTest.class));`
- `sources/com/yuwell/uhealth/view/impl/device/BleScaner.java:59`
  `bleScaner.startActivity(intent);`
- `sources/com/yuwell/uhealth/view/impl/device/BleScaner.java:61`
  `bleScaner.startActivity(new Intent("android.settings.APPLICATION_SETTINGS"));`
- `sources/com/yuwell/uhealth/view/impl/me/ContactUs.java:24`
  `startActivity(intent);`
- `sources/com/yuwell/uhealth/view/widget/TipsWindow.java:45`
  `TipsWindow.this.a.startActivity(intent);`

## BR035

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/cn/jpush/android/api/SystemAlertHelper.java:173`
  `SystemAlertHelper.e.loadUrl(str);`
- `sources/cn/jpush/android/u/f.java:108`
  `this.f.loadUrl(str2);`
- `sources/cn/jpush/android/ui/c.java:151`
  `this.g.loadUrl(str2);`
- `sources/cn/jpush/android/webview/bridge/b.java:43`
  `webView.loadUrl(this.b.a());`
- `sources/cn/udesk/activity/UdeskBaseWebViewActivity.java:85`
  `webView.loadUrl(str);`
- `sources/cn/udesk/activity/UdeskFormActivity.java:27`
  `this.mwebView.loadUrl(UdeskConst.HTTP + UdeskSDKManager.getInstance().getDomain(this) + "/im_client/feedback.html" + UdeskUtil.getFormUrlPara(this));`
- `sources/cn/udesk/activity/UdeskWebViewUrlAcivity.java:61`
  `this.mwebView.loadUrl(this.c);`
- `sources/cn/udesk/activity/WorkOrderWebViewActivity.java:91`
  `this.mwebView.loadUrl(this.d);`
- `sources/com/alipay/sdk/widget/d.java:280`
  `eVar.getWebView().loadUrl("javascript:(function() {\n    if (window.AlipayJSBridge) {\n        return\n    }\n\n    function alipayjsbridgeFunc(url) {\n        var iframe = document.createElement(\"iframe\");\n        iframe.style.width = \"1px\";\n        iframe.style.height = \"1px\";\n        ifr...`
- `sources/com/alipay/sdk/widget/e.java:367`
  `this.e.loadUrl(str);`
- `sources/com/youzan/androidsdk/basic/YouzanBaseWebViewCompat.java:84`
  `this.f1084.loadUrl(str);`
- `sources/com/youzan/androidsdk/basic/YouzanBasicSDKAdapter.java:113`
  `webViewCompat.loadUrl("https://h5.youzan.com/v2/im?c=wsc&v=2&kdt_id=" + str + "#talk!id=" + str + "&t=" + System.currentTimeMillis());`
- `sources/com/youzan/androidsdk/basic/YouzanBrowser.java:155`
  `super.loadUrl(str);`
- `sources/com/youzan/androidsdk/basic/YouzanBrowser.java:329`
  `super.loadUrl(str, map);`
- `sources/com/youzan/androidsdk/basic/web/plugin/WebClientWrapper.java:283`
  `webView.loadUrl(strPopBackUrl);`
- `sources/com/youzan/androidsdk/basic/web/plugin/WebClientWrapper.java:348`
  `webView.loadUrl("https://h5.youzan.com/wscvis/checkAuthMobile?kdtId=" + YouzanSDK.getSDKAdapter().kdtId + "&redirectUrl=" + URLEncoder.encode(string2));`
- `sources/com/youzan/androidsdk/basic/web/plugin/WebClientWrapper.java:486`
  `webView.loadUrl("https://h5.youzan.com/wscvis/checkAuthMobile?kdtId=" + YouzanSDK.getSDKAdapter().kdtId + "&redirectUrl=" + URLEncoder.encode(str));`
- `sources/com/youzan/androidsdk/tool/Javascript.java:10`
  `webViewCompat.loadUrl("javascript:window.YouzanJSBridge.trigger('share')");`
- `sources/com/youzan/systemweb/JsInjecter.java:74`
  `this.a.addJavascriptInterface(new CommonInterface(methodDispatcher), "YZAndroidJS");`
- `sources/com/youzan/systemweb/JsInjecter.java:75`
  `this.a.addJavascriptInterface(new CompatInterface(methodDispatcher2), "androidJS");`
- `sources/com/youzan/systemweb/JsInjecter.java:82`
  `webView.loadUrl(it2.next().toJavaScript());`
- `sources/com/youzan/systemweb/JsInjecter.java:117`
  `webView.loadUrl(JS_IS_READY);`
- `sources/com/youzan/systemweb/JsTrigger.java:22`
  `JsTrigger.this.a.loadUrl(this.a);`
- `sources/com/youzan/systemweb/WebViewClientWrapper.java:43`
  `this.a.loadUrl(str);`
- `sources/com/yuwell/uhealth/view/base/web/CommonWebViewClient.java:41`
  `webView.loadUrl("file:///android_asset/error.html?url=" + URLEncoder.encode(str2, "UTF-8"));`
- `sources/com/yuwell/uhealth/view/base/web/CommonWebViewClient.java:57`
  `webView.loadUrl(str);`
- `sources/com/yuwell/uhealth/view/base/web/UHealthWebViewActivity.java:29`
  `webView.loadUrl(str);`
- `sources/com/yuwell/uhealth/view/base/web/UHealthWebViewActivity.java:63`
  `this.webView.loadUrl(getIntent().getStringExtra("url"));`
- `sources/com/yuwell/uhealth/view/impl/data/bpm/BpStatistic.java:117`
  `this.mWebViewFrequence.loadUrl("file:///android_asset/bp-total.html");`
- `sources/com/yuwell/uhealth/view/impl/data/bpm/BpStatistic.java:139`
  `this.mWebViewAverage.loadUrl("file:///android_asset/bp-avg.html");`
- `sources/com/yuwell/uhealth/view/impl/data/glu/BgStatistic.java:146`
  `this.mWebViewAverage.loadUrl("file:///android_asset/bg-avg.html");`
- `sources/com/yuwell/uhealth/view/impl/data/gu/GuBgStatisticFragment.java:146`
  `this.mWebViewAverage.loadUrl("file:///android_asset/bg-avg.html");`
- `sources/com/yuwell/uhealth/view/impl/data/oxy/BoStatistic.java:120`
  `this.mWebViewFrequence.loadUrl("file:///android_asset/bo-total.html");`
- `sources/com/yuwell/uhealth/view/impl/data/oxy/BoStatistic.java:168`
  `this.mWebViewFrequence.loadUrl("file:///android_asset/bo-total.html");`
- `sources/com/yuwell/uhealth/view/impl/main/health/HealthGoogle.java:27`
  `webView.loadUrl(str);`
- `sources/com/yuwell/uhealth/view/impl/main/health/HealthGoogle.java:41`
  `this.webView.loadUrl("https://health.yuyue.com.cn/app2phone/?v=1.0.1#/healthPage");`
- `sources/com/yuwell/uhealth/view/impl/main/store/YouzanFragment.java:238`
  `this.c.loadUrl(getArguments().getString("url", GlobalConstant.STORE_URL));`

## BR040

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `sources/com/alibaba/sdk/android/oss/a.java:13`
  `import com.alibaba.sdk.android.oss.model.AbortMultipartUploadRequest;`
- `sources/com/alibaba/sdk/android/oss/a.java:17`
  `import com.alibaba.sdk.android.oss.model.CompleteMultipartUploadRequest;`
- `sources/com/alibaba/sdk/android/oss/a.java:54`
  `import com.alibaba.sdk.android.oss.model.InitiateMultipartUploadRequest;`
- `sources/com/alibaba/sdk/android/oss/a.java:64`
  `import com.alibaba.sdk.android.oss.model.MultipartUploadRequest;`
- `sources/com/alibaba/sdk/android/oss/a.java:77`
  `import com.alibaba.sdk.android.oss.model.ResumableDownloadRequest;`
- `sources/com/alibaba/sdk/android/oss/a.java:79`
  `import com.alibaba.sdk.android.oss.model.ResumableUploadRequest;`
- `sources/com/alibaba/sdk/android/oss/a.java:129`
  `public AbortMultipartUploadResult abortMultipartUpload(AbortMultipartUploadRequest abortMultipartUploadRequest) throws ServiceException, ClientException {`
- `sources/com/alibaba/sdk/android/oss/a.java:130`
  `return (AbortMultipartUploadResult) this.c.abortMultipartUpload(abortMultipartUploadRequest, null).getResult();`
- `sources/com/alibaba/sdk/android/oss/a.java:134`
  `public void abortResumableUpload(ResumableUploadRequest resumableUploadRequest) throws IOException {`
- `sources/com/alibaba/sdk/android/oss/a.java:135`
  `this.d.abortResumableUpload(resumableUploadRequest);`
- `sources/com/alibaba/sdk/android/oss/a.java:144`
  `public OSSAsyncTask<AbortMultipartUploadResult> asyncAbortMultipartUpload(AbortMultipartUploadRequest abortMultipartUploadRequest, OSSCompletedCallback<AbortMultipartUploadRequest, AbortMultipartUploadResult> oSSCompletedCallback) {`
- `sources/com/alibaba/sdk/android/oss/a.java:145`
  `return this.c.abortMultipartUpload(abortMultipartUploadRequest, oSSCompletedCallback);`
- `sources/com/alibaba/sdk/android/oss/a.java:154`
  `public OSSAsyncTask<CompleteMultipartUploadResult> asyncCompleteMultipartUpload(CompleteMultipartUploadRequest completeMultipartUploadRequest, OSSCompletedCallback<CompleteMultipartUploadRequest, CompleteMultipartUploadResult> oSSCompletedCallback) {`
- `sources/com/alibaba/sdk/android/oss/a.java:155`
  `return this.c.completeMultipartUpload(completeMultipartUploadRequest, oSSCompletedCallback);`
- `sources/com/alibaba/sdk/android/oss/a.java:244`
  `public OSSAsyncTask<InitiateMultipartUploadResult> asyncInitMultipartUpload(InitiateMultipartUploadRequest initiateMultipartUploadRequest, OSSCompletedCallback<InitiateMultipartUploadRequest, InitiateMultipartUploadResult> oSSCompletedCallback) {`
- `sources/com/alibaba/sdk/android/oss/a.java:245`
  `return this.c.initMultipartUpload(initiateMultipartUploadRequest, oSSCompletedCallback);`
- `sources/com/alibaba/sdk/android/oss/a.java:269`
  `public OSSAsyncTask<CompleteMultipartUploadResult> asyncMultipartUpload(MultipartUploadRequest multipartUploadRequest, OSSCompletedCallback<MultipartUploadRequest, CompleteMultipartUploadResult> oSSCompletedCallback) {`
- `sources/com/alibaba/sdk/android/oss/a.java:270`
  `return this.d.multipartUpload(multipartUploadRequest, oSSCompletedCallback);`
- `sources/com/alibaba/sdk/android/oss/a.java:304`
  `public OSSAsyncTask<ResumableDownloadResult> asyncResumableDownload(ResumableDownloadRequest resumableDownloadRequest, OSSCompletedCallback<ResumableDownloadRequest, ResumableDownloadResult> oSSCompletedCallback) {`
- `sources/com/alibaba/sdk/android/oss/a.java:305`
  `return this.d.resumableDownload(resumableDownloadRequest, oSSCompletedCallback);`
- `sources/com/alibaba/sdk/android/oss/a.java:309`
  `public OSSAsyncTask<ResumableUploadResult> asyncResumableUpload(ResumableUploadRequest resumableUploadRequest, OSSCompletedCallback<ResumableUploadRequest, ResumableUploadResult> oSSCompletedCallback) {`
- `sources/com/alibaba/sdk/android/oss/a.java:310`
  `return this.d.resumableUpload(resumableUploadRequest, oSSCompletedCallback);`
- `sources/com/alibaba/sdk/android/oss/a.java:314`
  `public OSSAsyncTask<ResumableUploadResult> asyncSequenceUpload(ResumableUploadRequest resumableUploadRequest, OSSCompletedCallback<ResumableUploadRequest, ResumableUploadResult> oSSCompletedCallback) {`
- `sources/com/alibaba/sdk/android/oss/a.java:315`
  `return this.d.sequenceUpload(resumableUploadRequest, oSSCompletedCallback);`
- `sources/com/alibaba/sdk/android/oss/a.java:329`
  `public CompleteMultipartUploadResult completeMultipartUpload(CompleteMultipartUploadRequest completeMultipartUploadRequest) throws ServiceException, ClientException {`
- `sources/com/alibaba/sdk/android/oss/a.java:330`
  `return this.c.syncCompleteMultipartUpload(completeMultipartUploadRequest);`
- `sources/com/alibaba/sdk/android/oss/a.java:424`
  `public InitiateMultipartUploadResult initMultipartUpload(InitiateMultipartUploadRequest initiateMultipartUploadRequest) throws ServiceException, ClientException {`
- `sources/com/alibaba/sdk/android/oss/a.java:425`
  `return (InitiateMultipartUploadResult) this.c.initMultipartUpload(initiateMultipartUploadRequest, null).getResult();`
- `sources/com/alibaba/sdk/android/oss/a.java:449`
  `public CompleteMultipartUploadResult multipartUpload(MultipartUploadRequest multipartUploadRequest) throws ServiceException, ClientException {`
- `sources/com/alibaba/sdk/android/oss/a.java:450`
  `return (CompleteMultipartUploadResult) this.d.multipartUpload(multipartUploadRequest, null).getResult();`
- `sources/com/alibaba/sdk/android/oss/a.java:494`
  `public ResumableUploadResult resumableUpload(ResumableUploadRequest resumableUploadRequest) throws ServiceException, ClientException {`
- `sources/com/alibaba/sdk/android/oss/a.java:495`
  `return (ResumableUploadResult) this.d.resumableUpload(resumableUploadRequest, null).getResult();`
- `sources/com/alibaba/sdk/android/oss/a.java:499`
  `public ResumableUploadResult sequenceUpload(ResumableUploadRequest resumableUploadRequest) throws ServiceException, ClientException {`
- `sources/com/alibaba/sdk/android/oss/a.java:500`
  `return (ResumableUploadResult) this.d.sequenceUpload(resumableUploadRequest, null).getResult();`
- `sources/com/alibaba/sdk/android/oss/a.java:504`
  `public ResumableDownloadResult syncResumableDownload(ResumableDownloadRequest resumableDownloadRequest) throws ServiceException, ClientException {`
- `sources/com/alibaba/sdk/android/oss/a.java:505`
  `return (ResumableDownloadResult) this.d.resumableDownload(resumableDownloadRequest, null).getResult();`
- `sources/com/alibaba/sdk/android/oss/OSS.java:6`
  `import com.alibaba.sdk.android.oss.model.AbortMultipartUploadRequest;`
- `sources/com/alibaba/sdk/android/oss/OSS.java:10`
  `import com.alibaba.sdk.android.oss.model.CompleteMultipartUploadRequest;`
- `sources/com/alibaba/sdk/android/oss/OSS.java:47`
  `import com.alibaba.sdk.android.oss.model.InitiateMultipartUploadRequest;`
- `sources/com/alibaba/sdk/android/oss/OSS.java:57`
  `import com.alibaba.sdk.android.oss.model.MultipartUploadRequest;`
- `sources/com/alibaba/sdk/android/oss/OSS.java:70`
  `import com.alibaba.sdk.android.oss.model.ResumableDownloadRequest;`
- `sources/com/alibaba/sdk/android/oss/OSS.java:72`
  `import com.alibaba.sdk.android.oss.model.ResumableUploadRequest;`
- `sources/com/alibaba/sdk/android/oss/OSS.java:82`
  `AbortMultipartUploadResult abortMultipartUpload(AbortMultipartUploadRequest abortMultipartUploadRequest) throws ServiceException, ClientException;`
- `sources/com/alibaba/sdk/android/oss/OSS.java:84`
  `void abortResumableUpload(ResumableUploadRequest resumableUploadRequest) throws IOException;`
- `sources/com/alibaba/sdk/android/oss/OSS.java:88`
  `OSSAsyncTask<AbortMultipartUploadResult> asyncAbortMultipartUpload(AbortMultipartUploadRequest abortMultipartUploadRequest, OSSCompletedCallback<AbortMultipartUploadRequest, AbortMultipartUploadResult> oSSCompletedCallback);`
- `sources/com/alibaba/sdk/android/oss/OSS.java:92`
  `OSSAsyncTask<CompleteMultipartUploadResult> asyncCompleteMultipartUpload(CompleteMultipartUploadRequest completeMultipartUploadRequest, OSSCompletedCallback<CompleteMultipartUploadRequest, CompleteMultipartUploadResult> oSSCompletedCallback);`
- `sources/com/alibaba/sdk/android/oss/OSS.java:128`
  `OSSAsyncTask<InitiateMultipartUploadResult> asyncInitMultipartUpload(InitiateMultipartUploadRequest initiateMultipartUploadRequest, OSSCompletedCallback<InitiateMultipartUploadRequest, InitiateMultipartUploadResult> oSSCompletedCallback);`
- `sources/com/alibaba/sdk/android/oss/OSS.java:138`
  `OSSAsyncTask<CompleteMultipartUploadResult> asyncMultipartUpload(MultipartUploadRequest multipartUploadRequest, OSSCompletedCallback<MultipartUploadRequest, CompleteMultipartUploadResult> oSSCompletedCallback);`
- `sources/com/alibaba/sdk/android/oss/OSS.java:152`
  `OSSAsyncTask<ResumableDownloadResult> asyncResumableDownload(ResumableDownloadRequest resumableDownloadRequest, OSSCompletedCallback<ResumableDownloadRequest, ResumableDownloadResult> oSSCompletedCallback);`
- `sources/com/alibaba/sdk/android/oss/OSS.java:154`
  `OSSAsyncTask<ResumableUploadResult> asyncResumableUpload(ResumableUploadRequest resumableUploadRequest, OSSCompletedCallback<ResumableUploadRequest, ResumableUploadResult> oSSCompletedCallback);`
- `sources/com/alibaba/sdk/android/oss/OSS.java:156`
  `OSSAsyncTask<ResumableUploadResult> asyncSequenceUpload(ResumableUploadRequest resumableUploadRequest, OSSCompletedCallback<ResumableUploadRequest, ResumableUploadResult> oSSCompletedCallback);`
- `sources/com/alibaba/sdk/android/oss/OSS.java:162`
  `CompleteMultipartUploadResult completeMultipartUpload(CompleteMultipartUploadRequest completeMultipartUploadRequest) throws ServiceException, ClientException;`
- `sources/com/alibaba/sdk/android/oss/OSS.java:200`
  `InitiateMultipartUploadResult initMultipartUpload(InitiateMultipartUploadRequest initiateMultipartUploadRequest) throws ServiceException, ClientException;`
- `sources/com/alibaba/sdk/android/oss/OSS.java:210`
  `CompleteMultipartUploadResult multipartUpload(MultipartUploadRequest multipartUploadRequest) throws ServiceException, ClientException;`
- `sources/com/alibaba/sdk/android/oss/OSS.java:230`
  `ResumableUploadResult resumableUpload(ResumableUploadRequest resumableUploadRequest) throws ServiceException, ClientException;`
- `sources/com/alibaba/sdk/android/oss/OSS.java:232`
  `ResumableUploadResult sequenceUpload(ResumableUploadRequest resumableUploadRequest) throws ServiceException, ClientException;`
- `sources/com/alibaba/sdk/android/oss/OSS.java:234`
  `ResumableDownloadResult syncResumableDownload(ResumableDownloadRequest resumableDownloadRequest) throws ServiceException, ClientException;`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:7`
  `import com.alibaba.sdk.android.oss.model.AbortMultipartUploadRequest;`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:11`
  `import com.alibaba.sdk.android.oss.model.CompleteMultipartUploadRequest;`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:48`
  `import com.alibaba.sdk.android.oss.model.InitiateMultipartUploadRequest;`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:58`
  `import com.alibaba.sdk.android.oss.model.MultipartUploadRequest;`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:71`
  `import com.alibaba.sdk.android.oss.model.ResumableDownloadRequest;`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:73`
  `import com.alibaba.sdk.android.oss.model.ResumableUploadRequest;`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:90`
  `public AbortMultipartUploadResult abortMultipartUpload(AbortMultipartUploadRequest abortMultipartUploadRequest) throws ServiceException, ClientException {`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:91`
  `return this.a.abortMultipartUpload(abortMultipartUploadRequest);`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:95`
  `public void abortResumableUpload(ResumableUploadRequest resumableUploadRequest) throws IOException {`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:96`
  `this.a.abortResumableUpload(resumableUploadRequest);`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:105`
  `public OSSAsyncTask<AbortMultipartUploadResult> asyncAbortMultipartUpload(AbortMultipartUploadRequest abortMultipartUploadRequest, OSSCompletedCallback<AbortMultipartUploadRequest, AbortMultipartUploadResult> oSSCompletedCallback) {`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:106`
  `return this.a.asyncAbortMultipartUpload(abortMultipartUploadRequest, oSSCompletedCallback);`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:115`
  `public OSSAsyncTask<CompleteMultipartUploadResult> asyncCompleteMultipartUpload(CompleteMultipartUploadRequest completeMultipartUploadRequest, OSSCompletedCallback<CompleteMultipartUploadRequest, CompleteMultipartUploadResult> oSSCompletedCallback) {`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:116`
  `return this.a.asyncCompleteMultipartUpload(completeMultipartUploadRequest, oSSCompletedCallback);`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:205`
  `public OSSAsyncTask<InitiateMultipartUploadResult> asyncInitMultipartUpload(InitiateMultipartUploadRequest initiateMultipartUploadRequest, OSSCompletedCallback<InitiateMultipartUploadRequest, InitiateMultipartUploadResult> oSSCompletedCallback) {`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:206`
  `return this.a.asyncInitMultipartUpload(initiateMultipartUploadRequest, oSSCompletedCallback);`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:230`
  `public OSSAsyncTask<CompleteMultipartUploadResult> asyncMultipartUpload(MultipartUploadRequest multipartUploadRequest, OSSCompletedCallback<MultipartUploadRequest, CompleteMultipartUploadResult> oSSCompletedCallback) {`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:231`
  `return this.a.asyncMultipartUpload(multipartUploadRequest, oSSCompletedCallback);`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:265`
  `public OSSAsyncTask<ResumableDownloadResult> asyncResumableDownload(ResumableDownloadRequest resumableDownloadRequest, OSSCompletedCallback<ResumableDownloadRequest, ResumableDownloadResult> oSSCompletedCallback) {`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:266`
  `return this.a.asyncResumableDownload(resumableDownloadRequest, oSSCompletedCallback);`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:270`
  `public OSSAsyncTask<ResumableUploadResult> asyncResumableUpload(ResumableUploadRequest resumableUploadRequest, OSSCompletedCallback<ResumableUploadRequest, ResumableUploadResult> oSSCompletedCallback) {`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:271`
  `return this.a.asyncResumableUpload(resumableUploadRequest, oSSCompletedCallback);`
- `sources/com/alibaba/sdk/android/oss/OSSClient.java:275`
  `public OSSAsyncTask<ResumableUploadResult> asyncSequenceUpload(ResumableUploadRequest resumableUploadRequest, OSSCompletedCallback<ResumableUploadRequest, ResumableUploadResult> oSSCompletedCallback) {`

## BR041

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `sources/androidx/appcompat/app/AppCompatViewInflater.java:32`
  `import com.umeng.analytics.pro.cb;`
- `sources/androidx/constraintlayout/motion/widget/b.java:13`
  `import com.umeng.analytics.pro.cb;`
- `sources/androidx/constraintlayout/motion/widget/KeyAttributes.java:11`
  `import com.umeng.analytics.pro.cb;`
- `sources/androidx/constraintlayout/motion/widget/KeyCycle.java:13`
  `import com.umeng.analytics.pro.cb;`
- `sources/androidx/constraintlayout/motion/widget/KeyCycleOscillator.java:11`
  `import com.umeng.analytics.pro.cb;`
- `sources/androidx/constraintlayout/motion/widget/KeyTimeCycle.java:12`
  `import com.umeng.analytics.pro.cb;`
- `sources/androidx/constraintlayout/motion/widget/SplineSet.java:10`
  `import com.umeng.analytics.pro.cb;`
- `sources/androidx/constraintlayout/motion/widget/TimeCycleSplineSet.java:11`
  `import com.umeng.analytics.pro.cb;`
- `sources/androidx/core/app/NotificationCompat.java:39`
  `import com.umeng.analytics.pro.d;`
- `sources/androidx/core/content/ContextCompat.java:71`
  `import com.umeng.analytics.pro.am;`
- `sources/androidx/core/provider/FontsContractCompat.java:31`
  `import com.umeng.analytics.pro.aq;`
- `sources/androidx/core/text/BidiFormatter.java:4`
  `import com.umeng.analytics.pro.cb;`
- `sources/androidx/cursoradapter/widget/CursorAdapter.java:16`
  `import com.umeng.analytics.pro.aq;`
- `sources/androidx/dynamicanimation/animation/DynamicAnimation.java:12`
  `import com.umeng.analytics.pro.am;`
- `sources/androidx/media/c.java:60`
  `return i & com.umeng.commonsdk.stateless.b.a;`
- `sources/androidx/versionedparcelable/ParcelUtils.java:8`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/aa/c.java:4`
  `import com.umeng.analytics.pro.cb;`
- `sources/cn/jiguang/ab/a.java:9`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/ad/d.java:14`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/aj/b.java:11`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/am/c.java:13`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/am/c.java:14`
  `import com.umeng.analytics.pro.cb;`
- `sources/cn/jiguang/an/b.java:10`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/an/e.java:8`
  `import com.umeng.analytics.pro.cb;`
- `sources/cn/jiguang/ao/a.java:19`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/ax/b.java:5`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/ax/g.java:8`
  `import com.umeng.analytics.pro.cb;`
- `sources/cn/jiguang/ax/h.java:11`
  `import com.umeng.analytics.pro.cb;`
- `sources/cn/jiguang/ax/i.java:8`
  `import com.umeng.analytics.pro.cb;`
- `sources/cn/jiguang/ay/b.java:6`
  `import com.umeng.analytics.pro.cb;`
- `sources/cn/jiguang/az/f.java:11`
  `import com.umeng.analytics.pro.cb;`
- `sources/cn/jiguang/az/g.java:5`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/az/g.java:6`
  `import com.umeng.analytics.pro.cb;`
- `sources/cn/jiguang/az/i.java:12`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/az/i.java:444`
  `boolean zContainsKey = bundleD.containsKey(com.umeng.analytics.pro.d.C);`
- `sources/cn/jiguang/az/i.java:447`
  `jSONObject.put("jg_latitude", bundleD.getDouble(com.umeng.analytics.pro.d.C));`
- `sources/cn/jiguang/b/a.java:7`
  `import com.umeng.analytics.pro.d;`
- `sources/cn/jiguang/b/b.java:8`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/bc/e.java:5`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/bc/e.java:6`
  `import com.umeng.analytics.pro.cb;`
- `sources/cn/jiguang/bd/a.java:13`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/bd/a.java:14`
  `import com.umeng.analytics.pro.cb;`
- `sources/cn/jiguang/be/b.java:12`
  `import com.umeng.analytics.pro.cb;`
- `sources/cn/jiguang/bf/a.java:6`
  `import com.umeng.analytics.pro.cb;`
- `sources/cn/jiguang/bf/a.java:105`
  `if (str.equals(com.umeng.analytics.pro.d.L)) {`
- `sources/cn/jiguang/bf/a.java:169`
  `return com.umeng.analytics.pro.d.L;`
- `sources/cn/jiguang/bf/e.java:184`
  `double d4 = bundle.getDouble(com.umeng.analytics.pro.d.C);`
- `sources/cn/jiguang/bf/e.java:197`
  `jSONObject.put(com.umeng.analytics.pro.d.C, d3);`
- `sources/cn/jiguang/bf/e.java:198`
  `jSONObject.put(com.umeng.analytics.pro.d.D, d2);`
- `sources/cn/jiguang/bf/e.java:204`
  `jSONObject.put(com.umeng.analytics.pro.d.C, d3);`
- `sources/cn/jiguang/bf/e.java:205`
  `jSONObject.put(com.umeng.analytics.pro.d.D, d2);`
- `sources/cn/jiguang/bf/f.java:22`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/bg/a.java:12`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/bi/c.java:10`
  `import com.umeng.analytics.pro.cb;`
- `sources/cn/jiguang/bi/c.java:53`
  `jSONObject.put(com.umeng.analytics.pro.d.C, bundle.getDouble(com.umeng.analytics.pro.d.C, 200.0d));`
- `sources/cn/jiguang/bi/c.java:54`
  `jSONObject.put(com.umeng.analytics.pro.d.D, bundle.getDouble("lot", 200.0d));`
- `sources/cn/jiguang/bi/k.java:60`
  `d2 = bundle.getDouble(com.umeng.analytics.pro.d.C);`
- `sources/cn/jiguang/bi/k.java:138`
  `mVar.h = bundle.getDouble(com.umeng.analytics.pro.d.C);`
- `sources/cn/jiguang/bi/m.java:4`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/bi/m.java:36`
  `mVar.h = jSONObject.optDouble(com.umeng.analytics.pro.d.C);`
- `sources/cn/jiguang/bi/m.java:37`
  `mVar.i = jSONObject.optDouble(com.umeng.analytics.pro.d.D);`
- `sources/cn/jiguang/bi/m.java:82`
  `jSONObject.put(com.umeng.analytics.pro.d.C, this.h);`
- `sources/cn/jiguang/bi/m.java:83`
  `jSONObject.put(com.umeng.analytics.pro.d.D, this.i);`
- `sources/cn/jiguang/bi/n.java:61`
  `jSONObject.put(com.umeng.analytics.pro.d.C, this.f);`
- `sources/cn/jiguang/bi/n.java:62`
  `jSONObject.put(com.umeng.analytics.pro.d.D, this.g);`
- `sources/cn/jiguang/bj/n.java:3`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/bk/h.java:12`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/bp/a.java:4`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/bq/d.java:11`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/bq/h.java:56`
  `jSONObject3.put("sentry_envelope_item_header", d.a(com.umeng.analytics.pro.d.aw));`
- `sources/cn/jiguang/bq/h.java:121`
  `jSONObject2.put("sentry_envelope_item_header", d.a(com.umeng.analytics.pro.d.aw));`
- `sources/cn/jiguang/bq/i.java:11`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/bq/i.java:12`
  `import com.umeng.analytics.pro.cb;`
- `sources/cn/jiguang/bs/a.java:9`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/bu/c.java:4`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/bv/j.java:5`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/by/f.java:3`
  `import com.umeng.analytics.pro.cb;`
- `sources/cn/jiguang/c/a.java:15`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/c/b.java:31`
  `import com.umeng.analytics.pro.am;`
- `sources/cn/jiguang/ca/b.java:4`
  `import com.umeng.analytics.pro.cb;`

## BR042

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/com/alibaba/sdk/android/oss/common/RequestParameters.java:37`
  `public static final String UPLOAD_ID = "uploadId";`
- `sources/com/alibaba/sdk/android/oss/common/RequestParameters.java:38`
  `public static final String UPLOAD_ID_MARKER = "upload-id-marker";`
- `sources/com/alibaba/sdk/android/oss/common/utils/OSSUtils.java:57`
  `private static final List<String> a = Arrays.asList(RequestParameters.SUBRESOURCE_BUCKETINFO, RequestParameters.SUBRESOURCE_ACL, RequestParameters.SUBRESOURCE_UPLOADS, "location", RequestParameters.SUBRESOURCE_CORS, RequestParameters.SUBRESOURCE_LOGGING, RequestParameters.SUBRESOURCE_WEBSITE, Reques...`
- `sources/com/alibaba/sdk/android/oss/common/utils/OSSUtils.java:385`
  `map.put(RequestParameters.UPLOAD_ID_MARKER, listMultipartUploadsRequest.getUploadIdMarker());`

## BR043

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/cn/jiguang/o/d.java:4`
  `import android.net.wifi.ScanResult;`
- `sources/cn/jiguang/o/d.java:83`
  `List<ScanResult> scanResults = wifiManager.getScanResults();`
- `sources/cn/jiguang/o/d.java:84`
  `if (scanResults != null && scanResults.size() != 0) {`
- `sources/cn/jiguang/o/d.java:85`
  `cn.jiguang.r.a.b("JLocationWifi", "scan wifi list success:" + scanResults);`
- `sources/cn/jiguang/o/d.java:86`
  `ArrayList<ScanResult> arrayList2 = new ArrayList(scanResults);`
- `sources/cn/jiguang/o/d.java:87`
  `for (ScanResult scanResult : arrayList2) {`
- `sources/cn/jiguang/o/d.java:88`
  `if (!(cVar.b.equals(cn.jiguang.x.d.c(scanResult.SSID)) && cVar.e.equals(scanResult.BSSID)) && scanResult.level >= -200) {`
- `sources/cn/jiguang/o/d.java:89`
  `for (ScanResult scanResult2 : arrayList2) {`
- `sources/cn/jiguang/o/d.java:90`
  `if (scanResult2 != scanResult && scanResult.SSID.equals(scanResult2.SSID) && scanResult.BSSID.equals(scanResult2.BSSID)) {`
- `sources/cn/jiguang/o/d.java:91`
  `scanResults.remove(scanResult);`
- `sources/cn/jiguang/o/d.java:95`
  `scanResults.remove(scanResult);`
- `sources/cn/jiguang/o/d.java:99`
  `Collections.sort(scanResults, new Comparator<ScanResult>() { // from class: cn.jiguang.o.d.1`
- `sources/cn/jiguang/o/d.java:102`
  `public int compare(ScanResult scanResult3, ScanResult scanResult4) {`
- `sources/cn/jiguang/o/d.java:103`
  `return scanResult4.level - scanResult3.level;`
- `sources/cn/jiguang/o/d.java:106`
  `for (int i2 = 0; i2 < scanResults.size() && i2 != i - 1; i2++) {`
- `sources/cn/jiguang/o/d.java:107`
  `ScanResult scanResult3 = scanResults.get(i2);`
- `sources/cn/jiguang/o/d.java:108`
  `String strC = cn.jiguang.x.d.c(scanResult3.SSID);`
- `sources/cn/jiguang/o/d.java:116`
  `cVar2.d = scanResult3.level;`
- `sources/cn/jiguang/o/d.java:117`
  `cVar2.e = scanResult3.BSSID;`
- `sources/com/alibaba/fastjson/serializer/SerializeWriter.java:14`
  `import no.nordicsemi.android.support.v18.scanner.ScanResult;`
- `sources/com/alibaba/fastjson/serializer/SerializeWriter.java:74`
  `for (int i2 = ScanResult.TX_POWER_NOT_PRESENT; i2 < 160; i2++) {`
- `sources/com/alipay/android/phone/scancode/export/ScanCallback.java:7`
  `void onScanResult(boolean z, Intent intent);`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanCallback.java:11`
  `boolean onScanFinish(Context context, MPScanResult mPScanResult, MPScanStarter mPScanStarter);`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanner.java:26`
  `import com.alipay.mobile.mascanengine.MultiMaScanResult;`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanner.java:84`
  `this.scanHandler.setContext(context, new ScanHandler.ScanResultCallbackProducer() { // from class: com.alipay.android.phone.scancode.export.adapter.MPScanner.1`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanner.java:85`
  `@Override // com.alipay.android.phone.scancode.export.camera.ScanHandler.ScanResultCallbackProducer`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanner.java:86`
  `public BQCScanEngine.EngineCallback makeScanResultCallback(ScanType scanType) {`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanner.java:130`
  `public void onResultMa(MultiMaScanResult multiMaScanResult) {`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanner.java:132`
  `MPScanner.this.mpScanListener.onSuccess(MPScanResult.fromMaScanResult(multiMaScanResult.maScanResults[0]));`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanner.java:137`
  `public void onScanResultType(int i, MultiMaScanResult multiMaScanResult) {`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanner.java:211`
  `public void openCameraAndStartScan() {`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanner.java:334`
  `public MPScanResult scanFromBitmap(Bitmap bitmap) {`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanner.java:336`
  `return MPScanResult.fromMaScanResult(this.maPictureEngineService.process(bitmap));`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanner.java:370`
  `public void startScan() {`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanResult.java:3`
  `import com.alipay.mobile.mascanengine.MaScanResult;`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanResult.java:7`
  `public class MPScanResult {`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanResult.java:11`
  `/* JADX INFO: renamed from: com.alipay.android.phone.scancode.export.adapter.MPScanResult$1, reason: invalid class name */`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanResult.java:33`
  `private MPScanResult() {`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanResult.java:36`
  `public static MPScanResult fromMaScanResult(MaScanResult maScanResult) {`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanResult.java:37`
  `if (maScanResult == null) {`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanResult.java:40`
  `MPScanResult mPScanResult = new MPScanResult();`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanResult.java:41`
  `mPScanResult.text = maScanResult.text;`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanResult.java:42`
  `int i = AnonymousClass1.$SwitchMap$com$alipay$mobile$mascanengine$MaScanType[maScanResult.type.ordinal()];`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanResult.java:44`
  `mPScanResult.mpRecognizeType = MPRecognizeType.QR_CODE;`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanResult.java:46`
  `mPScanResult.mpRecognizeType = MPRecognizeType.PDF417_CODE;`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanResult.java:48`
  `mPScanResult.mpRecognizeType = MPRecognizeType.BAR_CODE;`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanResult.java:50`
  `mPScanResult.mpRecognizeType = MPRecognizeType.DM_CODE;`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanResult.java:52`
  `return mPScanResult;`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanService.java:8`
  `import com.alipay.mobile.mascanengine.MultiMaScanResult;`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanService.java:16`
  `void notifyScanFinish(Context context, MPScanResult mPScanResult, MPScanStarter mPScanStarter);`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanService.java:18`
  `void notifyScanResult(boolean z, Intent intent);`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanService.java:24`
  `MultiMaScanResult syncScanBitmapResultFromPath(String str);`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanService.java:26`
  `MultiMaScanResult syncScanBitmapResultFromPath(String str, String str2, String str3);`
- `sources/com/alipay/android/phone/scancode/export/adapter/MPScanService.java:28`
  `MultiMaScanResult syncScanBitmapResultFromPath(String str, String str2, String str3, String str4, boolean z);`
- `sources/com/alipay/android/phone/scancode/export/camera/ScanHandler.java:23`
  `private ScanResultCallbackProducer scanResultCallbackProducer;`
- `sources/com/alipay/android/phone/scancode/export/camera/ScanHandler.java:26`
  `public interface ScanResultCallbackProducer {`
- `sources/com/alipay/android/phone/scancode/export/camera/ScanHandler.java:27`
  `BQCScanEngine.EngineCallback makeScanResultCallback(ScanType scanType);`
- `sources/com/alipay/android/phone/scancode/export/camera/ScanHandler.java:69`
  `if (ScanHandler.this.scanResultCallbackProducer == null) {`
- `sources/com/alipay/android/phone/scancode/export/camera/ScanHandler.java:74`
  `mPaasScanService.regScanEngine(scanType.toBqcScanType(), MaScanEngineImpl.class, ScanHandler.this.scanResultCallbackProducer.makeScanResultCallback(scanType));`
- `sources/com/alipay/android/phone/scancode/export/camera/ScanHandler.java:83`
  `if (ScanHandler.this.scanResultCallbackProducer == null || 2 <= ScanHandler.this.curState) {`
- `sources/com/alipay/android/phone/scancode/export/camera/ScanHandler.java:88`
  `mPaasScanService.regScanEngine(scanType.toBqcScanType(), MaScanEngineImpl.class, ScanHandler.this.scanResultCallbackProducer.makeScanResultCallback(scanType));`
- `sources/com/alipay/android/phone/scancode/export/camera/ScanHandler.java:99`
  `ScanHandler.this.scanResultCallbackProducer = null;`
- `sources/com/alipay/android/phone/scancode/export/camera/ScanHandler.java:117`
  `public void setContext(final Context context, final ScanResultCallbackProducer scanResultCallbackProducer) {`
- `sources/com/alipay/android/phone/scancode/export/camera/ScanHandler.java:122`
  `ScanHandler.this.scanResultCallbackProducer = scanResultCallbackProducer;`
- `sources/com/alipay/android/phone/scancode/export/camera/ScanHandler.java:163`
  `if (ScanHandler.this.scanResultCallbackProducer == null) {`
- `sources/com/alipay/android/phone/scancode/export/camera/ScanHandler.java:168`
  `mPaasScanService.regScanEngine(scanType.toBqcScanType(), MaScanEngineImpl.class, ScanHandler.this.scanResultCallbackProducer.makeScanResultCallback(scanType));`
- `sources/com/alipay/android/phone/scancode/export/listener/MPScanListener.java:4`
  `import com.alipay.android.phone.scancode.export.adapter.MPScanResult;`
- `sources/com/alipay/android/phone/scancode/export/listener/MPScanListener.java:14`
  `void onSuccess(MPScanResult mPScanResult);`
- `sources/com/alipay/camera2/operation/callback/OnReadImageListener.java:18`
  `import com.alipay.mobile.bqcscanservice.BQCScanResult;`
- `sources/com/alipay/camera2/operation/callback/OnReadImageListener.java:89`
  `private class ScanTask extends BQCScanTask<BQCScanResult> {`
- `sources/com/alipay/camera2/operation/callback/OnReadImageListener.java:107`
  `protected BQCScanResult doInBackground() {`
- `sources/com/alipay/camera2/operation/callback/OnReadImageListener.java:109`
  `BQCScanResult bQCScanResultProcess;`
- `sources/com/alipay/camera2/operation/callback/OnReadImageListener.java:124`
  `bQCScanResultProcess = scanImagePlanesArr != null ? this.a.process(scanImagePlanesArr, rectAccess$1100, OnReadImageListener.this.n, this.mPreviewFormat) : null;`
- `sources/com/alipay/camera2/operation/callback/OnReadImageListener.java:126`
  `bQCScanResultProcess = this.a.process(bArr, rectAccess$1100, OnReadImageListener.this.n, this.strideWidth, this.mPreviewFormat);`
- `sources/com/alipay/camera2/operation/callback/OnReadImageListener.java:137`
  `return bQCScanResultProcess;`
- `sources/com/alipay/camera2/operation/callback/OnReadImageListener.java:167`
  `BQCScanResult bQCScanResultDoInBackground = doInBackground();`
- `sources/com/alipay/camera2/operation/callback/OnReadImageListener.java:173`
  `onPostExecute(bQCScanResultDoInBackground);`
- `sources/com/alipay/camera2/operation/callback/OnReadImageListener.java:186`
  `public void onPostExecute(BQCScanResult bQCScanResult) {`
- `sources/com/alipay/camera2/operation/callback/OnReadImageListener.java:190`
  `if (bQCScanEngine.onProcessFinish(bQCScanResult)) {`
- `sources/com/alipay/mobile/bqcscanservice/BQCScanEngine.java:70`
  `public abstract boolean onProcessFinish(BQCScanResult bQCScanResult);`

## BR044

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/androidx/core/content/ContextCompat.java:39`
  `import android.net.wifi.WifiManager;`
- `sources/androidx/core/content/ContextCompat.java:153`
  `map.put(WifiManager.class, "wifi");`
- `sources/cn/jiguang/aj/b.java:6`
  `import android.net.wifi.WifiManager;`
- `sources/cn/jiguang/aj/b.java:79`
  `WifiManager wifiManager = (WifiManager) context.getApplicationContext().getSystemService("wifi");`
- `sources/cn/jiguang/aj/b.java:80`
  `if (wifiManager == null) {`
- `sources/cn/jiguang/aj/b.java:81`
  `cn.jiguang.r.a.b("JArp", "collect arp failed because get wifiManager failed");`
- `sources/cn/jiguang/aj/b.java:90`
  `this.f = wifiManager.getDhcpInfo();`
- `sources/cn/jiguang/o/d.java:6`
  `import android.net.wifi.WifiManager;`
- `sources/cn/jiguang/o/d.java:27`
  `WifiManager wifiManager;`
- `sources/cn/jiguang/o/d.java:29`
  `if (Build.VERSION.SDK_INT < 29 || !cn.jiguang.ag.a.a().a(1608) || (wifiManager = (WifiManager) context.getApplicationContext().getSystemService("wifi")) == null) {`
- `sources/cn/jiguang/o/d.java:35`
  `for (WifiConfiguration wifiConfiguration : wifiManager.getConfiguredNetworks()) {`
- `sources/cn/jiguang/o/d.java:55`
  `WifiManager wifiManager = (WifiManager) this.a.getApplicationContext().getSystemService("wifi");`
- `sources/cn/jiguang/o/d.java:56`
  `if (wifiManager == null || !wifiManager.isWifiEnabled()) {`
- `sources/cn/jiguang/o/d.java:58`
  `cn.jiguang.r.a.f("JLocationWifi", "get wifiManager failed");`
- `sources/cn/jiguang/o/d.java:83`
  `List<ScanResult> scanResults = wifiManager.getScanResults();`
- `sources/com/alipay/sdk/data/b.java:7`
  `import android.net.wifi.WifiManager;`
- `sources/com/alipay/sdk/data/b.java:95`
  `WifiInfo connectionInfo = ((WifiManager) context.getApplicationContext().getSystemService("wifi")).getConnectionInfo();`
- `sources/com/alipay/sdk/data/b.java:156`
  `WifiInfo connectionInfo = ((WifiManager) context.getApplicationContext().getSystemService("wifi")).getConnectionInfo();`
- `sources/com/alipay/sdk/util/a.java:6`
  `import android.net.wifi.WifiManager;`
- `sources/com/alipay/sdk/util/a.java:19`
  `macAddress = ((WifiManager) context.getApplicationContext().getSystemService("wifi")).getConnectionInfo().getMacAddress();`
- `sources/com/alipay/security/mobile/module/b/b.java:12`
  `import android.net.wifi.WifiManager;`
- `sources/com/alipay/security/mobile/module/b/b.java:522`
  `macAddress = ((WifiManager) context.getSystemService("wifi")).getConnectionInfo().getMacAddress();`
- `sources/com/alipay/security/mobile/module/b/b.java:615`
  `WifiManager wifiManager;`
- `sources/com/alipay/security/mobile/module/b/b.java:620`
  `wifiManager = (WifiManager) context.getSystemService("wifi");`
- `sources/com/alipay/security/mobile/module/b/b.java:623`
  `String bssid = wifiManager.isWifiEnabled() ? wifiManager.getConnectionInfo().getBSSID() : "";`
- `sources/com/example/smartlinklib/SmartLinkManipulator.java:5`
  `import android.net.wifi.WifiManager;`
- `sources/com/example/smartlinklib/SmartLinkManipulator.java:279`
  `DhcpInfo dhcpInfo = ((WifiManager) context.getSystemService("wifi")).getDhcpInfo();`
- `sources/com/hiflying/smartlink/AbstractSmartLinkerActivity.java:14`
  `import android.net.wifi.WifiManager;`
- `sources/com/hiflying/smartlink/AbstractSmartLinkerActivity.java:142`
  `WifiManager wifiManager = (WifiManager) getSystemService("wifi");`
- `sources/com/hiflying/smartlink/AbstractSmartLinkerActivity.java:143`
  `if (wifiManager == null || (connectionInfo = wifiManager.getConnectionInfo()) == null) {`
- `sources/com/hiflying/smartlink/AbstractSmartLinkerFragment.java:14`
  `import android.net.wifi.WifiManager;`
- `sources/com/hiflying/smartlink/AbstractSmartLinkerFragment.java:146`
  `WifiManager wifiManager = (WifiManager) this.c.getSystemService("wifi");`
- `sources/com/hiflying/smartlink/AbstractSmartLinkerFragment.java:147`
  `if (wifiManager == null || (connectionInfo = wifiManager.getConnectionInfo()) == null) {`
- `sources/com/hiflying/smartlink/v3/SnifferSmartLinkerSendAction.java:5`
  `import android.net.wifi.WifiManager;`
- `sources/com/hiflying/smartlink/v3/SnifferSmartLinkerSendAction.java:50`
  `DhcpInfo dhcpInfo = ((WifiManager) context.getSystemService("wifi")).getDhcpInfo();`
- `sources/com/mico/wifi/EasyLinkWifiManager.java:6`
  `import android.net.wifi.WifiManager;`
- `sources/com/mico/wifi/EasyLinkWifiManager.java:10`
  `public class EasyLinkWifiManager {`
- `sources/com/mico/wifi/EasyLinkWifiManager.java:11`
  `private WifiManager a;`
- `sources/com/mico/wifi/EasyLinkWifiManager.java:15`
  `public EasyLinkWifiManager(Context context) {`
- `sources/com/mico/wifi/EasyLinkWifiManager.java:20`
  `WifiManager wifiManager = (WifiManager) context.getSystemService("wifi");`
- `sources/com/mico/wifi/EasyLinkWifiManager.java:21`
  `this.a = wifiManager;`
- `sources/com/mico/wifi/EasyLinkWifiManager.java:22`
  `this.b = wifiManager.getConnectionInfo();`
- `sources/com/mxchip/easylink/EasyLinkAPI.java:5`
  `import android.net.wifi.WifiManager;`
- `sources/com/mxchip/easylink/EasyLinkAPI.java:15`
  `private WifiManager b;`
- `sources/com/mxchip/easylink/EasyLinkAPI.java:37`
  `WifiManager wifiManager = (WifiManager) this.a.getSystemService("wifi");`
- `sources/com/mxchip/easylink/EasyLinkAPI.java:38`
  `this.b = wifiManager;`
- `sources/com/mxchip/easylink/EasyLinkAPI.java:39`
  `WifiInfo connectionInfo = wifiManager.getConnectionInfo();`
- `sources/com/mxchip/easylink/EasyLinkAPI.java:45`
  `WifiManager wifiManager = (WifiManager) this.a.getSystemService("wifi");`
- `sources/com/mxchip/easylink/EasyLinkAPI.java:46`
  `this.b = wifiManager;`
- `sources/com/mxchip/easylink/EasyLinkAPI.java:47`
  `WifiInfo connectionInfo = wifiManager.getConnectionInfo();`
- `sources/com/mxchip/easylink/WifiApManager.java:5`
  `import android.net.wifi.WifiManager;`
- `sources/com/mxchip/easylink/WifiApManager.java:11`
  `private final WifiManager a;`
- `sources/com/mxchip/easylink/WifiApManager.java:17`
  `WifiManager wifiManager = (WifiManager) context.getSystemService("wifi");`
- `sources/com/mxchip/easylink/WifiApManager.java:18`
  `this.a = wifiManager;`
- `sources/com/mxchip/easylink/WifiApManager.java:19`
  `this.b = wifiManager.getClass().getMethod("setWifiApEnabled", WifiConfiguration.class, Boolean.TYPE);`
- `sources/com/mxchip/easylink/WifiApManager.java:20`
  `this.c = wifiManager.getClass().getMethod("getWifiApConfiguration", null);`
- `sources/com/mxchip/easylink/WifiApManager.java:21`
  `this.d = wifiManager.getClass().getMethod("getWifiApState", new Class[0]);`
- `sources/com/mxchip/easylink_minus/EasyLink_minus.java:9`
  `import android.net.wifi.WifiManager;`
- `sources/com/mxchip/easylink_minus/EasyLink_minus.java:91`
  `WifiManager wifiManager = (WifiManager) this.a.getSystemService("wifi");`
- `sources/com/mxchip/easylink_minus/EasyLink_minus.java:92`
  `if (wifiManager == null || wifiManager.getConfiguredNetworks() == null) {`
- `sources/com/mxchip/easylink_minus/EasyLink_minus.java:95`
  `for (WifiConfiguration wifiConfiguration : wifiManager.getConfiguredNetworks()) {`
- `sources/com/mxchip/easylink_minus/EasyLink_minus.java:98`
  `wifiManager.removeNetwork(wifiConfiguration.networkId);`
- `sources/com/mxchip/easylink_minus/EasyLink_minus.java:99`
  `wifiManager.saveConfiguration();`
- `sources/com/mxchip/easylink_minus/EasyLink_minus.java:120`
  `WifiManager wifiManager = (WifiManager) this.a.getSystemService("wifi");`
- `sources/com/mxchip/easylink_minus/EasyLink_minus.java:140`
  `wifiManager.addNetwork(wifiConfiguration);`
- `sources/com/mxchip/easylink_minus/EasyLink_minus.java:141`
  `wifiManager.saveConfiguration();`
- `sources/com/mxchip/easylink_minus/EasyLink_minus.java:142`
  `for (WifiConfiguration wifiConfiguration2 : wifiManager.getConfiguredNetworks()) {`
- `sources/com/mxchip/easylink_minus/EasyLink_minus.java:151`
  `wifiManager.disableNetwork(iIntValue);`
- `sources/com/mxchip/easylink_minus/EasyLink_minus.java:152`
  `wifiManager.enableNetwork(iIntValue, false);`
- `sources/com/mxchip/easylink_minus/EasyLink_minus.java:153`
  `wifiManager.startScan();`
- `sources/com/mxchip/jmdns/JmdnsAPI.java:4`
  `import android.net.wifi.WifiManager;`
- `sources/com/mxchip/jmdns/JmdnsAPI.java:28`
  `private WifiManager c = null;`
- `sources/com/mxchip/jmdns/JmdnsAPI.java:29`
  `private WifiManager.MulticastLock d = null;`
- `sources/com/mxchip/jmdns/JmdnsAPI.java:128`
  `this.c = (WifiManager) this.a.getSystemService("wifi");`
- `sources/com/mxchip/jmdns/JmdnsAPI.java:130`
  `WifiManager.MulticastLock multicastLockCreateMulticastLock = this.c.createMulticastLock("mylock");`
- `sources/com/mxchip/jmdns/JmdnsAPI.java:147`
  `this.c = (WifiManager) this.a.getSystemService("wifi");`
- `sources/com/mxchip/utils/EasyLinkWifiManager.java:6`
  `import android.net.wifi.WifiManager;`
- `sources/com/mxchip/utils/EasyLinkWifiManager.java:10`
  `public class EasyLinkWifiManager {`
- `sources/com/mxchip/utils/EasyLinkWifiManager.java:11`
  `private WifiManager a;`
- `sources/com/mxchip/utils/EasyLinkWifiManager.java:15`
  `public EasyLinkWifiManager(Context context) {`

## BR047

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/android/support/v4/media/MediaBrowserCompat.java:83`
  `Log.w(MediaBrowserCompat.TAG, "Unhandled message: " + message + "\n  Client version: 1\n  Service version: " + message.arg1);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:92`
  `Log.e(MediaBrowserCompat.TAG, "Could not unparcel the data.");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:211`
  `Log.w(MediaBrowserCompat.TAG, "Unknown result code: " + i + " (extras=" + this.mExtras + ", resultData=" + bundle + ")");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:544`
  `Log.i(MediaBrowserCompat.TAG, "The connected service doesn't support sendCustomAction.");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:557`
  `Log.i(MediaBrowserCompat.TAG, "Remote error sending a custom action: action=" + str + ", extras=" + bundle, e);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:587`
  `Log.i(MediaBrowserCompat.TAG, "Remote error subscribing media item: " + str);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:922`
  `Log.d(MediaBrowserCompat.TAG, "  mServiceBinderWrapper=" + this.mServiceBinderWrapper);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:923`
  `Log.d(MediaBrowserCompat.TAG, "  mCallbacksMessenger=" + this.mCallbacksMessenger);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:924`
  `Log.d(MediaBrowserCompat.TAG, "  mRootId=" + this.mRootId);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:925`
  `Log.d(MediaBrowserCompat.TAG, "  mMediaSessionToken=" + this.mMediaSessionToken);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1074`
  `Log.w(MediaBrowserCompat.TAG, "onConnect from service while mState=" + getStateLabel(this.mState) + "... ignoring");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1128`
  `Log.i(MediaBrowserCompat.TAG, "Remote error sending a custom action: action=" + str + ", extras=" + bundle, e);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1153`
  `Log.d(MediaBrowserCompat.TAG, "addSubscription failed with RemoteException parentId=" + str);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:831`
  `Log.e(MediaControllerCompat.TAG, "Dead object in sendCustomAction.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:840`
  `Log.e(MediaControllerCompat.TAG, "Dead object in setRating.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:857`
  `Log.w(TAG, "Failed to create MediaControllerImpl.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:889`
  `Log.e(TAG, "Dead object in getMediaController.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1618`
  `Log.e(MediaControllerCompat.TAG, "Dead object in getPlaybackState.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1648`
  `Log.e(MediaControllerCompat.TAG, "Dead object in getRatingType.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1662`
  `Log.e(MediaControllerCompat.TAG, "Dead object in getRepeatMode.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1680`
  `Log.e(MediaControllerCompat.TAG, "Dead object in getShuffleMode.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1702`
  `Log.e(MediaControllerCompat.TAG, "Dead object in isCaptioningEnabled.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1725`
  `Log.e(MediaControllerCompat.TAG, "Dead object in registerCallback.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1743`
  `Log.e(MediaControllerCompat.TAG, "Dead object in registerCallback.", e);`
- `sources/android/support/v4/media/session/MediaControllerCompat.java:1784`
  `Log.e(MediaControllerCompat.TAG, "Dead object in unregisterCallback.", e);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1214`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1220`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR_OVERLAY id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2020`
  `Log.i("AppCompatDelegate", "Failed to instantiate custom view inflater " + string + ". Falling back to default.", th);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2190`
  `Log.i("AppCompatDelegate", "The Activity's LayoutInflater already has a Factory installed so we can not install AppCompat's");`
- `sources/androidx/appcompat/app/AppCompatViewInflater.java:165`
  `Log.i("AppCompatViewInflater", "app:theme is now deprecated. Please move to using android:theme instead.");`
- `sources/androidx/appcompat/app/c.java:172`
  `Log.e("ResourcesFlusher", "Could not retrieve value from ThemedResourceCache#mUnthemedEntries", e4);`
- `sources/androidx/appcompat/content/res/AppCompatResources.java:90`
  `Log.e("AppCompatResources", "Failed to inflate ColorStateList, leaving it to the framework", e);`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:128`
  `Log.w("SupportMenuInflater", "Cannot instantiate class: " + str, e);`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:161`
  `Log.w("SupportMenuInflater", "Ignoring attribute 'itemActionViewLayout'. Action view already specified.");`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:242`
  `Log.w("SupportMenuInflater", "Ignoring attribute 'actionProviderClass'. Action view already specified.");`
- `sources/androidx/appcompat/widget/m.java:115`
  `Log.w("SuggestionsAdapter", "Invalid icon resource " + iconResource + " for " + componentName.flattenToShortString());`
- `sources/androidx/appcompat/widget/m.java:118`
  `Log.w("SuggestionsAdapter", e.toString());`
- `sources/androidx/appcompat/widget/m.java:169`
  `Log.w("SuggestionsAdapter", "Icon not found: " + uri + ", " + e2.getMessage());`
- `sources/androidx/appcompat/widget/m.java:172`
  `Log.w("SuggestionsAdapter", "Icon not found: " + uri + ", " + e2.getMessage());`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:59`
  `Log.e("AsldcInflateDelegate", "Exception while inflating <animated-selector>", e);`

## BR050

paper_id: B021
paper_title: Metadata-Based Privacy Assessment for Mobile mHealth

- `audit_reports/02_rule_by_rule_mapping.md:51`
  `| BR025 | B005 / Mobile health and privacy | confirmed | 'uhealth.db' 普通 xUtils DbUtils 创建；表含血压、血糖、血氧、成员资料，未见 SQLCipher。 | B005/B002 均把健康数据本地未加密存储列为关键检查项。 |`
- `audit_reports/02_rule_by_rule_mapping.md:52`
  `| BR026 | B002 / accredited health app privacy | confirmed | SharedPreferences 保存 'access_token'、'refress_token'、'current_familymember'、设备名/MAC/last_obj 等，未见加密。 | B002 关注本地个人数据存储安全；证据足够。 |`
- `audit_reports/02_rule_by_rule_mapping.md:53`
  `| BR027 | B002 / accredited health app privacy | confirmed | 'Logger' 写 external-cache LOG；'CrashLog' 在外部存储可用时写 '/uhealth/*crash.txt'；'LogUploadUtil' 上传日志 zip。 | 确认日志/崩溃报告写到外部/外部缓存路径；不确认每个文件都有健康数据。 |`
- `audit_reports/02_rule_by_rule_mapping.md:54`
  `| BR028 | B014 / privacy assessment review | not_supported | Manifest 'allowBackup=false'。 | 备份弱配置未成立。 |`
- `audit_reports/02_rule_by_rule_mapping.md:68`
  `| BR050 | B021 / metadata privacy assessment | not_testable | Login 中有隐私/许可 URL，但未离线保存远程政策内容；无法判定死链。 | 需要打开/快照政策页面。 |`
- `audit_reports/02_rule_by_rule_mapping.md:69`
  `| BR051 | B013 / privacy policy availability | not_testable | 未提供隐私政策正文。 | 无法判断是否遗漏健康/设备/BLE 类别。 |`
- `audit_reports/02_rule_by_rule_mapping.md:70`
  `| BR052 | B013 / privacy policy availability | not_testable | 未提供隐私政策正文和运行时第三方流量。 | 无法判断第三方共享披露。 |`

## BR051

paper_id: B013
paper_title: Availability and quality of mobile health app privacy policies

- `audit_reports/02_rule_by_rule_mapping.md:8`
  `- B002《Unaddressed privacy risks in accredited health and wellness apps》：健康 App 本地存储、网络传输和隐私政策承诺之间应逐项核对；论文发现本地明文存储和未充分披露较常见。`
- `audit_reports/02_rule_by_rule_mapping.md:9`
  `- B005《Mobile health and privacy: cross sectional study》：大规模 mHealth 静态/动态分析显示第三方接收者、不安全传输、隐私政策不一致是核心问题。`
- `audit_reports/02_rule_by_rule_mapping.md:11`
  `- B007《Privacy Settings of Third-Party Libraries in Android Apps》：第三方库默认隐私设置、初始化时机和披露不一致是可审计问题。`
- `audit_reports/02_rule_by_rule_mapping.md:14`
  `- B016《A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps》：Android 静态/动态检查应覆盖 cleartext config、导出组件、BLE/位置权限、数据流。`
- `audit_reports/02_rule_by_rule_mapping.md:31`
  `| BR005 | B021 / Metadata-Based Privacy Assessment for Mobile mHealth | not_testable | 未提供应用商店描述、应用元数据或当前隐私标签。 | 需要元数据与权限对照，当前材料不足。 |`
- `audit_reports/02_rule_by_rule_mapping.md:32`
  `| BR006 | B016 / COVID Android app privacy-security | confirmed | Manifest 引用 network security config；'network_security_config.xml' 第 3 行设置全局 'cleartextTrafficPermitted="true"'。 | B016 将 cleartext policy 作为静态安全检查项；此配置本身足够确认。 |`
- `audit_reports/02_rule_by_rule_mapping.md:45`
  `| BR019 | B011 / mobile medication apps | supported_hypothesis | 'BGMeasurement' 有 'medicine' 字段，但语义更像餐前/餐后或服药状态，未见完整处方/剂量/提醒。 | B011 针对药物 App；当前只支持弱假设，不确认 medication privacy finding。 |`
- `audit_reports/02_rule_by_rule_mapping.md:46`
  `| BR020 | B012 / depression app privacy | not_supported | 未发现 mood/depression/anxiety/journal/survey 核心字段。 | 当前 App 不是心理健康日志类。 |`
- `audit_reports/02_rule_by_rule_mapping.md:51`
  `| BR025 | B005 / Mobile health and privacy | confirmed | 'uhealth.db' 普通 xUtils DbUtils 创建；表含血压、血糖、血氧、成员资料，未见 SQLCipher。 | B005/B002 均把健康数据本地未加密存储列为关键检查项。 |`
- `audit_reports/02_rule_by_rule_mapping.md:52`
  `| BR026 | B002 / accredited health app privacy | confirmed | SharedPreferences 保存 'access_token'、'refress_token'、'current_familymember'、设备名/MAC/last_obj 等，未见加密。 | B002 关注本地个人数据存储安全；证据足够。 |`
- `audit_reports/02_rule_by_rule_mapping.md:53`
  `| BR027 | B002 / accredited health app privacy | confirmed | 'Logger' 写 external-cache LOG；'CrashLog' 在外部存储可用时写 '/uhealth/*crash.txt'；'LogUploadUtil' 上传日志 zip。 | 确认日志/崩溃报告写到外部/外部缓存路径；不确认每个文件都有健康数据。 |`
- `audit_reports/02_rule_by_rule_mapping.md:54`
  `| BR028 | B014 / privacy assessment review | not_supported | Manifest 'allowBackup=false'。 | 备份弱配置未成立。 |`
- `audit_reports/02_rule_by_rule_mapping.md:62`
  `| BR040 | B007 / SDK privacy settings | confirmed | 'GlobalContext' preInit UMeng；'Startup' 无条件 Youzan init/preload；'initSdk()' 初始化 JPush/Udesk/UMeng/Youzan。 | B007 关注 SDK 初始化和默认隐私设置；静态 init before feature use 成立。 |`
- `audit_reports/02_rule_by_rule_mapping.md:63`
  `| BR041 | B007 / SDK privacy settings | supported_hypothesis | 未看到 Youzan/JPush/Udesk 完整 consent gate；JPush 有 'JCollectionAuth' 切换，Youzan preload 更早。 | 是否自动日志/跟踪需抓包，因此不 confirmed。 |`
- `audit_reports/02_rule_by_rule_mapping.md:68`
  `| BR050 | B021 / metadata privacy assessment | not_testable | Login 中有隐私/许可 URL，但未离线保存远程政策内容；无法判定死链。 | 需要打开/快照政策页面。 |`
- `audit_reports/02_rule_by_rule_mapping.md:69`
  `| BR051 | B013 / privacy policy availability | not_testable | 未提供隐私政策正文。 | 无法判断是否遗漏健康/设备/BLE 类别。 |`
- `audit_reports/02_rule_by_rule_mapping.md:70`
  `| BR052 | B013 / privacy policy availability | not_testable | 未提供隐私政策正文和运行时第三方流量。 | 无法判断第三方共享披露。 |`
- `audit_reports/02_rule_by_rule_mapping.md:100`
  `| BR076 | B005 / Mobile health and privacy | not_testable | 未提供启动抓包。 | 需要验证第三方请求是否早于登录或功能使用。 |`
- `audit_reports/02_rule_by_rule_mapping.md:101`
  `| BR077 | B007 / SDK privacy settings | not_testable | 静态上 Youzan/UMeng/JPush 有早期 init；无抓包无法确认 SDK traffic before consent。 | B007 强调动态行为和设置披露。 |`
- `audit_reports/02_rule_by_rule_mapping.md:118`
  `| BR092 | B005 / Mobile health and privacy | not_testable | 存在 JPush/UMeng/Youzan/Udesk 等 SDK；无流量证据显示 adid/deviceId/userId 到第三方。 | 需要抓包或 SDK runtime evidence。 |`
- `audit_reports/02_rule_by_rule_mapping.md:123`
  `| BR097 | B019 / pulse oximeter privacy | supported_hypothesis | 'OxyData' 含 SpO2、heartRate、memberId、deviceSN/MAC，并进入通用 sync 表流程。无抓包。 | 脉搏血氧数据与账号/设备关联的代码路径明确，但实际云接收需验证。 |`

## BR052

paper_id: B013
paper_title: Availability and quality of mobile health app privacy policies

- `audit_reports/02_rule_by_rule_mapping.md:8`
  `- B002《Unaddressed privacy risks in accredited health and wellness apps》：健康 App 本地存储、网络传输和隐私政策承诺之间应逐项核对；论文发现本地明文存储和未充分披露较常见。`
- `audit_reports/02_rule_by_rule_mapping.md:9`
  `- B005《Mobile health and privacy: cross sectional study》：大规模 mHealth 静态/动态分析显示第三方接收者、不安全传输、隐私政策不一致是核心问题。`
- `audit_reports/02_rule_by_rule_mapping.md:11`
  `- B007《Privacy Settings of Third-Party Libraries in Android Apps》：第三方库默认隐私设置、初始化时机和披露不一致是可审计问题。`
- `audit_reports/02_rule_by_rule_mapping.md:14`
  `- B016《A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps》：Android 静态/动态检查应覆盖 cleartext config、导出组件、BLE/位置权限、数据流。`
- `audit_reports/02_rule_by_rule_mapping.md:31`
  `| BR005 | B021 / Metadata-Based Privacy Assessment for Mobile mHealth | not_testable | 未提供应用商店描述、应用元数据或当前隐私标签。 | 需要元数据与权限对照，当前材料不足。 |`
- `audit_reports/02_rule_by_rule_mapping.md:32`
  `| BR006 | B016 / COVID Android app privacy-security | confirmed | Manifest 引用 network security config；'network_security_config.xml' 第 3 行设置全局 'cleartextTrafficPermitted="true"'。 | B016 将 cleartext policy 作为静态安全检查项；此配置本身足够确认。 |`
- `audit_reports/02_rule_by_rule_mapping.md:45`
  `| BR019 | B011 / mobile medication apps | supported_hypothesis | 'BGMeasurement' 有 'medicine' 字段，但语义更像餐前/餐后或服药状态，未见完整处方/剂量/提醒。 | B011 针对药物 App；当前只支持弱假设，不确认 medication privacy finding。 |`
- `audit_reports/02_rule_by_rule_mapping.md:46`
  `| BR020 | B012 / depression app privacy | not_supported | 未发现 mood/depression/anxiety/journal/survey 核心字段。 | 当前 App 不是心理健康日志类。 |`
- `audit_reports/02_rule_by_rule_mapping.md:51`
  `| BR025 | B005 / Mobile health and privacy | confirmed | 'uhealth.db' 普通 xUtils DbUtils 创建；表含血压、血糖、血氧、成员资料，未见 SQLCipher。 | B005/B002 均把健康数据本地未加密存储列为关键检查项。 |`
- `audit_reports/02_rule_by_rule_mapping.md:52`
  `| BR026 | B002 / accredited health app privacy | confirmed | SharedPreferences 保存 'access_token'、'refress_token'、'current_familymember'、设备名/MAC/last_obj 等，未见加密。 | B002 关注本地个人数据存储安全；证据足够。 |`
- `audit_reports/02_rule_by_rule_mapping.md:53`
  `| BR027 | B002 / accredited health app privacy | confirmed | 'Logger' 写 external-cache LOG；'CrashLog' 在外部存储可用时写 '/uhealth/*crash.txt'；'LogUploadUtil' 上传日志 zip。 | 确认日志/崩溃报告写到外部/外部缓存路径；不确认每个文件都有健康数据。 |`
- `audit_reports/02_rule_by_rule_mapping.md:54`
  `| BR028 | B014 / privacy assessment review | not_supported | Manifest 'allowBackup=false'。 | 备份弱配置未成立。 |`
- `audit_reports/02_rule_by_rule_mapping.md:62`
  `| BR040 | B007 / SDK privacy settings | confirmed | 'GlobalContext' preInit UMeng；'Startup' 无条件 Youzan init/preload；'initSdk()' 初始化 JPush/Udesk/UMeng/Youzan。 | B007 关注 SDK 初始化和默认隐私设置；静态 init before feature use 成立。 |`
- `audit_reports/02_rule_by_rule_mapping.md:63`
  `| BR041 | B007 / SDK privacy settings | supported_hypothesis | 未看到 Youzan/JPush/Udesk 完整 consent gate；JPush 有 'JCollectionAuth' 切换，Youzan preload 更早。 | 是否自动日志/跟踪需抓包，因此不 confirmed。 |`
- `audit_reports/02_rule_by_rule_mapping.md:68`
  `| BR050 | B021 / metadata privacy assessment | not_testable | Login 中有隐私/许可 URL，但未离线保存远程政策内容；无法判定死链。 | 需要打开/快照政策页面。 |`
- `audit_reports/02_rule_by_rule_mapping.md:69`
  `| BR051 | B013 / privacy policy availability | not_testable | 未提供隐私政策正文。 | 无法判断是否遗漏健康/设备/BLE 类别。 |`
- `audit_reports/02_rule_by_rule_mapping.md:70`
  `| BR052 | B013 / privacy policy availability | not_testable | 未提供隐私政策正文和运行时第三方流量。 | 无法判断第三方共享披露。 |`
- `audit_reports/02_rule_by_rule_mapping.md:100`
  `| BR076 | B005 / Mobile health and privacy | not_testable | 未提供启动抓包。 | 需要验证第三方请求是否早于登录或功能使用。 |`
- `audit_reports/02_rule_by_rule_mapping.md:101`
  `| BR077 | B007 / SDK privacy settings | not_testable | 静态上 Youzan/UMeng/JPush 有早期 init；无抓包无法确认 SDK traffic before consent。 | B007 强调动态行为和设置披露。 |`
- `audit_reports/02_rule_by_rule_mapping.md:110`
  `| BR088 | B004 / data sharing privacy | not_testable | 未提供第三方抓包与健康流程时间关联。 | 需要动态流量。 |`
- `audit_reports/02_rule_by_rule_mapping.md:118`
  `| BR092 | B005 / Mobile health and privacy | not_testable | 存在 JPush/UMeng/Youzan/Udesk 等 SDK；无流量证据显示 adid/deviceId/userId 到第三方。 | 需要抓包或 SDK runtime evidence。 |`
- `audit_reports/02_rule_by_rule_mapping.md:123`
  `| BR097 | B019 / pulse oximeter privacy | supported_hypothesis | 'OxyData' 含 SpO2、heartRate、memberId、deviceSN/MAC，并进入通用 sync 表流程。无抓包。 | 脉搏血氧数据与账号/设备关联的代码路径明确，但实际云接收需验证。 |`
- `resources/AndroidManifest.xml:48`
  `<uses-permission android:name="android.permission.ACCESS_NOTIFICATION_POLICY"/>`

## BR055

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `sources/androidx/core/util/PatternsCompat.java:29`
  `Pattern patternCompile3 = Pattern.compile("(?:(?:(?:[a-zA-Z0-9[ -\ud7ff豈-﷏ﷰ-\uffef𐀀-\u1fffd𠀀-\u2fffd𰀀-\u3fffd\u40000-\u4fffd\u50000-\u5fffd\u60000-\u6fffd\u70000-\u7fffd\u80000-\u8fffd\u90000-\u9fffd\ua0000-\uafffd\ub0000-\ubfffd\uc0000-\ucfffd\ud0000-\udfffd\ue1000-\uefffd&&[^ [\u2000-\u200a]\u2028...`
- `sources/com/elvishew/xlog/internal/util/ObjectToStringUtil.java:99`
  `sb.append("tel:xxx-xxx-xxxx");`
- `sources/com/elvishew/xlog/internal/util/ObjectToStringUtil.java:101`
  `sb.append("smsto:xxx-xxx-xxxx");`

## BR058

paper_id: B022
paper_title: A Study of Android Application Security

- `audit_reports/02_rule_by_rule_mapping.md:11`
  `- B007《Privacy Settings of Third-Party Libraries in Android Apps》：第三方库默认隐私设置、初始化时机和披露不一致是可审计问题。`

## BR060

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `sources/cn/jiguang/af/b.java:47`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/cn/jiguang/az/f.java:84`
  `return cn.jiguang.ca.f.b(str, c(), "RSA/ECB/PKCS1Padding");`
- `sources/cn/jiguang/be/a.java:23`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/cn/jiguang/ca/f.java:115`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/alipay/mobile/common/logging/util/RSAUtil.java:41`
  `java.lang.String r2 = "RSA/ECB/PKCS1Padding"`
- `sources/com/alipay/mobile/common/logging/util/RSAUtil.java:123`
  `java.lang.String r2 = "RSA/ECB/PKCS1Padding"`
- `sources/com/alipay/mobile/mascanengine/imagetrace/sec/RSAUtil.java:47`
  `java.lang.String r2 = "RSA/ECB/PKCS1Padding"`
- `sources/com/alipay/mobile/mascanengine/imagetrace/sec/RSAUtil.java:129`
  `java.lang.String r2 = "RSA/ECB/PKCS1Padding"`
- `sources/com/alipay/sdk/encrypt/d.java:22`
  `java.lang.String r1 = "RSA/ECB/PKCS1Padding"`
- `sources/com/alipay/security/mobile/module/a/a/c.java:32`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/alipay/security/mobile/module/a/a/c.java:81`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/ta/utdid2/a/a/a.java:37`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/ta/utdid2/a/a/a.java:44`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/vivo/push/util/a.java:47`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/vivo/push/util/f.java:21`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/xiaomi/push/h.java:26`
  `Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/xiaomi/push/service/bt.java:33`
  `Cipher cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding");`
- `sources/com/youzan/androidsdk/tool/AESUtils.java:11`
  `public static String CIP_INSTANCE = "AES/CBC/PKCS5Padding";`
- `sources/com/yuwell/uhealth/global/utils/EncryptUtil.java:56`
  `Cipher cipher = Cipher.getInstance("DES/ECB/NoPadding");`
- `sources/com/yuwell/uhealth/global/utils/EncryptUtil.java:85`
  `Cipher cipher = Cipher.getInstance("DES/ECB/PKCS7Padding");`
- `sources/udesk/core/utils/AES.java:64`
  `return new String(b("AES/CBC/PKCS5Padding", this.a, this.c, Base64Decoder.decodeToBytes(str)));`
- `sources/udesk/core/utils/AES.java:68`
  `return Base64Encoder.encode(a("AES/CBC/PKCS5Padding", this.a, this.c, bArr));`

## BR061

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/constraintlayout/motion/widget/KeyAttributes.java:278`
  `public void setValue(String str, Object obj) {`
- `sources/androidx/constraintlayout/motion/widget/KeyCycle.java:455`
  `public void setValue(String str, Object obj) {`
- `sources/androidx/constraintlayout/motion/widget/KeyTimeCycle.java:280`
  `public void setValue(String str, Object obj) {`
- `sources/androidx/lifecycle/LiveData.java:71`
  `LiveData.this.setValue(obj);`
- `sources/cn/jiguang/api/JCoreInterface.java:242`
  `public static void sendData(Context context, String str, int i, byte[] bArr) {`
- `sources/cn/jiguang/bk/h.java:553`
  `cn.jiguang.bd.d.j("JCoreTCPManager", "send hb failed:sendData is null");`
- `sources/cn/jiguang/bn/b.java:323`
  `d.c("NioSSLSocketClient", "sendData failed, send data was null");`
- `sources/cn/jiguang/bn/b.java:330`
  `d.c("NioSSLSocketClient", "sendData failed, data length must less than " + this.p);`
- `sources/cn/jiguang/bn/c.java:92`
  `d.i("NioSocketClient", "sendData failed, send data was null");`
- `sources/cn/jiguang/bn/c.java:99`
  `d.i("NioSocketClient", "sendData failed, data length must less than " + this.j);`
- `sources/cn/jpush/android/d/b.java:68`
  `JCoreHelper.sendData(context, JPushConstants.SDK_TYPE, 4, 3, j2, cn.jpush.android.z.b.a(0, (byte) i, j, str));`
- `sources/cn/jpush/android/helper/JCoreHelper.java:165`
  `public static void sendData(Context context, String str, int i, int i2, long j, byte[] bArr) {`
- `sources/com/alipay/mobile/common/logging/http/HttpClient.java:69`
  `String protocol = urlA.getProtocol();`
- `sources/com/contec/spo2/code/a/f.java:225`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/g.java:318`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/g.java:517`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/g.java:532`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/g.java:545`
  `sendData(com.contec.spo2.code.a.a.a(1, 1, this.I, this.J, 0));`
- `sources/com/contec/spo2/code/a/g.java:611`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/g.java:715`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/g.java:824`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/g.java:839`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/g.java:920`
  `r3.sendData(r4)`
- `sources/com/contec/spo2/code/a/g.java:982`
  `sendData(com.contec.spo2.code.a.a.l());`
- `sources/com/contec/spo2/code/a/g.java:1115`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/g.java:1128`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/g.java:1203`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/base/ContecDevice.java:386`
  `sendData(com.contec.spo2.code.a.a.a(1));`
- `sources/com/contec/spo2/code/base/ContecDevice.java:392`
  `sendData(com.contec.spo2.code.a.a.a(2));`
- `sources/com/contec/spo2/code/base/ContecDevice.java:398`
  `sendData(com.contec.spo2.code.a.a.a(3));`
- `sources/com/contec/spo2/code/base/ContecDevice.java:474`
  `public void sendData(byte[] bArr) {`
- `sources/com/contec/spo2/code/connect/a.java:183`
  `bluetoothGattCharacteristic.setValue(bArr);`
- `sources/com/mxchip/easylink_v2/EasyLink_v2.java:75`
  `sendData(new DatagramPacket(bytes, 20, new InetSocketAddress(InetAddress.getByName(e), c())), e);`
- `sources/com/mxchip/easylink_v2/EasyLink_v2.java:87`
  `sendData(new DatagramPacket(new byte[i4], i4, new InetSocketAddress(InetAddress.getByName(f), c())), f);`
- `sources/com/mxchip/easylink_v2/EasyLink_v2.java:102`
  `sendData(new DatagramPacket(new byte[i6], i6, new InetSocketAddress(InetAddress.getByName(f), c())), f);`
- `sources/com/rtk/btconfigbluetooth/BTBle/BTBle.java:518`
  `this.mBLEConfigCharacteristic.setValue(bArr);`
- `sources/com/rtk/btconfigbluetooth/BTBle/BTBle.java:519`
  `return this.bluetoothGatt.writeCharacteristic(this.mBLEConfigCharacteristic) ? 1 : -1;`
- `sources/com/xiaomi/push/bg.java:259`
  `if (cVar != null && (url.getProtocol().equals("http") || url.getProtocol().equals(com.alipay.sdk.cons.b.a))) {`
- `sources/com/xiaomi/push/bg.java:433`
  `if (!"http".equals(url.getProtocol())) {`
- `sources/com/xiaomi/push/cz.java:122`
  `arrayList.add(new URL(url.getProtocol(), dbVarA.m215a(), dbVarA.a(), url.getFile()).toString());`

## BR062

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/com/contec/spo2/code/connect/a.java:245`
  `if (this.g.setCharacteristicNotification(bluetoothGattCharacteristic, z) && (descriptor = bluetoothGattCharacteristic.getDescriptor(UUID.fromString("00002902-0000-1000-8000-00805f9b34fb"))) != null) {`
- `sources/com/rtk/btconfigbluetooth/BTBle/BTBle.java:110`
  `public void onCharacteristicChanged(BluetoothGatt bluetoothGatt, BluetoothGattCharacteristic bluetoothGattCharacteristic) {`
- `sources/com/rtk/btconfigbluetooth/BTBle/BTBle.java:114`
  `public void onCharacteristicRead(BluetoothGatt bluetoothGatt, BluetoothGattCharacteristic bluetoothGattCharacteristic, int i) {`
- `sources/com/rtk/btconfigbluetooth/BTBle/BTBle.java:115`
  `Log.i(BTBle.this.TAG, "onCharacteristicRead : " + i + " , " + Arrays.toString(bluetoothGattCharacteristic.getValue()));`
- `sources/com/rtk/btconfigbluetooth/BTBle/BTBle.java:117`
  `Log.w(BTBle.this.TAG, "onCharacteristicRead fail: " + i);`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:127`
  `public void onCharacteristicChanged(BluetoothGatt bluetoothGatt, BluetoothGattCharacteristic bluetoothGattCharacteristic) {`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:185`
  `public void onCharacteristicRead(final BluetoothGatt bluetoothGatt, BluetoothGattCharacteristic bluetoothGattCharacteristic, final int i) {`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:189`
  `BleManagerHandler.this.onCharacteristicRead(bluetoothGatt, bluetoothGattCharacteristic);`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:217`
  `Log.e("BleManager", "onCharacteristicRead error " + i);`

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
- `sources/cn/jiguang/a/a.java:40`
  `public static final String i = d.b(new byte[]{85, 118, 97, 33, 60, 84, 32, 0, 98, 46, 73, 85, 85, 116, 18, 44});`
- `sources/cn/jiguang/al/a.java:89`
  `cn.jiguang.r.a.f("JArpHelper", "execute command failed");`
- `sources/cn/jiguang/ax/a.java:179`
  `byte[] bytes = str.getBytes("UTF-8");`
- `sources/cn/jiguang/bf/f.java:118`
  `byte[] bArr = (byte[]) obj;`
- `sources/cn/jiguang/bf/f.java:232`
  `byte[] bytes = str.getBytes("UTF-8");`
- `sources/cn/jiguang/bi/c.java:81`
  `byte[] bArrA2 = cn.jiguang.bm.b.a(context, bArrA);`
- `sources/cn/jiguang/bj/o.java:97`
  `ByteBuffer[] byteBufferArr = {ByteBuffer.wrap(new byte[]{(byte) (bArr.length >>> 8), (byte) (bArr.length & 255)}), ByteBuffer.wrap(bArr)};`
- `sources/cn/jiguang/bk/h.java:549`
  `byte[] bArrA = cn.jiguang.bm.b.a(this.l, cn.jiguang.bm.b.a(lValueOf.longValue(), JConstants.tcpSessionId, jF, (short) 1, i));`
- `sources/cn/jiguang/bm/a.java:17`
  `byte[] bArr2 = new byte[20];`
- `sources/cn/udesk/UdeskUtil.java:479`
  `byte[] r2 = r5.toByteArray()     // Catch: java.lang.Throwable -> L5a java.lang.Exception -> L5c`
- `sources/cn/udesk/UdeskUtil.java:492`
  `byte[] r4 = r5.toByteArray()     // Catch: java.lang.Exception -> L58 java.lang.Throwable -> L6c`
- `sources/cn/udesk/UdeskUtil.java:496`
  `byte[] r5 = r5.toByteArray()     // Catch: java.lang.Exception -> L58 java.lang.Throwable -> L6c`
- `sources/cn/udesk/UdeskUtil.java:560`
  `byte[] r2 = r1.toByteArray()`
- `sources/cn/udesk/UdeskUtil.java:602`
  `byte[] r1 = r1.toByteArray()`
- `sources/cn/udesk/UdeskUtil.java:1409`
  `byte[] byteArray = byteArrayOutputStream.toByteArray();`
- `sources/cn/udesk/camera/CameraInterface.java:491`
  `byte[] byteArray = byteArrayOutputStream.toByteArray();`
- `sources/com/alibaba/sdk/android/oss/common/utils/CRC64.java:95`
  `update(new byte[]{(byte) (i & 255)}, 1);`
- `sources/com/alipay/android/phone/mrpc/core/z.java:46`
  `byte[] bArr = (byte[]) new j(this.e.a(), method, iIncrementAndGet, strValue, eVar.a(), z).a();`
- `sources/com/alipay/ma/decode/MaDecode.java:136`
  `byte[] bArr2 = new byte[(int) j];`
- `sources/com/alipay/mobile/bqcscanservice/impl/BQCScanController.java:1074`
  `byte[] bArrA = BQCScanController.this.a();`
- `sources/com/alipay/mobile/common/logging/uploader/BaseUploader.java:130`
  `byte[] bArrGzipDataByString = LoggingUtil.gzipDataByString(strB);`
- `sources/com/alipay/mobile/common/logging/uploader/BaseUploader.java:225`
  `byte[] bArrGzipDataByString = LoggingUtil.gzipDataByString(strB);`
- `sources/com/alipay/mobile/common/logging/util/MathUtil.java:6`
  `byte[] bArr = new byte[4];`
- `sources/com/alipay/mobile/common/nativecrash/CrashFilterUtils.java:165`
  `boolean z2 = "com.alipay.android.launcher.service.LauncherService".equals(str2) || "com.alipay.android.launcher.service.LauncherService$InnerService".equals(str2) || "com.alipay.android.phone.mobilesdk.apm.service.APMInnerService".equals(str2) || "org.rome.android.ipp.binder.IppService".equals(str2)...`
- `sources/com/alipay/mobile/mascanengine/MaEngineService.java:413`
  `Map imageInfoJ = MaDecode.getImageInfoJ(new byte[0], 0, 0, 0, 0, 0, 0, 0);`
- `sources/com/alipay/sdk/packet/c.java:23`
  `byte[] bytes = bVar.b().getBytes();`
- `sources/com/alipay/sdk/packet/c.java:24`
  `byte[] bytes2 = bVar.a().getBytes();`
- `sources/com/alipay/sdk/packet/c.java:45`
  `byte[] r2 = r6.a()     // Catch: java.lang.Throwable -> L5e java.lang.Exception -> L60`
- `sources/com/alipay/sdk/packet/c.java:68`
  `byte[] r2 = a(r3, r2, r7)     // Catch: java.lang.Exception -> L59 java.lang.Throwable -> L77`
- `sources/com/alipay/sdk/packet/c.java:72`
  `byte[] r2 = com.alipay.sdk.encrypt.b.b(r2)     // Catch: java.lang.Exception -> L59 java.lang.Throwable -> L77`
- `sources/com/alipay/sdk/packet/impl/e.java:31`
  `byte[] bArrA = com.alipay.sdk.encrypt.b.a(str.getBytes(Charset.forName("UTF-8")));`
- `sources/com/alipay/sdk/packet/impl/e.java:46`
  `byte[] bArrB = bVarA.c;`
- `sources/com/alipay/security/mobile/module/a/a/a.java:35`
  `byte[] r4 = com.alipay.security.mobile.module.a.a.a.b`
- `sources/com/alipay/security/mobile/module/a/a/a.java:49`
  `byte[] r6 = com.alipay.security.mobile.module.a.a.a.b`
- `sources/com/alipay/security/mobile/module/a/a/a.java:74`
  `byte[] r9 = r9.getBytes(r3)`

## BR064

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/collection/LruCache.java:175`
  `throw new java.lang.IllegalStateException(getClass().getName() + ".sizeOf() is reporting inconsistent results!");`
- `sources/androidx/core/app/NotificationCompat.java:2528`
  `bundle.putCharSequence(NotificationCompat.EXTRA_SELF_DISPLAY_NAME, this.e.getName());`
- `sources/androidx/core/app/NotificationCompat.java:2623`
  `return this.e.getName();`
- `sources/androidx/core/app/NotificationCompat.java:2820`
  `if (!TextUtils.isEmpty(person.getName())) {`
- `sources/androidx/core/util/DebugUtils.java:18`
  `if ((simpleName == null || simpleName.length() <= 0) && (iLastIndexOf = (simpleName = obj.getClass().getName()).lastIndexOf(46)) > 0) {`
- `sources/androidx/versionedparcelable/VersionedParcel.java:55`
  `Class<?> cls = Class.forName(objectStreamClass.getName(), false, a.class.getClassLoader());`
- `sources/androidx/versionedparcelable/VersionedParcel.java:91`
  `Class cls2 = this.mParcelizerCache.get(cls.getName());`
- `sources/androidx/versionedparcelable/VersionedParcel.java:95`
  `Class<?> cls3 = Class.forName(String.format("%s.%sParcelizer", cls.getPackage().getName(), cls.getSimpleName()), false, cls.getClassLoader());`
- `sources/androidx/versionedparcelable/VersionedParcel.java:96`
  `this.mParcelizerCache.put(cls.getName(), cls3);`
- `sources/androidx/versionedparcelable/VersionedParcel.java:133`
  `throw new IllegalArgumentException(t.getClass().getName() + " cannot be VersionedParcelled");`
- `sources/androidx/versionedparcelable/VersionedParcel.java:138`
  `Method method = this.mWriteCache.get(cls.getName());`
- `sources/androidx/versionedparcelable/VersionedParcel.java:145`
  `this.mWriteCache.put(cls.getName(), declaredMethod);`
- `sources/butterknife/ButterKnife.java:49`
  `String name = cls.getName();`
- `sources/cn/jiguang/be/b.java:33`
  `cn.jiguang.bd.d.c("UploadLogUtils", "url is : " + str + "\n fileName is : " + file.getName() + "\n param is : " + map.toString());`
- `sources/cn/jiguang/bf/f.java:764`
  `cn.jiguang.bd.d.c("ReportUtils", "save report types=" + set + " at " + string + File.separator + fileA.getName());`
- `sources/cn/jiguang/bf/f.java:821`
  `cn.jiguang.bd.d.c("ReportUtils", "save report types=" + set + " at " + string + File.separator + d.a(context, string, jSONObjectA2, false).getName());`
- `sources/cn/udesk/aac/livedata/FileLiveData.java:583`
  `name = new File(localPath).getName();`
- `sources/com/alibaba/sdk/android/oss/internal/ResponseParsers.java:523`
  `String name = xmlPullParserNewPullParser.getName();`
- `sources/com/alibaba/sdk/android/oss/internal/ResponseParsers.java:843`
  `String name2 = xmlPullParserNewPullParser.getName();`
- `sources/com/alibaba/sdk/android/oss/internal/ResponseParsers.java:944`
  `String name = xmlPullParserNewPullParser.getName();`
- `sources/com/alibaba/sdk/android/oss/internal/ResponseParsers.java:969`
  `String name = xmlPullParserNewPullParser.getName();`
- `sources/com/alibaba/sdk/android/oss/model/ListMultipartUploadsResult.java:86`
  `String name = xmlPullParserNewPullParser.getName();`
- `sources/com/alibaba/sdk/android/oss/model/ListMultipartUploadsResult.java:132`
  `if ("Upload".equals(xmlPullParserNewPullParser.getName())) {`
- `sources/com/alibaba/sdk/android/oss/model/ListMultipartUploadsResult.java:134`
  `} else if ("CommonPrefixes".equals(xmlPullParserNewPullParser.getName())) {`
- `sources/com/alipay/apmobilesecuritysdk/d/c.java:39`
  `jSONObject.put("mac", fVar.c());`
- `sources/com/alipay/mobile/common/logging/LogContextImpl.java:203`
  `sb.append(UncaughtExceptionCallback.class.getName());`
- `sources/com/alipay/mobile/common/logging/LogContextImpl.java:267`
  `if (ProcessInfo.ALIAS_MAIN.equalsIgnoreCase(Thread.currentThread().getName())) {`
- `sources/com/alipay/mobile/common/logging/MdapLogUploadManager.java:44`
  `return file.getName().compareTo(file2.getName());`
- `sources/com/alipay/mobile/common/logging/api/DeviceHWInfo.java:23`
  `String name = file.getName();`
- `sources/com/alipay/mobile/common/logging/appender/AppenderManager.java:69`
  `if (file != null && file.exists() && file.isFile() && (strArrSplit = file.getName().split("_")) != null && strArrSplit.length >= 3) {`
- `sources/com/alipay/mobile/common/logging/appender/MdapFileAppender.java:102`
  `return new File(file, LoggingUtil.getMdapStyleName(c().getName()));`
- `sources/com/alipay/mobile/common/logging/appender/MdapFileAppender.java:110`
  `return new File(file, LoggingUtil.getMdapStyleName(c().getName()));`
- `sources/com/alipay/mobile/common/logging/impl/StatisticalExceptionHandler.java:350`
  `logContext.syncAppendLogEvent(new LogEvent(LogCategory.CATEGORY_CRASH, null, LogEvent.Level.ERROR, new ExceptionRender(logContext).a(ExceptionID.MONITORPOINT_IGNORE_CRASH, strUserTrackReport, null, false, str3, Thread.currentThread().getName(), true)));`
- `sources/com/alipay/mobile/common/logging/strategy/StoreFloodManager.java:94`
  `LoggerFactory.getTraceLogger().debug(TAG, "hit dealy upload,rename from:" + file.getName() + ",to :" + file2.getName());`
- `sources/com/alipay/mobile/common/logging/uploader/BaseUploader.java:107`
  `if (file.getName().contains("flood") && !str3.contains("floodDischarge")) {`
- `sources/com/alipay/mobile/common/logging/uploader/BaseUploader.java:108`
  `LoggerFactory.getTraceLogger().debug(a, "send flood file after process restart,fileName:" + file.getName() + ",change event from:" + str3 + " to:floodDischarge_KP");`
- `sources/com/alipay/mobile/common/logging/uploader/BaseUploader.java:123`
  `intent.putExtra("file", file.getName());`
- `sources/com/alipay/mobile/common/logging/uploader/RpcUploader.java:64`
  `String name = file.getName();`
- `sources/com/alipay/mobile/common/nativecrash/CrashCombineUtils.java:153`
  `Log.w("CrashCombineUtils", "getLatestTombAndDelOld, latestTombFile = " + file3.getName());`
- `sources/com/alipay/mobile/common/nativecrash/CrashCombineUtils.java:160`
  `Log.w("CrashCombineUtils", "getLatestTombAndDelOld, delete useless file" + file5.getName() + " result:" + file5.delete());`
- `sources/com/bumptech/glide/Glide.java:258`
  `throw new IllegalStateException("Attempting to register a Glide v3 module. If you see this, you or one of your dependencies may be including Glide v3 even though you're using Glide v4. You'll need to find and remove (or update) the offending dependency. The v3 module name is: " + glideModule.getClas...`
- `sources/com/bumptech/glide/load/engine/p.java:42`
  `byte[] bytes = this.f.getName().getBytes(Key.CHARSET);`
- `sources/com/contec/spo2/code/connect/ContecSdk.java:64`
  `if (bluetoothDevice.getName() == null || ContecSdk.this.d == null) {`
- `sources/com/contec/spo2/code/connect/ContecSdk.java:178`
  `ContecDevice contecDeviceA = com.contec.spo2.code.b.b.a().a(a(bluetoothDevice.getName()));`
- `sources/com/google/android/material/animation/MotionSpec.java:147`
  `return '\n' + getClass().getName() + '{' + Integer.toHexString(System.identityHashCode(this)) + " timings: " + this.a + "}\n";`
- `sources/com/google/android/material/animation/MotionTiming.java:98`
  `return '\n' + getClass().getName() + '{' + Integer.toHexString(System.identityHashCode(this)) + " delay: " + getDelay() + " duration: " + getDuration() + " interpolator: " + getInterpolator().getClass() + " repeatCount: " + getRepeatCount() + " repeatMode: " + getRepeatMode() + "}\n";`
- `sources/com/google/gson/FieldNamingPolicy.java:25`
  `return field.getName();`
- `sources/com/google/gson/internal/bind/TypeAdapters.java:631`
  `throw new UnsupportedOperationException("Attempted to serialize java.lang.Class: " + cls.getName() + ". Forgot to register a type adapter?");`
- `sources/com/lidroid/xutils/db/converter/ColumnConverterFactory.java:92`
  `a.put(cls.getName(), columnConverter);`
- `sources/com/lidroid/xutils/db/sqlite/CursorUtils.java:19`
  `private static final String b = ForeignLazyLoader.class.getName();`
- `sources/com/lidroid/xutils/db/sqlite/CursorUtils.java:20`
  `private static final String c = FinderLazyLoader.class.getName();`
- `sources/com/mxchip/jmdns/JmdnsAPI.java:86`
  `sb.append(JmdnsAPI.this.f.getAddress());`
- `sources/com/mxchip/jmdns/JmdnsAPI.java:94`
  `JmdnsAPI.this.h = "{\"deviceName\":\"" + JmdnsAPI.this.f.getName() + "\",\"deviceMac\":\"" + deviceMac + "\",\"deviceIP\":\"" + deviceIP + "\",\"deviceMacbind\":\"" + binding + "\",\"hardwareID\":\"" + str + "\",\"fogProductID\":\"" + fogProductID + "\",\"isEasyLinkOK\":\"" + isEasylinkOK + "\",\"is...`
- `sources/com/mxchip/utils/EasyLinkTXTRecordUtil.java:53`
  `if (!"".equals(str) && str.contains("MAC")) {`
- `sources/com/mxchip/utils/EasyLinkTXTRecordUtil.java:54`
  `return str.substring(str.indexOf("MAC=") + 4, str.indexOf("MAC=") + 21);`
- `sources/com/mxchip/utils/EasyLinkTXTRecordUtil.java:66`
  `if (!"".equals(str) && str.contains("MAC")) {`
- `sources/com/mxchip/utils/EasyLinkTXTRecordUtil.java:67`
  `return deleteMacMark(str.substring(str.indexOf("MAC=") + 4, str.indexOf("MAC=") + 21));`
- `sources/com/mxchip/utils/EasyLinkTXTRecordUtil.java:76`
  `public static String setDeviceName(String str) {`
- `sources/com/rtk/btconfigbluetooth/BTBle/BTBle.java:75`
  `String name = device.getName();`
- `sources/com/rtk/btconfigbluetooth/BTBle/BTBle.java:89`
  `if (device.getName() != null) {`
- `sources/com/rtk/btconfigbluetooth/BTBle/BTBle.java:90`
  `BTBle.this.updateBTScanResults(device.getName(), device.getAddress(), rssi);`
- `sources/com/rtk/btconfigbluetooth/BTBle/BTBle.java:96`
  `if (device.getBondState() != 12 || device.getName() == null) {`
- `sources/com/rtk/btconfigbluetooth/BTBle/BTBle.java:99`
  `BTBle.this.updateBTScanResults(device.getName(), device.getAddress(), rssi);`
- `sources/com/tencent/mm/opensdk/modelmsg/SendMessageToWX.java:104`
  `bundle.putString(SCENE_DATA_OBJECT_KEY_IDENTIFIER, iWXSceneDataObject.getClass().getName());`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:386`
  `a = DeviceTypeEnum.MAC;`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:388`
  `MLog.i(LOG_TAG, "getDeviceId, MAC: " + strH);`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:414`
  `DeviceTypeEnum deviceTypeEnum = DeviceTypeEnum.MAC;`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:426`
  `MLog.i(LOG_TAG, "getDeviceId, MAC: " + strG);`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:462`
  `DeviceTypeEnum deviceTypeEnum2 = DeviceTypeEnum.MAC;`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:492`
  `DeviceTypeEnum deviceTypeEnum3 = DeviceTypeEnum.MAC;`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:502`
  `MLog.i(LOG_TAG, "getDeviceId, MAC: " + strH3);`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:526`
  `a = DeviceTypeEnum.MAC;`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:551`
  `DeviceTypeEnum deviceTypeEnum = DeviceTypeEnum.MAC;`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:564`
  `MLog.i(LOG_TAG, "getDeviceId, MAC: " + strG);`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:605`
  `DeviceTypeEnum deviceTypeEnum2 = DeviceTypeEnum.MAC;`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:635`
  `DeviceTypeEnum deviceTypeEnum3 = DeviceTypeEnum.MAC;`
- `sources/com/umeng/commonsdk/statistics/common/DeviceConfig.java:645`
  `MLog.i(LOG_TAG, "getDeviceId, MAC: " + strH3);`
- `sources/com/umeng/commonsdk/statistics/common/DeviceTypeEnum.java:8`
  `MAC("mac", "mac"),`
- `sources/com/umeng/umzid/c.java:35`
  `editorEdit.putString("mac", strB).commit();`
- `sources/com/yuwell/bluetooth/BluetoothService.java:437`
  `this.b = bluetoothDevice.getName();`

## BR065

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/com/contec/spo2/code/connect/a.java:149`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/no/nordicsemi/android/ble/BleManagerCallbacks.java:47`
  `void onServicesDiscovered(@NonNull BluetoothDevice bluetoothDevice, boolean z);`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:637`
  `public final void onServicesDiscovered(@NonNull final BluetoothGatt bluetoothGatt, int i) {`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:642`
  `Log.e("BleManager", "onServicesDiscovered error " + i);`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:674`
  `bleManagerCallbacks.onServicesDiscovered(bluetoothGatt.getDevice(), zIsOptionalServiceSupported);`

## BR066

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/com/contec/spo2/code/connect/a.java:245`
  `if (this.g.setCharacteristicNotification(bluetoothGattCharacteristic, z) && (descriptor = bluetoothGattCharacteristic.getDescriptor(UUID.fromString("00002902-0000-1000-8000-00805f9b34fb"))) != null) {`
- `sources/com/rtk/btconfigbluetooth/BTBle/BTBle.java:50`
  `UUID BTCONF_SERVICE_UUID = UUID.fromString("0000ff01-0000-1000-8000-00805f9b34fb");`
- `sources/com/rtk/btconfigbluetooth/BTBle/BTBle.java:51`
  `UUID BTCONF_BLECONFIG_UUID = UUID.fromString("00002a0d-0000-1000-8000-00805f9b34fb");`
- `sources/com/youzan/spiderman/utils/DeviceUuidFactory.java:25`
  `uuid = UUID.fromString(string);`
- `sources/com/yuwell/bluetooth/BluetoothService.java:22`
  `private static final UUID o = UUID.fromString("fa87c0d0-afac-11de-8a39-0800200c9a66");`
- `sources/com/yuwell/bluetooth/BluetoothService.java:23`
  `private static final UUID p = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:20`
  `public static final UUID BLOOD_GLUCOSE = UUID.fromString("00002A18-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:21`
  `public static final UUID GLUCOSE_MEASUREMENT_CONTEXT = UUID.fromString("00002A34-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:22`
  `public static final UUID GLUCOSE_MEASURE_TYPE = UUID.fromString("d618d001-6000-1000-8000-000000000000");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:38`
  `UUID uuidFromString = UUID.fromString("0000fff1-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:40`
  `WEIGHT_READ = UUID.fromString("0000fff4-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:41`
  `BODY_COMPOSITION_MEASUREMENT = UUID.fromString("00002A9C-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:42`
  `URINE_CONTEC_NOTIFY = UUID.fromString("0000ff02-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:43`
  `URINE_CONTEC_WRITE = UUID.fromString("0000ff01-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:44`
  `UART_RX_CHARACTERISTIC_UUID = UUID.fromString("6E400002-B5A3-F393-E0A9-E50E24DCCA9E");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:45`
  `UART_TX_CHARACTERISTIC_UUID = UUID.fromString("6E400003-B5A3-F393-E0A9-E50E24DCCA9E");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:47`
  `SP_TX = UUID.fromString("02feff01-6000-1000-8000-000000000000");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:48`
  `SP_RX = UUID.fromString("02feff02-6000-1000-8000-000000000000");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:49`
  `FFF2 = UUID.fromString("0000fff2-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:50`
  `MOX_READ = UUID.fromString("0000ffe2-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:51`
  `SP_TX1 = UUID.fromString("d618d001-6000-1000-8000-000000000000");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:21`
  `public static final UUID BLOOD_GLUCOSE_MEASUREMMENT = UUID.fromString("00001808-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:22`
  `public static final UUID BLOOD_GLUCOSE_MEASUREMMENT_TYPE = UUID.fromString("d618d000-6000-1000-8000-000000000000");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:33`
  `CURRENT_TIME = UUID.fromString("00001805-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:34`
  `HEALTH_THERMOMETER = UUID.fromString("00001809-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:35`
  `UUID uuidFromString2 = UUID.fromString("0000fff0-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:37`
  `BODY_COMPOSITION = UUID.fromString("0000181B-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:38`
  `URINE_CONTEC = UUID.fromString("0000ff12-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:39`
  `UART_SERVICE_UUID = UUID.fromString("6E400001-B5A3-F393-E0A9-E50E24DCCA9E");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:41`
  `FE60 = UUID.fromString("0000fe60-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:42`
  `D618D = UUID.fromString("d618d000-6000-1000-8000-000000000000");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:43`
  `MOX = UUID.fromString("0000e0ff-3c17-d293-8e48-14fe2e4da212");`
- `sources/com/yuwell/bluetooth/le/device/battery/BatteryManager.java:21`
  `private static final UUID s = UUID.fromString("0000180F-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/device/battery/BatteryManager.java:22`
  `private static final UUID t = UUID.fromString("00002A19-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/uhealth/global/utils/mox/MoxManager.java:83`
  `BluetoothGattService service = bluetoothGatt.getService(UUID.fromString("0000e0ff-3c17-d293-8e48-14fe2e4da212"));`
- `sources/com/yuwell/uhealth/global/utils/mox/MoxManager.java:85`
  `UUID uuidFromString = UUID.fromString("0000ffe1-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/uhealth/global/utils/mox/MoxManager.java:86`
  `UUID uuidFromString2 = UUID.fromString("0000ffe2-0000-1000-8000-00805f9b34fb");`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:27`
  `private static final UUID i = UUID.fromString("00002900-0000-1000-8000-00805f9b34fb");`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:28`
  `private static final UUID j = UUID.fromString("00002901-0000-1000-8000-00805f9b34fb");`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:29`
  `private static final UUID k = UUID.fromString("00002902-0000-1000-8000-00805f9b34fb");`

## BR067

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/com/github/mikephil/charting/charts/BarLineChartBase.java:846`
  `public void setPinchZoom(boolean z) {`
- `sources/com/yuwell/bluetooth/le/core/YUBleManager.java:37`
  `public Request createBond() {`
- `sources/com/yuwell/bluetooth/le/core/YUBleManager.java:38`
  `return super.createBond();`
- `sources/com/yuwell/uhealth/view/impl/data/ho/HoHomeFragment.java:1035`
  `this.b.barChart.setPinchZoom(false);`
- `sources/no/nordicsemi/android/ble/BleManager.java:171`
  `protected Request createBond() {`
- `sources/no/nordicsemi/android/ble/BleManager.java:172`
  `return createBondInsecure();`
- `sources/no/nordicsemi/android/ble/BleManager.java:177`
  `protected Request createBondInsecure() {`
- `sources/no/nordicsemi/android/ble/BleManager.java:178`
  `return Request.createBond().P(this.d);`
- `sources/no/nordicsemi/android/ble/BleManager.java:362`
  `protected Request removeBond() {`
- `sources/no/nordicsemi/android/ble/BleManager.java:363`
  `return Request.removeBond().P(this.d);`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1275`
  `Method method = bluetoothDevice.getClass().getMethod("removeBond", new Class[0]);`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1276`
  `L1(3, "device.removeBond() (hidden)");`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1718`
  `L1(3, "device.createBond()");`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1719`
  `return bluetoothDevice.createBond();`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1722`
  `Method method = bluetoothDevice.getClass().getMethod("createBond", new Class[0]);`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1723`
  `L1(3, "device.createBond() (hidden)");`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1978`
  `Request requestP = Request.createBond().P(this);`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1991`
  `m0(Request.removeBond().P(this));`
- `sources/no/nordicsemi/android/ble/Request.java:388`
  `public static SimpleRequest removeBond() {`

## BR068

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/cn/jiguang/bm/d.java:69`
  `return "[LoginResponse] - code:" + this.a + ",sid:" + this.b + ", serverVersion:" + this.g + ", sessionKey:" + this.h + ", serverTime:" + this.c + ", idc:" + this.d + ", connectInfo:" + this.i;`
- `sources/com/alipay/camera2/operation/Camera2ConfigurationUtils.java:182`
  `boolean zIsSessionKeys = camera2CharacteristicsCache.isSessionKeys(CaptureRequest.CONTROL_AE_TARGET_FPS_RANGE);`
- `sources/com/alipay/camera2/operation/Camera2ConfigurationUtils.java:183`
  `MPaasLogger.d(TAG, new Object[]{"setup3AControlsLocked set fps range:", range2, ", defaultFpsRange:", range, ", fpsRangeIsSessionKey:", Boolean.valueOf(zIsSessionKeys)});`
- `sources/com/alipay/camera2/operation/Camera2ConfigurationUtils.java:185`
  `if (range2 != null && range2 != range && !zIsSessionKeys) {`
- `sources/com/alipay/camera2/operation/Camera2Manager.java:590`
  `List<CaptureRequest.Key<?>> availableSessionKeys = this.v.getAvailableSessionKeys();`
- `sources/com/alipay/camera2/operation/Camera2Manager.java:591`
  `if (availableSessionKeys != null && availableSessionKeys.size() > 0) {`
- `sources/com/alipay/camera2/operation/Camera2Manager.java:592`
  `sb.append("###sessionKeySize=" + String.valueOf(availableSessionKeys.size()));`
- `sources/com/alipay/camera2/operation/Camera2Manager.java:593`
  `sb.append("###availableSessionKeys=" + availableSessionKeys);`
- `sources/com/alipay/camera2/util/Camera2CharacteristicsCache.java:352`
  `public List<CaptureRequest.Key<?>> getAvailableSessionKeys() {`
- `sources/com/alipay/camera2/util/Camera2CharacteristicsCache.java:503`
  `this.y = cameraCharacteristics.getAvailableSessionKeys();`
- `sources/com/alipay/camera2/util/Camera2CharacteristicsCache.java:624`
  `sb.append(", mAvailableSessionKeys=" + String.valueOf(this.y));`
- `sources/okhttp3/Challenge.java:13`
  `public final class Challenge {`
- `sources/okhttp3/Challenge.java:17`
  `public Challenge(String str, Map<String, String> map) {`
- `sources/okhttp3/Challenge.java:44`
  `if (obj instanceof Challenge) {`
- `sources/okhttp3/Challenge.java:45`
  `Challenge challenge = (Challenge) obj;`
- `sources/okhttp3/Challenge.java:46`
  `if (challenge.a.equals(this.a) && challenge.b.equals(this.b)) {`
- `sources/okhttp3/JavaNetAuthenticator.java:21`
  `List<Challenge> listChallenges = response.challenges();`
- `sources/okhttp3/JavaNetAuthenticator.java:26`
  `int size = listChallenges.size();`
- `sources/okhttp3/JavaNetAuthenticator.java:28`
  `Challenge challenge = listChallenges.get(i);`
- `sources/okhttp3/JavaNetAuthenticator.java:29`
  `if ("Basic".equalsIgnoreCase(challenge.scheme())) {`
- `sources/okhttp3/JavaNetAuthenticator.java:32`
  `passwordAuthenticationRequestPasswordAuthentication = java.net.Authenticator.requestPasswordAuthentication(inetSocketAddress.getHostName(), a(proxy, httpUrlUrl), inetSocketAddress.getPort(), httpUrlUrl.scheme(), challenge.realm(), challenge.scheme(), httpUrlUrl.url(), Authenticator.RequestorType.PRO...`
- `sources/okhttp3/JavaNetAuthenticator.java:34`
  `passwordAuthenticationRequestPasswordAuthentication = java.net.Authenticator.requestPasswordAuthentication(httpUrlUrl.host(), a(proxy, httpUrlUrl), httpUrlUrl.port(), httpUrlUrl.scheme(), challenge.realm(), challenge.scheme(), httpUrlUrl.url(), Authenticator.RequestorType.SERVER);`
- `sources/okhttp3/Response.java:82`
  `public List<Challenge> challenges() {`
- `sources/okhttp3/Response.java:93`
  `return HttpHeaders.parseChallenges(headers(), str);`
- `sources/okhttp3/internal/http/HttpHeaders.java:45`
  `private static void a(java.util.List<okhttp3.Challenge> r8, okio.Buffer r9) {`
- `sources/okhttp3/internal/http/HttpHeaders.java:252`
  `public static List<Challenge> parseChallenges(Headers headers, String str) {`

## BR069

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/com/umeng/commonsdk/utils/UMUtils.java:795`
  `Log.e("UMUtils", "get mac e is " + th);`
- `sources/com/umeng/umzid/c.java:35`
  `editorEdit.putString("mac", strB).commit();`
- `sources/com/yuwell/bluetooth/BluetoothService.java:448`
  `b bVar2 = new b(bluetoothDevice, z);`
- `sources/com/yuwell/uhealth/databinding/BindBleDeviceBinding.java:54`
  `this.mac = textView2;`
- `sources/com/yuwell/uhealth/global/utils/UHBleCallbacksHandler.java:443`
  `public void onOxygenDataRead(BluetoothDevice bluetoothDevice, BloodOxygenData bloodOxygenData) {`
- `sources/com/yuwell/uhealth/global/utils/UHBleCallbacksHandler.java:448`
  `public void onPulseWaveRead(BluetoothDevice bluetoothDevice, int i) {`
- `sources/com/yuwell/uhealth/global/utils/UHBleCallbacksHandler.java:460`
  `public void onScaleDataRead(BluetoothDevice bluetoothDevice, WeightData weightData) {`
- `sources/com/yuwell/uhealth/global/utils/UHBleCallbacksHandler.java:465`
  `bodyFatConvertWeightData.setDeviceSN(bluetoothDevice.getAddress().replace(Constants.COLON_SEPARATOR, ""));`
- `sources/com/yuwell/uhealth/global/utils/UHBleCallbacksHandler.java:474`
  `public void onScaleError(BluetoothDevice bluetoothDevice) {`
- `sources/com/yuwell/uhealth/view/impl/data/fht/FhtHome.java:104`
  `BluetoothDevice currConnectBlueDevice = GlobalContext.getInstance().getCurrConnectBlueDevice();`
- `sources/com/yuwell/uhealth/view/impl/data/fht/FhtHome.java:106`
  `fetalData.setTerminalSN(currConnectBlueDevice.getAddress().replace(Constants.COLON_SEPARATOR, ""));`
- `sources/com/yuwell/uhealth/view/impl/data/oxy/BoUtils.java:36`
  `private static BluetoothDevice c;`
- `sources/com/yuwell/uhealth/view/impl/device/BindBleDevice.java:42`
  `start(context, str, new ScannerLayout.BluetoothDeviceInfo(str2, 0), z, z2);`
- `sources/com/yuwell/uhealth/view/impl/device/BindBleDevice.java:76`
  `this.p.setProduct(getIntent().getStringExtra("id"), getIntent().getStringExtra("mac"), getIntent().getIntExtra("type", 0));`
- `sources/javax/jmdns/impl/DNSRecord.java:365`
  `for (byte b : this.i.getAddress()) {`
- `sources/javax/jmdns/impl/ServiceInfoImpl.java:275`
  `public InetAddress getAddress() {`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1784`
  `request.L(bluetoothDevice, -5);`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1791`
  `public /* synthetic */ void v1(Request request, BluetoothDevice bluetoothDevice) {`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1793`
  `request.O(bluetoothDevice);`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1797`
  `awaitingRequest.L(bluetoothDevice, -3);`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1846`
  `public /* synthetic */ void x1(SleepRequest sleepRequest, BluetoothDevice bluetoothDevice) {`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1847`
  `sleepRequest.O(bluetoothDevice);`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:88`
  `public void onDescriptorWriteRequest(@NonNull BluetoothDevice bluetoothDevice, int i, @NonNull BluetoothGattDescriptor bluetoothGattDescriptor, boolean z, boolean z2, int i2, @NonNull byte[] bArr) {`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:89`
  `BleManagerHandler bleManagerHandlerG = BleServerManager.this.g(bluetoothDevice);`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:91`
  `bleManagerHandlerG.T1(BleServerManager.this.a, bluetoothDevice, i, bluetoothGattDescriptor, z, z2, i2, bArr);`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:96`
  `public void onExecuteWrite(@NonNull BluetoothDevice bluetoothDevice, int i, boolean z) {`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:97`
  `BleManagerHandler bleManagerHandlerG = BleServerManager.this.g(bluetoothDevice);`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:99`
  `bleManagerHandlerG.V1(BleServerManager.this.a, bluetoothDevice, i, z);`
- `sources/okio/HashingSink.java:61`
  `return ByteString.of(messageDigest != null ? messageDigest.digest() : this.mac.doFinal());`
- `sources/okio/HashingSink.java:75`
  `this.mac.update(segment.data, segment.pos, iMin);`
- `sources/okio/HashingSink.java:86`
  `Mac mac = Mac.getInstance(str);`
- `sources/okio/HashingSink.java:87`
  `this.mac = mac;`
- `sources/okio/HashingSink.java:88`
  `mac.init(new SecretKeySpec(byteString.toByteArray(), str));`

## BR070

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/no/nordicsemi/android/ble/BleManager.java:460`
  `protected boolean shouldAutoConnect() {`

## BR072

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `resources/AndroidManifest.xml:507`
  `<action android:name="cn.jpush.android.intent.RECEIVE_MESSAGE"/>`
- `resources/AndroidManifest.xml:599`
  `android:name="cn.jpush.android.ui.PopWinActivity"`
- `resources/AndroidManifest.xml:603`
  `<action android:name="cn.jpush.android.ui.PopWinActivity"/>`
- `resources/AndroidManifest.xml:609`
  `android:name="cn.jpush.android.ui.PushActivity"`
- `resources/AndroidManifest.xml:613`
  `<action android:name="cn.jpush.android.ui.PushActivity"/>`
- `resources/AndroidManifest.xml:619`
  `android:name="cn.jpush.android.service.PushService"`
- `resources/AndroidManifest.xml:624`
  `<action android:name="cn.jpush.android.intent.REGISTER"/>`
- `resources/AndroidManifest.xml:625`
  `<action android:name="cn.jpush.android.intent.REPORT"/>`
- `resources/AndroidManifest.xml:626`
  `<action android:name="cn.jpush.android.intent.PushService"/>`
- `resources/AndroidManifest.xml:627`
  `<action android:name="cn.jpush.android.intent.PUSH_TIME"/>`
- `resources/AndroidManifest.xml:631`
  `android:name="cn.jpush.android.service.PushReceiver"`
- `resources/AndroidManifest.xml:635`
  `<action android:name="cn.jpush.android.intent.NOTIFICATION_RECEIVED_PROXY"/>`
- `resources/AndroidManifest.xml:640`
  `android:name="cn.jpush.android.service.AlarmReceiver"`
- `resources/AndroidManifest.xml:643`
  `android:name="cn.jpush.android.service.SchedulerReceiver"`
- `resources/AndroidManifest.xml:646`
  `android:name="cn.jpush.android.service.DataProvider"`
- `resources/AndroidManifest.xml:652`
  `android:name="cn.jpush.android.service.JNotifyActivity"`
- `resources/AndroidManifest.xml:656`
  `<action android:name="cn.jpush.android.intent.JNotifyActivity"/>`
- `resources/AndroidManifest.xml:672`
  `<receiver android:name="cn.jpush.android.asus.AsusPushMessageReceiver"/>`
- `resources/AndroidManifest.xml:680`
  `android:name="cn.jpush.android.service.InitProvider"`
- `resources/AndroidManifest.xml:684`
  `android:name="cn.jpush.android.service.PluginVivoMessageReceiver"`
- `resources/AndroidManifest.xml:709`
  `android:name="cn.jpush.android.service.PluginOppoPushService"`
- `resources/AndroidManifest.xml:759`
  `android:name="com.xiaomi.mipush.sdk.PushMessageHandler"`
- `resources/AndroidManifest.xml:763`
  `android:name="com.xiaomi.mipush.sdk.MessageHandleService"`
- `resources/AndroidManifest.xml:774`
  `android:name="cn.jpush.android.service.PluginXiaomiPlatformsReceiver"`
- `resources/AndroidManifest.xml:777`
  `<action android:name="com.xiaomi.mipush.RECEIVE_MESSAGE"/>`
- `resources/AndroidManifest.xml:780`
  `<action android:name="com.xiaomi.mipush.MESSAGE_ARRIVED"/>`
- `resources/AndroidManifest.xml:783`
  `<action android:name="com.xiaomi.mipush.ERROR"/>`
- `resources/AndroidManifest.xml:788`
  `android:name="com.xiaomi.mipush.sdk.NotificationClickedActivity"`
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
- `sources/androidx/appcompat/view/menu/SubMenuBuilder.java:12`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/androidx/constraintlayout/motion/widget/b.java:14`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/androidx/constraintlayout/motion/widget/Debug.java:9`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/androidx/constraintlayout/motion/widget/MotionController.java:19`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:45`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/androidx/constraintlayout/motion/widget/SplineSet.java:11`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/androidx/constraintlayout/motion/widget/TimeCycleSplineSet.java:12`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintAnchor.java:7`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/androidx/constraintlayout/solver/widgets/analyzer/DependencyNode.java:3`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/androidx/constraintlayout/widget/ConstraintHelper.java:22`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:25`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/androidx/constraintlayout/widget/ConstraintSet.java:26`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/androidx/core/app/NotificationManagerCompat.java:29`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/androidx/core/graphics/drawable/IconCompat.java:477`
  `if (str.contains(com.xiaomi.mipush.sdk.Constants.COLON_SEPARATOR)) {`
- `sources/androidx/core/graphics/drawable/IconCompat.java:478`
  `String str2 = str.split(com.xiaomi.mipush.sdk.Constants.COLON_SEPARATOR, -1)[1];`
- `sources/androidx/core/graphics/drawable/IconCompat.java:481`
  `String str5 = str.split(com.xiaomi.mipush.sdk.Constants.COLON_SEPARATOR, -1)[0];`
- `sources/androidx/core/graphics/drawable/IconCompat.java:530`
  `return ((String) this.a).split(com.xiaomi.mipush.sdk.Constants.COLON_SEPARATOR, -1)[0];`
- `sources/androidx/core/net/UriCompat.java:6`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/androidx/core/os/LocaleListCompat.java:10`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/androidx/core/text/util/LinkifyCompat.java:16`
  `import cn.jpush.android.local.JPushConstants;`
- `sources/androidx/fragment/app/Fragment.java:54`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/androidx/fragment/app/FragmentPagerAdapter.java:10`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/androidx/media/f.java:13`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/androidx/transition/Transition.java:27`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/androidx/vectordrawable/graphics/drawable/PathInterpolatorCompat.java:15`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/cn/android/service/JTransitActivity.java:6`
  `import cn.jpush.android.local.ActionHelper;`
- `sources/cn/com/lasong/media/MediaLog.java:4`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/cn/jiguang/a/a.java:24`
  `import cn.jpush.android.service.DataShare;`
- `sources/cn/jiguang/a/a.java:25`
  `import cn.jpush.android.service.JCommonService;`
- `sources/cn/jiguang/a/a.java:26`
  `import cn.jpush.android.service.PushReceiver;`
- `sources/cn/jiguang/ab/a.java:10`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/cn/jiguang/ad/d.java:15`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/cn/jiguang/ae/d.java:10`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/cn/jiguang/ag/a.java:13`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/cn/jiguang/an/b.java:11`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/cn/jiguang/an/c.java:7`
  `import cn.jpush.android.api.JPushInterface;`
- `sources/cn/jiguang/analytics/page/ActivityLifecycle.java:91`
  `return "cn.jpush.android.intent.DActivity".equals(activity.getIntent().getAction());`
- `sources/cn/jiguang/analytics/page/JOperateActivityLifecycle.java:11`
  `import cn.jpush.android.local.JPushConstants;`
- `sources/cn/jiguang/ao/a.java:17`
  `import cn.jpush.android.api.JThirdPlatFormInterface;`
- `sources/cn/jiguang/ao/a.java:20`
  `import com.xiaomi.mipush.sdk.Constants;`
- `sources/cn/jiguang/ao/a.java:162`
  `cn.jiguang.y.b.a(context, (cn.jiguang.y.a<?>[]) new cn.jiguang.y.a[]{new cn.jiguang.y.a("cn.jpush.preferences.v2", "n_udp_report_device_info", "").a(Base64.encodeToString(str.getBytes(), 2))});`
- `sources/cn/jiguang/ao/a.java:397`
  `String str2 = (String) cn.jiguang.y.b.b(context, new cn.jiguang.y.a("cn.jpush.preferences.v2", "n_udp_report_device_info", ""));`
- `sources/cn/jiguang/ao/a.java:399`
  `str = (String) cn.jiguang.y.b.b(context, new cn.jiguang.y.a("cn.jpush.preferences.v2", "udp_report_device_info", ""));`
- `sources/cn/jiguang/api/JCoreInterface.java:17`
  `public static String DAEMON_ACTION = "cn.jpush.android.intent.DaemonService";`

## BR073

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:609`
  `this.e.saveHierarchyState(sparseArray);`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:327`
  `java.lang.String r5 = r2.getAttributeValue(r6, r5)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:329`
  `java.lang.String r7 = r2.getAttributeValue(r6, r7)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:330`
  `long r7 = java.lang.Long.parseLong(r7)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:332`
  `java.lang.String r6 = r2.getAttributeValue(r6, r9)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:333`
  `float r6 = java.lang.Float.parseFloat(r6)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:334`
  `androidx.appcompat.widget.ActivityChooserModel$HistoricalRecord r9 = new androidx.appcompat.widget.ActivityChooserModel$HistoricalRecord     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:335`
  `r9.<init>(r5, r7, r6)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:336`
  `r3.add(r9)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/constraintlayout/motion/widget/DesignTool.java:92`
  `constraintSet.setVerticalBias(view.getId(), Float.parseFloat(str));`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:575`
  `sparseArray.put(((View) constraintWidget.getCompanionWidget()).getId(), constraintWidget);`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:583`
  `constraintSet.applyToHelper((ConstraintHelper) view, constraintWidget2, layoutParams, sparseArray);`
- `sources/androidx/constraintlayout/motion/widget/SplineSet.java:294`
  `return new b(str, sparseArray);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:426`
  `int i3 = Integer.parseInt(strArrSplit[0]);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:427`
  `int i4 = Integer.parseInt(strArrSplit[1]);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:428`
  `int i5 = Integer.parseInt(strArrSplit[2]);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:437`
  `float f4 = i7 + ((int) ((Integer.parseInt(strArrSplit[3]) / 1920.0f) * height));`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1054`
  `public static final SparseIntArray a;`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1057`
  `SparseIntArray sparseIntArray = new SparseIntArray();`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1084`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_goneMarginBottom, 24);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1085`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_goneMarginStart, 25);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1086`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_goneMarginEnd, 26);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1087`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHorizontal_bias, 29);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1088`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintVertical_bias, 30);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1089`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintDimensionRatio, 44);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1090`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHorizontal_weight, 45);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1091`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintVertical_weight, 46);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1092`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHorizontal_chainStyle, 47);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1093`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintVertical_chainStyle, 48);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1094`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constrainedWidth, 27);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1095`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constrainedHeight, 28);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1096`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintWidth_default, 31);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1097`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHeight_default, 32);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1098`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintWidth_min, 33);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1099`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintWidth_max, 34);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1100`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintWidth_percent, 35);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1101`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHeight_min, 36);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1102`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHeight_max, 37);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1103`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHeight_percent, 38);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1104`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintLeft_creator, 39);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1105`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintTop_creator, 40);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1106`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintRight_creator, 41);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1107`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintBottom_creator, 42);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1108`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintBaseline_creator, 43);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1649`
  `this.a = Float.parseFloat(strSubstring4);`
- `sources/androidx/constraintlayout/widget/ConstraintSet.java:284`
  `private static SparseIntArray a;`
- `sources/androidx/constraintlayout/widget/ConstraintSet.java:349`
  `SparseIntArray sparseIntArray = new SparseIntArray();`
- `sources/androidx/constraintlayout/widget/ConstraintSet.java:350`
  `a = sparseIntArray;`
- `sources/androidx/constraintlayout/widget/ConstraintSet.java:351`
  `sparseIntArray.append(R.styleable.Layout_layout_constraintLeft_toLeftOf, 24);`
- `sources/androidx/constraintlayout/widget/StateSet.java:128`
  `int eventType = xmlPullParser.getEventType();`
- `sources/androidx/constraintlayout/widget/StateSet.java:131`
  `xmlPullParser.getName();`
- `sources/androidx/constraintlayout/widget/StateSet.java:133`
  `String name = xmlPullParser.getName();`
- `sources/androidx/core/content/res/FontResourcesParserCompat.java:180`
  `private static FontFileResourceEntry d(XmlPullParser xmlPullParser, Resources resources) throws XmlPullParserException, IOException {`
- `sources/androidx/core/content/res/FontResourcesParserCompat.java:181`
  `TypedArray typedArrayObtainAttributes = resources.obtainAttributes(Xml.asAttributeSet(xmlPullParser), R.styleable.FontFamilyFont);`
- `sources/androidx/core/content/res/FontResourcesParserCompat.java:230`
  `arrayList.add(Base64.decode(str, 0));`
- `sources/androidx/core/content/res/FontResourcesParserCompat.java:245`
  `return b(xmlPullParser, resources);`
- `sources/androidx/core/content/res/FontResourcesParserCompat.java:247`
  `throw new XmlPullParserException("No start tag found");`
- `sources/androidx/core/graphics/b.java:106`
  `public Typeface createFromFontFamilyFilesResourceEntry(Context context, FontResourcesParserCompat.FontFamilyFilesResourceEntry fontFamilyFilesResourceEntry, Resources resources, int i) throws NoSuchMethodException {`
- `sources/androidx/core/graphics/b.java:108`
  `for (FontResourcesParserCompat.FontFileResourceEntry fontFileResourceEntry : fontFamilyFilesResourceEntry.getEntries()) {`
- `sources/androidx/core/graphics/c.java:14`
  `import androidx.core.content.res.FontResourcesParserCompat;`
- `sources/androidx/core/graphics/c.java:95`
  `public Typeface createFromFontFamilyFilesResourceEntry(Context context, FontResourcesParserCompat.FontFamilyFilesResourceEntry fontFamilyFilesResourceEntry, Resources resources, int i) {`
- `sources/androidx/core/graphics/c.java:100`
  `for (FontResourcesParserCompat.FontFileResourceEntry fontFileResourceEntry : fontFamilyFilesResourceEntry.getEntries()) {`
- `sources/androidx/core/graphics/d.java:48`
  `public int a(FontResourcesParserCompat.FontFileResourceEntry fontFileResourceEntry) {`
- `sources/androidx/core/graphics/d.java:54`
  `public boolean b(FontResourcesParserCompat.FontFileResourceEntry fontFileResourceEntry) {`
- `sources/androidx/core/graphics/d.java:187`
  `FontResourcesParserCompat.FontFamilyFilesResourceEntry d(Typeface typeface) {`
- `sources/androidx/core/graphics/TypefaceCompatApi26Impl.java:141`
  `for (FontResourcesParserCompat.FontFileResourceEntry fontFileResourceEntry : fontFamilyFilesResourceEntry.getEntries()) {`
- `sources/androidx/core/graphics/TypefaceCompatApi29Impl.java:34`
  `FontResourcesParserCompat.FontFileResourceEntry fontFileResourceEntry = entries[i2];`
- `sources/androidx/core/graphics/drawable/IconCompat.java:390`
  `return new BitmapDrawable(context.getResources(), BitmapFactory.decodeByteArray((byte[]) this.a, this.mInt1, this.mInt2));`
- `sources/androidx/core/graphics/drawable/IconCompat.java:394`
  `return new BitmapDrawable(context.getResources(), BitmapFactory.decodeStream(inputStreamI));`
- `sources/androidx/core/provider/FontsContractCompat.java:449`
  `return fontRequest.getCertificates() != null ? fontRequest.getCertificates() : FontResourcesParserCompat.readCerts(resources, fontRequest.getCertificatesArrayResId());`
- `sources/androidx/databinding/ViewDataBinding.java:908`
  `protected static byte parse(String str, byte b2) {`
- `sources/androidx/databinding/ViewDataBinding.java:910`
  `return Byte.parseByte(str);`
- `sources/androidx/databinding/ViewDataBinding.java:991`
  `return Integer.parseInt(str);`
- `sources/androidx/databinding/ViewDataBinding.java:1011`
  `protected static <T> T getFromList(androidx.collection.LongSparseArray<T> longSparseArray, int i2) {`
- `sources/androidx/databinding/ViewDataBinding.java:1012`
  `if (longSparseArray == null || i2 < 0) {`
- `sources/androidx/print/PrintHelper.java:439`
  `options2.inJustDecodeBounds = true;`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:350`
  `ColorStateList namedColorStateList = TypedArrayUtils.getNamedColorStateList(typedArray, xmlPullParser, theme, "tint", 1);`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:354`
  `hVar.e = TypedArrayUtils.getNamedBoolean(typedArray, xmlPullParser, "autoMirrored", 5, hVar.e);`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:355`
  `gVar.k = TypedArrayUtils.getNamedFloat(typedArray, xmlPullParser, "viewportWidth", 7, gVar.k);`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:356`
  `float namedFloat = TypedArrayUtils.getNamedFloat(typedArray, xmlPullParser, "viewportHeight", 8, gVar.l);`

## BR074

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/android/support/v4/media/session/MediaControllerCompat.java:1494`
  `synchronized (mediaControllerImplApi21.mLock) {`
- `sources/android/support/v4/os/ResultReceiver.java:99`
  `synchronized (this) {`
- `sources/androidx/appcompat/R.java:1727`
  `public static final int[] SearchView = {android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.inputType, android.R.attr.imeOptions, com.yuwell.uhealth.R.attr.closeIcon, com.yuwell.uhealth.R.attr.commitIcon, com.yuwell.uhealth.R.attr.defaultQueryHint, com.yuwell.uhealth.R.attr.goIcon, com...`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:606`
  `intentFilter.addAction("android.os.action.POWER_SAVE_MODE_CHANGED");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:612`
  `return (Build.VERSION.SDK_INT < 21 || !this.c.isPowerSaveMode()) ? 1 : 2;`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:100`
  `canvas.save();`
- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:609`
  `this.e.saveHierarchyState(sparseArray);`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:468`
  `synchronized (this.a) {`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:479`
  `synchronized (this.a) {`
- `sources/androidx/appcompat/widget/AppCompatRatingBar.java:21`
  `protected synchronized void onMeasure(int i, int i2) {`
- `sources/androidx/appcompat/widget/AppCompatSpinner.java:703`
  `SavedState savedState = (SavedState) parcelable;`
- `sources/androidx/appcompat/widget/f.java:90`
  `int iSave = canvas.save();`
- `sources/androidx/appcompat/widget/f.java:96`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/appcompat/widget/i.java:345`
  `synchronized (rectF) {`
- `sources/androidx/appcompat/widget/i.java:413`
  `ViewCompat.saveAttributeDataForStyleable(textView, textView.getContext(), iArr, attributeSet, typedArrayObtainStyledAttributes, i, 0);`
- `sources/androidx/appcompat/widget/SwitchCompat.java:482`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/appcompat/widget/Toolbar.java:975`
  `if (!(parcelable instanceof SavedState)) {`
- `sources/androidx/cardview/widget/c.java:30`
  `int iSave = canvas.save();`
- `sources/androidx/cardview/widget/c.java:42`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/cardview/widget/g.java:114`
  `int iSave = canvas.save();`
- `sources/androidx/cardview/widget/g.java:131`
  `int iSave3 = canvas.save();`
- `sources/androidx/cardview/widget/g.java:139`
  `canvas.restoreToCount(iSave3);`
- `sources/androidx/cardview/widget/g.java:140`
  `int iSave4 = canvas.save();`
- `sources/androidx/cardview/widget/g.java:148`
  `canvas.restoreToCount(iSave4);`
- `sources/androidx/collection/LruCache.java:175`
  `throw new java.lang.IllegalStateException(getClass().getName() + ".sizeOf() is reporting inconsistent results!");`
- `sources/androidx/collection/LruCache.java:232`
  `java.lang.String r1 = ".sizeOf() is reporting inconsistent results!"`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:493`
  `canvas.save();`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:802`
  `int iSave = canvas.save();`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:807`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/core/provider/FontsContractCompat.java:508`
  `public static Typeface getFontSync(Context context, FontRequest fontRequest, @Nullable ResourcesCompat.FontCallback fontCallback, @Nullable Handler handler, boolean z, int i, int i2) {`
- `sources/androidx/core/widget/NestedScrollView.java:681`
  `int iSave = canvas.save();`
- `sources/androidx/core/widget/NestedScrollView.java:701`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/core/widget/NestedScrollView.java:706`
  `int iSave2 = canvas.save();`
- `sources/androidx/core/widget/NestedScrollView.java:725`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/databinding/library/baseAdapters/R.java:1689`
  `public static final int[] SearchView = {android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.inputType, android.R.attr.imeOptions, com.yuwell.uhealth.R.attr.closeIcon, com.yuwell.uhealth.R.attr.commitIcon, com.yuwell.uhealth.R.attr.defaultQueryHint, com.yuwell.uhealth.R.attr.goIcon, com...`
- `sources/androidx/drawerlayout/widget/DrawerLayout.java:718`
  `int iSave = canvas.save();`
- `sources/androidx/drawerlayout/widget/DrawerLayout.java:743`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/fragment/app/FragmentActivity.java:250`
  `this.mFragments.noteStateNotSaved();`
- `sources/androidx/fragment/app/FragmentActivity.java:295`
  `Log.w(TAG, "Invalid requestCode mapping in savedInstanceState.");`
- `sources/androidx/fragment/app/FragmentActivity.java:406`
  `this.mFragments.noteStateNotSaved();`
- `sources/androidx/fragment/app/FragmentActivity.java:443`
  `Parcelable parcelableSaveAllState = this.mFragments.saveAllState();`
- `sources/androidx/fragment/app/FragmentActivity.java:444`
  `if (parcelableSaveAllState != null) {`
- `sources/androidx/fragment/app/FragmentActivity.java:445`
  `bundle.putParcelable(FRAGMENTS_TAG, parcelableSaveAllState);`
- `sources/androidx/loader/content/ModernAsyncTask.java:23`
  `abstract class ModernAsyncTask<Params, Progress, Result> {`
- `sources/androidx/loader/content/ModernAsyncTask.java:48`
  `return new Thread(runnable, "ModernAsyncTask #" + this.a.getAndIncrement());`
- `sources/androidx/loader/content/ModernAsyncTask.java:68`
  `ModernAsyncTask.this.e.set(true);`
- `sources/androidx/loader/content/ModernAsyncTask.java:72`
  `result = (Result) ModernAsyncTask.this.b(this.a);`
- `sources/androidx/loader/content/ModernAsyncTask.java:198`
  `public final ModernAsyncTask<Params, Progress, Result> c(Executor executor, Params... paramsArr) {`
- `sources/androidx/media/session/MediaButtonReceiver.java:142`
  `BroadcastReceiver.PendingResult pendingResultGoAsync = goAsync();`
- `sources/androidx/media/session/MediaButtonReceiver.java:144`
  `a aVar = new a(applicationContext, intent, pendingResultGoAsync);`
- `sources/androidx/navigation/ui/R.java:1206`
  `public static final int transition_layout_save = 0x7f090624;`
- `sources/androidx/navigation/ui/R.java:2134`
  `public static final int BottomSheetBehavior_Layout_behavior_saveFlags = 0x00000008;`
- `sources/androidx/navigation/ui/R.java:2674`
  `public static final int[] BottomSheetBehavior_Layout = {android.R.attr.elevation, com.yuwell.uhealth.R.attr.backgroundTint, com.yuwell.uhealth.R.attr.behavior_draggable, com.yuwell.uhealth.R.attr.behavior_expandedOffset, com.yuwell.uhealth.R.attr.behavior_fitToContents, com.yuwell.uhealth.R.attr.beh...`
- `sources/androidx/print/PrintHelper.java:81`
  `@Override // android.os.AsyncTask`
- `sources/androidx/print/PrintHelper.java:208`
  `class a extends AsyncTask<Uri, Boolean, Bitmap> {`
- `sources/androidx/print/PrintHelper.java:234`
  `@Override // android.os.AsyncTask`
- `sources/androidx/print/PrintHelper.java:260`
  `synchronized (this) {`
- `sources/androidx/print/PrintHelper.java:324`
  `synchronized (this) {`
- `sources/androidx/recyclerview/widget/AsyncListDiffer.java:101`
  `AsyncListDiffer asyncListDiffer = AsyncListDiffer.this;`
- `sources/androidx/recyclerview/widget/DividerItemDecoration.java:38`
  `canvas.save();`
- `sources/androidx/recyclerview/widget/DividerItemDecoration.java:61`
  `canvas.save();`
- `sources/androidx/recyclerview/widget/LinearLayoutManager.java:26`
  `SavedState D;`
- `sources/androidx/recyclerview/widget/RecyclerView.java:5264`
  `int iSave = canvas.save();`
- `sources/androidx/recyclerview/widget/RecyclerView.java:5270`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/recyclerview/widget/RecyclerView.java:5295`
  `int iSave4 = canvas.save();`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:435`
  `int iSave = canvas.save();`
- `sources/androidx/viewpager/widget/ViewPager.java:1238`
  `int iSave = canvas.save();`
- `sources/androidx/viewpager/widget/ViewPager.java:1245`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/viewpager/widget/ViewPager.java:1248`
  `int iSave2 = canvas.save();`
- `sources/androidx/viewpager/widget/ViewPager.java:1255`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/viewpager2/widget/ViewPager2.java:925`
  `if (!(parcelable instanceof SavedState)) {`
- `sources/cn/jiguang/ax/g.java:53`
  `cn.jiguang.bd.d.i("JBannedConfig", "can't get url, give up upload");`
- `sources/cn/jiguang/ax/g.java:65`
  `str = "upload" + jSONObject.toString() + " error:" + gVarA.b();`
- `sources/cn/jiguang/ax/h.java:58`
  `cn.jiguang.bd.d.i("JLimitConfig", "can't get url, give up upload");`
- `sources/cn/jiguang/ax/h.java:70`
  `str = "upload" + jSONObject.toString() + " error:" + gVarA.b();`
- `sources/cn/jiguang/bd/a.java:96`
  `d.c("LogFileHelper", "request upload token success,response body:" + responseBody);`
- `sources/cn/jiguang/be/b.java:33`
  `cn.jiguang.bd.d.c("UploadLogUtils", "url is : " + str + "\n fileName is : " + file.getName() + "\n param is : " + map.toString());`
- `sources/cn/jiguang/be/b.java:72`
  `cn.jiguang.bd.d.c("UploadLogUtils", "response code is " + responseCode + ", response message is " + httpResponseHttpPost.toString());`
- `sources/cn/jiguang/be/b.java:77`
  `cn.jiguang.bd.d.c("UploadLogUtils", "error message is : " + th.getMessage());`
- `sources/cn/jiguang/be/b.java:84`
  `cn.jiguang.bd.d.c("UploadLogUtils", "UploadFile response is : " + responseBody);`

## BR075

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/android/support/v4/media/RatingCompat.java:9`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:48`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/android/support/v4/media/session/PlaybackStateCompat.java:12`
  `import com.alipay.sdk.util.g;`
- `sources/androidx/appcompat/R.java:1347`
  `public static final int AppCompatTextView_autoSizePresetSizes = 0x00000003;`
- `sources/androidx/appcompat/R.java:1708`
  `public static final int[] AppCompatTextView = {android.R.attr.textAppearance, com.yuwell.uhealth.R.attr.autoSizeMaxTextSize, com.yuwell.uhealth.R.attr.autoSizeMinTextSize, com.yuwell.uhealth.R.attr.autoSizePresetSizes, com.yuwell.uhealth.R.attr.autoSizeStepGranularity, com.yuwell.uhealth.R.attr.auto...`
- `sources/androidx/appcompat/app/ActionBar.java:20`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/appcompat/app/ActionBarDrawerToggle.java:21`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/appcompat/app/AlertController.java:39`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/appcompat/graphics/drawable/AnimatedStateListDrawableCompat.java:38`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:16`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/appcompat/widget/AbsActionBarView.java:18`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:36`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/appcompat/widget/ActionMenuView.java:25`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:11`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/appcompat/widget/AppCompatButton.java:190`
  `public void setAutoSizeTextTypeUniformWithPresetSizes(@NonNull int[] iArr, int i) throws IllegalArgumentException {`
- `sources/androidx/appcompat/widget/AppCompatButton.java:192`
  `super.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:246`
  `public void setAutoSizeTextTypeUniformWithPresetSizes(@NonNull int[] iArr, int i) throws IllegalArgumentException {`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:248`
  `super.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/f.java:14`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/appcompat/widget/ForwardingListener.java:10`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/appcompat/widget/h.java:17`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/appcompat/widget/i.java:26`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/appcompat/widget/i.java:396`
  `textPaint.reset();`
- `sources/androidx/appcompat/widget/i.java:424`
  `int i6 = R.styleable.AppCompatTextView_autoSizePresetSizes;`
- `sources/androidx/appcompat/widget/LinearLayoutCompat.java:18`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/appcompat/widget/o.java:12`
  `import com.alipay.sdk.app.PayTask;`
- `sources/androidx/appcompat/widget/ScrollingTabContainerView.java:32`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/appcompat/widget/SearchView.java:156`
  `return "SearchView.SavedState{" + Integer.toHexString(System.identityHashCode(this)) + " isIconified=" + this.b + com.alipay.sdk.util.g.d;`
- `sources/androidx/appcompat/widget/SwitchCompat.java:35`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/appcompat/widget/ToolbarWidgetWrapper.java:28`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/cardview/widget/c.java:11`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/cardview/widget/CardView.java:18`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/cardview/widget/g.java:17`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/constraintlayout/motion/widget/b.java:12`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/constraintlayout/motion/widget/c.java:9`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:392`
  `this.d.reset();`
- `sources/androidx/constraintlayout/solver/ArrayLinkedVariables.java:4`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/constraintlayout/solver/ArrayRow.java:5`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/constraintlayout/solver/ArrayRow.java:389`
  `public void reset() {`
- `sources/androidx/constraintlayout/solver/LinearSystem.java:6`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/constraintlayout/solver/LinearSystem.java:83`
  `solverVariableAcquire.reset();`
- `sources/androidx/constraintlayout/solver/LinearSystem.java:654`
  `constraintAnchor.resetSolverVariable(this.k);`
- `sources/androidx/constraintlayout/solver/LinearSystem.java:660`
  `solverVariable.reset();`
- `sources/androidx/constraintlayout/solver/LinearSystem.java:689`
  `arrayRowAcquire.reset();`
- `sources/androidx/constraintlayout/solver/LinearSystem.java:874`
  `public void reset() {`
- `sources/androidx/constraintlayout/solver/LinearSystem.java:885`
  `solverVariable.reset();`
- `sources/androidx/constraintlayout/solver/Metrics.java:51`
  `public void reset() {`
- `sources/androidx/constraintlayout/solver/PriorityGoalRow.java:4`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/constraintlayout/solver/SolverVariable.java:3`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/constraintlayout/solver/SolverVariableValues.java:4`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/constraintlayout/solver/widgets/Barrier.java:7`
  `import com.alipay.sdk.util.g;`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintAnchor.java:365`
  `public void resetFinalResolution() {`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintAnchor.java:370`
  `public void resetSolverVariable(Cache cache) {`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintAnchor.java:375`
  `solverVariable.reset();`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:12`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1117`
  `public void resetFinalResolution() {`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1122`
  `this.mAnchors.get(i).resetFinalResolution();`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1126`
  `public void resetSolverVariables(Cache cache) {`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1127`
  `this.mLeft.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1128`
  `this.mTop.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1129`
  `this.mRight.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1130`
  `this.mBottom.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1131`
  `this.mBaseline.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1132`
  `this.mCenter.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1133`
  `this.o.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1134`
  `this.p.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidgetContainer.java:9`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/constraintlayout/solver/widgets/WidgetContainer.java:63`
  `public void reset() {`
- `sources/androidx/constraintlayout/solver/widgets/WidgetContainer.java:65`
  `super.reset();`
- `sources/androidx/constraintlayout/solver/widgets/WidgetContainer.java:69`
  `public void resetSolverVariables(Cache cache) {`
- `sources/androidx/constraintlayout/solver/widgets/WidgetContainer.java:70`
  `super.resetSolverVariables(cache);`
- `sources/androidx/constraintlayout/solver/widgets/WidgetContainer.java:73`
  `this.mChildren.get(i).resetSolverVariables(cache);`
- `sources/androidx/constraintlayout/solver/widgets/analyzer/BasicMeasure.java:250`
  `boolean zDirectMeasureSetup = constraintWidgetContainer.directMeasureSetup(zEnabled);`
- `sources/androidx/constraintlayout/solver/widgets/analyzer/BasicMeasure.java:252`
  `zDirectMeasureWithOrientation2 = zDirectMeasureSetup & constraintWidgetContainer.directMeasureWithOrientation(zEnabled, 0);`
- `sources/androidx/constraintlayout/solver/widgets/analyzer/BasicMeasure.java:255`
  `zDirectMeasureWithOrientation2 = zDirectMeasureSetup;`
- `sources/androidx/constraintlayout/solver/widgets/analyzer/WidgetGroup.java:70`
  `linearSystem.reset();`
- `sources/androidx/constraintlayout/solver/widgets/analyzer/WidgetGroup.java:93`
  `linearSystem.reset();`
- `sources/androidx/constraintlayout/solver/widgets/analyzer/WidgetGroup.java:97`
  `linearSystem.reset();`
- `sources/androidx/constraintlayout/utils/widget/ImageFilterButton.java:19`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`
- `sources/androidx/constraintlayout/utils/widget/ImageFilterView.java:21`
  `import com.alipay.camera2.operation.Camera2ConfigurationUtils;`

## BR076

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `resources/AndroidManifest.xml:19`
  `<uses-feature`
- `resources/AndroidManifest.xml:35`
  `<uses-feature android:name="android.hardware.camera"/>`
- `resources/AndroidManifest.xml:36`
  `<uses-feature android:name="android.hardware.camera.autofocus"/>`
- `resources/AndroidManifest.xml:165`
  `android:name="com.yuwell.uhealth.view.impl.main.Login"`
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
- `resources/org/apache/commons/codec/language/bm/lang.txt:66`
  `field$ english true`
- `resources/org/apache/commons/codec/language/bm/lang.txt:267`
  `v[^aoeiu] german false // in german, "v" can be found before a vowel only`
- `resources/org/apache/commons/codec/language/bm/lang.txt:268`
  `y[^aoeiu] german false  // in german, "y" usually appears only in the last position; sometimes before a vowel`
- `resources/res/values/public.xml:6089`
  `<public type="layout" name="login" id="0x7f0c0126" />`
- `resources/res/values/public.xml:6453`
  `<public type="string" name="before" id="0x7f10008a" />`
- `resources/res/values/public.xml:6914`
  `<public type="string" name="login" id="0x7f100257" />`
- `resources/res/values/strings.xml:141`
  `<string name="before">前</string>`
- `resources/res/values/strings.xml:602`
  `<string name="login">登录</string>`
- `resources/res/values-en/strings.xml:75`
  `<string name="udesk_gps_downfile_tips">Currently in a non Wi-Fi environment, download a file consumes a certain amount of traffic. Do you want to continue?</string>`
- `resources/res/values-en/strings.xml:76`
  `<string name="udesk_gps_tips">Currently in a non Wi-Fi environment, sending a file consumes a certain amount of traffic. Do you want to continue?</string>`
- `resources/res/values-en/strings.xml:83`
  `<string name="udesk_has_uncomplete_tip">Download first, then click</string>`
- `resources/res/values-en/strings.xml:87`
  `<string name="udesk_im_time_format_dby">The day before yesterday</string>`
- `sources/androidx/activity/ComponentActivity.java:61`
  `throw new IllegalStateException("getLifecycle() returned null in ComponentActivity's constructor. Please make sure you are lazily constructing your Lifecycle in the first call to getLifecycle() rather than relying on field initialization.");`
- `sources/androidx/activity/ComponentActivity.java:97`
  `throw new IllegalStateException("Your activity is not yet attached to the Application instance. You can't request ViewModel before onCreate call.");`
- `sources/androidx/activity/ComponentActivity.java:137`
  `throw new IllegalStateException("Your activity is not yet attached to the Application instance. You can't request ViewModel before onCreate call.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1214`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1220`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR_OVERLAY id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1240`
  `throw new AndroidRuntimeException("Window feature must be requested before adding content");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2531`
  `throw new IllegalStateException("This Activity already has an action bar supplied by the window decor. Do not request Window.FEATURE_SUPPORT_ACTION_BAR and set windowActionBar to false in your theme to use a Toolbar instead.");`
- `sources/androidx/media/MediaBrowserServiceCompat.java:109`
  `throw new IllegalArgumentException("The value of the EXTRA_DOWNLOAD_PROGRESS field must be a float number within [0.0, 1.0].");`
- `sources/androidx/media/MediaBrowserServiceCompat.java:1247`
  `if (iBinder == pair.first && MediaBrowserCompatUtils.areSameOptions(bundle, pair.second)) {`
- `sources/androidx/media/MediaBrowserServiceCompat.java:1304`
  `throw new IllegalStateException("onCustomAction must call detach() or sendResult() or sendError() before returning for action=" + str + " extras=" + bundle);`
- `sources/androidx/media/MediaBrowserServiceCompat.java:1323`
  `throw new IllegalStateException("onLoadChildren must call detach() or sendResult() before returning for package=" + eVar.a + " id=" + str);`
- `sources/androidx/media/MediaBrowserServiceCompat.java:1334`
  `throw new IllegalStateException("onLoadItem must call detach() or sendResult() before returning for id=" + str);`
- `sources/androidx/media/MediaBrowserServiceCompat.java:1345`
  `throw new IllegalStateException("onSearch must call detach() or sendResult() before returning for query=" + str);`
- `sources/androidx/media/MediaBrowserServiceCompat.java:1372`
  `if (iBinder == it2.next().first) {`
- `sources/androidx/navigation/NavController.java:172`
  `if (bundle2 != null && (stringArrayList = bundle2.getStringArrayList("android-support-nav:controller:navigatorState:names")) != null) {`
- `sources/androidx/navigation/NavController.java:272`
  `throw new IllegalStateException("You must call setGraph() before calling getGraph()");`
- `sources/androidx/navigation/NavController.java:291`
  `throw new IllegalStateException("You must call setViewModelStore() before calling getViewModelStoreOwner().");`
- `sources/androidx/navigation/NavController.java:499`
  `bundle2.putStringArrayList("android-support-nav:controller:navigatorState:names", arrayList);`
- `sources/androidx/navigation/NavController.java:540`
  `throw new IllegalStateException("You must call setLifecycleOwner() before calling setOnBackPressedDispatcher()");`
- `sources/androidx/recyclerview/widget/RecyclerView.java:2508`
  `throw new IllegalArgumentException("Tmp detached view should be removed from RecyclerView before it can be recycled: " + viewHolder + RecyclerView.this.J());`
- `sources/androidx/recyclerview/widget/RecyclerView.java:2511`
  `throw new IllegalArgumentException("Trying to recycle an ignored view holder. You should first call stopIgnoringView(view) before calling recycle." + RecyclerView.this.J());`
- `sources/androidx/recyclerview/widget/RecyclerView.java:4185`
  `Log.e("RecyclerView", "Problem while matching changed view holders with the newones. The pre-layout information for the change holder " + viewHolder2 + " cannot be found but it is necessary for " + viewHolder + J());`
- `sources/cn/carbswang/android/numberpickerview/library/NumberPickerView.java:1320`
  `throw new IllegalArgumentException("mMaxValue - mMinValue + 1 should not be greater than mDisplayedValues.length, now ((mMaxValue - mMinValue + 1) is " + ((this.w - this.v) + 1) + " newDisplayedValues.length is " + strArr.length + ", you need to set MaxValue and MinValue before setDisplayedValues(St...`
- `sources/cn/carbswang/android/numberpickerview/library/NumberPickerView.java:1329`
  `throw new IllegalArgumentException("mDisplayedValues should not be null, you need to set mDisplayedValues first.");`
- `sources/cn/jiguang/an/e.java:36`
  `cn.jiguang.r.a.f("JDeviceIp", "request i config failed, " + th.getMessage());`
- `sources/cn/jiguang/an/e.java:39`
  `cn.jiguang.r.a.f("JDeviceIp", "request i config failed because can't get appKey");`
- `sources/cn/jiguang/an/e.java:44`
  `cn.jiguang.r.a.f("JDeviceIp", "request i config failed because can't get uid");`
- `sources/cn/jiguang/an/e.java:48`
  `cn.jiguang.r.a.f("JDeviceIp", "request i config failed because need register first");`
- `sources/cn/jiguang/an/e.java:64`
  `cn.jiguang.r.a.b("JDeviceIp", "request i config, url: " + str + ", paramJson: " + jSONObject);`
- `sources/cn/jiguang/an/e.java:77`
  `cn.jiguang.r.a.b("JDeviceIp", "request i config code:" + iB);`
- `sources/cn/jiguang/an/e.java:121`
  `cn.jiguang.r.a.b("JDeviceIp", "request i config success,response body:" + strA);`
- `sources/cn/jiguang/ax/g.java:41`
  `cn.jiguang.bd.d.i("JBannedConfig", "request bannedConfig failed because can't get appKey");`
- `sources/cn/jiguang/ax/g.java:51`
  `cn.jiguang.bd.d.c("JBannedConfig", "request url: " + str2 + ", param json:" + jSONObject.toString());`
- `sources/cn/jiguang/ax/g.java:88`
  `cn.jiguang.bd.d.c("JBannedConfig", "start request sdk banned config");`
- `sources/cn/jiguang/ax/g.java:91`
  `cn.jiguang.bd.d.i("JBannedConfig", "request banned config failed, code: " + iA);`
- `sources/cn/jiguang/ax/g.java:151`
  `cn.jiguang.bd.d.c("JSDKBannedHelper", "[isSDKBanned] first request banned config");`
- `sources/cn/jiguang/ax/g.java:159`
  `cn.jiguang.bd.d.c("JSDKBannedHelper", "request sdk banned config not time up, not request");`
- `sources/cn/jiguang/ax/g.java:174`
  `cn.jiguang.bd.d.c("JSDKBannedHelper", "from server sdk banned status: " + zEquals + ", next request time: " + jOptLong);`
- `sources/cn/jiguang/bd/a.java:48`
  `d.i("LogFileHelper", "request upload token failed because can't get appKey");`
- `sources/cn/jiguang/bd/a.java:57`
  `d.i("LogFileHelper", "request l config failed because can't get uid");`
- `sources/cn/jiguang/bd/a.java:62`
  `d.i("LogFileHelper", "request l config failed because need register first");`
- `sources/cn/jiguang/bd/a.java:96`
  `d.c("LogFileHelper", "request upload token success,response body:" + responseBody);`
- `sources/cn/jiguang/bi/c.java:41`
  `cn.jiguang.bd.d.h("ConnectingHelper", "Login with - juid:" + jF + ", appKey:" + strE + ", sdkVersion:" + strF + ", pluginPlatformType:" + ((int) bA));`
- `sources/cn/jiguang/bi/c.java:71`
  `cn.jiguang.bd.d.c("ConnectingHelper", "login \n juid:" + jF + "\n flag:" + ((int) sC) + "\n netType:" + iA + "\n deviceId:" + strA + "\n locInfo:" + string + "\n countryCode:" + upperCase + "\n accountId:" + strD + "\n sdkver:" + strF + "\n userType :" + i);`
- `sources/cn/jiguang/bi/c.java:73`
  `sb.append("login with cC:");`
- `sources/cn/jiguang/bi/c.java:88`
  `str3 = "Login failed - recv msg failed wit error:" + e;`
- `sources/cn/jiguang/bi/c.java:90`
  `if (pairA == null || (obj = pairA.first) == null || (obj2 = pairA.second) == null || ((cn.jiguang.bm.c) obj).c != 1) {`
- `sources/cn/jiguang/bi/c.java:91`
  `str3 = "Login failed - can't parse a Login Response";`
- `sources/cn/jiguang/bi/c.java:104`
  `cn.jiguang.bd.d.g("ConnectingHelper", "Login succeed - sid:" + JConstants.tcpSessionId + ", serverTime;" + j);`
- `sources/cn/jiguang/bi/c.java:106`
  `sb3.append("Login  success regID:");`
- `sources/cn/jiguang/bi/c.java:112`
  `cn.jiguang.bd.d.j("ConnectingHelper", "Login failed with server error - code:" + cn.jiguang.bp.d.a(i2));`
- `sources/cn/jiguang/bi/c.java:314`
  `if (pairA == null || (obj = pairA.first) == null || (obj2 = pairA.second) == null || ((cn.jiguang.bm.c) obj).c != 0) {`
- `sources/cn/jiguang/bk/i.java:226`
  `iIntValue = ((Integer) pairRemove.first).intValue();`
- `sources/cn/jiguang/bk/i.java:248`
  `sb.append(" is disconnected, go on send waiting request");`
- `sources/cn/jiguang/bk/i.java:255`
  `sb.append(" is disconnected, finish waiting request, code=");`
- `sources/cn/jiguang/bk/i.java:281`
  `a(context, ((Integer) pair.first).intValue(), aVar, gVar, bVar);`
- `sources/cn/jiguang/bk/i.java:447`
  `cn.jiguang.bd.d.c("TcpReporter", "socket at " + gVar + " is connected, deal with waiting request");`
- `sources/cn/jiguang/bk/i.java:456`
  `a(context, ((Integer) pair.first).intValue(), aVar, gVar, bVar);`

## BR077

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `sources/cn/jiguang/bn/b.java:468`
  `SSLContext sSLContext = SSLContext.getInstance("SSL");`
- `sources/cn/jiguang/bn/b.java:469`
  `this.j = sSLContext;`
- `sources/cn/jiguang/bn/b.java:470`
  `sSLContext.init(null, new TrustManager[]{new SSLTrustManager(i.a())}, new SecureRandom());`
- `sources/cn/udesk/rich/BaseImageLoader.java:68`
  `SSLContext sSLContext = SSLContext.getInstance("SSL");`
- `sources/cn/udesk/rich/BaseImageLoader.java:69`
  `a = sSLContext;`
- `sources/cn/udesk/rich/BaseImageLoader.java:70`
  `sSLContext.init(null, new TrustManager[]{bVar}, new SecureRandom());`
- `sources/cn/udesk/rich/BaseImageLoader.java:107`
  `if (httpURLConnection instanceof HttpsURLConnection) {`
- `sources/cn/udesk/rich/BaseImageLoader.java:108`
  `HttpsURLConnection httpsURLConnection = (HttpsURLConnection) httpURLConnection;`
- `sources/cn/udesk/rich/BaseImageLoader.java:109`
  `httpsURLConnection.setHostnameVerifier(b);`
- `sources/cn/udesk/rich/BaseImageLoader.java:110`
  `httpsURLConnection.setSSLSocketFactory(a.getSocketFactory());`
- `sources/com/lidroid/xutils/util/OtherUtils.java:205`
  `public static void trustAllHttpsURLConnection() {`
- `sources/com/lidroid/xutils/util/OtherUtils.java:209`
  `SSLContext sSLContext = SSLContext.getInstance("TLS");`
- `sources/com/lidroid/xutils/util/OtherUtils.java:210`
  `sSLContext.init(null, trustManagerArr, null);`
- `sources/com/lidroid/xutils/util/OtherUtils.java:211`
  `a = sSLContext.getSocketFactory();`
- `sources/com/lidroid/xutils/util/OtherUtils.java:216`
  `SSLSocketFactory sSLSocketFactory = a;`
- `sources/com/umeng/commonsdk/statistics/internal/c.java:239`
  `httpsURLConnection = (HttpsURLConnection) new URL(str).openConnection();`
- `sources/com/umeng/commonsdk/statistics/internal/c.java:244`
  `httpsURLConnection.setHostnameVerifier(SSLSocketFactory.STRICT_HOSTNAME_VERIFIER);`
- `sources/com/umeng/commonsdk/statistics/internal/c.java:245`
  `SSLContext sSLContext = SSLContext.getInstance("TLS");`
- `sources/com/umeng/commonsdk/statistics/internal/c.java:246`
  `sSLContext.init(null, null, new SecureRandom());`
- `sources/com/umeng/commonsdk/statistics/internal/c.java:247`
  `httpsURLConnection.setSSLSocketFactory(sSLContext.getSocketFactory());`
- `sources/com/umeng/commonsdk/statistics/internal/c.java:250`
  `httpsURLConnection.setRequestProperty("X-Umeng-UTC", String.valueOf(System.currentTimeMillis()));`
- `sources/com/umeng/commonsdk/statistics/internal/c.java:251`
  `httpsURLConnection.setRequestProperty("X-Umeng-Sdk", com.umeng.commonsdk.statistics.internal.a.a(this.c).b());`
- `sources/com/umeng/commonsdk/statistics/internal/c.java:252`
  `httpsURLConnection.setRequestProperty(HttpHeaders.CONTENT_TYPE, com.umeng.commonsdk.statistics.internal.a.a(this.c).a());`
- `sources/com/umeng/commonsdk/statistics/internal/c.java:253`
  `httpsURLConnection.setRequestProperty("Msg-Type", "envelope/json");`
- `sources/com/umeng/umzid/a.java:39`
  `HttpsURLConnection httpsURLConnection = (HttpsURLConnection) new URL(str).openConnection();`
- `sources/com/umeng/umzid/a.java:40`
  `httpsURLConnection.setHostnameVerifier(new C0151a());`
- `sources/com/umeng/umzid/a.java:41`
  `SSLContext sSLContext = SSLContext.getInstance("TLS");`
- `sources/com/umeng/umzid/a.java:42`
  `sSLContext.init(null, null, new SecureRandom());`
- `sources/com/umeng/umzid/a.java:43`
  `httpsURLConnection.setSSLSocketFactory(sSLContext.getSocketFactory());`
- `sources/com/umeng/umzid/a.java:44`
  `httpsURLConnection.setRequestProperty(HttpHeaders.CONTENT_TYPE, "application/json");`
- `sources/com/umeng/umzid/a.java:45`
  `httpsURLConnection.setConnectTimeout(30000);`
- `sources/com/umeng/umzid/a.java:46`
  `httpsURLConnection.setReadTimeout(30000);`
- `sources/com/umeng/umzid/a.java:47`
  `httpsURLConnection.setRequestMethod("POST");`
- `sources/com/umeng/umzid/a.java:48`
  `httpsURLConnection.setDoOutput(true);`
- `sources/com/umeng/umzid/a.java:49`
  `httpsURLConnection.setDoInput(true);`
- `sources/okhttp3/OkHttpClient.java:471`
  `private static SSLSocketFactory b(X509TrustManager x509TrustManager) {`
- `sources/okhttp3/OkHttpClient.java:473`
  `SSLContext sSLContext = Platform.get().getSSLContext();`
- `sources/okhttp3/OkHttpClient.java:474`
  `sSLContext.init(null, new TrustManager[]{x509TrustManager}, null);`
- `sources/okhttp3/OkHttpClient.java:475`
  `return sSLContext.getSocketFactory();`
- `sources/okhttp3/internal/huc/a.java:296`
  `@Override // javax.net.ssl.HttpsURLConnection`
- `sources/okhttp3/internal/huc/a.java:324`
  `@Override // javax.net.ssl.HttpsURLConnection`
- `sources/okhttp3/internal/huc/a.java:325`
  `public abstract void setSSLSocketFactory(SSLSocketFactory sSLSocketFactory);`
- `sources/okhttp3/internal/huc/HttpsURLConnectionImpl.java:287`
  `@Override // okhttp3.internal.huc.a, javax.net.ssl.HttpsURLConnection`
- `sources/okhttp3/internal/huc/HttpsURLConnectionImpl.java:318`
  `@Override // okhttp3.internal.huc.a, javax.net.ssl.HttpsURLConnection`
- `sources/okhttp3/internal/huc/HttpsURLConnectionImpl.java:319`
  `public void setSSLSocketFactory(SSLSocketFactory sSLSocketFactory) {`
- `sources/okhttp3/internal/huc/HttpsURLConnectionImpl.java:321`
  `httpURLConnectionImpl.a = httpURLConnectionImpl.a.newBuilder().sslSocketFactory(sSLSocketFactory).build();`
- `sources/org/ksoap2/transport/HttpsServiceConnectionSE.java:112`
  `public void setSSLSocketFactory(SSLSocketFactory sSLSocketFactory) {`
- `sources/org/ksoap2/transport/HttpsServiceConnectionSE.java:113`
  `this.a.setSSLSocketFactory(sSLSocketFactory);`

## BR078

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/cn/jiguang/aa/a.java:5`
  `import javax.net.ssl.HostnameVerifier;`
- `sources/cn/jiguang/aa/a.java:18`
  `private HostnameVerifier o;`
- `sources/cn/jiguang/ay/c.java:13`
  `import javax.net.ssl.HostnameVerifier;`
- `sources/cn/jiguang/ay/c.java:50`
  `HostnameVerifier hostnameVerifier = (HostnameVerifier) objArr[4];`
- `sources/cn/jiguang/ay/c.java:69`
  `httpRequest.setHostnameVerifier(hostnameVerifier);`
- `sources/cn/jiguang/net/HttpRequest.java:6`
  `import javax.net.ssl.HostnameVerifier;`
- `sources/cn/jiguang/net/HttpRequest.java:19`
  `private HostnameVerifier o;`
- `sources/cn/udesk/rich/BaseImageLoader.java:15`
  `import javax.net.ssl.HostnameVerifier;`
- `sources/cn/udesk/rich/BaseImageLoader.java:38`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/cn/udesk/rich/BaseImageLoader.java:39`
  `@SuppressLint({"BadHostnameVerifier"})`
- `sources/okhttp3/OkHttpClient.java:17`
  `import javax.net.ssl.HostnameVerifier;`
- `sources/okhttp3/OkHttpClient.java:23`
  `import okhttp3.Call;`
- `sources/okhttp3/OkHttpClient.java:24`
  `import okhttp3.EventListener;`
- `sources/okhttp3/OkHttpClient.java:25`
  `import okhttp3.Headers;`
- `sources/okhttp3/OkHttpClient.java:26`
  `import okhttp3.Response;`
- `sources/okhttp3/OkHttpClient.java:27`
  `import okhttp3.WebSocket;`
- `sources/okhttp3/OkHttpClient.java:28`
  `import okhttp3.internal.Internal;`
- `sources/okhttp3/OkHttpClient.java:376`
  `Builder(OkHttpClient okHttpClient) {`
- `sources/okhttp3/OkHttpClient.java:467`
  `public OkHttpClient() {`
- `sources/okhttp3/internal/Util.java:37`
  `import okhttp3.Headers;`
- `sources/okhttp3/internal/Util.java:38`
  `import okhttp3.HttpUrl;`
- `sources/okhttp3/internal/Util.java:39`
  `import okhttp3.MediaType;`
- `sources/okhttp3/internal/Util.java:40`
  `import okhttp3.RequestBody;`
- `sources/okhttp3/internal/connection/RealConnection.java:297`
  `if (this.f == null || list == null || !j(list) || address.hostnameVerifier() != OkHostnameVerifier.INSTANCE || !supportsUrl(address.url())) {`
- `sources/okhttp3/internal/connection/RealConnection.java:308`
  `ExchangeCodec h(OkHttpClient okHttpClient, Interceptor.Chain chain) throws SocketException {`
- `sources/okhttp3/internal/connection/RealConnection.java:428`
  `return this.d != null && OkHostnameVerifier.INSTANCE.verify(httpUrl.host(), (X509Certificate) this.d.peerCertificates().get(0));`
- `sources/okhttp3/internal/http2/PushObserver.java:15`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:21`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:26`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:31`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/platform/b.java:23`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/b.java:24`
  `import okhttp3.internal.Util;`
- `sources/okhttp3/internal/platform/b.java:25`
  `import okhttp3.internal.tls.CertificateChainCleaner;`
- `sources/okhttp3/internal/platform/b.java:26`
  `import okhttp3.internal.tls.TrustRootIndex;`
- `sources/okhttp3/internal/platform/b.java:217`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/b.java:227`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/b.java:238`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/b.java:370`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:12`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:36`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:75`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/d.java:11`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/d.java:64`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Platform.java:19`
  `import okhttp3.OkHttpClient;`
- `sources/okhttp3/internal/platform/Platform.java:20`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/Platform.java:21`
  `import okhttp3.internal.Util;`
- `sources/okhttp3/internal/platform/Platform.java:22`
  `import okhttp3.internal.tls.BasicCertificateChainCleaner;`
- `sources/okhttp3/internal/platform/Platform.java:23`
  `import okhttp3.internal.tls.BasicTrustRootIndex;`
- `sources/okhttp3/internal/platform/Platform.java:24`
  `import okhttp3.internal.tls.CertificateChainCleaner;`
- `sources/okhttp3/internal/tls/BasicCertificateChainCleaner.java:32`
  `@Override // okhttp3.internal.tls.CertificateChainCleaner`
- `sources/okhttp3/internal/tls/BasicTrustRootIndex.java:33`
  `@Override // okhttp3.internal.tls.TrustRootIndex`
- `sources/okhttp3/internal/tls/CertificateChainCleaner.java:1`
  `package okhttp3.internal.tls;`
- `sources/okhttp3/internal/tls/CertificateChainCleaner.java:8`
  `import okhttp3.internal.platform.Platform;`
- `sources/okhttp3/internal/tls/OkHostnameVerifier.java:74`
  `@Override // javax.net.ssl.HostnameVerifier`
- `sources/okhttp3/internal/ws/RealWebSocket.java:244`
  `@Override // okhttp3.WebSocket`
- `sources/retrofit2/g.java:296`
  `okhttp3.Call call = this.f;`

## BR079

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/cn/jpush/android/ad/a.java:207`
  `webSettings.setAllowFileAccess(false);`
- `sources/cn/jpush/android/ad/a.java:223`
  `webView.getSettings().setMixedContentMode(0);`
- `sources/cn/jpush/android/ad/a.java:616`
  `webSettings.setAllowFileAccess(false);`
- `sources/cn/jpush/android/ui/c.java:327`
  `this.g.getSettings().setJavaScriptEnabled(false);`
- `sources/cn/udesk/activity/UdeskBaseWebViewActivity.java:92`
  `@SuppressLint({"NewApi", "SetJavaScriptEnabled"})`
- `sources/cn/udesk/activity/UdeskBaseWebViewActivity.java:99`
  `settings.setJavaScriptEnabled(true);`
- `sources/cn/udesk/activity/UdeskBaseWebViewActivity.java:106`
  `settings.setAllowFileAccess(true);`
- `sources/cn/udesk/activity/UdeskBaseWebViewActivity.java:113`
  `settings.setMixedContentMode(0);`
- `sources/cn/udesk/activity/UdeskHelperArticleActivity.java:57`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/alipay/sdk/widget/e.java:327`
  `settings.setAllowFileAccess(false);`
- `sources/com/alipay/sdk/widget/e.java:330`
  `settings.setAllowFileAccessFromFileURLs(false);`
- `sources/com/alipay/sdk/widget/e.java:331`
  `settings.setAllowUniversalAccessFromFileURLs(false);`
- `sources/com/alipay/sdk/widget/e.java:334`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/youzan/androidsdk/basic/YouzanBaseWebViewCompat.java:48`
  `@SuppressLint({"SetJavaScriptEnabled"})`
- `sources/com/youzan/androidsdk/basic/YouzanBaseWebViewCompat.java:58`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/youzan/androidsdk/basic/YouzanBaseWebViewCompat.java:72`
  `settings.setMixedContentMode(0);`
- `sources/com/youzan/androidsdk/tool/WebParameter.java:37`
  `@SuppressLint({"SetJavaScriptEnabled"})`
- `sources/com/youzan/systemweb/YZBaseWebView.java:89`
  `@SuppressLint({"SetJavaScriptEnabled"})`
- `sources/com/youzan/systemweb/YZBaseWebView.java:92`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/yuwell/uhealth/view/impl/data/bodyfat/BodyFatStatistics.java:95`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/yuwell/uhealth/view/impl/data/bpm/BpStatistic.java:89`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/yuwell/uhealth/view/impl/data/glu/BgStatistic.java:114`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/yuwell/uhealth/view/impl/data/gu/GuBgStatisticFragment.java:114`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/yuwell/uhealth/view/impl/data/oxy/BoStatistic.java:130`
  `settings.setJavaScriptEnabled(true);`

## BR080

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/android/support/v4/media/MediaBrowserCompat.java:921`
  `Log.d(MediaBrowserCompat.TAG, "  mServiceConnection=" + this.mServiceConnection);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:922`
  `Log.d(MediaBrowserCompat.TAG, "  mServiceBinderWrapper=" + this.mServiceBinderWrapper);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:923`
  `Log.d(MediaBrowserCompat.TAG, "  mCallbacksMessenger=" + this.mCallbacksMessenger);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:924`
  `Log.d(MediaBrowserCompat.TAG, "  mRootId=" + this.mRootId);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:925`
  `Log.d(MediaBrowserCompat.TAG, "  mMediaSessionToken=" + this.mMediaSessionToken);`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1082`
  `Log.d(MediaBrowserCompat.TAG, "ServiceCallbacks.onConnect...");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1097`
  `Log.d(MediaBrowserCompat.TAG, "addSubscription failed with RemoteException.");`
- `sources/android/support/v4/media/MediaBrowserCompat.java:1153`
  `Log.d(MediaBrowserCompat.TAG, "addSubscription failed with RemoteException parentId=" + str);`
- `sources/androidx/constraintlayout/motion/utils/StopLogic.java:203`
  `Log.v(str, str2 + " end stage 2");`
- `sources/androidx/core/view/ViewCompat.java:725`
  `Log.d("ViewCompat", "Error calling dispatchFinishTemporaryDetach", e2);`
- `sources/androidx/core/view/ViewCompat.java:789`
  `Log.d("ViewCompat", "Error calling dispatchStartTemporaryDetach", e2);`
- `sources/androidx/fragment/app/c.java:59`
  `Log.v("FragmentManager", "onCreateView: id=0x" + Integer.toHexString(resourceId) + " fname=" + attributeValue + " existing=" + fragmentFindFragmentById);`
- `sources/androidx/fragment/app/g.java:80`
  `Log.d("FragmentManager", "moveto ACTIVITY_CREATED: " + this.b);`
- `sources/androidx/localbroadcastmanager/content/LocalBroadcastManager.java:188`
  `Log.v("LocalBroadcastManager", "  Filter matched!  match=0x" + Integer.toHexString(iMatch));`
- `sources/cn/com/lasong/media/record/audio/AudioRecorder.java:137`
  `MediaLog.d(list.size() + ",\n " + audioRecordingConfiguration.isClientSilenced() + ",\n " + audioRecordingConfiguration.getAudioSource() + ",\n " + audioRecordingConfiguration.getClientAudioSource() + ",\n " + audioRecordingConfiguration.getClientAudioSessionId() + ",\n " + audioRecordingConfigurati...`
- `sources/cn/udesk/rich/a.java:427`
  `Log.d("huhu", sb.toString());`
- `sources/com/alipay/camera/CameraConfigurationManager.java:515`
  `Log.d("CameraConfiguration", "Toggle Torch Error");`
- `sources/com/alipay/camera/base/AntCamera.java:171`
  `CameraLog.d("AntCamera", "openOptimized cost time: " + (SystemClock.elapsedRealtime() - jElapsedRealtime));`
- `sources/com/alipay/mobile/common/logging/uploader/BaseUploader.java:183`
  `Log.v(a, "logswitch: ".concat(String.valueOf(strSubstring)));`
- `sources/com/alipay/mobile/mascanengine/imagetrace/sec/HybridEncryption.java:82`
  `Log.d("scan_seed_scan", "seed seed" + new String(bytes2) + " pubkey " + this.c);`
- `sources/com/alipay/mobile/scansdk/ui/BaseScanFragment.java:276`
  `MPScanLog.d("BaseScanFragment", "initScanRect(): " + this.scanRect);`
- `sources/com/alipay/mobile/scansdk/ui/ToolScanTopView.java:208`
  `MPScanLog.d(TAG, "getScanRect: camera(" + camera + "), previewWidth(" + i + "), previewHeight(" + i2 + ")");`
- `sources/com/bumptech/glide/Glide.java:242`
  `Log.d("Glide", "Discovered GlideModule from manifest: " + it3.next().getClass());`
- `sources/com/bumptech/glide/load/engine/bitmap_recycle/LruArrayPool.java:113`
  `Log.v(aVarD.getTag(), "evicted: " + aVarD.getArrayLength(objF));`
- `sources/com/bumptech/glide/load/engine/bitmap_recycle/LruArrayPool.java:154`
  `Log.v(aVarE.getTag(), "Allocated " + aVar.b + " bytes");`
- `sources/com/bumptech/glide/load/engine/prefill/a.java:91`
  `Log.d("PreFillRunner", "allocated [" + preFillTypeB.d() + "x" + preFillTypeB.b() + "] " + preFillTypeB.a() + " size: " + bitmapByteSize);`
- `sources/com/bumptech/glide/load/resource/ImageDecoderResourceDecoder.java:82`
  `Log.v("ImageDecoder", "Resizing from [" + size.getWidth() + "x" + size.getHeight() + "] to [" + iRound + "x" + iRound2 + "] scaleFactor: " + scaleFactor);`
- `sources/com/bumptech/glide/load/resource/bitmap/BitmapImageDecoderResourceDecoder.java:22`
  `Log.v("BitmapImageDecoder", "Decoded [" + bitmapDecodeBitmap.getWidth() + "x" + bitmapDecodeBitmap.getHeight() + "] for [" + i + "x" + i2 + "]");`
- `sources/com/bumptech/glide/load/resource/bitmap/DefaultImageHeaderParser.java:323`
  `Log.d("DfltImageHeaderParser", "Illegal number of bytes for TI tag data tagType=" + ((int) sA3));`
- `sources/com/bumptech/glide/load/resource/bitmap/DefaultImageHeaderParser.java:326`
  `Log.d("DfltImageHeaderParser", "Illegal tagValueOffset=" + i3 + " tagType=" + ((int) sA3));`
- `sources/com/bumptech/glide/load/resource/bitmap/Downsampler.java:424`
  `Log.v("Downsampler", "Decoded " + f(bitmap) + " from [" + i2 + "x" + i3 + "] " + str + " with inBitmap " + j(options) + " for [" + i4 + "x" + i5 + "], sample size: " + options.inSampleSize + ", density: " + options.inDensity + ", target density: " + options.inTargetDensity + ", thread: " + Thread.cu...`
- `sources/com/bumptech/glide/load/resource/bitmap/TransformationUtils.java:183`
  `Log.v("TransformationUtils", "requested target size too big for input, fit centering instead");`
- `sources/com/bumptech/glide/load/resource/bitmap/TransformationUtils.java:269`
  `Log.v("TransformationUtils", "requested target size matches input, returning input");`
- `sources/com/bumptech/glide/load/resource/bitmap/TransformationUtils.java:278`
  `Log.v("TransformationUtils", "adjusted target size matches input, returning input");`
- `sources/com/bumptech/glide/load/resource/bitmap/TransformationUtils.java:285`
  `Log.v("TransformationUtils", "request: " + i + "x" + i2);`
- `sources/com/bumptech/glide/load/resource/bitmap/TransformationUtils.java:286`
  `Log.v("TransformationUtils", "toFit:   " + bitmap.getWidth() + "x" + bitmap.getHeight());`
- `sources/com/bumptech/glide/load/resource/bitmap/TransformationUtils.java:287`
  `Log.v("TransformationUtils", "toReuse: " + bitmap2.getWidth() + "x" + bitmap2.getHeight());`
- `sources/com/bumptech/glide/load/resource/bitmap/TransformationUtils.java:291`
  `Log.v("TransformationUtils", sb.toString());`
- `sources/com/bumptech/glide/load/resource/gif/ByteBufferGifDecoder.java:110`
  `Log.v("BufferGifDecoder", "Downsampling GIF, sampleSize: " + iMax + ", target dimens: [" + i + "x" + i2 + "], actual dimens: [" + gifHeader.getWidth() + "x" + gifHeader.getHeight() + "]");`
- `sources/com/hiflying/smartlink/v3/SnifferSmartLinker.java:27`
  `HFLog.d(this, String.format("setupSendAction: password-%s ssid-%s", str, Arrays.toString(strArr)));`

## BR081

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/cn/jiguang/net/SSLTrustManager.java:26`
  `KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());`
- `sources/com/vivo/push/c/a.java:4`
  `import android.security.keystore.KeyGenParameterSpec;`
- `sources/com/vivo/push/c/a.java:22`
  `KeyStore keyStore = KeyStore.getInstance("AndroidKeyStore");`
- `sources/com/vivo/push/c/a.java:40`
  `KeyGenerator keyGenerator = KeyGenerator.getInstance("AES", "AndroidKeyStore");`
- `sources/com/vivo/push/c/a.java:42`
  `keyGenerator.init(new KeyGenParameterSpec.Builder("AesKeyAlias", 3).setBlockModes("GCM").setEncryptionPaddings("NoPadding").setKeySize(256).build());`
- `sources/com/vivo/push/c/e.java:76`
  `KeyStore keyStore = KeyStore.getInstance("AndroidKeyStore");`
- `sources/com/vivo/push/c/e.java:139`
  `KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance(com.alipay.sdk.encrypt.d.a, "AndroidKeyStore");`

## BR082

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/androidx/core/content/FileProvider.java:51`
  `@Override // androidx.core.content.FileProvider.a`
- `sources/androidx/core/content/FileProvider.java:73`
  `@Override // androidx.core.content.FileProvider.a`
- `sources/cn/udesk/UdeskUtil.java:37`
  `import androidx.core.content.FileProvider;`
- `sources/cn/udesk/UdeskUtil.java:1044`
  `return FileProvider.getUriForFile(context, getExternalFileProviderName(context), file).toString();`
- `sources/cn/udesk/UdeskUtil.java:1047`
  `return FileProvider.getUriForFile(context, getExternalCacheProviderName(context), file).toString();`
- `sources/cn/udesk/UdeskUtil.java:1050`
  `return FileProvider.getUriForFile(context, getInternalFileProviderName(context), file).toString();`
- `sources/cn/udesk/UdeskUtil.java:1053`
  `return FileProvider.getUriForFile(context, getInternalCacheProviderName(context), file).toString();`
- `sources/cn/udesk/UdeskUtil.java:1056`
  `return FileProvider.getUriForFile(context, getExternalProviderName(context), file).toString();`
- `sources/cn/udesk/UdeskUtil.java:1270`
  `return FileProvider.getUriForFile(context, getExternalFileProviderName(context), file);`
- `sources/cn/udesk/UdeskUtil.java:1273`
  `return FileProvider.getUriForFile(context, getExternalCacheProviderName(context), file);`
- `sources/cn/udesk/UdeskUtil.java:1276`
  `return FileProvider.getUriForFile(context, getInternalFileProviderName(context), file);`
- `sources/cn/udesk/UdeskUtil.java:1279`
  `return FileProvider.getUriForFile(context, getInternalCacheProviderName(context), file);`
- `sources/cn/udesk/UdeskUtil.java:1282`
  `return FileProvider.getUriForFile(context, getExternalProviderName(context), file);`
- `sources/cn/udesk/provider/UdeskExternalCacheProvider.java:3`
  `import androidx.core.content.FileProvider;`
- `sources/cn/udesk/provider/UdeskExternalFileProvider.java:3`
  `import androidx.core.content.FileProvider;`
- `sources/cn/udesk/provider/UdeskExternalProvider.java:3`
  `import androidx.core.content.FileProvider;`
- `sources/cn/udesk/provider/UdeskInternalCacheProvider.java:3`
  `import androidx.core.content.FileProvider;`
- `sources/cn/udesk/provider/UdeskInternalFileProvider.java:3`
  `import androidx.core.content.FileProvider;`
- `sources/com/yuwell/androidbase/tool/FileManager.java:9`
  `import androidx.core.content.FileProvider;`
- `sources/com/yuwell/androidbase/tool/FileManager.java:365`
  `return FileProvider.getUriForFile(context, context.getPackageName() + "." + str, file);`
- `sources/com/yuwell/uhealth/global/utils/FileManager.java:8`
  `import androidx.core.content.FileProvider;`
- `sources/com/yuwell/uhealth/global/utils/FileManager.java:57`
  `return FileProvider.getUriForFile(context, context.getPackageName() + "." + str, file);`
- `sources/com/yuwell/uhealth/util/ShareUtil.java:7`
  `import androidx.core.content.FileProvider;`
- `sources/com/yuwell/uhealth/util/ShareUtil.java:15`
  `return FileProvider.getUriForFile(context, context.getPackageName().concat(".FileProvider1"), file);`
- `sources/com/yuwell/uhealth/util/VersionUtil.java:7`
  `import androidx.core.content.FileProvider;`
- `sources/com/yuwell/uhealth/util/VersionUtil.java:45`
  `Uri uriForFile = FileProvider.getUriForFile(context, "com.yuwell.uhealth.fileProvider", file);`
- `sources/com/zhihu/matisse/internal/utils/MediaStoreCompat.java:10`
  `import androidx.core.content.FileProvider;`
- `sources/com/zhihu/matisse/internal/utils/MediaStoreCompat.java:75`
  `Uri uriForFile = FileProvider.getUriForFile(this.a.get(), this.c.authority, fileA);`

## BR086

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/androidx/appcompat/R.java:62`
  `public static final int actionModeShareDrawable = 0x7f04004d;`
- `sources/androidx/appcompat/R.java:546`
  `public static final int abc_ab_share_pack_mtrl_alpha = 0x7f080006;`
- `sources/androidx/appcompat/R.java:554`
  `public static final int abc_btn_default_mtrl_shape = 0x7f08000e;`
- `sources/androidx/appcompat/R.java:1389`
  `public static final int AppCompatTheme_actionModeShareDrawable = 0x0000001a;`
- `sources/androidx/appcompat/R.java:1499`
  `public static final int DrawerArrowToggle_arrowShaftLength = 0x00000001;`
- `sources/androidx/appcompat/R.java:1709`
  `public static final int[] AppCompatTheme = {android.R.attr.windowIsFloating, android.R.attr.windowAnimationStyle, com.yuwell.uhealth.R.attr.actionBarDivider, com.yuwell.uhealth.R.attr.actionBarItemBackground, com.yuwell.uhealth.R.attr.actionBarPopupTheme, com.yuwell.uhealth.R.attr.actionBarSize, com...`
- `sources/androidx/appcompat/R.java:1713`
  `public static final int[] DrawerArrowToggle = {com.yuwell.uhealth.R.attr.arrowHeadLength, com.yuwell.uhealth.R.attr.arrowShaftLength, com.yuwell.uhealth.R.attr.barLength, com.yuwell.uhealth.R.attr.color, com.yuwell.uhealth.R.attr.drawableSize, com.yuwell.uhealth.R.attr.gapBetweenBars, com.yuwell.uhe...`
- `sources/androidx/appcompat/R.java:1732`
  `public static final int[] TextAppearance = {android.R.attr.textSize, android.R.attr.typeface, android.R.attr.textStyle, android.R.attr.textColor, android.R.attr.textColorHint, android.R.attr.textColorLink, android.R.attr.shadowColor, android.R.attr.shadowDx, android.R.attr.shadowDy, android.R.attr.s...`
- `sources/androidx/appcompat/app/AppCompatDelegate.java:161`
  `public abstract boolean isHandleNativeActionModesEnabled();`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2203`
  `public boolean isHandleNativeActionModesEnabled() {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2710`
  `return AppCompatDelegateImpl.this.isHandleNativeActionModesEnabled() ? a(callback) : super.onWindowStartingActionMode(callback);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2716`
  `if (AppCompatDelegateImpl.this.isHandleNativeActionModesEnabled() && i == 0) {`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:63`
  `this.d = typedArrayObtainStyledAttributes.getDimension(R.styleable.DrawerArrowToggle_arrowShaftLength, Camera2ConfigurationUtils.MIN_ZOOM_RATE);`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:340`
  `java.lang.String r3 = "Share records file not well-formed."`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:345`
  `java.lang.String r3 = "Share records file does not start with historical-records tag."`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:26`
  `private final int[] a = {R.drawable.abc_textfield_search_default_mtrl_alpha, R.drawable.abc_textfield_default_mtrl_alpha, R.drawable.abc_ab_share_pack_mtrl_alpha};`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:27`
  `private final int[] b = {R.drawable.abc_ic_commit_search_api_mtrl_alpha, R.drawable.abc_seekbar_tick_mark_material, R.drawable.abc_ic_menu_share_mtrl_alpha, R.drawable.abc_ic_menu_copy_mtrl_am_alpha, R.drawable.abc_ic_menu_cut_mtrl_alpha, R.drawable.abc_ic_menu_selectall_mtrl_alpha, R.drawable.abc_i...`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:192`
  `if (i == R.drawable.abc_btn_default_mtrl_shape) {`
- `sources/androidx/appcompat/widget/e.java:5`
  `import android.graphics.BitmapShader;`
- `sources/androidx/appcompat/widget/e.java:6`
  `import android.graphics.Shader;`
- `sources/androidx/appcompat/widget/e.java:12`
  `import android.graphics.drawable.ShapeDrawable;`
- `sources/androidx/appcompat/widget/e.java:13`
  `import android.graphics.drawable.shapes.RoundRectShape;`
- `sources/androidx/appcompat/widget/e.java:14`
  `import android.graphics.drawable.shapes.Shape;`
- `sources/androidx/appcompat/widget/e.java:29`
  `private Shape a() {`
- `sources/androidx/appcompat/widget/e.java:30`
  `return new RoundRectShape(new float[]{5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f}, null, null);`
- `sources/androidx/appcompat/widget/e.java:62`
  `ShapeDrawable shapeDrawable = new ShapeDrawable(a());`
- `sources/androidx/appcompat/widget/e.java:63`
  `shapeDrawable.getPaint().setShader(new BitmapShader(bitmap, Shader.TileMode.REPEAT, Shader.TileMode.CLAMP));`
- `sources/androidx/appcompat/widget/e.java:64`
  `shapeDrawable.getPaint().setColorFilter(bitmapDrawable.getPaint().getColorFilter());`
- `sources/androidx/appcompat/widget/e.java:65`
  `return z ? new ClipDrawable(shapeDrawable, 3, 1) : shapeDrawable;`
- `sources/androidx/appcompat/widget/SearchView.java:1340`
  `this.p.refreshAutoCompleteResults();`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:105`
  `this.f.getTheme().resolveAttribute(R.attr.actionModeShareDrawable, typedValue, true);`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:108`
  `activityChooserView.setDefaultActionButtonContentDescription(R.string.abc_shareactionprovider_share_with_application);`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:109`
  `activityChooserView.setExpandActivityOverflowButtonContentDescription(R.string.abc_shareactionprovider_share_with);`
- `sources/androidx/cardview/widget/CardView.java:77`
  `public void setShadowPadding(int i, int i2, int i3, int i4) {`
- `sources/androidx/cardview/widget/d.java:20`
  `void setShadowPadding(int i, int i2, int i3, int i4);`
- `sources/androidx/cardview/widget/g.java:13`
  `import android.graphics.Shader;`
- `sources/androidx/cardview/widget/g.java:90`
  `paint.setShader(new RadialGradient(Camera2ConfigurationUtils.MIN_ZOOM_RATE, Camera2ConfigurationUtils.MIN_ZOOM_RATE, f5, new int[]{i, i, this.n}, new float[]{Camera2ConfigurationUtils.MIN_ZOOM_RATE, f4, 1.0f}, Shader.TileMode.CLAMP));`
- `sources/androidx/cardview/widget/g.java:95`
  `paint2.setShader(new LinearGradient(Camera2ConfigurationUtils.MIN_ZOOM_RATE, (-f6) + f7, Camera2ConfigurationUtils.MIN_ZOOM_RATE, (-f6) - f7, new int[]{i2, i2, this.n}, new float[]{Camera2ConfigurationUtils.MIN_ZOOM_RATE, 0.5f, 1.0f}, Shader.TileMode.CLAMP));`
- `sources/androidx/constraintlayout/motion/widget/KeyCycle.java:50`
  `a.append(R.styleable.KeyCycle_waveShape, 5);`
- `sources/androidx/constraintlayout/motion/widget/KeyTimeCycle.java:62`
  `a.append(R.styleable.KeyTimeCycle_waveShape, 19);`
- `sources/androidx/constraintlayout/widget/R.java:62`
  `public static final int actionModeShareDrawable = 0x7f04004d;`
- `sources/androidx/constraintlayout/widget/R.java:731`
  `public static final int abc_ab_share_pack_mtrl_alpha = 0x7f080006;`
- `sources/androidx/constraintlayout/widget/R.java:739`
  `public static final int abc_btn_default_mtrl_shape = 0x7f08000e;`
- `sources/androidx/constraintlayout/widget/R.java:1646`
  `public static final int AppCompatTheme_actionModeShareDrawable = 0x0000001a;`
- `sources/androidx/constraintlayout/widget/R.java:2077`
  `public static final int DrawerArrowToggle_arrowShaftLength = 0x00000001;`
- `sources/androidx/constraintlayout/widget/R.java:2516`
  `public static final int[] AppCompatTheme = {android.R.attr.windowIsFloating, android.R.attr.windowAnimationStyle, com.yuwell.uhealth.R.attr.actionBarDivider, com.yuwell.uhealth.R.attr.actionBarItemBackground, com.yuwell.uhealth.R.attr.actionBarPopupTheme, com.yuwell.uhealth.R.attr.actionBarSize, com...`
- `sources/androidx/constraintlayout/widget/R.java:2525`
  `public static final int[] DrawerArrowToggle = {com.yuwell.uhealth.R.attr.arrowHeadLength, com.yuwell.uhealth.R.attr.arrowShaftLength, com.yuwell.uhealth.R.attr.barLength, com.yuwell.uhealth.R.attr.color, com.yuwell.uhealth.R.attr.drawableSize, com.yuwell.uhealth.R.attr.gapBetweenBars, com.yuwell.uhe...`
- `sources/androidx/constraintlayout/widget/R.java:2532`
  `public static final int[] KeyCycle = {android.R.attr.alpha, android.R.attr.translationX, android.R.attr.translationY, android.R.attr.scaleX, android.R.attr.scaleY, android.R.attr.rotation, android.R.attr.rotationX, android.R.attr.rotationY, android.R.attr.translationZ, android.R.attr.elevation, com....`
- `sources/androidx/constraintlayout/widget/R.java:2534`
  `public static final int[] KeyTimeCycle = {android.R.attr.alpha, android.R.attr.translationX, android.R.attr.translationY, android.R.attr.scaleX, android.R.attr.scaleY, android.R.attr.rotation, android.R.attr.rotationX, android.R.attr.rotationY, android.R.attr.translationZ, android.R.attr.elevation, ...`
- `sources/androidx/constraintlayout/widget/R.java:2562`
  `public static final int[] TextAppearance = {android.R.attr.textSize, android.R.attr.typeface, android.R.attr.textStyle, android.R.attr.textColor, android.R.attr.textColorHint, android.R.attr.textColorLink, android.R.attr.shadowColor, android.R.attr.shadowDx, android.R.attr.shadowDy, android.R.attr.s...`
- `sources/androidx/core/app/ActivityCompat.java:25`
  `import androidx.core.app.SharedElementCallback;`
- `sources/androidx/core/app/ActivityCompat.java:86`
  `public void onSharedElementsReady() {`
- `sources/androidx/core/app/ActivityCompat.java:87`
  `this.a.onSharedElementsReady();`
- `sources/androidx/core/app/ActivityCompat.java:91`
  `b(SharedElementCallback sharedElementCallback) {`
- `sources/androidx/core/app/ActivityCompat.java:92`
  `this.a = sharedElementCallback;`
- `sources/androidx/core/app/ActivityCompat.java:95`
  `@Override // android.app.SharedElementCallback`
- `sources/androidx/core/app/ActivityCompat.java:96`
  `public Parcelable onCaptureSharedElementSnapshot(View view, Matrix matrix, RectF rectF) {`
- `sources/androidx/core/app/ActivityCompat.java:97`
  `return this.a.onCaptureSharedElementSnapshot(view, matrix, rectF);`
- `sources/androidx/core/app/ActivityCompat.java:100`
  `@Override // android.app.SharedElementCallback`
- `sources/androidx/core/app/ActivityCompat.java:105`
  `@Override // android.app.SharedElementCallback`
- `sources/androidx/core/app/ActivityCompat.java:106`
  `public void onMapSharedElements(List<String> list, Map<String, View> map) {`
- `sources/androidx/core/app/ActivityCompat.java:107`
  `this.a.onMapSharedElements(list, map);`
- `sources/androidx/core/app/ActivityCompat.java:110`
  `@Override // android.app.SharedElementCallback`
- `sources/androidx/core/app/ActivityCompat.java:111`
  `public void onRejectSharedElements(List<View> list) {`
- `sources/androidx/core/app/ActivityCompat.java:112`
  `this.a.onRejectSharedElements(list);`
- `sources/androidx/core/app/ActivityCompat.java:228`
  `public static void setEnterSharedElementCallback(@NonNull Activity activity, @Nullable SharedElementCallback sharedElementCallback) {`
- `sources/androidx/core/app/ActivityCompat.java:230`
  `activity.setEnterSharedElementCallback(sharedElementCallback != null ? new b(sharedElementCallback) : null);`
- `sources/androidx/core/app/ActivityCompat.java:234`
  `public static void setExitSharedElementCallback(@NonNull Activity activity, @Nullable SharedElementCallback sharedElementCallback) {`
- `sources/androidx/core/app/ActivityCompat.java:236`
  `activity.setExitSharedElementCallback(sharedElementCallback != null ? new b(sharedElementCallback) : null);`
- `sources/androidx/core/app/ShareCompat.java:17`
  `import android.widget.ShareActionProvider;`
- `sources/androidx/core/app/ShareCompat.java:29`
  `public final class ShareCompat {`
- `sources/androidx/core/app/ShareCompat.java:62`
  `action.putExtra(ShareCompat.EXTRA_CALLING_PACKAGE, context.getPackageName());`
- `sources/androidx/core/app/ShareCompat.java:63`
  `action.putExtra(ShareCompat.EXTRA_CALLING_PACKAGE_INTEROP, context.getPackageName());`
- `sources/androidx/core/app/ShareCompat.java:64`
  `action.putExtra(ShareCompat.EXTRA_CALLING_ACTIVITY, componentName);`
- `sources/androidx/core/app/ShareCompat.java:65`
  `action.putExtra(ShareCompat.EXTRA_CALLING_ACTIVITY_INTEROP, componentName);`
- `sources/androidx/core/app/ShareCompat.java:311`
  `this.c = ShareCompat.b(intent);`
- `sources/androidx/core/app/ShareCompat.java:312`
  `this.d = ShareCompat.a(intent);`
- `sources/androidx/core/app/ShareCompat.java:447`
  `if (this.e == null && isMultipleShare()) {`
- `sources/androidx/core/app/ShareCompat.java:469`
  `public boolean isMultipleShare() {`
- `sources/androidx/core/app/ShareCompat.java:473`
  `public boolean isShareIntent() {`

## BR088

paper_id: B004
paper_title: Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation

- `sources/com/alipay/mobile/common/logging/LogContextImpl.java:275`
  `public void appendFulllinkLog(Runnable runnable) {`
- `sources/com/alipay/mobile/common/logging/api/LogContext.java:102`
  `void appendFulllinkLog(Runnable runnable);`
- `sources/com/alipay/mobile/common/logging/api/LoggerFactory.java:291`
  `public void appendFulllinkLog(Runnable runnable) {`
- `sources/com/alipay/mobile/common/logging/strategy/DelayUploadConfig.java:14`
  `import java.util.concurrent.ScheduledFuture;`
- `sources/com/alipay/mobile/common/logging/strategy/DelayUploadConfig.java:28`
  `private ScheduledFuture j = null;`
- `sources/com/alipay/mobile/common/logging/strategy/DelayUploadConfig.java:30`
  `static /* synthetic */ ScheduledFuture b(DelayUploadConfig delayUploadConfig) {`
- `sources/com/alipay/mobile/common/logging/strategy/DelayUploadConfig.java:59`
  `ScheduledFuture scheduledFuture = this.j;`
- `sources/com/alipay/mobile/common/logging/strategy/DelayUploadConfig.java:60`
  `if (scheduledFuture != null) {`
- `sources/com/alipay/mobile/common/logging/strategy/DelayUploadConfig.java:61`
  `scheduledFuture.cancel(false);`
- `sources/org/kxml2/wap/wv/WV.java:11`
  `public static final String[] tagTablePage2 = {"ADDGM", "AttListFunc", "BLENT", "CAAUT", "CAINV", "CALI", "CCLI", "ContListFunc", "CREAG", "DALI", "DCLI", "DELGR", "FundamentalFeat", "FWMSG", "GALS", "GCLI", "GETGM", "GETGP", "GETLM", "GETM", "GETPR", "GETSPI", "GETWL", "GLBLU", "GRCHN", "GroupAuthFu...`
- `sources/org/kxml2/wap/wv/WV.java:17`
  `public static final String[] tagTablePage8 = {"MP", "GETAUT", "GETJU", "VRID", "VerifyIDFunc"};`

## BR090

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `audit_reports/00_independent_security_review.md:16`
  `结论：confirmed。`
- `audit_reports/00_independent_security_review.md:61`
  `结论：confirmed。`
- `audit_reports/00_independent_security_review.md:86`
  `结论：confirmed。`
- `audit_reports/01_evidence_inventory.md:18`
  `- 结论只能使用 'confirmed'、'supported_hypothesis'、'not_supported'、'not_testable'。`
- `audit_reports/01_evidence_inventory.md:20`
  `- 单个字符串、单个权限、单个 SDK、单个 URL 不能直接作为 'confirmed'。`
- `audit_reports/02_rule_by_rule_mapping.md:3`
  `说明：本文件严格按 'rule_catalog.tsv' 的规则编号输出。结论只使用 'confirmed'、'supported_hypothesis'、'not_supported'、'not_testable'。'confirmed' 仅用于静态工件本身足够证明的配置/代码问题；运行时行为、BLE 攻击和云端实际接收在无设备/抓包时不强行确认。`
- `audit_reports/02_rule_by_rule_mapping.md:29`
  `| BR003 | B023 / Android Permissions Demystified | supported_hypothesis | 多个 SDK 包含推送、统计、客服、商城；Manifest 中 SDK 组件较多。未抓到 SDK 实际调用敏感 API。 | 仅有 SDK 存在不能 confirmed；可作为后续 SDK API/流量验证假设。 |`
- `audit_reports/02_rule_by_rule_mapping.md:32`
  `| BR006 | B016 / COVID Android app privacy-security | confirmed | Manifest 引用 network security config；'network_security_config.xml' 第 3 行设置全局 'cleartextTrafficPermitted="true"'。 | B016 将 cleartext policy 作为静态安全检查项；此配置本身足够确认。 |`
- `audit_reports/02_rule_by_rule_mapping.md:34`
  `| BR008 | B025 / Android TLS revisited | confirmed | base-config 全局允许明文流量，业务域虽使用 HTTPS，但策略允许任意域明文。 | B025 关注 NSC 对 TLS/明文策略的影响；这里确认“策略允许”，不确认实际明文业务流量。 |`
- `audit_reports/02_rule_by_rule_mapping.md:41`
  `| BR015 | B022 / Android Application Security | confirmed | 'Logger' header 写入 manufacturer、model、Android version、SDK、app version；CrashLog 也记录设备信息。 | B022 将设备信息聚合视为静态可见数据收集面。 |`
- `audit_reports/02_rule_by_rule_mapping.md:42`
  `| BR016 | B006 / Analyzing security issues... | confirmed | Manifest 暴露 JPUSH_APPKEY、OPPO_APPKEY/APPID/APPSECRET、Vivo api_key、mPaaS appkey/public key、BuildConfig WX_APP_ID、Youzan/Umeng key。 | B006 静态检查包括 APK 中 key/secret。这里确认 SDK/配置 secret 暴露，不确认服务器可被攻破。 |`
- `audit_reports/02_rule_by_rule_mapping.md:43`
  `| BR017 | B006 / Analyzing security issues... | confirmed | 'EncryptUtil' 固定 '"8yu&well"'，使用 DES/ECB。 | 固定密钥和固定 crypto 构造是规则指定信号。 |`
- `audit_reports/02_rule_by_rule_mapping.md:44`
  `| BR018 | B001 / Security Concerns in Android mHealth Apps | confirmed | 'BPMeasurement'、'BGMeasurement'、'OxyData'、'FamilyMember' 含血压、血糖、SpO2、心率、生日、电话、体重等字段。 | B001 把健康/个人测量数据作为 mHealth 敏感资产。 |`
- `audit_reports/02_rule_by_rule_mapping.md:51`
  `| BR025 | B005 / Mobile health and privacy | confirmed | 'uhealth.db' 普通 xUtils DbUtils 创建；表含血压、血糖、血氧、成员资料，未见 SQLCipher。 | B005/B002 均把健康数据本地未加密存储列为关键检查项。 |`
- `audit_reports/02_rule_by_rule_mapping.md:52`
  `| BR026 | B002 / accredited health app privacy | confirmed | SharedPreferences 保存 'access_token'、'refress_token'、'current_familymember'、设备名/MAC/last_obj 等，未见加密。 | B002 关注本地个人数据存储安全；证据足够。 |`
- `audit_reports/02_rule_by_rule_mapping.md:53`
  `| BR027 | B002 / accredited health app privacy | confirmed | 'Logger' 写 external-cache LOG；'CrashLog' 在外部存储可用时写 '/uhealth/*crash.txt'；'LogUploadUtil' 上传日志 zip。 | 确认日志/崩溃报告写到外部/外部缓存路径；不确认每个文件都有健康数据。 |`
- `audit_reports/02_rule_by_rule_mapping.md:55`
  `| BR029 | B016 / COVID Android app analysis | confirmed | 'UHealthWebViewActivity' exported 并加载外部 extra URL；'SNInputActivity' exported 可进设备 SN 页面。 | B016 导出组件检查适用；确认外部入口存在，不确认数据泄露。 |`
- `audit_reports/02_rule_by_rule_mapping.md:62`
  `| BR040 | B007 / SDK privacy settings | confirmed | 'GlobalContext' preInit UMeng；'Startup' 无条件 Youzan init/preload；'initSdk()' 初始化 JPush/Udesk/UMeng/Youzan。 | B007 关注 SDK 初始化和默认隐私设置；静态 init before feature use 成立。 |`
- `audit_reports/02_rule_by_rule_mapping.md:63`
  `| BR041 | B007 / SDK privacy settings | supported_hypothesis | 未看到 Youzan/JPush/Udesk 完整 consent gate；JPush 有 'JCollectionAuth' 切换，Youzan preload 更早。 | 是否自动日志/跟踪需抓包，因此不 confirmed。 |`
- `audit_reports/02_rule_by_rule_mapping.md:67`
  `| BR047 | B001 / Security Concerns in Android mHealth Apps | confirmed | 'SyncService' 记录解密下载、上传前 JSON、含 accessToken map；BLE 回调记录设备地址/测量 JSON；Logger 写 Android/file，日志可上传。 | B001 日志泄漏维度适用；代码链完整。 |`
- `audit_reports/02_rule_by_rule_mapping.md:71`
  `| BR055 | B014 / review methodology | confirmed | 本报告为每个 finding 记录文件、类、字段、rule_id 和证据链。 | 这是报告质量规则，本轮已执行。 |`
- `audit_reports/02_rule_by_rule_mapping.md:72`
  `| BR058 | B022 / Android Application Security | confirmed | 报告区分第一方、鱼跃 BLE 库、第三方 SDK，并避免把 SDK 行为直接算作第一方漏洞。 | 这是归因规则，本轮已执行。 |`
- `audit_reports/02_rule_by_rule_mapping.md:73`
  `| BR059 | B006 / Android mHealth issues | confirmed | 'SNInputActivity'、'UHealthWebViewActivity' 明确 'exported=true'；targetSdk 31 下显式导出。 | 导出组件攻击面静态成立。 |`
- `audit_reports/02_rule_by_rule_mapping.md:74`
  `| BR060 | B016 / COVID Android app analysis | confirmed | Manifest mPaaS 'workspaceId="dev"'、mobilegw/mpaasapi/logging/syncserver；BuildConfig HOST/HOST_HO；多环境/渠道配置可见。 | 确认环境/baseUrl/channel 配置存在；不确认可被外部切换。 |`
- `audit_reports/02_rule_by_rule_mapping.md:80`
  `| BR061 | B028 / BLE co-located app attacks | supported_hypothesis | 'MoxManager' 写 payload 只有固定字节、CRC/校验逻辑，未见 AES/HMAC/signature。 | B028 关注 BLE 应用层 payload 认证；无设备不能 confirmed。 |`
- `audit_reports/02_rule_by_rule_mapping.md:82`
  `| BR063 | B028 / BLE co-located app attacks | supported_hypothesis | 'MoxManager' 暴露 powerOff/pullData/reset/setLock/turnLight 等硬编码命令。 | 命令存在 confirmed，但“可被攻击利用”需设备验证，因此规则结论保守为 supported。 |`
- `audit_reports/02_rule_by_rule_mapping.md:85`
  `| BR066 | B028 / BLE co-located app attacks | confirmed | 自定义 service/characteristic UUID 在 'MoxManager'/Characteristic 中可见，协议表面暴露于 APK。 | 规则信号是 UUID 表暴露，静态足够。 |`
- `audit_reports/02_rule_by_rule_mapping.md:94`
  `| BR075 | B029 / BLE app-level access control | supported_hypothesis | 上传实体包含 deviceSN/MAC/deviceId/dataSource，但未见来源签名/provenance proof 字段。 | 云端是否校验未知，故不 confirmed。 |`
- `audit_reports/02_rule_by_rule_mapping.md:104`
  `| BR080 | B001 / mHealth logging | not_testable | 静态日志敏感性 confirmed；没有 logcat/文件日志样本。 | 动态规则需要实际日志出现。 |`
- `audit_reports/02_rule_by_rule_mapping.md:105`
  `| BR081 | B005 / local storage | not_testable | 静态表/Prefs confirmed；没有设备沙箱导出。 | 需要运行后 DB/Prefs 实体值。 |`
- `audit_reports/02_rule_by_rule_mapping.md:107`
  `| BR083 | B016 / exported component | not_testable | 静态 exported WebView/SNInput confirmed；未执行 adb am 调用验证状态变化。 | 需要实际调用。 |`
- `audit_reports/02_rule_by_rule_mapping.md:111`
  `| BR090 | B014 / validation selection | confirmed | 已把 cleartext config、WebView exported、DES/ECB、日志敏感、Prefs/DB、BLE app-layer 假设列为优先验证项。 | 这是后续验证规划规则。 |`
- `audit_reports/02_rule_by_rule_mapping.md:118`
  `| BR092 | B005 / Mobile health and privacy | not_testable | 存在 JPush/UMeng/Youzan/Udesk 等 SDK；无流量证据显示 adid/deviceId/userId 到第三方。 | 需要抓包或 SDK runtime evidence。 |`
- `audit_reports/03_detailed_findings_static_cloud_ble.md:5`
  `规则映射：BR006 confirmed；BR008 confirmed；BR095 supported_hypothesis。`
- `audit_reports/03_detailed_findings_static_cloud_ble.md:22`
  `- confirmed：App 安全策略允许明文流量。`
- `audit_reports/03_detailed_findings_static_cloud_ble.md:23`
  `- 不 confirmed：登录、同步或上传接口实际使用了 HTTP。当前没有抓包，且静态业务 host 是 HTTPS。`
- `audit_reports/03_detailed_findings_static_cloud_ble.md:28`
  `规则映射：BR029 confirmed；BR059 confirmed；BR035 supported_hypothesis。`
- `audit_reports/03_detailed_findings_static_cloud_ble.md:56`
  `- confirmed：外部可打开该 Activity 并控制 WebView URL。`
- `audit_reports/03_detailed_findings_static_cloud_ble.md:57`
  `- 不 confirmed：没有证据显示 JavaScript bridge、token 注入、Cookie 泄露或任意文件读取。`
- `audit_reports/03_detailed_findings_static_cloud_ble.md:61`
  `规则映射：BR026 confirmed；BR082 not_testable。`
- `audit_reports/03_detailed_findings_static_cloud_ble.md:92`
  `规则映射：BR025 confirmed；BR018 confirmed；BR091 supported_hypothesis；BR097 supported_hypothesis。`
- `audit_reports/03_detailed_findings_static_cloud_ble.md:118`
  `- confirmed：敏感表和普通 SQLite 存储存在。`
- `audit_reports/03_detailed_findings_static_cloud_ble.md:123`
  `规则映射：BR047 confirmed；BR027 confirmed；BR080 not_testable。`
- `audit_reports/03_detailed_findings_static_cloud_ble.md:152`
  `为什么 confirmed：`
- `audit_reports/03_detailed_findings_static_cloud_ble.md:154`
  `- 单个日志字符串不足以 confirmed；这里有完整链路：敏感源头（DB/同步/BLE/token）到日志 sink（Logger），再到本地文件和上传接口。`
- `audit_reports/03_detailed_findings_static_cloud_ble.md:162`
  `规则映射：BR017 confirmed；BR016 不用该点重复确认。`
- `audit_reports/03_detailed_findings_static_cloud_ble.md:184`
  `规则映射：BR040 confirmed；BR041 supported_hypothesis；BR016 confirmed；BR076/BR077/BR092 not_testable。`
- `audit_reports/03_detailed_findings_static_cloud_ble.md:203`
  `- confirmed：SDK 初始化代码和配置 key 存在。`
- `audit_reports/03_detailed_findings_static_cloud_ble.md:209`
  `规则映射：BR061-BR075 多数 supported_hypothesis，BR066 confirmed，BR097 supported_hypothesis。`
- `audit_reports/04_final_review_and_corrections.md:5`
  `## 1. 已复核并保留为 confirmed 的结论`
- `audit_reports/04_final_review_and_corrections.md:9`
  `保留为 confirmed。`
- `audit_reports/04_final_review_and_corrections.md:25`
  `保留为 confirmed。`
- `audit_reports/04_final_review_and_corrections.md:39`
  `保留为 confirmed。`
- `audit_reports/04_final_review_and_corrections.md:54`
  `保留为 confirmed。`
- `audit_reports/04_final_review_and_corrections.md:68`
  `保留为 confirmed。`
- `audit_reports/04_final_review_and_corrections.md:83`
  `保留为 confirmed。`
- `audit_reports/04_final_review_and_corrections.md:93`
  `- confirmed 只覆盖静态初始化/key 暴露。`
- `audit_reports/04_final_review_and_corrections.md:98`
  `保留为 confirmed。`
- `audit_reports/04_final_review_and_corrections.md:113`
  `最终维持 supported_hypothesis，而不是 confirmed。`
- `audit_reports/04_final_review_and_corrections.md:123`
  `- 如果写成 confirmed，会夸大。`
- `audit_reports/04_final_review_and_corrections.md:178`
  `- 该点应作为独立配置风险，而非 confirmed ContentProvider leak。`
- `audit_reports/04_final_review_and_corrections.md:197`
  `1. 敏感日志：BR047 confirmed。删除 token、明文上传 JSON、解密下载数据、BLE 地址/测量 JSON 日志；阻断日志上传敏感字段。`
- `audit_reports/04_final_review_and_corrections.md:198`
  `2. 导出 WebView：BR029 confirmed。关闭导出或加签名权限和 URL 白名单。`
- `audit_reports/04_final_review_and_corrections.md:199`
  `3. 固定 DES/ECB：BR017 confirmed。迁移协议或明确其不是安全边界；服务端补签名/nonce/重放防护。`
- `audit_reports/04_final_review_and_corrections.md:200`
  `4. 本地 token/健康数据存储：BR025/BR026 confirmed。至少 token 使用加密存储，健康 DB 评估加密和删除策略。`
- `audit_reports/04_final_review_and_corrections.md:204`
  `1. 明文策略和代理行为：BR006 confirmed + BR078/BR095 not_testable/supported。`
- `audit_reports/04_final_review_and_corrections.md:205`
  `2. SDK 同意前流量：BR040 confirmed + BR077 not_testable。`
- `audit_reports/04_final_review_and_corrections.md:218`
  `- 本报告没有把单个权限、SDK、URL 或字符串直接判定为 confirmed。`
- `audit_reports/04_final_review_and_corrections.md:219`
  `- 所有 confirmed 均有至少一个明确静态工件，且通常有源头到 sink 或配置到行为的代码链。`

## BR091

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/com/yuwell/uhealth/data/source/remote/AccountAPI.java:25`
  `@POST("api/account/cancel")`
- `sources/com/yuwell/uhealth/data/source/remote/AccountAPI.java:28`
  `@POST("api/account/login")`
- `sources/com/yuwell/uhealth/data/source/remote/AccountAPI.java:31`
  `@POST("api/account/refreshtoken")`
- `sources/com/yuwell/uhealth/data/source/remote/AccountAPI.java:34`
  `@POST("api/account/sendcode")`
- `sources/com/yuwell/uhealth/data/source/remote/AccountAPI.java:37`
  `@POST("api/user/updateuserinfo")`
- `sources/com/yuwell/uhealth/data/source/remote/AccountAPI.java:40`
  `@POST("api/user/uploadphoto")`
- `sources/com/yuwell/uhealth/data/source/remote/AccountAPI.java:41`
  `@Multipart`
- `sources/com/yuwell/uhealth/data/source/remote/FetalAPI.java:19`
  `@POST("api/fetalheart/add")`
- `sources/com/yuwell/uhealth/data/source/remote/FetalAPI.java:22`
  `@GET("api/fetalheart/getinmonth")`
- `sources/com/yuwell/uhealth/data/source/remote/FetalAPI.java:25`
  `@POST("api/fetalheart/remove")`
- `sources/com/yuwell/uhealth/data/source/remote/FetalAPI.java:28`
  `@POST("api/appshare/tosharefetalheart")`
- `sources/com/yuwell/uhealth/data/source/remote/HoActivityControlAPI.java:14`
  `@GET("applet/app/activity/mark/read")`
- `sources/com/yuwell/uhealth/data/source/remote/HoActivityControlAPI.java:17`
  `@GET("applet/app/activity/show")`
- `sources/com/yuwell/uhealth/data/source/remote/HoDeviceAPI.java:29`
  `@POST("applet/app/r-user-device/bindingDevice")`
- `sources/com/yuwell/uhealth/data/source/remote/HoDeviceAPI.java:32`
  `@GET("applet/app/dev-device-produce/getDevProduct")`
- `sources/com/yuwell/uhealth/data/source/remote/HoDeviceAPI.java:35`
  `@POST("applet/app/f-device-run-data/getDeviceRunData")`
- `sources/com/yuwell/uhealth/data/source/remote/HoDeviceAPI.java:38`
  `@POST("applet/app/f-device-run-time/getDeviceRunTime")`
- `sources/com/yuwell/uhealth/data/source/remote/HoDeviceAPI.java:41`
  `@POST("applet/app/f-device-run-time/getDeviceRunTimeList")`
- `sources/com/yuwell/uhealth/data/source/remote/HoDeviceAPI.java:44`
  `@GET("applet/app/f-device/getFDevice")`
- `sources/com/yuwell/uhealth/data/source/remote/HoDeviceAPI.java:47`
  `@GET("applet/app/r-user-device/getUserDevice")`
- `sources/com/yuwell/uhealth/data/source/remote/HoDeviceAPI.java:50`
  `@GET("applet/app/f-device/setAnion")`
- `sources/com/yuwell/uhealth/data/source/remote/HoDeviceAPI.java:53`
  `@GET("applet/app/f-device/setOxygen")`
- `sources/com/yuwell/uhealth/data/source/remote/HoDeviceAPI.java:56`
  `@GET("applet/app/f-device/setSwitch")`
- `sources/com/yuwell/uhealth/data/source/remote/HoDeviceAPI.java:59`
  `@GET("applet/app/f-device/setTime")`
- `sources/com/yuwell/uhealth/data/source/remote/HoDeviceAPI.java:62`
  `@GET("applet/app/f-device/setVoice")`
- `sources/com/yuwell/uhealth/data/source/remote/HoDeviceAPI.java:65`
  `@POST("applet/app/r-user-device/unBindingDevice")`
- `sources/com/yuwell/uhealth/data/source/remote/NewsAPI.java:12`
  `@GET("api/healthnews/articleurls")`
- `sources/com/yuwell/uhealth/data/source/remote/PatternAPI.java:27`
  `@GET("applet/app/pattern/enable")`
- `sources/com/yuwell/uhealth/data/source/remote/PatternAPI.java:30`
  `@GET("applet/app/pattern/query")`
- `sources/com/yuwell/uhealth/data/source/remote/SyncAPI.java:16`
  `@POST("api/datasync/index")`
- `sources/com/yuwell/uhealth/data/source/remote/SyncAPI.java:19`
  `@POST("/api/user/updateuserinfo")`
- `sources/com/yuwell/uhealth/data/source/remote/TerminalAPI.java:16`
  `@GET("api/terminalbinding/checkterminalbinding")`
- `sources/com/yuwell/uhealth/data/source/remote/TerminalAPI.java:19`
  `@POST("api/terminalbindingble/updatemac")`
- `sources/com/yuwell/uhealth/data/source/remote/UploadAPI.java:14`
  `@POST("api/logger/upload")`
- `sources/com/yuwell/uhealth/data/source/remote/UploadAPI.java:15`
  `@Multipart`

## BR092

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/androidx/appcompat/R.java:1727`
  `public static final int[] SearchView = {android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.inputType, android.R.attr.imeOptions, com.yuwell.uhealth.R.attr.closeIcon, com.yuwell.uhealth.R.attr.commitIcon, com.yuwell.uhealth.R.attr.defaultQueryHint, com.yuwell.uhealth.R.attr.goIcon, com...`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:612`
  `return (Build.VERSION.SDK_INT < 21 || !this.c.isPowerSaveMode()) ? 1 : 2;`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:100`
  `canvas.save();`
- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:609`
  `this.e.saveHierarchyState(sparseArray);`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:468`
  `synchronized (this.a) {`
- `sources/androidx/appcompat/widget/AppCompatRatingBar.java:21`
  `protected synchronized void onMeasure(int i, int i2) {`
- `sources/androidx/appcompat/widget/f.java:90`
  `int iSave = canvas.save();`
- `sources/androidx/appcompat/widget/f.java:96`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/appcompat/widget/i.java:345`
  `synchronized (rectF) {`
- `sources/androidx/appcompat/widget/i.java:413`
  `ViewCompat.saveAttributeDataForStyleable(textView, textView.getContext(), iArr, attributeSet, typedArrayObtainStyledAttributes, i, 0);`
- `sources/androidx/appcompat/widget/SwitchCompat.java:482`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/cardview/widget/c.java:30`
  `int iSave = canvas.save();`
- `sources/androidx/cardview/widget/g.java:114`
  `int iSave = canvas.save();`
- `sources/androidx/cardview/widget/g.java:139`
  `canvas.restoreToCount(iSave3);`
- `sources/androidx/cardview/widget/g.java:140`
  `int iSave4 = canvas.save();`
- `sources/androidx/cardview/widget/g.java:148`
  `canvas.restoreToCount(iSave4);`
- `sources/androidx/constraintlayout/motion/widget/MotionLayout.java:493`
  `canvas.save();`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:802`
  `int iSave = canvas.save();`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:807`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/core/widget/NestedScrollView.java:681`
  `int iSave = canvas.save();`
- `sources/androidx/core/widget/NestedScrollView.java:701`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/core/widget/NestedScrollView.java:706`
  `int iSave2 = canvas.save();`
- `sources/androidx/core/widget/NestedScrollView.java:725`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/databinding/library/baseAdapters/R.java:1689`
  `public static final int[] SearchView = {android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.inputType, android.R.attr.imeOptions, com.yuwell.uhealth.R.attr.closeIcon, com.yuwell.uhealth.R.attr.commitIcon, com.yuwell.uhealth.R.attr.defaultQueryHint, com.yuwell.uhealth.R.attr.goIcon, com...`
- `sources/androidx/drawerlayout/widget/DrawerLayout.java:718`
  `int iSave = canvas.save();`
- `sources/androidx/drawerlayout/widget/DrawerLayout.java:743`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/navigation/ui/R.java:1206`
  `public static final int transition_layout_save = 0x7f090624;`
- `sources/androidx/navigation/ui/R.java:2134`
  `public static final int BottomSheetBehavior_Layout_behavior_saveFlags = 0x00000008;`
- `sources/androidx/navigation/ui/R.java:2674`
  `public static final int[] BottomSheetBehavior_Layout = {android.R.attr.elevation, com.yuwell.uhealth.R.attr.backgroundTint, com.yuwell.uhealth.R.attr.behavior_draggable, com.yuwell.uhealth.R.attr.behavior_expandedOffset, com.yuwell.uhealth.R.attr.behavior_fitToContents, com.yuwell.uhealth.R.attr.beh...`
- `sources/androidx/print/PrintHelper.java:260`
  `synchronized (this) {`
- `sources/androidx/recyclerview/widget/DividerItemDecoration.java:38`
  `canvas.save();`
- `sources/androidx/recyclerview/widget/DividerItemDecoration.java:61`
  `canvas.save();`
- `sources/androidx/recyclerview/widget/RecyclerView.java:5264`
  `int iSave = canvas.save();`
- `sources/androidx/recyclerview/widget/RecyclerView.java:5270`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/recyclerview/widget/RecyclerView.java:5295`
  `int iSave4 = canvas.save();`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:435`
  `int iSave = canvas.save();`
- `sources/androidx/viewpager/widget/ViewPager.java:1238`
  `int iSave = canvas.save();`
- `sources/androidx/viewpager/widget/ViewPager.java:1245`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/viewpager/widget/ViewPager.java:1248`
  `int iSave2 = canvas.save();`
- `sources/androidx/viewpager/widget/ViewPager.java:1255`
  `canvas.restoreToCount(iSave2);`

## BR093

paper_id: B004
paper_title: Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation

- `sources/androidx/fragment/app/Fragment.java:53`
  `import androidx.savedstate.SavedStateRegistryOwner;`
- `sources/androidx/fragment/app/Fragment.java:62`
  `public class Fragment implements ComponentCallbacks, View.OnCreateContextMenuListener, LifecycleOwner, ViewModelStoreOwner, HasDefaultViewModelProviderFactory, SavedStateRegistryOwner {`
- `sources/cn/jiguang/an/d.java:74`
  `cn.jiguang.r.a.b("JDeviceIds", "ids not changed, need not report");`
- `sources/cn/jiguang/an/d.java:104`
  `cn.jiguang.r.a.f("JDeviceIds", "there are no data to report");`
- `sources/cn/jiguang/an/d.java:111`
  `cn.jiguang.r.a.b("JDeviceIds", str + "report success, reportData: " + this.b);`
- `sources/cn/jiguang/ax/g.java:79`
  `str = "upload" + jSONObject.toString() + " failed";`
- `sources/cn/jiguang/az/i.java:134`
  `cn.jiguang.bc.h.b("JOperateReport", "peripheralProperty:", th);`
- `sources/cn/jiguang/bf/f.java:821`
  `cn.jiguang.bd.d.c("ReportUtils", "save report types=" + set + " at " + string + File.separator + d.a(context, string, jSONObjectA2, false).getName());`
- `sources/cn/jiguang/bi/c.java:161`
  `cn.jiguang.bd.d.f("ConnectingHelper", "IMEI is duplicated reported by server. Give up now. ");`
- `sources/cn/jiguang/bp/c.java:70`
  `cn.jiguang.bd.d.c("RegKeyInfo", "save reg key info success");`
- `sources/cn/jiguang/bp/e.java:81`
  `cn.jiguang.bd.d.c("UDIDUtils", "Action:getSavedUuid");`
- `sources/cn/jiguang/bp/e.java:99`
  `cn.jiguang.bd.d.f("UDIDUtils", "Got sdcard file saved udid - " + strD);`
- `sources/cn/jiguang/ca/a.java:51`
  `cn.jiguang.bd.d.c("AuthUtils", "reportJSON=" + jSONObject);`
- `sources/cn/jiguang/e/a.java:346`
  `d.c("ShareProcessManager", "save uuid and createtime to sp,uuid:" + aVar.d + ",createtime:" + jCurrentTimeMillis);`
- `sources/cn/jiguang/f/a.java:501`
  `public static synchronized String d(Context context, String str) {`
- `sources/cn/jiguang/g/a.java:290`
  `return new a<>("cn.jiguang.sdk.user.profile", "sync_auth", -1L);`
- `sources/cn/udesk/aac/livedata/FileLiveData.java:76`
  `UdeskUtil.saveBitmap(this.b, this.a.getMsgContent(), videoThumbnail);`
- `sources/cn/udesk/aac/livedata/FileLiveData.java:477`
  `public void cancleUploadFile(MessageInfo messageInfo) {`
- `sources/cn/udesk/aac/livedata/SendMessageLiveData.java:93`
  `this.a.setNoNeedSave(true);`
- `sources/com/alibaba/sdk/android/oss/common/auth/HmacSHA1Signature.java:20`
  `synchronized (a) {`
- `sources/com/alibaba/sdk/android/oss/common/utils/DateUtil.java:32`
  `public static synchronized String currentFixedSkewedTimeInRFC822Format() {`
- `sources/com/alibaba/sdk/android/oss/internal/InternalRequestOperation.java:282`
  `if ((requestMessage.getMethod() == HttpMethod.POST || requestMessage.getMethod() == HttpMethod.PUT) && OSSUtils.isEmptyString((String) headers.get(HttpHeaders.CONTENT_TYPE))) {`
- `sources/com/alibaba/sdk/android/oss/internal/InternalRequestOperation.java:283`
  `headers.put(HttpHeaders.CONTENT_TYPE, OSSUtils.determineContentType(null, requestMessage.getUploadFilePath(), requestMessage.getObjectKey()));`
- `sources/com/alipay/android/app/helper/TidHelper.java:19`
  `public static synchronized String getTIDValue(Context context) {`
- `sources/com/alipay/apmobilesecuritysdk/e/a.java:20`
  `public static synchronized void a() {`
- `sources/com/alipay/apmobilesecuritysdk/e/a.java:23`
  `public static synchronized void a(Context context) {`
- `sources/com/alipay/apmobilesecuritysdk/e/a.java:28`
  `public static synchronized void a(Context context, b bVar) {`
- `sources/com/alipay/apmobilesecuritysdk/e/a.java:50`
  `public static synchronized b b(Context context) {`
- `sources/com/alipay/apmobilesecuritysdk/e/a.java:59`
  `public static synchronized b c(Context context) {`
- `sources/com/alipay/apmobilesecuritysdk/e/d.java:20`
  `public static synchronized void a() {`
- `sources/com/alipay/apmobilesecuritysdk/e/d.java:23`
  `public static synchronized void a(Context context) {`
- `sources/com/alipay/apmobilesecuritysdk/e/d.java:28`
  `public static synchronized void a(Context context, c cVar) {`
- `sources/com/alipay/apmobilesecuritysdk/e/d.java:52`
  `public static synchronized c b(Context context) {`
- `sources/com/alipay/apmobilesecuritysdk/e/d.java:61`
  `public static synchronized c c(Context context) {`
- `sources/com/alipay/apmobilesecuritysdk/e/h.java:75`
  `synchronized (h.class) {`
- `sources/com/alipay/mobile/common/logging/ContextInfo.java:386`
  `public final synchronized void J() {`
- `sources/com/alipay/mobile/common/logging/LogContextImpl.java:617`
  `public boolean isAutoReportClientLaunch() {`
- `sources/com/alipay/mobile/common/logging/api/LogContext.java:204`
  `ToolsUploadInterceptor getToolsUploadInterceptor();`
- `sources/com/alipay/mobile/common/logging/api/LogContext.java:214`
  `boolean isAutoReportClientLaunch();`
- `sources/com/alipay/mobile/common/logging/api/LogContext.java:361`
  `void setToolsUploadInterceptor(ToolsUploadInterceptor toolsUploadInterceptor);`

## BR094

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `sources/android/support/v4/media/session/MediaSessionCompat.java:622`
  `MediaSessionImplApi18.this.postToHandler(18, -1, -1, Long.valueOf(j), null);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:825`
  `synchronized (MediaSessionImplBase.this.mLock) {`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1031`
  `postToHandler(17);`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1036`
  `postToHandler(18, Long.valueOf(j));`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1041`
  `postToHandler(1, new Command(str, bundle, resultReceiverWrapper.mResultReceiver));`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1084`
  `postToHandler(11, Long.valueOf(j));`
- `sources/android/support/v4/media/session/MediaSessionCompat.java:1089`
  `postToHandler(13);`
- `sources/androidx/appcompat/app/AppCompatViewInflater.java:178`
  `/* JADX WARN: Failed to restore switch over string. Please report as a decompilation issue */`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:100`
  `canvas.save();`
- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:609`
  `this.e.saveHierarchyState(sparseArray);`
- `sources/androidx/appcompat/widget/ActivityChooserView.java:599`
  `ViewCompat.saveAttributeDataForStyleable(this, context, iArr, attributeSet, typedArrayObtainStyledAttributes, i, 0);`
- `sources/androidx/appcompat/widget/DrawableUtils.java:96`
  `/* JADX WARN: Failed to restore switch over string. Please report as a decompilation issue */`
- `sources/androidx/appcompat/widget/f.java:90`
  `int iSave = canvas.save();`
- `sources/androidx/appcompat/widget/f.java:96`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/appcompat/widget/ForwardingListener.java:136`
  `r0.postDelayed(r6, r3)`
- `sources/androidx/appcompat/widget/ForwardingListener.java:146`
  `r0.postDelayed(r6, r3)`
- `sources/androidx/appcompat/widget/o.java:68`
  `this.a.postDelayed(this.d, ViewConfiguration.getLongPressTimeout());`
- `sources/androidx/appcompat/widget/o.java:159`
  `this.a.postDelayed(this.e, j3);`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:137`
  `private synchronized boolean b(@NonNull Context context, long j2, @NonNull Drawable drawable) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:226`
  `private synchronized Drawable h(@NonNull Context context, long j2) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:405`
  `public synchronized void onConfigurationChanged(@NonNull Context context) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:412`
  `synchronized Drawable p(@NonNull Context context, @NonNull VectorEnabledTintResources vectorEnabledTintResources, @DrawableRes int i2) {`
- `sources/androidx/appcompat/widget/SearchView.java:1379`
  `View viewFindViewById2 = findViewById(R.id.submit_area);`
- `sources/androidx/appcompat/widget/SwitchCompat.java:482`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/asynclayoutinflater/R.java:1`
  `package androidx.asynclayoutinflater;`
- `sources/androidx/asynclayoutinflater/view/AsyncLayoutInflater.java:1`
  `package androidx.asynclayoutinflater.view;`
- `sources/androidx/asynclayoutinflater/view/AsyncLayoutInflater.java:20`
  `public final class AsyncLayoutInflater {`
- `sources/androidx/asynclayoutinflater/view/AsyncLayoutInflater.java:38`
  `cVar.d = AsyncLayoutInflater.this.a.inflate(cVar.c, cVar.b, false);`
- `sources/androidx/asynclayoutinflater/view/AsyncLayoutInflater.java:41`
  `AsyncLayoutInflater.this.c.d(cVar);`
- `sources/androidx/asynclayoutinflater/view/AsyncLayoutInflater.java:75`
  `AsyncLayoutInflater a;`
- `sources/androidx/asynclayoutinflater/view/AsyncLayoutInflater.java:107`
  `throw new RuntimeException("Failed to enqueue async inflate request", e);`
- `sources/androidx/asynclayoutinflater/view/AsyncLayoutInflater.java:131`
  `Log.w("AsyncLayoutInflater", "Failed to inflate resource in the background! Retrying on the UI thread", e);`
- `sources/androidx/asynclayoutinflater/view/AsyncLayoutInflater.java:135`
  `Log.w("AsyncLayoutInflater", e2);`
- `sources/androidx/asynclayoutinflater/view/AsyncLayoutInflater.java:147`
  `public AsyncLayoutInflater(@NonNull Context context) {`
- `sources/androidx/cardview/widget/c.java:30`
  `int iSave = canvas.save();`
- `sources/androidx/cardview/widget/c.java:42`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/cardview/widget/g.java:114`
  `int iSave = canvas.save();`
- `sources/androidx/cardview/widget/g.java:121`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/cardview/widget/g.java:122`
  `int iSave2 = canvas.save();`
- `sources/androidx/cardview/widget/g.java:130`
  `canvas.restoreToCount(iSave2);`

## BR095

paper_id: B025
paper_title: Why Eve and Mallory Still Love Android: Revisiting TLS (In)Security in Android Applications

- `resources/assets/js/highcharts.js:9`
  `R=g.navigator&&g.navigator.userAgent||"",y=c&&c.createElementNS&&!!c.createElementNS("http://www.w3.org/2000/svg","svg").createSVGRect,q=/(edge|msie|trident)/i.test(R)&&!g.opera,H=-1!==R.indexOf("Firefox"),D=-1!==R.indexOf("Chrome"),J=H&&4>parseInt(R.split("Firefox/")[1],10);return{product:"Highchar...`
- `resources/assets/js/highcharts.js:10`
  `SVG_NS:"http://www.w3.org/2000/svg",chartCount:0,seriesTypes:{},symbolSizes:{},svg:y,win:g,marginNames:["plotTop","marginRight","marginBottom","plotLeft"],noop:function(){},charts:[],dateFormats:{}}});O(q,"parts/Utilities.js",[q["parts/Globals.js"]],function(g){function c(b,h,e,z){var a=h?"Highchart...`
- `resources/assets/js/highcharts.js:65`
  `z=!0);var l=x.element;(e=a.element.getAttribute("id"))||a.element.setAttribute("id",e=M());if(d)for(a=b.getElementsByTagName("tspan");a.length;)a[0].setAttribute("y",0),f(k.dx)&&a[0].setAttribute("x",-k.dx),l.appendChild(a[0]);z&&x&&x.add({element:this.text?this.text.element:b});l.setAttributeNS("ht...`
- `resources/assets/js/highcharts.js:104`
  `this.width=b;this.height=a;for(this.boxWrapper.animate({width:b,height:a},{step:function(){this.attr({viewBox:"0 0 "+this.attr("width")+" "+this.attr("height")})},duration:m(e,!0)?void 0:0});f--;)h[f].align()};b.prototype.g=function(b){var h=this.createElement("g");return b?h.attr({"class":"highchar...`
- `resources/org.jivesoftware.smackx/smack-experimental-components.xml:2`
  `<scr:component xmlns:scr="http://www.osgi.org/xmlns/scr/v1.2.0"`
- `resources/org.jivesoftware.smackx/smack-extensions-components.xml:2`
  `<scr:component xmlns:scr="http://www.osgi.org/xmlns/scr/v1.2.0"`
- `resources/res/drawable/abc_ic_ab_back_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_arrow_drop_right_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_clear_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_go_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_menu_overflow_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_ic_voice_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/abc_list_divider_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:tint="?android:attr/colorForeground">`
- `resources/res/drawable/abc_seekbar_tick_mark_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/abc_text_cursor_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/res/drawable/abc_vector_test.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/avd_hide_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_hide_password__0_res_0x7f080000">`
- `resources/res/drawable/avd_show_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_show_password__0_res_0x7f080003">`
- `resources/res/drawable/bg_edit_text.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/btn_checkbox_checked_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/btn_checkbox_unchecked_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/btn_radio_off_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/btn_radio_on_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/circle_beat.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/circle_blue.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/circle_brown.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/circle_ff6775.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/circle_green.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/circle_grey.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/circle_list_item.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/circle_red.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/circle_white_alpha.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/circle_white_alpha_20.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/circle_white_with_green_stroke.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/circle_white_with_grey_stroke.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/circle_yellow.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/coin.xml:2`
  `<layer-list xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/dash_line.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="line">`
- `resources/res/drawable/dash_line_cccccc.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="line">`
- `resources/res/drawable/design_ic_visibility.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/design_ic_visibility_off.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/dottleline.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="line">`
- `resources/res/drawable/download_progress.xml:2`
  `<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/home_menu_divider.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/ho_to.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/ic_arrow_back_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_clock_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_close_white_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_gu_measure_divider.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="line">`
- `resources/res/drawable/ic_keyboard_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_mtrl_checked_circle.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_mtrl_chip_checked_black.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_mtrl_chip_checked_circle.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_mtrl_chip_close_circle.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/material_ic_calendar_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/material_ic_clear_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/material_ic_edit_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/material_ic_keyboard_arrow_left_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/material_ic_keyboard_arrow_right_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/material_ic_menu_arrow_down_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/material_ic_menu_arrow_up_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/mtrl_ic_arrow_drop_down.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/mtrl_ic_arrow_drop_up.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/mtrl_ic_cancel.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/mtrl_ic_error.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/mtrl_tabs_default_indicator.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/navigation_empty_icon.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/res/drawable/radiobutton_normal.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/radiobutton_selected.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/rectangle_bg_extreme_high.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/rectangle_bg_high.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/rectangle_bg_low.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/rectangle_bg_normal.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/rectangle_bo_low.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/rectangle_bo_normal.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/rectangle_bo_too_low.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/rectangle_bp_heavy.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/rectangle_bp_low.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/rectangle_bp_moderate.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`

## BR096

paper_id: B011
paper_title: Locking it down: The privacy and security of mobile medication apps

- `resources/AndroidManifest.xml:1003`
  `android:value="https://mgw.mpaas.cn-hangzhou.aliyuncs.com/mgw.htm"/>`
- `resources/AndroidManifest.xml:1006`
  `android:value="https://mpaasapi.mpaas.cn-hangzhou.aliyuncs.com/mgw.htm"/>`
- `resources/AndroidManifest.xml:1018`
  `android:value="https://mdap.mpaas.cn-hangzhou.aliyuncs.com"/>`
- `resources/AndroidManifest.xml:1042`
  `android:value="https://mdc.mpaas.cn-hangzhou.aliyuncs.com"/>`
- `resources/assets/js/highcharts.js:65`
  `z=!0);var l=x.element;(e=a.element.getAttribute("id"))||a.element.setAttribute("id",e=M());if(d)for(a=b.getElementsByTagName("tspan");a.length;)a[0].setAttribute("y",0),f(k.dx)&&a[0].setAttribute("x",-k.dx),l.appendChild(a[0]);z&&x&&x.add({element:this.text?this.text.element:b});l.setAttributeNS("ht...`
- `resources/assets/js/highcharts.js:150`
  `backgroundColor:q("#f7f7f7").setOpacity(.85).get(),borderWidth:1,shadow:!0,style:{color:"#333333",cursor:"default",fontSize:"12px",whiteSpace:"nowrap"}},credits:{enabled:!0,href:"https://www.highcharts.com?credits",position:{align:"right",x:-10,verticalAlign:"bottom",y:-5},style:{cursor:"pointer",co...`
- `resources/org.jivesoftware.smackx/smack-experimental-components.xml:2`
  `<scr:component xmlns:scr="http://www.osgi.org/xmlns/scr/v1.2.0"`
- `resources/org.jivesoftware.smackx/smack-extensions-components.xml:2`
  `<scr:component xmlns:scr="http://www.osgi.org/xmlns/scr/v1.2.0"`
- `resources/res/color/design_box_stroke_color.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/button_enable.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/selector_cb_unregister.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/layout/design_text_input_end_icon.xml:2`
  `<com.google.android.material.internal.CheckableImageButton xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/design_text_input_start_icon.xml:2`
  `<com.google.android.material.internal.CheckableImageButton xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/material_chip_input_combo.xml:2`
  `<com.google.android.material.timepicker.ChipTextInputComboView xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/material_time_input.xml:2`
  `<com.google.android.material.textfield.TextInputLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto"`
- `resources/res/layout/mtrl_picker_text_input_date.xml:2`
  `<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/sn_input.xml:2`
  `<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/udesk_confirm_pop_dialog.xml:2`
  `<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/menu/menu_add.xml:2`
  `<menu xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto">`
- `resources/res/menu/menu_delete.xml:2`
  `<menu xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto">`
- `resources/res/menu/menu_fht_delete.xml:2`
  `<menu xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto">`
- `resources/res/menu/menu_save.xml:2`
  `<menu xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto">`
- `sources/com/alibaba/sdk/android/oss/internal/InternalRequestOperation.java:1095`
  `throw new IllegalArgumentException("Endpoint must be a string like 'http://oss-cn-****.aliyuncs.com',or your cname like 'http://image.cnamedomain.com'!");`
- `sources/com/alipay/sdk/app/OpenAuthTask.java:165`
  `intent.putExtra("url", String.format("https://render.alipay.com/p/s/i?scheme=%s", Uri.encode(strC)));`
- `sources/com/alipay/sdk/app/PayTask.java:397`
  `if (strTrim.startsWith("https://wappaygw.alipay.com/service/rest.htm") || strTrim.startsWith("http://wappaygw.alipay.com/service/rest.htm")) {`
- `sources/com/alipay/sdk/app/PayTask.java:403`
  `if (strTrim.startsWith("https://mclient.alipay.com/service/rest.htm") || strTrim.startsWith("http://mclient.alipay.com/service/rest.htm")) {`
- `sources/com/alipay/sdk/app/PayTask.java:409`
  `if ((strTrim.startsWith("https://mclient.alipay.com/home/exterfaceAssign.htm") || strTrim.startsWith("http://mclient.alipay.com/home/exterfaceAssign.htm")) && ((strTrim.contains("alipay.wap.create.direct.pay.by.user") || strTrim.contains("create_forex_trade_wap")) && !TextUtils.isEmpty(strTrim.repla...`
- `sources/com/alipay/sdk/cons/a.java:5`
  `public static String a = "https://mobilegw.alipay.com/mgw.htm";`
- `sources/com/alipay/sdk/cons/a.java:6`
  `public static final String b = "https://mobilegw.alipaydev.com/mgw.htm";`
- `sources/com/alipay/sdk/cons/a.java:7`
  `public static final String c = "https://mcgw.alipay.com/sdklog.do";`
- `sources/com/alipay/sdk/cons/a.java:8`
  `public static final String d = "https://loggw-exsdk.alipay.com/loggw/logUpload.do";`
- `sources/com/alipay/sdk/cons/a.java:20`
  `public static final String p = "http://m.alipay.com/?action=h5quit";`
- `sources/com/elvishew/xlog/formatter/message/xml/DefaultXmlFormatter.java:25`
  `transformerNewTransformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", String.valueOf(4));`
- `sources/com/umeng/commonsdk/debug/UMLogCommon.java:27`
  `public static final String SC_10026 = "检测到SDK初始化过程遗漏UMConfigure.preInit函数，请参考【友盟+】合规指南: https://developer.umeng.com/docs/119267/detail/182050";`
- `sources/com/umeng/commonsdk/debug/UMLogCommon.java:28`
  `public static final String SC_10028 = "检测到未调用隐私授权API，详情见：https://developer.umeng.com/docs/119267/detail/182050";`
- `sources/com/umeng/commonsdk/statistics/UMServerURL.java:5`
  `public static String DEFAULT_URL = "https://ulogs.umeng.com";`
- `sources/com/umeng/commonsdk/statistics/UMServerURL.java:6`
  `public static String OVERSEA_DEFAULT_URL = "https://alogus.umeng.com";`
- `sources/com/umeng/commonsdk/statistics/UMServerURL.java:7`
  `public static String OVERSEA_SECONDARY_URL = "https://alogsus.umeng.com";`
- `sources/com/umeng/commonsdk/statistics/UMServerURL.java:15`
  `public static String SECONDARY_URL = "https://ulogs.umengcloud.com";`
- `sources/com/umeng/umzid/ZIDManager.java:100`
  `String strA = com.umeng.umzid.a.a("https://aaid.umeng.com/api/postZdata", jSONObject.toString());`
- `sources/com/xiaomi/push/service/v.java:86`
  `return "https://cn.register.xmpush.xiaomi.com" + str;`
- `sources/com/youzan/androidsdk/basic/web/plugin/WebClientWrapper.java:485`
  `if (!str.contains("/wscvis/checkAuthMobile") && !str.contains("passport.youzan.com") && !str.contains("https://www.youzan.com/intro/rule/") && !YouzanSDK.getSDKAdapter().isBoundMobile) {`
- `sources/com/youzan/androidsdk/tool/UserAgent.java:36`
  `okHttpClient.newCall(z ? new Request.Builder().url("https://open-pre.youzanyun.com/api/auth_exempt/youzan.cloud.secutity.code.query/1.0.0").post(formBodyBuild).build() : new Request.Builder().url("https://open.youzanyun.com/api/auth_exempt/youzan.cloud.secutity.code.query/1.0.0").post(formBodyBuild)...`
- `sources/com/youzan/androidsdk/tool/UserAgent.java:84`
  `okHttpClient.newCall(z ? new Request.Builder().url("https://open-pre.youzanyun.com/api/auth_exempt/youzan.cloud.app.shop.apply.login/1.0.0").post(formBodyBuild).build() : new Request.Builder().url("https://open.youzanyun.com/api/auth_exempt/youzan.cloud.app.shop.apply.login/1.0.0").post(formBodyBuil...`
- `sources/com/youzan/spiderman/c/a.java:6`
  `return "https://carmen.youzan.com/api/oauthentry/youzan.goldwing.modify.resource/1.0.0/get";`
- `sources/com/youzan/spiderman/c/a.java:10`
  `return "https://carmen.youzan.com/api/oauthentry/youzan.goldwing.upload/1.0.0/resource";`
- `sources/com/youzan/spiderman/c/a.java:14`
  `return "https://carmen.youzan.com/api/oauthentry/youzan.goldwing.get.certificate/1.0.0/config";`
- `sources/com/youzan/spiderman/cache/f.java:15`
  `str = "https://b.yzcdn.cn" + str;`
- `sources/com/youzan/spiderman/cache/f.java:17`
  `str = "https://img.yzcdn.cn" + str;`
- `sources/com/youzan/spiderman/cache/f.java:19`
  `str = "https://b.yzcdn.cn" + str;`
- `sources/com/youzan/spiderman/cache/f.java:27`
  `return new CacheUrl(Uri.parse("https://img.yzcdn.cn" + str));`
- `sources/com/youzan/spiderman/cache/f.java:30`
  `return new CacheUrl(Uri.parse("https://su.yzcdn.cn" + str));`
- `sources/com/yuwell/uhealth/BuildConfig.java:11`
  `public static final String HEALTH = "https://health.yuyue.com.cn/app2phone/?v=1.0.1#/healthPage";`
- `sources/com/yuwell/uhealth/BuildConfig.java:12`
  `public static final String HOST = "https://health.yuyue.com.cn/app2/";`
- `sources/com/yuwell/uhealth/BuildConfig.java:13`
  `public static final String HOST_HO = "https://iot.yuwell.com/";`
- `sources/com/yuwell/uhealth/data/model/net/WebServiceRequest.java:25`
  `new HttpTransportSE(GlobalContext.getHost() + "/" + str, 25000).call("http://www.yuwell.com/" + str2, soapSerializationEnvelope);`
- `sources/com/yuwell/uhealth/data/model/net/WebServiceTask.java:38`
  `new HttpTransportSE(GlobalContext.getHost() + "/" + str, 25000).call("http://www.yuwell.com/" + str2, soapSerializationEnvelope);`
- `sources/com/yuwell/uhealth/view/impl/main/Login.java:85`
  `UHealthWebViewActivity.start(login, "https://health.yuyue.com.cn/Softwarelicense.html", login.getString(R.string.licence));`
- `sources/com/yuwell/uhealth/view/impl/main/Login.java:96`
  `UHealthWebViewActivity.start(login, "https://health.yuyue.com.cn/legalnotice.html", login.getString(R.string.privacy_term));`
- `sources/io/reactivex/Completable.java:786`
  `ObjectHelper.requireNonNull(completableObserverOnSubscribe, "The RxJavaPlugins.onSubscribe hook returned a null CompletableObserver. Please check the handler provided to RxJavaPlugins.setOnCompletableSubscribe for invalid null returns. Further reading: https://github.com/ReactiveX/RxJava/wiki/Plugin...`
- `sources/io/reactivex/Maybe.java:1243`
  `ObjectHelper.requireNonNull(maybeObserverOnSubscribe, "The RxJavaPlugins.onSubscribe hook returned a null MaybeObserver. Please check the handler provided to RxJavaPlugins.setOnMaybeSubscribe for invalid null returns. Further reading: https://github.com/ReactiveX/RxJava/wiki/Plugins");`
- `sources/io/reactivex/Observable.java:3077`
  `ObjectHelper.requireNonNull(observerOnSubscribe, "The RxJavaPlugins.onSubscribe hook returned a null Observer. Please change the handler provided to RxJavaPlugins.setOnObservableSubscribe for invalid null returns. Further reading: https://github.com/ReactiveX/RxJava/wiki/Plugins");`
- `sources/io/reactivex/Single.java:1108`
  `ObjectHelper.requireNonNull(singleObserverOnSubscribe, "The RxJavaPlugins.onSubscribe hook returned a null SingleObserver. Please check the handler provided to RxJavaPlugins.setOnSingleSubscribe for invalid null returns. Further reading: https://github.com/ReactiveX/RxJava/wiki/Plugins");`
- `sources/org/kxml2/io/KXmlSerializer.java:349`
  `if ("http://xmlpull.org/v1/doc/features.html#indent-output".equals(str)) {`
- `sources/org/kxml2/io/KXmlSerializer.java:400`
  `if (!"http://xmlpull.org/v1/doc/features.html#indent-output".equals(str)) {`
- `sources/org/kxml2/kdom/Document.java:52`
  `this.b = (Boolean) xmlPullParser.getProperty("http://xmlpull.org/v1/doc/properties.html#xmldecl-standalone");`
- `sources/org/kxml2/wap/wv/WV.java:20`
  `public static final String[] attrStartTable = {"xmlns=http://www.wireless-village.org/CSP", "xmlns=http://www.wireless-village.org/PA", "xmlns=http://www.wireless-village.org/TRC", "xmlns=http://www.openmobilealliance.org/DTD/WV-CSP", "xmlns=http://www.openmobilealliance.org/DTD/WV-PA", "xmlns=http:...`
- `sources/org/xmlpull/v1/XmlPullParser.java:15`
  `public static final String FEATURE_PROCESS_DOCDECL = "http://xmlpull.org/v1/doc/features.html#process-docdecl";`
- `sources/org/xmlpull/v1/XmlPullParser.java:16`
  `public static final String FEATURE_PROCESS_NAMESPACES = "http://xmlpull.org/v1/doc/features.html#process-namespaces";`
- `sources/org/xmlpull/v1/XmlPullParser.java:17`
  `public static final String FEATURE_REPORT_NAMESPACE_ATTRIBUTES = "http://xmlpull.org/v1/doc/features.html#report-namespace-prefixes";`
- `sources/org/xmlpull/v1/XmlPullParser.java:18`
  `public static final String FEATURE_VALIDATION = "http://xmlpull.org/v1/doc/features.html#validation";`
- `sources/udesk/core/UdeskConst.java:67`
  `public static final String UD_QINIU_UPLOAD = "https://qn-im.udesk.cn/";`
- `sources/udesk/org/jivesoftware/smackx/caps/EntityCapsManager.java:219`
  `j = "http://www.igniterealtime.org/projects/smack";`
- `sources/udesk/org/jivesoftware/smackx/commands/AdHocCommandManager.java:33`
  `public static final String NAMESPACE = "http://jabber.org/protocol/commands";`
- `sources/udesk/org/jivesoftware/smackx/commands/AdHocCommandManager.java:204`
  `ServiceDiscoveryManager.getInstanceFor(xMPPConnection).addFeature("http://jabber.org/protocol/commands");`
- `sources/udesk/org/jivesoftware/smackx/commands/AdHocCommandManager.java:205`
  `ServiceDiscoveryManager.getInstanceFor(xMPPConnection).setNodeInformationProvider("http://jabber.org/protocol/commands", new b());`
- `sources/udesk/org/jivesoftware/smackx/commands/AdHocCommandManager.java:391`
  `this.d.publishItems(str, "http://jabber.org/protocol/commands", discoverItems);`
- `sources/udesk/org/jivesoftware/smackx/muc/packet/MUCAdmin.java:125`
  `sb.append("<query xmlns=\"http://jabber.org/protocol/muc#admin\">");`
- `sources/udesk/org/jivesoftware/smackx/muc/packet/MUCOwner.java:180`
  `sb.append("<query xmlns=\"http://jabber.org/protocol/muc#owner\">");`
- `sources/udesk/org/jivesoftware/smackx/offline/OfflineMessageManager.java:95`
  `return ServiceDiscoveryManager.getInstanceFor(this.a).supportsFeature(this.a.getServiceName(), "http://jabber.org/protocol/offline");`

## BR098

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/com/alibaba/sdk/android/oss/internal/InternalRequestOperation.java:1081`
  `OkHttpClient.Builder builderHostnameVerifier = new OkHttpClient.Builder().followRedirects(false).followSslRedirects(false).retryOnConnectionFailure(false).cache(null).hostnameVerifier(new c());`
- `sources/com/yuwell/uhealth/global/utils/http/ServiceGenerator.java:15`
  `OkHttpClient.Builder builder = new OkHttpClient.Builder();`
- `sources/com/yuwell/uhealth/global/utils/http/ServiceGenerator.java:20`
  `private static Retrofit.Builder a(String str) {`
- `sources/com/yuwell/uhealth/global/utils/http/ServiceGenerator.java:21`
  `return new Retrofit.Builder().baseUrl(str).addConverterFactory(FastJsonConverterFactory.create()).addCallAdapterFactory(RxJava2CallAdapterFactory.create());`
- `sources/com/yuwell/uhealth/global/utils/http/ServiceGenerator.java:25`
  `Retrofit.Builder builderA = a(BuildConfig.HOST);`
- `sources/com/yuwell/uhealth/global/utils/http/ServiceGenerator.java:26`
  `OkHttpClient.Builder builder = a;`
