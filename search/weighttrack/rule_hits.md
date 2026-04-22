# Rule Search Hits

## BR004

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/AndroidManifest.xml:17`
  `<uses-permission android:name="android.permission.VIBRATE"/>`
- `resources/AndroidManifest.xml:18`
  `<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>`
- `resources/AndroidManifest.xml:19`
  `<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>`

## BR005

paper_id: B021
paper_title: Metadata-Based Privacy Assessment for Mobile mHealth

- `resources/AndroidManifest.xml:18`
  `<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>`
- `resources/AndroidManifest.xml:19`
  `<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>`

## BR009

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/okhttp3/OkHttpClient.java:24`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/OkHttpClient.java:190`
  `X509TrustManager x509TrustManagerPlatformTrustManager = Util.platformTrustManager();`
- `sources/okhttp3/OkHttpClient.java:191`
  `this.sslSocketFactory = newSslSocketFactory(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/OkHttpClient.java:192`
  `this.certificateChainCleaner = CertificateChainCleaner.get(x509TrustManagerPlatformTrustManager);`
- `sources/okhttp3/OkHttpClient.java:219`
  `private static SSLSocketFactory newSslSocketFactory(X509TrustManager x509TrustManager) {`
- `sources/okhttp3/OkHttpClient.java:222`
  `sSLContext.init(null, new TrustManager[]{x509TrustManager}, null);`
- `sources/okhttp3/OkHttpClient.java:558`
  `public Builder sslSocketFactory(SSLSocketFactory sSLSocketFactory, X509TrustManager x509TrustManager) {`
- `sources/okhttp3/OkHttpClient.java:560`
  `Objects.requireNonNull(x509TrustManager, "trustManager == null");`
- `sources/okhttp3/OkHttpClient.java:562`
  `this.certificateChainCleaner = CertificateChainCleaner.get(x509TrustManager);`
- `sources/okhttp3/internal/Util.java:36`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/Util.java:661`
  `public static X509TrustManager platformTrustManager() {`
- `sources/okhttp3/internal/Util.java:666`
  `if (trustManagers.length != 1 || !(trustManagers[0] instanceof X509TrustManager)) {`
- `sources/okhttp3/internal/Util.java:669`
  `return (X509TrustManager) trustManagers[0];`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:19`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:68`
  `protected X509TrustManager trustManager(SSLSocketFactory sSLSocketFactory) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:77`
  `X509TrustManager x509TrustManager = (X509TrustManager) readFieldOrNull(fieldOrNull, X509TrustManager.class, "x509TrustManager");`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:78`
  `return x509TrustManager != null ? x509TrustManager : (X509TrustManager) readFieldOrNull(fieldOrNull, X509TrustManager.class, "trustManager");`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:193`
  `public CertificateChainCleaner buildCertificateChainCleaner(X509TrustManager x509TrustManager) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:195`
  `Class<?> cls = Class.forName("android.net.http.X509TrustManagerExtensions");`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:196`
  `return new AndroidCertificateChainCleaner(cls.getConstructor(X509TrustManager.class).newInstance(x509TrustManager), cls.getMethod("checkServerTrusted", X509Certificate[].class, String.class, String.class));`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:198`
  `return super.buildCertificateChainCleaner(x509TrustManager);`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:230`
  `public TrustRootIndex buildTrustRootIndex(X509TrustManager x509TrustManager) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:232`
  `Method declaredMethod = x509TrustManager.getClass().getDeclaredMethod("findTrustAnchorByIssuerAndSignature", X509Certificate.class);`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:234`
  `return new AndroidTrustRootIndex(x509TrustManager, declaredMethod);`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:236`
  `return super.buildTrustRootIndex(x509TrustManager);`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:242`
  `private final Method checkServerTrusted;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:243`
  `private final Object x509TrustManagerExtensions;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:250`
  `this.x509TrustManagerExtensions = obj;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:251`
  `this.checkServerTrusted = method;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:257`
  `return (List) this.checkServerTrusted.invoke(this.x509TrustManagerExtensions, (X509Certificate[]) list.toArray(new X509Certificate[list.size()]), "RSA", str);`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:330`
  `private final X509TrustManager trustManager;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:332`
  `AndroidTrustRootIndex(X509TrustManager x509TrustManager, Method method) {`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:334`
  `this.trustManager = x509TrustManager;`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:10`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:25`
  `public X509TrustManager trustManager(SSLSocketFactory sSLSocketFactory) {`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:32`
  `return (X509TrustManager) readFieldOrNull(fieldOrNull, X509TrustManager.class, "x509TrustManager");`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:10`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:54`
  `public X509TrustManager trustManager(SSLSocketFactory sSLSocketFactory) {`
- `sources/okhttp3/internal/platform/Platform.java:18`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/platform/Platform.java:60`
  `protected X509TrustManager trustManager(SSLSocketFactory sSLSocketFactory) {`
- `sources/okhttp3/internal/platform/Platform.java:66`
  `return (X509TrustManager) readFieldOrNull(fieldOrNull, X509TrustManager.class, "trustManager");`
- `sources/okhttp3/internal/platform/Platform.java:106`
  `public CertificateChainCleaner buildCertificateChainCleaner(X509TrustManager x509TrustManager) {`
- `sources/okhttp3/internal/platform/Platform.java:107`
  `return new BasicCertificateChainCleaner(buildTrustRootIndex(x509TrustManager));`
- `sources/okhttp3/internal/platform/Platform.java:111`
  `X509TrustManager x509TrustManagerTrustManager = trustManager(sSLSocketFactory);`
- `sources/okhttp3/internal/platform/Platform.java:112`
  `if (x509TrustManagerTrustManager == null) {`
- `sources/okhttp3/internal/platform/Platform.java:115`
  `return buildCertificateChainCleaner(x509TrustManagerTrustManager);`
- `sources/okhttp3/internal/platform/Platform.java:192`
  `public TrustRootIndex buildTrustRootIndex(X509TrustManager x509TrustManager) {`
- `sources/okhttp3/internal/platform/Platform.java:193`
  `return new BasicTrustRootIndex(x509TrustManager.getAcceptedIssuers());`
- `sources/okhttp3/internal/tls/CertificateChainCleaner.java:6`
  `import javax.net.ssl.X509TrustManager;`
- `sources/okhttp3/internal/tls/CertificateChainCleaner.java:13`
  `public static CertificateChainCleaner get(X509TrustManager x509TrustManager) {`
- `sources/okhttp3/internal/tls/CertificateChainCleaner.java:14`
  `return Platform.get().buildCertificateChainCleaner(x509TrustManager);`

## BR010

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/okhttp3/internal/connection/RealConnection.java:283`
  `if (this.http2Connection == null || route == null || route.proxy().type() != Proxy.Type.DIRECT || this.route.proxy().type() != Proxy.Type.DIRECT || !this.route.socketAddress().equals(route.socketAddress()) || route.address().hostnameVerifier() != OkHostnameVerifier.INSTANCE || !supportsUrl(address.u...`
- `sources/okhttp3/internal/connection/RealConnection.java:301`
  `return this.handshake != null && OkHostnameVerifier.INSTANCE.verify(httpUrl.host(), (X509Certificate) this.handshake.peerCertificates().get(0));`
- `sources/okhttp3/internal/tls/BasicCertificateChainCleaner.java:61`
  `x509Certificate.verify(x509Certificate2.getPublicKey());`

## BR011

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/okhttp3/internal/connection/ConnectionSpecSelector.java:11`
  `import javax.net.ssl.SSLHandshakeException;`
- `sources/okhttp3/internal/connection/ConnectionSpecSelector.java:58`
  `boolean z = iOException instanceof SSLHandshakeException;`
- `sources/okhttp3/internal/connection/ConnectionSpecSelector.java:59`
  `if ((z && (iOException.getCause() instanceof CertificateException)) || (iOException instanceof SSLPeerUnverifiedException)) {`
- `sources/okhttp3/internal/connection/ConnectionSpecSelector.java:62`
  `return z || (iOException instanceof SSLProtocolException) || (iOException instanceof SSLException);`
- `sources/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:9`
  `import java.security.cert.CertificateException;`
- `sources/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:11`
  `import javax.net.ssl.SSLHandshakeException;`
- `sources/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:159`
  `return iOException instanceof InterruptedIOException ? (iOException instanceof SocketTimeoutException) && !z : (((iOException instanceof SSLHandshakeException) && (iOException.getCause() instanceof CertificateException)) || (iOException instanceof SSLPeerUnverifiedException)) ? false : true;`

## BR012

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/okhttp3/Address.java:18`
  `final CertificatePinner certificatePinner;`
- `sources/okhttp3/Address.java:36`
  `public Address(String str, int i, Dns dns, SocketFactory socketFactory, @Nullable SSLSocketFactory sSLSocketFactory, @Nullable HostnameVerifier hostnameVerifier, @Nullable CertificatePinner certificatePinner, Authenticator authenticator, @Nullable Proxy proxy, List<Protocol> list, List<ConnectionSpe...`
- `sources/okhttp3/Address.java:53`
  `this.certificatePinner = certificatePinner;`
- `sources/okhttp3/Address.java:100`
  `public CertificatePinner certificatePinner() {`
- `sources/okhttp3/Address.java:101`
  `return this.certificatePinner;`
- `sources/okhttp3/Address.java:122`
  `CertificatePinner certificatePinner = this.certificatePinner;`
- `sources/okhttp3/Address.java:123`
  `return iHashCode4 + (certificatePinner != null ? certificatePinner.hashCode() : 0);`
- `sources/okhttp3/Address.java:127`
  `return this.dns.equals(address.dns) && this.proxyAuthenticator.equals(address.proxyAuthenticator) && this.protocols.equals(address.protocols) && this.connectionSpecs.equals(address.connectionSpecs) && this.proxySelector.equals(address.proxySelector) && Util.equal(this.proxy, address.proxy) && Util.e...`
- `sources/okhttp3/CertificatePinner.java:19`
  `public final class CertificatePinner {`
- `sources/okhttp3/CertificatePinner.java:20`
  `public static final CertificatePinner DEFAULT = new Builder().build();`
- `sources/okhttp3/CertificatePinner.java:26`
  `CertificatePinner(Set<Pin> set, @Nullable CertificateChainCleaner certificateChainCleaner) {`
- `sources/okhttp3/CertificatePinner.java:35`
  `if (obj instanceof CertificatePinner) {`
- `sources/okhttp3/CertificatePinner.java:36`
  `CertificatePinner certificatePinner = (CertificatePinner) obj;`
- `sources/okhttp3/CertificatePinner.java:37`
  `if (Util.equal(this.certificateChainCleaner, certificatePinner.certificateChainCleaner) && this.pins.equals(certificatePinner.pins)) {`
- `sources/okhttp3/CertificatePinner.java:66`
  `if (pin.hashAlgorithm.equals("sha256/")) {`
- `sources/okhttp3/CertificatePinner.java:125`
  `CertificatePinner withCertificateChainCleaner(@Nullable CertificateChainCleaner certificateChainCleaner) {`
- `sources/okhttp3/CertificatePinner.java:126`
  `return Util.equal(this.certificateChainCleaner, certificateChainCleaner) ? this : new CertificatePinner(this.pins, certificateChainCleaner);`
- `sources/okhttp3/CertificatePinner.java:133`
  `return "sha256/" + sha256((X509Certificate) certificate).b();`
- `sources/okhttp3/CertificatePinner.java:164`
  `} else if (str2.startsWith("sha256/")) {`
- `sources/okhttp3/CertificatePinner.java:165`
  `this.hashAlgorithm = "sha256/";`
- `sources/okhttp3/CertificatePinner.java:168`
  `throw new IllegalArgumentException("pins must start with 'sha256/' or 'sha1/': " + str2);`
- `sources/okhttp3/CertificatePinner.java:221`
  `public CertificatePinner build() {`
- `sources/okhttp3/CertificatePinner.java:222`
  `return new CertificatePinner(new LinkedHashSet(this.pins), null);`
- `sources/okhttp3/OkHttpClient.java:50`
  `final CertificatePinner certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:198`
  `this.certificatePinner = builder.certificatePinner.withCertificateChainCleaner(this.certificateChainCleaner);`
- `sources/okhttp3/OkHttpClient.java:288`
  `public CertificatePinner certificatePinner() {`
- `sources/okhttp3/OkHttpClient.java:289`
  `return this.certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:365`
  `CertificatePinner certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:411`
  `this.certificatePinner = CertificatePinner.DEFAULT;`
- `sources/okhttp3/OkHttpClient.java:446`
  `this.certificatePinner = okHttpClient.certificatePinner;`
- `sources/okhttp3/OkHttpClient.java:572`
  `public Builder certificatePinner(CertificatePinner certificatePinner) {`
- `sources/okhttp3/OkHttpClient.java:573`
  `Objects.requireNonNull(certificatePinner, "certificatePinner == null");`
- `sources/okhttp3/OkHttpClient.java:574`
  `this.certificatePinner = certificatePinner;`
- `sources/okhttp3/internal/connection/RealConnection.java:25`
  `import okhttp3.CertificatePinner;`
- `sources/okhttp3/internal/connection/RealConnection.java:192`
  `throw new SSLPeerUnverifiedException("Hostname " + address.url().host() + " not verified:\n    certificate: " + CertificatePinner.pin(x509Certificate) + "\n    DN: " + x509Certificate.getSubjectDN().getName() + "\n    subjectAltNames: " + OkHostnameVerifier.allSubjectAltNames(x509Certificate));`
- `sources/okhttp3/internal/connection/RealConnection.java:194`
  `address.certificatePinner().check(address.url().host(), handshake.peerCertificates());`
- `sources/okhttp3/internal/connection/RealConnection.java:287`
  `address.certificatePinner().check(address.url().host(), handshake().peerCertificates());`
- `sources/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:16`
  `import okhttp3.CertificatePinner;`
- `sources/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:133`
  `CertificatePinner certificatePinner;`
- `sources/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:138`
  `certificatePinner = this.client.certificatePinner();`
- `sources/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:142`
  `certificatePinner = null;`
- `sources/okhttp3/internal/http/RetryAndFollowUpInterceptor.java:144`
  `return new Address(httpUrl.host(), httpUrl.port(), this.client.dns(), this.client.socketFactory(), sSLSocketFactory, hostnameVerifier, certificatePinner, this.client.proxyAuthenticator(), this.client.proxy(), this.client.protocols(), this.client.connectionSpecs(), this.client.proxySelector());`

## BR013

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `resources/AndroidManifest.xml:2`
  `<manifest xmlns:android="http://schemas.android.com/apk/res/android"`
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
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/abc_seekbar_tick_mark_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/abc_text_cursor_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/res/drawable/abc_vector_test.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/admob_close_button_black_circle_white_cross.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/admob_close_button_white_circle_black_cross.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/avd_hide_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_hide_password__0_res_0x7f080000">`
- `resources/res/drawable/avd_show_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_show_password__0_res_0x7f080003">`
- `resources/res/drawable/bk_input_selector.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/btn_checkbox_checked_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/btn_checkbox_unchecked_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/btn_radio_off_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/btn_radio_on_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/cell_line_divider.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/res/drawable/circle.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/design_ic_visibility.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/design_ic_visibility_off.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/group_channel_list_unread_background.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
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

## BR014

paper_id: B022
paper_title: A Study of Android Application Security

- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1348`
  `panelFeatureState.qwertyMode = KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1;`
- `sources/androidx/appcompat/app/ToolbarActionBar.java:436`
  `menu.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);`
- `sources/androidx/appcompat/app/WindowDecorActionBar.java:1284`
  `menu.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);`
- `sources/androidx/core/content/ContextCompat.java:56`
  `import android.telephony.TelephonyManager;`
- `sources/androidx/core/content/ContextCompat.java:305`
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
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:24`
  `public class AdvertisingIdClient {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:63`
  `public AdvertisingIdClient(Context context) {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:67`
  `public static Info getAdvertisingIdInfo(Context context) {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:68`
  `AdvertisingIdClient advertisingIdClient = new AdvertisingIdClient(context, -1L, true, false);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:71`
  `advertisingIdClient.zzb(false);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:72`
  `Info infoZzd = advertisingIdClient.zzd(-1);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:73`
  `advertisingIdClient.zzc(infoZzd, true, 0.0f, SystemClock.elapsedRealtime() - jElapsedRealtime, "", null);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:81`
  `AdvertisingIdClient advertisingIdClient = new AdvertisingIdClient(context, -1L, false, false);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:83`
  `advertisingIdClient.zzb(false);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:85`
  `synchronized (advertisingIdClient) {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:86`
  `if (advertisingIdClient.zzc) {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:87`
  `Preconditions.checkNotNull(advertisingIdClient.zza);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:88`
  `Preconditions.checkNotNull(advertisingIdClient.zzb);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:89`
  `zZzd = advertisingIdClient.zzb.zzd();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:91`
  `synchronized (advertisingIdClient.zzd) {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:92`
  `zzb zzbVar = advertisingIdClient.zze;`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:94`
  `throw new IOException("AdvertisingIdClient is not connected.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:98`
  `advertisingIdClient.zzb(false);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:99`
  `if (!advertisingIdClient.zzc) {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:100`
  `throw new IOException("AdvertisingIdClient cannot reconnect.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:102`
  `Preconditions.checkNotNull(advertisingIdClient.zza);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:103`
  `Preconditions.checkNotNull(advertisingIdClient.zzb);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:105`
  `zZzd = advertisingIdClient.zzb.zzd();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:107`
  `Log.i("AdvertisingIdClient", "GMS remote exception ", e);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:111`
  `throw new IOException("AdvertisingIdClient cannot reconnect.", e2);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:115`
  `advertisingIdClient.zze();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:118`
  `advertisingIdClient.zza();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:137`
  `throw new IOException("AdvertisingIdClient is not connected.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:143`
  `throw new IOException("AdvertisingIdClient cannot reconnect.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:150`
  `Log.i("AdvertisingIdClient", "GMS remote exception ", e);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:154`
  `throw new IOException("AdvertisingIdClient cannot reconnect.", e2);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:203`
  `Log.i("AdvertisingIdClient", "AdvertisingIdClient unbindService failed.", th);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:268`
  `map.put("tag", "AdvertisingIdClient");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:274`
  `public AdvertisingIdClient(Context context, long j, boolean z, boolean z2) {`
- `sources/com/google/android/gms/ads/identifier/zza.java:10`
  `zza(AdvertisingIdClient advertisingIdClient, Map map) {`
- `sources/com/google/android/gms/ads/identifier/zzb.java:11`
  `private final WeakReference<AdvertisingIdClient> zzc;`
- `sources/com/google/android/gms/ads/identifier/zzb.java:14`
  `public zzb(AdvertisingIdClient advertisingIdClient, long j) {`
- `sources/com/google/android/gms/ads/identifier/zzb.java:15`
  `this.zzc = new WeakReference<>(advertisingIdClient);`
- `sources/com/google/android/gms/ads/identifier/zzb.java:21`
  `AdvertisingIdClient advertisingIdClient = this.zzc.get();`
- `sources/com/google/android/gms/ads/identifier/zzb.java:22`
  `if (advertisingIdClient != null) {`
- `sources/com/google/android/gms/ads/identifier/zzb.java:23`
  `advertisingIdClient.zza();`
- `sources/com/google/android/gms/ads/internal/util/zzaa.java:4`
  `import android.telephony.TelephonyManager;`
- `sources/com/google/android/gms/ads/internal/util/zzaa.java:9`
  `public final int zzq(Context context, TelephonyManager telephonyManager) {`
- `sources/com/google/android/gms/ads/internal/util/zzaa.java:11`
  `return (zzt.zzF(context, "android.permission.ACCESS_NETWORK_STATE") && telephonyManager.isDataEnabled()) ? 2 : 1;`
- `sources/com/google/android/gms/ads/internal/util/zzae.java:12`
  `import android.telephony.TelephonyManager;`
- `sources/com/google/android/gms/ads/internal/util/zzae.java:140`
  `public int zzq(Context context, TelephonyManager telephonyManager) {`
- `sources/com/google/android/gms/ads/internal/util/zzc.java:4`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/ads/internal/util/zzc.java:22`
  `isAdIdFakeForDebugLogging = AdvertisingIdClient.getIsAdIdFakeForDebugLogging(this.zza);`
- `sources/com/google/android/gms/ads/internal/util/zzt.java:23`
  `import android.telephony.TelephonyManager;`
- `sources/com/google/android/gms/ads/internal/util/zzt.java:127`
  `TelephonyManager telephonyManager = (TelephonyManager) context.getSystemService("phone");`
- `sources/com/google/android/gms/ads/internal/util/zzt.java:133`
  `return telephonyManager.getNetworkType();`
- `sources/com/google/android/gms/fitness/data/zzq.java:7`
  `import android.telephony.TelephonyManager;`

## BR015

paper_id: B022
paper_title: A Study of Android Application Security

- `sources/com/google/android/gms/ads/internal/util/zzt.java:662`
  `sb.append(Locale.getDefault());`
- `sources/com/google/android/gms/ads/internal/util/zzt.java:663`
  `if (Build.DEVICE != null) {`
- `sources/com/google/android/gms/ads/internal/util/zzt.java:665`
  `sb.append(Build.DEVICE);`
- `sources/com/google/android/gms/fitness/data/Device.java:30`
  `return new Device(Build.MANUFACTURER, Build.MODEL, zzq.zza(context), iZzb, 2);`
- `sources/com/google/android/gms/fitness/data/zzq.java:40`
  `if (!TextUtils.isEmpty(Build.PRODUCT) && Build.PRODUCT.startsWith("glass_")) {`
- `sources/com/google/android/gms/internal/ads/zzaxb.java:25`
  `String str = Build.DEVICE;`
- `sources/com/google/android/gms/internal/ads/zzaxb.java:27`
  `String str2 = Build.MANUFACTURER;`
- `sources/com/google/android/gms/internal/ads/zzaxb.java:29`
  `String str3 = Build.MODEL;`
- `sources/com/google/android/gms/internal/ads/zzcct.java:196`
  `String str2 = Build.MANUFACTURER;`
- `sources/com/google/android/gms/internal/ads/zzcct.java:197`
  `String string2 = Build.MODEL;`
- `sources/com/google/android/gms/internal/ads/zzcdu.java:174`
  `this.zzp = Build.DEVICE;`
- `sources/com/google/android/gms/internal/ads/zzcis.java:202`
  `return Build.VERSION.SDK_INT >= 31 ? Build.FINGERPRINT.contains("generic") || Build.FINGERPRINT.contains("emulator") : Build.DEVICE.startsWith("generic");`
- `sources/com/google/android/gms/internal/ads/zzflc.java:58`
  `String str = Build.MANUFACTURER;`
- `sources/com/google/android/gms/internal/ads/zzflc.java:59`
  `String str2 = Build.MODEL;`
- `sources/com/google/android/gms/internal/ads/zzfn.java:58`
  `String str = Build.DEVICE;`
- `sources/com/google/android/gms/internal/ads/zzfn.java:60`
  `String str2 = Build.MANUFACTURER;`
- `sources/com/google/android/gms/internal/ads/zzfn.java:62`
  `String str3 = Build.MODEL;`
- `sources/com/google/android/gms/internal/consent_sdk/zzbz.java:42`
  `if (Build.FINGERPRINT.startsWith("generic") || Build.FINGERPRINT.startsWith("unknown") || Build.MODEL.contains("google_sdk") || Build.MODEL.contains("Emulator") || Build.MODEL.contains("Android SDK built for x86") || Build.MANUFACTURER.contains("Genymotion")) {`
- `sources/com/google/android/gms/internal/consent_sdk/zzbz.java:45`
  `return (Build.BRAND.startsWith("generic") && Build.DEVICE.startsWith("generic")) || "google_sdk".equals(Build.PRODUCT);`
- `sources/com/google/android/material/datepicker/DaysOfWeekAdapter.java:57`
  `textView.setText(this.calendar.getDisplayName(7, CALENDAR_DAY_STYLE, Locale.getDefault()));`
- `sources/com/google/android/material/datepicker/DaysOfWeekAdapter.java:58`
  `textView.setContentDescription(String.format(viewGroup.getContext().getString(R.string.mtrl_picker_day_of_week_column_header), this.calendar.getDisplayName(7, 2, Locale.getDefault())));`
- `sources/com/google/android/material/internal/ManufacturerUtils.java:16`
  `return Build.MANUFACTURER.toLowerCase(Locale.ENGLISH).equals(MEIZU);`
- `sources/com/google/android/material/internal/ManufacturerUtils.java:20`
  `return Build.MANUFACTURER.toLowerCase(Locale.ENGLISH).equals(LGE);`
- `sources/com/google/android/material/internal/ManufacturerUtils.java:24`
  `return Build.MANUFACTURER.toLowerCase(Locale.ENGLISH).equals(SAMSUNG);`
- `sources/com/google/firebase/FirebaseCommonRegistrar.java:35`
  `arrayList.add(LibraryVersionComponent.create(DEVICE_NAME, safeValue(Build.PRODUCT)));`
- `sources/com/google/firebase/FirebaseCommonRegistrar.java:36`
  `arrayList.add(LibraryVersionComponent.create(DEVICE_MODEL, safeValue(Build.DEVICE)));`
- `sources/com/google/firebase/FirebaseCommonRegistrar.java:37`
  `arrayList.add(LibraryVersionComponent.create(DEVICE_BRAND, safeValue(Build.BRAND)));`
- `sources/com/ikdong/weight/activity/SettingActivity.java:291`
  `String strA = o.a("PARAM_LANG", Locale.getDefault().getLanguage());`
- `sources/com/ikdong/weight/activity/SettingActivity.java:293`
  `strA = Locale.getDefault().getLanguage();`
- `sources/com/ikdong/weight/activity/SyncFitbitActivity.java:99`
  `private SimpleDateFormat f1640d = new SimpleDateFormat("yyyyMMdd", Locale.getDefault());`
- `sources/com/ikdong/weight/activity/SyncWithingsActivity.java:84`
  `private final SimpleDateFormat f1680c = new SimpleDateFormat("yyyyMMdd", Locale.getDefault());`
- `sources/com/ikdong/weight/discover/ui/h.java:59`
  `strD = item.d() + "_" + Locale.getDefault().getLanguage().toUpperCase();`
- `sources/com/ikdong/weight/service/ImageSyncUpService.java:43`
  `this.f1886d = Locale.getDefault();`
- `sources/com/ikdong/weight/service/ImageTempSyncUpService.java:44`
  `this.f1888b = Locale.getDefault();`
- `sources/com/ikdong/weight/util/g.java:78`
  `String language = Locale.getDefault().getLanguage();`
- `sources/com/ikdong/weight/util/g.java:669`
  `java.util.Locale r1 = java.util.Locale.getDefault()`
- `sources/com/ikdong/weight/util/g.java:676`
  `java.util.Locale r0 = java.util.Locale.getDefault()     // Catch: java.lang.Exception -> L87`
- `sources/com/ikdong/weight/widget/a/ai.java:24`
  `private DateFormat f = DateFormat.getDateInstance(2, Locale.getDefault());`
- `sources/com/ikdong/weight/widget/b/c.java:71`
  `SimpleDateFormat simpleDateFormat = new SimpleDateFormat("yyyy-MM-dd", Locale.getDefault());`
- `sources/com/ikdong/weight/widget/fragment/BodyProgressFragment.java:618`
  `} else if (!com.ikdong.weight.util.g.a(BodyProgressFragment.this.getActivity(), ImageSyncUpService.class.getName()) && !FirebaseUtil.isLogin() && !Locale.getDefault().getCountry().equalsIgnoreCase(Locale.CHINA.getCountry())) {`
- `sources/com/ikdong/weight/widget/fragment/BodyProgressFragment.java:824`
  `} else if (!com.ikdong.weight.util.g.a(BodyProgressFragment.this.getActivity(), ImageSyncUpService.class.getName()) && !FirebaseUtil.isLogin() && !Locale.getDefault().getCountry().equalsIgnoreCase(Locale.CHINA.getCountry())) {`
- `sources/org/joda/time/chrono/BuddhistChronology.java:43`
  `org.joda.time.DateTimeZone r14 = org.joda.time.DateTimeZone.getDefault()     // Catch: java.lang.Throwable -> L3c`
- `sources/org/joda/time/chrono/CopticChronology.java:54`
  `dateTimeZone = DateTimeZone.getDefault();`
- `sources/org/joda/time/chrono/EthiopicChronology.java:54`
  `dateTimeZone = DateTimeZone.getDefault();`
- `sources/org/joda/time/chrono/GregorianChronology.java:66`
  `dateTimeZone = DateTimeZone.getDefault();`
- `sources/org/joda/time/chrono/IslamicChronology.java:96`
  `dateTimeZone = DateTimeZone.getDefault();`
- `sources/org/joda/time/chrono/JulianChronology.java:83`
  `dateTimeZone = DateTimeZone.getDefault();`
- `sources/org/joda/time/chrono/ZonedChronology.java:55`
  `dateTimeZone = DateTimeZone.getDefault();`
- `sources/org/joda/time/format/DateTimeFormat.java:368`
  `locale = Locale.getDefault();`

## BR016

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/AndroidManifest.xml:67`
  `android:name="com.google.android.backup.api_key"`
- `resources/res/values/public.xml:6281`
  `<public type="string" name="google_api_key" id="0x7f100076" />`
- `resources/res/values/public.xml:6283`
  `<public type="string" name="google_crash_reporting_api_key" id="0x7f100078" />`
- `resources/res/values/strings.xml:121`
  `<string name="google_api_key">AIzaSyBIvij7YSxShpurbdCkLo_BVEN4m999JRM</string>`
- `resources/res/values/strings.xml:123`
  `<string name="google_crash_reporting_api_key">AIzaSyBIvij7YSxShpurbdCkLo_BVEN4m999JRM</string>`
- `sources/com/google/android/gms/auth/api/proxy/ProxyClient.java:8`
  `public interface ProxyClient extends HasApiKey<AuthProxyOptions> {`
- `sources/com/google/android/gms/auth/api/signin/GoogleSignInOptions.java:205`
  `return new GoogleSignInOptions(3, (ArrayList<Scope>) new ArrayList(hashSet), !TextUtils.isEmpty(strOptString) ? new Account(strOptString, "com.google") : null, jSONObject.getBoolean("idTokenRequested"), jSONObject.getBoolean("serverAuthRequested"), jSONObject.getBoolean("forceCodeForRefreshToken"), ...`
- `sources/com/google/android/gms/auth/api/signin/GoogleSignInOptions.java:386`
  `jSONObject.put("forceCodeForRefreshToken", this.zal);`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:55`
  `public static final Task<Map<ApiKey<?>, String>> zai(HasApiKey<?> hasApiKey, HasApiKey<?>... hasApiKeyArr) {`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:56`
  `Preconditions.checkNotNull(hasApiKey, "Requested API must not be null.");`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:57`
  `for (HasApiKey<?> hasApiKey2 : hasApiKeyArr) {`
- `sources/com/google/android/gms/common/GoogleApiAvailability.java:58`
  `Preconditions.checkNotNull(hasApiKey2, "Requested API must not be null.");`
- `sources/com/google/android/gms/common/api/internal/zaae.java:21`
  `public static void zad(Activity activity, GoogleApiManager googleApiManager, ApiKey<?> apiKey) {`
- `sources/com/google/android/gms/internal/ads/zzbnd.java:5`
  `public static final zzbml<String> zza = zzbml.zzc("gads:safe_browsing:api_key", "AIzaSyDRKQ9d6kfsoZT2lUnZcZnBYvH69HExNPE");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zztk.java:31`
  `String strCheckNotEmpty = Preconditions.checkNotEmpty(intent.getStringExtra("com.google.firebase.auth.KEY_API_KEY"));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzvs.java:5`
  `REFRESH_TOKEN("refresh_token"),`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzwv.java:32`
  `this.zzi = Strings.emptyToNull(jSONObject.optString("refreshToken", null));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzxg.java:40`
  `this.zzd = Strings.emptyToNull(jSONObject.optString("refreshToken", null));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzxg.java:49`
  `this.zzm = jSONObject.optString("oauthAccessToken", null);`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzxl.java:31`
  `this.zzg = Strings.emptyToNull(jSONObject.optString("refreshToken", null));`
- `sources/com/google/android/gms/internal/safetynet/zzl.java:27`
  `strZzb = zzxVar.zzb("com.google.android.safetynet.ATTEST_API_KEY");`
- `sources/com/google/android/gms/internal/safetynet/zzx.java:50`
  `str2 = zzb("com.google.android.safetynet.API_KEY");`
- `sources/com/google/android/gms/safetynet/SafetyNetStatusCodes.java:18`
  `public static final int SAFE_BROWSING_MISSING_API_KEY = 12001;`
- `sources/com/google/android/gms/search/GoogleNowAuthState.java:56`
  `SafeParcelWriter.writeString(parcel, 2, getAccessToken(), false);`
- `sources/com/google/android/gms/signin/internal/SignInClientImpl.java:49`
  `bundle.putBoolean("com.google.android.gms.signin.internal.forceCodeForRefreshToken", false);`
- `sources/com/google/android/gms/signin/internal/SignInClientImpl.java:52`
  `bundle.putBoolean("com.google.android.gms.signin.internal.waitForAccessTokenRefresh", false);`
- `sources/com/google/firebase/FirebaseError.java:11`
  `public static final int ERROR_INVALID_API_KEY = 17023;`
- `sources/com/google/firebase/FirebaseOptions.java:12`
  `private static final String API_KEY_RESOURCE_NAME = "google_api_key";`
- `sources/com/google/firebase/FirebaseOptions.java:19`
  `private final String apiKey;`
- `sources/com/google/firebase/FirebaseOptions.java:28`
  `private String apiKey;`
- `sources/com/google/firebase/auth/OAuthProvider.java:32`
  `bundle.putString("com.google.firebase.auth.KEY_API_KEY", firebaseAuth.getApp().getOptions().getApiKey());`
- `sources/com/google/firebase/auth/internal/GenericIdpActivity.java:114`
  `zzf(zzg(Uri.parse(zzvf.zza(firebaseApp.getOptions().getApiKey())).buildUpon(), getIntent(), packageName, lowerCase).build(), packageName);`
- `sources/com/google/firebase/auth/internal/GenericIdpActivity.java:237`
  `String stringExtra = intent.getStringExtra("com.google.firebase.auth.KEY_API_KEY");`
- `sources/com/google/firebase/auth/internal/GenericIdpActivity.java:276`
  `builder.appendQueryParameter("eid", "p").appendQueryParameter("v", "X".concat(String.valueOf(stringExtra5))).appendQueryParameter("authType", "signInWithRedirect").appendQueryParameter("apiKey", stringExtra).appendQueryParameter("providerId", stringExtra2).appendQueryParameter("sessionId", strZza).a...`
- `sources/com/google/firebase/auth/internal/RecaptchaActivity.java:161`
  `String stringExtra = intent.getStringExtra("com.google.firebase.auth.KEY_API_KEY");`
- `sources/com/google/firebase/auth/internal/RecaptchaActivity.java:170`
  `return new Uri.Builder().scheme("https").appendPath("__").appendPath("auth").appendPath("handler").appendQueryParameter("apiKey", stringExtra).appendQueryParameter("authType", "verifyApp").appendQueryParameter("apn", str).appendQueryParameter("hl", !TextUtils.isEmpty(firebaseAuth.getLanguageCode()) ...`
- `sources/com/google/firebase/auth/internal/zzf.java:43`
  `intent.putExtra("com.google.firebase.auth.KEY_API_KEY", firebaseAuth.getApp().getOptions().getApiKey());`
- `sources/com/google/firebase/installations/FirebaseInstallations.java:37`
  `private static final String API_KEY_VALIDATION_MSG = "Please set a valid API key. A Firebase API key is required to communicate with Firebase server APIs: It authenticates your project with Google.Please refer to https://firebase.google.com/support/privacy/init-options.";`
- `sources/com/google/firebase/installations/Utils.java:16`
  `private static final Pattern API_KEY_FORMAT = Pattern.compile("\\AA[\\w-]{38}\\z");`
- `sources/com/google/firebase/installations/local/PersistedInstallation.java:19`
  `private static final String REFRESH_TOKEN_KEY = "RefreshToken";`
- `sources/com/google/firebase/installations/remote/AutoValue_InstallationResponse.java:102`
  `private String refreshToken;`
- `sources/com/google/firebase/installations/remote/FirebaseInstallationServiceClient.java:37`
  `private static final String API_KEY_HEADER = "x-goog-api-key";`
- `sources/com/google/firebase/installations/remote/FirebaseInstallationServiceClient.java:294`
  `httpURLConnection.addRequestProperty(API_KEY_HEADER, str);`
- `sources/com/ikdong/weight/R.java:6330`
  `public static final int google_api_key = 0x7f100076;`
- `sources/com/ikdong/weight/R.java:6332`
  `public static final int google_crash_reporting_api_key = 0x7f100078;`
- `sources/com/ikdong/weight/activity/FitBitActivity.java:125`
  `FitBitActivity.this.f1430a = (String) map.get("access_token");`
- `sources/com/ikdong/weight/activity/FitBitActivity.java:127`
  `g.a(fitBitActivity, "PARAM_FITBIT_ACCESS_TOKEN", fitBitActivity.f1430a);`
- `sources/com/ikdong/weight/activity/SyncFitbitActivity.java:337`
  `SyncFitbitActivity.this.e = (String) map.get("access_token");`
- `sources/com/ikdong/weight/activity/SyncFitbitActivity.java:340`
  `g.a(syncFitbitActivity, "PARAM_FITBIT_ACCESS_TOKEN", syncFitbitActivity.e);`
- `sources/com/ikdong/weight/activity/WithingsActivity.java:211`
  `}).build().newCall(new Request.Builder().url("https://oauth.withings.com/account/access_token?oauth_consumer_key=b2b08ef18d12b914de993c8bd2bebefb290863fd3d3c07bffccfcf7c26&oauth_nonce=" + strValueOf + "&oauth_signature=" + URLEncoder.encode(a("GET&https%3A%2F%2Foauth.withings.com%2Faccount%2Faccess_...`
- `sources/com/ikdong/weight/integration/withings/a/b.java:52`
  `}).build().newCall(new Request.Builder().url(String.format("https://wbsapi.withings.net/v2/oauth2?action=requesttoken&grant_type=authorization_code&client_id=4b108fd2097473b45a9ad20ea544983848a31816e78af6dfa147dbb9b2cff984&client_secret=ac86a69e2326d751f17d8287cfc53f0f23b359b47266757ae694dd972a45732...`
- `sources/com/ikdong/weight/integration/withings/a/b.java:104`
  `if (withingsTokenA != null && withingsTokenA.body != null && !TextUtils.isEmpty(withingsTokenA.body.access_token) && withingsTokenA.body.expires_in > 0) {`
- `sources/com/ikdong/weight/util/g.java:640`
  `String strB = b(context, "PARAM_FITBIT_ACCESS_TOKEN", "");`
- `sources/com/ikdong/weight/util/g.java:648`
  `a(context, "PARAM_FITBIT_ACCESS_TOKEN", "");`

## BR017

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `sources/com/bumptech/glide/g/a.java:4`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/g/a.java:13`
  `public void a(MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/g/b.java:35`
  `public void a(MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/g/b.java:36`
  `messageDigest.update(this.f280b.toString().getBytes(f779a));`
- `sources/com/bumptech/glide/load/g.java:4`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/g.java:12`
  `void a(MessageDigest messageDigest);`
- `sources/com/bumptech/glide/load/h.java:3`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/h.java:11`
  `public void a(byte[] bArr, Object obj, MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/h.java:51`
  `public void a(T t, MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/h.java:52`
  `this.f782c.a(b(), t, messageDigest);`
- `sources/com/bumptech/glide/load/b/x.java:4`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/b/b/j.java:55`
  `final MessageDigest f443a;`
- `sources/com/bumptech/glide/load/c/g.java:81`
  `public void a(MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/c/g.java:82`
  `messageDigest.update(f());`
- `sources/com/bumptech/glide/load/d/c.java:6`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/d/a/i.java:4`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/d/a/j.java:4`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/d/a/q.java:4`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/d/a/z.java:12`
  `import java.security.MessageDigest;`
- `sources/com/bumptech/glide/load/d/a/z.java:24`
  `public void a(byte[] bArr, Long l, MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/d/a/z.java:28`
  `messageDigest.update(this.f730a.putLong(l.longValue()).array());`
- `sources/com/bumptech/glide/load/d/a/z.java:40`
  `public void a(byte[] bArr, Integer num, MessageDigest messageDigest) {`
- `sources/com/bumptech/glide/load/d/a/z.java:47`
  `messageDigest.update(this.f731a.putInt(num.intValue()).array());`
- `sources/com/google/android/gms/common/zzm.java:74`
  `Preconditions.checkNotNull(messageDigestZza);`
- `sources/com/google/android/gms/common/zzm.java:75`
  `return String.format("%s: pkg=%s, sha1=%s, atk=%s, ver=%s", str2, str, Hex.bytesToStringLowercase(messageDigestZza.digest(zziVar.zzf())), Boolean.valueOf(z), "12451000.false");`
- `sources/com/google/android/gms/internal/ads/zzacl.java:95`
  `java.lang.String r6 = "'. Assuming AES-CTR crypto mode."`
- `sources/com/google/android/gms/internal/ads/zzafy.java:540`
  `MessageDigest[] messageDigestArr = new MessageDigest[length];`
- `sources/com/google/android/gms/internal/ads/zzafy.java:544`
  `messageDigestArr[i6] = MessageDigest.getInstance(strZzd);`
- `sources/com/google/android/gms/internal/ads/zzafy.java:617`
  `bArr6[i13] = MessageDigest.getInstance(strZzd2).digest(bArr7);`
- `sources/com/google/android/gms/internal/ads/zzaki.java:17`
  `private static MessageDigest zzc;`
- `sources/com/google/android/gms/internal/ads/zzaly.java:12`
  `import javax.crypto.spec.IvParameterSpec;`
- `sources/com/google/android/gms/internal/ads/zzaly.java:13`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/google/android/gms/internal/ads/zzaly.java:28`
  `zza = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/google/android/gms/internal/ads/zzaly.java:82`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(bArr, "AES");`
- `sources/com/google/android/gms/internal/ads/zzaly.java:84`
  `zzc().init(2, secretKeySpec, new IvParameterSpec(bArr2));`
- `sources/com/google/android/gms/internal/ads/zzazg.java:46`
  `MessageDigest messageDigest = this.zzb;`
- `sources/com/google/android/gms/internal/ads/zzazg.java:47`
  `if (messageDigest == null) {`
- `sources/com/google/android/gms/internal/ads/zzazg.java:50`
  `messageDigest.reset();`
- `sources/com/google/android/gms/internal/ads/zzazk.java:23`
  `MessageDigest messageDigestZza = zza();`
- `sources/com/google/android/gms/internal/ads/zzazk.java:24`
  `this.zzb = messageDigestZza;`
- `sources/com/google/android/gms/internal/ads/zzazk.java:25`
  `if (messageDigestZza == null) {`
- `sources/com/google/android/gms/internal/ads/zzazk.java:28`
  `messageDigestZza.reset();`
- `sources/com/google/android/gms/internal/ads/zzcis.java:85`
  `MessageDigest messageDigest = MessageDigest.getInstance("MD5");`
- `sources/com/google/android/gms/internal/ads/zzcis.java:86`
  `messageDigest.update(byteArray);`
- `sources/com/google/android/gms/internal/ads/zzcis.java:87`
  `messageDigest.update(byteArray2);`
- `sources/com/google/android/gms/internal/ads/zzcis.java:89`
  `System.arraycopy(messageDigest.digest(), 0, bArr, 0, 8);`
- `sources/com/google/android/gms/internal/ads/zzcis.java:100`
  `MessageDigest messageDigest = MessageDigest.getInstance("MD5");`
- `sources/com/google/android/gms/internal/ads/zzcis.java:101`
  `messageDigest.update(str.getBytes());`
- `sources/com/google/android/gms/internal/ads/zzcis.java:102`
  `return String.format(Locale.US, "%032X", new BigInteger(1, messageDigest.digest()));`
- `sources/com/google/android/gms/internal/ads/zzfmc.java:7`
  `import java.security.MessageDigest;`
- `sources/com/google/android/gms/internal/ads/zzgai.java:13`
  `return zzghp.zza.zza("AES/GCM-SIV/NoPadding");`
- `sources/com/google/android/gms/internal/ads/zzgaj.java:9`
  `import javax.crypto.spec.IvParameterSpec;`
- `sources/com/google/android/gms/internal/ads/zzgaj.java:10`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/google/android/gms/internal/ads/zzgaj.java:19`
  `this.zzb = new SecretKeySpec(bArr, "AES");`
- `sources/com/google/android/gms/internal/ads/zzgaj.java:24`
  `AlgorithmParameterSpec ivParameterSpec;`
- `sources/com/google/android/gms/internal/ads/zzgaj.java:35`
  `ivParameterSpec = new GCMParameterSpec(128, bArrZza, 0, length2);`
- `sources/com/google/android/gms/internal/ads/zzggt.java:13`
  `return zzghp.zza.zza("AES/CTR/NoPadding");`
- `sources/com/google/android/gms/internal/ads/zzggu.java:5`
  `import javax.crypto.spec.IvParameterSpec;`
- `sources/com/google/android/gms/internal/ads/zzggu.java:6`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/google/android/gms/internal/ads/zzggu.java:11`
  `private final SecretKeySpec zzb;`
- `sources/com/google/android/gms/internal/ads/zzggu.java:47`
  `cipher.init(1, this.zzb, new IvParameterSpec(bArr3));`
- `sources/com/google/android/gms/internal/ads/zzggv.java:13`
  `return zzghp.zza.zza("AES/ECB/NOPADDING");`
- `sources/com/google/android/gms/internal/ads/zzggw.java:13`
  `return zzghp.zza.zza("AES/CTR/NOPADDING");`
- `sources/com/google/android/gms/internal/ads/zzggx.java:8`
  `import javax.crypto.spec.IvParameterSpec;`
- `sources/com/google/android/gms/internal/ads/zzggx.java:9`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/google/android/gms/internal/ads/zzggx.java:17`
  `private final SecretKeySpec zze;`
- `sources/com/google/android/gms/internal/ads/zzggx.java:29`
  `SecretKeySpec secretKeySpec = new SecretKeySpec(bArr, "AES");`
- `sources/com/google/android/gms/internal/ads/zzggx.java:30`
  `this.zze = secretKeySpec;`
- `sources/com/google/android/gms/internal/ads/zzggx.java:32`
  `cipher.init(1, secretKeySpec);`
- `sources/com/google/android/gms/internal/ads/zzggy.java:13`
  `return zzghp.zza.zza("AES/GCM/NoPadding");`
- `sources/com/google/android/gms/internal/ads/zzggz.java:8`
  `import javax.crypto.spec.IvParameterSpec;`
- `sources/com/google/android/gms/internal/ads/zzggz.java:9`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/google/android/gms/internal/ads/zzggz.java:18`
  `throw new GeneralSecurityException("Can not use AES-GCM in FIPS-mode, as BoringCrypto module is not available.");`
- `sources/com/google/android/gms/internal/ads/zzggz.java:34`
  `AlgorithmParameterSpec gCMParameterSpec = (!zzgih.zzb() || zzgih.zza() > 19) ? new GCMParameterSpec(128, bArrZza, 0, length2) : new IvParameterSpec(bArrZza, 0, length2);`
- `sources/com/google/android/gms/internal/ads/zzgha.java:8`
  `import javax.crypto.spec.IvParameterSpec;`
- `sources/com/google/android/gms/internal/ads/zzgha.java:9`
  `import javax.crypto.spec.SecretKeySpec;`
- `sources/com/google/android/gms/internal/ads/zzgha.java:20`
  `throw new GeneralSecurityException("Can not use AES-SIV in FIPS-mode.");`
- `sources/com/google/android/gms/internal/ads/zzgha.java:44`
  `Cipher cipherZza = zzghp.zza.zza("AES/CTR/NoPadding");`
- `sources/com/google/android/gms/internal/ads/zzghm.java:179`
  `macZza.init(new SecretKeySpec(new byte[macZza.getMacLength()], str));`
- `sources/com/google/android/gms/internal/ads/zzghm.java:181`
  `macZza.init(new SecretKeySpec(bArr, str));`

## BR018

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:35`
  `int columnIndex4 = CursorUtil.getColumnIndex(cursorQuery, "run_attempt_count");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:76`
  `workInfoPojo.runAttemptCount = cursorQuery.getInt(columnIndex4);`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:99`
  `int columnIndex4 = CursorUtil.getColumnIndex(cursorQuery, "run_attempt_count");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:140`
  `workInfoPojo.runAttemptCount = cursorQuery.getInt(columnIndex4);`
- `sources/androidx/work/impl/model/WorkSpec.java:49`
  `public int runAttemptCount;`
- `sources/androidx/work/impl/model/WorkSpec.java:86`
  `this.runAttemptCount = workSpec.runAttemptCount;`
- `sources/androidx/work/impl/model/WorkSpec.java:113`
  `return this.state == WorkInfo.State.ENQUEUED && this.runAttemptCount > 0;`
- `sources/androidx/work/impl/model/WorkSpec.java:145`
  `jScalb = this.backoffDelayDuration * ((long) this.runAttemptCount);`
- `sources/androidx/work/impl/model/WorkSpec.java:147`
  `jScalb = (long) Math.scalb(this.backoffDelayDuration, this.runAttemptCount - 1);`
- `sources/androidx/work/impl/model/WorkSpec.java:181`
  `if (this.initialDelay != workSpec.initialDelay || this.intervalDuration != workSpec.intervalDuration || this.flexDuration != workSpec.flexDuration || this.runAttemptCount != workSpec.runAttemptCount || this.backoffDelayDuration != workSpec.backoffDelayDuration || this.periodStartTime != workSpec.per...`
- `sources/androidx/work/impl/model/WorkSpec.java:200`
  `int iHashCode3 = (((((((i2 + ((int) (j3 ^ (j3 >>> 32)))) * 31) + this.constraints.hashCode()) * 31) + this.runAttemptCount) * 31) + this.backoffPolicy.hashCode()) * 31;`
- `sources/androidx/work/impl/model/WorkSpec.java:242`
  `public int runAttemptCount;`
- `sources/androidx/work/impl/model/WorkSpec.java:254`
  `return new WorkInfo(UUID.fromString(this.id), this.state, this.output, this.tags, data, this.runAttemptCount);`
- `sources/androidx/work/impl/model/WorkSpec.java:265`
  `if (this.runAttemptCount != workInfoPojo.runAttemptCount) {`
- `sources/androidx/work/impl/model/WorkSpec.java:294`
  `int iHashCode3 = (((iHashCode2 + (data != null ? data.hashCode() : 0)) * 31) + this.runAttemptCount) * 31;`
- `sources/androidx/work/impl/model/WorkSpecDao.java:45`
  `WorkSpec.WorkInfoPojo getWorkStatusPojoForId(String str);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:47`
  `List<WorkSpec.WorkInfoPojo> getWorkStatusPojoForIds(List<String> list);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:49`
  `List<WorkSpec.WorkInfoPojo> getWorkStatusPojoForName(String str);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:51`
  `List<WorkSpec.WorkInfoPojo> getWorkStatusPojoForTag(String str);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:53`
  `LiveData<List<WorkSpec.WorkInfoPojo>> getWorkStatusPojoLiveDataForIds(List<String> list);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:55`
  `LiveData<List<WorkSpec.WorkInfoPojo>> getWorkStatusPojoLiveDataForName(String str);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:57`
  `LiveData<List<WorkSpec.WorkInfoPojo>> getWorkStatusPojoLiveDataForTag(String str);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:61`
  `int incrementWorkSpecRunAttemptCount(String str);`
- `sources/androidx/work/impl/model/WorkSpecDao.java:71`
  `int resetWorkSpecRunAttemptCount(String str);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:28`
  `private final SharedSQLiteStatement __preparedStmtOfIncrementWorkSpecRunAttemptCount;`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:32`
  `private final SharedSQLiteStatement __preparedStmtOfResetWorkSpecRunAttemptCount;`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:41`
  `return "INSERT OR IGNORE INTO 'WorkSpec' ('id','state','worker_class_name','input_merger_class_name','input','output','initial_delay','interval_duration','flex_duration','run_attempt_count','backoff_policy','backoff_delay_duration','period_start_time','minimum_retention_duration','schedule_requested...`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:77`
  `supportSQLiteStatement.bindLong(10, workSpec.runAttemptCount);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:131`
  `this.__preparedStmtOfIncrementWorkSpecRunAttemptCount = new SharedSQLiteStatement(roomDatabase) { // from class: androidx.work.impl.model.WorkSpecDao_Impl.5`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:134`
  `return "UPDATE workspec SET run_attempt_count=run_attempt_count+1 WHERE id=?";`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:137`
  `this.__preparedStmtOfResetWorkSpecRunAttemptCount = new SharedSQLiteStatement(roomDatabase) { // from class: androidx.work.impl.model.WorkSpecDao_Impl.6`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:140`
  `return "UPDATE workspec SET run_attempt_count=0 WHERE id=?";`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:240`
  `public int incrementWorkSpecRunAttemptCount(String str) {`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:242`
  `SupportSQLiteStatement supportSQLiteStatementAcquire = this.__preparedStmtOfIncrementWorkSpecRunAttemptCount.acquire();`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:255`
  `this.__preparedStmtOfIncrementWorkSpecRunAttemptCount.release(supportSQLiteStatementAcquire);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:260`
  `public int resetWorkSpecRunAttemptCount(String str) {`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:262`
  `SupportSQLiteStatement supportSQLiteStatementAcquire = this.__preparedStmtOfResetWorkSpecRunAttemptCount.acquire();`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:275`
  `this.__preparedStmtOfResetWorkSpecRunAttemptCount.release(supportSQLiteStatementAcquire);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:347`
  `RoomSQLiteQuery roomSQLiteQueryAcquire = RoomSQLiteQuery.acquire("SELECT 'required_network_type', 'requires_charging', 'requires_device_idle', 'requires_battery_not_low', 'requires_storage_not_low', 'trigger_content_update_delay', 'trigger_max_content_delay', 'content_uri_triggers', 'WorkSpec'.'id' ...`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:379`
  `int columnIndexOrThrow18 = CursorUtil.getColumnIndexOrThrow(cursorQuery, "run_attempt_count");`

## BR019

paper_id: B011
paper_title: Locking it down: The privacy and security of mobile medication apps

- `sources/androidx/appcompat/widget/ActivityChooserModel.java:387`
  `map.put(new ComponentName(activityResolveInfo.resolveInfo.activityInfo.packageName, activityResolveInfo.resolveInfo.activityInfo.name), activityResolveInfo);`
- `sources/androidx/coordinatorlayout/widget/DirectedAcyclicGraph.java:34`
  `this.mGraph.put(t, emptyList);`
- `sources/androidx/core/graphics/TypefaceCompatApi24Impl.java:102`
  `simpleArrayMap.put(uri, byteBufferMmap);`
- `sources/androidx/core/location/LocationManagerCompat.java:304`
  `LocationManagerCompat.sLocationListeners.put(this.mListener, arrayList);`
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
- `sources/androidx/transition/VisibilityPropagation.java:25`
  `transitionValues.values.put(PROPNAME_VIEW_CENTER, iArr);`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:140`
  `map2.put("initial_delay", new TableInfo.Column("initial_delay", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:141`
  `map2.put("interval_duration", new TableInfo.Column("interval_duration", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:142`
  `map2.put("flex_duration", new TableInfo.Column("flex_duration", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:143`
  `map2.put("run_attempt_count", new TableInfo.Column("run_attempt_count", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:144`
  `map2.put("backoff_policy", new TableInfo.Column("backoff_policy", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:145`
  `map2.put("backoff_delay_duration", new TableInfo.Column("backoff_delay_duration", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:146`
  `map2.put("period_start_time", new TableInfo.Column("period_start_time", "INTEGER", true, 0, null, 1));`
- `sources/com/google/android/gms/ads/AdapterResponseInfo.java:7`
  `import org.json.JSONObject;`
- `sources/com/google/android/gms/ads/LoadAdError.java:34`
  `public final JSONObject zzb() throws JSONException {`
- `sources/com/google/android/gms/ads/LoadAdError.java:35`
  `JSONObject jSONObjectZzb = super.zzb();`
- `sources/com/google/android/gms/ads/LoadAdError.java:38`
  `jSONObjectZzb.put("Response Info", "null");`
- `sources/com/google/android/gms/ads/LoadAdError.java:40`
  `jSONObjectZzb.put("Response Info", responseInfo.zzc());`
- `sources/com/google/android/gms/ads/LoadAdError.java:42`
  `return jSONObjectZzb;`
- `sources/com/google/android/gms/ads/ResponseInfo.java:14`
  `import org.json.JSONObject;`
- `sources/com/google/android/gms/ads/ResponseInfo.java:91`
  `public final JSONObject zzc() throws JSONException {`
- `sources/com/google/android/gms/ads/ResponseInfo.java:92`
  `JSONObject jSONObject = new JSONObject();`
- `sources/com/google/android/gms/ads/ResponseInfo.java:95`
  `jSONObject.put("Response ID", "null");`
- `sources/com/google/android/gms/ads/ResponseInfo.java:97`
  `jSONObject.put("Response ID", responseId);`
- `sources/com/google/android/gms/ads/ResponseInfo.java:103`
  `jSONObject.put("Mediation Adapter Class Name", mediationAdapterClassName);`
- `sources/com/google/android/gms/ads/ResponseInfo.java:108`
  `jSONArray.put(it.next().zzb());`
- `sources/com/google/android/gms/ads/ResponseInfo.java:110`
  `jSONObject.put("Adapter Responses", jSONArray);`
- `sources/com/google/android/gms/ads/ResponseInfo.java:111`
  `return jSONObject;`
- `sources/com/google/android/gms/ads/internal/util/zzcb.java:90`
  `JSONObject jSONObject6 = jSONObject3;`
- `sources/com/google/android/gms/ads/internal/util/zzcb.java:92`
  `jSONObject5.put("width", zzbgo.zzb().zzb(context, view2.getMeasuredWidth()));`
- `sources/com/google/android/gms/ads/internal/util/zzcb.java:93`
  `jSONObject5.put("height", zzbgo.zzb().zzb(context, view2.getMeasuredHeight()));`
- `sources/com/google/android/gms/ads/internal/util/zzcb.java:94`
  `jSONObject5.put("x", zzbgo.zzb().zzb(context, iArrZzj2[0] - iArrZzj[0]));`
- `sources/com/google/android/gms/ads/internal/util/zzcb.java:95`
  `jSONObject5.put("y", zzbgo.zzb().zzb(context, iArrZzj2[1] - iArrZzj[1]));`

## BR020

paper_id: B012
paper_title: Reviewing the data security and privacy policies of mobile apps for depression

- `sources/androidx/appcompat/widget/SearchView.java:94`
  `CursorAdapter mSuggestionsAdapter;`
- `sources/androidx/core/provider/FontProvider.java:84`
  `Cursor cursorQuery = null;`
- `sources/androidx/core/provider/FontProvider.java:88`
  `cursorQuery = context.getContentResolver().query(uriBuild, strArr, "query = ?", new String[]{fontRequest.getQuery()}, null, cancellationSignal);`
- `sources/androidx/core/provider/FontProvider.java:90`
  `cursorQuery = context.getContentResolver().query(uriBuild, strArr, "query = ?", new String[]{fontRequest.getQuery()}, null);`
- `sources/androidx/core/provider/FontProvider.java:93`
  `int columnIndex = cursorQuery.getColumnIndex(FontsContractCompat.Columns.RESULT_CODE);`
- `sources/androidx/core/provider/FontProvider.java:95`
  `int columnIndex2 = cursorQuery.getColumnIndex("_id");`
- `sources/androidx/core/provider/FontProvider.java:96`
  `int columnIndex3 = cursorQuery.getColumnIndex(FontsContractCompat.Columns.FILE_ID);`
- `sources/androidx/core/provider/FontProvider.java:97`
  `int columnIndex4 = cursorQuery.getColumnIndex(FontsContractCompat.Columns.TTC_INDEX);`
- `sources/androidx/core/provider/FontProvider.java:98`
  `int columnIndex5 = cursorQuery.getColumnIndex(FontsContractCompat.Columns.WEIGHT);`
- `sources/androidx/core/provider/FontProvider.java:99`
  `int columnIndex6 = cursorQuery.getColumnIndex(FontsContractCompat.Columns.ITALIC);`
- `sources/androidx/core/provider/FontProvider.java:100`
  `while (cursorQuery.moveToNext()) {`
- `sources/androidx/core/provider/FontProvider.java:101`
  `int i2 = columnIndex != -1 ? cursorQuery.getInt(columnIndex) : 0;`
- `sources/androidx/core/provider/FontProvider.java:102`
  `int i3 = columnIndex4 != -1 ? cursorQuery.getInt(columnIndex4) : 0;`
- `sources/androidx/room/InvalidationTracker.java:29`
  `static final String RESET_UPDATED_TABLES_SQL = "UPDATE room_table_modification_log SET invalidated = 0 WHERE invalidated = 1 ";`
- `sources/androidx/room/InvalidationTracker.java:152`
  `supportSQLiteDatabase.execSQL("PRAGMA temp_store = MEMORY;");`
- `sources/androidx/room/InvalidationTracker.java:153`
  `supportSQLiteDatabase.execSQL("PRAGMA recursive_triggers='ON';");`
- `sources/androidx/room/InvalidationTracker.java:154`
  `supportSQLiteDatabase.execSQL(CREATE_TRACKING_TABLE_SQL);`
- `sources/androidx/room/InvalidationTracker.java:194`
  `supportSQLiteDatabase.execSQL("INSERT OR IGNORE INTO room_table_modification_log VALUES(" + i + ", 0)");`
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
- `sources/androidx/work/impl/WorkDatabase_Impl.java:55`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'Dependency' ('work_spec_id' TEXT NOT NULL, 'prerequisite_id' TEXT NOT NULL, PRIMARY KEY('work_spec_id', 'prerequisite_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE , FOREIGN KEY('prerequisi...`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:56`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_Dependency_work_spec_id' ON 'Dependency' ('work_spec_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:57`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_Dependency_prerequisite_id' ON 'Dependency' ('prerequisite_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:58`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'WorkSpec' ('id' TEXT NOT NULL, 'state' INTEGER NOT NULL, 'worker_class_name' TEXT NOT NULL, 'input_merger_class_name' TEXT, 'input' BLOB NOT NULL, 'output' BLOB NOT NULL, 'initial_delay' INTEGER NOT NULL, 'interval_duration' INTEGER NOT NULL...`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:59`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkSpec_schedule_requested_at' ON 'WorkSpec' ('schedule_requested_at')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:60`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkSpec_period_start_time' ON 'WorkSpec' ('period_start_time')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:61`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'WorkTag' ('tag' TEXT NOT NULL, 'work_spec_id' TEXT NOT NULL, PRIMARY KEY('tag', 'work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:62`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkTag_work_spec_id' ON 'WorkTag' ('work_spec_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:63`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'SystemIdInfo' ('work_spec_id' TEXT NOT NULL, 'system_id' INTEGER NOT NULL, PRIMARY KEY('work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:30`
  `Cursor cursorQuery = DBUtil.query(this.__db, supportSQLiteQuery, true, null);`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:32`
  `int columnIndex = CursorUtil.getColumnIndex(cursorQuery, "id");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:33`
  `int columnIndex2 = CursorUtil.getColumnIndex(cursorQuery, "state");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:34`
  `int columnIndex3 = CursorUtil.getColumnIndex(cursorQuery, "output");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:35`
  `int columnIndex4 = CursorUtil.getColumnIndex(cursorQuery, "run_attempt_count");`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:38`
  `while (cursorQuery.moveToNext()) {`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:39`
  `if (!cursorQuery.isNull(columnIndex)) {`
- `sources/androidx/work/impl/model/RawWorkInfoDao_Impl.java:40`
  `String string = cursorQuery.getString(columnIndex);`

## BR021

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `resources/AndroidManifest.xml:75`
  `<provider`
- `resources/AndroidManifest.xml:84`
  `<provider`
- `resources/AndroidManifest.xml:749`
  `<provider`
- `resources/AndroidManifest.xml:836`
  `<provider`
- `resources/AndroidManifest.xml:855`
  `<provider`
- `resources/AndroidManifest.xml:864`
  `<provider`

## BR022

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `resources/res/xml/file_paths.xml:3`
  `<external-path`
- `resources/res/xml/nnf_provider_paths.xml:3`
  `<root-path`
- `resources/res/xml/provider_paths.xml:3`
  `<external-path`

## BR023

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `sources/androidx/core/content/FileProvider.java:24`
  `public class FileProvider extends ContentProvider {`
- `sources/androidx/startup/InitializationProvider.java:10`
  `public final class InitializationProvider extends ContentProvider {`
- `sources/com/google/android/gms/ads/MobileAdsInitProvider.java:12`
  `public class MobileAdsInitProvider extends ContentProvider {`
- `sources/com/google/android/gms/internal/ads/zzbjr.java:15`
  `public final class zzbjr extends ContentProvider {`
- `sources/com/google/android/gms/measurement/AppMeasurementContentProvider.java:14`
  `public class AppMeasurementContentProvider extends ContentProvider {`
- `sources/com/google/firebase/provider/FirebaseInitProvider.java:14`
  `public class FirebaseInitProvider extends ContentProvider {`

## BR024

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `sources/androidx/core/content/FileProvider.java:58`
  `if (!providerInfo.grantUriPermissions) {`

## BR025

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/androidx/room/InvalidationTracker.java:35`
  `final RoomDatabase mDatabase;`
- `sources/androidx/room/InvalidationTracker.java:146`
  `void internalInit(SupportSQLiteDatabase supportSQLiteDatabase) {`
- `sources/androidx/room/InvalidationTracker.java:152`
  `supportSQLiteDatabase.execSQL("PRAGMA temp_store = MEMORY;");`
- `sources/androidx/room/InvalidationTracker.java:153`
  `supportSQLiteDatabase.execSQL("PRAGMA recursive_triggers='ON';");`
- `sources/androidx/room/InvalidationTracker.java:154`
  `supportSQLiteDatabase.execSQL(CREATE_TRACKING_TABLE_SQL);`
- `sources/androidx/room/InvalidationTracker.java:155`
  `syncTriggers(supportSQLiteDatabase);`
- `sources/androidx/room/InvalidationTracker.java:156`
  `this.mCleanupStatement = supportSQLiteDatabase.compileStatement(RESET_UPDATED_TABLES_SQL);`
- `sources/androidx/room/InvalidationTracker.java:193`
  `private void startTrackingTable(SupportSQLiteDatabase supportSQLiteDatabase, int i) {`
- `sources/androidx/room/InvalidationTracker.java:194`
  `supportSQLiteDatabase.execSQL("INSERT OR IGNORE INTO room_table_modification_log VALUES(" + i + ", 0)");`
- `sources/androidx/room/util/FtsTableInfo.java:29`
  `return new FtsTableInfo(str, readColumns(supportSQLiteDatabase, str), readOptions(supportSQLiteDatabase, str));`
- `sources/androidx/room/util/FtsTableInfo.java:32`
  `private static Set<String> readColumns(SupportSQLiteDatabase supportSQLiteDatabase, String str) {`
- `sources/androidx/room/util/FtsTableInfo.java:33`
  `Cursor cursorQuery = supportSQLiteDatabase.query("PRAGMA table_info('" + str + "')");`
- `sources/androidx/room/util/TableInfo.java:130`
  `private static Map<String, Column> readColumns(SupportSQLiteDatabase supportSQLiteDatabase, String str) {`
- `sources/androidx/room/util/TableInfo.java:131`
  `Cursor cursorQuery = supportSQLiteDatabase.query("PRAGMA table_info('" + str + "')");`
- `sources/androidx/room/util/TableInfo.java:151`
  `private static Set<Index> readIndices(SupportSQLiteDatabase supportSQLiteDatabase, String str) {`
- `sources/androidx/room/util/TableInfo.java:152`
  `Cursor cursorQuery = supportSQLiteDatabase.query("PRAGMA index_list('" + str + "')");`
- `sources/androidx/room/util/TableInfo.java:181`
  `private static Index readIndex(SupportSQLiteDatabase supportSQLiteDatabase, String str, boolean z) {`
- `sources/androidx/room/util/TableInfo.java:182`
  `Cursor cursorQuery = supportSQLiteDatabase.query("PRAGMA index_xinfo('" + str + "')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:50`
  `public void onPostMigrate(SupportSQLiteDatabase supportSQLiteDatabase) {`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:54`
  `public void createAllTables(SupportSQLiteDatabase supportSQLiteDatabase) {`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:55`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'Dependency' ('work_spec_id' TEXT NOT NULL, 'prerequisite_id' TEXT NOT NULL, PRIMARY KEY('work_spec_id', 'prerequisite_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE , FOREIGN KEY('prerequisi...`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:56`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_Dependency_work_spec_id' ON 'Dependency' ('work_spec_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:57`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_Dependency_prerequisite_id' ON 'Dependency' ('prerequisite_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:58`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'WorkSpec' ('id' TEXT NOT NULL, 'state' INTEGER NOT NULL, 'worker_class_name' TEXT NOT NULL, 'input_merger_class_name' TEXT, 'input' BLOB NOT NULL, 'output' BLOB NOT NULL, 'initial_delay' INTEGER NOT NULL, 'interval_duration' INTEGER NOT NULL...`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:59`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkSpec_schedule_requested_at' ON 'WorkSpec' ('schedule_requested_at')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:60`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkSpec_period_start_time' ON 'WorkSpec' ('period_start_time')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:61`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'WorkTag' ('tag' TEXT NOT NULL, 'work_spec_id' TEXT NOT NULL, PRIMARY KEY('tag', 'work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:62`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkTag_work_spec_id' ON 'WorkTag' ('work_spec_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:63`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'SystemIdInfo' ('work_spec_id' TEXT NOT NULL, 'system_id' INTEGER NOT NULL, PRIMARY KEY('work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:64`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'WorkName' ('name' TEXT NOT NULL, 'work_spec_id' TEXT NOT NULL, PRIMARY KEY('name', 'work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:65`
  `supportSQLiteDatabase.execSQL("CREATE INDEX IF NOT EXISTS 'index_WorkName_work_spec_id' ON 'WorkName' ('work_spec_id')");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:66`
  `supportSQLiteDatabase.execSQL("CREATE TABLE IF NOT EXISTS 'WorkProgress' ('work_spec_id' TEXT NOT NULL, 'progress' BLOB NOT NULL, PRIMARY KEY('work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:186`
  `TableInfo tableInfo8 = TableInfo.read(supportSQLiteDatabase, "SystemIdInfo");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:198`
  `TableInfo tableInfo10 = TableInfo.read(supportSQLiteDatabase, "WorkName");`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:25`
  `private final RoomDatabase __db;`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:36`
  `public WorkSpecDao_Impl(RoomDatabase roomDatabase) {`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:37`
  `this.__db = roomDatabase;`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:38`
  `this.__insertionAdapterOfWorkSpec = new EntityInsertionAdapter<WorkSpec>(roomDatabase) { // from class: androidx.work.impl.model.WorkSpecDao_Impl.1`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:125`
  `this.__preparedStmtOfSetPeriodStartTime = new SharedSQLiteStatement(roomDatabase) { // from class: androidx.work.impl.model.WorkSpecDao_Impl.4`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:131`
  `this.__preparedStmtOfIncrementWorkSpecRunAttemptCount = new SharedSQLiteStatement(roomDatabase) { // from class: androidx.work.impl.model.WorkSpecDao_Impl.5`

## BR026

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/com/google/android/gms/ads/internal/util/zzcg.java:20`
  `SharedPreferences sharedPreferences = this.zza.getSharedPreferences("admob_user_agent", 0);`
- `sources/com/google/android/gms/ads/internal/util/zzcg.java:21`
  `String string = sharedPreferences.getString("user_agent", "");`
- `sources/com/google/android/gms/ads/internal/util/zzcg.java:28`
  `SharedPreferencesUtils.publishWorldReadableSharedPreferences(this.zza, sharedPreferences.edit().putString("user_agent", defaultUserAgent), "admob_user_agent");`
- `sources/com/google/android/gms/ads/internal/util/zzch.java:21`
  `SharedPreferences sharedPreferences;`
- `sources/com/google/android/gms/ads/internal/util/zzch.java:25`
  `sharedPreferences = this.zza.getSharedPreferences("admob_user_agent", 0);`
- `sources/com/google/android/gms/ads/internal/util/zzch.java:28`
  `sharedPreferences = this.zzb.getSharedPreferences("admob_user_agent", 0);`
- `sources/com/google/android/gms/ads/internal/util/zzch.java:31`
  `String string = sharedPreferences.getString("user_agent", "");`
- `sources/com/google/android/gms/ads/internal/util/zzch.java:36`
  `sharedPreferences.edit().putString("user_agent", string).apply();`
- `sources/com/google/android/gms/ads/internal/util/zzj.java:213`
  `SharedPreferences.Editor editor = this.zzg;`
- `sources/com/google/android/gms/ads/internal/util/zzj.java:679`
  `SharedPreferences.Editor editor = this.zzg;`
- `sources/com/google/android/gms/ads/internal/util/zzv.java:69`
  `android.content.SharedPreferences r4 = r8.getSharedPreferences(r5, r4)`
- `sources/com/google/android/gms/ads/internal/util/zzv.java:70`
  `android.content.SharedPreferences$Editor r4 = r4.edit()`
- `sources/com/google/android/gms/ads/internal/util/zzv.java:72`
  `android.content.SharedPreferences$Editor r3 = r4.putString(r6, r3)`
- `sources/com/google/android/gms/ads/internal/util/zzv.java:77`
  `com.google.android.gms.common.util.SharedPreferencesUtils.publishWorldReadableSharedPreferences(r8, r3, r5)`
- `sources/com/google/android/gms/internal/consent_sdk/zzl.java:75`
  `Object obj = application.getSharedPreferences(zzcbVarZza.zza, 0).getAll().get(zzcbVarZza.zzb);`
- `sources/com/google/firebase/auth/internal/RecaptchaActivity.java:139`
  `SharedPreferences.Editor editorEdit = getApplicationContext().getSharedPreferences("com.google.firebase.auth.internal.ProcessDeathHelper", 0).edit();`
- `sources/com/google/firebase/auth/internal/zzbg.java:4`
  `import android.content.SharedPreferences;`
- `sources/com/google/firebase/auth/internal/zzbm.java:59`
  `SharedPreferences.Editor editorEdit = context.getSharedPreferences("com.google.firebase.auth.internal.ProcessDeathHelper", 0).edit();`
- `sources/com/google/firebase/auth/internal/zzbm.java:68`
  `SharedPreferences.Editor editorEdit = context.getSharedPreferences("com.google.firebase.auth.internal.ProcessDeathHelper", 0).edit();`
- `sources/com/google/firebase/auth/internal/zzj.java:29`
  `private static final SharedPreferences zzg(Context context, String str) {`
- `sources/com/google/firebase/auth/internal/zzj.java:30`
  `return context.getSharedPreferences(String.format("com.google.firebase.auth.internal.browserSignInSessionStore.%s", str), 0);`
- `sources/com/google/firebase/auth/internal/zzj.java:36`
  `SharedPreferences sharedPreferencesZzg = zzg(context, str);`
- `sources/com/google/firebase/auth/internal/zzj.java:41`
  `String string = sharedPreferencesZzg.getString(str3, null);`
- `sources/com/google/firebase/auth/internal/zzj.java:42`
  `String string2 = sharedPreferencesZzg.getString(str4, null);`
- `sources/com/google/firebase/auth/internal/zzj.java:43`
  `String string3 = sharedPreferencesZzg.getString(str5, null);`
- `sources/com/google/firebase/auth/internal/zzj.java:83`
  `SharedPreferences sharedPreferencesZzg = zzg(context, str);`
- `sources/com/google/firebase/auth/internal/zzj.java:84`
  `zzf(sharedPreferencesZzg);`
- `sources/com/google/firebase/auth/internal/zzj.java:85`
  `SharedPreferences.Editor editorEdit = sharedPreferencesZzg.edit();`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:4`
  `import android.content.SharedPreferences;`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:27`
  `private final SharedPreferences firebaseSharedPreferences;`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:30`
  `this.firebaseSharedPreferences = context.getSharedPreferences(HEARTBEAT_PREFERENCES_NAME + str, 0);`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:33`
  `HeartBeatInfoStorage(SharedPreferences sharedPreferences) {`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:34`
  `this.firebaseSharedPreferences = sharedPreferences;`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:38`
  `return (int) this.firebaseSharedPreferences.getLong(HEART_BEAT_COUNT_TAG, 0L);`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:42`
  `SharedPreferences.Editor editorEdit = this.firebaseSharedPreferences.edit();`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:43`
  `for (Map.Entry<String, ?> entry : this.firebaseSharedPreferences.getAll().entrySet()) {`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:55`
  `for (Map.Entry<String, ?> entry : this.firebaseSharedPreferences.getAll().entrySet()) {`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:65`
  `for (Map.Entry<String, ?> entry : this.firebaseSharedPreferences.getAll().entrySet()) {`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:83`
  `HashSet hashSet = new HashSet(this.firebaseSharedPreferences.getStringSet(storedUserAgentString, new HashSet()));`
- `sources/com/google/firebase/heartbeatinfo/HeartBeatInfoStorage.java:86`
  `this.firebaseSharedPreferences.edit().remove(storedUserAgentString).commit();`

## BR027

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/androidx/core/content/ContextCompat.java:173`
  `return createFilesDir(new File(context.getApplicationInfo().dataDir, "no_backup"));`
- `sources/androidx/core/graphics/drawable/IconCompat.java:440`
  `return new FileInputStream(new File((String) this.mObj1));`
- `sources/androidx/core/os/EnvironmentCompat.java:22`
  `return file.getCanonicalPath().startsWith(Environment.getExternalStorageDirectory().getCanonicalPath()) ? Environment.getExternalStorageState() : "unknown";`
- `sources/androidx/core/util/AtomicFile.java:19`
  `this.mNewName = new File(file.getPath() + ".new");`
- `sources/androidx/core/util/AtomicFile.java:20`
  `this.mLegacyBackupName = new File(file.getPath() + ".bak");`
- `sources/androidx/documentfile/provider/RawDocumentFile.java:30`
  `File file = new File(this.mFile, str2);`
- `sources/androidx/multidex/MultiDex.java:58`
  `doInstallation(context, new File(applicationInfo.sourceDir), new File(applicationInfo.dataDir), "secondary-dexes", "", true);`
- `sources/androidx/multidex/MultiDex.java:88`
  `File file = new File(applicationInfo2.dataDir);`
- `sources/androidx/multidex/MultiDex.java:89`
  `doInstallation(context2, new File(applicationInfo.sourceDir), file, str + "secondary-dexes", str, false);`
- `sources/androidx/multidex/MultiDex.java:90`
  `doInstallation(context2, new File(applicationInfo2.sourceDir), file, "secondary-dexes", "", false);`
- `sources/androidx/multidex/MultiDex.java:252`
  `File file = new File(context.getFilesDir(), "secondary-dexes");`
- `sources/androidx/multidex/MultiDex.java:277`
  `File file2 = new File(file, CODE_CACHE_NAME);`
- `sources/androidx/multidex/MultiDexExtractor.java:61`
  `File file3 = new File(file2, LOCK_FILENAME);`
- `sources/androidx/sqlite/db/SupportSQLiteOpenHelper.java:91`
  `SQLiteDatabase.deleteDatabase(new File(str));`
- `sources/androidx/sqlite/db/SupportSQLiteOpenHelper.java:94`
  `if (!new File(str).delete()) {`
- `sources/androidx/sqlite/db/framework/FrameworkSQLiteOpenHelper.java:40`
  `this.mDelegate = new OpenHelper(this.mContext, new File(this.mContext.getNoBackupFilesDir(), this.mName).getAbsolutePath(), frameworkSQLiteDatabaseArr, this.mCallback);`
- `sources/androidx/work/impl/WorkDatabasePathHelper.java:54`
  `map.put(new File(defaultDatabasePath.getPath() + str), new File(databasePath.getPath() + str));`
- `sources/androidx/work/impl/WorkDatabasePathHelper.java:72`
  `return new File(context.getNoBackupFilesDir(), str);`
- `sources/com/activeandroid/ModelInfo.java:122`
  `scanForModelClasses(new File((String) it.next()), packageName, context.getClassLoader());`
- `sources/com/bumptech/glide/load/a/a/c.java:7`
  `import android.provider.MediaStore;`
- `sources/com/bumptech/glide/load/a/a/c.java:56`
  `if (Log.isLoggable("MediaStoreThumbFetcher", 3)) {`
- `sources/com/bumptech/glide/load/a/a/c.java:57`
  `Log.d("MediaStoreThumbFetcher", "Failed to find thumbnail file", e);`
- `sources/com/github/mikephil/charting/charts/Chart.java:15`
  `import android.provider.MediaStore;`
- `sources/com/github/mikephil/charting/utils/FileUtils.java:23`
  `File file = new File(Environment.getExternalStorageDirectory(), str);`
- `sources/com/github/mikephil/charting/utils/FileUtils.java:135`
  `File file = new File(Environment.getExternalStorageDirectory(), str);`
- `sources/com/google/android/gms/internal/ads/zzams.java:104`
  `File file = new File(String.format("%s/%s.jar", cacheDir, "1633031840514"));`
- `sources/com/google/android/gms/internal/ads/zzams.java:384`
  `zzy(new File(str));`
- `sources/com/google/android/gms/internal/auth/zzcz.java:87`
  `File file = new File(contextCreateDeviceProtectedStorageContext.getDir("phenotype_hermetic", 0), "overrides.txt");`
- `sources/com/google/android/gms/internal/gtm/zzcd.java:95`
  `File file = new File(path);`
- `sources/com/google/android/gms/internal/measurement/zzhy.java:85`
  `File file = new File(contextCreateDeviceProtectedStorageContext.getDir("phenotype_hermetic", 0), "overrides.txt");`
- `sources/com/google/android/gms/measurement/internal/zzam.java:29`
  `File file = new File(sQLiteDatabase.getPath());`
- `sources/com/google/android/gms/measurement/internal/zzli.java:1181`
  `FileChannel channel = new RandomAccessFile(new File(this.zzn.zzav().getFilesDir(), "google_app_measurement.db"), "rw").getChannel();`
- `sources/com/google/firebase/database/tubesock/WebSocket.java:265`
  `sSLSessionCache = new SSLSessionCache(new File(this.sslCacheDirectory));`
- `sources/com/google/firebase/storage/FileDownloadTask.java:86`
  `File file = new File(this.mDestinationFile.getPath());`
- `sources/com/ikdong/weight/util/f.java:52`
  `return Environment.getExternalStorageDirectory().getPath() + "/WeightTrack/weight_backup.json";`
- `sources/com/ikdong/weight/util/n.java:28`
  `File file = new File(Environment.getExternalStorageDirectory() + "/WeightTrack");`
- `sources/com/ikdong/weight/util/n.java:30`
  `f2036c = new File(file, "WTA.data");`
- `sources/com/ikdong/weight/util/n.java:31`
  `f2037d = new File(Environment.getDataDirectory() + "/data/com.ikdong.weight/databases/WTA.mp3");`
- `sources/com/ikdong/weight/util/u.java:23`
  `String str2 = Environment.getExternalStorageDirectory().getPath() + "/WeightTrack/foods_" + new SimpleDateFormat("yyyyMMddmmss").format(new Date()) + ".json";`
- `sources/com/ikdong/weight/util/u.java:24`
  `File file = new File(Environment.getExternalStorageDirectory().getPath() + "/WeightTrack");`

## BR028

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `resources/AndroidManifest.xml:48`
  `android:allowBackup="true"`

## BR029

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:96`
  `android:exported="true"`
- `resources/AndroidManifest.xml:218`
  `android:exported="true"`
- `resources/AndroidManifest.xml:234`
  `android:exported="true"`
- `resources/AndroidManifest.xml:256`
  `android:exported="true"`
- `resources/AndroidManifest.xml:278`
  `android:exported="true"`
- `resources/AndroidManifest.xml:294`
  `android:exported="true"`
- `resources/AndroidManifest.xml:310`
  `android:exported="true"`
- `resources/AndroidManifest.xml:326`
  `android:exported="true"`
- `resources/AndroidManifest.xml:342`
  `android:exported="true"`
- `resources/AndroidManifest.xml:364`
  `android:exported="true"`
- `resources/AndroidManifest.xml:380`
  `android:exported="true"`
- `resources/AndroidManifest.xml:500`
  `android:exported="true"`
- `resources/AndroidManifest.xml:642`
  `android:exported="true"`
- `resources/AndroidManifest.xml:657`
  `android:exported="true"`
- `resources/AndroidManifest.xml:738`
  `android:exported="true">`
- `resources/AndroidManifest.xml:783`
  `android:exported="true"`
- `resources/AndroidManifest.xml:799`
  `android:exported="true"`

## BR030

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:765`
  `android:exported="true"`
- `resources/AndroidManifest.xml:881`
  `android:exported="true"`

## BR031

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:697`
  `android:exported="true">`
- `resources/AndroidManifest.xml:709`
  `android:exported="true">`
- `resources/AndroidManifest.xml:719`
  `android:exported="true">`
- `resources/AndroidManifest.xml:728`
  `android:exported="true">`
- `resources/AndroidManifest.xml:765`
  `android:exported="true"`
- `resources/AndroidManifest.xml:956`
  `android:exported="true"`

## BR032

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `resources/AndroidManifest.xml:22`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:32`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:104`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:222`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:238`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:260`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:282`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:298`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:314`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:330`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:346`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:368`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:384`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:504`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:645`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:660`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:787`
  `<action android:name="android.intent.action.VIEW"/>`
- `resources/AndroidManifest.xml:803`
  `<action android:name="android.intent.action.VIEW"/>`

## BR033

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/androidx/browser/browseractions/BrowserActionsIntent.java:171`
  `return context.getPackageManager().queryIntentActivities(new Intent(ACTION_BROWSER_ACTIONS_OPEN, Uri.parse(TEST_URL)), 131072);`
- `sources/com/google/android/gms/ads/internal/zzs.java:88`
  `intent.setData(Uri.parse(str));`
- `sources/com/google/android/gms/ads/internal/util/zzay.java:17`
  `zzt.zzY(this.zza.zza, Uri.parse("https://support.google.com/dfp_premium/answer/7160685#push"));`
- `sources/com/google/android/gms/internal/ads/zzcal.java:26`
  `DownloadManager.Request request = new DownloadManager.Request(Uri.parse(str));`
- `sources/com/google/android/gms/internal/ads/zzcdu.java:62`
  `return packageManager.resolveActivity(new Intent("android.intent.action.VIEW", Uri.parse(str)), 65536);`
- `sources/com/google/android/gms/internal/ads/zzehp.java:191`
  `launchIntentForPackage.setData(Uri.parse(stringExtra3));`
- `sources/com/google/android/gms/internal/consent_sdk/zzbj.java:45`
  `Uri uri = Uri.parse(str);`
- `sources/com/google/android/gms/internal/icing/zzaf.java:25`
  `uri = string4 != null ? Uri.parse(string4) : null;`
- `sources/com/google/android/youtube/player/YouTubeIntents.java:80`
  `return a(context, Uri.parse("https://www.youtube.com/user/"));`
- `sources/com/google/android/youtube/player/YouTubeIntents.java:85`
  `return b(context, Uri.parse(strValueOf.length() != 0 ? "https://www.youtube.com/channel/".concat(strValueOf) : new String("https://www.youtube.com/channel/")));`
- `sources/com/google/android/youtube/player/YouTubeIntents.java:121`
  `return b(context, Uri.parse(strValueOf.length() != 0 ? "https://www.youtube.com/user/".concat(strValueOf) : new String("https://www.youtube.com/user/")));`
- `sources/com/google/firebase/auth/UserProfileChangeRequest.java:63`
  `this.zze = TextUtils.isEmpty(str2) ? null : Uri.parse(str2);`
- `sources/com/google/firebase/auth/internal/zzt.java:67`
  `this.zze = Uri.parse(this.zzd);`
- `sources/com/google/firebase/storage/UploadTask.java:295`
  `this.mUploadUri = Uri.parse(resultString);`
- `sources/com/ikdong/weight/activity/SyncFitbitActivity.java:177`
  `intent.setData(Uri.parse("https://www.fitbit.com/oauth2/authorize?response_type=code&client_id=227QDP&redirect_uri=wta%3A%2F%2Ffitbit&scope=activity%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&expires_in=604800"));`
- `sources/com/ikdong/weight/activity/WithingsActivity.java:189`
  `intent.setData(Uri.parse(str3));`
- `sources/com/ikdong/weight/integration/withings/a/b.java:38`
  `intent.setData(Uri.parse(strReplace));`
- `sources/com/ikdong/weight/widget/fragment/CalendarWeekPlanFragment.java:312`
  `CalendarWeekPlanFragment.this.startActivity(new Intent("android.intent.action.VIEW", Uri.parse(reference)));`
- `sources/com/ikdong/weight/widget/fragment/CalendarWeekPlanFragment.java:321`
  `CalendarWeekPlanFragment.this.startActivity(new Intent("android.intent.action.VIEW", Uri.parse(reference2)));`
- `sources/com/ikdong/weight/widget/fragment/CalendarWeekPlanFragment.java:337`
  `CalendarWeekPlanFragment.this.startActivity(new Intent("android.intent.action.VIEW", Uri.parse(reference3)));`
- `sources/com/ikdong/weight/widget/fragment/CalendarWeekPlanFragment.java:354`
  `Uri uri = Uri.parse(MediaStore.Images.Media.insertImage(CalendarWeekPlanFragment.this.getContext().getContentResolver(), bitmapDecodeFile, CalendarWeekPlanFragment.this.getContext().getString(R.string.title_photo), (String) null));`
- `sources/com/ikdong/weight/widget/fragment/i.java:61`
  `intent.setData(Uri.parse(string));`
- `sources/com/ikdong/weight/widget/fragment/ResourceFragment.java:84`
  `intent.setData(Uri.parse(String.format("market://details?id=%s", getContext().getPackageName())));`
- `sources/com/ikdong/weight/widget/fragment/ResourceFragment.java:97`
  `intent.setData(Uri.parse("http://line.me/R/ti/g/_oofMbFMj7"));`

## BR034

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/androidx/browser/customtabs/CustomTabsIntent.java:53`
  `ContextCompat.startActivity(context, this.intent, this.startAnimationBundle);`
- `sources/com/google/android/gms/ads/internal/zzs.java:89`
  `zzsVar.zzd.startActivity(intent);`
- `sources/com/google/android/gms/ads/internal/util/zzt.java:839`
  `context.startActivity(intent);`
- `sources/com/google/android/gms/internal/ads/zzehp.java:194`
  `context.startActivity(launchIntentForPackage);`
- `sources/com/google/android/gms/internal/gtm/zzfi.java:42`
  `context.startService(intent2);`
- `sources/com/google/android/gms/measurement/internal/zzfr.java:38`
  `this.zza.doStartService(context, className);`
- `sources/com/google/firebase/auth/internal/GenericIdpActivity.java:53`
  `if (LocalBroadcastManager.getInstance(this).sendBroadcast(intent)) {`
- `sources/com/google/firebase/auth/internal/GenericIdpActivity.java:67`
  `if (LocalBroadcastManager.getInstance(this).sendBroadcast(intent)) {`
- `sources/com/google/firebase/auth/internal/GenericIdpActivity.java:160`
  `if (LocalBroadcastManager.getInstance(this).sendBroadcast(intent2)) {`
- `sources/com/google/firebase/auth/internal/RecaptchaActivity.java:50`
  `LocalBroadcastManager.getInstance(this).sendBroadcast(intent);`
- `sources/com/google/firebase/auth/internal/RecaptchaActivity.java:61`
  `LocalBroadcastManager.getInstance(this).sendBroadcast(intent);`
- `sources/com/google/firebase/auth/internal/RecaptchaActivity.java:136`
  `if (LocalBroadcastManager.getInstance(this).sendBroadcast(intent3)) {`
- `sources/com/ikdong/weight/activity/FitnessDetailActivity.java:144`
  `FitnessDetailActivity.this.startActivity(new Intent(FitnessDetailActivity.this, (Class<?>) SocialLoginActivity.class));`
- `sources/com/ikdong/weight/activity/SyncFitbitActivity.java:178`
  `startActivity(intent);`
- `sources/com/ikdong/weight/activity/WeightInputActivity.java:441`
  `sendBroadcast(intent);`
- `sources/com/ikdong/weight/activity/WeightInputActivity.java:445`
  `sendBroadcast(intent2);`
- `sources/com/ikdong/weight/activity/WithingsActivity.java:190`
  `startActivity(intent);`
- `sources/com/ikdong/weight/integration/withings/a/b.java:39`
  `activity.startActivity(intent);`
- `sources/com/ikdong/weight/widget/fragment/i.java:62`
  `i.this.getActivity().startActivity(intent);`
- `sources/com/ikdong/weight/widget/fragment/ResourceFragment.java:85`
  `getActivity().startActivity(intent);`
- `sources/com/ikdong/weight/widget/fragment/ResourceFragment.java:98`
  `getActivity().startActivity(intent);`

## BR035

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/com/google/android/gms/ads/nonagon/signalgeneration/zzv.java:272`
  `webView.addJavascriptInterface(new TaggingLibraryJsInterface(webView, this.zzh), "gmaSdk");`
- `sources/com/google/android/gms/internal/ads/zzcpi.java:208`
  `super.loadUrl("about:blank");`
- `sources/com/google/android/gms/internal/ads/zzcpi.java:339`
  `super.loadUrl(str);`
- `sources/com/google/android/gms/internal/ads/zzfku.java:17`
  `this.zza.loadUrl(this.zzb);`
- `sources/com/google/android/gms/internal/ads/zzfkv.java:58`
  `webView.loadUrl(string2);`
- `sources/com/google/android/gms/internal/ads/zzflf.java:46`
  `webView2.loadUrl("javascript: null");`
- `sources/com/google/android/gms/internal/consent_sdk/zzch.java:36`
  `webView.loadUrl(strValueOf.length() != 0 ? "javascript:".concat(strValueOf) : new String("javascript:"));`
- `sources/com/ikdong/weight/activity/WebActivity.java:41`
  `webView.loadUrl(strA);`

## BR040

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `resources/AndroidManifest.xml:55`
  `android:name="com.google.android.gms.ads.APPLICATION_ID"`
- `resources/AndroidManifest.xml:746`
  `android:name="com.google.android.gms.ads.AdActivity"`
- `resources/AndroidManifest.xml:856`
  `android:name="com.google.android.gms.ads.MobileAdsInitProvider"`
- `resources/AndroidManifest.xml:861`
  `android:name="com.google.android.gms.ads.AdService"`
- `resources/res/layout/ads_image_banner.xml:6`
  `<com.google.android.gms.ads.AdView`
- `resources/res/layout/ad_native_layout.xml:18`
  `<com.google.android.gms.ads.formats.NativeContentAdView`
- `resources/res/layout/ad_native_layout.xml:94`
  `</com.google.android.gms.ads.formats.NativeContentAdView>`
- `sources/androidx/core/os/BuildCompat.java:4`
  `import com.google.android.gms.ads.RequestConfiguration;`
- `sources/com/google/ads/AdRequest.java:5`
  `public final class AdRequest {`
- `sources/com/google/ads/AdRequest.java:34`
  `private AdRequest() {`
- `sources/com/google/ads/AdSize.java:13`
  `private final com.google.android.gms.ads.AdSize zza;`
- `sources/com/google/ads/AdSize.java:22`
  `this(new com.google.android.gms.ads.AdSize(i, i2));`
- `sources/com/google/ads/AdSize.java:25`
  `public AdSize(com.google.android.gms.ads.AdSize adSize) {`
- `sources/com/google/ads/AdSize.java:109`
  `this(new com.google.android.gms.ads.AdSize(i, i2));`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:8`
  `import com.google.android.gms.ads.AdLoader;`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:9`
  `import com.google.android.gms.ads.AdRequest;`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:10`
  `import com.google.android.gms.ads.AdSize;`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:11`
  `import com.google.android.gms.ads.AdView;`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:12`
  `import com.google.android.gms.ads.interstitial.InterstitialAd;`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:13`
  `import com.google.android.gms.ads.mediation.MediationNativeAdapter;`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:14`
  `import com.google.android.gms.ads.mediation.MediationNativeListener;`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:15`
  `import com.google.android.gms.ads.mediation.NativeMediationAdRequest;`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:16`
  `import com.google.android.gms.ads.mediation.OnImmersiveModeUpdatedListener;`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:26`
  `public abstract class AbstractAdViewAdapter implements com.google.android.gms.ads.mediation.MediationBannerAdapter, MediationNativeAdapter, OnImmersiveModeUpdatedListener, com.google.android.gms.ads.mediation.zzb, zzcql {`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:32`
  `AdRequest buildAdRequest(Context context, com.google.android.gms.ads.mediation.MediationAdRequest mediationAdRequest, Bundle bundle, Bundle bundle2) {`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:33`
  `AdRequest.Builder builder = new AdRequest.Builder();`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:34`
  `Date birthday = mediationAdRequest.getBirthday();`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:38`
  `int gender = mediationAdRequest.getGender();`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:42`
  `Set<String> keywords = mediationAdRequest.getKeywords();`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:49`
  `Location location = mediationAdRequest.getLocation();`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:53`
  `if (mediationAdRequest.isTesting()) {`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:57`
  `if (mediationAdRequest.taggedForChildDirectedTreatment() != -1) {`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:58`
  `builder.zze(mediationAdRequest.taggedForChildDirectedTreatment() == 1);`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:60`
  `builder.zzd(mediationAdRequest.isDesignedForFamilies());`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:71`
  `@Override // com.google.android.gms.ads.mediation.MediationBannerAdapter`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:82`
  `com.google.android.gms.ads.mediation.zza zzaVar = new com.google.android.gms.ads.mediation.zza();`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:87`
  `@Override // com.google.android.gms.ads.mediation.zzb`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:100`
  `@Override // com.google.android.gms.ads.mediation.MediationAdapter`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:115`
  `@Override // com.google.android.gms.ads.mediation.OnImmersiveModeUpdatedListener`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:123`
  `@Override // com.google.android.gms.ads.mediation.MediationAdapter`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:131`
  `@Override // com.google.android.gms.ads.mediation.MediationAdapter`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:139`
  `@Override // com.google.android.gms.ads.mediation.MediationBannerAdapter`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:140`
  `public void requestBannerAd(Context context, com.google.android.gms.ads.mediation.MediationBannerListener mediationBannerListener, Bundle bundle, AdSize adSize, com.google.android.gms.ads.mediation.MediationAdRequest mediationAdRequest, Bundle bundle2) {`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:146`
  `this.mAdView.loadAd(buildAdRequest(context, mediationAdRequest, bundle2, bundle));`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:149`
  `@Override // com.google.android.gms.ads.mediation.MediationInterstitialAdapter`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:150`
  `public void requestInterstitialAd(Context context, com.google.android.gms.ads.mediation.MediationInterstitialListener mediationInterstitialListener, Bundle bundle, com.google.android.gms.ads.mediation.MediationAdRequest mediationAdRequest, Bundle bundle2) {`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:151`
  `InterstitialAd.load(context, getAdUnitId(bundle), buildAdRequest(context, mediationAdRequest, bundle2, bundle), new zzc(this, mediationInterstitialListener));`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:154`
  `@Override // com.google.android.gms.ads.mediation.MediationNativeAdapter`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:155`
  `public void requestNativeAd(Context context, MediationNativeListener mediationNativeListener, Bundle bundle, NativeMediationAdRequest nativeMediationAdRequest, Bundle bundle2) {`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:158`
  `builderWithAdListener.withNativeAdOptions(nativeMediationAdRequest.getNativeAdOptions());`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:159`
  `builderWithAdListener.withNativeAdOptions(nativeMediationAdRequest.getNativeAdRequestOptions());`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:160`
  `if (nativeMediationAdRequest.isUnifiedNativeAdRequested()) {`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:163`
  `if (nativeMediationAdRequest.zzb()) {`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:164`
  `for (String str : nativeMediationAdRequest.zza().keySet()) {`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:165`
  `builderWithAdListener.forCustomTemplateAd(str, zzeVar, true != nativeMediationAdRequest.zza().get(str).booleanValue() ? null : zzeVar);`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:170`
  `adLoaderBuild.loadAd(buildAdRequest(context, nativeMediationAdRequest, bundle2, bundle));`
- `sources/com/google/ads/mediation/AbstractAdViewAdapter.java:173`
  `@Override // com.google.android.gms.ads.mediation.MediationInterstitialAdapter`
- `sources/com/google/ads/mediation/AdUrlAdapter.java:4`
  `import com.google.android.gms.ads.mediation.MediationNativeAdapter;`
- `sources/com/google/ads/mediation/AdUrlAdapter.java:8`
  `public final class AdUrlAdapter extends AbstractAdViewAdapter implements com.google.android.gms.ads.mediation.MediationBannerAdapter, com.google.android.gms.ads.mediation.MediationInterstitialAdapter, MediationNativeAdapter {`
- `sources/com/google/ads/mediation/MediationAdRequest.java:4`
  `import com.google.ads.AdRequest;`
- `sources/com/google/ads/mediation/MediationAdRequest.java:11`
  `public class MediationAdRequest {`
- `sources/com/google/ads/mediation/MediationAdRequest.java:13`
  `private final AdRequest.Gender zzb;`
- `sources/com/google/ads/mediation/MediationAdRequest.java:18`
  `public MediationAdRequest(Date date, AdRequest.Gender gender, Set<String> set, boolean z, Location location) {`
- `sources/com/google/ads/mediation/MediationAdRequest.java:40`
  `public AdRequest.Gender getGender() {`
- `sources/com/google/ads/mediation/MediationBannerAdapter.java:14`
  `void requestBannerAd(MediationBannerListener mediationBannerListener, Activity activity, SERVER_PARAMETERS server_parameters, AdSize adSize, MediationAdRequest mediationAdRequest, ADDITIONAL_PARAMETERS additional_parameters);`
- `sources/com/google/ads/mediation/MediationBannerListener.java:3`
  `import com.google.ads.AdRequest;`
- `sources/com/google/ads/mediation/MediationBannerListener.java:12`
  `void onFailedToReceiveAd(MediationBannerAdapter<?, ?> mediationBannerAdapter, AdRequest.ErrorCode errorCode);`
- `sources/com/google/ads/mediation/MediationInterstitialAdapter.java:10`
  `void requestInterstitialAd(MediationInterstitialListener mediationInterstitialListener, Activity activity, SERVER_PARAMETERS server_parameters, MediationAdRequest mediationAdRequest, ADDITIONAL_PARAMETERS additional_parameters);`
- `sources/com/google/ads/mediation/MediationInterstitialListener.java:3`
  `import com.google.ads.AdRequest;`
- `sources/com/google/ads/mediation/MediationInterstitialListener.java:10`
  `void onFailedToReceiveAd(MediationInterstitialAdapter<?, ?> mediationInterstitialAdapter, AdRequest.ErrorCode errorCode);`
- `sources/com/google/ads/mediation/NetworkExtras.java:5`
  `public interface NetworkExtras extends com.google.android.gms.ads.mediation.NetworkExtras {`
- `sources/com/google/ads/mediation/zza.java:4`
  `import com.google.android.gms.ads.formats.UnifiedNativeAd;`
- `sources/com/google/ads/mediation/zza.java:5`
  `import com.google.android.gms.ads.formats.zzg;`
- `sources/com/google/ads/mediation/zza.java:6`
  `import com.google.android.gms.ads.mediation.UnifiedNativeAdMapper;`
- `sources/com/google/ads/mediation/zza.java:30`
  `@Override // com.google.android.gms.ads.mediation.UnifiedNativeAdMapper`
- `sources/com/google/ads/mediation/zza.java:35`
  `if (com.google.android.gms.ads.formats.zze.zza.get(view) != null) {`
- `sources/com/google/ads/mediation/zzb.java:3`
  `import com.google.android.gms.ads.AdListener;`
- `sources/com/google/ads/mediation/zzb.java:4`
  `import com.google.android.gms.ads.LoadAdError;`
- `sources/com/google/ads/mediation/zzb.java:5`
  `import com.google.android.gms.ads.admanager.AppEventListener;`
- `sources/com/google/ads/mediation/zzb.java:11`
  `final com.google.android.gms.ads.mediation.MediationBannerListener zzb;`

## BR041

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `resources/AndroidManifest.xml:768`
  `android:name="com.google.android.gms.analytics.AnalyticsReceiver"`
- `resources/AndroidManifest.xml:772`
  `android:name="com.google.android.gms.analytics.AnalyticsService"`
- `resources/AndroidManifest.xml:776`
  `android:name="com.google.android.gms.analytics.AnalyticsJobService"`
- `resources/AndroidManifest.xml:826`
  `android:name="com.google.firebase.components:com.google.firebase.analytics.connector.internal.AnalyticsConnectorRegistrar"`
- `sources/androidx/appcompat/app/AppCompatViewInflater.java:29`
  `import com.google.android.gms.analytics.ecommerce.Promotion;`
- `sources/androidx/appcompat/app/TwilightManager.java:8`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/appcompat/widget/SuggestionsAdapter.java:27`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/content/ContextCompat.java:69`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/content/FileProvider.java:16`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/graphics/drawable/IconCompat.java:32`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/provider/FontProvider.java:15`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/core/view/ContentInfoCompat.java:12`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:6`
  `import com.google.android.gms.analytics.ecommerce.ProductAction;`
- `sources/androidx/work/impl/constraints/trackers/BatteryNotLowTracker.java:9`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/bumptech/glide/load/a/a/b.java:4`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/bumptech/glide/load/b/c/a.java:6`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/bumptech/glide/load/c/w.java:8`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/analytics/AnalyticsJobService.java:1`
  `package com.google.android.gms.analytics;`
- `sources/com/google/android/gms/analytics/AnalyticsReceiver.java:1`
  `package com.google.android.gms.analytics;`
- `sources/com/google/android/gms/analytics/AnalyticsService.java:1`
  `package com.google.android.gms.analytics;`
- `sources/com/google/android/gms/analytics/CampaignTrackingReceiver.java:1`
  `package com.google.android.gms.analytics;`
- `sources/com/google/android/gms/analytics/CampaignTrackingReceiver.java:23`
  `boolean zZzi = zzfs.zzi(context, "com.google.android.gms.analytics.CampaignTrackingReceiver", true);`
- `sources/com/google/android/gms/analytics/CampaignTrackingService.java:1`
  `package com.google.android.gms.analytics;`
- `sources/com/google/android/gms/analytics/ExceptionParser.java:1`
  `package com.google.android.gms.analytics;`
- `sources/com/google/android/gms/analytics/ExceptionReporter.java:1`
  `package com.google.android.gms.analytics;`
- `sources/com/google/android/gms/analytics/ExceptionReporter.java:4`
  `import com.google.android.gms.analytics.HitBuilders;`
- `sources/com/google/android/gms/analytics/GoogleAnalytics.java:1`
  `package com.google.android.gms.analytics;`
- `sources/com/google/android/gms/analytics/HitBuilders.java:1`
  `package com.google.android.gms.analytics;`
- `sources/com/google/android/gms/analytics/HitBuilders.java:5`
  `import com.google.android.gms.analytics.ecommerce.Product;`
- `sources/com/google/android/gms/analytics/HitBuilders.java:6`
  `import com.google.android.gms.analytics.ecommerce.ProductAction;`
- `sources/com/google/android/gms/analytics/HitBuilders.java:7`
  `import com.google.android.gms.analytics.ecommerce.Promotion;`
- `sources/com/google/android/gms/analytics/HitBuilders.java:25`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:31`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:37`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:43`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:49`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:55`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:61`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:67`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:73`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:79`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:91`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:97`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:103`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:109`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:115`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:121`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:137`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:143`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:149`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:155`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:281`
  `throw new UnsupportedOperationException("Method not decompiled: com.google.android.gms.analytics.HitBuilders.HitBuilder.setCampaignParamsFromUrl(java.lang.String):com.google.android.gms.analytics.HitBuilders$HitBuilder");`
- `sources/com/google/android/gms/analytics/HitBuilders.java:326`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:332`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:338`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:344`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:360`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:366`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:377`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:383`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:394`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:400`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:427`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:433`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:439`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:445`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:451`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:457`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:463`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:469`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:475`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:481`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:493`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:499`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:505`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:516`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:522`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:528`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:539`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`
- `sources/com/google/android/gms/analytics/HitBuilders.java:545`
  `@Override // com.google.android.gms.analytics.HitBuilders.HitBuilder`

## BR042

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `resources/AndroidManifest.xml:19`
  `<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:24`
  `public class AdvertisingIdClient {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:87`
  `Preconditions.checkNotNull(advertisingIdClient.zza);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:88`
  `Preconditions.checkNotNull(advertisingIdClient.zzb);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:89`
  `zZzd = advertisingIdClient.zzb.zzd();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:91`
  `synchronized (advertisingIdClient.zzd) {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:92`
  `zzb zzbVar = advertisingIdClient.zze;`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:94`
  `throw new IOException("AdvertisingIdClient is not connected.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:98`
  `advertisingIdClient.zzb(false);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:99`
  `if (!advertisingIdClient.zzc) {`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:100`
  `throw new IOException("AdvertisingIdClient cannot reconnect.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:102`
  `Preconditions.checkNotNull(advertisingIdClient.zza);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:103`
  `Preconditions.checkNotNull(advertisingIdClient.zzb);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:105`
  `zZzd = advertisingIdClient.zzb.zzd();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:107`
  `Log.i("AdvertisingIdClient", "GMS remote exception ", e);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:111`
  `throw new IOException("AdvertisingIdClient cannot reconnect.", e2);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:115`
  `advertisingIdClient.zze();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:118`
  `advertisingIdClient.zza();`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:137`
  `throw new IOException("AdvertisingIdClient is not connected.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:143`
  `throw new IOException("AdvertisingIdClient cannot reconnect.");`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:150`
  `Log.i("AdvertisingIdClient", "GMS remote exception ", e);`
- `sources/com/google/android/gms/ads/identifier/AdvertisingIdClient.java:154`
  `throw new IOException("AdvertisingIdClient cannot reconnect.", e2);`
- `sources/com/google/android/gms/ads/identifier/zza.java:10`
  `zza(AdvertisingIdClient advertisingIdClient, Map map) {`
- `sources/com/google/android/gms/ads/identifier/zzb.java:11`
  `private final WeakReference<AdvertisingIdClient> zzc;`
- `sources/com/google/android/gms/ads/identifier/zzb.java:14`
  `public zzb(AdvertisingIdClient advertisingIdClient, long j) {`
- `sources/com/google/android/gms/ads/identifier/zzb.java:15`
  `this.zzc = new WeakReference<>(advertisingIdClient);`
- `sources/com/google/android/gms/ads/identifier/zzb.java:21`
  `AdvertisingIdClient advertisingIdClient = this.zzc.get();`
- `sources/com/google/android/gms/ads/internal/util/zzc.java:4`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/ads/internal/util/zzc.java:22`
  `isAdIdFakeForDebugLogging = AdvertisingIdClient.getIsAdIdFakeForDebugLogging(this.zza);`
- `sources/com/google/android/gms/ads/internal/util/zzj.java:153`
  `editor.putBoolean("gad_idless", z);`
- `sources/com/google/android/gms/internal/ads/zzams.java:7`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/internal/ads/zzanh.java:3`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/internal/ads/zzanh.java:13`
  `AdvertisingIdClient advertisingIdClientZzh = this.zzb.zzh();`
- `sources/com/google/android/gms/internal/ads/zzanh.java:14`
  `if (advertisingIdClientZzh == null) {`
- `sources/com/google/android/gms/internal/ads/zzanh.java:18`
  `AdvertisingIdClient.Info info = advertisingIdClientZzh.getInfo();`
- `sources/com/google/android/gms/internal/ads/zzblj.java:281`
  `public static final zzblb<Boolean> zzeg = zzblb.zzi(1, "gads:signals:ad_id_info:enabled", false);`
- `sources/com/google/android/gms/internal/ads/zzcib.java:4`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/internal/ads/zzcib.java:22`
  `this.zzb.zzd(AdvertisingIdClient.getAdvertisingIdInfo(this.zza));`
- `sources/com/google/android/gms/internal/ads/zzcic.java:4`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/internal/ads/zzcic.java:8`
  `public final zzfxa<AdvertisingIdClient.Info> zza(Context context, int i) {`
- `sources/com/google/android/gms/internal/ads/zzcwb.java:21`
  `String str = map.get("gad_idless");`
- `sources/com/google/android/gms/internal/ads/zzcwb.java:24`
  `map.remove("gad_idless");`
- `sources/com/google/android/gms/internal/ads/zzewc.java:6`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/internal/ads/zzewc.java:41`
  `AdvertisingIdClient.Info info = (AdvertisingIdClient.Info) obj;`
- `sources/com/google/android/gms/internal/ads/zzewd.java:4`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/internal/ads/zzewd.java:10`
  `private final AdvertisingIdClient.Info zza;`
- `sources/com/google/android/gms/internal/ads/zzewd.java:13`
  `public zzewd(AdvertisingIdClient.Info info, String str) {`
- `sources/com/google/android/gms/internal/ads/zzewd.java:22`
  `AdvertisingIdClient.Info info = this.zza;`
- `sources/com/google/android/gms/internal/ads/zzfna.java:6`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/internal/ads/zzfna.java:80`
  `AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(context);`
- `sources/com/google/android/gms/internal/consent_sdk/zzb.java:4`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/internal/consent_sdk/zzb.java:19`
  `AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(this.zza);`
- `sources/com/google/android/gms/internal/gtm/zzbi.java:4`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/internal/gtm/zzbi.java:14`
  `private AdvertisingIdClient.Info zzb;`
- `sources/com/google/android/gms/internal/gtm/zzbi.java:36`
  `private final synchronized com.google.android.gms.ads.identifier.AdvertisingIdClient.Info zzc() {`
- `sources/com/google/android/gms/internal/gtm/zzbi.java:41`
  `throw new UnsupportedOperationException("Method not decompiled: com.google.android.gms.internal.gtm.zzbi.zzc():com.google.android.gms.ads.identifier.AdvertisingIdClient$Info");`
- `sources/com/google/android/gms/internal/gtm/zzbi.java:69`
  `AdvertisingIdClient.Info infoZzc = zzc();`
- `sources/com/google/android/gms/internal/gtm/zzbi.java:79`
  `AdvertisingIdClient.Info infoZzc = zzc();`
- `sources/com/google/android/gms/internal/measurement/zzns.java:51`
  `zza = zzhvVarZza.zzd("measurement.ad_id_cache_time", WorkRequest.MIN_BACKOFF_MILLIS);`
- `sources/com/google/android/gms/measurement/internal/zzel.java:139`
  `zza = zza("measurement.ad_id_cache_time", lValueOf, lValueOf, new zzeh() { // from class: com.google.android.gms.measurement.internal.zzax`
- `sources/com/google/android/gms/measurement/internal/zzfn.java:5`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/measurement/internal/zzfn.java:84`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(true);`
- `sources/com/google/android/gms/measurement/internal/zzfn.java:86`
  `AdvertisingIdClient.Info advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(this.zzs.zzav());`
- `sources/com/google/android/gms/measurement/internal/zzfn.java:97`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(false);`
- `sources/com/google/android/gms/measurement/internal/zzkd.java:4`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/measurement/internal/zzkd.java:46`
  `AdvertisingIdClient.Info advertisingIdInfo;`
- `sources/com/google/android/gms/measurement/internal/zzkd.java:48`
  `AdvertisingIdClient.Info advertisingIdInfo2;`
- `sources/com/google/android/gms/measurement/internal/zzkd.java:57`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(true);`
- `sources/com/google/android/gms/measurement/internal/zzkd.java:60`
  `advertisingIdInfo2 = AdvertisingIdClient.getAdvertisingIdInfo(this.zzs.zzav());`
- `sources/com/google/android/gms/measurement/internal/zzkd.java:71`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(false);`
- `sources/com/google/android/gms/measurement/internal/zzkd.java:79`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(true);`
- `sources/com/google/android/gms/measurement/internal/zzkd.java:81`
  `advertisingIdInfo = AdvertisingIdClient.getAdvertisingIdInfo(this.zzs.zzav());`
- `sources/com/google/android/gms/measurement/internal/zzkd.java:95`
  `AdvertisingIdClient.setShouldSkipGmsCoreVersionCheck(false);`
- `sources/com/google/android/gms/tagmanager/zza.java:3`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/tagmanager/zza.java:17`
  `public final AdvertisingIdClient.Info zza() {`
- `sources/com/google/android/gms/tagmanager/zza.java:19`
  `return AdvertisingIdClient.getAdvertisingIdInfo(this.zza.zzi);`
- `sources/com/google/android/gms/tagmanager/zzc.java:3`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/tagmanager/zzc.java:7`
  `AdvertisingIdClient.Info zza();`
- `sources/com/google/android/gms/tagmanager/zzd.java:7`
  `import com.google.android.gms.ads.identifier.AdvertisingIdClient;`
- `sources/com/google/android/gms/tagmanager/zzd.java:15`
  `private volatile AdvertisingIdClient.Info zzf;`

## BR044

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/androidx/core/content/ContextCompat.java:40`
  `import android.net.wifi.WifiManager;`
- `sources/androidx/core/content/ContextCompat.java:312`
  `map.put(WifiManager.class, "wifi");`
- `sources/com/google/android/gms/internal/ads/zzjc.java:4`
  `import android.net.wifi.WifiManager;`
- `sources/com/google/android/gms/internal/ads/zzjc.java:8`
  `private final WifiManager zza;`
- `sources/com/google/android/gms/internal/ads/zzjc.java:11`
  `this.zza = (WifiManager) context.getApplicationContext().getSystemService("wifi");`

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
- `sources/androidx/appcompat/app/ActionBarDrawerToggle.java:218`
  `Log.w("ActionBarDrawerToggle", "DrawerToggle may not show up because NavigationIcon is not visible. You may need to call actionbar.setDisplayHomeAsUpEnabled(true);");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1071`
  `Log.i("AppCompatDelegate", "Failed to instantiate custom view inflater " + string + ". Falling back to default.", th);`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1115`
  `Log.i("AppCompatDelegate", "The Activity's LayoutInflater already has a Factory installed so we can not install AppCompat's");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1654`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1660`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR_OVERLAY id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1854`
  `Log.d("AppCompatDelegate", "Exception while getting ActivityInfo", e);`
- `sources/androidx/appcompat/app/ResourcesFlusher.java:166`
  `Log.e(TAG, "Could not retrieve value from ThemedResourceCache#mUnthemedEntries", e3);`
- `sources/androidx/appcompat/content/res/AppCompatResources.java:55`
  `Log.e(LOG_TAG, "Failed to inflate ColorStateList, leaving it to the framework", e);`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:286`
  `Log.w(SupportMenuInflater.LOG_TAG, "Ignoring attribute 'actionProviderClass'. Action view already specified.");`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:346`
  `Log.w(SupportMenuInflater.LOG_TAG, "Ignoring attribute 'itemActionViewLayout'. Action view already specified.");`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:389`
  `Log.w(SupportMenuInflater.LOG_TAG, "Cannot instantiate class: " + str, e);`
- `sources/androidx/appcompat/view/menu/MenuItemImpl.java:102`
  `Log.e(TAG, "Can't find activity to handle intent; ignoring", e);`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:312`
  `Log.w(TAG, "Failed to invoke TextView#nullLayouts() method", e);`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:210`
  `Log.e(TAG, "Exception while inflating drawable", e);`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:407`
  `Log.e("VdcInflateDelegate", "Exception while inflating <vector>", e);`

## BR050

paper_id: B021
paper_title: Metadata-Based Privacy Assessment for Mobile mHealth

- `security_audit/00_audit_scope_and_summary.md:46`
  `4. 'BR027 / B002 / Unaddressed privacy risks in accredited health and wellness apps'：App 将原始数据库复制到外部存储 '/WeightTrack/WTA.data'，将体重记录 JSON 导出到 '/WeightTrack/weight_backup.json'，并可导出 CSV、图片。由于数据库字段含健康/身体测量数据，这不是单纯文件名证据，而是“敏感模型 -> SQLite -> 外部存储导出”的完整链路。`
- `security_audit/00_audit_scope_and_summary.md:48`
  `5. 'BR028 / B014 / Privacy Assessment in Mobile Health Apps: Scoping Review'：Manifest 中 'android:allowBackup="true"'，且 App 本地保存敏感健康数据和第三方令牌，未见限制备份范围的数据提取规则。`
- `security_audit/01_independent_security_findings.md:143`
  `3. 抓包验证 'http://account.withings.com' 是否实际发生，以及 Android 9+ cleartext policy 是否阻断。`
- `security_audit/02_rule_by_rule_mapping.md:19`
  `| BR005 | B021 / Metadata-Based Privacy Assessment for Mobile mHealth | B021 属于元数据/商店描述与 APK 权限对照。 | 工作区没有 Google Play 商店描述、隐私标签、下载页元数据；不能比较“窄描述 + 宽权限”。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:20`
  `| BR006 | B016 / A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | B016 检查 Manifest 与 Network Security Config 中的明文配置。 | Manifest 未见 'usesCleartextTraffic="true"'；未发现 'network_security_config'。HTTP URL 另按 BR013 处理。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:42`
  `| BR028 | B014 / Privacy Assessment in Mobile Health Apps: Scoping Review | B014 总结 mHealth 隐私评估项目包括本地存储、远端存储、权限、通信、访问控制。 | Manifest 'allowBackup=true'；App 本地有敏感 SQLite 与 SharedPreferences token；未见 dataExtractionRules/backup exclusion。 | confirmed |`
- `security_audit/02_rule_by_rule_mapping.md:43`
  `| BR029 | B016 / A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | B016 使用 Manifest 组件、权限、运行时行为、代码漏洞做多角度审查。 | 多个 exported Activity；其中 'MeasureActivity' 可由 'wta://measure' 打开并展示本地测量数据。和 BR035 重叠，本条保守作为外部组件攻击面假设。 | supported_hypothesis |`
- `security_audit/02_rule_by_rule_mapping.md:44`
  `| BR030 | B016 / A privacy and security analysis... | 规则关注 exported service 可被外部触发敏感行为。 | 第一方 'WeightTileService' exported=true 但有系统 'BIND_QUICK_SETTINGS_TILE' 权限；'BackupService' 无 intent-filter；未见外部 service 可触发敏感同步。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:45`
  `| BR031 | B016 / A privacy and security analysis... | 规则关注外部 broadcast receiver 造成状态变化。 | Boot receivers 处理 'BOOT_COMPLETED'，用于提醒/备份启动；未见外部自定义广播直接修改健康数据。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:50`
  `| BR040 | B007 / Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | B007 特定研究对象是 Facebook SDK 隐私设置与初始化。 | 未发现 Facebook SDK；Google Ads/Firebase 不直接套用该论文规则。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:56`
  `| BR050 | B021 / Metadata-Based Privacy Assessment for Mobile mHealth | B021 使用商店元数据/隐私元数据评估 mHealth。 | 工作区没有 Play Store listing/privacy metadata；仅有本地 PolicyCnActivity，不能完成元数据对照。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:57`
  `| BR051 | B013 / Availability and quality of mobile health app privacy policies | B013 关注隐私政策是否可获得、内容质量。 | 本地有 'PolicyCnActivity' deep link，但未完成商店/官网政策检索，也未证明当前发布政策文本。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:59`
  `| BR055 | B014 / Privacy Assessment in Mobile Health Apps: Scoping Review | B014 强调评估标准异质，建议多项证据。 | 本报告已分 Manifest、存储、URL、SDK、动态证据缺口；该规则是报告质量控制项，不是 App 漏洞。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:62`
  `| BR060 | B016 / A privacy and security analysis... | 规则关注环境/后端配置错误，如测试环境、调试后端、错误开关。 | Firebase 使用 '/prd' 路径；未见 debug/test backend、staging key 或调试开关导致的数据泄露。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:106`
  `| BR092 | B005 / Mobile health and privacy | B005 动态研究发现第三方常参与数据收集/传输；规则要求 adid/deviceId/userId 到第三方域。 | AD_ID 权限和 Google Ads SDK 存在，但没有抓包或 payload 证明 adid/deviceId/userId 到第三方域。 | supported_hypothesis |`
- `security_audit/02_rule_by_rule_mapping.md:107`
  `| BR093 | B004 / Assessment of Data Sharing and Privacy Practices... | B004 对比实际共享与隐私披露。 | 无当前隐私政策文本和实际流量，不能判断未披露接收方。 | not_testable |`

## BR051

paper_id: B013
paper_title: Availability and quality of mobile health app privacy policies

- `security_audit/00_audit_scope_and_summary.md:46`
  `4. 'BR027 / B002 / Unaddressed privacy risks in accredited health and wellness apps'：App 将原始数据库复制到外部存储 '/WeightTrack/WTA.data'，将体重记录 JSON 导出到 '/WeightTrack/weight_backup.json'，并可导出 CSV、图片。由于数据库字段含健康/身体测量数据，这不是单纯文件名证据，而是“敏感模型 -> SQLite -> 外部存储导出”的完整链路。`
- `security_audit/00_audit_scope_and_summary.md:48`
  `5. 'BR028 / B014 / Privacy Assessment in Mobile Health Apps: Scoping Review'：Manifest 中 'android:allowBackup="true"'，且 App 本地保存敏感健康数据和第三方令牌，未见限制备份范围的数据提取规则。`
- `security_audit/02_rule_by_rule_mapping.md:19`
  `| BR005 | B021 / Metadata-Based Privacy Assessment for Mobile mHealth | B021 属于元数据/商店描述与 APK 权限对照。 | 工作区没有 Google Play 商店描述、隐私标签、下载页元数据；不能比较“窄描述 + 宽权限”。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:20`
  `| BR006 | B016 / A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | B016 检查 Manifest 与 Network Security Config 中的明文配置。 | Manifest 未见 'usesCleartextTraffic="true"'；未发现 'network_security_config'。HTTP URL 另按 BR013 处理。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:33`
  `| BR019 | B011 / Locking it down: The privacy and security of mobile medication apps | B011 关注药物、剂量、处方、提醒等 medication 数据。 | 未发现 medication、dose、prescription 等药物模型或字段；提醒功能是体重/日程提醒，不是药物。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:34`
  `| BR020 | B012 / Reviewing the data security and privacy policies of mobile apps for depression | B012 关注抑郁/精神健康 App 及相关敏感政策。 | App 是体重/健康记录，未发现 depression、mood、PHQ、therapy 等精神健康字段。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:44`
  `| BR030 | B016 / A privacy and security analysis... | 规则关注 exported service 可被外部触发敏感行为。 | 第一方 'WeightTileService' exported=true 但有系统 'BIND_QUICK_SETTINGS_TILE' 权限；'BackupService' 无 intent-filter；未见外部 service 可触发敏感同步。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:45`
  `| BR031 | B016 / A privacy and security analysis... | 规则关注外部 broadcast receiver 造成状态变化。 | Boot receivers 处理 'BOOT_COMPLETED'，用于提醒/备份启动；未见外部自定义广播直接修改健康数据。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:50`
  `| BR040 | B007 / Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | B007 特定研究对象是 Facebook SDK 隐私设置与初始化。 | 未发现 Facebook SDK；Google Ads/Firebase 不直接套用该论文规则。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:51`
  `| BR041 | B007 / Privacy Settings of Third-Party Libraries... | 同上，关注 SDK 默认隐私设置与同意前初始化。 | 未发现 Facebook SDK；AdMob/Firebase 需动态同意流量验证，不能按 B007 确认。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:56`
  `| BR050 | B021 / Metadata-Based Privacy Assessment for Mobile mHealth | B021 使用商店元数据/隐私元数据评估 mHealth。 | 工作区没有 Play Store listing/privacy metadata；仅有本地 PolicyCnActivity，不能完成元数据对照。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:57`
  `| BR051 | B013 / Availability and quality of mobile health app privacy policies | B013 关注隐私政策是否可获得、内容质量。 | 本地有 'PolicyCnActivity' deep link，但未完成商店/官网政策检索，也未证明当前发布政策文本。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:59`
  `| BR055 | B014 / Privacy Assessment in Mobile Health Apps: Scoping Review | B014 强调评估标准异质，建议多项证据。 | 本报告已分 Manifest、存储、URL、SDK、动态证据缺口；该规则是报告质量控制项，不是 App 漏洞。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:62`
  `| BR060 | B016 / A privacy and security analysis... | 规则关注环境/后端配置错误，如测试环境、调试后端、错误开关。 | Firebase 使用 '/prd' 路径；未见 debug/test backend、staging key 或调试开关导致的数据泄露。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:78`
  `| BR071 | B016 / A privacy and security analysis... | B016 包含 BLE/contact tracing 场景下位置/权限审查。 | Manifest 无 Bluetooth/BLE/Location 权限。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:88`
  `| BR076 | B005 / Mobile health and privacy | B005 的动态部分要求观察实际流量和数据传输。 | 无 pcap/har/proxy 抓包；不能确认实际运行时用户数据传输。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:89`
  `| BR077 | B007 / Facebook SDK privacy settings | B007 动态/配置验证需运行或 SDK 设置证据。 | 无 Facebook SDK，且无运行时 SDK 请求。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:93`
  `| BR081 | B005 / Mobile health and privacy | 规则要求运行后文件系统抽取，确认敏感值可读。 | 有静态 DB/Prefs 证据，但无运行时 DB 导出或真实值样本。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:94`
  `| BR082 | B002 / Unaddressed privacy risks... | 规则要求登出前后比较本地存储残留。 | 未运行 App、未登录/登出、无本地文件抽取。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:98`
  `| BR088 | B004 / Assessment of Data Sharing and Privacy Practices... | B004 关注敏感流程中第三方请求与政策不一致，需流量和政策。 | 无抓包、无当前政策文本，不能比较。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:99`
  `| BR090 | B014 / Privacy Assessment in Mobile Health Apps | B014 支持制定多层验证计划，但动态执行需要设备。 | 本报告给出验证计划，未执行设备验证。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:106`
  `| BR092 | B005 / Mobile health and privacy | B005 动态研究发现第三方常参与数据收集/传输；规则要求 adid/deviceId/userId 到第三方域。 | AD_ID 权限和 Google Ads SDK 存在，但没有抓包或 payload 证明 adid/deviceId/userId 到第三方域。 | supported_hypothesis |`
- `security_audit/02_rule_by_rule_mapping.md:107`
  `| BR093 | B004 / Assessment of Data Sharing and Privacy Practices... | B004 对比实际共享与隐私披露。 | 无当前隐私政策文本和实际流量，不能判断未披露接收方。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:111`
  `| BR097 | B019 / Pulse Oximeter App Privacy Policies During COVID-19 | B019 关注脉搏血氧/心率/设备测量与账号、政策披露。 | App 有本地 heartRate 字段并可 Firebase 同步，但无 SpO2/oximeter/device measurement 语义；不套用 pulse oximeter 规则。 | not_supported |`
- `security_audit/04_paper_source_review.md:57`
  `- 'C:\wujiangliang\app\xiangshan\database_beginner\snapshots\B005-mobile-health-privacy.html'`
- `security_audit/04_paper_source_review.md:127`
  `## B014 Privacy Assessment in Mobile Health Apps: Scoping Review`
- `security_audit/06_final_advisor_review.md:374`
  `2. 抓包 Withings 连接流程，确认 HTTP authorize 是否实际发生、Android cleartext policy 是否阻断。`

## BR052

paper_id: B013
paper_title: Availability and quality of mobile health app privacy policies

- `security_audit/00_audit_scope_and_summary.md:42`
  `2. 'BR025 / B005 / Mobile health and privacy: cross sectional study'：敏感健康数据进入本地 ActiveAndroid/SQLite 数据库 'WTA.mp3'；代码中未发现 SQLCipher、EncryptedFile、EncryptedSharedPreferences、MasterKey 等加密封装；同时存在原始数据库复制导出逻辑。`
- `security_audit/00_audit_scope_and_summary.md:44`
  `3. 'BR026 / B002 / Unaddressed privacy risks in accredited health and wellness apps'：Fitbit access token、Withings OAuth token/secret/refresh token JSON 等被写入普通 SharedPreferences 'worktrack_setting'。`
- `security_audit/00_audit_scope_and_summary.md:46`
  `4. 'BR027 / B002 / Unaddressed privacy risks in accredited health and wellness apps'：App 将原始数据库复制到外部存储 '/WeightTrack/WTA.data'，将体重记录 JSON 导出到 '/WeightTrack/weight_backup.json'，并可导出 CSV、图片。由于数据库字段含健康/身体测量数据，这不是单纯文件名证据，而是“敏感模型 -> SQLite -> 外部存储导出”的完整链路。`
- `security_audit/00_audit_scope_and_summary.md:48`
  `5. 'BR028 / B014 / Privacy Assessment in Mobile Health Apps: Scoping Review'：Manifest 中 'android:allowBackup="true"'，且 App 本地保存敏感健康数据和第三方令牌，未见限制备份范围的数据提取规则。`
- `security_audit/02_rule_by_rule_mapping.md:19`
  `| BR005 | B021 / Metadata-Based Privacy Assessment for Mobile mHealth | B021 属于元数据/商店描述与 APK 权限对照。 | 工作区没有 Google Play 商店描述、隐私标签、下载页元数据；不能比较“窄描述 + 宽权限”。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:20`
  `| BR006 | B016 / A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | B016 检查 Manifest 与 Network Security Config 中的明文配置。 | Manifest 未见 'usesCleartextTraffic="true"'；未发现 'network_security_config'。HTTP URL 另按 BR013 处理。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:33`
  `| BR019 | B011 / Locking it down: The privacy and security of mobile medication apps | B011 关注药物、剂量、处方、提醒等 medication 数据。 | 未发现 medication、dose、prescription 等药物模型或字段；提醒功能是体重/日程提醒，不是药物。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:34`
  `| BR020 | B012 / Reviewing the data security and privacy policies of mobile apps for depression | B012 关注抑郁/精神健康 App 及相关敏感政策。 | App 是体重/健康记录，未发现 depression、mood、PHQ、therapy 等精神健康字段。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:39`
  `| BR025 | B005 / Mobile health and privacy: cross sectional study | B005 结合静态/动态分析健康 App 数据收集、流量、tracker 和本地数据风险。 | ActiveAndroid DB 'WTA.mp3' 存储 'Weights'/'Goals'/'Images'；未发现 SQLCipher/EncryptedSharedPreferences/EncryptedFile/MasterKey；有原始 DB 复制导出。 | confirmed |`
- `security_audit/02_rule_by_rule_mapping.md:40`
  `| BR026 | B002 / Unaddressed privacy risks in accredited health and wellness apps | B002 原文检查本地设备存储和传输，指出健康/个人信息本地未加密存储会带来风险。 | 'g.a(context,key,string)' 写入普通 'worktrack_setting'；Fitbit access token 存入 'PARAM_FITBIT_ACCESS_TOKEN'；Withings token JSON 存入 'INT_WITHINGS_TOKEN'；旧 Withings token/secret 也用...`
- `security_audit/02_rule_by_rule_mapping.md:41`
  `| BR027 | B002 / Unaddressed privacy risks... | B002 将移动设备存储作为评估对象，特别关注个人/敏感信息是否被安全保护。 | 'util.n' 将 '/data/.../WTA.mp3' 复制到外部 '/WeightTrack/WTA.data'；'util.f' 将 Weight JSON 写入 '/WeightTrack/weight_backup.json'；CSV 和图片也写外部路径。 | confirmed |`
- `security_audit/02_rule_by_rule_mapping.md:42`
  `| BR028 | B014 / Privacy Assessment in Mobile Health Apps: Scoping Review | B014 总结 mHealth 隐私评估项目包括本地存储、远端存储、权限、通信、访问控制。 | Manifest 'allowBackup=true'；App 本地有敏感 SQLite 与 SharedPreferences token；未见 dataExtractionRules/backup exclusion。 | confirmed |`
- `security_audit/02_rule_by_rule_mapping.md:43`
  `| BR029 | B016 / A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps | B016 使用 Manifest 组件、权限、运行时行为、代码漏洞做多角度审查。 | 多个 exported Activity；其中 'MeasureActivity' 可由 'wta://measure' 打开并展示本地测量数据。和 BR035 重叠，本条保守作为外部组件攻击面假设。 | supported_hypothesis |`
- `security_audit/02_rule_by_rule_mapping.md:44`
  `| BR030 | B016 / A privacy and security analysis... | 规则关注 exported service 可被外部触发敏感行为。 | 第一方 'WeightTileService' exported=true 但有系统 'BIND_QUICK_SETTINGS_TILE' 权限；'BackupService' 无 intent-filter；未见外部 service 可触发敏感同步。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:45`
  `| BR031 | B016 / A privacy and security analysis... | 规则关注外部 broadcast receiver 造成状态变化。 | Boot receivers 处理 'BOOT_COMPLETED'，用于提醒/备份启动；未见外部自定义广播直接修改健康数据。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:50`
  `| BR040 | B007 / Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | B007 特定研究对象是 Facebook SDK 隐私设置与初始化。 | 未发现 Facebook SDK；Google Ads/Firebase 不直接套用该论文规则。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:51`
  `| BR041 | B007 / Privacy Settings of Third-Party Libraries... | 同上，关注 SDK 默认隐私设置与同意前初始化。 | 未发现 Facebook SDK；AdMob/Firebase 需动态同意流量验证，不能按 B007 确认。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:56`
  `| BR050 | B021 / Metadata-Based Privacy Assessment for Mobile mHealth | B021 使用商店元数据/隐私元数据评估 mHealth。 | 工作区没有 Play Store listing/privacy metadata；仅有本地 PolicyCnActivity，不能完成元数据对照。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:57`
  `| BR051 | B013 / Availability and quality of mobile health app privacy policies | B013 关注隐私政策是否可获得、内容质量。 | 本地有 'PolicyCnActivity' deep link，但未完成商店/官网政策检索，也未证明当前发布政策文本。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:59`
  `| BR055 | B014 / Privacy Assessment in Mobile Health Apps: Scoping Review | B014 强调评估标准异质，建议多项证据。 | 本报告已分 Manifest、存储、URL、SDK、动态证据缺口；该规则是报告质量控制项，不是 App 漏洞。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:62`
  `| BR060 | B016 / A privacy and security analysis... | 规则关注环境/后端配置错误，如测试环境、调试后端、错误开关。 | Firebase 使用 '/prd' 路径；未见 debug/test backend、staging key 或调试开关导致的数据泄露。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:78`
  `| BR071 | B016 / A privacy and security analysis... | B016 包含 BLE/contact tracing 场景下位置/权限审查。 | Manifest 无 Bluetooth/BLE/Location 权限。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:88`
  `| BR076 | B005 / Mobile health and privacy | B005 的动态部分要求观察实际流量和数据传输。 | 无 pcap/har/proxy 抓包；不能确认实际运行时用户数据传输。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:89`
  `| BR077 | B007 / Facebook SDK privacy settings | B007 动态/配置验证需运行或 SDK 设置证据。 | 无 Facebook SDK，且无运行时 SDK 请求。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:93`
  `| BR081 | B005 / Mobile health and privacy | 规则要求运行后文件系统抽取，确认敏感值可读。 | 有静态 DB/Prefs 证据，但无运行时 DB 导出或真实值样本。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:94`
  `| BR082 | B002 / Unaddressed privacy risks... | 规则要求登出前后比较本地存储残留。 | 未运行 App、未登录/登出、无本地文件抽取。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:98`
  `| BR088 | B004 / Assessment of Data Sharing and Privacy Practices... | B004 关注敏感流程中第三方请求与政策不一致，需流量和政策。 | 无抓包、无当前政策文本，不能比较。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:99`
  `| BR090 | B014 / Privacy Assessment in Mobile Health Apps | B014 支持制定多层验证计划，但动态执行需要设备。 | 本报告给出验证计划，未执行设备验证。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:106`
  `| BR092 | B005 / Mobile health and privacy | B005 动态研究发现第三方常参与数据收集/传输；规则要求 adid/deviceId/userId 到第三方域。 | AD_ID 权限和 Google Ads SDK 存在，但没有抓包或 payload 证明 adid/deviceId/userId 到第三方域。 | supported_hypothesis |`
- `security_audit/02_rule_by_rule_mapping.md:107`
  `| BR093 | B004 / Assessment of Data Sharing and Privacy Practices... | B004 对比实际共享与隐私披露。 | 无当前隐私政策文本和实际流量，不能判断未披露接收方。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:111`
  `| BR097 | B019 / Pulse Oximeter App Privacy Policies During COVID-19 | B019 关注脉搏血氧/心率/设备测量与账号、政策披露。 | App 有本地 heartRate 字段并可 Firebase 同步，但无 SpO2/oximeter/device measurement 语义；不套用 pulse oximeter 规则。 | not_supported |`
- `security_audit/03_evidence_chains.md:10`
  `- 'BR025 / B005 / Mobile health and privacy: cross sectional study'：confirmed。`
- `security_audit/03_evidence_chains.md:11`
  `- 'BR027 / B002 / Unaddressed privacy risks in accredited health and wellness apps'：confirmed。`
- `security_audit/04_paper_source_review.md:29`
  `## B002 Unaddressed privacy risks in accredited health and wellness apps`
- `security_audit/04_paper_source_review.md:33`
  `- 'C:\wujiangliang\app\xiangshan\database_beginner\snapshots\B002-accredited-health-app-privacy.html'`
- `security_audit/04_paper_source_review.md:53`
  `## B005 Mobile health and privacy: cross sectional study`
- `security_audit/04_paper_source_review.md:57`
  `- 'C:\wujiangliang\app\xiangshan\database_beginner\snapshots\B005-mobile-health-privacy.html'`
- `security_audit/04_paper_source_review.md:127`
  `## B014 Privacy Assessment in Mobile Health Apps: Scoping Review`
- `security_audit/04_paper_source_review.md:131`
  `- 'C:\wujiangliang\app\xiangshan\database_beginner\snapshots\B014-covid-contact-tracing-app-privacy-security.html'`
- `security_audit/04_paper_source_review.md:136`
  `- 原文把 App behavior、in-app information、personal information types、app communications、static/dynamic analyses、privacy policy existence/content 等作为分类。`
- `security_audit/04_paper_source_review.md:150`
  `## B016 A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps`
- `security_audit/04_paper_source_review.md:154`
  `- 'C:\wujiangliang\app\xiangshan\database_beginner\snapshots\B016-privacy-security-analysis-covid-android-apps.html'`

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

- `security_audit/02_rule_by_rule_mapping.md:50`
  `| BR040 | B007 / Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs | B007 特定研究对象是 Facebook SDK 隐私设置与初始化。 | 未发现 Facebook SDK；Google Ads/Firebase 不直接套用该论文规则。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:51`
  `| BR041 | B007 / Privacy Settings of Third-Party Libraries... | 同上，关注 SDK 默认隐私设置与同意前初始化。 | 未发现 Facebook SDK；AdMob/Firebase 需动态同意流量验证，不能按 B007 确认。 | not_supported |`

## BR059

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/AndroidManifest.xml:99`
  `<intent-filter>`
- `resources/AndroidManifest.xml:103`
  `<intent-filter android:label="@string/app_name">`
- `resources/AndroidManifest.xml:221`
  `<intent-filter>`
- `resources/AndroidManifest.xml:237`
  `<intent-filter>`
- `resources/AndroidManifest.xml:259`
  `<intent-filter>`
- `resources/AndroidManifest.xml:281`
  `<intent-filter>`
- `resources/AndroidManifest.xml:297`
  `<intent-filter>`
- `resources/AndroidManifest.xml:313`
  `<intent-filter>`
- `resources/AndroidManifest.xml:329`
  `<intent-filter>`
- `resources/AndroidManifest.xml:345`
  `<intent-filter>`
- `resources/AndroidManifest.xml:367`
  `<intent-filter>`
- `resources/AndroidManifest.xml:383`
  `<intent-filter>`
- `resources/AndroidManifest.xml:503`
  `<intent-filter>`
- `resources/AndroidManifest.xml:644`
  `<intent-filter>`
- `resources/AndroidManifest.xml:659`
  `<intent-filter>`
- `resources/AndroidManifest.xml:786`
  `<intent-filter>`
- `resources/AndroidManifest.xml:802`
  `<intent-filter>`

## BR060

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `sources/com/google/android/gms/internal/ads/zzaly.java:28`
  `zza = Cipher.getInstance("AES/CBC/PKCS5Padding");`
- `sources/com/google/android/gms/internal/ads/zzggv.java:13`
  `return zzghp.zza.zza("AES/ECB/NOPADDING");`
- `sources/com/google/android/gms/internal/ads/zzgib.java:29`
  `return zzghp.zza.zza("AES/ECB/NoPadding");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzlr.java:13`
  `return (Cipher) zzmh.zza.zza("AES/ECB/NOPADDING");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzmt.java:29`
  `return (Cipher) zzmh.zza.zza("AES/ECB/NoPadding");`

## BR061

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/core/view/inputmethod/EditorInfoCompat.java:198`
  `static int getProtocol(EditorInfo editorInfo) {`
- `sources/androidx/core/view/inputmethod/InputConnectionCompat.java:118`
  `int protocol = EditorInfoCompat.getProtocol(editorInfo);`
- `sources/androidx/lifecycle/LiveData.java:42`
  `LiveData.this.setValue(obj);`
- `sources/androidx/lifecycle/LiveData.java:64`
  `LiveData.this.setValue(obj2);`
- `sources/com/google/android/gms/auth/api/accounttransfer/AccountTransferClient.java:52`
  `public Task<Void> sendData(String str, byte[] bArr) {`
- `sources/com/google/android/gms/internal/ads/zzdp.java:81`
  `String protocol = url2.getProtocol();`
- `sources/com/google/android/gms/internal/ads/zzdp.java:86`
  `if (this.zzb || protocol.equals(url.getProtocol())) {`
- `sources/com/google/android/gms/internal/ads/zzdp.java:89`
  `String protocol2 = url.getProtocol();`
- `sources/com/google/firebase/database/core/Repo.java:491`
  `public void onDisconnectSetValue(final Path path, final Node node, final DatabaseReference.CompletionListener completionListener) {`
- `sources/com/google/gson/JsonPrimitive.java:14`
  `setValue(bool);`
- `sources/com/ikdong/weight/util/ad.java:125`
  `databaseReference.child(FirebaseUtil.getUid() + "/" + strValueOf).setValue(map, Long.valueOf(-weight.getDateAdded()));`
- `sources/okhttp3/Handshake.java:41`
  `String protocol = sSLSession.getProtocol();`
- `sources/okhttp3/internal/http2/Http2Connection.java:109`
  `public Protocol getProtocol() {`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:16`
  `final Method getProtocolMethod;`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:21`
  `this.getProtocolMethod = method2;`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:40`
  `String str = (String) this.getProtocolMethod.invoke(sSLSocket, new Object[0]);`

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
- `sources/androidx/recyclerview/widget/AdapterHelper.java:205`
  `int iUpdatePositionWithPostponed2 = updatePositionWithPostponed(updateOp.positionStart + (i * i5), updateOp.cmd);`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:206`
  `int i6 = updateOp.cmd;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:210`
  `UpdateOp updateOpObtainUpdateOp = obtainUpdateOp(updateOp.cmd, iUpdatePositionWithPostponed, i4, updateOp.payload);`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:213`
  `if (updateOp.cmd == 4) {`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:223`
  `UpdateOp updateOpObtainUpdateOp2 = obtainUpdateOp(updateOp.cmd, iUpdatePositionWithPostponed, i4, obj);`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:231`
  `int i2 = updateOp.cmd;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:509`
  `int cmd;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:515`
  `this.cmd = i;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:522`
  `int i = this.cmd;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:570`
  `updateOpAcquire.cmd = i;`
- `sources/androidx/room/RoomSQLiteQuery.java:96`
  `this.mBlobBindings = new byte[i2][];`
- `sources/androidx/work/impl/background/systemalarm/ConstraintsCommandHandler.java:44`
  `Logger.get().debug(TAG, String.format("Creating a delay_met command for workSpec with id (%s)", str2), new Throwable[0]);`
- `sources/androidx/work/impl/model/WorkProgressDao_Impl.java:37`
  `byte[] byteArrayInternal = Data.toByteArrayInternal(workProgress.mProgress);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:62`
  `byte[] byteArrayInternal = Data.toByteArrayInternal(workSpec.input);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:68`
  `byte[] byteArrayInternal2 = Data.toByteArrayInternal(workSpec.output);`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:94`
  `byte[] bArrContentUriTriggersToByteArray = WorkTypeConverters.contentUriTriggersToByteArray(constraints.getContentUriTriggers());`
- `sources/androidx/work/impl/model/WorkSpecDao_Impl.java:198`
  `byte[] byteArrayInternal = Data.toByteArrayInternal(data);`
- `sources/com/bumptech/glide/load/d/a/m.java:91`
  `byte[] bArr = (byte[]) this.l.a(65536, byte[].class);`
- `sources/com/google/android/gms/common/zzs.java:30`
  `byte[] bArr = iObjectWrapperZzd == null ? null : (byte[]) ObjectWrapper.unwrap(iObjectWrapperZzd);`
- `sources/com/google/android/gms/internal/ads/zzaaw.java:91`
  `byte[] bArrZzH = zzfdVar.zzH();`
- `sources/com/google/android/gms/internal/ads/zzabu.java:9`
  `private static final byte[] zza = zzfn.zzW("OpusHead");`
- `sources/com/google/android/gms/internal/ads/zzabu.java:272`
  `byte[] bArr = new byte[iZzf];`
- `sources/com/google/android/gms/internal/ads/zzafy.java:338`
  `byte[] bArrZzi = zzi(byteBuffer);`
- `sources/com/google/android/gms/internal/ads/zzafy.java:340`
  `byte[] bArrZzi2 = null;`
- `sources/com/google/android/gms/internal/ads/zzafy.java:341`
  `byte[] bArrZzi3 = null;`
- `sources/com/google/android/gms/internal/ads/zzafy.java:476`
  `byte[] bArrZzi4 = zzi(byteBufferZzf6);`
- `sources/com/google/android/gms/internal/ads/zzand.java:91`
  `byte[] bArrZzi = zzamv.zzi((String) zzbgq.zzc().zzb(zzblj.zzbI));`
- `sources/com/google/android/gms/internal/ads/zzasn.java:264`
  `byte[] r0 = new byte[r5]`
- `sources/com/google/android/gms/internal/ads/zzass.java:119`
  `byte[] r8 = new byte[r7]`
- `sources/com/google/android/gms/internal/ads/zzawn.java:8`
  `private static final byte[] zza = {0, 0, 0, 1};`
- `sources/com/google/android/gms/internal/ads/zzawn.java:29`
  `byte[] bArr2 = new byte[i2 + 4];`
- `sources/com/google/android/gms/internal/ads/zzazg.java:48`
  `return new byte[0];`
- `sources/com/google/android/gms/internal/ads/zzazg.java:52`
  `byte[] bArrDigest = this.zzb.digest();`

## BR064

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:199`
  `String name = xml.getName();`
- `sources/androidx/browser/customtabs/PostMessageServiceConnection.java:31`
  `intent.setClassName(str, PostMessageService.class.getName());`
- `sources/androidx/core/app/NotificationCompat.java:1363`
  `if (TextUtils.isEmpty(person.getName())) {`
- `sources/androidx/core/app/NotificationCompat.java:1371`
  `return this.mUser.getName();`
- `sources/androidx/core/app/NotificationCompat.java:1462`
  `messagingStyle = new Notification.MessagingStyle(this.mUser.getName());`
- `sources/androidx/core/app/NotificationCompat.java:1544`
  `CharSequence name = message.getPerson() == null ? "" : message.getPerson().getName();`
- `sources/androidx/core/app/NotificationCompat.java:1546`
  `name = this.mUser.getName();`
- `sources/androidx/core/app/NotificationCompat.java:1565`
  `bundle.putCharSequence(NotificationCompat.EXTRA_SELF_DISPLAY_NAME, this.mUser.getName());`
- `sources/androidx/core/content/FileProvider.java:167`
  `String name = xmlResourceParserLoadXmlMetaData.getName();`
- `sources/androidx/core/util/DebugUtils.java:12`
  `if ((simpleName == null || simpleName.length() <= 0) && (iLastIndexOf = (simpleName = obj.getClass().getName()).lastIndexOf(46)) > 0) {`
- `sources/androidx/savedstate/SavedStateRegistry.java:70`
  `this.mRecreatorProvider.add(cls.getName());`
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
- `sources/butterknife/ButterKnife.java:84`
  `String name = cls.getName();`
- `sources/com/activeandroid/Model.java:167`
  `Log.e(e3.getClass().getName(), e3);`
- `sources/com/bumptech/glide/b.java:152`
  `throw new IllegalStateException("Attempting to register a Glide v3 module. If you see this, you or one of your dependencies may be including Glide v3 even though you're using Glide v4. You'll need to find and remove (or update) the offending dependency. The v3 module name is: " + cVar2.getClass().ge...`
- `sources/com/bumptech/glide/load/b/x.java:76`
  `byte[] bytes = this.h.getName().getBytes(f779a);`
- `sources/com/google/android/gms/common/Feature.java:51`
  `return Objects.hashCode(getName(), Long.valueOf(getVersion()));`
- `sources/com/google/android/gms/common/Feature.java:56`
  `stringHelper.add(AppMeasurementSdk.ConditionalUserProperty.NAME, getName());`
- `sources/com/google/android/gms/fitness/data/BleDevice.java:68`
  `SafeParcelWriter.writeString(parcel, 1, getAddress(), false);`
- `sources/com/google/android/gms/fitness/data/DataSource.java:38`
  `sb.append(dataType.getName());`
- `sources/com/google/android/gms/fitness/request/DataTypeCreateRequest.java:102`
  `SafeParcelWriter.writeString(parcel, 1, getName(), false);`
- `sources/com/google/android/gms/fitness/request/zzbk.java:14`
  `private final String deviceAddress;`
- `sources/com/google/android/gms/fitness/request/zzbk.java:18`
  `this.deviceAddress = str;`
- `sources/com/google/android/gms/fitness/request/zzbk.java:23`
  `this.deviceAddress = str;`
- `sources/com/google/android/gms/fitness/request/zzbk.java:28`
  `return String.format("UnclaimBleDeviceRequest{%s}", this.deviceAddress);`
- `sources/com/google/android/gms/fitness/request/zzbk.java:34`
  `SafeParcelWriter.writeString(parcel, 2, this.deviceAddress, false);`
- `sources/com/google/android/gms/fitness/request/zzd.java:15`
  `private final String deviceAddress;`
- `sources/com/google/android/gms/fitness/request/zzd.java:20`
  `this.deviceAddress = str;`
- `sources/com/google/android/gms/fitness/request/zzd.java:26`
  `this.deviceAddress = str;`
- `sources/com/google/android/gms/fitness/request/zzd.java:32`
  `return String.format("ClaimBleDeviceRequest{%s %s}", this.deviceAddress, this.zzqk);`
- `sources/com/google/android/gms/fitness/request/zzd.java:38`
  `SafeParcelWriter.writeString(parcel, 1, this.deviceAddress, false);`
- `sources/com/google/android/gms/internal/ads/zzcni.java:41`
  `return new File(this.zzg, String.valueOf(file.getName()).concat(".done"));`
- `sources/com/google/android/gms/internal/ads/zzfod.java:170`
  `if (!hashSet.contains(file3.getName())) {`
- `sources/com/google/android/gms/internal/ads/zzfqr.java:36`
  `String name = obj.getClass().getName();`
- `sources/com/google/android/gms/internal/ads/zzfvg.java:533`
  `sb.append(objZzb.getClass().getName());`
- `sources/com/google/android/gms/internal/ads/zzfvg.java:750`
  `if (getClass().getName().startsWith("com.google.common.util.concurrent.")) {`
- `sources/com/google/android/gms/internal/ads/zzfvg.java:753`
  `sb.append(getClass().getName());`
- `sources/com/google/android/gms/internal/ads/zzfza.java:143`
  `if (concurrentMap.containsKey("type.googleapis.com/google.crypto.tink.EciesAeadHkdfPrivateKey") && (clsZzd = concurrentMap.get("type.googleapis.com/google.crypto.tink.EciesAeadHkdfPrivateKey").zzd()) != null && !clsZzd.getName().equals(zzfyiVar.getClass().getName())) {`
- `sources/com/google/android/gms/internal/ads/zzfza.java:145`
  `throw new GeneralSecurityException(String.format("public key manager corresponding to %s is already registered with %s, cannot be re-registered with %s", zzfyuVar.getClass().getName(), clsZzd.getName(), zzfyiVar.getClass().getName()));`
- `sources/com/google/android/gms/internal/ads/zzfza.java:188`
  `if (!zzfysVar.getClass().getName().equals(zzfysVar2.getClass().getName())) {`
- `sources/com/google/android/gms/internal/ads/zzfza.java:190`
  `throw new GeneralSecurityException(String.format("PrimitiveWrapper for primitive (%s) is already registered to be %s, cannot be re-registered with %s", clsZzb.getName(), zzfysVar2.getClass().getName(), zzfysVar.getClass().getName()));`
- `sources/com/google/android/gms/internal/ads/zzfza.java:243`
  `throw new GeneralSecurityException(String.format("typeUrl (%s) is already registered with %s, cannot be re-registered with %s", str, zzfyzVar.zzc().getName(), cls.getName()));`
- `sources/com/google/android/gms/internal/common/zzy.java:28`
  `String name = obj.getClass().getName();`
- `sources/com/google/android/gms/internal/fitness/zzco.java:47`
  `return unclaimBleDevice(googleApiClient, bleDevice.getAddress());`
- `sources/com/google/android/gms/internal/fitness/zzcs.java:19`
  `((zzbo) ((zzk) anyClient).getService()).zza(new com.google.android.gms.fitness.request.zzd(this.zzpd.getAddress(), this.zzpd, (zzcn) new zzei(this)));`
- `sources/com/google/android/gms/internal/fitness/zzey.java:44`
  `String name = obj.getClass().getName();`
- `sources/com/google/android/gms/internal/fitness/zzf.java:304`
  `sb.append(getClass().getName());`
- `sources/com/google/android/gms/internal/fitness/zzkq.java:123`
  `return "<" + getClass().getName() + '@' + Integer.toHexString(System.identityHashCode(this)) + " number=" + this.value + " name=" + name() + '>';`
- `sources/com/google/android/gms/internal/fitness/zzkq.java:151`
  `return "<" + getClass().getName() + '@' + Integer.toHexString(System.identityHashCode(this)) + " number=" + this.value + " name=" + name() + '>';`
- `sources/com/google/android/gms/internal/fitness/zzkq.java:327`
  `return "<" + getClass().getName() + '@' + Integer.toHexString(System.identityHashCode(this)) + " number=" + this.value + " name=" + name() + '>';`
- `sources/com/google/android/gms/internal/fitness/zzkq.java:429`
  `return "<" + getClass().getName() + '@' + Integer.toHexString(System.identityHashCode(this)) + " number=" + this.value + " name=" + name() + '>';`
- `sources/com/google/android/gms/internal/fitness/zzkq.java:461`
  `return "<" + getClass().getName() + '@' + Integer.toHexString(System.identityHashCode(this)) + " number=" + this.value + " name=" + name() + '>';`
- `sources/com/google/android/gms/internal/gtm/zzcs.java:28`
  `String lowerCase = xmlResourceParser.getName().toLowerCase(Locale.US);`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzae.java:36`
  `String name = obj.getClass().getName();`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzbq.java:112`
  `if (concurrentMap.containsKey(strZzc) && (clsZzd = ((zzbp) concurrentMap.get(strZzc)).zzd()) != null && !clsZzd.getName().equals(zzfgVar.getClass().getName())) {`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzbq.java:114`
  `throw new GeneralSecurityException(String.format("public key manager corresponding to %s is already registered with %s, cannot be re-registered with %s", zzfhVar.getClass().getName(), clsZzd.getName(), zzfgVar.getClass().getName()));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzbq.java:152`
  `if (!zzbjVar.getClass().getName().equals(zzbjVar2.getClass().getName())) {`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzbq.java:154`
  `throw new GeneralSecurityException(String.format("PrimitiveWrapper for primitive (%s) is already registered to be %s, cannot be re-registered with %s", clsZzb.getName(), zzbjVar2.getClass().getName(), zzbjVar.getClass().getName()));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzbq.java:201`
  `throw new GeneralSecurityException(String.format("typeUrl (%s) is already registered with %s, cannot be re-registered with %s", str, zzbpVar.zzc().getName(), cls.getName()));`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzti.java:156`
  `return new FirebaseAuthMultiFactorException(str, str2, new zzae(arrayList, zzag.zzb(zzpsVar.zzc(), zzpsVar.zzb()), firebaseAuth.getApp().getName(), zzpsVar.zza(), (zzx) firebaseUser));`
- `sources/com/google/android/material/animation/MotionSpec.java:137`
  `return '\n' + getClass().getName() + '{' + Integer.toHexString(System.identityHashCode(this)) + " timings: " + this.timings + "}\n";`
- `sources/com/google/android/material/animation/MotionTiming.java:108`
  `return '\n' + getClass().getName() + '{' + Integer.toHexString(System.identityHashCode(this)) + " delay: " + getDelay() + " duration: " + getDuration() + " interpolator: " + getInterpolator().getClass() + " repeatCount: " + getRepeatCount() + " repeatMode: " + getRepeatMode() + "}\n";`
- `sources/com/google/firebase/FirebaseApp.java:329`
  `Log.i(LOG_TAG, "Device in Direct Boot Mode: postponing initialization of Firebase APIs for app " + getName());`
- `sources/com/google/firebase/FirebaseApp.java:333`
  `Log.i(LOG_TAG, "Device unlocked: initializing all Firebase APIs for app " + getName());`
- `sources/com/google/firebase/auth/internal/zzbg.java:82`
  `jSONObject.put("applicationName", zzxVar.zza().getName());`
- `sources/com/google/firebase/auth/internal/zzbm.java:60`
  `editorEdit.putString("firebaseAppName", firebaseAuth.getApp().getName());`
- `sources/com/google/firebase/auth/internal/zzbm.java:69`
  `editorEdit.putString("firebaseAppName", firebaseAuth.getApp().getName());`
- `sources/com/google/firebase/auth/internal/zzx.java:40`
  `this.zzc = firebaseApp.getName();`
- `sources/com/google/firebase/database/FirebaseDatabaseComponent.java:34`
  `databaseConfig.setSessionPersistenceKey(this.app.getName());`
- `sources/com/google/firebase/database/android/SqlPersistenceStorageEngine.java:264`
  `iRemoveNested2 += removeNested(SERVER_CACHE_TABLE, path.child(namedNode.getName()));`
- `sources/com/google/firebase/database/android/SqlPersistenceStorageEngine.java:265`
  `iSaveNested2 += saveNested(path.child(namedNode.getName()), namedNode.getNode());`
- `sources/com/google/firebase/database/android/SqlPersistenceStorageEngine.java:590`
  `iSaveNested += saveNested(path.child(namedNode.getName()), namedNode.getNode());`
- `sources/com/google/firebase/database/core/SyncPoint.java:98`
  `hashSet.add(it.next().getName());`
- `sources/com/google/firebase/database/core/SyncTree.java:429`
  `if (!nodeEmpty.hasChild(namedNode.getName())) {`
- `sources/com/google/firebase/database/core/SyncTree.java:430`
  `nodeEmpty = nodeEmpty.updateImmediateChild(namedNode.getName(), namedNode.getNode());`
- `sources/com/google/firebase/database/core/WriteTree.java:175`
  `nodeEmpty = nodeEmpty.updateImmediateChild(namedNode3.getName(), namedNode3.getNode());`

## BR067

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/com/github/mikephil/charting/charts/BarLineChartBase.java:852`
  `public void setPinchZoom(boolean z) {`
- `sources/com/ikdong/weight/widget/fragment/ChartAnalysisFragment.java:658`
  `this.barChartView.setPinchZoom(false);`

## BR068

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/com/google/android/gms/auth/api/accounttransfer/AccountTransferStatusCodes.java:7`
  `public static final int CHALLENGE_NOT_ALLOWED = 20503;`
- `sources/com/google/android/gms/auth/api/accounttransfer/AccountTransferStatusCodes.java:24`
  `case CHALLENGE_NOT_ALLOWED /* 20503 */:`
- `sources/com/google/android/gms/auth/api/accounttransfer/AccountTransferStatusCodes.java:25`
  `return "CHALLENGE_NOT_ALLOWED";`
- `sources/com/google/android/gms/auth/api/accounttransfer/DeviceMetaData.java:27`
  `public boolean isChallengeAllowed() {`
- `sources/com/google/android/gms/auth/api/accounttransfer/DeviceMetaData.java:41`
  `SafeParcelWriter.writeBoolean(parcel, 4, isChallengeAllowed());`
- `sources/com/google/android/gms/internal/auth/zzby.java:26`
  `CHALLENGE_REQUIRED("ChallengeRequired"),`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzti.java:79`
  `sparseArray.put(17078, new Pair("ERROR_SECOND_FACTOR_REQUIRED", "Please complete a second factor challenge to finish signing into this account."));`
- `sources/com/ikdong/weight/R.java:5732`
  `public static final int content_challenge21_day = 0x7f0c005f;`
- `sources/com/ikdong/weight/R.java:5758`
  `public static final int dialog_challenge_pick = 0x7f0c0079;`
- `sources/com/ikdong/weight/R.java:5917`
  `public static final int list_plan_cal_item_challenge = 0x7f0c0118;`
- `sources/com/ikdong/weight/R.java:6810`
  `public static final int label_edit_challenge = 0x7f100256;`
- `sources/com/ikdong/weight/activity/Challenge21DayActivity.java:135`
  `this.f1345a.setNavigationOnClickListener(new View.OnClickListener() { // from class: com.ikdong.weight.activity.Challenge21DayActivity.4`
- `sources/com/ikdong/weight/activity/Challenge21DayActivity.java:138`
  `Challenge21DayActivity.this.finish();`
- `sources/com/ikdong/weight/activity/Challenge30AbsActivity.java:136`
  `this.f1353a.setNavigationOnClickListener(new View.OnClickListener() { // from class: com.ikdong.weight.activity.Challenge30AbsActivity.4`
- `sources/com/ikdong/weight/activity/Challenge30AbsActivity.java:139`
  `Challenge30AbsActivity.this.finish();`
- `sources/com/ikdong/weight/activity/ChallengeActivity.java:52`
  `setContentView(R.layout.challenges_toolbar);`
- `sources/com/ikdong/weight/activity/ChallengeActivity.java:55`
  `toolbar.setTitle(R.string.label_challenge);`
- `sources/com/ikdong/weight/activity/ChallengeActivity.java:58`
  `this.f1361a.setNavigationOnClickListener(new View.OnClickListener() { // from class: com.ikdong.weight.activity.-$$Lambda$ChallengeActivity$YvJFZ_V7vzUhRIUxElNKHSE42Tw`
- `sources/com/ikdong/weight/activity/ChallengeActivity.java:64`
  `runOnUiThread(new Runnable() { // from class: com.ikdong.weight.activity.ChallengeActivity.1`
- `sources/com/ikdong/weight/activity/ChallengeActivity.java:67`
  `ChallengeActivity.this.a();`
- `sources/com/ikdong/weight/activity/ChallengeActivity.java:173`
  `subMenuAddSubMenu.add(1, 2, 1, R.string.label_challenge_pick).setOnMenuItemClickListener(new MenuItem.OnMenuItemClickListener() { // from class: com.ikdong.weight.activity.ChallengeActivity.3`
- `sources/com/ikdong/weight/activity/ChallengeActivity.java:176`
  `ChallengeActivity.this.new a().execute(new Integer[0]);`
- `sources/com/ikdong/weight/activity/LogActivity.java:66`
  `MenuItem menuItemAdd2 = menu.add(0, R.id.menu_challenge, 0, R.string.label_recipe);`
- `sources/com/ikdong/weight/activity/LogActivity.java:72`
  `LogActivity.this.startActivity(new Intent(LogActivity.this, (Class<?>) ChallengeActivity.class));`
- `sources/com/ikdong/weight/model/CalItem.java:12`
  `public static final int CATE_CHALLENGE = 2;`
- `sources/com/ikdong/weight/model/Challenge.java:12`
  `@Table(name = "Challenge")`
- `sources/com/ikdong/weight/model/Challenge.java:13`
  `public class Challenge extends Model {`
- `sources/com/ikdong/weight/model/Image.java:20`
  `public static final int CATE_CHALLENGE = 2;`
- `sources/com/ikdong/weight/widget/a/g.java:37`
  `private DatabaseReference f2214c = FirebaseUtil.buildRef("guide/challenges/collection");`
- `sources/com/ikdong/weight/widget/a/h.java:39`
  `private DatabaseReference f2224c = FirebaseUtil.buildRef("guide/challenges/collection");`
- `sources/com/ikdong/weight/widget/b/d.java:51`
  `View viewInflate = this.f2306b.inflate(R.layout.grid_challenge_item, (ViewGroup) null);`
- `sources/com/ikdong/weight/widget/fragment/e.java:13`
  `import com.ikdong.weight.model.Challenge;`
- `sources/com/ikdong/weight/widget/fragment/e.java:27`
  `private Challenge f4166c;`
- `sources/com/ikdong/weight/widget/fragment/e.java:41`
  `if (challengeTitle.contains("{0}")) {`
- `sources/com/ikdong/weight/widget/fragment/e.java:42`
  `challengeTitle = challengeTitle.replace("{0}", this.f4166c.getValueParam() > 0 ? String.valueOf(this.f4166c.getValueParam()) : "1");`
- `sources/com/ikdong/weight/widget/fragment/e.java:44`
  `this.f4167d.setText(challengeTitle);`
- `sources/com/ikdong/weight/widget/fragment/k.java:298`
  `View viewInflate = this.e.inflate(R.layout.list_plan_cal_item_challenge, viewGroup, false);`
- `sources/com/ikdong/weight/widget/fragment/SolutionListFragment.java:61`
  `((ImageView) viewInflate.findViewById(R.id.sl_challenge_fitness_icon)).setColorFilter(Color.parseColor("#ffffff"), PorterDuff.Mode.SRC_ATOP);`
- `sources/com/ikdong/weight/widget/fragment/challenge/b.java:105`
  `view = this.j.inflate(R.layout.discover_list_challenge_item, viewGroup, false);`
- `sources/com/ikdong/weight/widget/fragment/challenge/b.java:111`
  `Picasso.with(this.f).load("http://wta-backup.oss-cn-shanghai.aliyuncs.com/challenge/" + this.i.get(i) + ".png").placeholder(R.drawable.placeholder).into(imageView);`
- `sources/com/ikdong/weight/widget/fragment/challenge/c.java:37`
  `viewFindViewById.findViewById(R.id.ads_content).setOnClickListener(new View.OnClickListener() { // from class: com.ikdong.weight.widget.fragment.challenge.c.1`
- `sources/com/ikdong/weight/widget/fragment/challenge/c.java:63`
  `viewFindViewById.findViewById(R.id.ads_content_1).setOnClickListener(new View.OnClickListener() { // from class: com.ikdong.weight.widget.fragment.challenge.c.2`
- `sources/com/ikdong/weight/widget/fragment/challenge/ChallengeDetailFragment.java:85`
  `Picasso.with(getContext()).load("http://wta-backup.oss-cn-shanghai.aliyuncs.com/challenge/" + this.f4135c + ".png").placeholder(R.drawable.placeholder).into(this.coverView);`
- `sources/okhttp3/Challenge.java:13`
  `public final class Challenge {`
- `sources/okhttp3/Challenge.java:17`
  `public Challenge(String str, Map<String, String> map) {`
- `sources/okhttp3/Challenge.java:28`
  `public Challenge(String str, String str2) {`
- `sources/okhttp3/Challenge.java:66`
  `if (obj instanceof Challenge) {`
- `sources/okhttp3/Challenge.java:67`
  `Challenge challenge = (Challenge) obj;`
- `sources/okhttp3/Challenge.java:68`
  `if (challenge.scheme.equals(this.scheme) && challenge.authParams.equals(this.authParams)) {`
- `sources/okhttp3/Response.java:153`
  `public List<Challenge> challenges() {`
- `sources/okhttp3/internal/http/HttpHeaders.java:107`
  `public static List<Challenge> parseChallenges(Headers headers, String str) {`
- `sources/okhttp3/internal/http/HttpHeaders.java:111`
  `parseChallengeHeader(arrayList, new c().b(headers.value(i)));`
- `sources/okhttp3/internal/http/HttpHeaders.java:130`
  `private static void parseChallengeHeader(java.util.List<okhttp3.Challenge> r8, c.c r9) {`
- `sources/okhttp3/internal/http/HttpHeaders.java:135`
  `throw new UnsupportedOperationException("Method not decompiled: okhttp3.internal.http.HttpHeaders.parseChallengeHeader(java.util.List, c.c):void");`

## BR071

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:48`
  `android:allowBackup="true"`

## BR073

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:656`
  `public void restoreToolbarHierarchyState(SparseArray<Parcelable> sparseArray) {`
- `sources/androidx/appcompat/widget/ActionBarOverlayLayout.java:658`
  `this.mDecorToolbar.restoreHierarchyState(sparseArray);`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:463`
  `java.lang.String r5 = r2.getAttributeValue(r6, r5)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:465`
  `java.lang.String r7 = r2.getAttributeValue(r6, r7)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:466`
  `long r7 = java.lang.Long.parseLong(r7)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:468`
  `java.lang.String r6 = r2.getAttributeValue(r6, r9)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:469`
  `float r6 = java.lang.Float.parseFloat(r6)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:470`
  `androidx.appcompat.widget.ActivityChooserModel$HistoricalRecord r9 = new androidx.appcompat.widget.ActivityChooserModel$HistoricalRecord     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:471`
  `r9.<init>(r5, r7, r6)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:472`
  `r3.add(r9)     // Catch: java.lang.Throwable -> L84 java.io.IOException -> L86 org.xmlpull.v1.XmlPullParserException -> La0`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:203`
  `TextViewCompat.setCompoundDrawableTintMode(this.mView, DrawableUtils.parseTintMode(tintTypedArrayObtainStyledAttributes4.getInt(R.styleable.AppCompatTextView_drawableTintMode, -1), null));`
- `sources/androidx/core/content/res/ColorStateListInflaterCompat.java:17`
  `import org.xmlpull.v1.XmlPullParser;`
- `sources/androidx/core/content/res/ColorStateListInflaterCompat.java:18`
  `import org.xmlpull.v1.XmlPullParserException;`
- `sources/androidx/core/content/res/FontResourcesParserCompat.java:21`
  `public class FontResourcesParserCompat {`
- `sources/androidx/core/content/res/FontResourcesParserCompat.java:217`
  `arrayList.add(Base64.decode(str, 0));`
- `sources/androidx/core/content/res/FontResourcesParserCompat.java:228`
  `TypedArray typedArrayObtainAttributes = resources.obtainAttributes(Xml.asAttributeSet(xmlPullParser), R.styleable.FontFamilyFont);`
- `sources/androidx/core/content/res/ResourcesCompat.java:25`
  `private static final WeakHashMap<ColorStateListCacheKey, SparseArray<ColorStateListCacheEntry>> sColorStateCaches = new WeakHashMap<>(0);`
- `sources/androidx/core/graphics/TypefaceCompatApi21Impl.java:145`
  `public Typeface createFromFontFamilyFilesResourceEntry(Context context, FontResourcesParserCompat.FontFamilyFilesResourceEntry fontFamilyFilesResourceEntry, Resources resources, int i) throws NoSuchMethodException {`
- `sources/androidx/core/graphics/TypefaceCompatApi21Impl.java:147`
  `for (FontResourcesParserCompat.FontFileResourceEntry fontFileResourceEntry : fontFamilyFilesResourceEntry.getEntries()) {`
- `sources/androidx/core/graphics/TypefaceCompatApi24Impl.java:10`
  `import androidx.core.content.res.FontResourcesParserCompat;`
- `sources/androidx/core/graphics/TypefaceCompatApi24Impl.java:116`
  `public Typeface createFromFontFamilyFilesResourceEntry(Context context, FontResourcesParserCompat.FontFamilyFilesResourceEntry fontFamilyFilesResourceEntry, Resources resources, int i) {`
- `sources/androidx/core/graphics/TypefaceCompatApi24Impl.java:121`
  `for (FontResourcesParserCompat.FontFileResourceEntry fontFileResourceEntry : fontFamilyFilesResourceEntry.getEntries()) {`
- `sources/androidx/core/graphics/TypefaceCompatApi26Impl.java:140`
  `for (FontResourcesParserCompat.FontFileResourceEntry fontFileResourceEntry : fontFamilyFilesResourceEntry.getEntries()) {`
- `sources/androidx/core/graphics/TypefaceCompatApi29Impl.java:133`
  `FontResourcesParserCompat.FontFileResourceEntry fontFileResourceEntry = entries[i2];`
- `sources/androidx/core/graphics/TypefaceCompatBaseImpl.java:20`
  `private ConcurrentHashMap<Long, FontResourcesParserCompat.FontFamilyFilesResourceEntry> mFontFamilies = new ConcurrentHashMap<>();`
- `sources/androidx/core/graphics/TypefaceCompatBaseImpl.java:122`
  `private FontResourcesParserCompat.FontFileResourceEntry findBestEntry(FontResourcesParserCompat.FontFamilyFilesResourceEntry fontFamilyFilesResourceEntry, int i) {`
- `sources/androidx/core/graphics/TypefaceCompatBaseImpl.java:123`
  `return (FontResourcesParserCompat.FontFileResourceEntry) findBestFont(fontFamilyFilesResourceEntry.getEntries(), i, new StyleExtractor<FontResourcesParserCompat.FontFileResourceEntry>() { // from class: androidx.core.graphics.TypefaceCompatBaseImpl.2`
- `sources/androidx/core/graphics/TypefaceCompatBaseImpl.java:125`
  `public int getWeight(FontResourcesParserCompat.FontFileResourceEntry fontFileResourceEntry) {`
- `sources/androidx/core/graphics/TypefaceCompatBaseImpl.java:130`
  `public boolean isItalic(FontResourcesParserCompat.FontFileResourceEntry fontFileResourceEntry) {`
- `sources/androidx/core/graphics/TypefaceCompatBaseImpl.java:163`
  `FontResourcesParserCompat.FontFamilyFilesResourceEntry getFontFamily(Typeface typeface) {`
- `sources/androidx/core/graphics/drawable/IconCompat.java:405`
  `return new BitmapDrawable(context.getResources(), BitmapFactory.decodeByteArray((byte[]) this.mObj1, this.mInt1, this.mInt2));`
- `sources/androidx/core/graphics/drawable/IconCompat.java:409`
  `return new BitmapDrawable(context.getResources(), BitmapFactory.decodeStream(uriInputStream));`
- `sources/androidx/core/net/ParseException.java:4`
  `public class ParseException extends RuntimeException {`
- `sources/androidx/core/net/ParseException.java:7`
  `ParseException(String str) {`
- `sources/androidx/core/provider/FontProvider.java:126`
  `return FontResourcesParserCompat.readCerts(resources, fontRequest.getCertificatesArrayResId());`
- `sources/androidx/core/view/DisplayCompat.java:70`
  `private static Point parsePhysicalDisplaySizeFromSystemProperties(String str, Display display) {`
- `sources/androidx/core/view/DisplayCompat.java:79`
  `return parseDisplaySize(systemProperty);`
- `sources/androidx/core/view/DisplayCompat.java:88`
  `physicalDisplaySizeFromSystemProperties = parsePhysicalDisplaySizeFromSystemProperties("sys.display-size", display);`
- `sources/androidx/core/view/DisplayCompat.java:90`
  `physicalDisplaySizeFromSystemProperties = parsePhysicalDisplaySizeFromSystemProperties("vendor.display-size", display);`
- `sources/androidx/customview/widget/ExploreByTouchHelper.java:43`
  `return sparseArrayCompat.size();`
- `sources/androidx/customview/widget/ExploreByTouchHelper.java:222`
  `return sparseArrayCompat;`
- `sources/androidx/fragment/app/FragmentTransition.java:677`
  `sparseArray.put(i, fragmentContainerTransition2);`
- `sources/androidx/print/PrintHelper.java:407`
  `options2.inJustDecodeBounds = true;`
- `sources/androidx/recyclerview/widget/RecyclerView.java:6777`
  `private SparseArray<Object> mData;`
- `sources/androidx/transition/ChangeBounds.java:131`
  `boolean namedBoolean = TypedArrayUtils.getNamedBoolean(typedArrayObtainStyledAttributes, (XmlResourceParser) attributeSet, "resizeClip", 0, false);`
- `sources/androidx/transition/ChangeTransform.java:72`
  `XmlPullParser xmlPullParser = (XmlPullParser) attributeSet;`
- `sources/androidx/transition/ChangeTransform.java:73`
  `this.mUseOverlay = TypedArrayUtils.getNamedBoolean(typedArrayObtainStyledAttributes, xmlPullParser, "reparentWithOverlay", 1, true);`
- `sources/androidx/transition/ChangeTransform.java:74`
  `this.mReparent = TypedArrayUtils.getNamedBoolean(typedArrayObtainStyledAttributes, xmlPullParser, "reparent", 0, true);`
- `sources/androidx/transition/PatternPathMotion.java:11`
  `import org.xmlpull.v1.XmlPullParser;`
- `sources/androidx/transition/PatternPathMotion.java:32`
  `String namedString = TypedArrayUtils.getNamedString(typedArrayObtainStyledAttributes, (XmlPullParser) attributeSet, "patternPathData", 0);`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:490`
  `ColorStateList namedColorStateList = TypedArrayUtils.getNamedColorStateList(typedArray, xmlPullParser, theme, "tint", 1);`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:494`
  `vectorDrawableCompatState.mAutoMirrored = TypedArrayUtils.getNamedBoolean(typedArray, xmlPullParser, "autoMirrored", 5, vectorDrawableCompatState.mAutoMirrored);`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:495`
  `vPathRenderer.mViewportWidth = TypedArrayUtils.getNamedFloat(typedArray, xmlPullParser, "viewportWidth", 7, vPathRenderer.mViewportWidth);`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:496`
  `vPathRenderer.mViewportHeight = TypedArrayUtils.getNamedFloat(typedArray, xmlPullParser, "viewportHeight", 8, vPathRenderer.mViewportHeight);`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:498`
  `throw new XmlPullParserException(typedArray.getPositionDescription() + "<vector> tag requires viewportWidth > 0");`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:501`
  `throw new XmlPullParserException(typedArray.getPositionDescription() + "<vector> tag requires viewportHeight > 0");`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:506`
  `throw new XmlPullParserException(typedArray.getPositionDescription() + "<vector> tag requires width > 0");`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:509`
  `throw new XmlPullParserException(typedArray.getPositionDescription() + "<vector> tag requires height > 0");`
- `sources/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat.java:511`
  `vPathRenderer.setAlpha(TypedArrayUtils.getNamedFloat(typedArray, xmlPullParser, "alpha", 4, vPathRenderer.getAlpha()));`
- `sources/androidx/versionedparcelable/VersionedParcel.java:11`
  `import android.util.SparseBooleanArray;`
- `sources/androidx/versionedparcelable/VersionedParcel.java:250`
  `public void writeSparseBooleanArray(SparseBooleanArray sparseBooleanArray, int i) {`
- `sources/androidx/versionedparcelable/VersionedParcel.java:252`
  `if (sparseBooleanArray == null) {`
- `sources/com/activeandroid/Model.java:52`
  `if (!type.equals(parserForType.getSerializedType())) {`
- `sources/com/activeandroid/Model.java:53`
  `Log.w(String.format("TypeSerializer returned wrong type: expected a %s but got a %s", parserForType.getSerializedType(), type));`
- `sources/com/activeandroid/Model.java:121`
  `if (parserForType != null) {`
- `sources/com/activeandroid/Model.java:122`
  `type = parserForType.getSerializedType();`
- `sources/com/bumptech/glide/load/f.java:3`
  `import com.bumptech.glide.load.ImageHeaderParser;`
- `sources/com/bumptech/glide/load/f.java:12`
  `public static ImageHeaderParser.ImageType a(List<ImageHeaderParser> list, InputStream inputStream, com.bumptech.glide.load.b.a.b bVar) throws IOException {`
- `sources/com/bumptech/glide/load/f.java:32`
  `return ImageHeaderParser.ImageType.UNKNOWN;`
- `sources/com/bumptech/glide/load/f.java:35`
  `public static ImageHeaderParser.ImageType a(List<ImageHeaderParser> list, ByteBuffer byteBuffer) {`
- `sources/com/bumptech/glide/load/f.java:37`
  `return ImageHeaderParser.ImageType.UNKNOWN;`
- `sources/com/bumptech/glide/load/f.java:41`
  `ImageHeaderParser.ImageType imageTypeA = list.get(i).a(byteBuffer);`
- `sources/com/bumptech/glide/load/f.java:42`
  `if (imageTypeA != ImageHeaderParser.ImageType.UNKNOWN) {`
- `sources/com/bumptech/glide/load/f.java:46`
  `return ImageHeaderParser.ImageType.UNKNOWN;`
- `sources/com/bumptech/glide/load/ImageHeaderParser.java:7`
  `public interface ImageHeaderParser {`
- `sources/com/bumptech/glide/load/b/x.java:82`
  `return "ResourceCacheKey{sourceKey=" + this.f560d + ", signature=" + this.e + ", width=" + this.f + ", height=" + this.g + ", decodedResourceClass=" + this.h + ", transformation='" + this.j + "', options=" + this.i + '}';`
- `sources/com/bumptech/glide/load/c/e.java:106`
  `return new ByteArrayInputStream(Base64.decode(str.substring(iIndexOf + 1), 0));`
- `sources/com/bumptech/glide/load/d/a.java:65`
  `if (Log.isLoggable("ImageDecoder", 2)) {`
- `sources/com/bumptech/glide/load/d/a.java:66`
  `Log.v("ImageDecoder", "Resizing from [" + size.getWidth() + "x" + size.getHeight() + "] to [" + iRound + "x" + iRound2 + "] scaleFactor: " + fA);`
- `sources/com/bumptech/glide/load/d/a.java:68`
  `imageDecoder.setTargetSize(iRound, iRound2);`

## BR074

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/android/support/v4/media/session/MediaControllerCompat.java:1531`
  `synchronized (mediaControllerImplApi21.mLock) {`
- `sources/android/support/v4/os/ResultReceiver.java:93`
  `synchronized (this) {`
- `sources/androidx/appcompat/R.java:1724`
  `public static final int[] SearchView = {android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.inputType, android.R.attr.imeOptions, com.ikdong.weight.R.attr.closeIcon, com.ikdong.weight.R.attr.commitIcon, com.ikdong.weight.R.attr.defaultQueryHint, com.ikdong.weight.R.attr.goIcon, com.ikd...`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2352`
  `return (Build.VERSION.SDK_INT < 21 || !this.mPowerManager.isPowerSaveMode()) ? 1 : 2;`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:203`
  `canvas.save();`
- `sources/androidx/appcompat/view/menu/ActionMenuItemView.java:99`
  `this.mSavedPaddingLeft = i;`
- `sources/androidx/appcompat/widget/ActionMenuPresenter.java:482`
  `public Parcelable onSaveInstanceState() {`
- `sources/androidx/appcompat/widget/ActionMenuPresenter.java:483`
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
- `sources/androidx/appcompat/widget/AppCompatRatingBar.java:30`
  `protected synchronized void onMeasure(int i, int i2) {`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:136`
  `int iSave = canvas.save();`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:142`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:27`
  `private boolean mAsyncFontPending;`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:223`
  `if (this.mAsyncFontPending) {`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:306`
  `this.mAsyncFontPending = this.mFontTypeface == null;`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:266`
  `synchronized (rectF) {`
- `sources/androidx/appcompat/widget/ButtonBarLayout.java:25`
  `saveAttributeDataForStyleable(context, R.styleable.ButtonBarLayout, attributeSet, typedArrayObtainStyledAttributes, 0, 0);`
- `sources/androidx/appcompat/widget/SearchView.java:90`
  `private final View mSubmitArea;`
- `sources/androidx/appcompat/widget/SearchView.java:91`
  `private boolean mSubmitButtonEnabled;`
- `sources/androidx/appcompat/widget/SwitchCompat.java:857`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:34`
  `int iSave = canvas.save();`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:46`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:208`
  `int iSave = canvas.save();`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:222`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:223`
  `int iSave3 = canvas.save();`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:230`
  `canvas.restoreToCount(iSave3);`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:231`
  `int iSave4 = canvas.save();`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:238`
  `canvas.restoreToCount(iSave4);`
- `sources/androidx/collection/LruCache.java:102`
  `throw new java.lang.IllegalStateException(getClass().getName() + ".sizeOf() is reporting inconsistent results!");`
- `sources/androidx/collection/LruCache.java:159`
  `java.lang.String r1 = ".sizeOf() is reporting inconsistent results!"`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:129`
  `sRectPool = new Pools.SynchronizedPool(12);`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:819`
  `int iSave = canvas.save();`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:824`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/core/content/ContextCompat.java:78`
  `private static final Object sSync = new Object();`
- `sources/androidx/core/content/ContextCompat.java:143`
  `synchronized (sLock) {`
- `sources/androidx/core/content/pm/ShortcutManagerCompat.java:186`
  `public static void reportShortcutUsed(Context context, String str) {`
- `sources/androidx/core/content/res/FontResourcesParserCompat.java:23`
  `public static final int FETCH_STRATEGY_ASYNC = 1;`
- `sources/androidx/core/location/LocationManagerCompat.java:147`
  `synchronized (sLocationListeners) {`
- `sources/androidx/core/location/LocationManagerCompat.java:156`
  `synchronized (sLocationListeners) {`
- `sources/androidx/core/location/LocationManagerCompat.java:190`
  `synchronized (weakHashMap) {`
- `sources/androidx/core/location/LocationManagerCompat.java:260`
  `synchronized (GnssLazyLoader.sGnssStatusListeners) {`
- `sources/androidx/core/location/LocationManagerCompat.java:269`
  `synchronized (GnssLazyLoader.sGnssStatusListeners) {`
- `sources/androidx/core/location/LocationManagerCompat.java:278`
  `synchronized (GnssLazyLoader.sGnssStatusListeners) {`
- `sources/androidx/core/provider/FontRequestWorker.java:31`
  `static Typeface requestFontSync(final Context context, final FontRequest fontRequest, CallbackWithHandler callbackWithHandler, final int i, int i2) {`
- `sources/androidx/core/provider/FontRequestWorker.java:39`
  `TypefaceResult fontSync = getFontSync(strCreateCacheId, context, fontRequest, i);`
- `sources/androidx/core/provider/FontRequestWorker.java:40`
  `callbackWithHandler.onTypefaceResult(fontSync);`
- `sources/androidx/core/provider/FontRequestWorker.java:41`
  `return fontSync.mTypeface;`
- `sources/androidx/core/provider/FontRequestWorker.java:44`
  `TypefaceResult typefaceResult = (TypefaceResult) RequestExecutor.submit(DEFAULT_EXECUTOR_SERVICE, new Callable<TypefaceResult>() { // from class: androidx.core.provider.FontRequestWorker.1`
- `sources/androidx/core/provider/FontRequestWorker.java:48`
  `return FontRequestWorker.getFontSync(strCreateCacheId, context, fontRequest, i);`
- `sources/androidx/core/provider/FontRequestWorker.java:59`
  `static Typeface requestFontAsync(final Context context, final FontRequest fontRequest, final int i, Executor executor, final CallbackWithHandler callbackWithHandler) {`
- `sources/androidx/core/provider/FontRequestWorker.java:75`
  `synchronized (LOCK) {`
- `sources/androidx/core/provider/FontRequestWorker.java:90`
  `return FontRequestWorker.getFontSync(strCreateCacheId, context, fontRequest, i);`
- `sources/androidx/core/provider/FontRequestWorker.java:102`
  `synchronized (FontRequestWorker.LOCK) {`
- `sources/androidx/core/provider/FontRequestWorker.java:122`
  `static TypefaceResult getFontSync(String str, Context context, FontRequest fontRequest, int i) {`
- `sources/androidx/core/provider/FontsContractCompat.java:83`
  `FontRequestWorker.requestFontAsync(context.getApplicationContext(), fontRequest, 0, RequestExecutor.createHandlerExecutor(handler), callbackWithHandler);`
- `sources/androidx/core/provider/FontsContractCompat.java:166`
  `public static Typeface getFontSync(Context context, FontRequest fontRequest, ResourcesCompat.FontCallback fontCallback, Handler handler, boolean z, int i, int i2) {`
- `sources/androidx/core/view/ViewCompat.java:185`
  `public static void saveAttributeDataForStyleable(View view, Context context, int[] iArr, AttributeSet attributeSet, TypedArray typedArray, int i, int i2) {`
- `sources/androidx/core/view/ViewCompat.java:187`
  `Api29Impl.saveAttributeDataForStyleable(view, context, iArr, attributeSet, typedArray, i, i2);`
- `sources/androidx/core/widget/NestedScrollView.java:61`
  `private SavedState mSavedState;`
- `sources/androidx/core/widget/NestedScrollView.java:1249`
  `scrollTo(getScrollX(), this.mSavedState.scrollPosition);`
- `sources/androidx/core/widget/NestedScrollView.java:1250`
  `this.mSavedState = null;`
- `sources/androidx/core/widget/NestedScrollView.java:1334`
  `int iSave = canvas.save();`
- `sources/androidx/core/widget/NestedScrollView.java:1353`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/core/widget/NestedScrollView.java:1358`
  `int iSave2 = canvas.save();`
- `sources/androidx/core/widget/NestedScrollView.java:1376`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/drawerlayout/widget/DrawerLayout.java:863`
  `int iSave = canvas.save();`
- `sources/androidx/drawerlayout/widget/DrawerLayout.java:888`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/fragment/app/Fragment.java:161`
  `public void onSaveInstanceState(Bundle bundle) {`
- `sources/androidx/fragment/app/FragmentActivity.java:68`
  `this.mFragments.noteStateNotSaved();`
- `sources/androidx/fragment/app/FragmentActivity.java:139`
  `Log.w(TAG, "Invalid requestCode mapping in savedInstanceState.");`
- `sources/androidx/fragment/app/FragmentActivity.java:272`
  `Parcelable parcelableSaveAllState = this.mFragments.saveAllState();`
- `sources/androidx/fragment/app/FragmentActivity.java:273`
  `if (parcelableSaveAllState != null) {`
- `sources/androidx/fragment/app/FragmentActivity.java:274`
  `bundle.putParcelable(FRAGMENTS_TAG, parcelableSaveAllState);`
- `sources/androidx/fragment/app/FragmentActivity.java:395`
  `this.mFragments.noteStateNotSaved();`
- `sources/androidx/fragment/app/FragmentManagerImpl.java:86`
  `boolean mStateSaved;`

## BR075

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/androidx/appcompat/R.java:1341`
  `public static final int AppCompatTextView_autoSizePresetSizes = 0x00000003;`
- `sources/androidx/appcompat/R.java:1705`
  `public static final int[] AppCompatTextView = {android.R.attr.textAppearance, com.ikdong.weight.R.attr.autoSizeMaxTextSize, com.ikdong.weight.R.attr.autoSizeMinTextSize, com.ikdong.weight.R.attr.autoSizePresetSizes, com.ikdong.weight.R.attr.autoSizeStepGranularity, com.ikdong.weight.R.attr.autoSizeT...`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:233`
  `resetGroup();`
- `sources/androidx/appcompat/view/SupportMenuInflater.java:236`
  `public void resetGroup() {`
- `sources/androidx/appcompat/view/menu/MenuItemImpl.java:616`
  `actionProvider2.reset();`
- `sources/androidx/appcompat/widget/AppCompatButton.java:182`
  `public void setAutoSizeTextTypeUniformWithPresetSizes(int[] iArr, int i) {`
- `sources/androidx/appcompat/widget/AppCompatButton.java:184`
  `super.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatButton.java:189`
  `appCompatTextHelper.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:180`
  `this.mView.setAutoSizeTextTypeUniformWithPresetSizes(autoSizeTextAvailableSizes, 0);`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:182`
  `public void setAutoSizeTextTypeUniformWithPresetSizes(int[] iArr, int i) {`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:184`
  `super.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatTextView.java:189`
  `appCompatTextHelper.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:47`
  `private boolean mHasPresetAutoSizeValues = false;`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:63`
  `if (typedArrayObtainStyledAttributes.hasValue(R.styleable.AppCompatTextView_autoSizePresetSizes) && (resourceId = typedArrayObtainStyledAttributes.getResourceId(R.styleable.AppCompatTextView_autoSizePresetSizes, 0)) > 0) {`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:65`
  `setupAutoSizeUniformPresetSizes(typedArrayObtainTypedArray);`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:71`
  `if (!this.mHasPresetAutoSizeValues) {`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:167`
  `private void setupAutoSizeUniformPresetSizes(TypedArray typedArray) {`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:322`
  `((LayoutParams) getChildAt(i2).getLayoutParams()).resetTouchBehaviorTracking();`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:325`
  `this.mDisallowInterceptReset = false;`
- `sources/androidx/core/app/NotificationCompat.java:2398`
  `private int mCustomSizePreset;`
- `sources/androidx/core/app/NotificationCompat.java:2412`
  `this.mCustomSizePreset = 0;`
- `sources/androidx/core/app/NotificationCompat.java:2422`
  `this.mCustomSizePreset = 0;`
- `sources/androidx/core/app/NotificationCompat.java:2450`
  `this.mCustomSizePreset = bundle.getInt(KEY_CUSTOM_SIZE_PRESET, 0);`
- `sources/androidx/core/app/NotificationCompat.java:2573`
  `wearableExtender.mCustomSizePreset = this.mCustomSizePreset;`
- `sources/androidx/core/app/NotificationCompat.java:2689`
  `public WearableExtender setCustomSizePreset(int i) {`
- `sources/androidx/core/app/NotificationCompat.java:2690`
  `this.mCustomSizePreset = i;`
- `sources/androidx/core/app/NotificationCompat.java:2695`
  `public int getCustomSizePreset() {`
- `sources/androidx/core/app/NotificationCompat.java:2696`
  `return this.mCustomSizePreset;`
- `sources/androidx/core/provider/FontRequestWorker.java:27`
  `static void resetTypefaceCache() {`
- `sources/androidx/core/text/BidiFormatter.java:149`
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
  `void setAutoSizeTextTypeUniformWithPresetSizes(int[] iArr, int i);`
- `sources/androidx/core/widget/TextViewCompat.java:219`
  `public static void setAutoSizeTextTypeUniformWithPresetSizes(TextView textView, int[] iArr, int i) {`
- `sources/androidx/core/widget/TextViewCompat.java:221`
  `textView.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/core/widget/TextViewCompat.java:223`
  `((AutoSizeableTextView) textView).setAutoSizeTextTypeUniformWithPresetSizes(iArr, i);`
- `sources/androidx/fragment/app/FragmentTransition.java:131`
  `fragmentTransitionImplChooseImpl.setNameOverridesReordered(viewGroup, arrayList2, arrayList, arrayListPrepareSetNameOverridesReordered, arrayMap);`
- `sources/androidx/fragment/app/FragmentTransition.java:184`
  `fragmentTransitionImplChooseImpl.scheduleNameReset(viewGroup, arrayList2, arrayMap);`
- `sources/androidx/fragment/app/FragmentTransitionImpl.java:148`
  `void scheduleNameReset(ViewGroup viewGroup, final ArrayList<View> arrayList, final Map<String, String> map) {`
- `sources/androidx/loader/app/LoaderManagerImpl.java:139`
  `loader.reset();`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:63`
  `void reset() {`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:236`
  `this.mCallback.markViewHoldersUpdated(i, updateOp.itemCount, updateOp.payload);`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:451`
  `this.mCallback.markViewHoldersUpdated(updateOp.positionStart, updateOp.itemCount, updateOp.payload);`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:573`
  `updateOpAcquire.payload = obj;`
- `sources/androidx/recyclerview/widget/AdapterHelper.java:582`
  `updateOp.payload = null;`
- `sources/androidx/recyclerview/widget/AsyncListDiffer.java:133`
  `public Object getChangePayload(int i2, int i3) {`
- `sources/androidx/recyclerview/widget/AsyncListDiffer.java:137`
  `return AsyncListDiffer.this.mConfig.getDiffCallback().getChangePayload(obj, obj2);`
- `sources/androidx/recyclerview/widget/DefaultItemAnimator.java:155`
  `resetAnimation(viewHolder);`
- `sources/androidx/recyclerview/widget/FastScroller.java:143`
  `resetHideDelay(HIDE_DELAY_AFTER_DRAGGING_MS);`
- `sources/androidx/recyclerview/widget/FastScroller.java:145`
  `resetHideDelay(1500);`
- `sources/androidx/recyclerview/widget/FastScroller.java:197`
  `private void resetHideDelay(int i) {`
- `sources/androidx/recyclerview/widget/LinearLayoutManager.java:300`
  `this.mAnchorInfo.reset();`
- `sources/androidx/recyclerview/widget/LinearLayoutManager.java:942`
  `layoutChunkResult.resetInternal();`
- `sources/androidx/recyclerview/widget/LinearLayoutManager.java:1596`
  `void resetInternal() {`
- `sources/androidx/recyclerview/widget/RecyclerView.java:2122`
  `private void resetScroll() {`
- `sources/androidx/recyclerview/widget/RecyclerView.java:2411`
  `this.mAdapterHelper.reset();`
- `sources/androidx/recyclerview/widget/RecyclerView.java:2463`
  `resetFocusInfo();`
- `sources/androidx/recyclerview/widget/RecyclerView.java:2586`
  `this.mViewInfoStore.addToPreLayout(childViewHolderInt, this.mItemAnimator.recordPreLayoutInformation(this.mState, childViewHolderInt, ItemAnimator.buildAdapterChangeFlagsForAnimations(childViewHolderInt), childViewHolderInt.getUnmodifiedPayloads()));`
- `sources/androidx/recyclerview/widget/RecyclerView.java:2706`
  `resetFocusInfo();`
- `sources/androidx/recyclerview/widget/RecyclerView.java:4351`
  `viewHolder.addChangePayload(null);`
- `sources/androidx/recyclerview/widget/RecyclerView.java:4469`
  `onBindViewHolder(vh, i, vh.getUnmodifiedPayloads());`
- `sources/androidx/recyclerview/widget/RecyclerView.java:4471`
  `vh.clearPayload();`
- `sources/androidx/recyclerview/widget/RecyclerView.java:5889`
  `private static final List<Object> FULLUPDATE_PAYLOADS = Collections.emptyList();`
- `sources/androidx/recyclerview/widget/RecyclerView.java:5903`
  `List<Object> mPayloads = null;`
- `sources/androidx/recyclerview/widget/RecyclerView.java:5904`
  `List<Object> mUnmodifiedPayloads = null;`
- `sources/androidx/recyclerview/widget/RecyclerView.java:6078`
  `createPayloadsIfNeeded();`
- `sources/androidx/recyclerview/widget/RecyclerView.java:6079`
  `this.mPayloads.add(obj);`
- `sources/androidx/recyclerview/widget/RecyclerView.java:6083`
  `private void createPayloadsIfNeeded() {`
- `sources/androidx/recyclerview/widget/RecyclerView.java:6084`
  `if (this.mPayloads == null) {`
- `sources/androidx/recyclerview/widget/RecyclerView.java:6086`
  `this.mPayloads = arrayList;`
- `sources/androidx/recyclerview/widget/RecyclerView.java:6087`
  `this.mUnmodifiedPayloads = Collections.unmodifiableList(arrayList);`
- `sources/androidx/recyclerview/widget/RecyclerView.java:6091`
  `void clearPayload() {`
- `sources/androidx/recyclerview/widget/RecyclerView.java:6092`
  `List<Object> list = this.mPayloads;`
- `sources/androidx/recyclerview/widget/RecyclerView.java:6107`
  `return FULLUPDATE_PAYLOADS;`
- `sources/androidx/recyclerview/widget/RecyclerView.java:6110`
  `void resetInternal() {`
- `sources/androidx/recyclerview/widget/RecyclerView.java:6119`
  `clearPayload();`
- `sources/androidx/room/InvalidationTracker.java:29`
  `static final String RESET_UPDATED_TABLES_SQL = "UPDATE room_table_modification_log SET invalidated = 0 WHERE invalidated = 1 ";`

## BR076

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `resources/assets/articles/daily_tips.txt:30`
  `Unreasonable goals usually demoralize an individual who is after losing weight. That is because if you realize that you are unable to achieve your objectives, you will be frustrated other than being motivated. That is why we recommend that you consult a doctor before beginning the journey tow weight...`
- `resources/assets/articles/daily_tips.txt:53`
  `27.Work out what to do first in the morning`
- `resources/assets/articles/daily_tips.txt:111`
  `56.Take a Cup of Water before taking a Meal`
- `resources/assets/articles/daily_tips.txt:112`
  `Before you can take a meal or a snack, take a cup of water and this will help you in losing your weight. If you stay hydrated, you will not desire to take calories.`
- `resources/assets/articles/daily_tips.txt:146`
  `When you prepare your food before traveling, you will have a healthy meal. Just pack your food and ensure that you have snacks.`
- `resources/assets/articles/daily_tips.txt:151`
  `76.Ensure that you sleep before midnight`
- `resources/assets/articles/daily_tips.txt:152`
  `When you go to bed before midnight, you will definitely enjoy the benefits of sleep.`
- `resources/assets/articles/daily_tips.txt:156`
  `For to get quality sleep before going to bed, dim your lights 1-2 hours before going to bed. You sleep faster.`
- `resources/assets/articles/daily_tips.txt:158`
  `Light from devices such as computer, TV or phone brings confusion to mind, and one may think that there is light outside. That needs to be turned earlier enough before going to bed.`
- `resources/assets/articles/daily_tips.txt:160`
  `You can read a book 1-2 hours before going to bed, and this will prepare you for a pleasant sleep.`
- `resources/assets/articles/daily_tips.txt:165`
  `83.Practice Meditation or Breathing as the first thing in the Morning`
- `resources/assets/articles/daily_tips.txt:174`
  `This bag should be packed with attire for doing the gym. Go to the gym early in the morning before going to work, during lunch break or after work.`
- `resources/res/layout/hms_picker_view.xml:111`
  `android:id="@+id/first"`
- `resources/res/layout/hms_picker_view.xml:117`
  `android:id="@+id/third"`
- `resources/res/layout/keyboard.xml:7`
  `android:id="@+id/first"`
- `resources/res/layout/keyboard.xml:13`
  `android:id="@+id/third"`
- `resources/res/layout/keyboard_right_drawable.xml:7`
  `android:id="@+id/first"`
- `resources/res/layout/keyboard_right_drawable.xml:13`
  `android:id="@+id/third"`
- `resources/res/layout/keyboard_right_drawable_with_header.xml:13`
  `android:id="@+id/first"`
- `resources/res/layout/keyboard_right_drawable_with_header.xml:19`
  `android:id="@+id/third"`
- `resources/res/layout/keyboard_text.xml:7`
  `android:id="@+id/first"`
- `resources/res/layout/keyboard_text.xml:13`
  `android:id="@+id/third"`
- `resources/res/layout/keyboard_text_with_header.xml:13`
  `android:id="@+id/first"`
- `resources/res/layout/keyboard_text_with_header.xml:19`
  `android:id="@+id/third"`
- `resources/res/layout/keyboard_with_header.xml:13`
  `android:id="@+id/first"`
- `resources/res/layout/keyboard_with_header.xml:19`
  `android:id="@+id/third"`
- `resources/res/layout/number_picker_view.xml:90`
  `android:id="@+id/first"`
- `resources/res/layout/number_picker_view.xml:96`
  `android:id="@+id/third"`
- `resources/res/layout/time_picker_view.xml:85`
  `android:id="@+id/first"`
- `resources/res/layout/time_picker_view.xml:91`
  `android:id="@+id/third"`
- `resources/res/values/arrays.xml:83`
  `<item>on every first Friday</item>`
- `resources/res/values/arrays.xml:85`
  `<item>on every third Friday</item>`
- `resources/res/values/arrays.xml:90`
  `<item>on every first Monday</item>`
- `resources/res/values/arrays.xml:92`
  `<item>on every third Monday</item>`
- `resources/res/values/arrays.xml:97`
  `<item>on every first Saturday</item>`
- `resources/res/values/arrays.xml:99`
  `<item>on every third Saturday</item>`
- `resources/res/values/arrays.xml:104`
  `<item>on every first Sunday</item>`
- `resources/res/values/arrays.xml:106`
  `<item>on every third Sunday</item>`
- `resources/res/values/arrays.xml:111`
  `<item>on every first Thursday</item>`
- `resources/res/values/arrays.xml:113`
  `<item>on every third Thursday</item>`
- `resources/res/values/arrays.xml:118`
  `<item>on every first Tuesday</item>`
- `resources/res/values/arrays.xml:120`
  `<item>on every third Tuesday</item>`
- `resources/res/values/arrays.xml:125`
  `<item>on every first Wednesday</item>`
- `resources/res/values/arrays.xml:127`
  `<item>on every third Wednesday</item>`
- `resources/res/values/arrays.xml:216`
  `<item>Before meals</item>`
- `resources/res/values/public.xml:3803`
  `<public type="id" name="field" id="0x7f090374" />`
- `resources/res/values/public.xml:3810`
  `<public type="id" name="first" id="0x7f09037b" />`
- `resources/res/values/public.xml:4340`
  `<public type="id" name="login" id="0x7f09058d" />`
- `resources/res/values/public.xml:5211`
  `<public type="id" name="third" id="0x7f0908f4" />`
- `resources/res/values/strings.xml:409`
  `<string name="label_activity_99">Field hockey</string>`
- `resources/res/values/strings.xml:439`
  `<string name="label_before">Before</string>`
- `resources/res/values/strings.xml:440`
  `<string name="label_before_meal">Before a meal</string>`
- `resources/res/values/strings.xml:515`
  `<string name="label_challenge_exercises_9">Do {0} squats before sitting down</string>`
- `resources/res/values/strings.xml:648`
  `<string name="label_first_day_week">First day of week</string>`
- `resources/res/values/strings.xml:974`
  `<string name="label_weight_before_meal">Weight-in before a meal</string>`
- `resources/res/values/strings.xml:1082`
  `<string name="msg_error_file_csv_content_invalid">Invalid data. Please correct it first.</string>`
- `resources/res/values/strings.xml:1095`
  `<string name="msg_fields_required">Below field is required</string>`
- `resources/res/values/strings.xml:1116`
  `<string name="msg_join_community">Need join weight community first</string>`
- `resources/res/values/strings.xml:1126`
  `<string name="msg_login_success">Login successfully!</string>`
- `resources/res/values/strings.xml:1158`
  `<string name="msg_rest_plan_first">Set the first day of plan</string>`
- `resources/res/values/strings.xml:1171`
  `<string name="msg_setup_profile_first">Please setup your profile first</string>`
- `resources/res/values/strings.xml:1176`
  `<string name="msg_sync_login_fail">Failed to login!</string>`
- `resources/res/values/strings.xml:1234`
  `<string name="nnf_select_something_first">Please select something first</string>`
- `resources/res/values/strings.xml:1343`
  `<string name="title_exit_feedback">Feedback before exit</string>`
- `sources/androidx/activity/ComponentActivity.java:49`
  `throw new IllegalStateException("getLifecycle() returned null in ComponentActivity's constructor. Please make sure you are lazily constructing your Lifecycle in the first call to getLifecycle() rather than relying on field initialization.");`
- `sources/androidx/activity/ComponentActivity.java:140`
  `throw new IllegalStateException("Your activity is not yet attached to the Application instance. You can't request ViewModel before onCreate call.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:309`
  `throw new IllegalStateException("This Activity already has an action bar supplied by the window decor. Do not request Window.FEATURE_SUPPORT_ACTION_BAR and set windowActionBar to false in your theme to use a Toolbar instead.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1648`
  `throw new AndroidRuntimeException("Window feature must be requested before adding content");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1654`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR id when requesting this feature.");`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1660`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR_OVERLAY id when requesting this feature.");`
- `sources/androidx/core/view/WindowInsetsCompat.java:14`
  `import java.lang.reflect.Field;`
- `sources/androidx/core/view/WindowInsetsCompat.java:358`
  `private static Field sAttachInfoField = null;`
- `sources/androidx/core/view/WindowInsetsCompat.java:360`
  `private static Field sVisibleInsetsField = null;`
- `sources/androidx/core/view/WindowInsetsCompat.java:943`
  `private static Field sConsumedField = null;`
- `sources/androidx/core/view/WindowInsetsCompat.java:984`
  `Log.i(WindowInsetsCompat.TAG, "Could not retrieve WindowInsets.CONSUMED field", e);`
- `sources/androidx/core/view/WindowInsetsCompat.java:988`
  `Field field = sConsumedField;`
- `sources/androidx/core/view/WindowInsetsCompat.java:989`
  `if (field != null) {`
- `sources/androidx/core/view/WindowInsetsCompat.java:991`
  `WindowInsets windowInsets = (WindowInsets) field.get(null);`
- `sources/androidx/core/view/WindowInsetsCompat.java:996`
  `Log.i(WindowInsetsCompat.TAG, "Could not get value from WindowInsets.CONSUMED field", e2);`
- `sources/androidx/core/view/WindowInsetsCompat.java:1108`
  `static final int FIRST = 1;`

## BR077

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `sources/okhttp3/OkHttpClient.java:219`
  `private static SSLSocketFactory newSslSocketFactory(X509TrustManager x509TrustManager) {`
- `sources/okhttp3/OkHttpClient.java:221`
  `SSLContext sSLContext = Platform.get().getSSLContext();`
- `sources/okhttp3/OkHttpClient.java:222`
  `sSLContext.init(null, new TrustManager[]{x509TrustManager}, null);`
- `sources/okhttp3/OkHttpClient.java:223`
  `return sSLContext.getSocketFactory();`

## BR078

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/okhttp3/OkHttpClient.java:19`
  `import javax.net.ssl.HostnameVerifier;`
- `sources/okhttp3/OkHttpClient.java:25`
  `import okhttp3.Call;`
- `sources/okhttp3/OkHttpClient.java:26`
  `import okhttp3.EventListener;`
- `sources/okhttp3/OkHttpClient.java:27`
  `import okhttp3.Headers;`
- `sources/okhttp3/OkHttpClient.java:28`
  `import okhttp3.Response;`
- `sources/okhttp3/OkHttpClient.java:29`
  `import okhttp3.WebSocket;`
- `sources/okhttp3/OkHttpClient.java:30`
  `import okhttp3.internal.Internal;`
- `sources/okhttp3/OkHttpClient.java:197`
  `this.hostnameVerifier = builder.hostnameVerifier;`
- `sources/okhttp3/OkHttpClient.java:566`
  `public Builder hostnameVerifier(HostnameVerifier hostnameVerifier) {`
- `sources/okhttp3/OkHttpClient.java:567`
  `Objects.requireNonNull(hostnameVerifier, "hostnameVerifier == null");`
- `sources/okhttp3/OkHttpClient.java:568`
  `this.hostnameVerifier = hostnameVerifier;`
- `sources/okhttp3/internal/Util.java:37`
  `import okhttp3.Headers;`
- `sources/okhttp3/internal/Util.java:38`
  `import okhttp3.HttpUrl;`
- `sources/okhttp3/internal/Util.java:39`
  `import okhttp3.MediaType;`
- `sources/okhttp3/internal/Util.java:40`
  `import okhttp3.RequestBody;`
- `sources/okhttp3/internal/Util.java:41`
  `import okhttp3.ResponseBody;`
- `sources/okhttp3/internal/Util.java:42`
  `import okhttp3.internal.http2.Header;`
- `sources/okhttp3/internal/connection/RealConnection.java:283`
  `if (this.http2Connection == null || route == null || route.proxy().type() != Proxy.Type.DIRECT || this.route.proxy().type() != Proxy.Type.DIRECT || !this.route.socketAddress().equals(route.socketAddress()) || route.address().hostnameVerifier() != OkHostnameVerifier.INSTANCE || !supportsUrl(address.u...`
- `sources/okhttp3/internal/connection/RealConnection.java:301`
  `return this.handshake != null && OkHostnameVerifier.INSTANCE.verify(httpUrl.host(), (X509Certificate) this.handshake.peerCertificates().get(0));`
- `sources/okhttp3/internal/connection/RealConnection.java:304`
  `public HttpCodec newCodec(OkHttpClient okHttpClient, Interceptor.Chain chain, StreamAllocation streamAllocation) throws SocketException {`
- `sources/okhttp3/internal/connection/RealConnection.java:363`
  `@Override // okhttp3.internal.http2.Http2Connection.Listener`
- `sources/okhttp3/internal/http2/PushObserver.java:8`
  `public static final PushObserver CANCEL = new PushObserver() { // from class: okhttp3.internal.http2.PushObserver.1`
- `sources/okhttp3/internal/http2/PushObserver.java:9`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:14`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:19`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/http2/PushObserver.java:23`
  `@Override // okhttp3.internal.http2.PushObserver`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:20`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:21`
  `import okhttp3.internal.Util;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:22`
  `import okhttp3.internal.tls.CertificateChainCleaner;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:23`
  `import okhttp3.internal.tls.TrustRootIndex;`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:66`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:81`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:192`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:229`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:254`
  `@Override // okhttp3.internal.tls.CertificateChainCleaner`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:337`
  `@Override // okhttp3.internal.tls.TrustRootIndex`
- `sources/okhttp3/internal/platform/AndroidPlatform.java:369`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:11`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/ConscryptPlatform.java:23`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:11`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:12`
  `import okhttp3.internal.Util;`
- `sources/okhttp3/internal/platform/Jdk9Platform.java:53`
  `@Override // okhttp3.internal.platform.Platform`
- `sources/okhttp3/internal/platform/Platform.java:19`
  `import okhttp3.OkHttpClient;`
- `sources/okhttp3/internal/platform/Platform.java:20`
  `import okhttp3.Protocol;`
- `sources/okhttp3/internal/platform/Platform.java:21`
  `import okhttp3.internal.tls.BasicCertificateChainCleaner;`
- `sources/okhttp3/internal/platform/Platform.java:22`
  `import okhttp3.internal.tls.BasicTrustRootIndex;`
- `sources/okhttp3/internal/platform/Platform.java:23`
  `import okhttp3.internal.tls.CertificateChainCleaner;`
- `sources/okhttp3/internal/platform/Platform.java:24`
  `import okhttp3.internal.tls.TrustRootIndex;`
- `sources/okhttp3/internal/tls/CertificateChainCleaner.java:1`
  `package okhttp3.internal.tls;`
- `sources/okhttp3/internal/tls/CertificateChainCleaner.java:7`
  `import okhttp3.internal.platform.Platform;`
- `sources/okhttp3/internal/ws/RealWebSocket.java:313`
  `@Override // okhttp3.WebSocket`

## BR079

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/com/google/android/gms/ads/internal/zzs.java:68`
  `this.zzf.getSettings().setJavaScriptEnabled(true);`
- `sources/com/google/android/gms/ads/internal/util/zzae.java:89`
  `webSettings.setAllowFileAccessFromFileURLs(false);`
- `sources/com/google/android/gms/ads/internal/util/zzae.java:90`
  `webSettings.setAllowUniversalAccessFromFileURLs(false);`
- `sources/com/google/android/gms/internal/ads/zzcpi.java:118`
  `settings.setAllowFileAccess(false);`
- `sources/com/google/android/gms/internal/ads/zzcpi.java:120`
  `settings.setJavaScriptEnabled(true);`
- `sources/com/google/android/gms/internal/ads/zzfld.java:9`
  `webView.getSettings().setJavaScriptEnabled(true);`
- `sources/com/google/android/gms/internal/ads/zzflf.java:42`
  `webView.getSettings().setJavaScriptEnabled(true);`
- `sources/com/google/android/gms/internal/consent_sdk/zzat.java:43`
  `zzbeVarZza.getSettings().setJavaScriptEnabled(true);`

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
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:1854`
  `Log.d("AppCompatDelegate", "Exception while getting ActivityInfo", e);`
- `sources/androidx/core/view/ViewCompat.java:651`
  `Log.d(TAG, "Error calling dispatchStartTemporaryDetach", e);`
- `sources/androidx/core/view/ViewCompat.java:672`
  `Log.d(TAG, "Error calling dispatchFinishTemporaryDetach", e);`
- `sources/androidx/fragment/app/BackStackState.java:115`
  `Log.v("FragmentManager", "Instantiate " + backStackRecord + " op #" + i2 + " base fragment #" + this.mOps[i3]);`
- `sources/androidx/fragment/app/FragmentManagerImpl.java:789`
  `Log.v(TAG, "Ignoring moving " + fragment + " to state " + this.mCurState + "since it is not added to " + this);`
- `sources/androidx/fragment/app/FragmentManagerImpl.java:894`
  `Log.v(TAG, "Removed fragment from active set " + fragment);`
- `sources/androidx/fragment/app/FragmentManagerImpl.java:1765`
  `Log.v(TAG, "restoreSaveState: re-attaching retained " + fragment);`
- `sources/androidx/fragment/app/FragmentManagerImpl.java:1781`
  `Log.v(TAG, "Discarding retained Fragment " + fragment + " that was not found in the set of active Fragments " + fragmentManagerState.mActive);`
- `sources/androidx/fragment/app/FragmentManagerImpl.java:1807`
  `Log.v(TAG, "restoreSaveState: active (" + fragmentInstantiate.mWho + "): " + fragmentInstantiate);`
- `sources/androidx/fragment/app/FragmentManagerImpl.java:2412`
  `Log.v(TAG, "onCreateView: id=0x" + Integer.toHexString(resourceId) + " fname=" + str2 + " existing=" + fragmentFindFragmentById);`
- `sources/androidx/localbroadcastmanager/content/LocalBroadcastManager.java:152`
  `Log.v(TAG, "Resolving type " + strResolveTypeIfNeeded + " scheme " + scheme + " of intent " + intent);`
- `sources/androidx/localbroadcastmanager/content/LocalBroadcastManager.java:157`
  `Log.v(TAG, "Action list: " + arrayList3);`
- `sources/androidx/localbroadcastmanager/content/LocalBroadcastManager.java:184`
  `Log.v(TAG, "  Filter matched!  match=0x" + Integer.toHexString(iMatch));`
- `sources/com/activeandroid/Cache.java:38`
  `Log.v("Cache cleared.");`
- `sources/com/activeandroid/Cache.java:47`
  `Log.v("ActiveAndroid disposed. Call initialize to use library.");`
- `sources/com/bumptech/glide/b.java:136`
  `Log.d("Glide", "Discovered GlideModule from manifest: " + it2.next().getClass());`
- `sources/com/bumptech/glide/load/b/a/j.java:92`
  `Log.v(aVarB.a(), "Allocated " + aVar.f402a + " bytes");`
- `sources/com/bumptech/glide/load/d/a.java:66`
  `Log.v("ImageDecoder", "Resizing from [" + size.getWidth() + "x" + size.getHeight() + "] to [" + iRound + "x" + iRound2 + "] scaleFactor: " + fA);`
- `sources/com/bumptech/glide/load/d/a/d.java:18`
  `Log.v("BitmapImageDecoder", "Decoded [" + bitmapDecodeBitmap.getWidth() + "x" + bitmapDecodeBitmap.getHeight() + "] for [" + i + "x" + i2 + "]");`
- `sources/com/bumptech/glide/load/d/a/k.java:230`
  `Log.d("DfltImageHeaderParser", "Illegal tagValueOffset=" + i3 + " tagType=" + ((int) sB3));`
- `sources/com/bumptech/glide/load/d/a/k.java:234`
  `Log.d("DfltImageHeaderParser", "Illegal number of bytes for TI tag data tagType=" + ((int) sB3));`
- `sources/com/bumptech/glide/load/d/a/x.java:107`
  `Log.v("TransformationUtils", "requested target size matches input, returning input");`
- `sources/com/bumptech/glide/load/d/a/x.java:116`
  `Log.v("TransformationUtils", "adjusted target size matches input, returning input");`
- `sources/com/bumptech/glide/load/d/a/x.java:123`
  `Log.v("TransformationUtils", "request: " + i + "x" + i2);`
- `sources/com/bumptech/glide/load/d/a/x.java:124`
  `Log.v("TransformationUtils", "toFit:   " + bitmap.getWidth() + "x" + bitmap.getHeight());`
- `sources/com/bumptech/glide/load/d/a/x.java:125`
  `Log.v("TransformationUtils", "toReuse: " + bitmapA.getWidth() + "x" + bitmapA.getHeight());`
- `sources/com/bumptech/glide/load/d/a/x.java:129`
  `Log.v("TransformationUtils", sb.toString());`
- `sources/com/bumptech/glide/load/d/a/x.java:140`
  `Log.v("TransformationUtils", "requested target size larger or equal to input, returning input");`
- `sources/com/google/android/gms/internal/ads/zzakd.java:24`
  `Log.d(zza, "decode object failure");`
- `sources/com/google/android/gms/internal/ads/zzatc.java:184`
  `Log.d("MediaCodecInfo", sb3.toString());`
- `sources/com/google/android/gms/internal/ads/zzoh.java:309`
  `Log.d("MediaCodecInfo", sb3.toString());`
- `sources/com/google/android/gms/internal/icing/zzax.java:17`
  `Log.d("SearchAuth", "ClearTokenImpl success");`

## BR081

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzew.java:5`
  `import android.security.keystore.KeyGenParameterSpec;`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzew.java:37`
  `KeyGenerator keyGenerator = KeyGenerator.getInstance("AES", "AndroidKeyStore");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzew.java:38`
  `keyGenerator.init(new KeyGenParameterSpec.Builder(strZza, 3).setKeySize(256).setBlockModes(CodePackage.GCM).setEncryptionPaddings("NoPadding").build());`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzfa.java:22`
  `KeyStore keyStore = KeyStore.getInstance("AndroidKeyStore");`
- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzfa.java:55`
  `KeyStore keyStore = KeyStore.getInstance("AndroidKeyStore");`

## BR082

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/androidx/core/content/FileProvider.java:221`
  `@Override // androidx.core.content.FileProvider.PathStrategy`
- `sources/androidx/core/content/FileProvider.java:248`
  `@Override // androidx.core.content.FileProvider.PathStrategy`
- `sources/com/ikdong/weight/service/GenericFileProvider.java:3`
  `import androidx.core.content.FileProvider;`
- `sources/com/ikdong/weight/widget/fragment/ad.java:18`
  `import androidx.core.content.FileProvider;`
- `sources/com/ikdong/weight/widget/fragment/ad.java:55`
  `intent.putExtra("android.intent.extra.STREAM", FileProvider.getUriForFile(ad.this.getActivity(), ad.this.getActivity().getApplicationContext().getPackageName() + ".service.GenericFileProvider", file));`
- `sources/com/ikdong/weight/widget/fragment/BodyProgressFragment.java:27`
  `import androidx.core.content.FileProvider;`
- `sources/com/ikdong/weight/widget/fragment/BodyProgressFragment.java:500`
  `Uri uriForFile = FileProvider.getUriForFile(getContext(), "com.ikdong.weight.fileprovider", h());`
- `sources/com/ikdong/weight/widget/fragment/CalendarWeekPlanFragment.java:39`
  `import androidx.core.content.FileProvider;`
- `sources/com/ikdong/weight/widget/fragment/CalendarWeekPlanFragment.java:690`
  `Uri uriForFile = FileProvider.getUriForFile(getContext(), "com.ikdong.weight.fileprovider", fileF);`
- `sources/com/nononsenseapps/filepicker/d.java:7`
  `import androidx.core.content.FileProvider;`
- `sources/com/nononsenseapps/filepicker/d.java:96`
  `return FileProvider.getUriForFile(getContext(), getContext().getApplicationContext().getPackageName() + ".provider", file);`

## BR086

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/androidx/appcompat/R.java:62`
  `public static final int actionModeShareDrawable = 0x7f04001a;`
- `sources/androidx/appcompat/R.java:543`
  `public static final int abc_ab_share_pack_mtrl_alpha = 0x7f080008;`
- `sources/androidx/appcompat/R.java:551`
  `public static final int abc_btn_default_mtrl_shape = 0x7f080010;`
- `sources/androidx/appcompat/R.java:1383`
  `public static final int AppCompatTheme_actionModeShareDrawable = 0x0000001a;`
- `sources/androidx/appcompat/R.java:1495`
  `public static final int DrawerArrowToggle_arrowShaftLength = 0x00000001;`
- `sources/androidx/appcompat/R.java:1706`
  `public static final int[] AppCompatTheme = {android.R.attr.windowIsFloating, android.R.attr.windowAnimationStyle, com.ikdong.weight.R.attr.actionBarDivider, com.ikdong.weight.R.attr.actionBarItemBackground, com.ikdong.weight.R.attr.actionBarPopupTheme, com.ikdong.weight.R.attr.actionBarSize, com.ikd...`
- `sources/androidx/appcompat/R.java:1710`
  `public static final int[] DrawerArrowToggle = {com.ikdong.weight.R.attr.arrowHeadLength, com.ikdong.weight.R.attr.arrowShaftLength, com.ikdong.weight.R.attr.barLength, com.ikdong.weight.R.attr.color, com.ikdong.weight.R.attr.drawableSize, com.ikdong.weight.R.attr.gapBetweenBars, com.ikdong.weight.R....`
- `sources/androidx/appcompat/R.java:1729`
  `public static final int[] TextAppearance = {android.R.attr.textSize, android.R.attr.typeface, android.R.attr.textStyle, android.R.attr.textColor, android.R.attr.textColorHint, android.R.attr.textColorLink, android.R.attr.shadowColor, android.R.attr.shadowDx, android.R.attr.shadowDy, android.R.attr.s...`
- `sources/androidx/appcompat/app/AppCompatDelegate.java:76`
  `public abstract boolean isHandleNativeActionModesEnabled();`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:968`
  `public boolean isHandleNativeActionModesEnabled() {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2236`
  `if (AppCompatDelegateImpl.this.isHandleNativeActionModesEnabled()) {`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2253`
  `if (AppCompatDelegateImpl.this.isHandleNativeActionModesEnabled() && i == 0) {`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:24`
  `private float mArrowShaftLength;`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:67`
  `this.mArrowShaftLength = typedArrayObtainStyledAttributes.getDimension(R.styleable.DrawerArrowToggle_arrowShaftLength, 0.0f);`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:180`
  `float fLerp2 = lerp(this.mBarLength, this.mArrowShaftLength, this.mProgress);`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:476`
  `java.lang.String r3 = "Share records file not well-formed."`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:481`
  `java.lang.String r3 = "Share records file does not start with historical-records tag."`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:28`
  `private final int[] COLORFILTER_TINT_COLOR_CONTROL_NORMAL = {R.drawable.abc_textfield_search_default_mtrl_alpha, R.drawable.abc_textfield_default_mtrl_alpha, R.drawable.abc_ab_share_pack_mtrl_alpha};`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:29`
  `private final int[] TINT_COLOR_CONTROL_NORMAL = {R.drawable.abc_ic_commit_search_api_mtrl_alpha, R.drawable.abc_seekbar_tick_mark_material, R.drawable.abc_ic_menu_share_mtrl_alpha, R.drawable.abc_ic_menu_copy_mtrl_am_alpha, R.drawable.abc_ic_menu_cut_mtrl_alpha, R.drawable.abc_ic_menu_selectall_mtrl...`
- `sources/androidx/appcompat/widget/AppCompatDrawableManager.java:131`
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
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:72`
  `ShapeDrawable shapeDrawable = new ShapeDrawable(getDrawableShape());`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:73`
  `shapeDrawable.getPaint().setShader(new BitmapShader(bitmap, Shader.TileMode.REPEAT, Shader.TileMode.CLAMP));`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:74`
  `shapeDrawable.getPaint().setColorFilter(bitmapDrawable.getPaint().getColorFilter());`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:75`
  `return z ? new ClipDrawable(shapeDrawable, 3, 1) : shapeDrawable;`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:98`
  `private Shape getDrawableShape() {`
- `sources/androidx/appcompat/widget/AppCompatProgressBarHelper.java:99`
  `return new RoundRectShape(new float[]{5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f}, null, null);`
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
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:19`
  `public static final String EXTRA_DEFAULT_SHARE_MENU_ITEM = "android.support.customtabs.extra.SHARE_MENU_ITEM";`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:118`
  `public Builder addDefaultShareMenuItem() {`
- `sources/androidx/browser/customtabs/CustomTabsIntent.java:119`
  `this.mIntent.putExtra(CustomTabsIntent.EXTRA_DEFAULT_SHARE_MENU_ITEM, true);`
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
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:85`
  `this.mCornerShadowPaint.setAlpha(i);`

## BR088

paper_id: B004
paper_title: Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation

- `sources/com/google/android/gms/internal/p002firebaseauthapi/zzti.java:71`
  `sparseArray.put(17057, new Pair("ERROR_WEB_CONTEXT_ALREADY_PRESENTED", "A headful operation is already in progress. Please wait for that to finish."));`

## BR090

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `security_audit/00_audit_scope_and_summary.md:23`
  `结论严格限定为 'confirmed'、'supported_hypothesis'、'not_supported'、'not_testable' 四类。没有抓包、logcat、设备交互、真实账号会话时，不把运行时泄露判为 confirmed。`
- `security_audit/00_audit_scope_and_summary.md:25`
  `凡证据链没有达到 confirmed 门槛的条目，报告均按 'supported_hypothesis'、'not_supported' 或 'not_testable' 处理，并明确视为“不足以确认”，不强行下结论。`
- `security_audit/00_audit_scope_and_summary.md:36`
  `## 2. 主要 confirmed 结论`
- `security_audit/00_audit_scope_and_summary.md:50`
  `6. 'BR013 / B010 / Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues'：Withings 现行集成以 'http://account.withings.com/oauth2_user/authorize2' 发起 OAuth 授权；遗留 WithingsActivity 中还存在 'http://wbsapi.withings.net/measure' 明文测量接口调用并携带 ...`
- `security_audit/00_audit_scope_and_summary.md:58`
  `10. 'BR091 / B010 / Client-Focused Security Assessment...'：第一方 Firebase 同步代码将体重、进度、腰围、臀围、肌肉、心率、体脂、水分、内脏脂肪、日记等字段组装后写入 'https://weighttrackassistant.firebaseio.com/prd/sync'；注册跟踪也将年龄、体重、身高、性别、国家、BMI 发送到 'init_profile'。这是“模型字段 -> payload -> endpoint call path”的 confirmed 静态/代码级云上传链。`
- `security_audit/00_audit_scope_and_summary.md:66`
  `3. 独立分析中 OAuth 'state' 未校验：Fitbit 授权 URL 未包含 state，Withings 授权 URL 包含固定 'state=10001'，回调代码只读取 'code'，未读取/比较 state。该点不是 rule_catalog 中独立漏洞类型，因此不作为新增 rule confirmed，只在独立安全分析中列为 supported_hypothesis。`
- `security_audit/00_audit_scope_and_summary.md:79`
  `- '03_evidence_chains.md'：关键 confirmed/supported_hypothesis 的细证据链。`
- `security_audit/01_independent_security_findings.md:30`
  `### 为什么不是 confirmed`
- `security_audit/01_independent_security_findings.md:38`
  `因此本报告不把它扩大成“账号接管 confirmed”。`
- `security_audit/01_independent_security_findings.md:44`
  `'confirmed' 作为 App 自身访问控制缺陷；对应数据库规则中主要落在 'BR035 / B026'。这里独立强调的是 App 自己实现了可选图案锁，但没有在所有敏感 Activity 上做统一门禁。`
- `security_audit/01_independent_security_findings.md:68`
  `- 动态 confirmed 仍建议用 'adb shell am start -a android.intent.action.VIEW -d "wta://measure?PARAM_CATE=heartRate&PARAM_TITLE=Heart"' 复测。`
- `security_audit/01_independent_security_findings.md:74`
  `'supported_hypothesis'。数据库 rule 主要覆盖敏感数据外部存储；本点强调“从外部存储导入任意备份文件后替换/恢复本地健康数据库”的完整性风险。由于 'util.e' 反编译质量有限，当前报告不把它升级为 confirmed 数据篡改。`
- `security_audit/01_independent_security_findings.md:112`
  `'confirmed' 对应 'BR016'，独立分析中强调它的影响边界：移动端 public client 中嵌入 secret 不能作为真正服务端秘密使用；如果第三方仍把它当 confidential client credential，则可能扩大 token endpoint 滥用风险。`
- `security_audit/01_independent_security_findings.md:130`
  `静态代码存在 'confirmed'；当前 UI 可达性不足。Manifest 声明 'WithingsActivity' 但未导出，现行 Withings 同步使用 'SyncWithingsActivity' 和 'integration.withings.a.b'。因此报告把遗留代码作为 APK 攻击面/维护风险，而不把它等同于用户正常流程必触发。`
- `security_audit/02_rule_by_rule_mapping.md:7`
  `- 'verdict' 只使用 'confirmed'、'supported_hypothesis'、'not_supported'、'not_testable'。`
- `security_audit/02_rule_by_rule_mapping.md:8`
  `- 对动态规则，没有设备、抓包、logcat、运行时本地文件抽取时，一律不升级为 confirmed。`
- `security_audit/02_rule_by_rule_mapping.md:27`
  `| BR013 | B010 / Client-Focused Security Assessment... | B010 原文指出 mHealth 传输安全不足会影响保密性/完整性，常见问题是不受保护连接。 | 现行 Withings 授权入口使用 'http://account.withings.com/oauth2_user/authorize2'；遗留 Withings 测量 API 使用 'http://wbsapi.withings.net/measure' 并携带 OAuth token/userid/signature。 | confirmed |`
- `security_audit/02_rule_by_rule_mapping.md:30`
  `| BR016 | B006 / Analyzing security issues of android mobile health and medical applications | B006 将 app code/resources 中的安全问题、凭据、通信风险纳入静态分析。 | 第一方/资源中存在 Fitbit Basic Authorization、Withings 'client_secret'、Google/Firebase API key、AdMob app id、Google backup api_key。 | confirmed |`
- `security_audit/02_rule_by_rule_mapping.md:32`
  `| BR018 | B001 / Security Concerns in Android mHealth Apps | B001 明确 mHealth App 处理敏感医疗/健康数据，需要检查存储、传输、日志等。 | 第一方 'Weight'、'Goal'、'Image' 模型含体重、心率、BMI、体脂、肌肉、围度、日记、年龄、身高、性别、食物营养等字段。 | confirmed |`
- `security_audit/02_rule_by_rule_mapping.md:39`
  `| BR025 | B005 / Mobile health and privacy: cross sectional study | B005 结合静态/动态分析健康 App 数据收集、流量、tracker 和本地数据风险。 | ActiveAndroid DB 'WTA.mp3' 存储 'Weights'/'Goals'/'Images'；未发现 SQLCipher/EncryptedSharedPreferences/EncryptedFile/MasterKey；有原始 DB 复制导出。 | confirmed |`
- `security_audit/02_rule_by_rule_mapping.md:40`
  `| BR026 | B002 / Unaddressed privacy risks in accredited health and wellness apps | B002 原文检查本地设备存储和传输，指出健康/个人信息本地未加密存储会带来风险。 | 'g.a(context,key,string)' 写入普通 'worktrack_setting'；Fitbit access token 存入 'PARAM_FITBIT_ACCESS_TOKEN'；Withings token JSON 存入 'INT_WITHINGS_TOKEN'；旧 Withings token/secret 也用...`
- `security_audit/02_rule_by_rule_mapping.md:41`
  `| BR027 | B002 / Unaddressed privacy risks... | B002 将移动设备存储作为评估对象，特别关注个人/敏感信息是否被安全保护。 | 'util.n' 将 '/data/.../WTA.mp3' 复制到外部 '/WeightTrack/WTA.data'；'util.f' 将 Weight JSON 写入 '/WeightTrack/weight_backup.json'；CSV 和图片也写外部路径。 | confirmed |`
- `security_audit/02_rule_by_rule_mapping.md:42`
  `| BR028 | B014 / Privacy Assessment in Mobile Health Apps: Scoping Review | B014 总结 mHealth 隐私评估项目包括本地存储、远端存储、权限、通信、访问控制。 | Manifest 'allowBackup=true'；App 本地有敏感 SQLite 与 SharedPreferences token；未见 dataExtractionRules/backup exclusion。 | confirmed |`
- `security_audit/02_rule_by_rule_mapping.md:46`
  `| BR032 | B026 / Measuring the Insecurity of Mobile Deep Links of Android | B026 原文说明 mobile deep links 是指向 App 内具体位置的 URI，scheme URL 有被劫持/误用风险。 | Manifest 暴露多个 'wta://' deep link，包括 'fitbit'、'withings'、'input'、'measure'、'youtube_video' 等。 | confirmed |`
- `security_audit/02_rule_by_rule_mapping.md:48`
  `| BR034 | B026 / Measuring the Insecurity... | 规则关注 URI 参数进入敏感 API/DB/命令。 | 'SyncFitbitActivity' 将 URI 'code' 送 token endpoint；'SyncWithingsActivity' 将 'code' 送 token endpoint；'MeasureActivity' 将 'PARAM_CATE' 送本地 DB 查询。 | confirmed |`
- `security_audit/02_rule_by_rule_mapping.md:49`
  `| BR035 | B026 / Measuring the Insecurity... | 规则关注 deep link 打开敏感页面/动作前缺少 auth check。 | 'NavigatorActivity' 才执行图案锁；'MeasureActivity' exported deep link 直接读 'PARAM_CATE' 并显示本地 Weight 数据，无图案锁检查。 | confirmed |`
- `security_audit/02_rule_by_rule_mapping.md:55`
  `| BR047 | B001 / Security Concerns in Android mHealth Apps | B001 将日志和侧信道列入 mHealth 安全关注面。 | 遗留 'WithingsActivity' 打印测量 response 和 OAuth token response；response 包含 'oauth_token'/'oauth_token_secret' 或测量数据。 | confirmed |`
- `security_audit/02_rule_by_rule_mapping.md:60`
  `| BR058 | B022 / A Study of Android Application Security | B022 是静态分析方法论；规则强调第一方/第三方区分。 | 本报告已区分第一方 'com.ikdong.weight' 与第三方 SDK；未把 SDK 单字符串作为第一方 confirmed。 | not_supported |`
- `security_audit/02_rule_by_rule_mapping.md:92`
  `| BR080 | B001 / Security Concerns in Android mHealth Apps | B001 关注 logcat 中实际出现敏感信息。 | 有静态 'System.out.println' 代码，但无 logcat，因此运行时日志泄露不能 confirmed。 | not_testable |`
- `security_audit/02_rule_by_rule_mapping.md:105`
  `| BR091 | B010 / Client-Focused Security Assessment... | B010 关注 mHealth 数据传输的保密性、完整性和服务器通信；rule 允许由 endpoint call path 确认。 | Firebase 'buildRef' 指向 'https://weighttrackassistant.firebaseio.com/prd'；'trackRegister' 上传 age/weight/height/gender/country/BMI；'BackupService' 和 'ad.a' 上传体重、围度、心率、体脂、日记等到 s...`
- `security_audit/02_rule_by_rule_mapping.md:116`
  `- confirmed：12 条。BR013、BR016、BR018、BR025、BR026、BR027、BR028、BR032、BR034、BR035、BR047、BR091。`
- `security_audit/03_evidence_chains.md:9`
  `- 'BR018 / B001 / Security Concerns in Android mHealth Apps'：confirmed。`
- `security_audit/03_evidence_chains.md:10`
  `- 'BR025 / B005 / Mobile health and privacy: cross sectional study'：confirmed。`
- `security_audit/03_evidence_chains.md:11`
  `- 'BR027 / B002 / Unaddressed privacy risks in accredited health and wellness apps'：confirmed。`
- `security_audit/03_evidence_chains.md:57`
  `- 'BR027 / B002'：confirmed。`
- `security_audit/03_evidence_chains.md:58`
  `- 'BR025 / B005'：confirmed。`
- `security_audit/03_evidence_chains.md:94`
  `### 为什么是 confirmed`
- `security_audit/03_evidence_chains.md:112`
  `- 'BR026 / B002'：confirmed。`
- `security_audit/03_evidence_chains.md:150`
  `- 'BR091 / B010'：confirmed。`
- `security_audit/03_evidence_chains.md:184`
  `### 为什么 BR091 是 confirmed`
- `security_audit/03_evidence_chains.md:188`
  `### 为什么 BR094 不是 confirmed`
- `security_audit/03_evidence_chains.md:200`
  `- 'BR013 / B010'：confirmed。`
- `security_audit/03_evidence_chains.md:201`
  `- 'BR016 / B006'：confirmed。`
- `security_audit/03_evidence_chains.md:202`
  `- 'BR047 / B001'：confirmed。`
- `security_audit/03_evidence_chains.md:255`
  `- 现行 HTTP 授权入口 confirmed，因为 'SyncWithingsActivity' 使用现行 helper。`
- `security_audit/03_evidence_chains.md:256`
  `- 遗留 HTTP 测量和日志代码 confirmed 存在于 APK，但当前 UI 可达性不足；不声称正常用户流程一定触发旧路径。`
- `security_audit/03_evidence_chains.md:262`
  `- 'BR016 / B006'：confirmed，硬编码 Basic credential。`
- `security_audit/03_evidence_chains.md:263`
  `- 'BR026 / B002'：confirmed，token 存普通 SharedPreferences。`
- `security_audit/03_evidence_chains.md:264`
  `- 'BR034 / B026'：confirmed，deep link code 到 token endpoint。`
- `security_audit/03_evidence_chains.md:265`
  `- 'BR091 / B010'：Fitbit 这里主要是第三方导入/Google Fit 写入，不作为 Firebase cloud confirmed 的主证据。`
- `security_audit/03_evidence_chains.md:310`
  `Fitbit/Google Fit 都是用户授权后的第三方健康平台集成。报告确认 token 存储和数据写入/读取路径，不声称未授权泄露。Fitbit scope 包含 location/heartrate/sleep 等较广，但当前代码证据主要展示 body weight API；单个 scope 字符串不能单独作为敏感数据泄露 confirmed。`
- `security_audit/03_evidence_chains.md:316`
  `- 'BR032 / B026'：confirmed。`
- `security_audit/03_evidence_chains.md:317`
  `- 'BR034 / B026'：confirmed。`
- `security_audit/03_evidence_chains.md:318`
  `- 'BR035 / B026'：confirmed。`
- `security_audit/03_evidence_chains.md:364`
  `静态路径 confirmed。动态上能否由任意 App 成功触发、是否受 Android 任务栈/用户确认影响，需要 ADB/browser 实测，因此 BR084 仍 not_testable。`
- `security_audit/03_evidence_chains.md:370`
  `- 'BR016 / B006'：confirmed。`
- `security_audit/04_paper_source_review.md:25`
  `- 'BR018' retained confirmed。`
- `security_audit/04_paper_source_review.md:26`
  `- 'BR047' retained confirmed，但明确是“静态敏感日志代码”，不是“运行时日志文件已泄露”。`
- `security_audit/04_paper_source_review.md:49`
  `- 'BR026' retained confirmed，因为 token 存储 API 调用、key 名、读取/使用链路均明确。`
- `security_audit/04_paper_source_review.md:50`
  `- 'BR027' retained confirmed，因为不是单一外部路径字符串，而是敏感 DB 源路径到外部文件复制。`
- `security_audit/04_paper_source_review.md:73`
  `- 'BR025' retained confirmed。`
- `security_audit/04_paper_source_review.md:74`
  `- 'BR092' retained supported_hypothesis；AdMob/AD_ID 证据不足以 confirmed。`
- `security_audit/04_paper_source_review.md:98`
  `- 'BR016' retained confirmed。`
- `security_audit/04_paper_source_review.md:123`
  `- 'BR013' retained confirmed：现行 Withings OAuth 授权入口 HTTP；遗留 Withings 测量 API HTTP。`
- `security_audit/04_paper_source_review.md:124`
  `- 'BR091' retained confirmed：Firebase endpoint + payload + call path 明确。`
- `security_audit/04_paper_source_review.md:146`
  `- 'BR028' retained confirmed，因为 allowBackup 与敏感 SQLite/Prefs 同时存在。`
- `security_audit/04_paper_source_review.md:186`
  `- 对本报告的启发是：不能只凭单个权限 confirmed；必须找 API 调用、功能或数据 sink。`
- `security_audit/04_paper_source_review.md:194`
  `- 'BR001-BR003' 均不升级为 confirmed。'ACCESS_WIFI_STATE'、'AD_ID' 属于 supported_hypothesis 或第三方 SDK 能力，需要运行时 API/流量。`
- `security_audit/04_paper_source_review.md:253`
  `- 'BR032' confirmed：Manifest 多个 'wta://' scheme。`
- `security_audit/04_paper_source_review.md:254`
  `- 'BR034' confirmed：URI 参数进入 token endpoint 和本地 DB 查询。`
- `security_audit/04_paper_source_review.md:255`
  `- 'BR035' confirmed：'wta://measure' 可到本地敏感测量页面，未执行图案锁。`
- `security_audit/05_artifact_inventory.md:35`
  `- 'AD_ID'、AdvertisingIdClient、AdMob/Firebase provider 位于第三方 SDK/资源配置，只有 supported_hypothesis，不作为第一方 confirmed 泄露。`
- `security_audit/05_artifact_inventory.md:83`
  `- 'http://wta-backup.oss-cn-shanghai.aliyuncs.com/food_database/...' 等食物数据库下载 URL。该类不是健康数据上传，不作为 BR013 confirmed 主证据，但属于独立内容完整性复测候选。`
- `security_audit/05_artifact_inventory.md:98`
  `- HTTP endpoint 仍按 BR013 confirmed，不混同为 TrustManager/HostnameVerifier。`
- `security_audit/05_artifact_inventory.md:128`
  `- 'BR047' confirmed 静态敏感日志代码。`
- `security_audit/06_final_advisor_review.md:6`
  `2. 对每个 confirmed 结论检查：是否有论文依据、是否有 App 中双重或链式证据、是否误把单个字符串/权限/SDK/URL当成漏洞。`
- `security_audit/06_final_advisor_review.md:10`
  `## 1. retained confirmed`
- `security_audit/06_final_advisor_review.md:21`
  `- 保留 confirmed。`
- `security_audit/06_final_advisor_review.md:37`
  `- 保留 confirmed，但不要声称“真实用户数据明文样本已读取”，因为没有运行时 DB。`
- `security_audit/06_final_advisor_review.md:52`
  `- 保留 confirmed。`

## BR092

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/androidx/appcompat/R.java:1724`
  `public static final int[] SearchView = {android.R.attr.focusable, android.R.attr.maxWidth, android.R.attr.inputType, android.R.attr.imeOptions, com.ikdong.weight.R.attr.closeIcon, com.ikdong.weight.R.attr.commitIcon, com.ikdong.weight.R.attr.defaultQueryHint, com.ikdong.weight.R.attr.goIcon, com.ikd...`
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:2352`
  `return (Build.VERSION.SDK_INT < 21 || !this.mPowerManager.isPowerSaveMode()) ? 1 : 2;`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:203`
  `canvas.save();`
- `sources/androidx/appcompat/view/menu/ActionMenuItemView.java:99`
  `this.mSavedPaddingLeft = i;`
- `sources/androidx/appcompat/widget/ActionMenuPresenter.java:482`
  `public Parcelable onSaveInstanceState() {`
- `sources/androidx/appcompat/widget/ActivityChooserModel.java:170`
  `synchronized (this.mInstanceLock) {`
- `sources/androidx/appcompat/widget/AppCompatRatingBar.java:30`
  `protected synchronized void onMeasure(int i, int i2) {`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:136`
  `int iSave = canvas.save();`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:142`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:27`
  `private boolean mAsyncFontPending;`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:223`
  `if (this.mAsyncFontPending) {`
- `sources/androidx/appcompat/widget/AppCompatTextHelper.java:306`
  `this.mAsyncFontPending = this.mFontTypeface == null;`
- `sources/androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:266`
  `synchronized (rectF) {`
- `sources/androidx/appcompat/widget/ButtonBarLayout.java:25`
  `saveAttributeDataForStyleable(context, R.styleable.ButtonBarLayout, attributeSet, typedArrayObtainStyledAttributes, 0, 0);`
- `sources/androidx/appcompat/widget/SearchView.java:90`
  `private final View mSubmitArea;`
- `sources/androidx/appcompat/widget/SearchView.java:91`
  `private boolean mSubmitButtonEnabled;`
- `sources/androidx/appcompat/widget/SwitchCompat.java:857`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/cardview/widget/CardViewBaseImpl.java:34`
  `int iSave = canvas.save();`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:208`
  `int iSave = canvas.save();`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:223`
  `int iSave3 = canvas.save();`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:230`
  `canvas.restoreToCount(iSave3);`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:231`
  `int iSave4 = canvas.save();`
- `sources/androidx/cardview/widget/RoundRectDrawableWithShadow.java:238`
  `canvas.restoreToCount(iSave4);`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:129`
  `sRectPool = new Pools.SynchronizedPool(12);`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:819`
  `int iSave = canvas.save();`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:824`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/core/content/ContextCompat.java:78`
  `private static final Object sSync = new Object();`
- `sources/androidx/core/content/ContextCompat.java:143`
  `synchronized (sLock) {`
- `sources/androidx/core/content/pm/ShortcutManagerCompat.java:186`
  `public static void reportShortcutUsed(Context context, String str) {`
- `sources/androidx/core/content/res/FontResourcesParserCompat.java:23`
  `public static final int FETCH_STRATEGY_ASYNC = 1;`
- `sources/androidx/core/location/LocationManagerCompat.java:147`
  `synchronized (sLocationListeners) {`
- `sources/androidx/core/location/LocationManagerCompat.java:156`
  `synchronized (sLocationListeners) {`
- `sources/androidx/core/location/LocationManagerCompat.java:190`
  `synchronized (weakHashMap) {`
- `sources/androidx/core/location/LocationManagerCompat.java:260`
  `synchronized (GnssLazyLoader.sGnssStatusListeners) {`
- `sources/androidx/core/location/LocationManagerCompat.java:269`
  `synchronized (GnssLazyLoader.sGnssStatusListeners) {`
- `sources/androidx/core/location/LocationManagerCompat.java:278`
  `synchronized (GnssLazyLoader.sGnssStatusListeners) {`
- `sources/androidx/core/view/ViewCompat.java:185`
  `public static void saveAttributeDataForStyleable(View view, Context context, int[] iArr, AttributeSet attributeSet, TypedArray typedArray, int i, int i2) {`
- `sources/androidx/core/widget/NestedScrollView.java:61`
  `private SavedState mSavedState;`
- `sources/androidx/core/widget/NestedScrollView.java:1250`
  `this.mSavedState = null;`
- `sources/androidx/core/widget/NestedScrollView.java:1334`
  `int iSave = canvas.save();`

## BR093

paper_id: B004
paper_title: Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation

- `sources/androidx/core/os/ProcessCompat.java:72`
  `synchronized (sResolvedLock) {`
- `sources/androidx/fragment/app/Fragment.java:40`
  `import androidx.savedstate.SavedStateRegistryController;`
- `sources/androidx/fragment/app/Fragment.java:41`
  `import androidx.savedstate.SavedStateRegistryOwner;`
- `sources/androidx/fragment/app/Fragment.java:49`
  `public class Fragment implements ComponentCallbacks, View.OnCreateContextMenuListener, LifecycleOwner, ViewModelStoreOwner, SavedStateRegistryOwner {`
- `sources/androidx/work/ForegroundUpdater.java:9`
  `ListenableFuture<Void> setForegroundAsync(Context context, UUID uuid, ForegroundInfo foregroundInfo);`
- `sources/androidx/work/impl/utils/WorkForegroundUpdater.java:31`
  `public ListenableFuture<Void> setForegroundAsync(final Context context, final UUID uuid, final ForegroundInfo foregroundInfo) {`
- `sources/androidx/work/impl/utils/WorkForegroundUpdater.java:41`
  `throw new IllegalStateException("Calls to setForegroundAsync() must complete before a ListenableWorker signals completion of work by returning an instance of Result.");`
- `sources/com/google/android/gms/internal/ads/zzfdk.java:222`
  `public final synchronized void zzp(String str) {`
- `sources/com/google/android/gms/internal/ads/zzfdk.java:228`
  `public final synchronized void zzq() {`
- `sources/com/google/android/gms/internal/consent_sdk/zzbz.java:15`
  `public static synchronized String zza(Context context) {`
- `sources/com/google/android/gms/internal/gtm/zzcn.java:28`
  `Preconditions.checkNotMainThread("ClientId should be saved from worker thread");`
- `sources/com/google/android/gms/measurement/internal/zzal.java:21`
  `private static final String[] zzc = {"app_version", "ALTER TABLE apps ADD COLUMN app_version TEXT;", "app_store", "ALTER TABLE apps ADD COLUMN app_store TEXT;", "gmp_version", "ALTER TABLE apps ADD COLUMN gmp_version INTEGER;", "dev_cert_hash", "ALTER TABLE apps ADD COLUMN dev_cert_hash INTEGER;", "...`
- `sources/com/google/android/gms/measurement/internal/zzal.java:402`
  `contentValues.put("adid_reporting_enabled", Boolean.valueOf(zzgVar.zzai()));`
- `sources/com/google/android/gms/measurement/internal/zzlk.java:558`
  `zzI(sb, 1, "service_upload", Boolean.valueOf(zzgcVar.zzaZ()));`
- `sources/com/google/android/material/datepicker/MaterialDatePicker.java:100`
  `super.onSaveInstanceState(bundle);`
- `sources/com/google/firebase/installations/remote/RequestLimiter.java:39`
  `private synchronized void resetBackoffStrategy() {`
- `sources/com/ikdong/weight/activity/SyncGoogleFitActivity.java:304`
  `a.a(this, timeInMillis, calendar2.getTimeInMillis(), new a.InterfaceC0054a() { // from class: com.ikdong.weight.activity.-$$Lambda$SyncGoogleFitActivity$B-xQrzb7g1J4cAaEAr9Am1ndwjE`
- `sources/com/ikdong/weight/widget/fragment/DrinkDetailFragment.java:81`
  `this.f2833a.save();`
- `sources/com/ikdong/weight/widget/fragment/FoodPlanDetailFragment.java:102`
  `FoodPlanDetailFragment.this.f3090b.save();`

## BR094

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `sources/a/a/a/f.java:50`
  `synchronized (this) {`
- `sources/android/support/customtabs/ICustomTabsCallback.java:18`
  `void onPostMessage(String str, Bundle bundle);`
- `sources/android/support/customtabs/ICustomTabsCallback.java:27`
  `static final int TRANSACTION_onPostMessage = 5;`
- `sources/android/support/customtabs/ICustomTabsService.java:22`
  `boolean requestPostMessageChannel(ICustomTabsCallback iCustomTabsCallback, Uri uri);`
- `sources/android/support/customtabs/ICustomTabsService.java:35`
  `static final int TRANSACTION_postMessage = 8;`
- `sources/android/support/customtabs/ICustomTabsService.java:36`
  `static final int TRANSACTION_requestPostMessageChannel = 7;`
- `sources/android/support/customtabs/ICustomTabsService.java:113`
  `parcel2.writeInt(iPostMessage);`
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
- `sources/androidx/appcompat/app/AppCompatDelegateImpl.java:122`
  `boolean mInvalidatePanelMenuPosted;`
- `sources/androidx/appcompat/graphics/drawable/DrawerArrowDrawable.java:203`
  `canvas.save();`
- `sources/androidx/appcompat/view/menu/ListMenuPresenter.java:150`
  `public void saveHierarchyState(Bundle bundle) {`
- `sources/androidx/appcompat/widget/ActivityChooserView.java:95`
  `saveAttributeDataForStyleable(context, R.styleable.ActivityChooserView, attributeSet, typedArrayObtainStyledAttributes, i, 0);`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:136`
  `int iSave = canvas.save();`
- `sources/androidx/appcompat/widget/AppCompatSeekBarHelper.java:142`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/appcompat/widget/DrawableUtils.java:41`
  `/* JADX WARN: Failed to restore switch over string. Please report as a decompilation issue */`
- `sources/androidx/appcompat/widget/ForwardingListener.java:136`
  `r0.postDelayed(r6, r3)`
- `sources/androidx/appcompat/widget/ForwardingListener.java:146`
  `r0.postDelayed(r6, r3)`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:63`
  `public static synchronized ResourceManagerInternal get() {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:80`
  `public synchronized void setHooks(ResourceManagerHooks resourceManagerHooks) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:107`
  `public synchronized void onConfigurationChanged(Context context) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:219`
  `private synchronized Drawable getCachedDrawable(Context context, long j) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:235`
  `private synchronized boolean addDrawableToCache(Context context, long j, Drawable drawable) {`
- `sources/androidx/appcompat/widget/ResourceManagerInternal.java:249`
  `synchronized Drawable onDrawableLoadedFromResources(Context context, VectorEnabledTintResources vectorEnabledTintResources, int i) {`
- `sources/androidx/appcompat/widget/SearchView.java:90`
  `private final View mSubmitArea;`
- `sources/androidx/appcompat/widget/SearchView.java:239`
  `View viewFindViewById2 = findViewById(R.id.submit_area);`
- `sources/androidx/appcompat/widget/SearchView.java:240`
  `this.mSubmitArea = viewFindViewById2;`
- `sources/androidx/appcompat/widget/SearchView.java:621`
  `post(this.mUpdateDrawableStateRunnable);`
- `sources/androidx/appcompat/widget/SearchView.java:630`
  `Drawable background2 = this.mSubmitArea.getBackground();`
- `sources/androidx/appcompat/widget/SwitchCompat.java:857`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/appcompat/widget/TooltipCompatHandler.java:134`
  `this.mAnchor.postDelayed(this.mHideRunnable, j2);`
- `sources/androidx/appcompat/widget/TooltipCompatHandler.java:169`
  `this.mAnchor.postDelayed(this.mShowRunnable, ViewConfiguration.getLongPressTimeout());`
- `sources/androidx/asynclayoutinflater/R.java:1`
  `package androidx.asynclayoutinflater;`
- `sources/androidx/asynclayoutinflater/view/AsyncLayoutInflater.java:1`
  `package androidx.asynclayoutinflater.view;`

## BR095

paper_id: B025
paper_title: Why Eve and Mallory Still Love Android: Revisiting TLS (In)Security in Android Applications

- `resources/AndroidManifest.xml:2`
  `<manifest xmlns:android="http://schemas.android.com/apk/res/android"`
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
  `<shape xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/drawable/abc_seekbar_tick_mark_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/abc_text_cursor_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/res/drawable/abc_vector_test.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/admob_close_button_black_circle_white_cross.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/admob_close_button_white_circle_black_cross.xml:2`
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
- `resources/res/drawable/cell_line_divider.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/res/drawable/circle.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/design_ic_visibility.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/design_ic_visibility_off.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/group_channel_list_unread_background.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
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
- `resources/res/drawable/nnf_ic_create_new_folder_white_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/nnf_ic_folder_black_48dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/nnf_ic_save_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable/profile_placeholder.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/res/drawable/typing_indicator_dot.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
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
- `resources/res/drawable-anydpi-v21/baseline_home_white_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/baseline_more_horiz_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_accessibility_grey_600_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_add_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_add_white_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_all_inclusive_white_36dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_arrow_back_white_36dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_arrow_downward_grey_600_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_arrow_downward_white_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_arrow_drop_down_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_arrow_drop_down_black_36dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_arrow_drop_up_black_36dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_arrow_drop_up_grey_500_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_arrow_forward_white_36dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_arrow_upward_grey_600_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_arrow_upward_white_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_assignment_grey_600_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_autorenew_grey_600_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_beenhere_white_48dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_book_white_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_check_box_grey_600_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_close_white_36dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_cloud_upload_grey_600_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_date_range_white_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_domain_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_done_white_36dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/drawable-anydpi-v21/ic_down.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`

## BR096

paper_id: B011
paper_title: Locking it down: The privacy and security of mobile medication apps

- `resources/res/color/design_box_stroke_color.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/layout/design_text_input_end_icon.xml:2`
  `<com.google.android.material.internal.CheckableImageButton xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/design_text_input_start_icon.xml:2`
  `<com.google.android.material.internal.CheckableImageButton xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout/msg_activity_login.xml:2`
  `<androidx.coordinatorlayout.widget.CoordinatorLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto"`
- `resources/res/layout/mtrl_picker_text_input_date.xml:2`
  `<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/res/layout-v21/msg_activity_login.xml:2`
  `<androidx.coordinatorlayout.widget.CoordinatorLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto"`
- `resources/res/menu/context_delete.xml:2`
  `<menu xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto">`
- `resources/res/menu/drink_poupup_menu.xml:2`
  `<menu xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/res/values/strings.xml:119`
  `<string name="firebase_database_url">https://weighttrackassistant.firebaseio.com</string>`
- `sources/com/google/android/gms/ads/internal/util/zzay.java:17`
  `zzt.zzY(this.zza.zza, Uri.parse("https://support.google.com/dfp_premium/answer/7160685#push"));`
- `sources/com/google/android/gms/auth/api/credentials/IdentityProviders.java:8`
  `public static final String FACEBOOK = "https://www.facebook.com";`
- `sources/com/google/android/gms/auth/api/credentials/IdentityProviders.java:9`
  `public static final String GOOGLE = "https://accounts.google.com";`
- `sources/com/google/android/gms/auth/api/credentials/IdentityProviders.java:10`
  `public static final String LINKEDIN = "https://www.linkedin.com";`
- `sources/com/google/android/gms/auth/api/credentials/IdentityProviders.java:11`
  `public static final String MICROSOFT = "https://login.live.com";`
- `sources/com/google/android/gms/auth/api/credentials/IdentityProviders.java:12`
  `public static final String PAYPAL = "https://www.paypal.com";`
- `sources/com/google/android/gms/auth/api/credentials/IdentityProviders.java:13`
  `public static final String TWITTER = "https://twitter.com";`
- `sources/com/google/android/gms/auth/api/credentials/IdentityProviders.java:14`
  `public static final String YAHOO = "https://login.yahoo.com";`
- `sources/com/google/android/gms/common/FirstPartyScopes.java:5`
  `public static final String GAMES_1P = "https://www.googleapis.com/auth/games.firstparty";`
- `sources/com/google/android/gms/common/Scopes.java:5`
  `public static final String APP_STATE = "https://www.googleapis.com/auth/appstate";`
- `sources/com/google/android/gms/common/Scopes.java:6`
  `public static final String CLOUD_SAVE = "https://www.googleapis.com/auth/datastoremobile";`
- `sources/com/google/android/gms/common/Scopes.java:7`
  `public static final String DRIVE_APPFOLDER = "https://www.googleapis.com/auth/drive.appdata";`
- `sources/com/google/android/gms/common/Scopes.java:8`
  `public static final String DRIVE_APPS = "https://www.googleapis.com/auth/drive.apps";`
- `sources/com/google/android/gms/common/Scopes.java:9`
  `public static final String DRIVE_FILE = "https://www.googleapis.com/auth/drive.file";`
- `sources/com/google/android/gms/common/Scopes.java:10`
  `public static final String DRIVE_FULL = "https://www.googleapis.com/auth/drive";`
- `sources/com/google/android/gms/common/Scopes.java:12`
  `public static final String GAMES = "https://www.googleapis.com/auth/games";`
- `sources/com/google/android/gms/common/Scopes.java:13`
  `public static final String GAMES_LITE = "https://www.googleapis.com/auth/games_lite";`
- `sources/com/google/android/gms/common/Scopes.java:17`
  `public static final String PLUS_LOGIN = "https://www.googleapis.com/auth/plus.login";`
- `sources/com/google/android/gms/common/Scopes.java:18`
  `public static final String PLUS_ME = "https://www.googleapis.com/auth/plus.me";`
- `sources/com/google/android/gms/fitness/Fitness.java:193`
  `SCOPE_ACTIVITY_READ = new Scope("https://www.googleapis.com/auth/fitness.activity.read");`
- `sources/com/google/android/gms/fitness/Fitness.java:194`
  `SCOPE_ACTIVITY_READ_WRITE = new Scope("https://www.googleapis.com/auth/fitness.activity.write");`
- `sources/com/google/android/gms/fitness/Fitness.java:195`
  `SCOPE_LOCATION_READ = new Scope("https://www.googleapis.com/auth/fitness.location.read");`
- `sources/com/google/android/gms/fitness/Fitness.java:196`
  `SCOPE_LOCATION_READ_WRITE = new Scope("https://www.googleapis.com/auth/fitness.location.write");`
- `sources/com/google/android/gms/fitness/Fitness.java:197`
  `SCOPE_BODY_READ = new Scope("https://www.googleapis.com/auth/fitness.body.read");`
- `sources/com/google/android/gms/fitness/Fitness.java:198`
  `SCOPE_BODY_READ_WRITE = new Scope("https://www.googleapis.com/auth/fitness.body.write");`
- `sources/com/google/android/gms/fitness/Fitness.java:199`
  `SCOPE_NUTRITION_READ = new Scope("https://www.googleapis.com/auth/fitness.nutrition.read");`
- `sources/com/google/android/gms/fitness/Fitness.java:200`
  `SCOPE_NUTRITION_READ_WRITE = new Scope("https://www.googleapis.com/auth/fitness.nutrition.write");`
- `sources/com/google/android/gms/fitness/Fitness.java:201`
  `zzkf = new Scope("https://www.googleapis.com/auth/fitness.heart_rate.read");`
- `sources/com/google/android/gms/fitness/Fitness.java:202`
  `zzkg = new Scope("https://www.googleapis.com/auth/fitness.heart_rate.write");`
- `sources/com/google/android/gms/fitness/Fitness.java:203`
  `zzkh = new Scope("https://www.googleapis.com/auth/fitness.respiratory_rate.read");`
- `sources/com/google/android/gms/fitness/Fitness.java:204`
  `zzki = new Scope("https://www.googleapis.com/auth/fitness.respiratory_rate.write");`
- `sources/com/google/android/gms/fitness/Fitness.java:205`
  `zzkj = new Scope("https://www.googleapis.com/auth/fitness.sleep.read");`
- `sources/com/google/android/gms/fitness/Fitness.java:206`
  `zzkk = new Scope("https://www.googleapis.com/auth/fitness.sleep.write");`
- `sources/com/google/android/gms/fitness/FitnessOptions.java:54`
  `this.zzkl.add(new Scope("https://www.googleapis.com/auth/fitness.activity.read"));`
- `sources/com/google/android/gms/fitness/FitnessOptions.java:56`
  `this.zzkl.add(new Scope("https://www.googleapis.com/auth/fitness.activity.write"));`
- `sources/com/google/android/gms/fitness/FitnessOptions.java:66`
  `this.zzkl.add(new Scope("https://www.googleapis.com/auth/fitness.sleep.read"));`
- `sources/com/google/android/gms/fitness/FitnessOptions.java:68`
  `this.zzkl.add(new Scope("https://www.googleapis.com/auth/fitness.sleep.write"));`
- `sources/com/google/android/gms/fitness/data/DataType.java:171`
  `DataType dataType = new DataType("com.google.step_count.delta", 2, "https://www.googleapis.com/auth/fitness.activity.read", "https://www.googleapis.com/auth/fitness.activity.write", Field.FIELD_STEPS);`
- `sources/com/google/android/gms/fitness/data/DataType.java:173`
  `TYPE_STEP_COUNT_CUMULATIVE = new DataType("com.google.step_count.cumulative", 1, "https://www.googleapis.com/auth/fitness.activity.read", "https://www.googleapis.com/auth/fitness.activity.write", Field.FIELD_STEPS);`
- `sources/com/google/android/gms/fitness/data/DataType.java:174`
  `TYPE_STEP_COUNT_CADENCE = new DataType("com.google.step_count.cadence", 1, "https://www.googleapis.com/auth/fitness.activity.read", "https://www.googleapis.com/auth/fitness.activity.write", Field.FIELD_RPM);`
- `sources/com/google/android/gms/fitness/data/DataType.java:175`
  `zzmd = new DataType("com.google.internal.goal", 2, "https://www.googleapis.com/auth/fitness.activity.read", "https://www.googleapis.com/auth/fitness.activity.write", Field.zznd);`
- `sources/com/google/android/gms/fitness/data/DataType.java:176`
  `TYPE_ACTIVITY_SEGMENT = new DataType("com.google.activity.segment", 2, "https://www.googleapis.com/auth/fitness.activity.read", "https://www.googleapis.com/auth/fitness.activity.write", Field.FIELD_ACTIVITY);`
- `sources/com/google/android/gms/fitness/data/DataType.java:177`
  `TYPE_SLEEP_SEGMENT = new DataType("com.google.sleep.segment", 2, "https://www.googleapis.com/auth/fitness.sleep.read", "https://www.googleapis.com/auth/fitness.sleep.write", Field.FIELD_SLEEP_SEGMENT_TYPE);`
- `sources/com/google/android/gms/fitness/data/DataType.java:178`
  `DataType dataType2 = new DataType("com.google.calories.expended", 2, "https://www.googleapis.com/auth/fitness.activity.read", "https://www.googleapis.com/auth/fitness.activity.write", Field.FIELD_CALORIES);`
- `sources/com/google/android/gms/fitness/data/DataType.java:180`
  `TYPE_BASAL_METABOLIC_RATE = new DataType("com.google.calories.bmr", 1, "https://www.googleapis.com/auth/fitness.activity.read", "https://www.googleapis.com/auth/fitness.activity.write", Field.FIELD_CALORIES);`
- `sources/com/google/android/gms/fitness/data/DataType.java:181`
  `TYPE_POWER_SAMPLE = new DataType("com.google.power.sample", 1, "https://www.googleapis.com/auth/fitness.activity.read", "https://www.googleapis.com/auth/fitness.activity.write", Field.FIELD_WATTS);`
- `sources/com/google/android/gms/fitness/data/DataType.java:182`
  `zzme = new DataType("com.google.sensor.events", 2, "https://www.googleapis.com/auth/fitness.activity.read", "https://www.googleapis.com/auth/fitness.activity.write", Field.zznf, Field.zzng, Field.zznh);`
- `sources/com/google/android/gms/fitness/data/DataType.java:183`
  `TYPE_HEART_RATE_BPM = new DataType("com.google.heart_rate.bpm", 1, "https://www.googleapis.com/auth/fitness.heart_rate.read", "https://www.googleapis.com/auth/fitness.heart_rate.write", Field.FIELD_BPM);`
- `sources/com/google/android/gms/fitness/data/DataType.java:184`
  `zzmf = new DataType("com.google.respiratory_rate", 1, "https://www.googleapis.com/auth/fitness.respiratory_rate.read", "https://www.googleapis.com/auth/fitness.respiratory_rate.write", Field.zznc);`
- `sources/com/google/android/gms/fitness/data/DataType.java:185`
  `TYPE_LOCATION_SAMPLE = new DataType("com.google.location.sample", 1, "https://www.googleapis.com/auth/fitness.location.read", "https://www.googleapis.com/auth/fitness.location.write", Field.FIELD_LATITUDE, Field.FIELD_LONGITUDE, Field.FIELD_ACCURACY, Field.FIELD_ALTITUDE);`
- `sources/com/google/android/gms/fitness/data/DataType.java:186`
  `TYPE_LOCATION_TRACK = new DataType("com.google.location.track", 2, "https://www.googleapis.com/auth/fitness.location.read", "https://www.googleapis.com/auth/fitness.location.write", Field.FIELD_LATITUDE, Field.FIELD_LONGITUDE, Field.FIELD_ACCURACY, Field.FIELD_ALTITUDE);`
- `sources/com/google/android/gms/fitness/data/DataType.java:187`
  `DataType dataType3 = new DataType("com.google.distance.delta", 2, "https://www.googleapis.com/auth/fitness.location.read", "https://www.googleapis.com/auth/fitness.location.write", Field.FIELD_DISTANCE);`
- `sources/com/google/android/gms/fitness/data/DataType.java:189`
  `zzmg = new DataType("com.google.distance.cumulative", 1, "https://www.googleapis.com/auth/fitness.location.read", "https://www.googleapis.com/auth/fitness.location.write", Field.FIELD_DISTANCE);`
- `sources/com/google/android/gms/fitness/data/DataType.java:190`
  `TYPE_SPEED = new DataType("com.google.speed", 1, "https://www.googleapis.com/auth/fitness.location.read", "https://www.googleapis.com/auth/fitness.location.write", Field.FIELD_SPEED);`
- `sources/com/google/android/gms/fitness/data/DataType.java:191`
  `TYPE_CYCLING_WHEEL_REVOLUTION = new DataType("com.google.cycling.wheel_revolution.cumulative", 1, "https://www.googleapis.com/auth/fitness.location.read", "https://www.googleapis.com/auth/fitness.location.write", Field.FIELD_REVOLUTIONS);`
- `sources/com/google/android/gms/fitness/data/DataType.java:192`
  `TYPE_CYCLING_WHEEL_RPM = new DataType("com.google.cycling.wheel_revolution.rpm", 1, "https://www.googleapis.com/auth/fitness.location.read", "https://www.googleapis.com/auth/fitness.location.write", Field.FIELD_RPM);`
- `sources/com/google/android/gms/fitness/data/DataType.java:193`
  `TYPE_CYCLING_PEDALING_CUMULATIVE = new DataType("com.google.cycling.pedaling.cumulative", 1, "https://www.googleapis.com/auth/fitness.activity.read", "https://www.googleapis.com/auth/fitness.activity.write", Field.FIELD_REVOLUTIONS);`
- `sources/com/google/android/gms/fitness/data/DataType.java:194`
  `TYPE_CYCLING_PEDALING_CADENCE = new DataType("com.google.cycling.pedaling.cadence", 1, "https://www.googleapis.com/auth/fitness.activity.read", "https://www.googleapis.com/auth/fitness.activity.write", Field.FIELD_RPM);`
- `sources/com/google/android/gms/fitness/data/DataType.java:195`
  `TYPE_HEIGHT = new DataType("com.google.height", 1, "https://www.googleapis.com/auth/fitness.body.read", "https://www.googleapis.com/auth/fitness.body.write", Field.FIELD_HEIGHT);`
- `sources/com/google/android/gms/fitness/data/DataType.java:196`
  `TYPE_WEIGHT = new DataType("com.google.weight", 1, "https://www.googleapis.com/auth/fitness.body.read", "https://www.googleapis.com/auth/fitness.body.write", Field.FIELD_WEIGHT);`
- `sources/com/google/android/gms/fitness/data/DataType.java:197`
  `TYPE_BODY_FAT_PERCENTAGE = new DataType("com.google.body.fat.percentage", 1, "https://www.googleapis.com/auth/fitness.body.read", "https://www.googleapis.com/auth/fitness.body.write", Field.FIELD_PERCENTAGE);`
- `sources/com/google/android/gms/fitness/data/DataType.java:198`
  `TYPE_NUTRITION = new DataType("com.google.nutrition", 1, "https://www.googleapis.com/auth/fitness.nutrition.read", "https://www.googleapis.com/auth/fitness.nutrition.write", Field.FIELD_NUTRIENTS, Field.FIELD_MEAL_TYPE, Field.FIELD_FOOD_ITEM);`
- `sources/com/google/android/gms/fitness/data/DataType.java:199`
  `DataType dataType4 = new DataType("com.google.hydration", 1, "https://www.googleapis.com/auth/fitness.nutrition.read", "https://www.googleapis.com/auth/fitness.nutrition.write", Field.FIELD_VOLUME);`
- `sources/com/google/android/gms/fitness/data/DataType.java:201`
  `TYPE_WORKOUT_EXERCISE = new DataType("com.google.activity.exercise", 1, "https://www.googleapis.com/auth/fitness.activity.read", "https://www.googleapis.com/auth/fitness.activity.write", Field.FIELD_EXERCISE, Field.FIELD_REPETITIONS, Field.zzmz, Field.FIELD_RESISTANCE_TYPE, Field.FIELD_RESISTANCE);`
- `sources/com/google/android/gms/fitness/data/DataType.java:202`
  `DataType dataType5 = new DataType("com.google.active_minutes", 2, "https://www.googleapis.com/auth/fitness.activity.read", "https://www.googleapis.com/auth/fitness.activity.write", Field.FIELD_DURATION);`
- `sources/com/google/android/gms/fitness/data/DataType.java:205`
  `zzmh = new DataType("com.google.device_on_body", 1, "https://www.googleapis.com/auth/fitness.activity.read", "https://www.googleapis.com/auth/fitness.activity.write", Field.zznj);`
- `sources/com/google/android/gms/fitness/data/DataType.java:206`
  `zzmi = new DataType("com.google.internal.primary_device", 2, "https://www.googleapis.com/auth/fitness.activity.read", "https://www.googleapis.com/auth/fitness.activity.write", Field.zzne);`
- `sources/com/google/android/gms/fitness/data/DataType.java:207`
  `AGGREGATE_ACTIVITY_SUMMARY = new DataType("com.google.activity.summary", 2, "https://www.googleapis.com/auth/fitness.activity.read", "https://www.googleapis.com/auth/fitness.activity.write", Field.FIELD_ACTIVITY, Field.FIELD_DURATION, Field.FIELD_NUM_SEGMENTS);`
- `sources/com/google/android/gms/fitness/data/DataType.java:208`
  `AGGREGATE_BASAL_METABOLIC_RATE_SUMMARY = new DataType("com.google.calories.bmr.summary", 2, "https://www.googleapis.com/auth/fitness.body.read", "https://www.googleapis.com/auth/fitness.body.write", Field.FIELD_AVERAGE, Field.FIELD_MAX, Field.FIELD_MIN);`
- `sources/com/google/android/gms/fitness/data/DataType.java:212`
  `TYPE_HEART_POINTS = new DataType("com.google.heart_minutes", 2, "https://www.googleapis.com/auth/fitness.activity.read", "https://www.googleapis.com/auth/fitness.activity.write", Field.FIELD_INTENSITY);`
- `sources/com/google/android/gms/fitness/data/DataType.java:213`
  `AGGREGATE_HEART_POINTS = new DataType("com.google.heart_minutes.summary", 2, "https://www.googleapis.com/auth/fitness.activity.read", "https://www.googleapis.com/auth/fitness.activity.write", Field.FIELD_INTENSITY, Field.FIELD_DURATION);`

## BR098

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/com/google/firebase/database/FirebaseDatabase.java:48`
  `String databaseUrl = firebaseApp.getOptions().getDatabaseUrl();`
- `sources/com/google/firebase/storage/network/NetworkRequest.java:92`
  `public static Uri getBaseUrl(EmulatedServiceSettings emulatedServiceSettings) {`
- `sources/com/ikdong/weight/activity/FitBitActivity.java:109`
  `new OkHttpClient.Builder().addInterceptor(new Interceptor() { // from class: com.ikdong.weight.activity.FitBitActivity.2`
- `sources/com/ikdong/weight/activity/FitBitActivity.java:290`
  `Response responseExecute = new OkHttpClient.Builder().addInterceptor(new Interceptor() { // from class: com.ikdong.weight.activity.FitBitActivity.4`
- `sources/com/ikdong/weight/activity/SyncFitbitActivity.java:319`
  `new OkHttpClient.Builder().addInterceptor(new Interceptor() { // from class: com.ikdong.weight.activity.SyncFitbitActivity.5`
- `sources/com/ikdong/weight/activity/SyncFitbitActivity.java:434`
  `Response responseExecute = new OkHttpClient.Builder().addInterceptor(new Interceptor() { // from class: com.ikdong.weight.activity.SyncFitbitActivity.7`
- `sources/com/ikdong/weight/activity/WithingsActivity.java:121`
  `Response responseExecute = new OkHttpClient.Builder().addInterceptor(new Interceptor() { // from class: com.ikdong.weight.activity.WithingsActivity.2`
- `sources/com/ikdong/weight/activity/WithingsActivity.java:146`
  `new OkHttpClient.Builder().addInterceptor(new Interceptor() { // from class: com.ikdong.weight.activity.WithingsActivity.3`
- `sources/com/ikdong/weight/activity/WithingsActivity.java:206`
  `new OkHttpClient.Builder().addInterceptor(new Interceptor() { // from class: com.ikdong.weight.activity.WithingsActivity.5`
- `sources/com/ikdong/weight/integration/withings/a/a.java:25`
  `interfaceC0055a.post(new OkHttpClient.Builder().addInterceptor(new Interceptor() { // from class: com.ikdong.weight.integration.withings.a.-$$Lambda$a$oPj__YvkxxLYHh9aglCg8Q0ngAQ`
- `sources/com/ikdong/weight/integration/withings/a/b.java:47`
  `new OkHttpClient.Builder().addInterceptor(new Interceptor() { // from class: com.ikdong.weight.integration.withings.a.-$$Lambda$b$HFRgRoyaccE01Yxz7Ok9ZSlG0zE`
