# Rule Search Hits

## BR002

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/AndroidManifest.xml:32`
  `<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>`
- `resources/AndroidManifest.xml:33`
  `<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>`
- `resources/AndroidManifest.xml:34`
  `<uses-permission android:name="android.permission.INTERNET"/>`

## BR003

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/AndroidManifest.xml:18`
  `<uses-permission`
- `resources/AndroidManifest.xml:21`
  `<uses-permission`
- `resources/AndroidManifest.xml:24`
  `<uses-permission android:name="android.permission.BLUETOOTH_CONNECT"/>`
- `resources/AndroidManifest.xml:25`
  `<uses-permission`
- `resources/AndroidManifest.xml:28`
  `<uses-permission android:name="android.permission.BLUETOOTH_ADVERTISE"/>`

## BR004

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/AndroidManifest.xml:15`
  `<uses-permission android:name="android.permission.VIBRATE"/>`
- `resources/AndroidManifest.xml:16`
  `<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>`
- `resources/AndroidManifest.xml:17`
  `<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>`
- `resources/AndroidManifest.xml:18`
  `<uses-permission`

## BR006

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:43`
  `android:usesCleartextTraffic="true"`

## BR009

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/j3/a.java:21`
  `import javax.net.ssl.X509TrustManager;`
- `sources/j3/a.java:87`
  `public final X509TrustManager f10554a;`
- `sources/j3/a.java:90`
  `public b(X509TrustManager x509TrustManager, Method method) {`
- `sources/j3/a.java:92`
  `this.f10554a = x509TrustManager;`
- `sources/j3/a.java:177`
  `public CertificateChainCleaner buildCertificateChainCleaner(X509TrustManager x509TrustManager) {`
- `sources/j3/a.java:179`
  `Class<?> cls = Class.forName("android.net.http.X509TrustManagerExtensions");`
- `sources/j3/a.java:180`
  `return new C0108a(cls.getConstructor(X509TrustManager.class).newInstance(x509TrustManager), cls.getMethod("checkServerTrusted", X509Certificate[].class, String.class, String.class));`
- `sources/j3/a.java:182`
  `return super.buildCertificateChainCleaner(x509TrustManager);`
- `sources/j3/a.java:187`
  `public TrustRootIndex buildTrustRootIndex(X509TrustManager x509TrustManager) {`
- `sources/j3/a.java:189`
  `Method declaredMethod = x509TrustManager.getClass().getDeclaredMethod("findTrustAnchorByIssuerAndSignature", X509Certificate.class);`
- `sources/j3/a.java:191`
  `return new b(x509TrustManager, declaredMethod);`
- `sources/j3/a.java:193`
  `return super.buildTrustRootIndex(x509TrustManager);`
- `sources/j3/a.java:363`
  `public X509TrustManager trustManager(SSLSocketFactory sSLSocketFactory) {`
- `sources/j3/a.java:372`
  `X509TrustManager x509TrustManager = (X509TrustManager) Platform.a(objA, X509TrustManager.class, "x509TrustManager");`
- `sources/j3/a.java:373`
  `return x509TrustManager != null ? x509TrustManager : (X509TrustManager) Platform.a(objA, X509TrustManager.class, "trustManager");`
- `sources/j3/b.java:10`
  `import javax.net.ssl.X509TrustManager;`
- `sources/j3/b.java:59`
  `public X509TrustManager trustManager(SSLSocketFactory sSLSocketFactory) {`
- `sources/okhttp3/OkHttpClient.java:24`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/OkHttpClient.java:460`
  `public Builder sslSocketFactory(SSLSocketFactory sSLSocketFactory, X509TrustManager x509TrustManager) {`
- `sources/okhttp3/OkHttpClient.java:462`
  `Objects.requireNonNull(x509TrustManager, "trustManager == null");`
- `sources/okhttp3/OkHttpClient.java:464`
  `this.f12166n = CertificateChainCleaner.get(x509TrustManager);`
- `sources/okhttp3/OkHttpClient.java:773`
  `X509TrustManager x509TrustManagerPlatformTrustManager = Util.platformTrustManager();`
- `sources/okhttp3/OkHttpClient.java:776`
  `sSLContext.init(null, new TrustManager[]{x509TrustManagerPlatformTrustManager}, null);`
- `sources/okhttp3/OkHttpClient.java:778`
  `this.f12142n = CertificateChainCleaner.get(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/internal/Util.java:32`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/Util.java:422`
  `public static X509TrustManager platformTrustManager() {`
- `sources/okhttp3/internal/Util.java:427`
  `if (trustManagers.length == 1 && (trustManagers[0] instanceof X509TrustManager)) {`
- `sources/okhttp3/internal/Util.java:428`
  `return (X509TrustManager) trustManagers[0];`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:10`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:73`
  `public X509TrustManager trustManager(SSLSocketFactory sSLSocketFactory) {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:80`
  `return (X509TrustManager) Platform.a(objA, X509TrustManager.class, "x509TrustManager");`
- `sources/okhttp3/internal/platform/Platform.java:20`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/platform/Platform.java:95`
  `public CertificateChainCleaner buildCertificateChainCleaner(X509TrustManager x509TrustManager) {`
- `sources/okhttp3/internal/platform/Platform.java:96`
  `return new BasicCertificateChainCleaner(buildTrustRootIndex(x509TrustManager));`
- `sources/okhttp3/internal/platform/Platform.java:99`
  `public TrustRootIndex buildTrustRootIndex(X509TrustManager x509TrustManager) {`
- `sources/okhttp3/internal/platform/Platform.java:100`
  `return new BasicTrustRootIndex(x509TrustManager.getAcceptedIssuers());`
- `sources/okhttp3/internal/platform/Platform.java:163`
  `public X509TrustManager trustManager(SSLSocketFactory sSLSocketFactory) {`
- `sources/okhttp3/internal/platform/Platform.java:169`
  `return (X509TrustManager) a(objA, X509TrustManager.class, "trustManager");`
- `sources/okhttp3/internal/platform/Platform.java:176`
  `X509TrustManager x509TrustManagerTrustManager = trustManager(sSLSocketFactory);`
- `sources/okhttp3/internal/platform/Platform.java:177`
  `if (x509TrustManagerTrustManager != null) {`
- `sources/okhttp3/internal/platform/Platform.java:178`
  `return buildCertificateChainCleaner(x509TrustManagerTrustManager);`
- `sources/okhttp3/internal/tls/CertificateChainCleaner.java:7`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/tls/CertificateChainCleaner.java:12`
  `public static CertificateChainCleaner get(X509TrustManager x509TrustManager) {`
- `sources/okhttp3/internal/tls/CertificateChainCleaner.java:13`
  `return Platform.get().buildCertificateChainCleaner(x509TrustManager);`

## BR010

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/okhttp3/internal/connection/RealConnection.java:278`
  `if (this.f12300g == null || route == null || route.proxy().type() != Proxy.Type.DIRECT || this.b.proxy().type() != Proxy.Type.DIRECT || !this.b.socketAddress().equals(route.socketAddress()) || route.address().hostnameVerifier() != OkHostnameVerifier.INSTANCE || !supportsUrl(address.url())) {`
- `sources/okhttp3/internal/connection/RealConnection.java:368`
  `return this.f12298e != null && OkHostnameVerifier.INSTANCE.verify(httpUrl.host(), (X509Certificate) this.f12298e.peerCertificates().get(0));`
- `sources/okhttp3/internal/tls/BasicCertificateChainCleaner.java:27`
  `x509Certificate.verify(x509Certificate2.getPublicKey());`
- `sources/okhttp3/internal/tls/OkHostnameVerifier.java:83`
  `public boolean verify(String str, X509Certificate x509Certificate) {`

## BR011

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:11`
  `import java.security.cert.CertificateException;`
- `sources/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:13`
  `import javax.net.ssl.SSLHandshakeException;`
- `sources/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:146`
  `return (!(iOException instanceof ProtocolException) && (!(iOException instanceof InterruptedIOException) ? (!(iOException instanceof SSLHandshakeException) || !(iOException.getCause() instanceof CertificateException)) && !(iOException instanceof SSLPeerUnverifiedException) : (iOException instanceof ...`

## BR012

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/okhttp3/Address.java:49`
  `public final CertificatePinner f12001k;`
- `sources/okhttp3/Address.java:51`
  `public Address(String str, int i, Dns dns, SocketFactory socketFactory, @Nullable SSLSocketFactory sSLSocketFactory, @Nullable HostnameVerifier hostnameVerifier, @Nullable CertificatePinner certificatePinner, Authenticator authenticator, @Nullable Proxy proxy, List<Protocol> list, List<ConnectionSpe...`
- `sources/okhttp3/Address.java:68`
  `this.f12001k = certificatePinner;`
- `sources/okhttp3/Address.java:76`
  `public CertificatePinner certificatePinner() {`
- `sources/okhttp3/Address.java:106`
  `CertificatePinner certificatePinner = this.f12001k;`
- `sources/okhttp3/Address.java:107`
  `return iHashCode4 + (certificatePinner != null ? certificatePinner.hashCode() : 0);`
- `sources/okhttp3/CertificatePinner.java:20`
  `public final class CertificatePinner {`
- `sources/okhttp3/CertificatePinner.java:21`
  `public static final CertificatePinner DEFAULT = new Builder().build();`
- `sources/okhttp3/CertificatePinner.java:42`
  `public CertificatePinner build() {`
- `sources/okhttp3/CertificatePinner.java:43`
  `return new CertificatePinner(new LinkedHashSet(this.f12048a), null);`
- `sources/okhttp3/CertificatePinner.java:74`
  `if (!str2.startsWith("sha256/")) {`
- `sources/okhttp3/CertificatePinner.java:75`
  `throw new IllegalArgumentException(c.a.a("pins must start with 'sha256/' or 'sha1/': ", str2));`
- `sources/okhttp3/CertificatePinner.java:77`
  `this.f12050c = "sha256/";`
- `sources/okhttp3/CertificatePinner.java:104`
  `public CertificatePinner(Set<a> set, @Nullable CertificateChainCleaner certificateChainCleaner) {`
- `sources/okhttp3/CertificatePinner.java:113`
  `StringBuilder sbA = androidx.activity.b.a("sha256/");`
- `sources/okhttp3/CertificatePinner.java:126`
  `if (obj instanceof CertificatePinner) {`
- `sources/okhttp3/CertificatePinner.java:127`
  `CertificatePinner certificatePinner = (CertificatePinner) obj;`
- `sources/okhttp3/CertificatePinner.java:128`
  `if (Util.equal(this.b, certificatePinner.b) && this.f12047a.equals(certificatePinner.f12047a)) {`
- `sources/okhttp3/CertificatePinner.java:184`
  `if (aVar.f12050c.equals("sha256/")) {`
- `sources/okhttp3/OkHttpClient.java:97`
  `public final CertificatePinner f12144p;`
- `sources/okhttp3/OkHttpClient.java:181`
  `public CertificatePinner f12168p;`
- `sources/okhttp3/OkHttpClient.java:228`
  `this.f12168p = CertificatePinner.DEFAULT;`
- `sources/okhttp3/OkHttpClient.java:281`
  `public Builder certificatePinner(CertificatePinner certificatePinner) {`
- `sources/okhttp3/OkHttpClient.java:282`
  `Objects.requireNonNull(certificatePinner, "certificatePinner == null");`
- `sources/okhttp3/OkHttpClient.java:283`
  `this.f12168p = certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:641`
  `public CertificatePinner certificatePinner() {`
- `sources/okhttp3/OkHttpClient.java:790`
  `CertificatePinner certificatePinner = builder.f12168p;`
- `sources/okhttp3/OkHttpClient.java:792`
  `this.f12144p = Util.equal(certificatePinner.b, certificateChainCleaner) ? certificatePinner : new CertificatePinner(certificatePinner.f12047a, certificateChainCleaner);`
- `sources/okhttp3/internal/connection/RealConnection.java:23`
  `import okhttp3.CertificatePinner;`
- `sources/okhttp3/internal/connection/RealConnection.java:200`
  `throw new SSLPeerUnverifiedException("Hostname " + address.url().host() + " not verified:\n    certificate: " + CertificatePinner.pin(x509Certificate) + "\n    DN: " + x509Certificate.getSubjectDN().getName() + "\n    subjectAltNames: " + OkHostnameVerifier.allSubjectAltNames(x509Certificate));`
- `sources/okhttp3/internal/connection/RealConnection.java:202`
  `address.certificatePinner().check(address.url().host(), handshake.peerCertificates());`
- `sources/okhttp3/internal/connection/RealConnection.java:282`
  `address.certificatePinner().check(address.url().host(), handshake().peerCertificates());`
- `sources/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:18`
  `import okhttp3.CertificatePinner;`
- `sources/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:51`
  `CertificatePinner certificatePinner;`
- `sources/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:56`
  `certificatePinner = this.f12339a.certificatePinner();`
- `sources/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:60`
  `certificatePinner = null;`
- `sources/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:62`
  `return new Address(httpUrl.host(), httpUrl.port(), this.f12339a.dns(), this.f12339a.socketFactory(), sSLSocketFactory, hostnameVerifier, certificatePinner, this.f12339a.proxyAuthenticator(), this.f12339a.proxy(), this.f12339a.protocols(), this.f12339a.connectionSpecs(), this.f12339a.proxySelector())...`

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
- `resources/res/drawable/circle_blue.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/circle_green.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/circle_grey.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/circle_yellow.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/divider.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/ic_arrow_back_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_calendar_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_clear_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_close_white_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_edit_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_keyboard_arrow_left_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`

## BR014

paper_id: B022
paper_title: A Study of Android Application Security

- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2089`
  `boolean z4 = KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1;`
- `sources/androidx/appcompat/app/f.java:329`
  `menuB.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);`
- `sources/androidx/appcompat/app/WindowDecorActionBar.java:956`
  `menu.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);`
- `sources/androidx/core/content/ContextCompat.java:55`
  `import android.telephony.TelephonyManager;`
- `sources/androidx/core/content/ContextCompat.java:131`
  `map.put(TelephonyManager.class, "phone");`

## BR015

paper_id: B022
paper_title: A Study of Android Application Security

- `sources/com/alibaba/fastjson/JSON.java:46`
  `public static TimeZone defaultTimeZone = TimeZone.getDefault();`
- `sources/com/alibaba/fastjson/JSON.java:47`
  `public static Locale defaultLocale = Locale.getDefault();`
- `sources/com/google/android/material/datepicker/e.java:80`
  `textView.setText(this.f4884a.getDisplayName(7, f4883d, Locale.getDefault()));`
- `sources/com/google/android/material/datepicker/e.java:81`
  `textView.setContentDescription(String.format(viewGroup.getContext().getString(R.string.mtrl_picker_day_of_week_column_header), this.f4884a.getDisplayName(7, 2, Locale.getDefault())));`
- `sources/com/google/android/material/datepicker/RangeDateSelector.java:235`
  `pairCreate = calendarI.get(1) == calendarI2.get(1) ? calendarI.get(1) == calendarH.get(1) ? Pair.create(d.c(l4.longValue(), Locale.getDefault()), d.c(l5.longValue(), Locale.getDefault())) : Pair.create(d.c(l4.longValue(), Locale.getDefault()), d.d(l5.longValue(), Locale.getDefault())) : Pair.create(...`
- `sources/com/google/android/material/datepicker/SingleDateSelector.java:114`
  `return resources.getString(R.string.mtrl_picker_date_header_selected, d.d(l4.longValue(), Locale.getDefault()));`
- `sources/com/google/android/material/internal/ManufacturerUtils.java:10`
  `return Build.MANUFACTURER.equalsIgnoreCase("samsung");`
- `sources/com/scwang/smartrefresh/layout/header/ClassicsHeader.java:357`
  `this.mLastUpdateFormat = new SimpleDateFormat(this.mTextUpdate, Locale.getDefault());`

## BR016

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `sources/com/contec/verify/ContecFoetalEncryptUtils.java:11`
  `private native int getAppKey(byte[] bArr, byte[] bArr2, byte[] bArr3);`

## BR017

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `sources/androidx/core/content/pm/PackageInfoCompat.java:73`
  `bArr3[i] = MessageDigest.getInstance("SHA256").digest(signatures.get(i).toByteArray());`
- `sources/com/contec/spo2/code/tools/a.java:12`
  `byte[] bArrDigest = MessageDigest.getInstance("MD5").digest(bArr);`
- `sources/com/yuwell/androidbase/tool/FileManager.java:34`
  `MessageDigest messageDigest = MessageDigest.getInstance("MD5");`
- `sources/com/yuwell/base/util/EncryptUtil.java:26`
  `f5688a = SecretKeyFactory.getInstance("DES").generateSecret(new DESKeySpec(b));`
- `sources/com/yuwell/base/util/EncryptUtil.java:34`
  `MessageDigest messageDigest = MessageDigest.getInstance("MD5");`
- `sources/com/yuwell/base/util/EncryptUtil.java:35`
  `messageDigest.update(str.getBytes());`
- `sources/com/yuwell/base/util/EncryptUtil.java:36`
  `byte[] bArrDigest = messageDigest.digest();`
- `sources/com/yuwell/base/util/EncryptUtil.java:61`
  `Cipher cipher = Cipher.getInstance("DES/NoPadding");`
- `sources/com/yuwell/base/util/EncryptUtil.java:90`
  `Cipher cipher = Cipher.getInstance("DES/PKCS7Padding");`
- `sources/okio/ByteString.java:24`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/org/greenrobot/essentials/StringUtils.java:38`
  `MessageDigest messageDigest = MessageDigest.getInstance(str2);`
- `sources/org/greenrobot/essentials/StringUtils.java:39`
  `messageDigest.update(str.getBytes(str3));`
- `sources/org/greenrobot/essentials/StringUtils.java:40`
  `return hex(messageDigest.digest());`
- `sources/org/greenrobot/essentials/io/IoUtils.java:32`
  `MessageDigest messageDigest = MessageDigest.getInstance(str);`
- `sources/org/greenrobot/essentials/io/IoUtils.java:37`
  `return messageDigest.digest();`
- `sources/org/greenrobot/essentials/io/IoUtils.java:39`
  `messageDigest.update(bArr, 0, i);`

## BR018

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/com/airbnb/lottie/model/layer/BaseLayer.java:360`
  `this.f3796h.set(CircleImageView.X_OFFSET, CircleImageView.X_OFFSET, canvas.getWidth(), canvas.getHeight());`
- `sources/com/airbnb/lottie/model/layer/ImageLayer.java:68`
  `this.f3817x.set(0, 0, imageAsset.getWidth(), imageAsset.getHeight());`
- `sources/com/airbnb/lottie/model/layer/ImageLayer.java:69`
  `this.f3818y.set(0, 0, (int) (imageAsset.getWidth() * fDpScale), (int) (imageAsset.getHeight() * fDpScale));`
- `sources/com/airbnb/lottie/model/layer/ImageLayer.java:78`
  `rectF.set(rectF.left, rectF.top, Math.min(rectF.right, r6.getWidth()), Math.min(rectF.bottom, r6.getHeight()));`
- `sources/com/airbnb/lottie/parser/LayerParser.java:14`
  `return new Layer(Collections.emptyList(), lottieComposition, "__container", -1L, Layer.LayerType.PreComp, -1L, null, Collections.emptyList(), new AnimatableTransform(), 0, 0, 0, CircleImageView.X_OFFSET, CircleImageView.X_OFFSET, bounds.width(), bounds.height(), null, null, Collections.emptyList(), ...`
- `sources/com/contec/spo2/code/bean/a.java:1`
  `package com.contec.spo2.code.bean;`
- `sources/com/contec/spo2/code/bean/b.java:1`
  `package com.contec.spo2.code.bean;`
- `sources/com/contec/spo2/code/bean/c.java:1`
  `package com.contec.spo2.code.bean;`
- `sources/com/contec/spo2/code/bean/d.java:1`
  `package com.contec.spo2.code.bean;`
- `sources/com/contec/spo2/code/bean/DayStepsData.java:1`
  `package com.contec.spo2.code.bean;`
- `sources/com/contec/spo2/code/bean/DayStepsData.java:6`
  `public class DayStepsData implements Serializable {`
- `sources/com/contec/spo2/code/bean/DayStepsData.java:21`
  `public int getCalorie() {`
- `sources/com/contec/spo2/code/bean/DayStepsData.java:33`
  `public int getStepCount() {`
- `sources/com/contec/spo2/code/bean/DayStepsData.java:41`
  `public void setCalorie(int i) {`
- `sources/com/contec/spo2/code/bean/DayStepsData.java:53`
  `public void setStepCount(int i) {`
- `sources/com/contec/spo2/code/bean/DeviceType.java:1`
  `package com.contec.spo2.code.bean;`
- `sources/com/contec/spo2/code/bean/e.java:1`
  `package com.contec.spo2.code.bean;`
- `sources/com/contec/spo2/code/bean/EcgData.java:1`
  `package com.contec.spo2.code.bean;`
- `sources/com/contec/spo2/code/bean/EcgData.java:7`
  `public class EcgData implements Serializable {`
- `sources/com/contec/spo2/code/bean/EcgData.java:56`
  `public int[] getEcgData() {`
- `sources/com/contec/spo2/code/bean/EcgData.java:108`
  `public void setEcgData(int[] iArr) {`
- `sources/com/contec/spo2/code/bean/f.java:1`
  `package com.contec.spo2.code.bean;`
- `sources/com/contec/spo2/code/bean/FiveMinStepsData.java:1`
  `package com.contec.spo2.code.bean;`
- `sources/com/contec/spo2/code/bean/FiveMinStepsData.java:6`
  `public class FiveMinStepsData implements Serializable {`
- `sources/com/contec/spo2/code/bean/FiveMinStepsData.java:33`
  `public short[] getStepFiveDataBean() {`
- `sources/com/contec/spo2/code/bean/FiveMinStepsData.java:53`
  `public void setStepFiveDataBean(short[] sArr) {`
- `sources/com/contec/spo2/code/bean/g.java:1`
  `package com.contec.spo2.code.bean;`
- `sources/com/contec/spo2/code/bean/PieceData.java:1`
  `package com.contec.spo2.code.bean;`
- `sources/com/contec/spo2/code/bean/PieceData.java:51`
  `public int[] getSpo2Data() {`
- `sources/com/contec/spo2/code/bean/PieceData.java:87`
  `public void setSpo2Data(int[] iArr) {`
- `sources/com/contec/spo2/code/bean/SdkConstants.java:1`
  `package com.contec.spo2.code.bean;`
- `sources/com/contec/spo2/code/bean/SdkConstants.java:18`
  `public static final int ERRORCODE_CONTINUE_DELETE_SPO2_TIMEOUT = 10551553;`
- `sources/com/contec/spo2/code/bean/SdkConstants.java:23`
  `public static final int ERRORCODE_CONTINUE_INFO_SPO2_TIMEOUT = 10486017;`
- `sources/com/contec/spo2/code/bean/SdkConstants.java:27`
  `public static final int ERRORCODE_CONTINUE_SPO2_DATA_TIMEOUT = 10682624;`
- `sources/com/contec/spo2/code/bean/SdkConstants.java:29`
  `public static final int ERRORCODE_DAY_STEPS_TIMEOUT = 9568512;`
- `sources/com/contec/spo2/code/bean/SdkConstants.java:32`
  `public static final int ERRORCODE_ECG_INFO_TIMEOUT = 9765120;`
- `sources/com/contec/spo2/code/bean/SdkConstants.java:33`
  `public static final int ERRORCODE_ECG_TIMEOUT = 9830656;`
- `sources/com/contec/spo2/code/bean/SdkConstants.java:35`
  `public static final int ERRORCODE_FIVE_MIN_STEPS_INFO_TIMEOUT = 9634048;`
- `sources/com/contec/spo2/code/bean/SdkConstants.java:36`
  `public static final int ERRORCODE_FIVE_MIN_STEPS_TIMEOUT = 9699584;`
- `sources/com/contec/spo2/code/bean/SdkConstants.java:40`
  `public static final int ERRORCODE_PIECE_CODE_SPO2_TIMEOUT = 10290177;`

## BR019

paper_id: B011
paper_title: Locking it down: The privacy and security of mobile medication apps

- `sources/androidx/appcompat/widget/ActivityChooserModel.java:184`
  `map.put(new ComponentName(activityInfo.packageName, activityInfo.name), activityResolveInfo);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:403`
  `this.f1215a.put(getId(), this);`
- `sources/androidx/transition/ChangeBounds.java:435`
  `transitionValues.values.put("android:changeBounds:bounds", new Rect(view.getLeft(), view.getTop(), view.getRight(), view.getBottom()));`
- `sources/androidx/transition/ChangeClipBounds.java:88`
  `transitionValues.values.put("android:clipBounds:clip", clipBounds);`
- `sources/androidx/transition/ChangeClipBounds.java:90`
  `transitionValues.values.put("android:clipBounds:bounds", new Rect(0, 0, view.getWidth(), view.getHeight()));`
- `sources/androidx/transition/Explode.java:32`
  `transitionValues.values.put("android:explode:screenBounds", new Rect(i, i4, view.getWidth() + i, view.getHeight() + i4));`
- `sources/androidx/transition/VisibilityPropagation.java:33`
  `transitionValues.values.put("android:visibilityPropagation:center", iArr);`
- `sources/com/airbnb/lottie/animation/content/GradientStrokeContent.java:103`
  `this.f3623o.put(jA, linearGradient2);`
- `sources/com/airbnb/lottie/animation/content/GradientStrokeContent.java:125`
  `this.f3624p.put(jA2, radialGradient2);`
- `sources/com/contec/spo2/code/connect/ContecSdk.java:127`
  `map.put("SpO201", DeviceType.CMS50E);`
- `sources/com/contec/spo2/code/connect/ContecSdk.java:128`
  `this.f4130l.put("SpO202", DeviceType.CMS50F);`
- `sources/com/contec/spo2/code/connect/ContecSdk.java:129`
  `this.f4130l.put("SpO206", DeviceType.CMS50I);`
- `sources/com/contec/spo2/code/connect/ContecSdk.java:130`
  `this.f4130l.put("SpO208", DeviceType.CMS50D);`
- `sources/com/contec/spo2/code/connect/ContecSdk.java:133`
  `map2.put("SpO209", deviceType);`
- `sources/com/contec/spo2/code/connect/ContecSdk.java:134`
  `this.f4130l.put("SpO210", deviceType);`
- `sources/com/yuwell/bluetooth/le/device/bpm/BPMData.java:6`
  `import org.json.JSONObject;`
- `sources/com/yuwell/bluetooth/le/device/oxi/BloodOxygenData.java:4`
  `import org.json.JSONObject;`
- `sources/com/yuwell/bluetooth/le/device/oxi/OximeterManager.java:341`
  `sbA6.append(bloodOxygenData.toJsonString());`
- `sources/l/c.java:120`
  `simpleArrayMap.put(uri, byteBufferMmap);`
- `sources/okhttp3/internal/cache/CacheInterceptor.java:98`
  `CacheRequest cacheRequestPut = this.f12243a.put(responseBuild2);`
- `sources/w2/a.java:127`
  `this.f13417c.put(Type.CRN, "CRN");`
- `sources/w2/a.java:128`
  `this.f13417c.put(Type.HORIZONTALPAGEBREAKS, "HORIZONTALPAGEBREAKS");`
- `sources/w2/a.java:129`
  `this.f13417c.put(Type.VERTICALPAGEBREAKS, "VERTICALPAGEBREAKS");`
- `sources/w2/a.java:130`
  `this.f13417c.put(Type.DEFAULTROWHEIGHT, "DEFAULTROWHEIGHT");`
- `sources/w2/a.java:131`
  `this.f13417c.put(Type.TEMPLATE, "TEMPLATE");`
- `sources/w2/a.java:132`
  `this.f13417c.put(Type.PANE, "PANE");`
- `sources/w2/a.java:133`
  `this.f13417c.put(Type.SCL, "SCL");`
- `sources/w2/a.java:134`
  `this.f13417c.put(Type.PALETTE, "PALETTE");`

## BR020

paper_id: B012
paper_title: Reviewing the data security and privacy policies of mobile apps for depression

- `sources/androidx/core/provider/d.java:64`
  `cursorQuery = context.getContentResolver().query(uriBuild, new String[]{"_id", FontsContractCompat.Columns.FILE_ID, FontsContractCompat.Columns.TTC_INDEX, FontsContractCompat.Columns.VARIATION_SETTINGS, FontsContractCompat.Columns.WEIGHT, FontsContractCompat.Columns.ITALIC, FontsContractCompat.Colum...`
- `sources/androidx/core/provider/d.java:65`
  `if (cursorQuery != null && cursorQuery.getCount() > 0) {`
- `sources/androidx/core/provider/d.java:66`
  `int columnIndex = cursorQuery.getColumnIndex(FontsContractCompat.Columns.RESULT_CODE);`
- `sources/androidx/core/provider/d.java:68`
  `int columnIndex2 = cursorQuery.getColumnIndex("_id");`
- `sources/androidx/core/provider/d.java:69`
  `int columnIndex3 = cursorQuery.getColumnIndex(FontsContractCompat.Columns.FILE_ID);`
- `sources/androidx/core/provider/d.java:70`
  `int columnIndex4 = cursorQuery.getColumnIndex(FontsContractCompat.Columns.TTC_INDEX);`
- `sources/androidx/core/provider/d.java:71`
  `int columnIndex5 = cursorQuery.getColumnIndex(FontsContractCompat.Columns.WEIGHT);`
- `sources/androidx/core/provider/d.java:72`
  `int columnIndex6 = cursorQuery.getColumnIndex(FontsContractCompat.Columns.ITALIC);`
- `sources/androidx/core/provider/d.java:73`
  `while (cursorQuery.moveToNext()) {`
- `sources/androidx/core/provider/d.java:74`
  `int i = columnIndex != -1 ? cursorQuery.getInt(columnIndex) : 0;`
- `sources/androidx/core/provider/d.java:75`
  `arrayList.add(new FontsContractCompat.FontInfo(columnIndex3 == -1 ? ContentUris.withAppendedId(uriBuild, cursorQuery.getLong(columnIndex2)) : ContentUris.withAppendedId(uriBuild2, cursorQuery.getLong(columnIndex3)), columnIndex4 != -1 ? cursorQuery.getInt(columnIndex4) : 0, columnIndex5 != -1 ? curs...`
- `sources/com/yuwell/healthmanager/data/model/BPMeasurement.java:7`
  `@Entity`
- `sources/com/yuwell/healthmanager/data/model/BPMeasurementCursor.java:5`
  `import io.objectbox.Cursor;`
- `sources/com/yuwell/healthmanager/data/model/BPMeasurementCursor.java:8`
  `import io.objectbox.internal.CursorFactory;`
- `sources/com/yuwell/healthmanager/data/model/BPMeasurementCursor.java:13`
  `public final class BPMeasurementCursor extends Cursor<BPMeasurement> {`
- `sources/com/yuwell/healthmanager/data/model/BPMeasurementCursor.java:41`
  `public static final class a implements CursorFactory<BPMeasurement> {`
- `sources/com/yuwell/healthmanager/data/model/BPMeasurementCursor.java:42`
  `@Override // io.objectbox.internal.CursorFactory`
- `sources/com/yuwell/healthmanager/data/model/BPMeasurementCursor.java:43`
  `public Cursor<BPMeasurement> createCursor(Transaction transaction, long j4, BoxStore boxStore) {`
- `sources/com/yuwell/healthmanager/data/model/BPMeasurementCursor.java:44`
  `return new BPMeasurementCursor(transaction, j4, boxStore);`
- `sources/com/yuwell/healthmanager/data/model/BPMeasurementCursor.java:48`
  `public BPMeasurementCursor(Transaction transaction, long j4, BoxStore boxStore) {`
- `sources/com/yuwell/healthmanager/data/model/BPMeasurementCursor.java:52`
  `@Override // io.objectbox.Cursor`
- `sources/com/yuwell/healthmanager/data/model/BPMeasurementCursor.java:58`
  `@Override // io.objectbox.Cursor`
- `sources/com/yuwell/healthmanager/data/model/BPMeasurementCursor.java:64`
  `Cursor.collect313311(this.cursor, 0L, 1, i4, str, 0, null, 0, null, 0, null, i5, i5 != 0 ? date.getTime() : 0L, f5811e, bPMeasurement.deleteFlag, f5814h, bPMeasurement.pulseRate, f5815j, bPMeasurement.level, f5816k, bPMeasurement.user, 0, 0, f5812f, bPMeasurement.sbp, 0, 0.0d);`
- `sources/com/yuwell/healthmanager/data/model/BPMeasurementCursor.java:65`
  `long jCollect313311 = Cursor.collect313311(this.cursor, bPMeasurement.id, 2, 0, null, 0, null, 0, null, 0, null, 0, 0L, 0, 0L, 0, 0L, 0, 0, 0, 0, 0, 0, f5813g, bPMeasurement.dbp, 0, 0.0d);`
- `sources/com/yuwell/healthmanager/data/model/BPMeasurement_.java:3`
  `import com.yuwell.healthmanager.data.model.BPMeasurementCursor;`
- `sources/com/yuwell/healthmanager/data/model/BPMeasurement_.java:7`
  `import io.objectbox.internal.CursorFactory;`
- `sources/com/yuwell/healthmanager/data/model/BPMeasurement_.java:29`
  `public static final CursorFactory<BPMeasurement> __CURSOR_FACTORY = new BPMeasurementCursor.a();`
- `sources/com/yuwell/healthmanager/data/model/BPMeasurement_.java:76`
  `public CursorFactory<BPMeasurement> getCursorFactory() {`
- `sources/com/yuwell/healthmanager/data/model/BPMeasurement_.java:77`
  `return __CURSOR_FACTORY;`
- `sources/com/yuwell/healthmanager/data/model/FetalHeartMeasurement.java:8`
  `@Entity`
- `sources/com/yuwell/healthmanager/data/model/FetalHeartMeasurementCursor.java:6`
  `import io.objectbox.Cursor;`
- `sources/com/yuwell/healthmanager/data/model/FetalHeartMeasurementCursor.java:9`
  `import io.objectbox.internal.CursorFactory;`
- `sources/com/yuwell/healthmanager/data/model/FetalHeartMeasurementCursor.java:14`
  `public final class FetalHeartMeasurementCursor extends Cursor<FetalHeartMeasurement> {`
- `sources/com/yuwell/healthmanager/data/model/FetalHeartMeasurementCursor.java:39`
  `public static final class a implements CursorFactory<FetalHeartMeasurement> {`
- `sources/com/yuwell/healthmanager/data/model/FetalHeartMeasurementCursor.java:40`
  `@Override // io.objectbox.internal.CursorFactory`
- `sources/com/yuwell/healthmanager/data/model/FetalHeartMeasurementCursor.java:41`
  `public Cursor<FetalHeartMeasurement> createCursor(Transaction transaction, long j4, BoxStore boxStore) {`
- `sources/com/yuwell/healthmanager/data/model/FetalHeartMeasurementCursor.java:42`
  `return new FetalHeartMeasurementCursor(transaction, j4, boxStore);`
- `sources/com/yuwell/healthmanager/data/model/FetalHeartMeasurementCursor.java:46`
  `public FetalHeartMeasurementCursor(Transaction transaction, long j4, BoxStore boxStore) {`
- `sources/com/yuwell/healthmanager/data/model/FetalHeartMeasurementCursor.java:50`
  `@Override // io.objectbox.Cursor`
- `sources/com/yuwell/healthmanager/data/model/FetalHeartMeasurementCursor.java:56`
  `@Override // io.objectbox.Cursor`

## BR021

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `resources/AndroidManifest.xml:197`
  `<provider`
- `resources/AndroidManifest.xml:206`
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

## BR023

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `sources/androidx/lifecycle/ProcessLifecycleOwnerInitializer.java:19`
  `public class ProcessLifecycleOwnerInitializer extends ContentProvider {`

## BR024

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `sources/androidx/core/content/FileProvider.java:195`
  `if (!providerInfo.grantUriPermissions) {`

## BR026

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:26`
  `return SharedPreferencesUtil.getSharedPreferences(a(), "auto_save", true);`
- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:30`
  `return SharedPreferencesUtil.getSharedPreferences(a(), "bg_device", "");`
- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:34`
  `return SharedPreferencesUtil.getSharedPreferences(a(), BG_UNTT, 0);`
- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:38`
  `return SharedPreferencesUtil.getSharedPreferences(a(), "bo_device", "");`
- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:42`
  `return SharedPreferencesUtil.getSharedPreferences(a(), "bp_device", "");`
- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:46`
  `return SharedPreferencesUtil.getSharedPreferences(a(), BP_UNTT, 0);`
- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:50`
  `return SharedPreferencesUtil.getSharedPreferences(a(), "fetus_device", "");`
- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:54`
  `return SharedPreferencesUtil.getSharedPreferences(a(), HOME_PAGE, 0);`
- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:58`
  `return SharedPreferencesUtil.getSharedPreferences(a(), "hts_device", "");`
- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:62`
  `return SharedPreferencesUtil.getSharedPreferences(a(), HTS_UNIT, 1);`
- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:98`
  `SharedPreferencesUtil.setEditor(a(), "auto_save", z3);`
- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:102`
  `SharedPreferencesUtil.setEditor(a(), "bg_device", str);`
- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:106`
  `SharedPreferencesUtil.setEditor(a(), BG_UNTT, i);`
- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:110`
  `SharedPreferencesUtil.setEditor(a(), "bo_device", str);`
- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:114`
  `SharedPreferencesUtil.setEditor(a(), "bp_device", str);`
- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:118`
  `SharedPreferencesUtil.setEditor(a(), BP_UNTT, i);`
- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:122`
  `SharedPreferencesUtil.setEditor(a(), "fetus_device", str);`
- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:126`
  `SharedPreferencesUtil.setEditor(a(), "fetus_volume", z3);`
- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:134`
  `SharedPreferencesUtil.setEditor(a(), HOME_PAGE, i);`
- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:138`
  `SharedPreferencesUtil.setEditor(a(), "hts_device", str);`
- `sources/com/yuwell/healthmanager/utils/SettingUtil.java:142`
  `SharedPreferencesUtil.setEditor(a(), HTS_UNIT, i);`

## BR027

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/androidx/core/content/FileProvider.java:31`
  `public static final File f1553c = new File("/");`
- `sources/androidx/core/graphics/drawable/IconCompat.java:507`
  `return new FileInputStream(new File((String) this.f1613a));`
- `sources/androidx/core/util/AtomicFile.java:25`
  `this.b = new File(file.getPath() + ".new");`
- `sources/androidx/core/util/AtomicFile.java:26`
  `this.f1740c = new File(file.getPath() + ".bak");`
- `sources/com/github/mikephil/charting/charts/Chart.java:14`
  `import android.provider.MediaStore;`
- `sources/com/github/mikephil/charting/utils/FileUtils.java:199`
  `File file = new File(Environment.getExternalStorageDirectory(), str);`
- `sources/com/yuwell/androidbase/tool/FileManager.java:69`
  `return copyFile(new File(str), new File(str2));`
- `sources/com/yuwell/androidbase/tool/FileManager.java:81`
  `return getFileUri(context, new File(str, str2), str3);`
- `sources/com/yuwell/androidbase/tool/ImageUtil.java:13`
  `import android.provider.MediaStore;`
- `sources/com/yuwell/androidbase/tool/ImageUtil.java:140`
  `uri2 = MediaStore.Images.Media.EXTERNAL_CONTENT_URI;`
- `sources/com/yuwell/androidbase/tool/ImageUtil.java:142`
  `uri2 = MediaStore.Video.Media.EXTERNAL_CONTENT_URI;`
- `sources/com/yuwell/androidbase/tool/ImageUtil.java:144`
  `uri2 = MediaStore.Audio.Media.EXTERNAL_CONTENT_URI;`
- `sources/com/yuwell/healthmanager/utils/ExcelUtil.java:164`
  `File file = new File(str2);`
- `sources/com/yuwell/healthmanager/utils/ExcelUtil.java:209`
  `File file = new File(str2);`
- `sources/com/yuwell/healthmanager/utils/ExcelUtil.java:254`
  `File file = new File(str2);`
- `sources/com/yuwell/healthmanager/utils/ExcelUtil.java:299`
  `File file = new File(str2);`
- `sources/com/yuwell/healthmanager/view/impl/data/Data.java:86`
  `Uri uriForFile = FileProvider.getUriForFile(Data.this, Data.this.getPackageName() + ".fileprovider", new File(this.f6052a));`
- `sources/com/yuwell/healthmanager/view/impl/measure/fetus/FetalMeasureActivity.java:315`
  `this.D = new File(Constants.FETAL_AUDIO_PATH);`
- `sources/com/yuwell/healthmanager/view/impl/measure/fetus/FetalMeasureActivity.java:316`
  `this.F = new File(Constants.FETAL_RAW_PATH);`
- `sources/com/yuwell/healthmanager/view/impl/measure/fetus/FhtResultActivity.java:564`
  `File file = new File(fetalHeartMeasurement.localRawFilePath);`
- `sources/com/yuwell/healthmanager/view/impl/share/BpShareActivity.java:179`
  `Uri uriForFile = FileProvider.getUriForFile(this, getPackageName() + ".fileprovider", new File(str));`
- `sources/io/objectbox/BoxStore.java:320`
  `return g(new File(BoxStoreBuilder.d(obj), BoxStoreBuilder.c(str)).getCanonicalPath());`
- `sources/io/objectbox/BoxStoreBuilder.java:135`
  `return file != null ? new File(file, strC) : new File(strC);`
- `sources/io/objectbox/BoxStoreBuilder.java:237`
  `File file = new File(BoxStore.f(this.b), "data.mdb");`

## BR028

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `resources/AndroidManifest.xml:40`
  `android:allowBackup="true"`

## BR029

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:51`
  `android:exported="true">`
- `resources/AndroidManifest.xml:60`
  `android:exported="true"`
- `resources/AndroidManifest.xml:64`
  `android:exported="true"`
- `resources/AndroidManifest.xml:81`
  `android:exported="true"`
- `resources/AndroidManifest.xml:85`
  `android:exported="true"`
- `resources/AndroidManifest.xml:89`
  `android:exported="true"`
- `resources/AndroidManifest.xml:93`
  `android:exported="true"`
- `resources/AndroidManifest.xml:97`
  `android:exported="true"`
- `resources/AndroidManifest.xml:101`
  `android:exported="true"`
- `resources/AndroidManifest.xml:105`
  `android:exported="true"`
- `resources/AndroidManifest.xml:109`
  `android:exported="true"`
- `resources/AndroidManifest.xml:114`
  `android:exported="true"`
- `resources/AndroidManifest.xml:119`
  `android:exported="true"`
- `resources/AndroidManifest.xml:124`
  `android:exported="true"`
- `resources/AndroidManifest.xml:129`
  `android:exported="true"`
- `resources/AndroidManifest.xml:134`
  `android:exported="true"`
- `resources/AndroidManifest.xml:139`
  `android:exported="true"`
- `resources/AndroidManifest.xml:144`
  `android:exported="true"`
- `resources/AndroidManifest.xml:149`
  `android:exported="true"`
- `resources/AndroidManifest.xml:154`
  `android:exported="true"`
- `resources/AndroidManifest.xml:159`
  `android:exported="true"`
- `resources/AndroidManifest.xml:164`
  `android:exported="true"`
- `resources/AndroidManifest.xml:169`
  `android:exported="true"`
- `resources/AndroidManifest.xml:174`
  `android:exported="true"`

## BR031

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:216`
  `android:exported="true">`

## BR033

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/com/yuwell/healthmanager/utils/PermissionUtil.java:60`
  `intent.setData(Uri.parse(sbA.toString()));`

## BR034

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/com/yuwell/healthmanager/utils/PermissionPageManagement.java:18`
  `activity.startActivity(intent);`
- `sources/com/yuwell/healthmanager/utils/PermissionPageManagement.java:96`
  `activity.startActivity(intent);`
- `sources/com/yuwell/healthmanager/utils/PermissionPageManagement.java:130`
  `activity.startActivity(intent);`
- `sources/com/yuwell/healthmanager/utils/PermissionUtil.java:61`
  `activity.startActivity(intent);`

## BR035

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/com/yuwell/healthmanager/view/impl/setting/WebViewActivity.java:70`
  `this.webView.loadUrl(str);`
- `sources/com/yuwell/healthmanager/view/impl/statistics/BgStatistic.java:173`
  `this.mWebViewFrequence.loadUrl("file:///android_asset/bg-total.html");`
- `sources/com/yuwell/healthmanager/view/impl/statistics/BgStatistic.java:184`
  `this.mWebViewAverage.loadUrl("file:///android_asset/bg-avg.html");`
- `sources/com/yuwell/healthmanager/view/impl/statistics/BoStatistic.java:104`
  `this.mWebViewFrequence.loadUrl("file:///android_asset/bo-total.html");`
- `sources/com/yuwell/healthmanager/view/impl/statistics/BpStatistic.java:164`
  `this.mWebViewFrequence.loadUrl("file:///android_asset/bp-total.html");`
- `sources/com/yuwell/healthmanager/view/impl/statistics/BpStatistic.java:175`
  `this.mWebViewAverage.loadUrl("file:///android_asset/bp-avg.html");`
- `sources/com/yuwell/healthmanager/view/impl/statistics/HtsStatistic.java:125`
  `this.mWebViewFrequence.loadUrl("file:///android_asset/hts-total.html");`

## BR040

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `sources/no/nordicsemi/android/ble/b.java:41`
  `((ReadRequest) this.f11687c).lambda$notifyValueChanged$1(this.b, (byte[]) this.f11688d);`
- `sources/no/nordicsemi/android/ble/BleManager.java:336`
  `ReadRequest readRequestNewReadBatteryLevelRequest = Request.newReadBatteryLevelRequest();`
- `sources/no/nordicsemi/android/ble/BleManager.java:337`
  `readRequestNewReadBatteryLevelRequest.s(this.f11572d);`
- `sources/no/nordicsemi/android/ble/BleManager.java:340`
  `readRequestNewReadBatteryLevelRequest.with(new DataReceivedCallback() { // from class: no.nordicsemi.android.ble.g`
- `sources/no/nordicsemi/android/ble/BleManager.java:349`
  `public ReadRequest readCharacteristic(@Nullable BluetoothGattCharacteristic bluetoothGattCharacteristic) {`
- `sources/no/nordicsemi/android/ble/BleManager.java:350`
  `ReadRequest readRequestNewReadRequest = Request.newReadRequest(bluetoothGattCharacteristic);`
- `sources/no/nordicsemi/android/ble/BleManager.java:351`
  `readRequestNewReadRequest.s(this.f11572d);`
- `sources/no/nordicsemi/android/ble/BleManager.java:352`
  `return readRequestNewReadRequest;`
- `sources/no/nordicsemi/android/ble/BleManager.java:356`
  `public ReadRequest readDescriptor(@Nullable BluetoothGattDescriptor bluetoothGattDescriptor) {`
- `sources/no/nordicsemi/android/ble/BleManager.java:357`
  `ReadRequest readRequestNewReadRequest = Request.newReadRequest(bluetoothGattDescriptor);`
- `sources/no/nordicsemi/android/ble/BleManager.java:358`
  `readRequestNewReadRequest.s(this.f11572d);`
- `sources/no/nordicsemi/android/ble/BleManager.java:359`
  `return readRequestNewReadRequest;`
- `sources/no/nordicsemi/android/ble/BleManager.java:533`
  `public WaitForReadRequest waitForRead(@Nullable BluetoothGattCharacteristic bluetoothGattCharacteristic) {`
- `sources/no/nordicsemi/android/ble/BleManager.java:534`
  `WaitForReadRequest waitForReadRequest = new WaitForReadRequest(22, bluetoothGattCharacteristic);`
- `sources/no/nordicsemi/android/ble/BleManager.java:535`
  `waitForReadRequest.y(this.f11572d);`
- `sources/no/nordicsemi/android/ble/BleManager.java:536`
  `return waitForReadRequest;`
- `sources/no/nordicsemi/android/ble/BleManager.java:650`
  `public WaitForReadRequest waitForRead(@Nullable BluetoothGattCharacteristic bluetoothGattCharacteristic, @Nullable byte[] bArr) {`
- `sources/no/nordicsemi/android/ble/BleManager.java:651`
  `WaitForReadRequest waitForReadRequest = new WaitForReadRequest(22, bluetoothGattCharacteristic, bArr, 0, bArr != null ? bArr.length : 0);`
- `sources/no/nordicsemi/android/ble/BleManager.java:652`
  `waitForReadRequest.y(this.f11572d);`
- `sources/no/nordicsemi/android/ble/BleManager.java:653`
  `return waitForReadRequest;`
- `sources/no/nordicsemi/android/ble/BleManager.java:730`
  `public WaitForReadRequest waitForRead(@Nullable BluetoothGattCharacteristic bluetoothGattCharacteristic, @Nullable byte[] bArr, int i4, int i5) {`
- `sources/no/nordicsemi/android/ble/BleManager.java:731`
  `WaitForReadRequest waitForReadRequest = new WaitForReadRequest(22, bluetoothGattCharacteristic, bArr, i4, i5);`
- `sources/no/nordicsemi/android/ble/BleManager.java:732`
  `waitForReadRequest.y(this.f11572d);`
- `sources/no/nordicsemi/android/ble/BleManager.java:733`
  `return waitForReadRequest;`
- `sources/no/nordicsemi/android/ble/BleManager.java:745`
  `public WaitForReadRequest waitForRead(@Nullable BluetoothGattDescriptor bluetoothGattDescriptor) {`
- `sources/no/nordicsemi/android/ble/BleManager.java:746`
  `WaitForReadRequest waitForReadRequest = new WaitForReadRequest(22, bluetoothGattDescriptor);`
- `sources/no/nordicsemi/android/ble/BleManager.java:747`
  `waitForReadRequest.y(this.f11572d);`
- `sources/no/nordicsemi/android/ble/BleManager.java:748`
  `return waitForReadRequest;`
- `sources/no/nordicsemi/android/ble/BleManager.java:760`
  `public WaitForReadRequest waitForRead(@Nullable BluetoothGattDescriptor bluetoothGattDescriptor, @Nullable byte[] bArr) {`
- `sources/no/nordicsemi/android/ble/BleManager.java:761`
  `WaitForReadRequest waitForReadRequest = new WaitForReadRequest(22, bluetoothGattDescriptor, bArr, 0, bArr != null ? bArr.length : 0);`
- `sources/no/nordicsemi/android/ble/BleManager.java:762`
  `waitForReadRequest.y(this.f11572d);`
- `sources/no/nordicsemi/android/ble/BleManager.java:763`
  `return waitForReadRequest;`
- `sources/no/nordicsemi/android/ble/BleManager.java:767`
  `public WaitForReadRequest waitForRead(@Nullable BluetoothGattDescriptor bluetoothGattDescriptor, @Nullable byte[] bArr, int i4, int i5) {`
- `sources/no/nordicsemi/android/ble/BleManager.java:768`
  `WaitForReadRequest waitForReadRequest = new WaitForReadRequest(22, bluetoothGattDescriptor, bArr, i4, i5);`
- `sources/no/nordicsemi/android/ble/BleManager.java:769`
  `waitForReadRequest.y(this.f11572d);`
- `sources/no/nordicsemi/android/ble/BleManager.java:770`
  `return waitForReadRequest;`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:389`
  `if (request instanceof ReadRequest) {`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:390`
  `ReadRequest readRequest = (ReadRequest) request;`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:391`
  `readRequest.r(bluetoothGatt.getDevice(), value);`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:392`
  `if (readRequest.f11631u > 0) {`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:393`
  `BleManagerHandler.this.J(readRequest);`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:395`
  `readRequest.m(bluetoothGatt.getDevice());`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:410`
  `if (request2 instanceof ReadRequest) {`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:68`
  `public void onCharacteristicReadRequest(@NonNull BluetoothDevice bluetoothDevice, int i, int i4, @NonNull BluetoothGattCharacteristic bluetoothGattCharacteristic) {`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:69`
  `WaitForReadRequest waitForReadRequest;`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:88`
  `if ((awaitingRequest instanceof WaitForReadRequest) && awaitingRequest.f11636c == bluetoothGattCharacteristic && !awaitingRequest.u()) {`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:89`
  `waitForReadRequest = (WaitForReadRequest) bleManagerHandlerA.G;`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:90`
  `if (waitForReadRequest.f11667v == null) {`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:91`
  `waitForReadRequest.f11667v = value;`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:93`
  `value = waitForReadRequest.x(bleManagerHandlerA.f11595v);`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:95`
  `waitForReadRequest = null;`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:106`
  `if (waitForReadRequest == null) {`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:113`
  `waitForReadRequest.handler.post(new k0(waitForReadRequest, bluetoothDevice, bArr));`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:114`
  `waitForReadRequest.f11669x++;`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:115`
  `if (!waitForReadRequest.f11670y) {`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:119`
  `waitForReadRequest.m(bluetoothDevice);`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:214`
  `public void onDescriptorReadRequest(@NonNull BluetoothDevice bluetoothDevice, int i, int i4, @NonNull BluetoothGattDescriptor bluetoothGattDescriptor) {`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:215`
  `WaitForReadRequest waitForReadRequest;`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:234`
  `if ((awaitingRequest instanceof WaitForReadRequest) && awaitingRequest.f11637d == bluetoothGattDescriptor && !awaitingRequest.u()) {`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:235`
  `waitForReadRequest = (WaitForReadRequest) bleManagerHandlerA.G;`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:236`
  `if (waitForReadRequest.f11667v == null) {`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:237`
  `waitForReadRequest.f11667v = value;`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:239`
  `value = waitForReadRequest.x(bleManagerHandlerA.f11595v);`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:241`
  `waitForReadRequest = null;`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:252`
  `if (waitForReadRequest == null) {`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:259`
  `waitForReadRequest.handler.post(new k0(waitForReadRequest, bluetoothDevice, bArr));`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:260`
  `waitForReadRequest.f11669x++;`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:261`
  `if (!waitForReadRequest.f11670y) {`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:265`
  `waitForReadRequest.m(bluetoothDevice);`
- `sources/no/nordicsemi/android/ble/k0.java:9`
  `public final /* synthetic */ WaitForReadRequest f11844a;`
- `sources/no/nordicsemi/android/ble/k0.java:15`
  `public /* synthetic */ k0(WaitForReadRequest waitForReadRequest, BluetoothDevice bluetoothDevice, byte[] bArr) {`
- `sources/no/nordicsemi/android/ble/k0.java:16`
  `this.f11844a = waitForReadRequest;`
- `sources/no/nordicsemi/android/ble/q.java:35`
  `((WaitForReadRequest) this.b).lambda$notifySuccess$1((BluetoothDevice) this.f11856c);`
- `sources/no/nordicsemi/android/ble/ReadRequest.java:28`
  `public final class ReadRequest extends SimpleValueRequest<DataReceivedCallback> implements Operation {`
- `sources/no/nordicsemi/android/ble/ReadRequest.java:45`
  `public ReadRequest(@NonNull int i) {`
- `sources/no/nordicsemi/android/ble/ReadRequest.java:68`
  `public ReadRequest filter(@NonNull DataFilter dataFilter) {`
- `sources/no/nordicsemi/android/ble/ReadRequest.java:74`
  `public ReadRequest merge(@NonNull DataMerger dataMerger) {`
- `sources/no/nordicsemi/android/ble/ReadRequest.java:115`
  `public ReadRequest s(@NonNull i0 i0Var) {`
- `sources/no/nordicsemi/android/ble/ReadRequest.java:125`
  `public ReadRequest before(@NonNull BeforeCallback beforeCallback) {`
- `sources/no/nordicsemi/android/ble/ReadRequest.java:132`
  `public ReadRequest done(@NonNull SuccessCallback successCallback) {`

## BR043

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/com/alibaba/fastjson/serializer/SerializeWriter.java:12`
  `import no.nordicsemi.android.support.v18.scanner.ScanResult;`
- `sources/com/alibaba/fastjson/serializer/SerializeWriter.java:85`
  `for (int i4 = ScanResult.TX_POWER_NOT_PRESENT; i4 < 160; i4++) {`
- `sources/com/contec/spo2/code/a/a.java:5`
  `import no.nordicsemi.android.support.v18.scanner.ScanResult;`
- `sources/com/contec/spo2/code/a/a.java:24`
  `bArr[1] = (byte) (i & ScanResult.TX_POWER_NOT_PRESENT);`
- `sources/com/contec/spo2/code/a/a.java:25`
  `bArr[2] = (byte) (i4 & ScanResult.TX_POWER_NOT_PRESENT);`
- `sources/com/contec/spo2/code/a/a.java:50`
  `bArr[5] = (byte) (i7 & ScanResult.TX_POWER_NOT_PRESENT);`
- `sources/com/contec/spo2/code/a/a.java:51`
  `bArr[6] = (byte) ((i7 >> 7) & ScanResult.TX_POWER_NOT_PRESENT);`
- `sources/com/contec/spo2/code/a/a.java:101`
  `bArr[2] = (byte) (i4 & ScanResult.TX_POWER_NOT_PRESENT);`
- `sources/com/contec/spo2/code/a/a.java:102`
  `bArr[3] = (byte) ((i4 >> 7) & ScanResult.TX_POWER_NOT_PRESENT);`
- `sources/com/contec/spo2/code/a/a.java:114`
  `bArr[5] = (byte) (i7 & ScanResult.TX_POWER_NOT_PRESENT);`
- `sources/com/contec/spo2/code/a/a.java:115`
  `bArr[6] = (byte) ((i7 >> 7) & ScanResult.TX_POWER_NOT_PRESENT);`
- `sources/com/contec/spo2/code/a/a.java:116`
  `bArr[7] = (byte) ((i7 >> 14) & ScanResult.TX_POWER_NOT_PRESENT);`
- `sources/com/contec/spo2/code/a/a.java:168`
  `bArr[2] = (byte) (i4 & ScanResult.TX_POWER_NOT_PRESENT);`
- `sources/com/contec/spo2/code/a/a.java:169`
  `bArr[3] = (byte) ((i4 >> 7) & ScanResult.TX_POWER_NOT_PRESENT);`
- `sources/com/contec/spo2/code/a/a.java:184`
  `bArr[1] = (byte) (i & ScanResult.TX_POWER_NOT_PRESENT);`
- `sources/com/contec/spo2/code/a/a.java:190`
  `bArr[7] = (byte) (i9 & ScanResult.TX_POWER_NOT_PRESENT);`
- `sources/com/contec/spo2/code/a/a.java:191`
  `bArr[8] = (byte) ((i9 >> 7) & ScanResult.TX_POWER_NOT_PRESENT);`
- `sources/com/contec/spo2/code/a/a.java:208`
  `bArr[2] = (byte) (i4 & ScanResult.TX_POWER_NOT_PRESENT);`
- `sources/com/contec/spo2/code/a/a.java:209`
  `bArr[3] = (byte) ((i4 >> 7) & ScanResult.TX_POWER_NOT_PRESENT);`
- `sources/com/contec/spo2/code/a/a.java:233`
  `bArr[2] = (byte) (i4 & ScanResult.TX_POWER_NOT_PRESENT);`
- `sources/com/contec/spo2/code/a/a.java:234`
  `bArr[3] = (byte) ((i4 >> 7) & ScanResult.TX_POWER_NOT_PRESENT);`
- `sources/com/contec/spo2/code/a/f.java:16`
  `import no.nordicsemi.android.support.v18.scanner.ScanResult;`
- `sources/com/contec/spo2/code/a/f.java:393`
  `sendData(com.contec.spo2.code.a.a.h(ScanResult.TX_POWER_NOT_PRESENT));`
- `sources/com/contec/spo2/code/a/g.java:19`
  `import no.nordicsemi.android.support.v18.scanner.ScanResult;`
- `sources/com/contec/spo2/code/a/g.java:1343`
  `sendData(com.contec.spo2.code.a.a.h(ScanResult.TX_POWER_NOT_PRESENT));`
- `sources/com/contec/spo2/code/connect/ContecSdk.java:313`
  `this.f4122c.startLeScan(this.f4131m);`
- `sources/com/contec/spo2/code/tools/a.java:5`
  `import no.nordicsemi.android.support.v18.scanner.ScanResult;`
- `sources/com/contec/spo2/code/tools/a.java:14`
  `bArr2[i] = (byte) ((bArrDigest[i] ^ bArrDigest[i + 8]) & ScanResult.TX_POWER_NOT_PRESENT);`
- `sources/com/yuwell/bluetooth/le/core/BleScanner.java:10`
  `import no.nordicsemi.android.support.v18.scanner.BluetoothLeScannerCompat;`
- `sources/com/yuwell/bluetooth/le/core/BleScanner.java:91`
  `BluetoothLeScannerCompat.getScanner().startScan(list, new ScanSettings.Builder().setScanMode(2).setReportDelay(1000L).setUseHardwareBatchingIfSupported(false).build(), this.f5727g);`
- `sources/com/yuwell/bluetooth/le/core/BleScanner.java:103`
  `BluetoothLeScannerCompat.getScanner().stopScan(this.f5727g);`
- `sources/com/yuwell/bluetooth/le/core/BleScanner.java:114`
  `public final void restartScan() {`
- `sources/com/yuwell/bluetooth/le/core/BleScanner.java:119`
  `BleScanner.this.startScan(false);`
- `sources/com/yuwell/bluetooth/le/core/BleScanner.java:140`
  `public final void startScan(boolean z3) {`
- `sources/com/yuwell/bluetooth/le/core/BleService.java:23`
  `import no.nordicsemi.android.support.v18.scanner.ScanResult;`
- `sources/com/yuwell/bluetooth/le/core/BleService.java:52`
  `public void onBatchScanResults(@NonNull List<ScanResult> list) {`
- `sources/com/yuwell/bluetooth/le/core/BleService.java:53`
  `ScanResult next;`
- `sources/com/yuwell/bluetooth/le/core/BleService.java:54`
  `Iterator<ScanResult> it = list.iterator();`
- `sources/com/yuwell/bluetooth/le/core/BleService.java:75`
  `StringBuilder sbA2 = androidx.activity.b.a("onBatchScanResults(), Device=");`
- `sources/com/yuwell/bluetooth/le/core/BleService.java:120`
  `public void onScanResult(int i, @NonNull ScanResult scanResult) {`
- `sources/com/yuwell/bluetooth/le/core/BleService.java:122`
  `Log.d("BleService", "onScanResult: " + scanResult);`
- `sources/com/yuwell/bluetooth/le/core/BleService.java:159`
  `BleService.this.startScan(z3);`
- `sources/com/yuwell/bluetooth/le/core/BleService.java:189`
  `BleService.this.startScan(false);`
- `sources/com/yuwell/bluetooth/le/core/BleService.java:204`
  `BleService.this.scanner.restartScan();`
- `sources/com/yuwell/bluetooth/le/core/BleService.java:256`
  `public boolean onDeviceScanned(ScanResult scanResult) {`
- `sources/com/yuwell/bluetooth/le/core/BleService.java:258`
  `return (yUBleManager == null || yUBleManager.isConnected() || !this.mBleManager.connectable(scanResult.getDevice(), scanResult.getRssi(), scanResult.getScanRecord())) ? false : true;`
- `sources/com/yuwell/bluetooth/le/core/BleService.java:277`
  `public final void startScan(boolean z3) {`
- `sources/com/yuwell/bluetooth/le/core/BleService.java:278`
  `this.scanner.startScan(z3);`
- `sources/com/yuwell/bluetooth/le/core/BleService.java:304`
  `this.scanner.startScan(false);`
- `sources/com/yuwell/healthmanager/vm/MainViewModel.java:35`
  `import no.nordicsemi.android.support.v18.scanner.ScanResult;`
- `sources/com/yuwell/healthmanager/vm/MainViewModel.java:73`
  `public void onBatchScanResults(@NonNull List<ScanResult> list) {`
- `sources/com/yuwell/healthmanager/vm/MainViewModel.java:74`
  `ScanResult next;`
- `sources/com/yuwell/healthmanager/vm/MainViewModel.java:75`
  `super.onBatchScanResults(list);`
- `sources/com/yuwell/healthmanager/vm/MainViewModel.java:76`
  `Iterator<ScanResult> it = list.iterator();`
- `sources/com/yuwell/healthmanager/vm/MainViewModel.java:84`
  `StringBuilder sbA = b.a("onBatchScanResults(), Device=");`
- `sources/com/yuwell/healthmanager/vm/MainViewModel.java:134`
  `public void onScanResult(int i, @NonNull ScanResult scanResult) {`
- `sources/com/yuwell/healthmanager/vm/MainViewModel.java:135`
  `super.onScanResult(i, scanResult);`
- `sources/f1/g.java:4`
  `import android.bluetooth.le.ScanResult;`
- `sources/f1/g.java:11`
  `import no.nordicsemi.android.support.v18.scanner.BluetoothLeScannerCompat;`
- `sources/f1/g.java:42`
  `List<ScanResult> list = (List) this.f6648c;`
- `sources/f1/g.java:48`
  `a.b.this.d(((no.nordicsemi.android.support.v18.scanner.a) BluetoothLeScannerCompat.getScanner()).f(list));`
- `sources/f3/f.java:13`
  `import no.nordicsemi.android.support.v18.scanner.BluetoothLeScannerCompat;`
- `sources/f3/f.java:15`
  `import no.nordicsemi.android.support.v18.scanner.ScanResult;`
- `sources/f3/f.java:44`
  `public void onBatchScanResults(@NonNull List<ScanResult> list) {`
- `sources/f3/f.java:59`
  `intent.putExtra(BluetoothLeScannerCompat.EXTRA_CALLBACK_TYPE, 1);`
- `sources/f3/f.java:60`
  `intent.putParcelableArrayListExtra(BluetoothLeScannerCompat.EXTRA_LIST_SCAN_RESULT, new ArrayList<>(list));`
- `sources/f3/f.java:61`
  `intent.setExtrasClassLoader(ScanResult.class.getClassLoader());`
- `sources/f3/f.java:78`
  `intent.putExtra(BluetoothLeScannerCompat.EXTRA_ERROR_CODE, i);`
- `sources/f3/f.java:85`
  `public void onScanResult(int i, @NonNull ScanResult scanResult) {`
- `sources/f3/f.java:95`
  `intent.putExtra(BluetoothLeScannerCompat.EXTRA_CALLBACK_TYPE, i);`
- `sources/f3/f.java:96`
  `intent.putParcelableArrayListExtra(BluetoothLeScannerCompat.EXTRA_LIST_SCAN_RESULT, new ArrayList<>(Collections.singletonList(scanResult)));`
- `sources/f3/g.java:8`
  `import no.nordicsemi.android.support.v18.scanner.ScanResult;`
- `sources/f3/g.java:26`
  `public void onBatchScanResults(@NonNull List<ScanResult> list) {`
- `sources/f3/g.java:29`
  `scanCallback.onBatchScanResults(list);`
- `sources/f3/g.java:42`
  `public void onScanResult(int i, @NonNull ScanResult scanResult) {`
- `sources/f3/g.java:45`
  `scanCallback.onScanResult(i, scanResult);`
- `sources/h1/f.java:6`
  `import no.nordicsemi.android.support.v18.scanner.BluetoothLeScannerCompat;`
- `sources/h1/f.java:7`
  `import no.nordicsemi.android.support.v18.scanner.ScanResult;`
- `sources/h1/f.java:36`
  `((BluetoothLeScannerCompat.a) this.b).c(1, (ScanResult) this.f6691c);`
- `sources/jxl/biff/XFRecord.java:23`
  `import no.nordicsemi.android.support.v18.scanner.ScanResult;`

## BR044

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/androidx/core/content/ContextCompat.java:39`
  `import android.net.wifi.WifiManager;`
- `sources/androidx/core/content/ContextCompat.java:138`
  `map.put(WifiManager.class, "wifi");`

## BR047

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/a/k.java:66`
  `Log.e("ResourcesFlusher", "Could not retrieve value from ThemedResourceCache#mUnthemedEntries", e6);`
- `sources/androidx/activity/result/ActivityResultRegistry.java:162`
  `Log.w("ActivityResultRegistry", "Dropping pending result for request " + str + ": " + this.f102g.get(str));`
- `sources/androidx/activity/result/ActivityResultRegistry.java:166`
  `Log.w("ActivityResultRegistry", "Dropping pending result for request " + str + ": " + this.f103h.getParcelable(str));`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1200`
  `Log.i("AppCompatDelegate", "Failed to instantiate custom view inflater " + string + ". Falling back to default.", th);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1348`
  `Log.i("AppCompatDelegate", "The Activity's LayoutInflater already has a Factory installed so we can not install AppCompat's");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1604`
  `Log.i("AppCompatDelegate", "Failed to instantiate custom view inflater " + string + ". Falling back to default.", th);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2102`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2108`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR_OVERLAY id when requesting this feature.");`
- `sources/androidx/appcompat/content/res/AppCompatResources.java:81`
  `Log.e("AppCompatResources", "Failed to inflate ColorStateList, leaving it to the framework", e4);`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:181`
  `Log.w("SupportMenuInflater", "Cannot instantiate class: " + str, e4);`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:218`
  `Log.w("SupportMenuInflater", "Ignoring attribute 'itemActionViewLayout'. Action view already specified.");`
- `sources/androidx/appcompat/widget/AppCompatEditText.java:139`
  `Log.i("ReceiveContent", "Can't handle drop: no activity: view=" + this);`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:85`
  `Log.e("AsldcInflateDelegate", "Exception while inflating <animated-selector>", e4);`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:97`
  `Log.e("AvdcInflateDelegate", "Exception while inflating <animated-vector>", e4);`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:121`
  `Log.e("DrawableDelegate", "Exception while inflating <drawable>", e4);`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:137`
  `Log.e("VdcInflateDelegate", "Exception while inflating <vector>", e4);`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:380`
  `Log.e("ResourceManagerInternal", "Exception while inflating drawable", e4);`
- `sources/androidx/constraintlayout/widget/ConstraintSet.java:1227`
  `Log.w("ConstraintSet", sbA.toString());`
- `sources/androidx/constraintlayout/widget/ConstraintSet.java:1234`
  `Log.w("ConstraintSet", sbA2.toString());`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:537`
  `Log.e("CoordinatorLayout", "No keylines defined for " + this + " - attempted index lookup " + i);`
- `sources/androidx/core/app/NotificationManagerCompat.java:243`
  `Log.d("NotifManCompat", "Scheduling retry for " + i4 + " ms");`
- `sources/androidx/core/app/NotificationManagerCompat.java:338`
  `Log.d("NotifManCompat", "Connected to service " + componentName);`
- `sources/androidx/core/app/NotificationManagerCompat.java:346`
  `Log.d("NotifManCompat", "Disconnected from service " + componentName);`
- `sources/androidx/core/content/res/ColorStateListInflaterCompat.java:119`
  `Log.e("CSLCompat", "Failed to inflate ColorStateList.", e4);`
- `sources/androidx/core/content/res/ComplexColorCompat.java:52`
  `Log.e("ComplexColorCompat", "Failed to inflate ComplexColor.", e4);`
- `sources/androidx/core/graphics/TypefaceCompatUtil.java:98`
  `Log.e("TypefaceCompatUtil", "Error copying resource contents to temp file: " + e.getMessage());`
- `sources/androidx/core/os/TraceCompat.java:50`
  `Log.v("TraceCompat", "Unable to invoke asyncTraceBegin() via reflection.");`
- `sources/androidx/core/os/TraceCompat.java:66`
  `Log.v("TraceCompat", "Unable to invoke endAsyncSection() via reflection.");`
- `sources/androidx/core/os/TraceCompat.java:81`
  `Log.v("TraceCompat", "Unable to invoke isTagEnabled() via reflection.");`
- `sources/androidx/core/os/TraceCompat.java:94`
  `Log.v("TraceCompat", "Unable to invoke traceCounter() via reflection.");`
- `sources/androidx/core/view/ViewCompat.java:300`
  `Log.w("WindowInsetsCompat", sbA.toString(), e4);`
- `sources/androidx/core/view/ViewCompat.java:416`
  `Log.e("ViewCompat", "Couldn't find method", e4);`
- `sources/androidx/core/view/ViewCompat.java:642`
  `Log.d("ViewCompat", "Error calling dispatchFinishTemporaryDetach", e4);`
- `sources/androidx/core/view/ViewCompat.java:678`
  `Log.d("ViewCompat", "Error calling dispatchStartTemporaryDetach", e4);`
- `sources/androidx/core/view/WindowInsetsCompat.java:139`
  `Log.w("WindowInsetsCompat", sbA.toString(), e4);`
- `sources/androidx/core/view/WindowInsetsCompat.java:971`
  `Log.e("WindowInsetsCompat", sbA.toString(), e4);`
- `sources/androidx/core/view/WindowInsetsCompat.java:1017`
  `Log.e("WindowInsetsCompat", sbA.toString(), e4);`
- `sources/androidx/customview/widget/ViewDragHelper.java:457`
  `Log.e("ViewDragHelper", "Ignoring pointerId=" + i + " because ACTION_DOWN was not received for this pointer before ACTION_MOVE. It likely happened because  ViewDragHelper did not receive all the events in the event stream.");`
- `sources/androidx/fragment/app/a.java:161`
  `printWriter.println(Integer.toHexString(this.f2215e));`
- `sources/androidx/fragment/app/a.java:168`
  `printWriter.println(Integer.toHexString(this.f2217g));`

## BR052

paper_id: B013
paper_title: Availability and quality of mobile health app privacy policies

- `audit_reports/01_database_rule_audit.md:84`
  `### R054 / P014 / Unaddressed privacy risks in accredited health and wellness apps`
- `audit_reports/01_database_rule_audit.md:119`
  `### R068 / P017 / Mobile health and privacy: cross sectional study`
- `audit_reports/02_evidence_chains.md:11`
  `- R054 / P014 / Unaddressed privacy risks in accredited health and wellness apps / 'confirmed'`

## BR055

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `sources/androidx/core/util/PatternsCompat.java:25`
  `Pattern patternCompile3 = Pattern.compile("(?:(?:(?:[a-zA-Z0-9[ -\ud7ff豈-﷏ﷰ-\uffef𐀀-\u1fffd𠀀-\u2fffd𰀀-\u3fffd\u40000-\u4fffd\u50000-\u5fffd\u60000-\u6fffd\u70000-\u7fffd\u80000-\u8fffd\u90000-\u9fffd\ua0000-\uafffd\ub0000-\ubfffd\uc0000-\ucfffd\ud0000-\udfffd\ue1000-\uefffd&&[^ [\u2000-\u200a]\u2028...`

## BR061

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/lifecycle/LiveData.java:97`
  `LiveData.this.setValue(obj);`
- `sources/com/contec/spo2/code/a/f.java:180`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/f.java:268`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/g.java:140`
  `g.this.sendData(com.contec.spo2.code.a.a.h(1));`
- `sources/com/contec/spo2/code/a/g.java:287`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/g.java:486`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/g.java:501`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/g.java:514`
  `sendData(com.contec.spo2.code.a.a.a(1, 1, this.I, this.J, 0));`
- `sources/com/contec/spo2/code/a/g.java:580`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/g.java:684`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/g.java:793`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/g.java:808`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/g.java:904`
  `r3.sendData(r4)`
- `sources/com/contec/spo2/code/a/g.java:966`
  `sendData(com.contec.spo2.code.a.a.l());`
- `sources/com/contec/spo2/code/a/g.java:1099`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/g.java:1112`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/a/g.java:1187`
  `r4.sendData(r5)`
- `sources/com/contec/spo2/code/base/ContecDevice.java:435`
  `sendData(com.contec.spo2.code.a.a.a(1));`
- `sources/com/contec/spo2/code/base/ContecDevice.java:441`
  `sendData(com.contec.spo2.code.a.a.a(2));`
- `sources/com/contec/spo2/code/base/ContecDevice.java:447`
  `sendData(com.contec.spo2.code.a.a.a(3));`
- `sources/com/contec/spo2/code/base/ContecDevice.java:523`
  `public void sendData(byte[] bArr) {`
- `sources/com/yuwell/bluetooth/le/device/bpm/BPMManager.java:220`
  `bPMManager5.writeCharacteristic(bluetoothGattCharacteristic, bArr).done((SuccessCallback) new e1.a(this, i)).enqueue();`
- `sources/com/yuwell/bluetooth/le/device/bpm/BPMManager.java:381`
  `writeCharacteristic(this.f5755y, RecordAccessControlPointData.abortOperation()).enqueue();`
- `sources/com/yuwell/bluetooth/le/device/bpm/BPMManager.java:404`
  `writeCharacteristic(this.f5755y, RecordAccessControlPointData.deleteAllStoredRecords()).enqueue();`
- `sources/com/yuwell/bluetooth/le/device/bpm/BPMManager.java:429`
  `writeCharacteristic(bluetoothGattCharacteristic, new byte[]{1, b4, b5}).enqueue();`
- `sources/com/yuwell/bluetooth/le/device/bpm/BPMManager.java:463`
  `mutableData.setValue(1, 17, 0);`
- `sources/com/yuwell/bluetooth/le/device/bpm/BPMManager.java:464`
  `mutableData.setValue(i6, 17, 1);`
- `sources/com/yuwell/bluetooth/le/device/bpm/BPMManager.java:465`
  `mutableData.setValue(2, 17, 2);`
- `sources/com/yuwell/bluetooth/le/device/bpm/BPMManager.java:467`
  `mutableData.setValue(Integer.valueOf(iArr[i7]).intValue(), 17, i5);`
- `sources/com/yuwell/bluetooth/le/device/bpm/BPMManager.java:470`
  `writeCharacteristic(bluetoothGattCharacteristic, mutableData).done(new a1.c(this, i)).enqueue();`
- `sources/com/yuwell/bluetooth/le/device/gls/GlucoseManager.java:239`
  `glucoseManager3.writeCharacteristic(bluetoothGattCharacteristic, bArr).done((SuccessCallback) new e1.a(this, i4)).enqueue();`
- `sources/com/yuwell/bluetooth/le/device/gls/GlucoseManager.java:370`
  `mutableData.setValue(1, 17, 0);`
- `sources/com/yuwell/bluetooth/le/device/gls/GlucoseManager.java:371`
  `mutableData.setValue(i6, 17, 1);`
- `sources/com/yuwell/bluetooth/le/device/gls/GlucoseManager.java:372`
  `mutableData.setValue(2, 17, 2);`
- `sources/com/yuwell/bluetooth/le/device/gls/GlucoseManager.java:374`
  `mutableData.setValue(Integer.valueOf(iArr[i7]).intValue(), 17, i5);`
- `sources/com/yuwell/bluetooth/le/device/gls/GlucoseManager.java:377`
  `writeCharacteristic(bluetoothGattCharacteristic, mutableData).done(new c(this, i4)).enqueue();`
- `sources/com/yuwell/bluetooth/le/device/gls/GlucoseManager.java:383`
  `writeCharacteristic(bluetoothGattCharacteristic, new byte[]{0, 0, (byte) i}, bluetoothGattCharacteristic.getWriteType()).done(new SuccessCallback() { // from class: h1.d`
- `sources/com/yuwell/bluetooth/le/device/gls/GlucoseManager.java:408`
  `writeCharacteristic(bluetoothGattCharacteristic, new byte[]{0, 0, (byte) i}, bluetoothGattCharacteristic.getWriteType()).done(new SuccessCallback() { // from class: h1.c`
- `sources/com/yuwell/bluetooth/le/device/oxi/OximeterManager.java:83`
  `oximeterManager.writeCharacteristic(oximeterManager.f5782q, bArr).enqueue();`
- `sources/com/yuwell/healthmanager/view/impl/add/BgAdd.java:124`
  `this.dialview.setValue(f4);`

## BR062

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/com/contec/spo2/code/connect/a.java:270`
  `if (this.f4137f.setCharacteristicNotification(bluetoothGattCharacteristic, z3) && (descriptor = bluetoothGattCharacteristic.getDescriptor(UUID.fromString("00002902-0000-1000-8000-00805f9b34fb"))) != null) {`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:167`
  `public void onCharacteristicRead(android.bluetooth.BluetoothGatt r7, android.bluetooth.BluetoothGattCharacteristic r8, int r9) {`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:172`
  `throw new UnsupportedOperationException("Method not decompiled: no.nordicsemi.android.ble.BleManagerHandler.AnonymousClass3.onCharacteristicRead(android.bluetooth.BluetoothGatt, android.bluetooth.BluetoothGattCharacteristic, int):void");`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1804`
  `public void onCharacteristicRead(@NonNull BluetoothGatt bluetoothGatt, @NonNull BluetoothGattCharacteristic bluetoothGattCharacteristic) {`

## BR063

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/no/nordicsemi/android/ble/common/data/cgm/CGMSpecificOpsControlPointData.java:90`
  `MutableData mutableData = new MutableData(new byte[(z3 ? 2 : 0) + 11]);`
- `sources/no/nordicsemi/android/ble/common/data/hr/HeartRateControlPointData.java:9`
  `public static final byte[] f11806a = {1};`

## BR064

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/collection/LruCache.java:189`
  `throw new java.lang.IllegalStateException(getClass().getName() + ".sizeOf() is reporting inconsistent results!");`
- `sources/androidx/core/app/NotificationCompat.java:3426`
  `bundle.putCharSequence(NotificationCompat.EXTRA_SELF_DISPLAY_NAME, this.f1469f.getName());`
- `sources/androidx/core/app/NotificationCompat.java:3541`
  `return this.f1469f.getName();`
- `sources/androidx/core/app/NotificationCompat.java:3783`
  `if (!TextUtils.isEmpty(person.getName())) {`
- `sources/androidx/core/util/DebugUtils.java:15`
  `if (simpleName.length() <= 0 && (iLastIndexOf = (simpleName = obj.getClass().getName()).lastIndexOf(46)) > 0) {`
- `sources/androidx/versionedparcelable/VersionedParcel.java:55`
  `Class<?> cls = Class.forName(objectStreamClass.getName(), false, a.class.getClassLoader());`
- `sources/androidx/versionedparcelable/VersionedParcel.java:75`
  `Class cls2 = this.mParcelizerCache.get(cls.getName());`
- `sources/androidx/versionedparcelable/VersionedParcel.java:79`
  `Class<?> cls3 = Class.forName(String.format("%s.%sParcelizer", cls.getPackage().getName(), cls.getSimpleName()), false, cls.getClassLoader());`
- `sources/androidx/versionedparcelable/VersionedParcel.java:80`
  `this.mParcelizerCache.put(cls.getName(), cls3);`
- `sources/androidx/versionedparcelable/VersionedParcel.java:126`
  `Method method = this.mWriteCache.get(cls.getName());`
- `sources/androidx/versionedparcelable/VersionedParcel.java:133`
  `this.mWriteCache.put(cls.getName(), declaredMethod);`
- `sources/butterknife/ButterKnife.java:46`
  `String name = cls.getName();`
- `sources/com/contec/spo2/code/connect/ContecSdk.java:91`
  `if (bluetoothDevice.getName() == null || (bluetoothSearchCallback = ContecSdk.this.f4123d) == null) {`
- `sources/com/contec/spo2/code/connect/ContecSdk.java:174`
  `String name = bluetoothDevice.getName();`
- `sources/com/google/android/material/animation/MotionSpec.java:162`
  `return '\n' + getClass().getName() + '{' + Integer.toHexString(System.identityHashCode(this)) + " timings: " + this.f4467a + "}\n";`
- `sources/com/google/android/material/animation/MotionTiming.java:89`
  `return '\n' + getClass().getName() + '{' + Integer.toHexString(System.identityHashCode(this)) + " delay: " + getDelay() + " duration: " + getDuration() + " interpolator: " + getInterpolator().getClass() + " repeatCount: " + getRepeatCount() + " repeatMode: " + getRepeatMode() + "}\n";`
- `sources/com/yuwell/bluetooth/BluetoothService.java:489`
  `this.b = bluetoothDevice.getName();`
- `sources/com/yuwell/bluetooth/le/core/BleService.java:61`
  `String deviceName = next.getScanRecord() != null ? next.getScanRecord().getDeviceName() : next.getDevice().getName();`
- `sources/com/yuwell/bluetooth/le/core/BleService.java:62`
  `if (!TextUtils.isEmpty(deviceName)) {`
- `sources/com/yuwell/bluetooth/le/core/BleService.java:77`
  `sbA2.append(", mDeviceName=");`
- `sources/com/yuwell/bluetooth/le/core/BleService.java:78`
  `sbA2.append(deviceName);`
- `sources/com/yuwell/bluetooth/le/device/bpm/BPMManager.java:396`
  `return super.connectable(bluetoothDevice, i, scanRecord) && isSpecfiedDevice(bluetoothDevice.getName());`
- `sources/com/yuwell/bluetooth/le/device/fetus/FetusManager.java:135`
  `return super.connectable(bluetoothDevice, i, scanRecord) && isSpecfiedDevice(bluetoothDevice.getName());`
- `sources/com/yuwell/bluetooth/le/device/gls/GlucoseManager.java:331`
  `return super.connectable(bluetoothDevice, i, scanRecord) && isSpecfiedDevice(bluetoothDevice.getName());`
- `sources/com/yuwell/bluetooth/le/device/hts/ThermometerManager.java:180`
  `String name = bluetoothDevice.getName();`
- `sources/com/yuwell/bluetooth/le/device/oxi/OximeterManager.java:275`
  `String name = bluetoothDevice.getName();`
- `sources/com/yuwell/healthmanager/databinding/ActivityFetusMeasureBinding.java:67`
  `public final TextView tvDeviceName;`
- `sources/com/yuwell/healthmanager/databinding/ActivityFetusMeasureBinding.java:114`
  `this.tvDeviceName = textView3;`
- `sources/com/yuwell/healthmanager/view/impl/MainActivity.java:390`
  `String name = bluetoothDevice.getName();`
- `sources/com/yuwell/healthmanager/view/impl/MainActivity.java:423`
  `if (YuActivityManager.isTopActivity(YuActivityManager.getActivityByName(FetalMeasureActivity.class.getName())) || YuActivityManager.isTopActivity(YuActivityManager.getActivityByName(FhtResultActivity.class.getName())) || YuActivityManager.isTopActivity(YuActivityManager.getActivityByName(FhtImageAct...`
- `sources/com/yuwell/healthmanager/view/impl/home/BgHome.java:111`
  `if (bluetoothDevice2 == null || !GlucoseManager.isSpecfiedDevice(bluetoothDevice2.getName())) {`
- `sources/com/yuwell/healthmanager/view/impl/home/BgHome.java:119`
  `if (i == 2 && (bluetoothDevice = (BluetoothDevice) message.obj) != null && GlucoseManager.isSpecfiedDevice(bluetoothDevice.getName())) {`
- `sources/com/yuwell/healthmanager/view/impl/home/BgHome.java:120`
  `String strReplace = bluetoothDevice.getName().replace("BG", "").replace("-", "");`
- `sources/com/yuwell/healthmanager/view/impl/home/BoHome.java:97`
  `if (bluetoothDevice2 == null || !OximeterManager.isSpecfiedDevice(bluetoothDevice2.getName())) {`
- `sources/com/yuwell/healthmanager/view/impl/home/BoHome.java:109`
  `if (i == 2 && (bluetoothDevice = (BluetoothDevice) message.obj) != null && OximeterManager.isSpecfiedDevice(bluetoothDevice.getName())) {`
- `sources/com/yuwell/healthmanager/view/impl/home/BoHome.java:110`
  `String name = bluetoothDevice.getName();`
- `sources/com/yuwell/healthmanager/view/impl/home/BpHome.java:121`
  `if (i == 2 && (bluetoothDevice = (BluetoothDevice) message.obj) != null && BPMManager.isSpecfiedDevice(bluetoothDevice.getName())) {`
- `sources/com/yuwell/healthmanager/view/impl/home/BpHome.java:122`
  `String strReplace = bluetoothDevice.getName().replace("BP", "").replace("-", "");`
- `sources/com/yuwell/healthmanager/view/impl/home/BpHome.java:133`
  `if (bluetoothDevice2 == null || !BPMManager.isSpecfiedDevice(bluetoothDevice2.getName())) {`
- `sources/com/yuwell/healthmanager/view/impl/home/FetusHome.java:101`
  `if (bluetoothDevice2 == null || !FetusManager.isSpecfiedDevice(bluetoothDevice2.getName()) || (drawable = ContextCompat.getDrawable(requireContext(), R.drawable.ic_fetus_device_disconnected)) == null) {`
- `sources/com/yuwell/healthmanager/view/impl/home/FetusHome.java:108`
  `if (i == 2 && (bluetoothDevice = (BluetoothDevice) message.obj) != null && FetusManager.isSpecfiedDevice(bluetoothDevice.getName())) {`
- `sources/com/yuwell/healthmanager/view/impl/home/FetusHome.java:109`
  `String name = bluetoothDevice.getName();`
- `sources/com/yuwell/healthmanager/view/impl/home/HtsHome.java:140`
  `if ((i == 2 || i == 0) && (bluetoothDevice = (BluetoothDevice) message.obj) != null && ThermometerManager.isSpecfiedDevice(bluetoothDevice.getName())) {`
- `sources/com/yuwell/healthmanager/view/impl/home/HtsHome.java:141`
  `boolean zIsEarDevice = HtsUtil.isEarDevice(bluetoothDevice.getName());`
- `sources/com/yuwell/healthmanager/view/impl/home/HtsHome.java:148`
  `String name = bluetoothDevice.getName();`
- `sources/com/yuwell/healthmanager/view/impl/measure/BgMeasure.java:153`
  `if (obj == null || !GlucoseManager.isSpecfiedDevice(((BluetoothDevice) obj).getName()) || ((BluetoothDevice) message.obj) == null) {`
- `sources/com/yuwell/healthmanager/view/impl/measure/BoMeasure.java:128`
  `if (obj == null || !OximeterManager.isSpecfiedDevice(((BluetoothDevice) obj).getName()) || (menuItem = this.E) == null) {`
- `sources/com/yuwell/healthmanager/view/impl/measure/BpMeasure.java:34`
  `public TextView mDeviceName;`
- `sources/com/yuwell/healthmanager/view/impl/measure/BpMeasure.java:81`
  `possibleReasonAdapter.setData(DeviceUtil.getPossibleReason(this.mDeviceName.getText() == null ? "" : this.mDeviceName.getText().toString(), this));`
- `sources/com/yuwell/healthmanager/view/impl/measure/BpMeasure.java:100`
  `this.mDeviceName.setText(stringExtra.replace("BP", "").replace("-", ""));`
- `sources/com/yuwell/healthmanager/view/impl/measure/BpMeasure.java:109`
  `this.mDeviceName.setText((CharSequence) null);`
- `sources/com/yuwell/healthmanager/view/impl/measure/BpMeasure.java:128`
  `if (obj == null || !BPMManager.isSpecfiedDevice(((BluetoothDevice) obj).getName())) {`
- `sources/com/yuwell/healthmanager/view/impl/measure/BpMeasure.java:133`
  `String name = bluetoothDevice.getName();`
- `sources/com/yuwell/healthmanager/view/impl/measure/BpMeasure.java:135`
  `this.mDeviceName.setText(name.replace("BP", "").replace("-", ""));`
- `sources/com/yuwell/healthmanager/view/impl/measure/BpMeasure_ViewBinding.java:49`
  `bpMeasure.mDeviceName = null;`
- `sources/com/yuwell/healthmanager/view/impl/measure/BpMeasure_ViewBinding.java:59`
  `bpMeasure.mDeviceName = (TextView) Utils.findRequiredViewAsType(view, R.id.text_name, "field 'mDeviceName'", TextView.class);`
- `sources/com/yuwell/healthmanager/view/impl/measure/HtsEarMeasure.java:116`
  `if (obj == null || !ThermometerManager.isSpecfiedDevice(((BluetoothDevice) obj).getName()) || ((BluetoothDevice) message.obj) == null) {`
- `sources/com/yuwell/healthmanager/view/impl/measure/HtsMeasure.java:115`
  `if (obj == null || !ThermometerManager.isSpecfiedDevice(((BluetoothDevice) obj).getName()) || ((BluetoothDevice) message.obj) == null) {`
- `sources/com/yuwell/healthmanager/view/impl/measure/fetus/FetalMeasureActivity.java:340`
  `if (bluetoothDevice == null || !FetusManager.isSpecfiedDevice(bluetoothDevice.getName())) {`
- `sources/com/yuwell/healthmanager/vm/MainViewModel.java:86`
  `sbA.append(", mDeviceName=");`
- `sources/com/yuwell/healthmanager/vm/MainViewModel.java:87`
  `sbA.append(next.getScanRecord() != null ? next.getScanRecord().getDeviceName() : next.getDevice().getName());`
- `sources/com/yuwell/healthmanager/vm/MainViewModel.java:95`
  `String name = device.getName();`
- `sources/com/yuwell/healthmanager/vm/MainViewModel.java:224`
  `if (this.f6422g == null || TextUtils.isEmpty(str) || 2 != this.f6422g.getConnectionState() || (device = this.f6422g.getDevice()) == null || str.equals(device.getAddress())) {`
- `sources/j1/c.java:123`
  `this.f10545a.saveHTSData(d4, i, z3, HtsUtil.isEarDevice(bluetoothDevice.getName()));`
- `sources/j1/c.java:155`
  `messageObtain.obj = bluetoothDevice.getName();`
- `sources/no/nordicsemi/android/ble/BleManager.java:90`
  `if (bluetoothDevice2 == null || bluetoothDevice == null || !bluetoothDevice.getAddress().equals(bluetoothDevice2.getAddress())) {`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:253`
  `sbA.append(bluetoothGatt.getDevice().getAddress());`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:856`
  `if (BleManagerHandler.this.f11577c == null || bluetoothDevice == null || !bluetoothDevice.getAddress().equals(BleManagerHandler.this.f11577c.getAddress())) {`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:183`
  `sbA.append(bluetoothDevice.getAddress());`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:196`
  `sbA2.append(bluetoothDevice.getAddress());`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:202`
  `sbA3.append(bluetoothDevice.getAddress());`
- `sources/no/nordicsemi/android/support/v18/scanner/a.java:212`
  `if (scanFilter.getDeviceAddress() != null) {`
- `sources/no/nordicsemi/android/support/v18/scanner/a.java:213`
  `builder.setDeviceAddress(scanFilter.getDeviceAddress());`
- `sources/no/nordicsemi/android/support/v18/scanner/a.java:215`
  `if (scanFilter.getDeviceName() != null) {`
- `sources/no/nordicsemi/android/support/v18/scanner/a.java:216`
  `builder.setDeviceName(scanFilter.getDeviceName());`
- `sources/no/nordicsemi/android/support/v18/scanner/BluetoothLeScannerCompat.java:168`
  `String address = scanResult.getDevice().getAddress();`
- `sources/no/nordicsemi/android/support/v18/scanner/PendingIntentReceiver.java:51`
  `builder.setDeviceAddress(scanFilter.getDeviceAddress()).setDeviceName(scanFilter.getDeviceName()).setServiceUuid(scanFilter.getServiceUuid(), scanFilter.getServiceUuidMask()).setManufacturerData(scanFilter.getManufacturerId(), scanFilter.getManufacturerData(), scanFilter.getManufacturerDataMask());`
- `sources/no/nordicsemi/android/support/v18/scanner/ScanFilter.java:58`
  `builder.setDeviceName(parcel.readString());`
- `sources/no/nordicsemi/android/support/v18/scanner/ScanFilter.java:61`
  `builder.setDeviceAddress(parcel.readString());`
- `sources/no/nordicsemi/android/support/v18/scanner/ScanFilter.java:163`
  `public String getDeviceAddress() {`

## BR065

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/com/contec/spo2/code/connect/a.java:186`
  `public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i) {`
- `sources/no/nordicsemi/android/ble/BleManagerCallbacks.java:48`
  `void onServicesDiscovered(@NonNull BluetoothDevice bluetoothDevice, boolean z3);`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:672`
  `public final void onServicesDiscovered(@NonNull final BluetoothGatt bluetoothGatt, int i) {`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:712`
  `bleManagerCallbacks.onServicesDiscovered(bluetoothGatt2.getDevice(), z3);`

## BR066

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/com/contec/spo2/code/connect/a.java:270`
  `if (this.f4137f.setCharacteristicNotification(bluetoothGattCharacteristic, z3) && (descriptor = bluetoothGattCharacteristic.getDescriptor(UUID.fromString("00002902-0000-1000-8000-00805f9b34fb"))) != null) {`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:21`
  `public static final UUID BLOOD_GLUCOSE = UUID.fromString("00002A18-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:22`
  `public static final UUID GLUCOSE_MEASUREMENT_CONTEXT = UUID.fromString("00002A34-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:23`
  `public static final UUID GLUCOSE_MEASURE_TYPE = UUID.fromString("d618d001-6000-1000-8000-000000000000");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:39`
  `UUID uuidFromString = UUID.fromString("0000fff1-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:41`
  `WEIGHT_READ = UUID.fromString("0000fff4-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:42`
  `BODY_COMPOSITION_MEASUREMENT = UUID.fromString("00002A9C-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:43`
  `URINE_CONTEC_NOTIFY = UUID.fromString("0000ff02-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:44`
  `URINE_CONTEC_WRITE = UUID.fromString("0000ff01-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:45`
  `UART_RX_CHARACTERISTIC_UUID = UUID.fromString("6E400002-B5A3-F393-E0A9-E50E24DCCA9E");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:46`
  `UART_TX_CHARACTERISTIC_UUID = UUID.fromString("6E400003-B5A3-F393-E0A9-E50E24DCCA9E");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:48`
  `SP_TX = UUID.fromString("02feff01-6000-1000-8000-000000000000");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:49`
  `SP_RX = UUID.fromString("02feff02-6000-1000-8000-000000000000");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:50`
  `FFF2 = UUID.fromString("0000fff2-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:51`
  `MOX_READ = UUID.fromString("0000ffe2-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Characteristic.java:52`
  `SP_TX1 = UUID.fromString("d618d001-6000-1000-8000-000000000000");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:22`
  `public static final UUID BLOOD_GLUCOSE_MEASUREMMENT = UUID.fromString("00001808-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:23`
  `public static final UUID BLOOD_GLUCOSE_MEASUREMMENT_TYPE = UUID.fromString("d618d000-6000-1000-8000-000000000000");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:34`
  `CURRENT_TIME = UUID.fromString("00001805-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:35`
  `HEALTH_THERMOMETER = UUID.fromString("00001809-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:36`
  `UUID uuidFromString2 = UUID.fromString("0000fff0-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:38`
  `BODY_COMPOSITION = UUID.fromString("0000181B-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:39`
  `URINE_CONTEC = UUID.fromString("0000ff12-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:40`
  `UART_SERVICE_UUID = UUID.fromString("6E400001-B5A3-F393-E0A9-E50E24DCCA9E");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:42`
  `FE60 = UUID.fromString("0000fe60-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:43`
  `D618D = UUID.fromString("d618d000-6000-1000-8000-000000000000");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:44`
  `MOX = UUID.fromString("0000e0ff-3c17-d293-8e48-14fe2e4da212");`
- `sources/com/yuwell/bluetooth/le/constants/Service.java:45`
  `GLS_FE60 = UUID.fromString("02feff01-6000-1000-8000-000000000000");`
- `sources/com/yuwell/bluetooth/le/device/battery/BatteryManager.java:26`
  `public static final UUID f5745s = UUID.fromString("0000180F-0000-1000-8000-00805f9b34fb");`
- `sources/com/yuwell/bluetooth/le/device/battery/BatteryManager.java:29`
  `public static final UUID f5746t = UUID.fromString("00002A19-0000-1000-8000-00805f9b34fb");`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:36`
  `public static final UUID f11603j = UUID.fromString("00002901-0000-1000-8000-00805f9b34fb");`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:39`
  `public static final UUID f11604k = UUID.fromString("00002902-0000-1000-8000-00805f9b34fb");`
- `sources/no/nordicsemi/android/support/v18/scanner/a.java:211`
  `builder.setServiceUuid(scanFilter.getServiceUuid(), scanFilter.getServiceUuidMask()).setManufacturerData(scanFilter.getManufacturerId(), scanFilter.getManufacturerData(), scanFilter.getManufacturerDataMask());`
- `sources/no/nordicsemi/android/support/v18/scanner/PendingIntentReceiver.java:51`
  `builder.setDeviceAddress(scanFilter.getDeviceAddress()).setDeviceName(scanFilter.getDeviceName()).setServiceUuid(scanFilter.getServiceUuid(), scanFilter.getServiceUuidMask()).setManufacturerData(scanFilter.getManufacturerId(), scanFilter.getManufacturerData(), scanFilter.getManufacturerDataMask());`
- `sources/no/nordicsemi/android/support/v18/scanner/ScanFilter.java:65`
  `builder.setServiceUuid(parcelUuid);`
- `sources/no/nordicsemi/android/support/v18/scanner/ScanFilter.java:67`
  `builder.setServiceUuid(parcelUuid, (ParcelUuid) parcel.readParcelable(ParcelUuid.class.getClassLoader()));`
- `sources/no/nordicsemi/android/support/v18/scanner/ScanFilter.java:202`
  `public ParcelUuid getServiceUuid() {`
- `sources/no/nordicsemi/android/support/v18/scanner/ScanFilter.java:207`
  `public ParcelUuid getServiceUuidMask() {`
- `sources/no/nordicsemi/android/support/v18/scanner/ScanFilter.java:374`
  `public Builder setServiceUuid(@Nullable ParcelUuid parcelUuid) {`
- `sources/no/nordicsemi/android/support/v18/scanner/ScanFilter.java:380`
  `public Builder setServiceUuid(@Nullable ParcelUuid parcelUuid, @Nullable ParcelUuid parcelUuid2) {`

## BR067

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/com/github/mikephil/charting/charts/BarLineChartBase.java:896`
  `public void setPinchZoom(boolean z3) {`
- `sources/com/yuwell/bluetooth/le/core/YUBleManager.java:42`
  `public Request createBond() {`
- `sources/com/yuwell/bluetooth/le/core/YUBleManager.java:43`
  `return super.createBond();`
- `sources/no/nordicsemi/android/ble/BleManager.java:187`
  `public Request createBond() {`
- `sources/no/nordicsemi/android/ble/BleManager.java:188`
  `return createBondInsecure();`
- `sources/no/nordicsemi/android/ble/BleManager.java:193`
  `public Request createBondInsecure() {`
- `sources/no/nordicsemi/android/ble/BleManager.java:194`
  `return Request.createBond().n(this.f11572d);`
- `sources/no/nordicsemi/android/ble/BleManager.java:384`
  `public Request removeBond() {`
- `sources/no/nordicsemi/android/ble/BleManager.java:385`
  `return Request.removeBond().n(this.f11572d);`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1346`
  `this.f11579e.log(3, "device.createBond()");`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1347`
  `boolean zCreateBond = bluetoothDevice.createBond();`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1348`
  `if (!z3 || zCreateBond) {`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1349`
  `return zCreateBond;`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1351`
  `Request requestN = Request.createBond().n(this);`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1364`
  `J(Request.removeBond().n(this));`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1517`
  `Method method = bluetoothDevice.getClass().getMethod("removeBond", new Class[0]);`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1518`
  `this.f11579e.log(3, "device.removeBond() (hidden)");`
- `sources/no/nordicsemi/android/ble/Request.java:130`
  `public static SimpleRequest createBond() {`
- `sources/no/nordicsemi/android/ble/Request.java:310`
  `public static SimpleRequest removeBond() {`

## BR068

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/okhttp3/Challenge.java:13`
  `public final class Challenge {`
- `sources/okhttp3/Challenge.java:19`
  `public Challenge(String str, Map<String, String> map) {`
- `sources/okhttp3/Challenge.java:46`
  `if (obj instanceof Challenge) {`
- `sources/okhttp3/Challenge.java:47`
  `Challenge challenge = (Challenge) obj;`
- `sources/okhttp3/Challenge.java:48`
  `if (challenge.f12052a.equals(this.f12052a) && challenge.b.equals(this.b)) {`
- `sources/okhttp3/Response.java:94`
  `public List<Challenge> challenges() {`
- `sources/okhttp3/Response.java:105`
  `return HttpHeaders.parseChallenges(headers(), str);`
- `sources/okhttp3/internal/http/HttpHeaders.java:102`
  `public static java.util.List<okhttp3.Challenge> parseChallenges(okhttp3.Headers r20, java.lang.String r21) {`
- `sources/okhttp3/internal/http/HttpHeaders.java:107`
  `throw new UnsupportedOperationException("Method not decompiled: okhttp3.internal.http.HttpHeaders.parseChallenges(okhttp3.Headers, java.lang.String):java.util.List");`

## BR069

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/com/yuwell/bluetooth/BluetoothService.java:487`
  `public synchronized void connect(BluetoothDevice bluetoothDevice, boolean z3) {`
- `sources/com/yuwell/bluetooth/BluetoothService.java:500`
  `b bVar2 = new b(bluetoothDevice, z3);`
- `sources/e1/a.java:48`
  `public void onRequestFailed(BluetoothDevice bluetoothDevice, int i) {`
- `sources/j1/c.java:49`
  `public void onBatteryValueRead(@NonNull BluetoothDevice bluetoothDevice, int i) {`
- `sources/j1/c.java:53`
  `public void onBloodPressureMeasurementRead(@NonNull BluetoothDevice bluetoothDevice, @NonNull BPMData bPMData) {`
- `sources/j1/c.java:62`
  `public void onCholesterolMeasurementRead(@NonNull BluetoothDevice bluetoothDevice, @NonNull CholesterolData cholesterolData) {`
- `sources/j1/c.java:117`
  `public void onGlucoseMeasurementRead(@NonNull BluetoothDevice bluetoothDevice, @NonNull GlucoseData glucoseData) {`
- `sources/j1/c.java:122`
  `public void onHTValueReceived(@NonNull BluetoothDevice bluetoothDevice, double d4, int i, boolean z3) {`
- `sources/j1/c.java:123`
  `this.f10545a.saveHTSData(d4, i, z3, HtsUtil.isEarDevice(bluetoothDevice.getName()));`
- `sources/j1/c.java:178`
  `public void onOxygenDataRead(@NonNull BluetoothDevice bluetoothDevice, @NonNull BloodOxygenData bloodOxygenData) {`
- `sources/j1/c.java:183`
  `public void onPulseWaveRead(@NonNull BluetoothDevice bluetoothDevice, int i) {`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1051`
  `request.j(bluetoothDevice, -5);`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1057`
  `public void lambda$nextRequest$27(Request request, BluetoothDevice bluetoothDevice) {`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1059`
  `request.m(bluetoothDevice);`
- `sources/no/nordicsemi/android/ble/BleManagerHandler.java:1063`
  `awaitingRequest.j(bluetoothDevice, -3);`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:325`
  `public void onExecuteWrite(@NonNull BluetoothDevice bluetoothDevice, int i, boolean z3) {`
- `sources/no/nordicsemi/android/ble/BleServerManager.java:327`
  `BleManagerHandler bleManagerHandlerA = BleServerManager.a(BleServerManager.this, bluetoothDevice);`
- `sources/okio/HashingSink.java:88`
  `Mac mac = Mac.getInstance(str);`
- `sources/okio/HashingSink.java:89`
  `this.f12538c = mac;`
- `sources/okio/HashingSink.java:90`
  `mac.init(new SecretKeySpec(byteString.toByteArray(), str));`

## BR070

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/no/nordicsemi/android/ble/BleManager.java:488`
  `public boolean shouldAutoConnect() {`

## BR071

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:40`
  `android:allowBackup="true"`

## BR073

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/appcompat/graphics/drawable/a.java:322`
  `SparseArray<Drawable.ConstantState> sparseArray = this.f329f;`
- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:601`
  `this.f619e.saveHierarchyState(sparseArray);`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:353`
  `if (!"historical-record".equals(NewPullParser.getName())) {`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:354`
  `throw new XmlPullParserException("Share records file not well-formed.");`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:356`
  `list.add(new HistoricalRecord(NewPullParser.getAttributeValue(null, "activity"), Long.parseLong(NewPullParser.getAttributeValue(null, "time")), Float.parseFloat(NewPullParser.getAttributeValue(null, "weight"))));`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:196`
  `int i4 = Integer.parseInt(strArrSplit[0]);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:197`
  `int i5 = Integer.parseInt(strArrSplit[1]);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:198`
  `int i6 = Integer.parseInt(strArrSplit[2]);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:207`
  `float f7 = i8 + ((int) ((Integer.parseInt(strArrSplit[3]) / 1920.0f) * height));`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:632`
  `public static final SparseIntArray f1246a;`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:662`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_goneMarginBottom, 24);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:663`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_goneMarginStart, 25);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:664`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_goneMarginEnd, 26);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:665`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHorizontal_bias, 29);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:666`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintVertical_bias, 30);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:667`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintDimensionRatio, 44);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:668`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHorizontal_weight, 45);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:669`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintVertical_weight, 46);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:670`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHorizontal_chainStyle, 47);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:671`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintVertical_chainStyle, 48);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:672`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constrainedWidth, 27);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:673`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constrainedHeight, 28);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:674`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintWidth_default, 31);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:675`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHeight_default, 32);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:676`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintWidth_min, 33);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:677`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintWidth_max, 34);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:678`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintWidth_percent, 35);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:679`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHeight_min, 36);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:680`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHeight_max, 37);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:681`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintHeight_percent, 38);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:682`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintLeft_creator, 39);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:683`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintTop_creator, 40);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:684`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintRight_creator, 41);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:685`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintBottom_creator, 42);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:686`
  `sparseIntArray.append(R.styleable.ConstraintLayout_Layout_layout_constraintBaseline_creator, 43);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:1202`
  `this.f1229a = Float.parseFloat(strSubstring4);`
- `sources/androidx/core/content/res/FontResourcesParserCompat.java:123`
  `arrayList.add(Base64.decode(str, 0));`
- `sources/androidx/core/content/res/FontResourcesParserCompat.java:161`
  `while (xmlPullParser.next() != 3) {`
- `sources/androidx/core/content/res/FontResourcesParserCompat.java:162`
  `if (xmlPullParser.getEventType() == 2) {`
- `sources/androidx/core/content/res/FontResourcesParserCompat.java:163`
  `if (xmlPullParser.getName().equals("font")) {`
- `sources/androidx/core/content/res/FontResourcesParserCompat.java:164`
  `TypedArray typedArrayObtainAttributes2 = resources.obtainAttributes(Xml.asAttributeSet(xmlPullParser), R.styleable.FontFamilyFont);`
- `sources/androidx/core/graphics/TypefaceCompatApi26Impl.java:106`
  `for (FontResourcesParserCompat.FontFileResourceEntry fontFileResourceEntry : fontFamilyFilesResourceEntry.getEntries()) {`
- `sources/androidx/core/graphics/TypefaceCompatApi29Impl.java:40`
  `FontResourcesParserCompat.FontFileResourceEntry fontFileResourceEntry = entries[i4];`
- `sources/androidx/core/graphics/drawable/IconCompat.java:538`
  `bitmapDrawable = new BitmapDrawable(context.getResources(), BitmapFactory.decodeByteArray((byte[]) this.f1613a, this.mInt1, this.mInt2));`
- `sources/androidx/core/graphics/drawable/IconCompat.java:543`
  `bitmapDrawable = new BitmapDrawable(context.getResources(), BitmapFactory.decodeStream(uriInputStream));`
- `sources/androidx/core/net/ParseException.java:6`
  `public class ParseException extends RuntimeException {`
- `sources/androidx/core/net/ParseException.java:11`
  `public ParseException(@NonNull String str) {`
- `sources/androidx/core/provider/d.java:104`
  `List<List<byte[]>> certificates = fontRequest.getCertificates() != null ? fontRequest.getCertificates() : FontResourcesParserCompat.readCerts(resources, fontRequest.getCertificatesArrayResId());`
- `sources/androidx/lifecycle/SavedStateHandle.java:25`
  `public static final Class[] f2476e = {Boolean.TYPE, boolean[].class, Double.TYPE, double[].class, Integer.TYPE, int[].class, Long.TYPE, long[].class, String.class, String[].class, Binder.class, Bundle.class, Byte.TYPE, byte[].class, Character.TYPE, char[].class, CharSequence.class, CharSequence[].cl...`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:725`
  `ColorStateList namedColorStateList = TypedArrayUtils.getNamedColorStateList(typedArrayObtainAttributes, xmlPullParser, theme, "tint", 1);`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:729`
  `hVar2.f3306e = TypedArrayUtils.getNamedBoolean(typedArrayObtainAttributes, xmlPullParser, "autoMirrored", 5, hVar2.f3306e);`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:730`
  `gVar3.f3297k = TypedArrayUtils.getNamedFloat(typedArrayObtainAttributes, xmlPullParser, "viewportWidth", 7, gVar3.f3297k);`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:731`
  `float namedFloat = TypedArrayUtils.getNamedFloat(typedArrayObtainAttributes, xmlPullParser, "viewportHeight", 8, gVar3.f3298l);`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:734`
  `throw new XmlPullParserException(typedArrayObtainAttributes.getPositionDescription() + "<vector> tag requires viewportWidth > 0");`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:910`
  `throw new XmlPullParserException("no path defined");`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:912`
  `throw new XmlPullParserException(typedArrayObtainAttributes.getPositionDescription() + "<vector> tag requires height > 0");`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:914`
  `throw new XmlPullParserException(typedArrayObtainAttributes.getPositionDescription() + "<vector> tag requires viewportHeight > 0");`
- `sources/androidx/versionedparcelable/VersionedParcel.java:11`
  `import android.util.SparseBooleanArray;`
- `sources/androidx/versionedparcelable/VersionedParcel.java:714`
  `public void writeSparseBooleanArray(SparseBooleanArray sparseBooleanArray, int i) {`
- `sources/androidx/versionedparcelable/VersionedParcel.java:716`
  `if (sparseBooleanArray == null) {`
- `sources/cn/com/lasong/media/IMP3DecodeCallback.java:7`
  `public interface IMP3DecodeCallback {`
- `sources/cn/com/lasong/media/MP3Player.java:8`
  `public class MP3Player implements IMP3DecodeCallback {`
- `sources/cn/com/lasong/media/MP3Player.java:20`
  `@Override // cn.com.lasong.media.IMP3DecodeCallback`
- `sources/cn/com/lasong/media/MP3Player.java:31`
  `@Override // cn.com.lasong.media.IMP3DecodeCallback`
- `sources/com/airbnb/lottie/parser/LayerParser.java:11`
  `public class LayerParser {`
- `sources/com/airbnb/lottie/parser/LayerParser.java:12`
  `public static Layer parse(LottieComposition lottieComposition) {`
- `sources/com/alibaba/fastjson/JSON.java:263`
  `public static final Object parse(byte[] bArr, Feature... featureArr) {`
- `sources/com/alibaba/fastjson/JSON.java:265`
  `return parseObject(new String(bArr, "UTF-8"), featureArr);`
- `sources/com/alibaba/fastjson/JSON.java:353`
  `defaultJSONParser.handleResovleTask(arrayList);`
- `sources/com/alibaba/fastjson/JSON.java:355`
  `defaultJSONParser.close();`
- `sources/com/alibaba/fastjson/JSON.java:367`
  `public static <T> T parseObject(String str, Type type, ParserConfig parserConfig, Feature... featureArr) {`
- `sources/com/alibaba/fastjson/JSON.java:368`
  `return (T) parseObject(str, type, parserConfig, null, DEFAULT_PARSER_FEATURE, featureArr);`
- `sources/com/alibaba/fastjson/JSON.java:406`
  `public static final <T> T parseObject(String str, TypeReference<T> typeReference, Feature... featureArr) {`
- `sources/com/alibaba/fastjson/JSON.java:526`
  `T t3 = (T) defaultJSONParser.parseObject(type);`
- `sources/com/alibaba/fastjson/JSON.java:527`
  `defaultJSONParser.handleResovleTask(t3);`
- `sources/com/alibaba/fastjson/JSON.java:528`
  `defaultJSONParser.close();`
- `sources/com/alibaba/fastjson/JSON.java:532`
  `public static final <T> T parseObject(byte[] bArr, Type type, Feature... featureArr) {`
- `sources/com/alibaba/fastjson/JSON.java:534`
  `return (T) parseObject(new String(bArr, "UTF-8"), type, featureArr);`
- `sources/com/alibaba/fastjson/parser/JSONLexer.java:182`
  `throw new UnsupportedOperationException("Method not decompiled: com.alibaba.fastjson.parser.JSONLexer.d(char[], int):java.lang.String");`
- `sources/com/alibaba/fastjson/parser/JSONLexer.java:185`
  `public static final byte[] decodeFast(String str, int i, int i4) {`

## BR074

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/activity/ComponentActivity.java:59`
  `public class ComponentActivity extends androidx.core.app.ComponentActivity implements ContextAware, ViewModelStoreOwner, HasDefaultViewModelProviderFactory, SavedStateRegistryOwner, OnBackPressedDispatcherOwner, ActivityResultRegistryOwner, ActivityResultCaller {`
- `sources/androidx/activity/ComponentActivity.java:150`
  `public final /* synthetic */ ActivityResultContract.SynchronousResult b;`
- `sources/androidx/activity/ComponentActivity.java:152`
  `public a(int i, ActivityResultContract.SynchronousResult synchronousResult) {`
- `sources/androidx/activity/ComponentActivity.java:154`
  `this.b = synchronousResult;`
- `sources/androidx/activity/ComponentActivity.java:187`
  `ActivityResultContract.SynchronousResult<O> synchronousResult = activityResultContract.getSynchronousResult(componentActivity, i4);`
- `sources/androidx/activity/ComponentActivity.java:188`
  `if (synchronousResult != null) {`
- `sources/androidx/activity/ComponentActivity.java:189`
  `new Handler(Looper.getMainLooper()).post(new a(i, synchronousResult));`
- `sources/androidx/activity/ComponentActivity.java:241`
  `this.f69e = SavedStateRegistryController.create(this);`
- `sources/androidx/activity/ComponentActivity.java:325`
  `ViewTreeSavedStateRegistryOwner.set(getWindow().getDecorView(), this);`
- `sources/androidx/activity/result/ActivityResultRegistry.java:222`
  `public final void onSaveInstanceState(@NonNull Bundle bundle) {`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:12`
  `public static final class SynchronousResult<T> {`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:18`
  `public SynchronousResult(@SuppressLint({"UnknownNullness"}) T t3) {`
- `sources/androidx/activity/result/contract/ActivityResultContract.java:32`
  `public SynchronousResult<O> getSynchronousResult(@NonNull Context context, @SuppressLint({"UnknownNullness"}) I i) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:32`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(@NonNull Context context, @NonNull String str) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:57`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(@NonNull Context context, @NonNull String str) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:104`
  `public final ActivityResultContract.SynchronousResult<List<Uri>> getSynchronousResult(@NonNull Context context, @NonNull String str) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:126`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(@NonNull Context context, @NonNull String[] strArr) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:152`
  `public final ActivityResultContract.SynchronousResult<Uri> getSynchronousResult(@NonNull Context context, @Nullable Uri uri) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:182`
  `public final ActivityResultContract.SynchronousResult<List<Uri>> getSynchronousResult(@NonNull Context context, @NonNull String[] strArr) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:231`
  `public ActivityResultContract.SynchronousResult<Map<String, Boolean>> getSynchronousResult(@NonNull Context context, @Nullable String[] strArr) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:233`
  `return new ActivityResultContract.SynchronousResult<>(Collections.emptyMap());`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:245`
  `return new ActivityResultContract.SynchronousResult<>(arrayMap);`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:282`
  `public ActivityResultContract.SynchronousResult<Boolean> getSynchronousResult(@NonNull Context context, @Nullable String str) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:284`
  `return new ActivityResultContract.SynchronousResult<>(Boolean.FALSE);`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:287`
  `return new ActivityResultContract.SynchronousResult<>(Boolean.TRUE);`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:346`
  `public final ActivityResultContract.SynchronousResult<Boolean> getSynchronousResult(@NonNull Context context, @NonNull Uri uri) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:368`
  `public final ActivityResultContract.SynchronousResult<Bitmap> getSynchronousResult(@NonNull Context context, @Nullable Void r22) {`
- `sources/androidx/activity/result/contract/ActivityResultContracts.java:393`
  `public final ActivityResultContract.SynchronousResult<Bitmap> getSynchronousResult(@NonNull Context context, @NonNull Uri uri) {`
- `sources/androidx/appcompat/R.java:799`
  `public static final int view_tree_saved_state_registry_owner = 0x7f0902a8;`
- `sources/androidx/appcompat/R.java:1718`
  `public static final int[] SearchView = {android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.inputType, android.R.attr.imeOptions, com.yuwell.healthmanager.R.attr.closeIcon, com.yuwell.healthmanager.R.attr.commitIcon, com.yuwell.healthmanager.R.attr.defaultQueryHint, com.yuwell.healthma...`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:463`
  `intentFilter.addAction("android.os.action.POWER_SAVE_MODE_CHANGED");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:469`
  `return this.f216c.isPowerSaveMode() ? 2 : 1;`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:123`
  `canvas.save();`
- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:601`
  `this.f619e.saveHierarchyState(sparseArray);`
- `sources/androidx/appcompat/widget/ActivityChooserView.java:325`
  `synchronized (activityChooserModel.f659a) {`
- `sources/androidx/appcompat/widget/ActivityChooserView.java:386`
  `synchronized (activityChooserModel.f659a) {`
- `sources/androidx/appcompat/widget/AppCompatRatingBar.java:24`
  `public synchronized void onMeasure(int i, int i4) {`
- `sources/androidx/appcompat/widget/SwitchCompat.java:475`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/collection/LruCache.java:189`
  `throw new java.lang.IllegalStateException(getClass().getName() + ".sizeOf() is reporting inconsistent results!");`
- `sources/androidx/collection/LruCache.java:246`
  `java.lang.String r1 = ".sizeOf() is reporting inconsistent results!"`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:509`
  `int iSave = canvas.save();`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:514`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/core/content/pm/ShortcutManagerCompat.java:132`
  `public static ShortcutInfoCompatSaver<?> d(Context context) {`
- `sources/androidx/core/provider/FontsContractCompat.java:165`
  `public static Typeface getFontSync(Context context, FontRequest fontRequest, @Nullable ResourcesCompat.FontCallback fontCallback, @Nullable Handler handler, boolean z3, int i, int i4) {`
- `sources/androidx/core/widget/NestedScrollView.java:486`
  `int iSave = canvas.save();`
- `sources/androidx/core/widget/NestedScrollView.java:505`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/core/widget/NestedScrollView.java:510`
  `int iSave2 = canvas.save();`
- `sources/androidx/core/widget/NestedScrollView.java:528`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/drawerlayout/widget/DrawerLayout.java:571`
  `int iSave = canvas.save();`
- `sources/androidx/drawerlayout/widget/DrawerLayout.java:599`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/fragment/app/Fragment.java:80`
  `public class Fragment implements ComponentCallbacks, View.OnCreateContextMenuListener, LifecycleOwner, ViewModelStoreOwner, HasDefaultViewModelProviderFactory, SavedStateRegistryOwner, ActivityResultCaller {`
- `sources/androidx/fragment/app/FragmentActivity.java:232`
  `fragmentActivity.f2130n.noteStateNotSaved();`
- `sources/androidx/fragment/app/FragmentActivity.java:237`
  `fragmentActivity.f2130n.noteStateNotSaved();`
- `sources/androidx/fragment/app/FragmentManager.java:1354`
  `this.L.i = isStateSaved();`
- `sources/androidx/fragment/app/FragmentTabHost.java:65`
  `public static class b extends View.BaseSavedState {`
- `sources/androidx/loader/content/AsyncTaskLoader.java:74`
  `} else if (asyncTaskLoader.isAbandoned()) {`
- `sources/androidx/loader/content/AsyncTaskLoader.java:75`
  `asyncTaskLoader.onCanceled(d4);`
- `sources/androidx/loader/content/AsyncTaskLoader.java:77`
  `asyncTaskLoader.commitContentChanged();`
- `sources/androidx/loader/content/AsyncTaskLoader.java:78`
  `asyncTaskLoader.f2529n = SystemClock.uptimeMillis();`
- `sources/androidx/loader/content/AsyncTaskLoader.java:79`
  `asyncTaskLoader.f2526k = null;`
- `sources/androidx/loader/content/AsyncTaskLoader.java:80`
  `asyncTaskLoader.deliverResult(d4);`
- `sources/androidx/loader/content/ModernAsyncTask.java:23`
  `public abstract class ModernAsyncTask<Params, Progress, Result> {`
- `sources/androidx/loader/content/ModernAsyncTask.java:57`
  `StringBuilder sbA = androidx.activity.b.a("ModernAsyncTask #");`
- `sources/androidx/loader/content/ModernAsyncTask.java:79`
  `ModernAsyncTask.this.f2554e.set(true);`
- `sources/androidx/loader/content/ModernAsyncTask.java:83`
  `result = (Result) ModernAsyncTask.this.a(this.f2560a);`
- `sources/androidx/loader/content/ModernAsyncTask.java:100`
  `ModernAsyncTask modernAsyncTask = ModernAsyncTask.this;`
- `sources/androidx/loader/content/ModernAsyncTask.java:101`
  `if (modernAsyncTask.f2554e.get()) {`
- `sources/androidx/loader/content/ModernAsyncTask.java:104`
  `modernAsyncTask.d(result);`
- `sources/androidx/loader/content/ModernAsyncTask.java:106`
  `Log.w("AsyncTask", e4);`
- `sources/androidx/loader/content/ModernAsyncTask.java:108`
  `ModernAsyncTask modernAsyncTask2 = ModernAsyncTask.this;`
- `sources/androidx/loader/content/ModernAsyncTask.java:109`
  `if (modernAsyncTask2.f2554e.get()) {`
- `sources/androidx/loader/content/ModernAsyncTask.java:185`
  `modernAsyncTask.f2552c = Status.FINISHED;`
- `sources/androidx/loader/content/ModernAsyncTask.java:201`
  `public ModernAsyncTask() {`
- `sources/androidx/loader/content/ModernAsyncTask.java:217`
  `synchronized (ModernAsyncTask.class) {`
- `sources/androidx/navigation/ui/R.java:1171`
  `public static final int transition_layout_save = 0x7f090244;`
- `sources/androidx/navigation/ui/R.java:2079`
  `public static final int BottomSheetBehavior_Layout_behavior_saveFlags = 0x00000007;`
- `sources/androidx/navigation/ui/R.java:2592`
  `public static final int[] BottomSheetBehavior_Layout = {android.R.attr.elevation, com.yuwell.healthmanager.R.attr.backgroundTint, com.yuwell.healthmanager.R.attr.behavior_expandedOffset, com.yuwell.healthmanager.R.attr.behavior_fitToContents, com.yuwell.healthmanager.R.attr.behavior_halfExpandedRati...`
- `sources/androidx/recyclerview/widget/AsyncListDiffer.java:121`
  `AsyncListDiffer asyncListDiffer = AsyncListDiffer.this;`
- `sources/androidx/recyclerview/widget/AsyncListDiffer.java:122`
  `if (asyncListDiffer.f2670g == aVar.f2672c) {`
- `sources/androidx/recyclerview/widget/AsyncListDiffer.java:126`
  `List<T> list2 = asyncListDiffer.f2669f;`

## BR075

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/androidx/appcompat/R.java:1328`
  `public static final int AppCompatTextView_autoSizePresetSizes = 0x00000003;`
- `sources/androidx/appcompat/R.java:1697`
  `public static final int[] AppCompatTextView = {android.R.attr.textAppearance, com.yuwell.healthmanager.R.attr.autoSizeMaxTextSize, com.yuwell.healthmanager.R.attr.autoSizeMinTextSize, com.yuwell.healthmanager.R.attr.autoSizePresetSizes, com.yuwell.healthmanager.R.attr.autoSizeStepGranularity, com.yu...`
- `sources/androidx/appcompat/widget/AppCompatButton.java:203`
  `public void setAutoSizeTextTypeUniformWithPresetSizes(@NonNull int[] iArr, int i) throws IllegalArgumentException {`
- `sources/androidx/appcompat/widget/AppCompatButton.java:205`
  `super.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:277`
  `public void setAutoSizeTextTypeUniformWithPresetSizes(@NonNull int[] iArr, int i) throws IllegalArgumentException {`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:279`
  `super.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/constraintlayout/solver/ArrayRow.java:334`
  `public void reset() {`
- `sources/androidx/constraintlayout/solver/LinearSystem.java:137`
  `solverVariable.reset();`
- `sources/androidx/constraintlayout/solver/LinearSystem.java:454`
  `constraintAnchor.resetSolverVariable(this.f1101j);`
- `sources/androidx/constraintlayout/solver/LinearSystem.java:460`
  `solverVariable.reset();`
- `sources/androidx/constraintlayout/solver/LinearSystem.java:478`
  `arrayRow.reset();`
- `sources/androidx/constraintlayout/solver/LinearSystem.java:781`
  `public void reset() {`
- `sources/androidx/constraintlayout/solver/LinearSystem.java:792`
  `solverVariable.reset();`
- `sources/androidx/constraintlayout/solver/Metrics.java:39`
  `public void reset() {`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintAnchor.java:381`
  `public void reset() {`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintAnchor.java:388`
  `this.f1116a.reset();`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintAnchor.java:391`
  `public void resetSolverVariable(Cache cache) {`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintAnchor.java:396`
  `solverVariable.reset();`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:633`
  `constraintAnchor.reset();`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1231`
  `this.mAnchors.get(i).reset();`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1235`
  `public void resetResolutionNodes() {`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1237`
  `this.mListAnchors[i].getResolutionNode().reset();`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1241`
  `public void resetSolverVariables(Cache cache) {`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1242`
  `this.f1157s.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1243`
  `this.f1158t.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1244`
  `this.f1159u.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1245`
  `this.f1160v.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1246`
  `this.f1161w.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1247`
  `this.f1164z.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1248`
  `this.f1162x.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1249`
  `this.f1163y.resetSolverVariable(cache);`
- `sources/androidx/constraintlayout/solver/widgets/WidgetContainer.java:192`
  `public void reset() {`
- `sources/androidx/constraintlayout/solver/widgets/WidgetContainer.java:194`
  `super.reset();`
- `sources/androidx/constraintlayout/solver/widgets/WidgetContainer.java:198`
  `public void resetSolverVariables(Cache cache) {`
- `sources/androidx/constraintlayout/solver/widgets/WidgetContainer.java:199`
  `super.resetSolverVariables(cache);`
- `sources/androidx/constraintlayout/solver/widgets/WidgetContainer.java:202`
  `this.mChildren.get(i).resetSolverVariables(cache);`
- `sources/androidx/core/app/FrameMetricsAggregator.java:229`
  `public SparseIntArray[] reset() {`
- `sources/androidx/core/app/NotificationCompat.java:2576`
  `public int getCustomSizePreset() {`
- `sources/androidx/core/app/NotificationCompat.java:2683`
  `public WearableExtender setCustomSizePreset(int i) {`
- `sources/androidx/core/app/NotificationCompat.java:2816`
  `this.i = bundle.getInt("customSizePreset", 0);`
- `sources/androidx/core/provider/FontsContractCompat.java:191`
  `public static void resetCache() {`
- `sources/androidx/core/provider/FontsContractCompat.java:197`
  `public static void resetTypefaceCache() {`
- `sources/androidx/core/text/BidiFormatter.java:359`
  `if (getStereoReset() && z3) {`
- `sources/androidx/core/view/ActionProvider.java:70`
  `public void reset() {`
- `sources/androidx/core/widget/AutoSizeableTextView.java:30`
  `void setAutoSizeTextTypeUniformWithPresetSizes(@NonNull int[] iArr, int i) throws IllegalArgumentException;`
- `sources/androidx/core/widget/TextViewCompat.java:250`
  `public static void setAutoSizeTextTypeUniformWithPresetSizes(@NonNull TextView textView, @NonNull int[] iArr, int i) throws IllegalArgumentException {`
- `sources/androidx/core/widget/TextViewCompat.java:252`
  `textView.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/core/widget/TextViewCompat.java:254`
  `((AutoSizeableTextView) textView).setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/loader/app/LoaderManager.java:25`
  `void onLoaderReset(@NonNull Loader<D> loader);`
- `sources/androidx/loader/app/LoaderManagerImpl.java:190`
  `loader.reset();`
- `sources/androidx/loader/content/CursorLoader.java:160`
  `if (isReset()) {`
- `sources/androidx/navigation/ui/R.java:1907`
  `public static final int AppCompatTextView_autoSizePresetSizes = 0x00000003;`
- `sources/androidx/navigation/ui/R.java:2588`
  `public static final int[] AppCompatTextView = {android.R.attr.textAppearance, com.yuwell.healthmanager.R.attr.autoSizeMaxTextSize, com.yuwell.healthmanager.R.attr.autoSizeMinTextSize, com.yuwell.healthmanager.R.attr.autoSizePresetSizes, com.yuwell.healthmanager.R.attr.autoSizeStepGranularity, com.yu...`
- `sources/androidx/recyclerview/widget/AsyncListDiffer.java:89`
  `public Object getChangePayload(int i, int i4) {`
- `sources/androidx/recyclerview/widget/AsyncListDiffer.java:95`
  `return AsyncListDiffer.this.b.getDiffCallback().getChangePayload(obj, obj2);`
- `sources/androidx/recyclerview/widget/DiffUtil.java:26`
  `public Object getChangePayload(int i, int i4) {`
- `sources/androidx/recyclerview/widget/DiffUtil.java:331`
  `public Object getChangePayload(@NonNull T t3, @NonNull T t4) {`
- `sources/androidx/recyclerview/widget/RecyclerView.java:3426`
  `resetScroll();`
- `sources/androidx/recyclerview/widget/RecyclerView.java:4195`
  `resetFocusInfo();`
- `sources/androidx/recyclerview/widget/SortedList.java:69`
  `public Object getChangePayload(T2 t22, T2 t23) {`
- `sources/androidx/recyclerview/widget/SortedList.java:70`
  `return this.f2944a.getChangePayload(t22, t23);`
- `sources/androidx/recyclerview/widget/SortedList.java:108`
  `public Object getChangePayload(T2 t22, T2 t23) {`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:1443`
  `this.f3281j.reset();`
- `sources/cn/com/lasong/media/RWByteArray.java:53`
  `reset();`
- `sources/com/airbnb/lottie/LottieDrawable.java:359`
  `this.f3539a.reset();`
- `sources/com/airbnb/lottie/R.java:1160`
  `public static final int AppCompatTextView_autoSizePresetSizes = 0x00000003;`
- `sources/com/airbnb/lottie/R.java:1511`
  `public static final int[] AppCompatTextView = {android.R.attr.textAppearance, com.yuwell.healthmanager.R.attr.autoSizeMaxTextSize, com.yuwell.healthmanager.R.attr.autoSizeMinTextSize, com.yuwell.healthmanager.R.attr.autoSizePresetSizes, com.yuwell.healthmanager.R.attr.autoSizeStepGranularity, com.yu...`
- `sources/com/airbnb/lottie/animation/content/PolystarContent.java:183`
  `this.f3637a.reset();`
- `sources/com/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation.java:131`
  `this.f3692a.reset();`
- `sources/com/airbnb/lottie/animation/keyframe/TransformKeyframeAnimation.java:158`
  `this.f3692a.reset();`
- `sources/com/github/mikephil/charting/charts/BarLineChartBase.java:807`
  `public void resetZoom() {`
- `sources/com/github/mikephil/charting/charts/BarLineChartBase.java:808`
  `this.mViewPortHandler.resetZoom(this.mZoomMatrixBuffer);`
- `sources/com/github/mikephil/charting/components/Legend.java:410`
  `public void resetCustom() {`
- `sources/com/github/mikephil/charting/data/LineDataSet.java:175`
  `public void resetCircleColors() {`
- `sources/com/github/mikephil/charting/jobs/AnimatedViewPortJob.java:72`
  `public void resetAnimator() {`
- `sources/com/github/mikephil/charting/jobs/AnimatedZoomJob.java:52`
  `animatedZoomJob.resetAnimator();`
- `sources/com/github/mikephil/charting/renderer/LineChartRenderer.java:135`
  `this.cubicPath.reset();`
- `sources/com/github/mikephil/charting/renderer/LineChartRenderer.java:175`
  `this.cubicFillPath.reset();`
- `sources/com/github/mikephil/charting/renderer/LineChartRenderer.java:275`
  `this.cubicPath.reset();`
- `sources/com/github/mikephil/charting/renderer/LineChartRenderer.java:295`
  `this.cubicFillPath.reset();`

## BR076

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `resources/functions.properties:1`
  `# The default names (the English) for all function names in java`
- `resources/functions.properties:174`
  `names=NAMES`
- `resources/functions.properties:215`
  `request=REQUEST`
- `resources/functions_de.properties:1`
  `# The function names in German`
- `resources/functions_de.properties:175`
  `names=NAMEN`
- `resources/functions_de.properties:221`
  `request=ABFRAGEN`
- `resources/functions_en.properties:1`
  `# The default names (the English) for all function names in java`
- `resources/functions_en.properties:174`
  `names=NAMES`
- `resources/functions_en.properties:215`
  `request=REQUEST`
- `resources/functions_es.properties:1`
  `# The function names in Spanish`
- `resources/functions_es.properties:122`
  `get=PIVOT.FIELD	INDICAR.CAMPO.TABLA.DI`
- `resources/functions_es.properties:192`
  `names=NOMBRES`
- `resources/functions_es.properties:239`
  `request=SOLICITAR`
- `resources/functions_fr.properties:1`
  `# The function names in French`
- `resources/functions_fr.properties:176`
  `names=NOMS`
- `resources/functions_fr.properties:221`
  `request=REQUETE`
- `resources/functions_nl.properties:1`
  `# The default names in Dutch`
- `resources/functions_nl.properties:174`
  `names=NAMEN`
- `resources/functions_nl.properties:216`
  `request=VERZOEKEN`
- `resources/res/values/strings.xml:39`
  `<string name="apply_for_location_service_setting">This feature requires you to turn on location services. Please click OK to authorize</string>`
- `resources/res/values/strings.xml:49`
  `<string name="before_dinner">Before dinner</string>`
- `resources/res/values/strings.xml:50`
  `<string name="before_lunch">Before lunch</string>`
- `resources/res/values/strings.xml:51`
  `<string name="before_meal">Before meals</string>`
- `resources/res/values/strings.xml:52`
  `<string name="before_sleep">Before bedtime</string>`
- `resources/res/values/strings.xml:189`
  `<string name="hts_first_step_detail">1. Make sure the temperature probe is clean before use.\n\n2.Take off the cover. Point the temperature probe to the center of the forehead, with a distance of 0–3cm in between (make sure there is no cover between the temperature probe and the forehead). Then pres...`
- `resources/res/values/strings.xml:349`
  `<string name="share_tip_select_date">Please select a date first</string>`
- `resources/res/values/strings.xml:392`
  `<string name="string_arr_solution_1_0">Fasten cuff correctly before measurement.</string>`
- `resources/res/values/strings.xml:400`
  `<string name="string_arr_solution_2_1">Fasten cuff correctly before measurement.</string>`
- `sources/androidx/activity/ComponentActivity.java:246`
  `throw new IllegalStateException("getLifecycle() returned null in ComponentActivity's constructor. Please make sure you are lazily constructing your Lifecycle in the first call to getLifecycle() rather than relying on field initialization.");`
- `sources/androidx/activity/ComponentActivity.java:338`
  `throw new IllegalStateException("Your activity is not yet attached to the Application instance. You can't request ViewModel before onCreate call.");`
- `sources/androidx/activity/ComponentActivity.java:378`
  `throw new IllegalStateException("Your activity is not yet attached to the Application instance. You can't request ViewModel before onCreate call.");`
- `sources/androidx/activity/result/ActivityResultRegistry.java:69`
  `public void launch(I i, @Nullable ActivityOptionsCompat activityOptionsCompat) {`
- `sources/androidx/activity/result/ActivityResultRegistry.java:103`
  `public void launch(I i, @Nullable ActivityOptionsCompat activityOptionsCompat) {`
- `sources/androidx/activity/result/ActivityResultRegistry.java:162`
  `Log.w("ActivityResultRegistry", "Dropping pending result for request " + str + ": " + this.f102g.get(str));`
- `sources/androidx/activity/result/ActivityResultRegistry.java:166`
  `Log.w("ActivityResultRegistry", "Dropping pending result for request " + str + ": " + this.f103h.getParcelable(str));`
- `sources/androidx/activity/result/ActivityResultRegistry.java:234`
  `throw new IllegalStateException("LifecycleOwner " + lifecycleOwner + " is attempting to register while current state is " + lifecycle.getCurrentState() + ". LifecycleOwners must call register before they are STARTED.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:93`
  `import java.lang.reflect.Field;`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1034`
  `Field declaredField = Resources.class.getDeclaredField("mResourcesImpl");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1038`
  `Log.e("ResourcesFlusher", "Could not retrieve Resources#mResourcesImpl field", e5);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1042`
  `Field field = k.f18g;`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1043`
  `if (field != null) {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1045`
  `obj = field.get(resources);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1053`
  `Field declaredField2 = obj.getClass().getDeclaredField("mDrawableCache");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1057`
  `Log.e("ResourcesFlusher", "Could not retrieve ResourcesImpl#mDrawableCache field", e7);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1061`
  `Field field2 = k.f13a;`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1077`
  `Field declaredField3 = Resources.class.getDeclaredField("mDrawableCache");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1081`
  `Log.e("ResourcesFlusher", "Could not retrieve Resources#mDrawableCache field", e9);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1085`
  `Field field3 = k.f13a;`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1099`
  `Field declaredField4 = Resources.class.getDeclaredField("mDrawableCache");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1103`
  `Log.e("ResourcesFlusher", "Could not retrieve Resources#mDrawableCache field", e11);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1107`
  `Field field4 = k.f13a;`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1886`
  `throw new IllegalStateException("This Activity already has an action bar supplied by the window decor. Do not request Window.FEATURE_SUPPORT_ACTION_BAR and set windowActionBar to false in your theme to use a Toolbar instead.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2102`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2108`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR_OVERLAY id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2119`
  `throw new AndroidRuntimeException("Window feature must be requested before adding content");`
- `sources/androidx/appcompat/widget/SearchView.java:937`
  `Log.e("SearchView", "Failed launch activity: " + intentC, e5);`
- `sources/androidx/appcompat/widget/SearchView.java:1152`
  `/* JADX WARN: Type inference fix 'apply assigned field type' failed`
- `sources/androidx/core/view/WindowInsetsCompat.java:22`
  `import java.lang.reflect.Field;`
- `sources/androidx/core/view/WindowInsetsCompat.java:70`
  `throw new IllegalArgumentException(androidx.fragment.app.l.b("type needs to be >= FIRST and <= LAST, type=", i));`
- `sources/androidx/core/view/WindowInsetsCompat.java:114`
  `public static Field f1832a;`
- `sources/androidx/core/view/WindowInsetsCompat.java:115`
  `public static Field b;`
- `sources/androidx/core/view/WindowInsetsCompat.java:118`
  `public static Field f1833c;`
- `sources/androidx/core/view/WindowInsetsCompat.java:125`
  `Field declaredField = View.class.getDeclaredField("mAttachInfo");`
- `sources/androidx/core/view/WindowInsetsCompat.java:129`
  `Field declaredField2 = cls.getDeclaredField("mStableInsets");`
- `sources/androidx/core/view/WindowInsetsCompat.java:132`
  `Field declaredField3 = cls.getDeclaredField("mContentInsets");`
- `sources/androidx/core/view/WindowInsetsCompat.java:701`
  `public static Field f1835e = null;`
- `sources/androidx/core/view/WindowInsetsCompat.java:728`
  `Log.i("WindowInsetsCompat", "Could not retrieve WindowInsets.CONSUMED field", e4);`
- `sources/androidx/core/view/WindowInsetsCompat.java:732`
  `Field field = f1835e;`
- `sources/androidx/core/view/WindowInsetsCompat.java:733`
  `if (field != null) {`
- `sources/androidx/core/view/WindowInsetsCompat.java:735`
  `WindowInsets windowInsets = (WindowInsets) field.get(null);`
- `sources/androidx/core/view/WindowInsetsCompat.java:740`
  `Log.i("WindowInsetsCompat", "Could not get value from WindowInsets.CONSUMED field", e5);`
- `sources/androidx/core/view/WindowInsetsCompat.java:930`
  `public static Field f1846l;`
- `sources/androidx/core/view/WindowInsetsCompat.java:933`
  `public static Field f1847m;`
- `sources/androidx/customview/widget/ViewDragHelper.java:457`
  `Log.e("ViewDragHelper", "Ignoring pointerId=" + i + " because ACTION_DOWN was not received for this pointer before ACTION_MOVE. It likely happened because  ViewDragHelper did not receive all the events in the event stream.");`
- `sources/androidx/customview/widget/ViewDragHelper.java:499`
  `/* JADX WARN: Type inference fix 'apply assigned field type' failed`
- `sources/androidx/fragment/app/Fragment.java:331`
  `public void launch(I i, @Nullable ActivityOptionsCompat activityOptionsCompat) {`
- `sources/androidx/fragment/app/Fragment.java:334`
  `throw new IllegalStateException("Operation cannot be started before fragment is in created state");`
- `sources/androidx/fragment/app/Fragment.java:336`
  `activityResultLauncher.launch(i, activityOptionsCompat);`
- `sources/androidx/fragment/app/Fragment.java:475`
  `throw new IllegalStateException(l.d("Fragment ", this, " is attempting to registerForActivityResult after being created. Fragments must call registerForActivityResult() before they are created (i.e. initialization, onAttach(), or onCreate())."));`
- `sources/androidx/fragment/app/Fragment.java:1001`
  `throw new IllegalStateException("Can't access the Fragment View's LifecycleOwner when getView() is null i.e., before onCreateView() or after onDestroyView()");`

## BR077

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `sources/okhttp3/OkHttpClient.java:771`
  `SSLSocketFactory sSLSocketFactory = builder.f12165m;`
- `sources/okhttp3/OkHttpClient.java:772`
  `if (sSLSocketFactory == null && z3) {`
- `sources/okhttp3/OkHttpClient.java:775`
  `SSLContext sSLContext = Platform.get().getSSLContext();`
- `sources/okhttp3/OkHttpClient.java:776`
  `sSLContext.init(null, new TrustManager[]{x509TrustManagerPlatformTrustManager}, null);`
- `sources/okhttp3/OkHttpClient.java:777`
  `this.f12141m = sSLContext.getSocketFactory();`

## BR078

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/j3/a.java:22`
  `import okhttp3.Protocol;`
- `sources/j3/a.java:23`
  `import okhttp3.internal.Util;`
- `sources/j3/a.java:24`
  `import okhttp3.internal.platform.Platform;`
- `sources/j3/a.java:25`
  `import okhttp3.internal.tls.CertificateChainCleaner;`
- `sources/j3/a.java:26`
  `import okhttp3.internal.tls.TrustRootIndex;`
- `sources/j3/a.java:176`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/j3/a.java:186`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/j3/a.java:197`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/j3/a.java:361`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/j3/b.java:11`
  `import okhttp3.Protocol;`
- `sources/j3/b.java:12`
  `import okhttp3.internal.Util;`
- `sources/j3/b.java:13`
  `import okhttp3.internal.platform.Platform;`
- `sources/j3/b.java:58`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/OkHttpClient.java:19`
  `import javax.net.ssl.HostnameVerifier;`
- `sources/okhttp3/OkHttpClient.java:25`
  `import okhttp3.Call;`
- `sources/okhttp3/OkHttpClient.java:26`
  `import okhttp3.ConnectionSpec;`
- `sources/okhttp3/OkHttpClient.java:27`
  `import okhttp3.EventListener;`
- `sources/okhttp3/OkHttpClient.java:28`
  `import okhttp3.Headers;`
- `sources/okhttp3/OkHttpClient.java:29`
  `import okhttp3.Response;`
- `sources/okhttp3/OkHttpClient.java:30`
  `import okhttp3.WebSocket;`
- `sources/okhttp3/OkHttpClient.java:468`
  `public Builder(OkHttpClient okHttpClient) {`
- `sources/okhttp3/OkHttpClient.java:535`
  `@Override // okhttp3.internal.Internal`
- `sources/okhttp3/OkHttpClient.java:546`
  `@Override // okhttp3.internal.Internal`
- `sources/okhttp3/internal/Util.java:33`
  `import okhttp3.Headers;`
- `sources/okhttp3/internal/Util.java:34`
  `import okhttp3.HttpUrl;`
- `sources/okhttp3/internal/Util.java:35`
  `import okhttp3.MediaType;`
- `sources/okhttp3/internal/Util.java:36`
  `import okhttp3.RequestBody;`
- `sources/okhttp3/internal/Util.java:37`
  `import okhttp3.ResponseBody;`
- `sources/okhttp3/internal/Util.java:38`
  `import okhttp3.internal.http2.Header;`
- `sources/okhttp3/internal/connection/RealConnection.java:278`
  `if (this.f12300g == null || route == null || route.proxy().type() != Proxy.Type.DIRECT || this.b.proxy().type() != Proxy.Type.DIRECT || !this.b.socketAddress().equals(route.socketAddress()) || route.address().hostnameVerifier() != OkHostnameVerifier.INSTANCE || !supportsUrl(address.url())) {`
- `sources/okhttp3/internal/connection/RealConnection.java:368`
  `return this.f12298e != null && OkHostnameVerifier.INSTANCE.verify(httpUrl.host(), (X509Certificate) this.f12298e.peerCertificates().get(0));`
- `sources/okhttp3/internal/http2/PushObserver.java:12`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:18`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:23`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:28`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:11`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:32`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:71`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Platform.java:21`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/Platform.java:22`
  `import okhttp3.internal.tls.BasicCertificateChainCleaner;`
- `sources/okhttp3/internal/platform/Platform.java:23`
  `import okhttp3.internal.tls.BasicTrustRootIndex;`
- `sources/okhttp3/internal/platform/Platform.java:24`
  `import okhttp3.internal.tls.CertificateChainCleaner;`
- `sources/okhttp3/internal/platform/Platform.java:25`
  `import okhttp3.internal.tls.TrustRootIndex;`
- `sources/okhttp3/internal/tls/BasicCertificateChainCleaner.java:34`
  `@Override // okhttp3.internal.tls.CertificateChainCleaner`
- `sources/okhttp3/internal/tls/BasicTrustRootIndex.java:35`
  `@Override // okhttp3.internal.tls.TrustRootIndex`
- `sources/okhttp3/internal/tls/CertificateChainCleaner.java:1`
  `package okhttp3.internal.tls;`
- `sources/okhttp3/internal/tls/CertificateChainCleaner.java:8`
  `import okhttp3.internal.platform.Platform;`
- `sources/okhttp3/internal/ws/RealWebSocket.java:307`
  `@Override // okhttp3.WebSocket`
- `sources/retrofit2/h.java:361`
  `okhttp3.Call call = this.f13013f;`

## BR079

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/com/yuwell/healthmanager/view/impl/statistics/BgStatistic.java:218`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/yuwell/healthmanager/view/impl/statistics/BoStatistic.java:172`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/yuwell/healthmanager/view/impl/statistics/BpStatistic.java:209`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/yuwell/healthmanager/view/impl/statistics/HtsStatistic.java:193`
  `settings.setJavaScriptEnabled(true);`

## BR080

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/androidx/core/view/ViewCompat.java:642`
  `Log.d("ViewCompat", "Error calling dispatchFinishTemporaryDetach", e4);`
- `sources/androidx/core/view/ViewCompat.java:678`
  `Log.d("ViewCompat", "Error calling dispatchStartTemporaryDetach", e4);`
- `sources/androidx/fragment/app/s.java:106`
  `Log.v("FragmentManager", "Fragment " + fragmentFindFragmentById + " has been inflated via the <fragment> tag: id=0x" + Integer.toHexString(resourceId));`
- `sources/androidx/fragment/app/s.java:120`
  `Log.v("FragmentManager", "Retained Fragment " + fragmentFindFragmentById + " has been re-attached via the <fragment> tag: id=0x" + Integer.toHexString(resourceId));`
- `sources/cn/com/lasong/media/record/audio/AudioRecorder.java:134`
  `MediaLog.d(list.size() + ",\n " + audioRecordingConfiguration.isClientSilenced() + ",\n " + audioRecordingConfiguration.getAudioSource() + ",\n " + audioRecordingConfiguration.getClientAudioSource() + ",\n " + audioRecordingConfiguration.getClientAudioSessionId() + ",\n " + audioRecordingConfigurati...`
- `sources/com/yuwell/bluetooth/BluetoothService.java:98`
  `Log.d("BluetoothService", sbA.toString());`
- `sources/com/yuwell/bluetooth/BluetoothService.java:129`
  `android.util.Log.d(r0, r1)`
- `sources/com/yuwell/bluetooth/BluetoothService.java:303`
  `Log.d("BluetoothService", "create ConnectedThread: " + str);`
- `sources/com/yuwell/bluetooth/BluetoothService.java:362`
  `Log.d("BluetoothService", "setState() " + this.f5700g + " -> " + i);`
- `sources/com/yuwell/bluetooth/BluetoothService.java:382`
  `Log.d("BluetoothService", "connected, Socket Type:" + str);`
- `sources/com/yuwell/bluetooth/BluetoothService.java:423`
  `Log.d("BluetoothService", "start");`
- `sources/com/yuwell/bluetooth/BluetoothService.java:448`
  `Log.d("BluetoothService", "stop");`
- `sources/com/yuwell/bluetooth/BluetoothService.java:490`
  `Log.d("BluetoothService", "connect to: " + bluetoothDevice);`
- `sources/com/yuwell/bluetooth/le/core/BleScanner.java:105`
  `Log.d("BleScanner", "stopScanInternal: " + e4);`
- `sources/com/yuwell/bluetooth/le/device/bpm/BPMManager.java:157`
  `Log.d("BPMManager", "onNumberOfRecordsReceived: " + i);`
- `sources/com/yuwell/bluetooth/le/device/bpm/BPMManager.java:162`
  `Log.d("BPMManager", "onRecordAccessOperationCompleted: " + i);`
- `sources/com/yuwell/bluetooth/le/device/bpm/BPMManager.java:170`
  `Log.d("BPMManager", "onRecordAccessOperationCompletedWithNoRecordsFound: " + i);`
- `sources/com/yuwell/bluetooth/le/device/bpm/BPMManager.java:175`
  `Log.d("BPMManager", "onRecordAccessOperationError:" + i + ", error:" + i4);`
- `sources/com/yuwell/bluetooth/le/device/bpm/BPMManager.java:337`
  `Log.d(toString(), "onDeviceDisconnected");`
- `sources/com/yuwell/bluetooth/le/device/oxi/OximeterManager.java:139`
  `Log.d(OximeterManager.TAG, "onFail");`
- `sources/com/yuwell/bluetooth/le/device/oxi/OximeterManager.java:149`
  `Log.d(OximeterManager.TAG, "onRealtimeSpo2End");`
- `sources/com/yuwell/healthmanager/vm/MainViewModel.java:90`
  `Log.d("MainViewModel", sbA.toString());`

## BR082

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/androidx/core/content/FileProvider.java:56`
  `@Override // androidx.core.content.FileProvider.a`
- `sources/androidx/core/content/FileProvider.java:78`
  `@Override // androidx.core.content.FileProvider.a`
- `sources/com/yuwell/androidbase/tool/FileManager.java:10`
  `import androidx.core.content.FileProvider;`
- `sources/com/yuwell/androidbase/tool/FileManager.java:363`
  `return FileProvider.getUriForFile(context, context.getPackageName() + "." + str, file);`
- `sources/com/yuwell/healthmanager/utils/ShareUtil.java:8`
  `import androidx.core.content.FileProvider;`
- `sources/com/yuwell/healthmanager/utils/ShareUtil.java:17`
  `return FileProvider.getUriForFile(context, context.getPackageName().concat(".fileprovider"), file);`
- `sources/com/yuwell/healthmanager/view/impl/data/Data.java:17`
  `import androidx.core.content.FileProvider;`
- `sources/com/yuwell/healthmanager/view/impl/data/Data.java:86`
  `Uri uriForFile = FileProvider.getUriForFile(Data.this, Data.this.getPackageName() + ".fileprovider", new File(this.f6052a));`
- `sources/com/yuwell/healthmanager/view/impl/share/BpShareActivity.java:19`
  `import androidx.core.content.FileProvider;`
- `sources/com/yuwell/healthmanager/view/impl/share/BpShareActivity.java:179`
  `Uri uriForFile = FileProvider.getUriForFile(this, getPackageName() + ".fileprovider", new File(str));`

## BR086

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/androidx/appcompat/R.java:70`
  `public static final int actionModeShareDrawable = 0x7f040032;`
- `sources/androidx/appcompat/R.java:546`
  `public static final int abc_ab_share_pack_mtrl_alpha = 0x7f080006;`
- `sources/androidx/appcompat/R.java:554`
  `public static final int abc_btn_default_mtrl_shape = 0x7f08000e;`
- `sources/androidx/appcompat/R.java:1371`
  `public static final int AppCompatTheme_actionModeShareDrawable = 0x0000001b;`
- `sources/androidx/appcompat/R.java:1482`
  `public static final int DrawerArrowToggle_arrowShaftLength = 0x00000001;`
- `sources/androidx/appcompat/R.java:1698`
  `public static final int[] AppCompatTheme = {android.R.attr.windowIsFloating, android.R.attr.windowAnimationStyle, com.yuwell.healthmanager.R.attr.actionBarDivider, com.yuwell.healthmanager.R.attr.actionBarItemBackground, com.yuwell.healthmanager.R.attr.actionBarPopupTheme, com.yuwell.healthmanager.R...`
- `sources/androidx/appcompat/R.java:1702`
  `public static final int[] DrawerArrowToggle = {com.yuwell.healthmanager.R.attr.arrowHeadLength, com.yuwell.healthmanager.R.attr.arrowShaftLength, com.yuwell.healthmanager.R.attr.barLength, com.yuwell.healthmanager.R.attr.color, com.yuwell.healthmanager.R.attr.drawableSize, com.yuwell.healthmanager.R...`
- `sources/androidx/appcompat/R.java:1723`
  `public static final int[] TextAppearance = {android.R.attr.textSize, android.R.attr.typeface, android.R.attr.textStyle, android.R.attr.textColor, android.R.attr.textColorHint, android.R.attr.textColorLink, android.R.attr.shadowColor, android.R.attr.shadowDx, android.R.attr.shadowDy, android.R.attr.s...`
- `sources/androidx/appcompat/app/AppCompatDelegate.java:147`
  `public abstract boolean isHandleNativeActionModesEnabled();`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1362`
  `public boolean isHandleNativeActionModesEnabled() {`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:86`
  `this.f304d = typedArrayObtainStyledAttributes.getDimension(R.styleable.DrawerArrowToggle_arrowShaftLength, CircleImageView.X_OFFSET);`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:9`
  `import android.graphics.Shader;`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:39`
  `public final int[] f707a = {R.drawable.abc_textfield_search_default_mtrl_alpha, R.drawable.abc_textfield_default_mtrl_alpha, R.drawable.abc_ab_share_pack_mtrl_alpha};`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:40`
  `public final int[] b = {R.drawable.abc_ic_commit_search_api_mtrl_alpha, R.drawable.abc_seekbar_tick_mark_material, R.drawable.abc_ic_menu_share_mtrl_alpha, R.drawable.abc_ic_menu_copy_mtrl_am_alpha, R.drawable.abc_ic_menu_cut_mtrl_alpha, R.drawable.abc_ic_menu_selectall_mtrl_alpha, R.drawable.abc_ic...`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:86`
  `bitmapDrawable2.setTileModeX(Shader.TileMode.REPEAT);`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:139`
  `if (i == R.drawable.abc_btn_default_mtrl_shape) {`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:112`
  `this.f898f.getTheme().resolveAttribute(R.attr.actionModeShareDrawable, typedValue, true);`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:115`
  `activityChooserView.setDefaultActionButtonContentDescription(R.string.abc_shareactionprovider_share_with_application);`
- `sources/androidx/appcompat/widget/ShareActionProvider.java:116`
  `activityChooserView.setExpandActivityOverflowButtonContentDescription(R.string.abc_shareactionprovider_share_with);`
- `sources/androidx/core/app/ActivityCompat.java:26`
  `import androidx.core.app.SharedElementCallback;`
- `sources/androidx/core/app/ActivityCompat.java:101`
  `public static class c extends android.app.SharedElementCallback {`
- `sources/androidx/core/app/ActivityCompat.java:116`
  `public void onSharedElementsReady() {`
- `sources/androidx/core/app/ActivityCompat.java:117`
  `this.f1343a.onSharedElementsReady();`
- `sources/androidx/core/app/ActivityCompat.java:121`
  `public c(SharedElementCallback sharedElementCallback) {`
- `sources/androidx/core/app/ActivityCompat.java:122`
  `this.f1342a = sharedElementCallback;`
- `sources/androidx/core/app/ActivityCompat.java:125`
  `@Override // android.app.SharedElementCallback`
- `sources/androidx/core/app/ActivityCompat.java:126`
  `public Parcelable onCaptureSharedElementSnapshot(View view, Matrix matrix, RectF rectF) {`
- `sources/androidx/core/app/ActivityCompat.java:127`
  `return this.f1342a.onCaptureSharedElementSnapshot(view, matrix, rectF);`
- `sources/androidx/core/app/ActivityCompat.java:130`
  `@Override // android.app.SharedElementCallback`
- `sources/androidx/core/app/ActivityCompat.java:135`
  `@Override // android.app.SharedElementCallback`
- `sources/androidx/core/app/ActivityCompat.java:136`
  `public void onMapSharedElements(List<String> list, Map<String, View> map) {`
- `sources/androidx/core/app/ActivityCompat.java:137`
  `this.f1342a.onMapSharedElements(list, map);`
- `sources/androidx/core/app/ActivityCompat.java:140`
  `@Override // android.app.SharedElementCallback`
- `sources/androidx/core/app/ActivityCompat.java:141`
  `public void onRejectSharedElements(List<View> list) {`
- `sources/androidx/core/app/ActivityCompat.java:142`
  `this.f1342a.onRejectSharedElements(list);`
- `sources/androidx/core/app/ActivityCompat.java:166`
  `public static void finishAfterTransition(@NonNull Activity activity) {`
- `sources/androidx/core/app/ActivityCompat.java:167`
  `activity.finishAfterTransition();`
- `sources/androidx/core/app/ActivityCompat.java:253`
  `public static void setEnterSharedElementCallback(@NonNull Activity activity, @Nullable SharedElementCallback sharedElementCallback) {`
- `sources/androidx/core/app/ActivityCompat.java:254`
  `activity.setEnterSharedElementCallback(sharedElementCallback != null ? new c(sharedElementCallback) : null);`
- `sources/androidx/core/app/ActivityCompat.java:257`
  `public static void setExitSharedElementCallback(@NonNull Activity activity, @Nullable SharedElementCallback sharedElementCallback) {`
- `sources/androidx/core/app/ActivityCompat.java:258`
  `activity.setExitSharedElementCallback(sharedElementCallback != null ? new c(sharedElementCallback) : null);`
- `sources/androidx/core/app/ShareCompat.java:18`
  `import android.widget.ShareActionProvider;`
- `sources/androidx/core/app/ShareCompat.java:30`
  `public final class ShareCompat {`
- `sources/androidx/core/app/ShareCompat.java:70`
  `action.putExtra(ShareCompat.EXTRA_CALLING_PACKAGE, context.getPackageName());`
- `sources/androidx/core/app/ShareCompat.java:71`
  `action.putExtra(ShareCompat.EXTRA_CALLING_PACKAGE_INTEROP, context.getPackageName());`
- `sources/androidx/core/app/ShareCompat.java:403`
  `if (this.f1539e == null && isMultipleShare()) {`
- `sources/androidx/core/app/ShareCompat.java:425`
  `public boolean isMultipleShare() {`
- `sources/androidx/core/app/ShareCompat.java:429`
  `public boolean isShareIntent() {`
- `sources/androidx/core/app/ShareCompat.java:441`
  `String stringExtra = intent.getStringExtra(ShareCompat.EXTRA_CALLING_PACKAGE);`
- `sources/androidx/core/app/ShareCompat.java:442`
  `this.f1537c = stringExtra == null ? intent.getStringExtra(ShareCompat.EXTRA_CALLING_PACKAGE_INTEROP) : stringExtra;`
- `sources/androidx/core/app/ShareCompat.java:443`
  `this.f1538d = ShareCompat.a(intent);`
- `sources/androidx/core/app/ShareCompat.java:448`
  `if (this.f1539e == null && isMultipleShare()) {`
- `sources/androidx/core/app/ShareCompat.java:488`
  `ShareActionProvider shareActionProvider = !(actionProvider instanceof ShareActionProvider) ? new ShareActionProvider(intentBuilder.f1530a) : (ShareActionProvider) actionProvider;`
- `sources/androidx/core/app/ShareCompat.java:489`
  `StringBuilder sbA = androidx.activity.b.a(".sharecompat_");`
- `sources/androidx/core/app/ShareCompat.java:491`
  `shareActionProvider.setShareHistoryFileName(sbA.toString());`
- `sources/androidx/core/app/ShareCompat.java:492`
  `shareActionProvider.setShareIntent(intentBuilder.getIntent());`
- `sources/androidx/core/app/ShareCompat.java:493`
  `menuItem.setActionProvider(shareActionProvider);`
- `sources/androidx/core/app/SharedElementCallback.java:19`
  `public abstract class SharedElementCallback {`
- `sources/androidx/core/app/SharedElementCallback.java:24`
  `public interface OnSharedElementsReadyListener {`
- `sources/androidx/core/app/SharedElementCallback.java:25`
  `void onSharedElementsReady();`
- `sources/androidx/core/app/SharedElementCallback.java:28`
  `public Parcelable onCaptureSharedElementSnapshot(View view, Matrix matrix, RectF rectF) {`
- `sources/androidx/core/app/SharedElementCallback.java:61`
  `bundle.putParcelable("sharedElement:snapshot:bitmap", bitmap);`
- `sources/androidx/core/app/SharedElementCallback.java:62`
  `bundle.putString("sharedElement:snapshot:imageScaleType", imageView.getScaleType().toString());`
- `sources/androidx/core/app/SharedElementCallback.java:67`
  `bundle.putFloatArray("sharedElement:snapshot:imageMatrix", fArr);`
- `sources/androidx/core/app/SharedElementCallback.java:104`
  `Bitmap bitmap = (Bitmap) bundle.getParcelable("sharedElement:snapshot:bitmap");`
- `sources/androidx/core/app/SharedElementCallback.java:110`
  `imageView2.setScaleType(ImageView.ScaleType.valueOf(bundle.getString("sharedElement:snapshot:imageScaleType")));`
- `sources/androidx/core/app/SharedElementCallback.java:114`
  `float[] floatArray = bundle.getFloatArray("sharedElement:snapshot:imageMatrix");`
- `sources/androidx/core/content/res/ComplexColorCompat.java:5`
  `import android.graphics.Shader;`
- `sources/androidx/core/content/res/ComplexColorCompat.java:18`
  `public final Shader f1586a;`
- `sources/androidx/core/content/res/ComplexColorCompat.java:63`
  `public Shader getShader() {`
- `sources/androidx/core/graphics/drawable/IconCompat.java:12`
  `import android.graphics.BitmapShader;`
- `sources/androidx/core/graphics/drawable/IconCompat.java:17`
  `import android.graphics.Shader;`
- `sources/androidx/core/graphics/drawable/IconCompat.java:131`
  `BitmapShader bitmapShader = new BitmapShader(bitmap, tileMode, tileMode);`
- `sources/androidx/core/graphics/drawable/IconCompat.java:134`
  `bitmapShader.setLocalMatrix(matrix);`
- `sources/androidx/core/graphics/drawable/IconCompat.java:135`
  `paint.setShader(bitmapShader);`
- `sources/androidx/core/graphics/drawable/RoundedBitmapDrawable.java:5`
  `import android.graphics.BitmapShader;`
- `sources/androidx/core/graphics/drawable/RoundedBitmapDrawable.java:12`
  `import android.graphics.Shader;`
- `sources/androidx/core/graphics/drawable/RoundedBitmapDrawable.java:27`
  `public final BitmapShader f1617e;`
- `sources/androidx/core/graphics/drawable/RoundedBitmapDrawable.java:65`
  `Shader.TileMode tileMode = Shader.TileMode.CLAMP;`
- `sources/androidx/core/graphics/drawable/RoundedBitmapDrawable.java:66`
  `this.f1617e = new BitmapShader(bitmap, tileMode, tileMode);`

## BR090

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `audit_reports/00_independent_security_notes.md:7`
  `本文件先列出我独立检查后认为存在安全风险、但不能直接归入数据库论文规则 confirmed 结论的问题。它们不替代 'rule_catalog.tsv' 的逐条结论；逐条规则见 '03_rule_by_rule_mapping.tsv'。`
- `audit_reports/00_independent_security_notes.md:30`
  `### 为什么不是论文规则 confirmed`
- `audit_reports/00_independent_security_notes.md:32`
  `数据库中 WebView 相关规则主要关注不可信 Web 内容、JavaScript bridge、popup/iframe、Java-to-JavaScript 跨边界跟踪。当前证据显示统计页加载的是 'file:///android_asset/...html' 本地资源，未发现 'addJavascriptInterface' 或第三方 Web 内容接收这些数据。因此我没有把它归为 R030/R033/R035/R036 confirmed，只在 R034 中给出 supported_hypothesis：敏感健康统计值确实被 Java 传入 JS，但尚未看到外泄路径。`
- `audit_reports/00_independent_security_notes.md:36`
  `Manifest 中 'android:allowBackup="true"'，而 App 在本地 ObjectBox、cache/files 中保存健康测量记录、胎心原始数据、胎心音频路径和导出文件。该配置本身不是数据库规则中的独立漏洞类型，但会扩大本地数据恢复/迁移/取证面。由于未运行 'adb backup'、未确认设备 Android 版本与备份策略，本报告不把它当作 confirmed 数据泄露，只作为独立风险。`
- `audit_reports/00_independent_security_notes.md:61`
  `Manifest 中 'usesCleartextTraffic="true"'，'WebViewActivity' 会加载 'http://breath.yuwell.com/...' 法律声明页面。当前未发现健康数据通过 HTTP 上传，因此不能按 R023/R049/R053/R066 confirmed；但这仍是健康类 App 中不理想的网络安全姿态。HTTP 法律页面可被中间人篡改，也会泄露访问该页面的网络元数据。`
- `audit_reports/00_independent_security_notes.md:70`
  `源码中存在 Classic Bluetooth insecure RFCOMM server/client 代码：'listenUsingInsecureRfcommWithServiceRecord' 与 'createInsecureRfcommSocketToServiceRecord'。但是当前主要健康设备流程使用 BLE GATT 管理器，未确认这段 Classic Bluetooth 服务在当前 UI 中可达。因此它不是本次规则审计中的 confirmed 漏洞，而是需要 reachability 检查的遗留风险。`
- `audit_reports/01_database_rule_audit.md:29`
  `## 2. Method and Available Evidence`
- `audit_reports/01_database_rule_audit.md:35`
  `结论约束：每条规则只使用 'confirmed'、'supported_hypothesis'、'not_supported'、'not_testable'。单个字符串、单个权限、单个 SDK、单个 URL 不作为 confirmed。BLE、网络上传、后台行为没有运行态样本时不强行 confirmed。`
- `audit_reports/01_database_rule_audit.md:37`
  `## 3. Confirmed Findings`
- `audit_reports/01_database_rule_audit.md:41`
  `结论：'confirmed'`
- `audit_reports/01_database_rule_audit.md:54`
  `结论：'confirmed'`
- `audit_reports/01_database_rule_audit.md:66`
  `为什么 confirmed：日志调用、返回对象 'toString()'、实体 'toString()' 三段代码拼成完整静态路径。输出字段明确为胎心健康结果、测量时间和敏感文件路径，不是单个日志字符串猜测。`
- `audit_reports/01_database_rule_audit.md:70`
  `结论：'confirmed'`
- `audit_reports/01_database_rule_audit.md:86`
  `结论：'confirmed'`
- `audit_reports/01_database_rule_audit.md:97`
  `结论：'supported_hypothesis'。Manifest 中多个健康数据相关 Activity 为 'exported=true'，例如 'Data'、'BpStatistic'、'BoStatistic'、'BgStatistic'、'HtsStatistic'、'BpMeasure'、'BgMeasure'、'BoMeasure'、'HtsMeasure'、'BgResult'、'BpResult'、'HtsResult' 等。未在 Manifest 上看到自定义权限保护这些 Activity。没有 ADB/PoC 证明外部 App 可直接造成敏感数据泄露、越权修改或测量操作，...`
- `audit_reports/01_database_rule_audit.md:105`
  `结论：'supported_hypothesis'。'BpStatistic'、'BgStatistic'、'BoStatistic'、'HtsStatistic' 使用 'evaluateJavascript(...)' 把健康统计数据送入 WebView；这些 WebView 开启 JavaScript 和 DOM storage；release 构建中仍开启 WebView debugging。加载内容是本地 assets HTML，未发现第三方 Web 内容、'addJavascriptInterface'、远程 tracking endpoint，因此不能 confirmed 外泄或...`
- `audit_reports/01_database_rule_audit.md:117`
  `结论：'supported_hypothesis'。BLE 日志记录 BluetoothDevice、deviceName、RSSI；本地设置保存设备选择；同一 App 本地存储健康测量时间序列。未发现远程发送或第三方关联，因此不是 confirmed。`
- `audit_reports/01_database_rule_audit.md:125`
  `结论：'supported_hypothesis'。申请 BLE、位置、存储、Internet，且有 'requestLegacyExternalStorage=true' 与 'WRITE_EXTERNAL_STORAGE'。BLE/location 对扫描外设可能有功能需要，storage 对导出/分享可能有功能需要，因此不能仅凭权限列表 confirmed “过度”。`
- `audit_reports/01_database_rule_audit.md:135`
  `为什么不是 confirmed：缺少真实 BLE 外设、GATT 流量、绑定/重连记录、恶意本地 App PoC。因此不能确认实际设备可被 mis-bond、注入或越权访问；只能说明代码实现符合论文讨论的高风险模式。`
- `audit_reports/01_database_rule_audit.md:147`
  `未支持的规则：R021、R022、R024。未发现自定义 'X509TrustManager' 接受任意证书、'HostnameVerifier' 永远返回 true、一方自定义 TLS 栈替换安全默认。'usesCleartextTraffic=true' 和 HTTP 法律声明是独立弱点，但不是健康数据 TLS 误用 confirmed。`
- `audit_reports/01_database_rule_audit.md:169`
  `BLE/手动输入 -> 'DataRepository'/ViewModel -> ObjectBox entity -> DAO 保存 -> 统计 WebView/导出 Excel/结果页展示。该链路支撑 R006 confirmed、R051 confirmed、R054 confirmed、R055 supported_hypothesis、R057 supported_hypothesis。`
- `audit_reports/01_database_rule_audit.md:173`
  `BLE 'FetusManager' -> 'FetalMeasureActivity' 接收 'FetusData' -> raw/audio 写入 app cache -> 'FetalHeartMeasurement' 保存路径与测量值 -> 'FetusHome' recent result 日志输出 -> 'FhtResultActivity' 读取 raw/audio 并生成截图分享。该链路支撑 R050 confirmed、R051 confirmed、R054 confirmed；同时支持 R093/R095 not_supported，因为没有看到上传/静默外泄，只看到本地生...`
- `audit_reports/01_database_rule_audit.md:181`
  `静态 URL 仅确认 HTTP 法律声明页面。未发现健康数据 API、第三方服务器、analytics/tracker endpoint。该链路支撑 R023/R049/R052/R053/R059/R064/R065/R066/R072 not_supported。独立问题是全局允许 cleartext + HTTP 法律页面需要修正，但不能上升为健康数据明文传输 confirmed。`
- `audit_reports/02_evidence_chains.md:9`
  `- R050 / P013 / Security Concerns in Android mHealth Apps / 'confirmed'`
- `audit_reports/02_evidence_chains.md:10`
  `- R051 / P013 / Security Concerns in Android mHealth Apps / 'confirmed'`
- `audit_reports/02_evidence_chains.md:11`
  `- R054 / P014 / Unaddressed privacy risks in accredited health and wellness apps / 'confirmed'`
- `audit_reports/02_evidence_chains.md:70`
  `- R006 / P002 / 'confirmed'`
- `audit_reports/02_evidence_chains.md:71`
  `- R051 / P013 / 'confirmed'`
- `audit_reports/02_evidence_chains.md:72`
  `- R054 / P014 / 'confirmed'`
- `audit_reports/02_evidence_chains.md:129`
  `- R051 / P013 / 'confirmed'`
- `audit_reports/02_evidence_chains.md:130`
  `- R054 / P014 / 'confirmed'`
- `audit_reports/02_evidence_chains.md:147`
  `为什么不是媒体外泄 confirmed：当前看到的是用户触发的导出/打开操作，没有后台上传或远程 exfil endpoint。`
- `audit_reports/02_evidence_chains.md:161`
  `为什么不是 R095 confirmed：R095 关注截图/图像/音频/视频 artifacts exfiltrated；当前没有远程 exfil 或静默外泄证据，只看到用户可见分享。`
- `audit_reports/02_evidence_chains.md:220`
  `为什么不是 confirmed：缺少 'adb shell am start' 或恶意 App 调用 PoC；还未证明外部 extras 可造成敏感数据泄露、越权设备操作或持久化污染。`
- `audit_reports/04_source_evidence_index.md:83`
  `说明：BLE Manager 的 GATT read/write/notification 证据分散在 'sources/com/yuwell/bluetooth/le/manager/*Manager.java'，主报告中按链路引用；真实设备级 confirmed 需要抓包和外设复测。`

## BR092

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/androidx/appcompat/R.java:1718`
  `public static final int[] SearchView = {android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.inputType, android.R.attr.imeOptions, com.yuwell.healthmanager.R.attr.closeIcon, com.yuwell.healthmanager.R.attr.commitIcon, com.yuwell.healthmanager.R.attr.defaultQueryHint, com.yuwell.healthma...`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:469`
  `return this.f216c.isPowerSaveMode() ? 2 : 1;`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:123`
  `canvas.save();`
- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:601`
  `this.f619e.saveHierarchyState(sparseArray);`
- `sources/androidx/appcompat/widget/ActivityChooserView.java:325`
  `synchronized (activityChooserModel.f659a) {`
- `sources/androidx/appcompat/widget/ActivityChooserView.java:386`
  `synchronized (activityChooserModel.f659a) {`
- `sources/androidx/appcompat/widget/AppCompatRatingBar.java:24`
  `public synchronized void onMeasure(int i, int i4) {`
- `sources/androidx/appcompat/widget/SwitchCompat.java:475`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:509`
  `int iSave = canvas.save();`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:514`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/core/widget/NestedScrollView.java:486`
  `int iSave = canvas.save();`
- `sources/androidx/core/widget/NestedScrollView.java:505`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/core/widget/NestedScrollView.java:510`
  `int iSave2 = canvas.save();`
- `sources/androidx/core/widget/NestedScrollView.java:528`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/drawerlayout/widget/DrawerLayout.java:571`
  `int iSave = canvas.save();`
- `sources/androidx/drawerlayout/widget/DrawerLayout.java:599`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/fragment/app/FragmentTabHost.java:65`
  `public static class b extends View.BaseSavedState {`
- `sources/androidx/navigation/ui/R.java:1171`
  `public static final int transition_layout_save = 0x7f090244;`
- `sources/androidx/navigation/ui/R.java:2079`
  `public static final int BottomSheetBehavior_Layout_behavior_saveFlags = 0x00000007;`
- `sources/androidx/navigation/ui/R.java:2592`
  `public static final int[] BottomSheetBehavior_Layout = {android.R.attr.elevation, com.yuwell.healthmanager.R.attr.backgroundTint, com.yuwell.healthmanager.R.attr.behavior_expandedOffset, com.yuwell.healthmanager.R.attr.behavior_fitToContents, com.yuwell.healthmanager.R.attr.behavior_halfExpandedRati...`
- `sources/androidx/recyclerview/widget/DividerItemDecoration.java:69`
  `canvas.save();`
- `sources/androidx/recyclerview/widget/DividerItemDecoration.java:90`
  `canvas.save();`
- `sources/androidx/recyclerview/widget/RecyclerView.java:4695`
  `int iSave = canvas.save();`
- `sources/androidx/recyclerview/widget/RecyclerView.java:4701`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/recyclerview/widget/RecyclerView.java:4726`
  `int iSave4 = canvas.save();`
- `sources/androidx/viewpager/widget/ViewPager.java:798`
  `int iSave = canvas.save();`
- `sources/androidx/viewpager/widget/ViewPager.java:805`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/viewpager/widget/ViewPager.java:808`
  `int iSave2 = canvas.save();`
- `sources/androidx/viewpager/widget/ViewPager.java:815`
  `canvas.restoreToCount(iSave2);`
- `sources/com/airbnb/lottie/LottieDrawable.java:351`
  `canvas.save();`
- `sources/com/airbnb/lottie/R.java:1529`
  `public static final int[] SearchView = {android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.inputType, android.R.attr.imeOptions, com.yuwell.healthmanager.R.attr.closeIcon, com.yuwell.healthmanager.R.attr.commitIcon, com.yuwell.healthmanager.R.attr.defaultQueryHint, com.yuwell.healthma...`
- `sources/com/airbnb/lottie/model/layer/BaseLayer.java:362`
  `L.beginSection("Layer#saveLayer");`
- `sources/com/airbnb/lottie/model/layer/BaseLayer.java:363`
  `canvas.saveLayer(this.f3796h, this.f3791c, 31);`
- `sources/com/airbnb/lottie/model/layer/BaseLayer.java:364`
  `L.endSection("Layer#saveLayer");`
- `sources/com/airbnb/lottie/model/layer/ImageLayer.java:66`
  `canvas.save();`
- `sources/com/github/mikephil/charting/components/MarkerImage.java:59`
  `int iSave = canvas.save();`
- `sources/com/github/mikephil/charting/components/MarkerImage.java:62`
  `canvas.restoreToCount(iSave);`
- `sources/com/github/mikephil/charting/renderer/PieChartRenderer.java:141`
  `canvas.save();`
- `sources/com/github/mikephil/charting/utils/Utils.java:157`
  `canvas.save();`
- `sources/com/github/mikephil/charting/utils/Utils.java:193`
  `canvas.save();`

## BR093

paper_id: B004
paper_title: Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation

- `sources/androidx/fragment/app/z.java:25`
  `import androidx.savedstate.SavedStateRegistryController;`
- `sources/androidx/fragment/app/z.java:609`
  `fragment3.W = SavedStateRegistryController.create(fragment3);`
- `sources/androidx/recyclerview/widget/RecyclerView.java:2936`
  `RecyclerView.this.mPostedAnimatorRunner = false;`
- `sources/com/yuwell/healthmanager/data/source/DataRepository.java:564`
  `EventBus.getDefault().post(messageObtain);`

## BR094

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `sources/androidx/activity/result/ActivityResultRegistry.java:222`
  `public final void onSaveInstanceState(@NonNull Bundle bundle) {`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:123`
  `canvas.save();`
- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:601`
  `this.f619e.saveHierarchyState(sparseArray);`
- `sources/androidx/appcompat/widget/ActivityChooserView.java:639`
  `ViewCompat.saveAttributeDataForStyleable(this, context, iArr, attributeSet, typedArrayObtainStyledAttributes, i, 0);`
- `sources/androidx/appcompat/widget/DrawableUtils.java:78`
  `/* JADX WARN: Failed to restore switch over string. Please report as a decompilation issue */`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:182`
  `public final synchronized boolean b(@NonNull Context context, long j4, @NonNull Drawable drawable) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:216`
  `public final synchronized Drawable d(@NonNull Context context, long j4) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:416`
  `public synchronized void onConfigurationChanged(@NonNull Context context) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:423`
  `public synchronized void setHooks(ResourceManagerHooks resourceManagerHooks) {`
- `sources/androidx/appcompat/widget/SearchView.java:1448`
  `View viewFindViewById2 = findViewById(R.id.submit_area);`
- `sources/androidx/appcompat/widget/SwitchCompat.java:475`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/constraintlayout/solver/widgets/ConstraintWidget.java:1305`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:38:0x0084 -> B:39:0x0085). Please report as a decompilation issue!!! */`
- `sources/androidx/core/app/SharedElementCallback.java:85`
  `this.f1540a.postTranslate(-rectF.left, -rectF.top);`
- `sources/androidx/core/app/SharedElementCallback.java:86`
  `this.f1540a.postScale(fMin2, fMin2);`
- `sources/androidx/core/content/pm/ShortcutManagerCompat.java:43`
  `public static volatile ShortcutInfoCompatSaver<?> f1584a;`
- `sources/androidx/core/content/pm/ShortcutManagerCompat.java:333`
  `public static void reportShortcutUsed(@NonNull Context context, @NonNull String str) {`
- `sources/androidx/core/location/LocationManagerCompat.java:379`
  `synchronized (simpleArrayMap) {`
- `sources/androidx/core/location/LocationManagerCompat.java:389`
  `synchronized (simpleArrayMap2) {`
- `sources/androidx/core/location/LocationManagerCompat.java:399`
  `synchronized (simpleArrayMap3) {`
- `sources/androidx/core/os/CancellationSignal.java:45`
  `synchronized (this) {`
- `sources/androidx/core/os/CancellationSignal.java:55`
  `synchronized (this) {`
- `sources/androidx/core/os/HandlerCompat.java:36`
  `public static boolean postDelayed(@NonNull Handler handler, @NonNull Runnable runnable, @Nullable Object obj, long j4) {`
- `sources/androidx/core/os/HandlerCompat.java:38`
  `return handler.postDelayed(runnable, obj, j4);`
- `sources/androidx/core/os/TraceCompat.java:33`
  `f1661c = Trace.class.getMethod("asyncTraceBegin", cls, String.class, cls2);`
- `sources/androidx/core/os/TraceCompat.java:34`
  `f1662d = Trace.class.getMethod("asyncTraceEnd", cls, String.class, cls2);`
- `sources/androidx/core/os/TraceCompat.java:44`
  `Trace.beginAsyncSection(str, i);`
- `sources/androidx/core/os/TraceCompat.java:50`
  `Log.v("TraceCompat", "Unable to invoke asyncTraceBegin() via reflection.");`
- `sources/androidx/core/os/TraceCompat.java:60`
  `Trace.endAsyncSection(str, i);`
- `sources/androidx/core/os/TraceCompat.java:66`
  `Log.v("TraceCompat", "Unable to invoke endAsyncSection() via reflection.");`
- `sources/androidx/core/provider/FontsContractCompat.java:165`
  `public static Typeface getFontSync(Context context, FontRequest fontRequest, @Nullable ResourcesCompat.FontCallback fontCallback, @Nullable Handler handler, boolean z3, int i, int i4) {`
- `sources/androidx/core/util/PatternsCompat.java:25`
  `Pattern patternCompile3 = Pattern.compile("(?:(?:(?:[a-zA-Z0-9[ -\ud7ff豈-﷏ﷰ-\uffef𐀀-\u1fffd𠀀-\u2fffd𰀀-\u3fffd\u40000-\u4fffd\u50000-\u5fffd\u60000-\u6fffd\u70000-\u7fffd\u80000-\u8fffd\u90000-\u9fffd\ua0000-\uafffd\ub0000-\ubfffd\uc0000-\ucfffd\ud0000-\udfffd\ue1000-\uefffd&&[^ [\u2000-\u200a]\u2028...`
- `sources/androidx/core/util/TimeUtils.java:130`
  `synchronized (f1744a) {`
- `sources/androidx/core/util/TimeUtils.java:137`
  `synchronized (f1744a) {`
- `sources/androidx/core/view/ViewCompat.java:1310`
  `public static void postOnAnimation(@NonNull View view, Runnable runnable) {`
- `sources/androidx/core/view/ViewCompat.java:1311`
  `view.postOnAnimation(runnable);`
- `sources/androidx/core/view/ViewCompat.java:1314`
  `public static void postOnAnimationDelayed(@NonNull View view, Runnable runnable, long j4) {`
- `sources/androidx/core/view/ViewCompat.java:1315`
  `view.postOnAnimationDelayed(runnable, j4);`
- `sources/androidx/core/widget/AutoScrollHelper.java:384`
  `androidx.core.view.ViewCompat.postOnAnimationDelayed(r7, r0, r3)`
- `sources/androidx/core/widget/ContentLoadingProgressBar.java:61`
  `public synchronized void hide() {`
- `sources/androidx/core/widget/ContentLoadingProgressBar.java:71`
  `postDelayed(this.f1921e, 500 - j5);`

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
- `resources/res/drawable/circle_blue.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/circle_green.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/circle_grey.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/circle_yellow.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/divider.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/ic_arrow_back_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_calendar_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_clear_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_close_white_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_edit_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_keyboard_arrow_left_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_keyboard_arrow_right_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_menu_arrow_down_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_menu_arrow_up_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_mtrl_checked_circle.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_mtrl_chip_checked_black.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_mtrl_chip_checked_circle.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/ic_mtrl_chip_close_circle.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/line_black_5.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
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
- `resources/res/drawable/rectangle_bo_low.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/rectangle_bo_normal.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/rectangle_bo_too_low.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/retangle_round_conner_grey_background.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/_avd_hide_password__0_res_0x7f080000.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/res/drawable/_avd_hide_password__1_res_0x7f080001.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/res/drawable/_avd_hide_password__2_res_0x7f080002.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/res/drawable/_avd_show_password__0_res_0x7f080003.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/res/drawable/_avd_show_password__1_res_0x7f080004.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/res/drawable/_avd_show_password__2_res_0x7f080005.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/res/layout/abc_action_bar_title_item.xml:2`
  `<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/abc_action_bar_up_container.xml:2`
  `<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/abc_action_menu_layout.xml:2`
  `<androidx.appcompat.widget.ActionMenuView xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto"`
- `resources/res/layout/abc_action_mode_bar.xml:2`
  `<androidx.appcompat.widget.ActionBarContextView xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/abc_action_mode_close_item_material.xml:2`
  `<ImageView xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto"`
- `resources/res/layout/abc_activity_chooser_view.xml:2`
  `<view xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/abc_alert_dialog_button_bar_material.xml:2`
  `<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/abc_alert_dialog_material.xml:2`
  `<androidx.appcompat.widget.AlertDialogLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/abc_alert_dialog_title_material.xml:2`
  `<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/abc_cascading_menu_item_layout.xml:2`
  `<androidx.appcompat.view.menu.ListMenuItemView xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/abc_dialog_title_material.xml:2`
  `<androidx.appcompat.widget.FitWindowsLinearLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/abc_expanded_menu_layout.xml:2`
  `<androidx.appcompat.view.menu.ExpandedMenuView xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/abc_list_menu_item_icon.xml:2`
  `<ImageView xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/abc_list_menu_item_layout.xml:2`
  `<androidx.appcompat.view.menu.ListMenuItemView xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/abc_popup_menu_header_item_layout.xml:2`
  `<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/abc_popup_menu_item_layout.xml:2`
  `<androidx.appcompat.view.menu.ListMenuItemView xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/abc_screen_content_include.xml:2`
  `<merge xmlns:android="http://schemas.android.com/apk/res/android">`

## BR096

paper_id: B011
paper_title: Locking it down: The privacy and security of mobile medication apps

- `resources/assets/js/highcharts.js:65`
  `z=!0);var l=x.element;(e=a.element.getAttribute("id"))||a.element.setAttribute("id",e=M());if(d)for(a=b.getElementsByTagName("tspan");a.length;)a[0].setAttribute("y",0),f(k.dx)&&a[0].setAttribute("x",-k.dx),l.appendChild(a[0]);z&&x&&x.add({element:this.text?this.text.element:b});l.setAttributeNS("ht...`
- `resources/assets/js/highcharts.js:150`
  `backgroundColor:q("#f7f7f7").setOpacity(.85).get(),borderWidth:1,shadow:!0,style:{color:"#333333",cursor:"default",fontSize:"12px",whiteSpace:"nowrap"}},credits:{enabled:!0,href:"https://www.highcharts.com?credits",position:{align:"right",x:-10,verticalAlign:"bottom",y:-5},style:{cursor:"pointer",co...`
- `resources/res/color/design_box_stroke_color.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/layout/design_text_input_end_icon.xml:2`
  `<com.google.android.material.internal.CheckableImageButton xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/design_text_input_start_icon.xml:2`
  `<com.google.android.material.internal.CheckableImageButton xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/mtrl_picker_text_input_date.xml:2`
  `<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/menu/menu_fht_delete.xml:2`
  `<menu xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto">`
- `sources/com/yuwell/healthmanager/view/impl/setting/WebViewActivity.java:18`
  `public String C = "http://breath.yuwell.com/ConsumerApi/license/legalnotice/legalnotice-cn.html";`
- `sources/com/yuwell/healthmanager/view/impl/setting/WebViewActivity.java:19`
  `public String D = "http://breath.yuwell.com/ConsumerApi/license/legalnotice/legalnotice-en.html";`
- `sources/com/yuwell/healthmanager/view/impl/setting/WebViewActivity.java:20`
  `public String E = "http://breath.yuwell.com/ConsumerApi/license/legalnotice/legalnotice-es.html";`
- `sources/com/yuwell/healthmanager/view/impl/setting/WebViewActivity.java:21`
  `public String F = "http://breath.yuwell.com/ConsumerApi/license/legalnotice/legalnotice-pt.html";`
- `sources/io/objectbox/sync/SyncBuilder.java:73`
  `throw new IllegalStateException("This library does not include ObjectBox Sync. Please visit https://objectbox.io/sync/ for options.");`
- `sources/io/objectbox/sync/server/SyncServerBuilder.java:38`
  `throw new IllegalStateException("This library does not include ObjectBox Sync Server. Please visit https://objectbox.io/sync/ for options.");`
- `sources/io/reactivex/Completable.java:780`
  `ObjectHelper.requireNonNull(completableObserverOnSubscribe, "The RxJavaPlugins.onSubscribe hook returned a null CompletableObserver. Please check the handler provided to RxJavaPlugins.setOnCompletableSubscribe for invalid null returns. Further reading: https://github.com/ReactiveX/RxJava/wiki/Plugin...`
- `sources/io/reactivex/Maybe.java:1243`
  `ObjectHelper.requireNonNull(maybeObserverOnSubscribe, "The RxJavaPlugins.onSubscribe hook returned a null MaybeObserver. Please check the handler provided to RxJavaPlugins.setOnMaybeSubscribe for invalid null returns. Further reading: https://github.com/ReactiveX/RxJava/wiki/Plugins");`
- `sources/io/reactivex/Observable.java:3079`
  `ObjectHelper.requireNonNull(observerOnSubscribe, "The RxJavaPlugins.onSubscribe hook returned a null Observer. Please change the handler provided to RxJavaPlugins.setOnObservableSubscribe for invalid null returns. Further reading: https://github.com/ReactiveX/RxJava/wiki/Plugins");`
- `sources/io/reactivex/Single.java:1108`
  `ObjectHelper.requireNonNull(singleObserverOnSubscribe, "The RxJavaPlugins.onSubscribe hook returned a null SingleObserver. Please check the handler provided to RxJavaPlugins.setOnSingleSubscribe for invalid null returns. Further reading: https://github.com/ReactiveX/RxJava/wiki/Plugins");`
- `sources/jxl/demo/ReadWrite.java:114`
  `writableHyperlink.setURL(new URL("http://www.andykhan.com/jexcelapi/index.html"));`
- `sources/jxl/demo/Write.java:298`
  `writableSheet.addCell(new Formula(2, 16, "HYPERLINK(\"http://www.andykhan.com/jexcelapi\", \"JExcelApi Home Page\")"));`
- `sources/jxl/demo/Write.java:299`
  `writableSheet.addCell(new Label(3, 16, "HYPERLINK(\"http://www.andykhan.com/jexcelapi\", \"JExcelApi Home Page\")"));`
- `sources/jxl/demo/Write.java:493`
  `URL url = new URL("http://www.andykhan.com/jexcelapi");`
- `sources/jxl/demo/Write.java:511`
  `writableSheetCreateSheet3.addHyperlink(new WritableHyperlink(0, 38, 0, 38, new URL("http://www.amazon.co.uk/exec/obidos/ASIN/0571058086/qid=1099836249/sr=1-3/ref=sr_1_11_3/202-6017285-1620664")));`
- `sources/jxl/read/biff/HyperlinkRecord.java:137`
  `this.f11115g = new URL("http://www.andykhan.com/jexcelapi/index.html");`
- `sources/jxl/read/biff/HyperlinkRecord.java:150`
  `this.f11115g = new URL("http://www.andykhan.com/jexcelapi/index.html");`
- `sources/pl/droidsonroids/gif/GifTextureView.java:251`
  `int attributeIntValue = attributeSet.getAttributeIntValue("http://schemas.android.com/apk/res/android", "scaleType", -1);`
