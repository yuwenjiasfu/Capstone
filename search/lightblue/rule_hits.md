THE KEY is the represent of API key, it can not be uploaded to GitHub, so I just use the word THE KEY
# Rule Search Hits

## BR001

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:29`
  `<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:30`
  `<uses-permission android:name="android.permission.CAMERA"/>`

## BR002

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:21`
  `<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:22`
  `<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:23`
  `<uses-permission android:name="android.permission.BLUETOOTH_SCAN"/>`

## BR003

paper_id: B023
paper_title: Android Permissions Demystified

- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:15`
  `<uses-permission`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:18`
  `<uses-permission`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:22`
  `<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:23`
  `<uses-permission android:name="android.permission.BLUETOOTH_SCAN"/>`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:24`
  `<uses-permission android:name="android.permission.BLUETOOTH_CONNECT"/>`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:25`
  `<uses-permission android:name="android.permission.BLUETOOTH_ADVERTISE"/>`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:26`
  `<uses-permission android:name="android.permission.INTERNET"/>`

## BR005

paper_id: B021
paper_title: Metadata-Based Privacy Assessment for Mobile mHealth

- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:28`
  `<uses-permission android:name="android.permission.VIBRATE"/>`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:29`
  `<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:30`
  `<uses-permission android:name="android.permission.CAMERA"/>`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:42`
  `<uses-permission android:name="com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE"/>`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:43`
  `<uses-permission android:name="android.permission.ACCESS_ADSERVICES_ATTRIBUTION"/>`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:44`
  `<uses-permission android:name="android.permission.ACCESS_ADSERVICES_AD_ID"/>`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:45`
  `<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>`

## BR009

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/M8/A.java:20`
  `import javax.net.ssl.X509TrustManager;`
- `sources/M8/A.java:280`
  `private static SSLSocketFactory y(X509TrustManager x509TrustManager) {`
- `sources/M8/A.java:283`
  `sSLContextM.init(null, new TrustManager[]{x509TrustManager}, null);`
- `sources/M8/A.java:421`
  `X509TrustManager x509TrustManagerB = N8.e.B();`
- `sources/M8/A.java:422`
  `this.f9581G = y(x509TrustManagerB);`
- `sources/M8/A.java:423`
  `this.f9582H = V8.c.b(x509TrustManagerB);`
- `sources/N8/e.java:38`
  `import javax.net.ssl.X509TrustManager;`
- `sources/N8/e.java:111`
  `public static X509TrustManager B() {`
- `sources/N8/e.java:118`
  `if (trustManager instanceof X509TrustManager) {`
- `sources/N8/e.java:119`
  `return (X509TrustManager) trustManager;`
- `sources/T8/f.java:18`
  `import javax.net.ssl.X509TrustManager;`
- `sources/T8/f.java:142`
  `private final X509TrustManager f12670a;`
- `sources/T8/f.java:147`
  `c(X509TrustManager x509TrustManager, Method method) {`
- `sources/T8/f.java:149`
  `this.f12670a = x509TrustManager;`
- `sources/T8/f.java:233`
  `public V8.c c(X509TrustManager x509TrustManager) {`
- `sources/T8/f.java:235`
  `Class<?> cls = Class.forName("android.net.http.X509TrustManagerExtensions");`
- `sources/T8/f.java:236`
  `return new a(cls.getConstructor(X509TrustManager.class).newInstance(x509TrustManager), cls.getMethod("checkServerTrusted", X509Certificate[].class, String.class, String.class));`
- `sources/T8/f.java:238`
  `return super.c(x509TrustManager);`
- `sources/T8/f.java:243`
  `public V8.e d(X509TrustManager x509TrustManager) {`
- `sources/T8/f.java:245`
  `Method declaredMethod = x509TrustManager.getClass().getDeclaredMethod("findTrustAnchorByIssuerAndSignature", X509Certificate.class);`
- `sources/T8/f.java:247`
  `return new c(x509TrustManager, declaredMethod);`
- `sources/T8/f.java:249`
  `return super.d(x509TrustManager);`
- `sources/T8/j.java:18`
  `import javax.net.ssl.X509TrustManager;`
- `sources/T8/j.java:101`
  `public V8.c c(X509TrustManager x509TrustManager) {`
- `sources/T8/j.java:102`
  `return new V8.a(d(x509TrustManager));`
- `sources/T8/j.java:105`
  `public V8.e d(X509TrustManager x509TrustManager) {`
- `sources/T8/j.java:106`
  `return new V8.b(x509TrustManager.getAcceptedIssuers());`
- `sources/V8/c.java:5`
  `import javax.net.ssl.X509TrustManager;`
- `sources/V8/c.java:9`
  `public static c b(X509TrustManager x509TrustManager) {`
- `sources/V8/c.java:10`
  `return j.l().c(x509TrustManager);`

## BR010

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/V8/a.java:27`
  `x509Certificate.verify(x509Certificate2.getPublicKey());`

## BR011

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/P8/b.java:73`
  `if (((iOException instanceof SSLHandshakeException) && (iOException.getCause() instanceof CertificateException)) || (iOException instanceof SSLPeerUnverifiedException)) {`

## BR012

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/M8/C1800g.java:48`
  `return "sha256/" + d((X509Certificate) certificate).c();`

## BR013

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `resources/com.punchthrough.lightblueexplorer.apk/res/color/design_box_stroke_color.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/com.punchthrough.lightblueexplorer.apk/res/color/m3_textfield_input_text_color.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$avd_hide_password__0.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$avd_hide_password__1.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$avd_hide_password__2.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$avd_show_password__0.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$avd_show_password__1.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$avd_show_password__2.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$m3_avd_hide_password__0.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$m3_avd_hide_password__1.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$m3_avd_show_password__0.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$m3_avd_show_password__1.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$mtrl_switch_thumb_checked_unchecked__1.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$mtrl_switch_thumb_unchecked_checked__0.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$mtrl_switch_thumb_unchecked_checked__1.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_ab_back_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_arrow_drop_right_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_clear_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_go_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_menu_copy_mtrl_am_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_menu_cut_mtrl_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_menu_overflow_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_menu_paste_mtrl_am_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_menu_selectall_mtrl_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_menu_share_mtrl_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_voice_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_seekbar_tick_mark_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_star_black_48dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_star_half_black_48dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_text_cursor_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_vector_test.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/arrow_down.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/arrow_down_to_line.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/arrow_up.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/arrow_up_to_line.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/avd_hide_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_hide_password__0_res_0x7f080000">`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/avd_show_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_show_password__0_res_0x7f080003">`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/btn_checkbox_checked_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/btn_checkbox_unchecked_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`

## BR014

paper_id: B022
paper_title: A Study of Android Application Security

- `sources/androidx/appcompat/app/h.java:1150`
  `boolean z10 = KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1;`
- `sources/androidx/appcompat/app/w.java:693`
  `menuE.setQwertyMode(KeyCharacterMap.load(keyEvent != null ? keyEvent.getDeviceId() : -1).getKeyboardType() != 1);`
- `sources/androidx/compose/ui/platform/r.java:1291`
  `MotionEvent motionEventObtain = MotionEvent.obtain(motionEvent.getDownTime() == motionEvent.getEventTime() ? j9 : motionEvent.getDownTime(), j9, i9, pointerCount, pointerPropertiesArr, pointerCoordsArr, motionEvent.getMetaState(), z9 ? 0 : motionEvent.getButtonState(), motionEvent.getXPrecision(), m...`
- `sources/androidx/compose/ui/platform/r.java:1476`
  `return getFocusOwner().a(new C3465b(AbstractC2233b0.h(viewConfiguration, getContext()) * f9, f9 * AbstractC2233b0.e(viewConfiguration, getContext()), motionEvent.getEventTime(), motionEvent.getDeviceId()));`
- `sources/androidx/core/view/C2258o.java:69`
  `iArr[0] = AbstractC2233b0.g(context, viewConfiguration, motionEvent.getDeviceId(), i9, motionEvent.getSource());`
- `sources/androidx/core/view/C2258o.java:70`
  `iArr[1] = AbstractC2233b0.f(context, viewConfiguration, motionEvent.getDeviceId(), i9, motionEvent.getSource());`
- `sources/androidx/core/view/C2258o.java:75`
  `int deviceId = motionEvent.getDeviceId();`
- `sources/com/google/android/datatransport/cct/d.java:21`
  `import android.telephony.TelephonyManager;`
- `sources/com/google/android/datatransport/cct/d.java:319`
  `private static TelephonyManager k(Context context) {`
- `sources/com/google/android/datatransport/cct/d.java:320`
  `return (TelephonyManager) context.getSystemService("phone");`
- `sources/D/J.java:17`
  `return context.getDeviceId();`
- `sources/E/d.java:28`
  `return context.getDeviceId();`
- `sources/m3/C3844a.java:113`
  `throw new IOException("AdvertisingIdClient is not connected.");`
- `sources/m3/C3844a.java:119`
  `throw new IOException("AdvertisingIdClient cannot reconnect.");`
- `sources/m3/C3844a.java:122`
  `throw new IOException("AdvertisingIdClient cannot reconnect.", e9);`
- `sources/m3/C3844a.java:130`
  `Log.i("AdvertisingIdClient", "GMS remote exception ", e10);`
- `sources/m3/C3844a.java:170`
  `Log.i("AdvertisingIdClient", "AdvertisingIdClient unbindService failed.", th);`
- `sources/m3/C3844a.java:242`
  `map.put("tag", "AdvertisingIdClient");`

## BR015

paper_id: B022
paper_title: A Study of Android Application Security

- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:116`
  `return "HUAWEI".equalsIgnoreCase(Build.BRAND) && "HWANE".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:120`
  `return "OnePlus".equalsIgnoreCase(Build.BRAND) && "OnePlus6".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:124`
  `return "OnePlus".equalsIgnoreCase(Build.BRAND) && "OnePlus6T".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:128`
  `return "REDMI".equalsIgnoreCase(Build.BRAND) && "joyeuse".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:132`
  `return "SAMSUNG".equalsIgnoreCase(Build.BRAND) && "J7XELTE".equalsIgnoreCase(Build.DEVICE) && Build.VERSION.SDK_INT >= 27;`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExcludedSupportedSizesQuirk.java:136`
  `return "SAMSUNG".equalsIgnoreCase(Build.BRAND) && "ON7XELTE".equalsIgnoreCase(Build.DEVICE) && Build.VERSION.SDK_INT >= 27;`
- `sources/androidx/camera/camera2/internal/compat/quirk/ExtraSupportedSurfaceCombinationsQuirk.java:58`
  `String str = Build.DEVICE;`
- `sources/androidx/camera/camera2/internal/compat/quirk/ImageCaptureFailedWhenVideoCaptureIsBoundQuirk.java:29`
  `if (!"samsung".equalsIgnoreCase(Build.BRAND)) {`
- `sources/androidx/camera/camera2/internal/compat/quirk/ImageCaptureFailedWhenVideoCaptureIsBoundQuirk.java:32`
  `String str = Build.DEVICE;`
- `sources/androidx/camera/camera2/internal/compat/quirk/ImageCaptureFailedWhenVideoCaptureIsBoundQuirk.java:37`
  `return "vivo".equalsIgnoreCase(Build.BRAND) && "vivo 1805".equalsIgnoreCase(Build.MODEL);`
- `sources/androidx/camera/camera2/internal/compat/quirk/JpegHalCorruptImageQuirk.java:18`
  `return f19044a.contains(Build.DEVICE.toLowerCase(Locale.US));`
- `sources/androidx/camera/camera2/internal/compat/quirk/PreviewPixelHDRnetQuirk.java:16`
  `return "Google".equals(Build.MANUFACTURER) && f19046a.contains(Build.DEVICE.toLowerCase(Locale.getDefault()));`
- `sources/androidx/camera/core/internal/compat/quirk/ImageCaptureRotationOptionQuirk.java:13`
  `String str2 = Build.MODEL;`
- `sources/androidx/camera/core/internal/compat/quirk/ImageCaptureRotationOptionQuirk.java:14`
  `if (str2.contains("google_sdk") || str2.contains("Emulator") || str2.contains("Cuttlefish") || str2.contains("Android SDK built for x86") || Build.MANUFACTURER.contains("Genymotion")) {`
- `sources/androidx/camera/core/internal/compat/quirk/ImageCaptureRotationOptionQuirk.java:17`
  `return (Build.BRAND.startsWith("generic") && Build.DEVICE.startsWith("generic")) || Build.PRODUCT.equals("google_sdk") || Build.HARDWARE.contains("ranchu");`
- `sources/androidx/camera/core/internal/compat/quirk/IncorrectJpegMetadataQuirk.java:17`
  `return "Samsung".equalsIgnoreCase(Build.BRAND) && f19124a.contains(Build.DEVICE.toUpperCase(Locale.US));`
- `sources/androidx/camera/view/internal/compat/quirk/SurfaceViewStretchedQuirk.java:9`
  `return "LENOVO".equalsIgnoreCase(Build.MANUFACTURER) && "Q706F".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/view/internal/compat/quirk/SurfaceViewStretchedQuirk.java:13`
  `return "OPPO".equalsIgnoreCase(Build.MANUFACTURER) && "OP4E75L1".equalsIgnoreCase(Build.DEVICE);`
- `sources/androidx/camera/view/internal/compat/quirk/SurfaceViewStretchedQuirk.java:17`
  `if (!"SAMSUNG".equalsIgnoreCase(Build.MANUFACTURER)) {`
- `sources/androidx/camera/view/internal/compat/quirk/SurfaceViewStretchedQuirk.java:20`
  `String str = Build.DEVICE;`
- `sources/com/google/android/datatransport/cct/d.java:384`
  `return iVar.p().a("sdk-version", Build.VERSION.SDK_INT).c("model", Build.MODEL).c("hardware", Build.HARDWARE).c("device", Build.DEVICE).c("product", Build.PRODUCT).c("os-uild", Build.ID).c("manufacturer", Build.MANUFACTURER).c("fingerprint", Build.FINGERPRINT).b("tz-offset", l()).a("net-type", h(act...`
- `sources/com/google/firebase/FirebaseCommonRegistrar.java:47`
  `arrayList.add(h.b("device-name", e(Build.PRODUCT)));`
- `sources/com/google/firebase/FirebaseCommonRegistrar.java:48`
  `arrayList.add(h.b("device-model", e(Build.DEVICE)));`
- `sources/com/google/firebase/FirebaseCommonRegistrar.java:49`
  `arrayList.add(h.b("device-brand", e(Build.BRAND)));`
- `sources/com/punchthrough/lightblueexplorer/DeviceCapabilitiesActivity.java:84`
  `String str2 = Build.MANUFACTURER;`
- `sources/com/punchthrough/lightblueexplorer/DeviceCapabilitiesActivity.java:86`
  `String str3 = Build.MODEL;`
- `sources/D/J.java:62`
  `A.Q.a("CameraValidator", "Verifying camera lens facing on " + Build.DEVICE + ", lensFacingInteger: " + numD);`
- `sources/X/g.java:21`
  `Q.a("FlashAvailability", String.format("Device is known to throw an exception while checking flash availability. Flash is not available. [Manufacturer: %s, Model: %s, API Level: %d].", Build.MANUFACTURER, Build.MODEL, Integer.valueOf(Build.VERSION.SDK_INT)));`
- `sources/X/g.java:23`
  `Q.d("FlashAvailability", String.format("Exception thrown while checking for flash availability on device not known to throw exceptions during this check. Please file an issue at https://issuetracker.google.com/issues/new?component=618491&template=1257717 with this error message [Manufacturer: %s, Mo...`
- `sources/X0/AbstractC4724t.java:16`
  `private static final boolean f42795a = AbstractC1838t.b(Build.DEVICE, "layoutlib");`

## BR016

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/res/values/public.xml:4501`
  `<public type="string" name="google_api_key" id="0x7f130138" />`
- `resources/res/values/public.xml:4503`
  `<public type="string" name="google_crash_reporting_api_key" id="0x7f13013a" />`
- `resources/res/values/strings.xml:43`
  `<string name="adafruit_auth_error_message">Please check that you\'ve entered your username and secret key correctly.</string>`
- `resources/res/values/strings.xml:315`
  `<string name="google_api_key">AIzaSyDynFtwUV6aAD0kerTCTsOIw6DjvEnl_24</string>`
- `resources/res/values/strings.xml:317`
  `<string name="google_crash_reporting_api_key">AIzaSyDynFtwUV6aAD0kerTCTsOIw6DjvEnl_24</string>`
- `resources/res/values/strings.xml:738`
  `<string name="secret_aio_key">Secret AIO Key</string>`
- `sources/com/punchthrough/lightblueexplorer/R.java:4556`
  `public static final int google_api_key = 0x7f130138;`
- `sources/com/punchthrough/lightblueexplorer/R.java:4558`
  `public static final int google_crash_reporting_api_key = 0x7f13013a;`
- `sources/J5/F.java:43`
  `f7910f = E6.N.k(D6.C.a(f9.d("2C06"), "Acceleration"), D6.C.a(f9.d("2B33"), "ACS Control Point"), D6.C.a(f9.d("2B30"), "ACS Data In"), D6.C.a(f9.d("2B32"), "ACS Data Out Indicate"), D6.C.a(f9.d("2B31"), "ACS Data Out Notify"), D6.C.a(f9.d("2B2F"), "ACS Status"), D6.C.a(f9.d("2BDC"), "Active Preset In...`
- `sources/m3/a.java:58`
  `bundle.putBoolean("com.google.android.gms.signin.internal.forceCodeForRefreshToken", false);`
- `sources/m3/a.java:61`
  `bundle.putBoolean("com.google.android.gms.signin.internal.waitForAccessTokenRefresh", false);`
- `sources/P4/n.java:50`
  `return new n(strA, c4312s.a("google_api_key"), c4312s.a("firebase_database_url"), c4312s.a("ga_trackingId"), c4312s.a("gcm_defaultSenderId"), c4312s.a("google_storage_bucket"), c4312s.a("project_id"));`
- `sources/s4/c.java:81`
  `jSONObject.put("RefreshToken", dVar.f());`
- `sources/s4/c.java:102`
  `String strOptString3 = jSONObjectC.optString("RefreshToken", null);`
- `sources/X5/C4735a.java:36`
  `F fB = aVar.b(aVar.g().g().b("Authorization", "apikey " + this.f42955a).a());`

## BR017

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `sources/com/google/android/gms/measurement/internal/C2953j5.java:193`
  `MessageDigest messageDigestT0 = d6.T0();`
- `sources/com/google/android/gms/measurement/internal/C2953j5.java:194`
  `if (messageDigestT0 == null) {`
- `sources/com/google/android/gms/measurement/internal/C2953j5.java:197`
  `return String.format(Locale.US, "%032X", new BigInteger(1, messageDigestT0.digest(str2.getBytes())));`
- `sources/com/google/android/gms/measurement/internal/Z5.java:1206`
  `MessageDigest messageDigestT0 = d6.T0();`
- `sources/P3/z.java:56`
  `AbstractC4310p.l(messageDigestB);`
- `sources/P3/z.java:57`
  `return String.format("%s: pkg=%s, sha256=%s, atk=%s, ver=%s", str2, str, y3.i.a(messageDigestB.digest(vVar.e0())), Boolean.valueOf(z9), "12451000.false");`
- `sources/Y4/AbstractC4892j.java:272`
  `MessageDigest messageDigest = MessageDigest.getInstance(str);`
- `sources/Y4/AbstractC4892j.java:273`
  `messageDigest.update(bArr);`

## BR018

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/com/google/android/gms/common/api/internal/q.java:50`
  `Log.wtf("GoogleApiManager", "Received null response from onSignInSuccess", new Exception());`
- `sources/com/mailchimp/sdk/api/model/ContactEventResponse.java:7`
  `@Metadata(bv = {1, 0, C3473h.INTEGER_FIELD_NUMBER}, d1 = {"\u0000\f\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\u0018\u00002\u00020\u0001B\u0005¢\u0006\u0002\u0010\u0002¨\u0006\u0003"}, d2 = {"Lcom/mailchimp/sdk/api/model/ContactEventResponse;", "", "()V", "mailchimp-sdk-api_release"}, k...`
- `sources/com/mailchimp/sdk/api/model/ContactEventResponse.java:8`
  `public final class ContactEventResponse {`
- `sources/com/mailchimp/sdk/api/model/UpdateContactResponse.java:8`
  `@Metadata(bv = {1, 0, C3473h.INTEGER_FIELD_NUMBER}, d1 = {"\u0000\"\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0006\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0002\b\u0086\b\u0018\u00002\u00020\u0001B\r\u0012\u0006\u0010\u0002\u001a\u00020\u000...`
- `sources/com/mailchimp/sdk/api/model/UpdateContactResponse.java:9`
  `public final /* data */ class UpdateContactResponse {`
- `sources/com/mailchimp/sdk/api/model/UpdateContactResponse.java:12`
  `public UpdateContactResponse(String str) {`
- `sources/com/mailchimp/sdk/api/model/UpdateContactResponse.java:17`
  `public static /* synthetic */ UpdateContactResponse copy$default(UpdateContactResponse updateContactResponse, String str, int i9, Object obj) {`
- `sources/com/mailchimp/sdk/api/model/UpdateContactResponse.java:19`
  `str = updateContactResponse.email;`
- `sources/com/mailchimp/sdk/api/model/UpdateContactResponse.java:21`
  `return updateContactResponse.copy(str);`
- `sources/com/mailchimp/sdk/api/model/UpdateContactResponse.java:29`
  `public final UpdateContactResponse copy(String email) {`
- `sources/com/mailchimp/sdk/api/model/UpdateContactResponse.java:31`
  `return new UpdateContactResponse(email);`
- `sources/com/mailchimp/sdk/api/model/UpdateContactResponse.java:36`
  `return (other instanceof UpdateContactResponse) && AbstractC1838t.b(this.email, ((UpdateContactResponse) other).email);`
- `sources/com/mailchimp/sdk/api/model/UpdateContactResponse.java:54`
  `return "UpdateContactResponse(email=" + this.email + ")";`

## BR019

paper_id: B011
paper_title: Locking it down: The privacy and security of mobile medication apps

- `sources/A4/i.java:13`
  `JSONObject jSONObject = new JSONObject(str);`
- `sources/A4/i.java:14`
  `return b(jSONObject.getString("rolloutId"), jSONObject.getString("parameterKey"), jSONObject.getString("parameterValue"), jSONObject.getString("variantId"), jSONObject.getLong("templateVersion"));`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:827`
  `this.f21402w.put(getId(), this);`
- `sources/androidx/transition/C2348b.java:382`
  `xVar.f24591a.put("android:changeBounds:bounds", new Rect(view.getLeft(), view.getTop(), view.getRight(), view.getBottom()));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:137`
  `map2.put("initial_delay", new e.a("initial_delay", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:138`
  `map2.put("interval_duration", new e.a("interval_duration", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:139`
  `map2.put("flex_duration", new e.a("flex_duration", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:140`
  `map2.put("run_attempt_count", new e.a("run_attempt_count", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:141`
  `map2.put("backoff_policy", new e.a("backoff_policy", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:142`
  `map2.put("backoff_delay_duration", new e.a("backoff_delay_duration", "INTEGER", true, 0, null, 1));`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:143`
  `map2.put("last_enqueue_time", new e.a("last_enqueue_time", "INTEGER", true, 0, "-1", 1));`
- `sources/G4/c.java:46`
  `return new JSONObject(str);`
- `sources/G4/c.java:88`
  `JSONObject g(D4.c cVar) {`
- `sources/G4/m.java:25`
  `public d a(InterfaceC4860C interfaceC4860C, JSONObject jSONObject) {`
- `sources/G4/m.java:26`
  `int iOptInt = jSONObject.optInt("settings_version", 0);`
- `sources/G4/m.java:27`
  `int iOptInt2 = jSONObject.optInt("cache_duration", 3600);`
- `sources/G4/m.java:28`
  `return new d(d(interfaceC4860C, iOptInt2, jSONObject), jSONObject.has("session") ? c(jSONObject.getJSONObject("session")) : c(new JSONObject()), b(jSONObject.getJSONObject("features")), iOptInt, iOptInt2, jSONObject.optDouble("on_demand_upload_rate_per_minute", 10.0d), jSONObject.optDouble("on_deman...`
- `sources/h/n.java:23`
  `map2.put((p0) entry.getKey(), matrix);`
- `sources/I3/M.java:277`
  `contentValues.put("next_request_ms", Long.valueOf(j9));`
- `sources/I3/M.java:279`
  `contentValues.put("backend_name", pVar.b());`
- `sources/I3/M.java:280`
  `contentValues.put("priority", Integer.valueOf(AbstractC3746a.a(pVar.d())));`
- `sources/I3/M.java:385`
  `contentValues.put("extras", Base64.encodeToString(pVar.c(), 0));`
- `sources/I3/M.java:405`
  `contentValues.put("context_id", Long.valueOf(jK1));`
- `sources/I3/M.java:406`
  `contentValues.put("transport_name", iVar.n());`
- `sources/I3/M.java:407`
  `contentValues.put("timestamp_ms", Long.valueOf(iVar.f()));`
- `sources/I3/M.java:408`
  `contentValues.put("uptime_ms", Long.valueOf(iVar.o()));`
- `sources/I3/M.java:409`
  `contentValues.put("payload_encoding", iVar.e().b().a());`
- `sources/I3/M.java:410`
  `contentValues.put("code", iVar.d());`
- `sources/I3/M.java:411`
  `contentValues.put("num_attempts", (Integer) 0);`
- `sources/I3/M.java:412`
  `contentValues.put("inline", Boolean.valueOf(z9));`
- `sources/I3/M.java:413`
  `contentValues.put("payload", z9 ? bArrA : new byte[0]);`
- `sources/I3/M.java:414`
  `contentValues.put("product_id", iVar.l());`
- `sources/J5/K.java:156`
  `map.put(D6.G.c(D6.G.g(123)), "Hanlynn Technologies");`
- `sources/J5/K.java:157`
  `map.put(D6.G.c(D6.G.g(124)), "A & R Cambridge");`
- `sources/J5/K.java:158`
  `map.put(D6.G.c(D6.G.g(125)), "Seers Technology Co., Ltd.");`
- `sources/J5/K.java:159`
  `map.put(D6.G.c(D6.G.g(126)), "Sports Tracking Technologies Ltd.");`
- `sources/J5/K.java:160`
  `map.put(D6.G.c(D6.G.g(ModuleDescriptor.MODULE_VERSION)), "Autonet Mobile");`
- `sources/J5/K.java:161`
  `map.put(D6.G.c(D6.G.g(128)), "DeLorme Publishing Company, Inc.");`
- `sources/J5/K.java:162`
  `map.put(D6.G.c(D6.G.g(129)), "WuXi Vimicro");`
- `sources/J5/K.java:260`
  `map.put(D6.G.c(D6.G.g(227)), "inMusic Brands, Inc");`

## BR020

paper_id: B012
paper_title: Reviewing the data security and privacy policies of mobile apps for depression

- `sources/androidx/work/impl/C2370j.java:21`
  `gVar.x(AbstractC3720m.e("UPDATE WorkSpec\n                SET input_merger_class_name = '" + OverwritingInputMerger.class.getName() + "'\n                WHERE input_merger_class_name IS NULL\n                "));`
- `sources/androidx/work/impl/C2370j.java:22`
  `gVar.x("CREATE TABLE IF NOT EXISTS '_new_WorkSpec' (\n                'id' TEXT NOT NULL,\n                'state' INTEGER NOT NULL,\n                'worker_class_name' TEXT NOT NULL,\n                'input_merger_class_name' TEXT NOT NULL,\n                'input' BLOB NOT NULL,\n                ...`
- `sources/androidx/work/impl/C2370j.java:23`
  `gVar.x("INSERT INTO '_new_WorkSpec' (\n            'id',\n            'state',\n            'worker_class_name',\n            'input_merger_class_name',\n            'input',\n            'output',\n            'initial_delay',\n            'interval_duration',\n            'flex_duration',\n       ...`
- `sources/androidx/work/impl/H.java:11`
  `gVar.x("CREATE TABLE IF NOT EXISTS '_new_WorkSpec' ('id' TEXT NOT NULL, 'state' INTEGER NOT NULL, 'worker_class_name' TEXT NOT NULL, 'input_merger_class_name' TEXT, 'input' BLOB NOT NULL, 'output' BLOB NOT NULL, 'initial_delay' INTEGER NOT NULL, 'interval_duration' INTEGER NOT NULL, 'flex_duration' ...`
- `sources/androidx/work/impl/H.java:12`
  `gVar.x("INSERT INTO '_new_WorkSpec' ('id','state','worker_class_name','input_merger_class_name','input','output','initial_delay','interval_duration','flex_duration','run_attempt_count','backoff_policy','backoff_delay_duration','period_start_time','minimum_retention_duration','schedule_requested_at',...`
- `sources/androidx/work/impl/I.java:16`
  `gVar.x("CREATE TABLE IF NOT EXISTS '_new_WorkSpec' ('id' TEXT NOT NULL, 'state' INTEGER NOT NULL, 'worker_class_name' TEXT NOT NULL, 'input_merger_class_name' TEXT, 'input' BLOB NOT NULL, 'output' BLOB NOT NULL, 'initial_delay' INTEGER NOT NULL, 'interval_duration' INTEGER NOT NULL, 'flex_duration' ...`
- `sources/androidx/work/impl/I.java:17`
  `gVar.x("INSERT INTO '_new_WorkSpec' ('id','state','worker_class_name','input_merger_class_name','input','output','initial_delay','interval_duration','flex_duration','run_attempt_count','backoff_policy','backoff_delay_duration','last_enqueue_time','minimum_retention_duration','schedule_requested_at',...`
- `sources/androidx/work/impl/J.java:11`
  `gVar.x("CREATE TABLE IF NOT EXISTS '_new_WorkSpec' ('id' TEXT NOT NULL, 'state' INTEGER NOT NULL, 'worker_class_name' TEXT NOT NULL, 'input_merger_class_name' TEXT NOT NULL, 'input' BLOB NOT NULL, 'output' BLOB NOT NULL, 'initial_delay' INTEGER NOT NULL, 'interval_duration' INTEGER NOT NULL, 'flex_d...`
- `sources/androidx/work/impl/J.java:12`
  `gVar.x("INSERT INTO '_new_WorkSpec' ('id','state','worker_class_name','input_merger_class_name','input','output','initial_delay','interval_duration','flex_duration','run_attempt_count','backoff_policy','backoff_delay_duration','last_enqueue_time','minimum_retention_duration','schedule_requested_at',...`
- `sources/androidx/work/impl/M.java:16`
  `gVar.x("CREATE TABLE IF NOT EXISTS '_new_WorkSpec' ('id' TEXT NOT NULL, 'state' INTEGER NOT NULL, 'worker_class_name' TEXT NOT NULL, 'input_merger_class_name' TEXT NOT NULL, 'input' BLOB NOT NULL, 'output' BLOB NOT NULL, 'initial_delay' INTEGER NOT NULL, 'interval_duration' INTEGER NOT NULL, 'flex_d...`
- `sources/androidx/work/impl/M.java:17`
  `gVar.x("INSERT INTO '_new_WorkSpec' ('id','state','worker_class_name','input_merger_class_name','input','output','initial_delay','interval_duration','flex_duration','run_attempt_count','backoff_policy','backoff_delay_duration','last_enqueue_time','minimum_retention_duration','schedule_requested_at',...`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:48`
  `gVar.x("CREATE TABLE IF NOT EXISTS 'Dependency' ('work_spec_id' TEXT NOT NULL, 'prerequisite_id' TEXT NOT NULL, PRIMARY KEY('work_spec_id', 'prerequisite_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE , FOREIGN KEY('prerequisite_id') REFERENCES 'Wor...`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:51`
  `gVar.x("CREATE TABLE IF NOT EXISTS 'WorkSpec' ('id' TEXT NOT NULL, 'state' INTEGER NOT NULL, 'worker_class_name' TEXT NOT NULL, 'input_merger_class_name' TEXT NOT NULL, 'input' BLOB NOT NULL, 'output' BLOB NOT NULL, 'initial_delay' INTEGER NOT NULL, 'interval_duration' INTEGER NOT NULL, 'flex_durati...`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:54`
  `gVar.x("CREATE TABLE IF NOT EXISTS 'WorkTag' ('tag' TEXT NOT NULL, 'work_spec_id' TEXT NOT NULL, PRIMARY KEY('tag', 'work_spec_id'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/androidx/work/impl/WorkDatabase_Impl.java:56`
  `gVar.x("CREATE TABLE IF NOT EXISTS 'SystemIdInfo' ('work_spec_id' TEXT NOT NULL, 'generation' INTEGER NOT NULL DEFAULT 0, 'system_id' INTEGER NOT NULL, PRIMARY KEY('work_spec_id', 'generation'), FOREIGN KEY('work_spec_id') REFERENCES 'WorkSpec'('id') ON UPDATE CASCADE ON DELETE CASCADE )");`
- `sources/com/punchthrough/lightblueexplorer/R.java:2817`
  `public static final int material_cursor_inset = 0x7f070236;`
- `sources/D2/C1153d.java:735`
  `@Override // android.database.Cursor`
- `sources/D2/C1153d.java:740`
  `@Override // android.database.Cursor`
- `sources/D2/o.java:593`
  `String str3 = "CREATE TEMP TRIGGER IF NOT EXISTS " + f3455q.b(str, str2) + " AFTER " + str2 + " ON '" + str + "' BEGIN UPDATE room_table_modification_log SET invalidated = 1 WHERE table_id = " + i9 + " AND invalidated = 0; END";`
- `sources/D2/o.java:706`
  `this.f3465i = gVar.D("UPDATE room_table_modification_log SET invalidated = 0 WHERE invalidated = 1");`
- `sources/I3/M.java:162`
  `return M.O(this.f34971a, (Cursor) obj);`
- `sources/I3/M.java:225`
  `return M.H(this.f34976a, (Cursor) obj);`
- `sources/I3/M.java:286`
  `public static /* synthetic */ byte[] b0(Cursor cursor) {`
- `sources/I3/M.java:341`
  `return M.q((Cursor) obj);`
- `sources/I3/M.java:390`
  `public static /* synthetic */ C3088f l(long j9, Cursor cursor) {`
- `sources/I3/M.java:391`
  `cursor.moveToNext();`
- `sources/I3/M.java:392`
  `return C3088f.c().c(cursor.getLong(0)).b(j9).a();`
- `sources/I3/M.java:508`
  `return M.q0((Cursor) obj);`
- `sources/I3/M.java:545`
  `return M.J0(this.f34977a, arrayList, pVar, (Cursor) obj);`
- `sources/I3/M.java:607`
  `return M.X0((Cursor) obj);`
- `sources/I3/M.java:650`
  `final String str = "UPDATE events SET num_attempts = num_attempts + 1 WHERE _id in " + C1(iterable);`
- `sources/I3/W.java:136`
  `sQLiteDatabase.execSQL("CREATE TABLE events (_id INTEGER PRIMARY KEY, context_id INTEGER NOT NULL, transport_name TEXT NOT NULL, timestamp_ms INTEGER NOT NULL, uptime_ms INTEGER NOT NULL, payload BLOB NOT NULL, code INTEGER, num_attempts INTEGER NOT NULL,FOREIGN KEY (context_id) REFERENCES transport...`
- `sources/I3/W.java:137`
  `sQLiteDatabase.execSQL("CREATE TABLE event_metadata (_id INTEGER PRIMARY KEY, event_id INTEGER NOT NULL, name TEXT NOT NULL, value TEXT NOT NULL,FOREIGN KEY (event_id) REFERENCES events(_id) ON DELETE CASCADE)");`
- `sources/I3/W.java:138`
  `sQLiteDatabase.execSQL("CREATE TABLE transport_contexts (_id INTEGER PRIMARY KEY, backend_name TEXT NOT NULL, priority INTEGER NOT NULL, next_request_ms INTEGER NOT NULL)");`
- `sources/I3/W.java:139`
  `sQLiteDatabase.execSQL("CREATE INDEX events_backend_id on events(context_id)");`
- `sources/I3/W.java:140`
  `sQLiteDatabase.execSQL("CREATE UNIQUE INDEX contexts_backend_priority on transport_contexts(backend_name, priority)");`
- `sources/I3/W.java:144`
  `sQLiteDatabase.execSQL("ALTER TABLE events ADD COLUMN pseudonymous_id TEXT");`
- `sources/I3/W.java:145`
  `sQLiteDatabase.execSQL("ALTER TABLE events ADD COLUMN experiment_ids_clear_blob BLOB");`
- `sources/I3/W.java:153`
  `sQLiteDatabase.execSQL("CREATE TABLE global_log_event_state (last_metrics_upload_ms BIGINT PRIMARY KEY)");`
- `sources/I3/W.java:154`
  `sQLiteDatabase.execSQL(f34934y);`

## BR021

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:119`
  `<provider`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:150`
  `<provider`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:207`
  `<provider`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:217`
  `<provider`

## BR022

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `resources/com.punchthrough.lightblueexplorer.apk/res/xml/image_share_filepaths.xml:3`
  `<files-path`
- `resources/com.punchthrough.lightblueexplorer.apk/res/xml/provider_paths.xml:3`
  `<files-path`

## BR023

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `sources/androidx/startup/InitializationProvider.java:11`
  `public class InitializationProvider extends ContentProvider {`
- `sources/com/google/firebase/provider/FirebaseInitProvider.java:16`
  `public class FirebaseInitProvider extends ContentProvider {`
- `sources/com/google/mlkit/common/internal/MlKitInitProvider.java:14`
  `public class MlKitInitProvider extends ContentProvider {`

## BR024

paper_id: B024
paper_title: Detecting Passive Content Leaks and Pollution in Android Applications

- `sources/androidx/core/content/FileProvider.java:297`
  `if (!providerInfo.grantUriPermissions) {`

## BR025

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/com/google/android/gms/measurement/internal/C2922f2.java:203`
  `SQLiteDatabase sQLiteDatabaseI = I();`
- `sources/com/google/android/gms/measurement/internal/C2922f2.java:235`
  `sQLiteDatabaseI.beginTransaction();`
- `sources/com/google/android/gms/measurement/internal/C2922f2.java:236`
  `sQLiteDatabaseI.delete("messages", "type == ?", new String[]{Integer.toString(3)});`
- `sources/com/google/android/gms/measurement/internal/C2922f2.java:237`
  `sQLiteDatabaseI.setTransactionSuccessful();`
- `sources/com/google/android/gms/measurement/internal/C2922f2.java:238`
  `sQLiteDatabaseI.endTransaction();`
- `sources/com/google/android/gms/measurement/internal/C2922f2.java:239`
  `sQLiteDatabaseI.close();`
- `sources/com/google/android/gms/measurement/internal/C2922f2.java:241`
  `} catch (SQLiteDatabaseLockedException unused) {`
- `sources/com/google/android/gms/measurement/internal/C2922f2.java:245`
  `sQLiteDatabase.close();`
- `sources/com/google/android/gms/measurement/internal/C2922f2.java:250`
  `if (sQLiteDatabase.inTransaction()) {`
- `sources/com/google/android/gms/measurement/internal/H5.java:1484`
  `SQLiteDatabase sQLiteDatabaseZ = c2954kJ0.z();`
- `sources/com/google/android/gms/measurement/internal/H5.java:1486`
  `int iDelete = sQLiteDatabaseZ.delete("apps", "app_id=?", strArr) + sQLiteDatabaseZ.delete("events", "app_id=?", strArr) + sQLiteDatabaseZ.delete("events_snapshot", "app_id=?", strArr) + sQLiteDatabaseZ.delete("user_attributes", "app_id=?", strArr) + sQLiteDatabaseZ.delete("conditional_properties", "...`
- `sources/com/google/android/gms/measurement/internal/r.java:50`
  `@Override // android.database.sqlite.SQLiteOpenHelper`
- `sources/com/google/android/gms/measurement/internal/r.java:51`
  `public final void onDowngrade(SQLiteDatabase sQLiteDatabase, int i9, int i10) {`
- `sources/com/google/android/gms/measurement/internal/r.java:54`
  `@Override // android.database.sqlite.SQLiteOpenHelper`
- `sources/com/google/android/gms/measurement/internal/r.java:55`
  `public final void onOpen(SQLiteDatabase sQLiteDatabase) {`
- `sources/com/google/android/gms/measurement/internal/r.java:56`
  `AbstractC3023u.c(this.f29165w.h(), sQLiteDatabase, "events", "CREATE TABLE IF NOT EXISTS events ( app_id TEXT NOT NULL, name TEXT NOT NULL, lifetime_count INTEGER NOT NULL, current_bundle_count INTEGER NOT NULL, last_fire_timestamp INTEGER NOT NULL, PRIMARY KEY (app_id, name)) ;", "app_id,name,lifet...`
- `sources/com/google/android/gms/measurement/internal/r.java:57`
  `AbstractC3023u.c(this.f29165w.h(), sQLiteDatabase, "events_snapshot", "CREATE TABLE IF NOT EXISTS events_snapshot ( app_id TEXT NOT NULL, name TEXT NOT NULL, lifetime_count INTEGER NOT NULL, current_bundle_count INTEGER NOT NULL, last_fire_timestamp INTEGER NOT NULL, last_bundled_timestamp INTEGER, ...`
- `sources/com/google/android/gms/measurement/internal/r.java:58`
  `AbstractC3023u.c(this.f29165w.h(), sQLiteDatabase, "conditional_properties", "CREATE TABLE IF NOT EXISTS conditional_properties ( app_id TEXT NOT NULL, origin TEXT NOT NULL, name TEXT NOT NULL, value BLOB NOT NULL, creation_timestamp INTEGER NOT NULL, active INTEGER NOT NULL, trigger_event_name TEXT...`
- `sources/com/google/android/gms/measurement/internal/r.java:59`
  `AbstractC3023u.c(this.f29165w.h(), sQLiteDatabase, "user_attributes", "CREATE TABLE IF NOT EXISTS user_attributes ( app_id TEXT NOT NULL, name TEXT NOT NULL, set_timestamp INTEGER NOT NULL, value BLOB NOT NULL, PRIMARY KEY (app_id, name)) ;", "app_id,name,set_timestamp,value", C2954k.f29032g);`
- `sources/com/google/android/gms/measurement/internal/r.java:60`
  `AbstractC3023u.c(this.f29165w.h(), sQLiteDatabase, "apps", "CREATE TABLE IF NOT EXISTS apps ( app_id TEXT NOT NULL, app_instance_id TEXT, gmp_app_id TEXT, resettable_device_id_hash TEXT, last_bundle_index INTEGER NOT NULL, last_bundle_end_timestamp INTEGER NOT NULL, PRIMARY KEY (app_id)) ;", "app_id...`
- `sources/com/google/android/gms/measurement/internal/r.java:61`
  `AbstractC3023u.c(this.f29165w.h(), sQLiteDatabase, "queue", "CREATE TABLE IF NOT EXISTS queue ( app_id TEXT NOT NULL, bundle_end_timestamp INTEGER NOT NULL, data BLOB NOT NULL);", "app_id,bundle_end_timestamp,data", C2954k.f29035j);`
- `sources/com/google/android/gms/measurement/internal/r.java:62`
  `AbstractC3023u.c(this.f29165w.h(), sQLiteDatabase, "raw_events_metadata", "CREATE TABLE IF NOT EXISTS raw_events_metadata ( app_id TEXT NOT NULL, metadata_fingerprint INTEGER NOT NULL, metadata BLOB NOT NULL, PRIMARY KEY (app_id, metadata_fingerprint));", "app_id,metadata_fingerprint,metadata", null...`
- `sources/com/google/android/gms/measurement/internal/r.java:63`
  `AbstractC3023u.c(this.f29165w.h(), sQLiteDatabase, "raw_events", "CREATE TABLE IF NOT EXISTS raw_events ( app_id TEXT NOT NULL, name TEXT NOT NULL, timestamp INTEGER NOT NULL, metadata_fingerprint INTEGER NOT NULL, data BLOB NOT NULL);", "app_id,name,timestamp,metadata_fingerprint,data", C2954k.f290...`
- `sources/com/google/android/gms/measurement/internal/r.java:64`
  `AbstractC3023u.c(this.f29165w.h(), sQLiteDatabase, "event_filters", "CREATE TABLE IF NOT EXISTS event_filters ( app_id TEXT NOT NULL, audience_id INTEGER NOT NULL, filter_id INTEGER NOT NULL, event_name TEXT NOT NULL, data BLOB NOT NULL, PRIMARY KEY (app_id, event_name, audience_id, filter_id));", "...`
- `sources/com/google/android/gms/measurement/internal/r.java:65`
  `AbstractC3023u.c(this.f29165w.h(), sQLiteDatabase, "property_filters", "CREATE TABLE IF NOT EXISTS property_filters ( app_id TEXT NOT NULL, audience_id INTEGER NOT NULL, filter_id INTEGER NOT NULL, property_name TEXT NOT NULL, data BLOB NOT NULL, PRIMARY KEY (app_id, property_name, audience_id, filt...`
- `sources/com/google/android/gms/measurement/internal/r.java:66`
  `AbstractC3023u.c(this.f29165w.h(), sQLiteDatabase, "audience_filter_values", "CREATE TABLE IF NOT EXISTS audience_filter_values ( app_id TEXT NOT NULL, audience_id INTEGER NOT NULL, current_results BLOB, PRIMARY KEY (app_id, audience_id));", "app_id,audience_id,current_results", null);`
- `sources/com/google/android/gms/measurement/internal/r.java:67`
  `AbstractC3023u.c(this.f29165w.h(), sQLiteDatabase, "app2", "CREATE TABLE IF NOT EXISTS app2 ( app_id TEXT NOT NULL, first_open_count INTEGER NOT NULL, PRIMARY KEY (app_id));", "app_id,first_open_count", C2954k.f29038m);`
- `sources/I3/M.java:89`
  `} catch (SQLiteDatabaseLockedException e9) {`
- `sources/I3/M.java:98`
  `public static /* synthetic */ Object B0(String str, C3085c.b bVar, long j9, SQLiteDatabase sQLiteDatabase) {`
- `sources/I3/M.java:99`
  `if (((Boolean) D1(sQLiteDatabase.rawQuery("SELECT 1 FROM log_event_dropped WHERE log_source = ? AND reason = ?", new String[]{str, Integer.toString(bVar.a())}), new b() { // from class: i3.y`
- `sources/I3/M.java:156`
  `public static /* synthetic */ Integer F0(final M m9, long j9, SQLiteDatabase sQLiteDatabase) {`
- `sources/I3/M.java:159`
  `D1(sQLiteDatabase.rawQuery("SELECT COUNT(*), transport_name FROM events WHERE timestamp_ms < ? GROUP BY transport_name", strArr), new b() { // from class: i3.r`
- `sources/I3/M.java:165`
  `return Integer.valueOf(sQLiteDatabase.delete("events", "timestamp_ms < ?", strArr));`
- `sources/I3/M.java:221`
  `sQLiteDatabase.compileStatement(str).execute();`
- `sources/I3/M.java:222`
  `D1(sQLiteDatabase.rawQuery(str2, null), new b() { // from class: i3.u`
- `sources/I3/M.java:228`
  `sQLiteDatabase.compileStatement("DELETE FROM events WHERE num_attempts >= 16").execute();`
- `sources/I3/M.java:232`
  `public static /* synthetic */ Object R0(M m9, SQLiteDatabase sQLiteDatabase) {`
- `sources/I3/M.java:234`
  `sQLiteDatabase.compileStatement("DELETE FROM log_event_dropped").execute();`
- `sources/I3/M.java:235`
  `sQLiteDatabase.compileStatement("UPDATE global_log_event_state SET last_metrics_upload_ms=" + m9.f34916x.a()).execute();`
- `sources/I3/M.java:275`
  `public static /* synthetic */ Object a0(long j9, a3.p pVar, SQLiteDatabase sQLiteDatabase) {`

## BR026

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/A5/f.java:53`
  `Log.w("SessionsSettings", "CorruptionException in settings DataStore in " + v.f15297a.e() + '.', c3118c);`
- `sources/androidx/datastore/preferences/protobuf/AbstractC2283c.java:1`
  `package androidx.datastore.preferences.protobuf;`
- `sources/androidx/datastore/preferences/protobuf/AbstractC2283c.java:3`
  `import androidx.datastore.preferences.protobuf.AbstractC2304y;`
- `sources/androidx/datastore/preferences/protobuf/AbstractC2283c.java:9`
  `/* JADX INFO: renamed from: androidx.datastore.preferences.protobuf.c, reason: case insensitive filesystem */`
- `sources/androidx/datastore/preferences/protobuf/AbstractC2285e.java:1`
  `package androidx.datastore.preferences.protobuf;`
- `sources/androidx/datastore/preferences/protobuf/AbstractC2285e.java:3`
  `import androidx.datastore.preferences.protobuf.AbstractC2304y;`
- `sources/androidx/datastore/preferences/protobuf/AbstractC2285e.java:6`
  `/* JADX INFO: renamed from: androidx.datastore.preferences.protobuf.e, reason: case insensitive filesystem */`
- `sources/androidx/datastore/preferences/protobuf/AbstractC2292l.java:1`
  `package androidx.datastore.preferences.protobuf;`
- `sources/androidx/datastore/preferences/protobuf/AbstractC2292l.java:3`
  `import androidx.datastore.preferences.protobuf.AbstractC2304y;`
- `sources/androidx/datastore/preferences/protobuf/AbstractC2292l.java:6`
  `/* JADX INFO: renamed from: androidx.datastore.preferences.protobuf.l, reason: case insensitive filesystem */`
- `sources/androidx/datastore/preferences/protobuf/AbstractC2300u.java:1`
  `package androidx.datastore.preferences.protobuf;`
- `sources/androidx/datastore/preferences/protobuf/AbstractC2300u.java:3`
  `import androidx.datastore.preferences.protobuf.AbstractC2304y;`
- `sources/androidx/datastore/preferences/protobuf/AbstractC2300u.java:6`
  `/* JADX INFO: renamed from: androidx.datastore.preferences.protobuf.u, reason: case insensitive filesystem */`
- `sources/androidx/datastore/preferences/protobuf/AbstractC2303x.java:1`
  `package androidx.datastore.preferences.protobuf;`
- `sources/androidx/datastore/preferences/protobuf/AbstractC2303x.java:3`
  `import androidx.datastore.preferences.protobuf.AbstractC2304y;`
- `sources/androidx/datastore/preferences/protobuf/AbstractC2303x.java:6`
  `/* JADX INFO: renamed from: androidx.datastore.preferences.protobuf.x, reason: case insensitive filesystem */`
- `sources/androidx/datastore/preferences/protobuf/AbstractC2304y.java:1`
  `package androidx.datastore.preferences.protobuf;`
- `sources/androidx/datastore/preferences/protobuf/AbstractC2304y.java:8`
  `/* JADX INFO: renamed from: androidx.datastore.preferences.protobuf.y, reason: case insensitive filesystem */`
- `sources/androidx/datastore/preferences/protobuf/AbstractC2304y.java:30`
  `/* JADX INFO: renamed from: androidx.datastore.preferences.protobuf.y$a */`
- `sources/androidx/datastore/preferences/protobuf/AbstractC2304y.java:35`
  `/* JADX INFO: renamed from: androidx.datastore.preferences.protobuf.y$b */`
- `sources/androidx/datastore/preferences/protobuf/b0.java:1`
  `package androidx.datastore.preferences.protobuf;`
- `sources/androidx/datastore/preferences/protobuf/C2289i.java:254`
  `@Override // androidx.datastore.preferences.protobuf.d0`
- `sources/androidx/datastore/preferences/protobuf/C2289i.java:358`
  `@Override // androidx.datastore.preferences.protobuf.d0`
- `sources/androidx/datastore/preferences/protobuf/C2289i.java:430`
  `@Override // androidx.datastore.preferences.protobuf.d0`
- `sources/androidx/datastore/preferences/protobuf/C2289i.java:507`
  `@Override // androidx.datastore.preferences.protobuf.d0`
- `sources/androidx/datastore/preferences/protobuf/C2289i.java:560`
  `@Override // androidx.datastore.preferences.protobuf.d0`
- `sources/androidx/datastore/preferences/protobuf/C2289i.java:602`
  `@Override // androidx.datastore.preferences.protobuf.d0`
- `sources/androidx/datastore/preferences/protobuf/C2289i.java:643`
  `@Override // androidx.datastore.preferences.protobuf.d0`
- `sources/androidx/datastore/preferences/protobuf/C2289i.java:702`
  `@Override // androidx.datastore.preferences.protobuf.d0`
- `sources/androidx/datastore/preferences/protobuf/C2289i.java:755`
  `@Override // androidx.datastore.preferences.protobuf.d0`
- `sources/androidx/datastore/preferences/protobuf/C2289i.java:796`
  `@Override // androidx.datastore.preferences.protobuf.d0`
- `sources/androidx/datastore/preferences/protobuf/C2289i.java:844`
  `@Override // androidx.datastore.preferences.protobuf.d0`
- `sources/androidx/datastore/preferences/protobuf/C2289i.java:885`
  `@Override // androidx.datastore.preferences.protobuf.d0`
- `sources/androidx/datastore/preferences/protobuf/C2289i.java:1026`
  `@Override // androidx.datastore.preferences.protobuf.d0`
- `sources/androidx/datastore/preferences/protobuf/C2289i.java:1080`
  `@Override // androidx.datastore.preferences.protobuf.d0`
- `sources/androidx/datastore/preferences/protobuf/C2297q.java:11`
  `@Override // androidx.datastore.preferences.protobuf.AbstractC2296p`
- `sources/androidx/datastore/preferences/protobuf/C2297q.java:17`
  `@Override // androidx.datastore.preferences.protobuf.AbstractC2296p`
- `sources/androidx/datastore/preferences/protobuf/C2297q.java:23`
  `@Override // androidx.datastore.preferences.protobuf.AbstractC2296p`
- `sources/androidx/datastore/preferences/protobuf/C2297q.java:29`
  `@Override // androidx.datastore.preferences.protobuf.AbstractC2296p`
- `sources/androidx/datastore/preferences/protobuf/C2297q.java:35`
  `@Override // androidx.datastore.preferences.protobuf.AbstractC2296p`

## BR027

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/androidx/core/graphics/drawable/IconCompat.java:325`
  `return new FileInputStream(new File((String) this.f22377b));`
- `sources/androidx/profileinstaller/h.java:179`
  `String name = new File(applicationInfo.sourceDir).getName();`
- `sources/androidx/work/impl/F.java:19`
  `return new File(C2361a.f24862a.a(context), "androidx.work.workdb");`
- `sources/com/google/android/gms/internal/measurement/C2584f3.java:123`
  `File file = new File(context.getDir("phenotype_hermetic", 0), "overrides.txt");`
- `sources/com/google/android/gms/measurement/internal/AbstractC3023u.java:31`
  `File file = new File(AbstractC2626k0.a().g(sQLiteDatabase.getPath()));`
- `sources/com/google/android/gms/measurement/internal/H5.java:533`
  `FileChannel channel = new RandomAccessFile(new File(AbstractC2626k0.a().b(this.f28513l.zza().getFilesDir(), "google_app_measurement.db")), "rw").getChannel();`
- `sources/e4/g.java:47`
  `File fileS = s(new File(filesDir, str));`
- `sources/e4/g.java:49`
  `this.f3859d = s(new File(fileS, "open-sessions"));`
- `sources/e4/g.java:50`
  `this.f3860e = s(new File(fileS, "reports"));`
- `sources/e4/g.java:51`
  `this.f3861f = s(new File(fileS, "priority-reports"));`
- `sources/e4/g.java:52`
  `this.f3862g = s(new File(fileS, "native-reports"));`
- `sources/e4/g.java:56`
  `File file = new File(this.f3857b, str);`
- `sources/H2/h.java:67`
  `H2.b.a(new File(str));`

## BR029

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:65`
  `android:exported="true">`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:76`
  `android:exported="true"`

## BR030

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:243`
  `android:exported="true"`

## BR031

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:318`
  `android:exported="true"`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:344`
  `android:exported="true"`

## BR033

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/com/punchthrough/lightblueexplorer/MicrochipReferencesActivity.java:76`
  `intent.setData(Uri.parse(((S) item).c()));`
- `sources/com/punchthrough/lightblueexplorer/ui/launch/LaunchActivity.java:119`
  `intent.setData(Uri.parse("package:" + this.f30967x.getPackageName()));`

## BR034

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/com/google/android/gms/measurement/internal/H5.java:411`
  `this.f28513l.zza().sendBroadcast(intent);`
- `sources/com/punchthrough/lightblueexplorer/MicrochipReferencesActivity.java:77`
  `microchipReferencesActivity.startActivity(intent);`
- `sources/com/punchthrough/lightblueexplorer/ui/launch/LaunchActivity.java:121`
  `launchActivity.startActivity(intent);`
- `sources/o5/AbstractC4032l.java:219`
  `context.sendBroadcast(intent);`

## BR035

paper_id: B026
paper_title: Measuring the Insecurity of Mobile Deep Links of Android

- `sources/L6/C3758b.java:57`
  `webView.loadUrl(this.f36760a);`

## BR040

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `sources/C3/a.java:14`
  `private final String f2902c = "com.google.android.gms.ads.identifier.internal.IAdvertisingIdService";`
- `sources/C3/d.java:9`
  `super(iBinder, "com.google.android.gms.ads.identifier.internal.IAdvertisingIdService");`
- `sources/C3/e.java:12`
  `IInterface iInterfaceQueryLocalInterface = iBinder.queryLocalInterface("com.google.android.gms.ads.identifier.internal.IAdvertisingIdService");`
- `sources/k6/C3619B.java:416`
  `public void onCharacteristicReadRequest(BluetoothDevice bluetoothDevice, int i9, int i10, BluetoothGattCharacteristic bluetoothGattCharacteristic) {`
- `sources/k6/C3619B.java:496`
  `public void onDescriptorReadRequest(BluetoothDevice bluetoothDevice, int i9, int i10, BluetoothGattDescriptor bluetoothGattDescriptor) {`
- `sources/m3/C3844a.java:196`
  `Intent intent = new Intent("com.google.android.gms.ads.identifier.service.START");`

## BR041

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:176`
  `android:name="com.google.firebase.components:com.google.firebase.analytics.connector.internal.AnalyticsConnectorRegistrar"`
- `sources/com/google/android/gms/internal/measurement/C2573e1.java:214`
  `Class.forName("com.google.firebase.analytics.FirebaseAnalytics", false, getClass().getClassLoader());`
- `sources/com/google/android/gms/measurement/AppMeasurement.java:10`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/com/google/android/gms/measurement/internal/C2929g2.java:76`
  `Class<?> clsLoadClass = zza().getClassLoader().loadClass("com.google.firebase.analytics.FirebaseAnalytics");`
- `sources/com/google/firebase/analytics/a.java:1`
  `package com.google.firebase.analytics;`
- `sources/com/google/firebase/analytics/FirebaseAnalytics.java:1`
  `package com.google.firebase.analytics;`
- `sources/com/google/firebase/analytics/connector/internal/a.java:1`
  `package com.google.firebase.analytics.connector.internal;`
- `sources/com/google/firebase/analytics/connector/internal/AnalyticsConnectorRegistrar.java:1`
  `package com.google.firebase.analytics.connector.internal;`
- `sources/com/google/firebase/analytics/connector/internal/AnalyticsConnectorRegistrar.java:25`
  `return Arrays.asList(C4326c.c(InterfaceC4173a.class).b(q.i(C4124f.class)).b(q.i(Context.class)).b(q.i(O4.d.class)).e(new g() { // from class: com.google.firebase.analytics.connector.internal.b`
- `sources/com/google/firebase/analytics/connector/internal/c.java:1`
  `package com.google.firebase.analytics.connector.internal;`
- `sources/com/google/firebase/analytics/connector/internal/d.java:1`
  `package com.google.firebase.analytics.connector.internal;`
- `sources/com/google/firebase/analytics/connector/internal/e.java:1`
  `package com.google.firebase.analytics.connector.internal;`
- `sources/com/google/firebase/analytics/connector/internal/f.java:1`
  `package com.google.firebase.analytics.connector.internal;`
- `sources/com/punchthrough/lightblueexplorer/common/App.java:19`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/i5/d.java:5`
  `import com.google.firebase.analytics.FirebaseAnalytics;`
- `sources/i5/d.java:79`
  `com.google.firebase.analytics.FirebaseAnalytics r0 = r3.f7469b`
- `sources/Q4/C4174b.java:6`
  `import com.google.firebase.analytics.connector.internal.f;`
- `sources/Q4/C4174b.java:95`
  `if (com.google.firebase.analytics.connector.internal.a.f(str) && com.google.firebase.analytics.connector.internal.a.c(str2, bundle) && com.google.firebase.analytics.connector.internal.a.d(str, str2, bundle)) {`
- `sources/Q4/C4174b.java:96`
  `com.google.firebase.analytics.connector.internal.a.b(str, str2, bundle);`
- `sources/Q4/C4174b.java:104`
  `if (!com.google.firebase.analytics.connector.internal.a.f(str) || e(str)) {`
- `sources/Q4/C4174b.java:108`
  `Object dVar = "fiam".equals(str) ? new com.google.firebase.analytics.connector.internal.d(aVar, bVar) : "clx".equals(str) ? new f(aVar, bVar) : null;`

## BR042

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:29`
  `<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:44`
  `<uses-permission android:name="android.permission.ACCESS_ADSERVICES_AD_ID"/>`
- `sources/com/google/android/gms/internal/measurement/A6.java:14`
  `c2680q3E.d("measurement.client.ad_id_consent_fix", true);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:180`
  `f26934a = c2680q3E.b("measurement.ad_id_cache_time", 10000L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:181`
  `f26936b = c2680q3E.b("measurement.app_uninstalled_additional_ad_id_cache_time", 3600000L);`
- `sources/com/google/android/gms/measurement/internal/C2954k.java:48`
  `private static final String[] f29033h = {"app_version", "ALTER TABLE apps ADD COLUMN app_version TEXT;", "app_store", "ALTER TABLE apps ADD COLUMN app_store TEXT;", "gmp_version", "ALTER TABLE apps ADD COLUMN gmp_version INTEGER;", "dev_cert_hash", "ALTER TABLE apps ADD COLUMN dev_cert_hash INTEGER;...`
- `sources/com/google/android/gms/measurement/internal/C2954k.java:883`
  `cursorQuery = z().query("apps", new String[]{"app_instance_id", "gmp_app_id", "resettable_device_id_hash", "last_bundle_index", "last_bundle_start_timestamp", "last_bundle_end_timestamp", "app_version", "app_store", "gmp_version", "dev_cert_hash", "measurement_enabled", "day", "daily_public_events_c...`
- `sources/com/google/android/gms/measurement/internal/G.java:395`
  `f28424b = F("measurement.ad_id_cache_time", 10000L, new Z1() { // from class: com.google.android.gms.measurement.internal.H`
- `sources/com/google/android/gms/measurement/internal/G.java:401`
  `f28427c = F("measurement.app_uninstalled_additional_ad_id_cache_time", 3600000L, new Z1() { // from class: com.google.android.gms.measurement.internal.y0`
- `sources/m3/C3844a.java:113`
  `throw new IOException("AdvertisingIdClient is not connected.");`
- `sources/m3/C3844a.java:119`
  `throw new IOException("AdvertisingIdClient cannot reconnect.");`
- `sources/m3/C3844a.java:122`
  `throw new IOException("AdvertisingIdClient cannot reconnect.", e9);`
- `sources/m3/C3844a.java:130`
  `Log.i("AdvertisingIdClient", "GMS remote exception ", e10);`

## BR043

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:56`
  `@Metadata(d1 = {"\u0000Û\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u000b\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0004\n\u0002\u0010\u0012\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u000e\n\u0002\u0010 \n\u0002\u0018\...`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:82`
  `public C1763m scanResult;`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:1503`
  `C1763m c1763m = this.scanResult;`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:1507`
  `AbstractC1838t.t("scanResult");`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:1518`
  `this.scanResult = c1763m;`
- `sources/com/punchthrough/lightblueexplorer/ui/devicedetails/DeviceDetailActivity.java:62`
  `@Metadata(d1 = {"\u0000|\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002...`
- `sources/com/punchthrough/lightblueexplorer/ui/devicedetails/DeviceDetailActivity.java:72`
  `public C1763m scanResult;`
- `sources/com/punchthrough/lightblueexplorer/ui/devicedetails/DeviceDetailActivity.java:1127`
  `C1763m c1763m = this.scanResult;`
- `sources/com/punchthrough/lightblueexplorer/ui/devicedetails/DeviceDetailActivity.java:1131`
  `AbstractC1838t.t("scanResult");`
- `sources/com/punchthrough/lightblueexplorer/ui/devicedetails/DeviceDetailActivity.java:1137`
  `this.scanResult = c1763m;`
- `sources/G6/k.java:837`
  `AbstractC1065p.Q(1739356405, i9, -1, "com.punchthrough.lightblueexplorer.ui.screens.PeripheralsScanResultsSection.<anonymous>.<anonymous> (PeripheralsScreen.kt:401)");`
- `sources/G6/k.java:1544`
  `AbstractC1838t.g(list, "scanResults");`
- `sources/G6/k.java:1550`
  `AbstractC1065p.Q(-1713938452, i9, -1, "com.punchthrough.lightblueexplorer.ui.screens.PeripheralsScanResultsSection (PeripheralsScreen.kt:378)");`
- `sources/G6/k.java:1596`
  `AbstractC1838t.g(list, "scanResults");`
- `sources/H5/a0.java:108`
  `return "Peripheral(name=" + this.f7149a + ", rssi=" + this.f7150b + ", macAddress=" + this.f7151c + ", isStale=" + this.f7152d + ", bluetoothPeripheral=" + this.f7153e + ", scanResult=" + this.f7154f + ")";`
- `sources/H5/b0.java:96`
  `return "PeripheralScanResult(txPower=" + this.f7173a + ", localName=" + this.f7174b + ", advertisingPacketRawBytes=" + this.f7175c + ", advertiseFlagsDescription=" + this.f7176d + ", serviceUuids=" + this.f7177e + ", manufacturerSpecificData=" + this.f7178f + ", serviceData=" + this.f7179g + ")";`
- `sources/H5/c0.java:47`
  `@Metadata(d1 = {"\u0000\u0084\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0...`
- `sources/H5/c0.java:604`
  `super(0, obj, f0.class, "clearScanResultsList", "clearScanResultsList()V", 0);`
- `sources/J5/C1763m.java:122`
  `AbstractC1838t.g(lVar, "scanResult");`
- `sources/J5/N.java:6`
  `super("Cannot start BLE scan because BluetoothLeScanner is not available on this device.");`
- `sources/K5/b.java:17`
  `import android.bluetooth.le.BluetoothLeScanner;`
- `sources/K5/b.java:20`
  `import android.bluetooth.le.ScanResult;`
- `sources/K5/b.java:133`
  `public void onScanResult(int i9, ScanResult scanResult) {`
- `sources/K5/b.java:134`
  `AbstractC1838t.g(scanResult, "result");`
- `sources/K5/b.java:135`
  `C1763m c1763m = new C1763m(new d(scanResult));`
- `sources/K5/b.java:159`
  `private final BluetoothLeScanner y() {`
- `sources/K5/b.java:162`
  `return bluetoothAdapterX.getBluetoothLeScanner();`
- `sources/K5/b.java:197`
  `BluetoothLeScanner bluetoothLeScannerY = y();`
- `sources/K5/b.java:198`
  `if (bluetoothLeScannerY != null) {`
- `sources/K5/b.java:199`
  `bluetoothLeScannerY.stopScan(this.f8330f);`
- `sources/K5/b.java:224`
  `BluetoothLeScanner bluetoothLeScannerY = y();`
- `sources/K5/b.java:225`
  `if (bluetoothLeScannerY != null) {`
- `sources/K5/b.java:227`
  `bluetoothLeScannerY.startScan((List<ScanFilter>) list, scanSettings, this.f8330f);`
- `sources/K5/d.java:8`
  `import android.bluetooth.le.ScanResult;`
- `sources/K5/d.java:17`
  `private final ScanResult f8336w;`
- `sources/K5/d.java:24`
  `return new d((ScanResult) parcel.readParcelable(d.class.getClassLoader()));`
- `sources/K5/d.java:34`
  `public d(ScanResult scanResult) {`
- `sources/K5/d.java:35`
  `AbstractC1838t.g(scanResult, "result");`
- `sources/K5/d.java:36`
  `this.f8336w = scanResult;`

## BR047

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/A/H.java:261`
  `Log.e("ImageCapture", "Failed to acquire latest image.", e9);`
- `sources/androidx/appcompat/app/h.java:1197`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR id when requesting this feature.");`
- `sources/androidx/appcompat/app/h.java:1203`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR_OVERLAY id when requesting this feature.");`
- `sources/androidx/appcompat/app/h.java:2295`
  `Log.i("AppCompatDelegate", "Failed to instantiate custom view inflater " + string + ". Falling back to default.", th);`
- `sources/androidx/appcompat/app/h.java:2617`
  `Log.i("AppCompatDelegate", "The Activity's LayoutInflater already has a Factory installed so we can not install AppCompat's");`
- `sources/androidx/appcompat/app/q.java:206`
  `Log.i("AppCompatViewInflater", "app:theme is now deprecated. Please move to using android:theme instead.");`
- `sources/androidx/appcompat/view/g.java:202`
  `Log.w("SupportMenuInflater", "Cannot instantiate class: " + str, e9);`
- `sources/androidx/appcompat/view/g.java:235`
  `Log.w("SupportMenuInflater", "Ignoring attribute 'itemActionViewLayout'. Action view already specified.");`
- `sources/androidx/appcompat/view/g.java:316`
  `Log.w("SupportMenuInflater", "Ignoring attribute 'actionProviderClass'. Action view already specified.");`
- `sources/androidx/appcompat/widget/X.java:270`
  `Log.e("ResourceManagerInternal", "Exception while inflating drawable", e9);`
- `sources/androidx/compose/ui/focus/FocusOwnerImpl.java:794`
  `System.out.println((Object) "FocusRelatedWarning: Dispatching intercepted soft keyboard event while the focus system is invalidated.");`
- `sources/androidx/constraintlayout/widget/b.java:230`
  `Log.e("TransitionLayout", " Custom Attribute \"" + str + "\" not found on " + cls.getName());`
- `sources/androidx/constraintlayout/widget/b.java:233`
  `Log.e("TransitionLayout", e10.getMessage());`
- `sources/androidx/constraintlayout/widget/b.java:234`
  `Log.e("TransitionLayout", " Custom Attribute \"" + str + "\" not found on " + cls.getName());`
- `sources/androidx/constraintlayout/widget/e.java:891`
  `Log.w("ConstraintSet", "unused attribute 0x" + Integer.toHexString(index) + "   " + f21564r0.get(index));`
- `sources/androidx/constraintlayout/widget/e.java:894`
  `Log.w("ConstraintSet", "Unknown attribute 0x" + Integer.toHexString(index) + "   " + f21564r0.get(index));`
- `sources/androidx/constraintlayout/widget/e.java:2083`
  `Log.w("ConstraintSet", "unused attribute 0x" + Integer.toHexString(index) + "   " + f21537g.get(index));`
- `sources/androidx/constraintlayout/widget/e.java:2089`
  `Log.w("ConstraintSet", "Unknown attribute 0x" + Integer.toHexString(index) + "   " + f21537g.get(index));`
- `sources/androidx/constraintlayout/widget/e.java:2158`
  `Log.w("ConstraintSet", "Unknown attribute 0x" + Integer.toHexString(index) + "   " + f21537g.get(index));`
- `sources/androidx/constraintlayout/widget/e.java:2406`
  `Log.w("ConstraintSet", "unused attribute 0x" + Integer.toHexString(index) + "   " + f21537g.get(index));`
- `sources/androidx/coordinatorlayout/widget/CoordinatorLayout.java:684`
  `Log.e("CoordinatorLayout", "No keylines defined for " + this + " - attempted index lookup " + i9);`
- `sources/androidx/core/content/res/c.java:59`
  `Log.e("CSLCompat", "Failed to inflate ColorStateList.", e9);`
- `sources/androidx/core/content/res/d.java:71`
  `Log.e("ComplexColorCompat", "Failed to inflate ComplexColor.", e9);`
- `sources/androidx/core/content/res/h.java:352`
  `Log.w("ResourcesCompat", "Failed to inflate ColorStateList, leaving it to the framework", e9);`
- `sources/androidx/core/graphics/k.java:75`
  `Log.e("TypefaceCompatUtil", "Error copying resource contents to temp file: " + e.getMessage());`
- `sources/androidx/core/view/C2278y0.java:53`
  `Log.w("WindowInsetsCompat", "Failed to get visible insets from AttachInfo " + e9.getMessage(), e9);`
- `sources/androidx/core/view/C2278y0.java:72`
  `Log.w("WindowInsetsCompat", "Failed to get insets from AttachInfo. " + e9.getMessage(), e9);`
- `sources/androidx/core/view/C2278y0.java:842`
  `Log.e("WindowInsetsCompat", "Failed to get visible insets. (Reflection error). " + e9.getMessage(), e9);`
- `sources/androidx/core/view/C2278y0.java:884`
  `Log.e("WindowInsetsCompat", "Failed to get visible insets. (Reflection error). " + e9.getMessage(), e9);`
- `sources/androidx/fragment/app/A.java:271`
  `Log.d("FragmentManager", "moveto VIEW_CREATED: " + this.f23131c);`
- `sources/androidx/fragment/app/A.java:301`
  `Log.v("FragmentManager", "requestFocus: Saved focused view " + viewFindFocus + " for Fragment " + this.f23131c);`
- `sources/androidx/fragment/app/C2306a.java:248`
  `printWriter.println(Integer.toHexString(this.f23145e));`
- `sources/androidx/fragment/app/C2306a.java:255`
  `printWriter.println(Integer.toHexString(this.f23147g));`
- `sources/androidx/fragment/app/C2306a.java:262`
  `printWriter.println(this.f23153m);`
- `sources/androidx/fragment/app/C2306a.java:269`
  `printWriter.println(this.f23155o);`
- `sources/androidx/fragment/app/C2306a.java:331`
  `printWriter.println(Integer.toHexString(aVar.f23164e));`
- `sources/androidx/fragment/app/C2306a.java:338`
  `printWriter.println(Integer.toHexString(aVar.f23166g));`
- `sources/androidx/fragment/app/C2310e.java:307`
  `Log.v("FragmentManager", "Adding BackProgressCallbacks for Animators to operation " + dVarA);`
- `sources/androidx/fragment/app/C2310e.java:1146`
  `Log.v("FragmentManager", "Ignoring Animation set on " + nVarI2 + " as Animations cannot run alongside Animators.");`
- `sources/androidx/fragment/app/C2310e.java:1149`
  `Log.v("FragmentManager", "Ignoring Animation set on " + nVarI2 + " as Animations cannot run alongside Transitions.");`

## BR050

paper_id: B021
paper_title: Metadata-Based Privacy Assessment for Mobile mHealth

- `audit_reports/lightblue_beginner_audit_report.md:109`
  `- 论文：B010 'Client-Focused Security Assessment of mHealth Apps...'；B019 'Assessment of Privacy Policies of Apps for Core Symptoms of COVID-19'；B008 'Your Signal, Their Data...'`
- `audit_reports/rule_by_rule_mapping.md:44`
  `- BR042 | B008 'Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android' | 'not_supported' | 'BluetoothLeScanner.startScan' 在一方 'K5.b'，不在第三方 SDK namespace。`
- `audit_reports/rule_by_rule_mapping.md:48`
  `- BR050 | B021 'Mobile App Metadata-Based Privacy Assessment' | 'not_testable' | 未能解码/获取 privacy URL 文本并验证可达性。`
- `audit_reports/rule_by_rule_mapping.md:49`
  `- BR051 | B013 'Assessment of Availability, Readability, and Content of Privacy Policies of mHealth Apps' | 'not_testable' | 缺隐私政策正文，无法判断是否遗漏 BLE/location/device data。`
- `audit_reports/rule_by_rule_mapping.md:50`
  `- BR052 | B013 'Assessment of Availability, Readability, and Content of Privacy Policies of mHealth Apps' | 'not_testable' | 缺隐私政策正文，无法判断第三方分享披露。`
- `audit_reports/rule_by_rule_mapping.md:51`
  `- BR055 | B014 'Privacy Assessment in Mobile Health Apps' | 'confirmed' | 本审计提供 file/class/function/rule 证据；该条是报告质量 meta-rule。`
- `audit_reports/rule_by_rule_mapping.md:54`
  `- BR060 | B016 'A privacy and security analysis...' | 'not_supported' | 未见 env/baseUrl/channel flag 可切换 backend。`

## BR051

paper_id: B013
paper_title: Availability and quality of mobile health app privacy policies

- `audit_reports/lightblue_beginner_audit_report.md:75`
  `- B005 'Mobile health and privacy: cross sectional study'：论文将 App 代码中的数据收集操作、App 流量中的数据传输、第三方 recipient、trackers/adverts 与隐私政策一致性作为核心指标；其结果指出大部分代码收集和流量传输涉及 external service providers，且部分传输不符合 privacy policy。该论文支持对 Firebase/Mailchimp/Adafruit recipient 做区分，但没有抓包时不能确认实际传输。`
- `audit_reports/lightblue_beginner_audit_report.md:76`
  `- B002 'Unaddressed privacy risks in accredited health and wellness apps'：论文方法包括数据输入、设备本地存储抽取、加密机制检查、传输抓包和 privacy policy 对照；其背景指出设备丢失时，未加密本地医疗信息可能被恶意用户访问。该论文支持检查 token/secret/health data 的本地存储，但本 App 没有运行后本地文件，不能确认设备上已有真实 secret。`
- `audit_reports/lightblue_beginner_audit_report.md:100`
  `- 论文：B002 'Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment'`
- `audit_reports/lightblue_beginner_audit_report.md:109`
  `- 论文：B010 'Client-Focused Security Assessment of mHealth Apps...'；B019 'Assessment of Privacy Policies of Apps for Core Symptoms of COVID-19'；B008 'Your Signal, Their Data...'`
- `audit_reports/lightblue_beginner_audit_report.md:118`
  `- 论文：B005 'Mobile health and privacy: cross sectional study'；B007 'Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs'`
- `audit_reports/rule_by_rule_mapping.md:11`
  `- BR005 | B021 'Mobile App Metadata-Based Privacy Assessment' | 'not_testable' | 未提供 app store description/privacy metadata，无法比较描述与权限。`
- `audit_reports/rule_by_rule_mapping.md:12`
  `- BR006 | B016 'A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps' | 'not_supported' | Manifest 未见 'usesCleartextTraffic=true' 或 cleartext domain config。`
- `audit_reports/rule_by_rule_mapping.md:25`
  `- BR019 | B011 'Locking It Down: The Privacy and Security of Mobile Medication Apps' | 'not_supported' | 未见 medication/dose/prescription/reminder 字段。`
- `audit_reports/rule_by_rule_mapping.md:26`
  `- BR020 | B012 'Privacy and Security Behavioral Assessment of Depression Apps' | 'not_supported' | 未见 mood/depression/anxiety/journal/survey 字段。`
- `audit_reports/rule_by_rule_mapping.md:36`
  `- BR030 | B016 'A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps' | 'not_supported' | 未见导出一方 Service 触发 sync/upload/device command。`
- `audit_reports/rule_by_rule_mapping.md:37`
  `- BR031 | B016 'A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps' | 'not_supported' | 未见导出一方 BroadcastReceiver 进入敏感模块。`
- `audit_reports/rule_by_rule_mapping.md:42`
  `- BR040 | B007 'Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs' | 'not_supported' | 未发现 Facebook SDK，不能把 Firebase/Mailchimp 套用为 Facebook 规则。`
- `audit_reports/rule_by_rule_mapping.md:43`
  `- BR041 | B007 'Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs' | 'not_supported' | 未发现 Facebook SDK auto logging/default settings。`
- `audit_reports/rule_by_rule_mapping.md:44`
  `- BR042 | B008 'Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android' | 'not_supported' | 'BluetoothLeScanner.startScan' 在一方 'K5.b'，不在第三方 SDK namespace。`
- `audit_reports/rule_by_rule_mapping.md:48`
  `- BR050 | B021 'Mobile App Metadata-Based Privacy Assessment' | 'not_testable' | 未能解码/获取 privacy URL 文本并验证可达性。`
- `audit_reports/rule_by_rule_mapping.md:49`
  `- BR051 | B013 'Assessment of Availability, Readability, and Content of Privacy Policies of mHealth Apps' | 'not_testable' | 缺隐私政策正文，无法判断是否遗漏 BLE/location/device data。`
- `audit_reports/rule_by_rule_mapping.md:50`
  `- BR052 | B013 'Assessment of Availability, Readability, and Content of Privacy Policies of mHealth Apps' | 'not_testable' | 缺隐私政策正文，无法判断第三方分享披露。`
- `audit_reports/rule_by_rule_mapping.md:51`
  `- BR055 | B014 'Privacy Assessment in Mobile Health Apps' | 'confirmed' | 本审计提供 file/class/function/rule 证据；该条是报告质量 meta-rule。`
- `audit_reports/rule_by_rule_mapping.md:54`
  `- BR060 | B016 'A privacy and security analysis...' | 'not_supported' | 未见 env/baseUrl/channel flag 可切换 backend。`
- `audit_reports/rule_by_rule_mapping.md:68`
  `- BR071 | B016 'A privacy and security analysis...' | 'not_testable' | BLE/location 权限有功能解释，但隐私政策正文不可用。`
- `audit_reports/rule_by_rule_mapping.md:76`
  `- BR076 | B005 'Mobile health and privacy: cross sectional study' | 'not_testable' | 无首启抓包；静态 Firebase/Mailchimp 初始化只能指导复测。`
- `audit_reports/rule_by_rule_mapping.md:77`
  `- BR077 | B007 'Privacy Settings of Third-Party Libraries...' | 'not_testable' | 无同意前后抓包；且无 Facebook SDK。`
- `audit_reports/rule_by_rule_mapping.md:81`
  `- BR081 | B005 'Mobile health and privacy...' | 'not_testable' | 无使用后 DB/prefs/DataStore 抽取。`
- `audit_reports/rule_by_rule_mapping.md:82`
  `- BR082 | B002 'Unaddressed privacy risks...' | 'not_testable' | 无 logout/delete 生命周期测试和存储抽取。`
- `audit_reports/rule_by_rule_mapping.md:83`
  `- BR083 | B016 'A privacy and security analysis...' | 'not_testable' | 未做 adb 调用 exported component 测试。`
- `audit_reports/rule_by_rule_mapping.md:86`
  `- BR088 | B004 'Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation' | 'not_testable' | 无第三方请求与 health/mental/medication flow 同步抓包。`
- `audit_reports/rule_by_rule_mapping.md:87`
  `- BR090 | B014 'Privacy Assessment in Mobile Health Apps' | 'not_testable' | 未做手机端动态验证。`
- `audit_reports/rule_by_rule_mapping.md:92`
  `- BR092 | B005 'Mobile health and privacy...' | 'supported_hypothesis' | Firebase/Mailchimp/Adafruit third-party recipients 与 device_model analytics 代码存在；无 adid/deviceId/userId 上传抓包。`
- `audit_reports/rule_by_rule_mapping.md:93`
  `- BR093 | B004 'Assessment of the Data Sharing and Privacy Practices...' | 'not_testable' | 缺隐私政策正文和 observed traffic，无法判断 recipient 是否未披露。`
- `audit_reports/rule_by_rule_mapping.md:94`
  `- BR094 | B016 'A privacy and security analysis...' | 'not_supported' | 未见单个 API 组合 identity + device + location + health context。`
- `audit_reports/rule_by_rule_mapping.md:97`
  `- BR097 | B019 'Assessment of Privacy Policies of Apps for Core Symptoms of COVID-19' | 'supported_hypothesis' | demo 包含 heart/glucose/blood pressure GATT，Adafruit 可上传任意 BLE bytes；无真实账号关联上传。`

## BR052

paper_id: B013
paper_title: Availability and quality of mobile health app privacy policies

- `audit_reports/lightblue_beginner_audit_report.md:75`
  `- B005 'Mobile health and privacy: cross sectional study'：论文将 App 代码中的数据收集操作、App 流量中的数据传输、第三方 recipient、trackers/adverts 与隐私政策一致性作为核心指标；其结果指出大部分代码收集和流量传输涉及 external service providers，且部分传输不符合 privacy policy。该论文支持对 Firebase/Mailchimp/Adafruit recipient 做区分，但没有抓包时不能确认实际传输。`
- `audit_reports/lightblue_beginner_audit_report.md:76`
  `- B002 'Unaddressed privacy risks in accredited health and wellness apps'：论文方法包括数据输入、设备本地存储抽取、加密机制检查、传输抓包和 privacy policy 对照；其背景指出设备丢失时，未加密本地医疗信息可能被恶意用户访问。该论文支持检查 token/secret/health data 的本地存储，但本 App 没有运行后本地文件，不能确认设备上已有真实 secret。`
- `audit_reports/lightblue_beginner_audit_report.md:100`
  `- 论文：B002 'Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment'`
- `audit_reports/lightblue_beginner_audit_report.md:109`
  `- 论文：B010 'Client-Focused Security Assessment of mHealth Apps...'；B019 'Assessment of Privacy Policies of Apps for Core Symptoms of COVID-19'；B008 'Your Signal, Their Data...'`
- `audit_reports/lightblue_beginner_audit_report.md:118`
  `- 论文：B005 'Mobile health and privacy: cross sectional study'；B007 'Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs'`
- `audit_reports/rule_by_rule_mapping.md:11`
  `- BR005 | B021 'Mobile App Metadata-Based Privacy Assessment' | 'not_testable' | 未提供 app store description/privacy metadata，无法比较描述与权限。`
- `audit_reports/rule_by_rule_mapping.md:12`
  `- BR006 | B016 'A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps' | 'not_supported' | Manifest 未见 'usesCleartextTraffic=true' 或 cleartext domain config。`
- `audit_reports/rule_by_rule_mapping.md:25`
  `- BR019 | B011 'Locking It Down: The Privacy and Security of Mobile Medication Apps' | 'not_supported' | 未见 medication/dose/prescription/reminder 字段。`
- `audit_reports/rule_by_rule_mapping.md:26`
  `- BR020 | B012 'Privacy and Security Behavioral Assessment of Depression Apps' | 'not_supported' | 未见 mood/depression/anxiety/journal/survey 字段。`
- `audit_reports/rule_by_rule_mapping.md:31`
  `- BR025 | B005 'Mobile health and privacy: cross sectional study' | 'not_supported' | 未见一方 SQLite 敏感字段；WorkManager/AndroidX DB 属框架。`
- `audit_reports/rule_by_rule_mapping.md:32`
  `- BR026 | B002 'Unaddressed privacy risks in accredited health and wellness apps' | 'supported_hypothesis' | 'ADAFRUIT_IO_USERNAME' 与 'ADAFRUIT_IO_SECRET_KEY' 写入 DataStore；无设备抽取，不能 confirmed。`
- `audit_reports/rule_by_rule_mapping.md:33`
  `- BR027 | B002 'Unaddressed privacy risks in accredited health and wellness apps' | 'not_supported' | 未见 report/health/log/export 写到外部存储。`
- `audit_reports/rule_by_rule_mapping.md:34`
  `- BR028 | B014 'Privacy Assessment in Mobile Health Apps' | 'not_supported' | Manifest 'allowBackup=false'；本地 secret 风险不等于 backup 风险 confirmed。`
- `audit_reports/rule_by_rule_mapping.md:35`
  `- BR029 | B016 'A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps' | 'not_supported' | 导出 Activity 未见进入 account/device/report page。`
- `audit_reports/rule_by_rule_mapping.md:36`
  `- BR030 | B016 'A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps' | 'not_supported' | 未见导出一方 Service 触发 sync/upload/device command。`
- `audit_reports/rule_by_rule_mapping.md:37`
  `- BR031 | B016 'A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps' | 'not_supported' | 未见导出一方 BroadcastReceiver 进入敏感模块。`
- `audit_reports/rule_by_rule_mapping.md:42`
  `- BR040 | B007 'Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs' | 'not_supported' | 未发现 Facebook SDK，不能把 Firebase/Mailchimp 套用为 Facebook 规则。`
- `audit_reports/rule_by_rule_mapping.md:43`
  `- BR041 | B007 'Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs' | 'not_supported' | 未发现 Facebook SDK auto logging/default settings。`
- `audit_reports/rule_by_rule_mapping.md:44`
  `- BR042 | B008 'Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android' | 'not_supported' | 'BluetoothLeScanner.startScan' 在一方 'K5.b'，不在第三方 SDK namespace。`
- `audit_reports/rule_by_rule_mapping.md:48`
  `- BR050 | B021 'Mobile App Metadata-Based Privacy Assessment' | 'not_testable' | 未能解码/获取 privacy URL 文本并验证可达性。`
- `audit_reports/rule_by_rule_mapping.md:49`
  `- BR051 | B013 'Assessment of Availability, Readability, and Content of Privacy Policies of mHealth Apps' | 'not_testable' | 缺隐私政策正文，无法判断是否遗漏 BLE/location/device data。`
- `audit_reports/rule_by_rule_mapping.md:50`
  `- BR052 | B013 'Assessment of Availability, Readability, and Content of Privacy Policies of mHealth Apps' | 'not_testable' | 缺隐私政策正文，无法判断第三方分享披露。`
- `audit_reports/rule_by_rule_mapping.md:51`
  `- BR055 | B014 'Privacy Assessment in Mobile Health Apps' | 'confirmed' | 本审计提供 file/class/function/rule 证据；该条是报告质量 meta-rule。`
- `audit_reports/rule_by_rule_mapping.md:54`
  `- BR060 | B016 'A privacy and security analysis...' | 'not_supported' | 未见 env/baseUrl/channel flag 可切换 backend。`
- `audit_reports/rule_by_rule_mapping.md:68`
  `- BR071 | B016 'A privacy and security analysis...' | 'not_testable' | BLE/location 权限有功能解释，但隐私政策正文不可用。`
- `audit_reports/rule_by_rule_mapping.md:76`
  `- BR076 | B005 'Mobile health and privacy: cross sectional study' | 'not_testable' | 无首启抓包；静态 Firebase/Mailchimp 初始化只能指导复测。`
- `audit_reports/rule_by_rule_mapping.md:77`
  `- BR077 | B007 'Privacy Settings of Third-Party Libraries...' | 'not_testable' | 无同意前后抓包；且无 Facebook SDK。`
- `audit_reports/rule_by_rule_mapping.md:81`
  `- BR081 | B005 'Mobile health and privacy...' | 'not_testable' | 无使用后 DB/prefs/DataStore 抽取。`
- `audit_reports/rule_by_rule_mapping.md:82`
  `- BR082 | B002 'Unaddressed privacy risks...' | 'not_testable' | 无 logout/delete 生命周期测试和存储抽取。`
- `audit_reports/rule_by_rule_mapping.md:83`
  `- BR083 | B016 'A privacy and security analysis...' | 'not_testable' | 未做 adb 调用 exported component 测试。`
- `audit_reports/rule_by_rule_mapping.md:86`
  `- BR088 | B004 'Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation' | 'not_testable' | 无第三方请求与 health/mental/medication flow 同步抓包。`
- `audit_reports/rule_by_rule_mapping.md:87`
  `- BR090 | B014 'Privacy Assessment in Mobile Health Apps' | 'not_testable' | 未做手机端动态验证。`
- `audit_reports/rule_by_rule_mapping.md:92`
  `- BR092 | B005 'Mobile health and privacy...' | 'supported_hypothesis' | Firebase/Mailchimp/Adafruit third-party recipients 与 device_model analytics 代码存在；无 adid/deviceId/userId 上传抓包。`
- `audit_reports/rule_by_rule_mapping.md:93`
  `- BR093 | B004 'Assessment of the Data Sharing and Privacy Practices...' | 'not_testable' | 缺隐私政策正文和 observed traffic，无法判断 recipient 是否未披露。`
- `audit_reports/rule_by_rule_mapping.md:94`
  `- BR094 | B016 'A privacy and security analysis...' | 'not_supported' | 未见单个 API 组合 identity + device + location + health context。`
- `audit_reports/rule_by_rule_mapping.md:97`
  `- BR097 | B019 'Assessment of Privacy Policies of Apps for Core Symptoms of COVID-19' | 'supported_hypothesis' | demo 包含 heart/glucose/blood pressure GATT，Adafruit 可上传任意 BLE bytes；无真实账号关联上传。`
- `resources/com.punchthrough.lightblueexplorer.apk/res/menu/menu_about_activity.xml:8`
  `android:id="@+id/menu_privacy_policy"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/menu/menu_about_activity.xml:9`
  `android:title="@string/privacy_policy_settings_title"`
- `resources/res/values/public.xml:3676`
  `<public type="id" name="menu_privacy_policy" id="0x7f0a0146" />`
- `resources/res/values/strings.xml:682`
  `<string name="privacy_policy_title">LightBlue® Privacy Policy</string>`

## BR058

paper_id: B022
paper_title: A Study of Android Application Security

- `audit_reports/evidence_chains.md:89`
  `1. First-party Activity：'LaunchActivity' exported=true，包含 'MAIN'、'VIEW'、'LAUNCHER'，未见 data URI、host、scheme、BROWSABLE。'MainActivity' exported=true，含 SEARCH action；未见外部 URI 参数进入敏感动作。'DevOptionsActivity' 与 'QRCodeScannerActivity' exported=false。`
- `audit_reports/evidence_chains.md:90`
  `2. First-party provider：'androidx.core.content.FileProvider' authority 'com.punchthrough.lightblueexplorer.provider'，exported=false，grantUriPermissions=true。'provider_paths.xml' 使用 '<files-path name="external_files" path="."/>'。因 provider 不导出，不能确认外部读取/写入。`
- `audit_reports/evidence_chains.md:91`
  `3. Third-party/system components：Firebase/MLKit providers exported=false；WorkManager/SystemJobService exported=true 但有系统权限或框架用途；ProfileInstaller receiver exported=true 并带 'android.permission.DUMP'。`
- `audit_reports/evidence_chains.md:100`
  `2. First-party endpoints：Adafruit base URL 为 'https://io.adafruit.com/api/v2/'；Mailchimp endpoint 为 'https://%s.api.mailchimp.com/clientapi/1.0/'；Firebase/Google endpoints 属第三方 SDK。`
- `audit_reports/evidence_chains.md:102`
  `4. Third-party TLS classes：'V8.d'、'V8.c'、OkHttp 相关类为库实现，不能直接按一方弱 TLS confirmed。`
- `audit_reports/lightblue_beginner_audit_report.md:118`
  `- 论文：B005 'Mobile health and privacy: cross sectional study'；B007 'Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs'`
- `audit_reports/mentor_review.md:103`
  `2. 把 Firebase/Mailchimp 首启或同意前发包从 supported/confirmed 降级为动态规则 'not_testable'，只在 cloud/third-party recipient 层保留 static hypothesis。`
- `audit_reports/rule_by_rule_mapping.md:42`
  `- BR040 | B007 'Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs' | 'not_supported' | 未发现 Facebook SDK，不能把 Firebase/Mailchimp 套用为 Facebook 规则。`
- `audit_reports/rule_by_rule_mapping.md:43`
  `- BR041 | B007 'Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs' | 'not_supported' | 未发现 Facebook SDK auto logging/default settings。`
- `audit_reports/rule_by_rule_mapping.md:77`
  `- BR077 | B007 'Privacy Settings of Third-Party Libraries...' | 'not_testable' | 无同意前后抓包；且无 Facebook SDK。`
- `audit_reports/rule_by_rule_mapping.md:92`
  `- BR092 | B005 'Mobile health and privacy...' | 'supported_hypothesis' | Firebase/Mailchimp/Adafruit third-party recipients 与 device_model analytics 代码存在；无 adid/deviceId/userId 上传抓包。`
- `sources/M8/AbstractC3941o.java:30`
  `throw new UnsupportedOperationException("third-party implementation of CancellableContinuation is not supported");`

## BR059

paper_id: B006
paper_title: Analyzing security issues of android mobile health and medical applications

- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:78`
  `<intent-filter>`

## BR061

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/B0/O0.java:278`
  `o02.f1303u.setValue(d.ShuttingDown);`
- `sources/B0/O0.java:1352`
  `this.f1303u.setValue(d.ShuttingDown);`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:56`
  `@Metadata(d1 = {"\u0000Û\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u000b\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0004\n\u0002\u0010\u0012\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u000e\n\u0002\u0010 \n\u0002\u0018\...`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:672`
  `BluetoothGattCharacteristic bluetoothGattCharacteristic = this.microchipWriteCharacteristic;`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:674`
  `d9.a.f31145a.c("Unable to write to characteristic- microchipWriteCharacteristic is null", new Object[0]);`
- `sources/J5/C1753c.java:33`
  `bluetoothGattCharacteristic.setValue(bArr);`
- `sources/J5/C1753c.java:34`
  `return this.f7925a.writeCharacteristic(bluetoothGattCharacteristic);`
- `sources/J5/C1753c.java:38`
  `bluetoothGattDescriptor.setValue(bArr);`
- `sources/J5/C1753c.java:39`
  `return this.f7925a.writeDescriptor(bluetoothGattDescriptor);`
- `sources/J5/C1753c.java:106`
  `return Build.VERSION.SDK_INT >= 33 ? this.f7925a.writeDescriptor(bluetoothGattDescriptor, bArr) == 0 : b(bluetoothGattDescriptor, bArr);`
- `sources/J5/C1753c.java:119`
  `return Build.VERSION.SDK_INT >= 33 ? this.f7925a.writeCharacteristic(bluetoothGattCharacteristic, bArr, i9) == 0 : a(bluetoothGattCharacteristic, bArr, i9);`
- `sources/k6/AbstractC3620C.java:100`
  `bluetoothGattDescriptor.setValue(BluetoothGattDescriptor.DISABLE_NOTIFICATION_VALUE);`
- `sources/k6/AbstractC3620C.java:107`
  `bluetoothGattDescriptor2.setValue(bytes);`
- `sources/k6/C3619B.java:1307`
  `this.f35521l.setValue(bArr);`
- `sources/k6/C3619B.java:1852`
  `bluetoothGattCharacteristic.setValue(bArr);`
- `sources/M8/u.java:45`
  `String protocol = sSLSession.getProtocol();`
- `sources/R5/a.java:105`
  `AbstractC1838t.g(bluetoothGattCharacteristic, "writeCharacteristic");`
- `sources/Y8/h.java:134`
  `if (AbstractC1838t.b(url.getProtocol(), "file")) {`

## BR063

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/com/google/android/gms/measurement/internal/C2922f2.java:214`
  `return B(3, new byte[0]);`
- `sources/com/google/android/gms/measurement/internal/C3035v4.java:56`
  `return new byte[0];`
- `sources/com/google/android/gms/measurement/internal/C3035v4.java:235`
  `return new byte[0];`
- `sources/com/google/android/gms/measurement/internal/C3035v4.java:238`
  `return new byte[0];`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:591`
  `byte[] bArrK = serialDevice.k(text);`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:614`
  `byte[] bArrL = serialDevice.l(text);`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:648`
  `byte[] bArrH = aVar != null ? aVar.h(payload, (byte) 83) : null;`
- `sources/com/punchthrough/lightblueexplorer/ui/characteristicdetail/b.java:1425`
  `byte[] bArrC = AbstractC1935e.c(((com.punchthrough.lightblueexplorer.ui.characteristicdetail.c) this.f30824E.getValue()).k().c().h(), ((com.punchthrough.lightblueexplorer.ui.characteristicdetail.c) this.f30824E.getValue()).e().getSavedFormat(), ((com.punchthrough.lightblueexplorer.ui.characteristicd...`
- `sources/I3/M.java:413`
  `contentValues.put("payload", z9 ? bArrA : new byte[0]);`
- `sources/I3/M.java:422`
  `byte[] bArrCopyOfRange = Arrays.copyOfRange(bArrA, (i9 - 1) * iE, Math.min(i9 * iE, bArrA.length));`
- `sources/J5/F.java:43`
  `f7910f = E6.N.k(D6.C.a(f9.d("2C06"), "Acceleration"), D6.C.a(f9.d("2B33"), "ACS Control Point"), D6.C.a(f9.d("2B30"), "ACS Data In"), D6.C.a(f9.d("2B32"), "ACS Data Out Indicate"), D6.C.a(f9.d("2B31"), "ACS Data Out Notify"), D6.C.a(f9.d("2B2F"), "ACS Status"), D6.C.a(f9.d("2BDC"), "Active Preset In...`
- `sources/P3/E.java:56`
  `byte[] bArr = aVarB == null ? null : (byte[]) A3.b.f(aVarB);`
- `sources/R5/a.java:175`
  `byte[] bArrD = d(bArr);`
- `sources/R5/a.java:317`
  `byte[] bArr2 = new byte[2];`
- `sources/v5/C4603c.java:95`
  `byte[] bArr = new byte[iRemaining];`

## BR064

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/compose/ui/platform/C0.java:10`
  `str = obj.getClass().isAnonymousClass() ? obj.getClass().getName() : obj.getClass().getSimpleName();`
- `sources/androidx/work/impl/C2370j.java:21`
  `gVar.x(AbstractC3720m.e("UPDATE WorkSpec\n                SET input_merger_class_name = '" + OverwritingInputMerger.class.getName() + "'\n                WHERE input_merger_class_name IS NULL\n                "));`
- `sources/B0/AbstractC1034c.java:13`
  `return Thread.currentThread().getName();`
- `sources/c5/c.java:39`
  `return field.getName();`
- `sources/C6/C2509a.java:124`
  `return "AdvertisementData(connectionStatus=" + this.f26084a + ", deviceName=" + this.f26085b + ", serviceUuids=" + this.f26086c + ", manufacturerSpecificData=" + this.f26087d + ", rawAdvertisementPacket=" + this.f26088e + ")";`
- `sources/C6/m.java:108`
  `AbstractC1838t.g(str, "deviceName");`
- `sources/C6/m.java:226`
  `AbstractC1838t.g(str, "deviceName");`
- `sources/C6/m.java:283`
  `return "DeviceDetailViewState(deviceName=" + this.f26221a + ", macAddress=" + this.f26222b + ", advertisementData=" + this.f26223c + ", services=" + this.f26224d + ", showMtuDialog=" + this.f26225e + ", requestedMtuInput=" + this.f26226f + ", dialogState=" + this.f26227g + ", txPower=" + this.f26228...`
- `sources/C6/t.java:30`
  `AbstractC1838t.g(str, "deviceName");`
- `sources/C6/t.java:85`
  `return "LaunchCharacteristicDetails(deviceName=" + this.f26263a + ", serviceUuid=" + this.f26264b + ", characteristicUuid=" + this.f26265c + ", readableName=" + this.f26266d + ", device=" + this.f26267e + ", service=" + this.f26268f + ")";`
- `sources/com/google/android/gms/internal/measurement/AbstractC2673p4.java:28`
  `str = String.format("%s.BlazeGenerated%sLoader", cls.getPackage().getName(), cls.getSimpleName());`
- `sources/com/google/android/gms/internal/measurement/AbstractC2673p4.java:53`
  `Logger.getLogger(AbstractC2540a4.class.getName()).logp(Level.SEVERE, "com.google.protobuf.GeneratedExtensionRegistryLoader", "load", "Unable to load " + cls.getSimpleName(), (Throwable) e13);`
- `sources/com/google/android/gms/internal/measurement/C2.java:59`
  `return "<" + a.class.getName() + '@' + Integer.toHexString(System.identityHashCode(this)) + " number=" + this.f26534w + " name=" + name() + '>';`
- `sources/com/google/android/gms/internal/measurement/C2630k4.java:185`
  `throw new IllegalArgumentException(String.format("Wrong object type used with protocol message reflection.\nField number: %d, field java type: %s, value type: %s\n", Integer.valueOf(interfaceC2648m4.zza()), interfaceC2648m4.zzb().c(), obj.getClass().getName()));`
- `sources/com/google/android/gms/internal/measurement/C2663o2.java:102`
  `return "<" + b.class.getName() + '@' + Integer.toHexString(System.identityHashCode(this)) + " number=" + this.f27205w + " name=" + name() + '>';`
- `sources/com/google/android/gms/internal/measurement/C2679q2.java:58`
  `return "<" + b.class.getName() + '@' + Integer.toHexString(System.identityHashCode(this)) + " number=" + this.f27226w + " name=" + name() + '>';`
- `sources/com/google/android/gms/internal/measurement/EnumC2661o0.java:27`
  `sb.append(EnumC2661o0.class.getName());`
- `sources/com/google/android/gms/internal/measurement/EnumC2726w2.java:49`
  `return "<" + EnumC2726w2.class.getName() + '@' + Integer.toHexString(System.identityHashCode(this)) + " number=" + this.f27348w + " name=" + name() + '>';`
- `sources/com/google/android/gms/internal/measurement/L1.java:63`
  `return "<" + b.class.getName() + '@' + Integer.toHexString(System.identityHashCode(this)) + " number=" + this.f26638w + " name=" + name() + '>';`
- `sources/com/google/android/gms/internal/measurement/N1.java:67`
  `return "<" + b.class.getName() + '@' + Integer.toHexString(System.identityHashCode(this)) + " number=" + this.f26692w + " name=" + name() + '>';`
- `sources/com/google/android/gms/internal/measurement/Q1.java:201`
  `return "<" + d.class.getName() + '@' + Integer.toHexString(System.identityHashCode(this)) + " number=" + this.f26709w + " name=" + name() + '>';`
- `sources/com/google/android/gms/internal/measurement/Q1.java:250`
  `return "<" + e.class.getName() + '@' + Integer.toHexString(System.identityHashCode(this)) + " number=" + this.f26716w + " name=" + name() + '>';`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:56`
  `@Metadata(d1 = {"\u0000Û\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u000b\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0004\n\u0002\u0010\u0012\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u000e\n\u0002\u0010 \n\u0002\u0018\...`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:118`
  `private String deviceName = "";`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:321`
  `aVarS0.x(microchipActivity.deviceName);`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:337`
  `MicrochipActivity.this.deviceName = new String(bArr, C3711d.f36679b);`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:432`
  `final String string = microchipActivity.getString(R.string.alert_dialog_title_disconnect_from_device, microchipActivity.deviceName);`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:435`
  `final String string2 = microchipActivity2.getString(R.string.return_to_scanning_prompt, microchipActivity2.deviceName);`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:533`
  `intent.putExtra("com.punchthrough.lightblueexplorer.ui.devicedetails.DeviceDetailActivity.SelectedDeviceName", this.deviceName);`
- `sources/com/punchthrough/lightblueexplorer/ui/characteristicdetail/b.java:381`
  `String name = yVar.getName();`
- `sources/com/punchthrough/lightblueexplorer/ui/characteristicdetail/b.java:1119`
  `return AbstractC3720m.C("LightBlue" + yVar.getName(), " ", "", false, 4, null);`
- `sources/com/punchthrough/lightblueexplorer/ui/devicedetails/DeviceDetailActivity.java:1073`
  `intent.putExtra("com.punchthrough.lightblueexplorer.ui.devicedetails.DeviceDetailActivity.SelectedDeviceName", launchData.c());`
- `sources/F3/V.java:27`
  `String str2 = obj.getClass().getName() + "@" + Integer.toHexString(System.identityHashCode(obj));`
- `sources/F3/V.java:29`
  `string = "<" + str2 + " threw " + e9.getClass().getName() + ">";`
- `sources/f5/n.java:797`
  `throw new UnsupportedOperationException("Attempted to serialize java.lang.Class: " + cls.getName() + ". Forgot to register a type adapter?");`
- `sources/G3/AbstractC1467v.java:28`
  `String str2 = obj.getClass().getName() + "@" + Integer.toHexString(System.identityHashCode(obj));`
- `sources/G3/AbstractC1467v.java:30`
  `string = "<" + str2 + " threw " + e9.getClass().getName() + ">";`
- `sources/H3/AbstractC1574h2.java:28`
  `String str2 = obj.getClass().getName() + '@' + Integer.toHexString(System.identityHashCode(obj));`
- `sources/H3/AbstractC1574h2.java:30`
  `string = "<" + str2 + " threw " + e9.getClass().getName() + ">";`
- `sources/H5/f0.java:1634`
  `AbstractC1838t.g(str2, "connectingDeviceName");`
- `sources/H5/f0.java:1675`
  `AbstractC1838t.g(str2, "connectingDeviceName");`
- `sources/H5/f0.java:1724`
  `return "ViewState(currentAlertContent=" + this.f7274a + ", searchQuery=" + this.f7275b + ", rssiFilterMin=" + this.f7276c + ", isRssiFilterEnabled=" + this.f7277d + ", isConnecting=" + this.f7278e + ", connectingDeviceName=" + this.f7279f + ", showRssiFilterDialog=" + this.f7280g + ")";`
- `sources/J5/C1754d.java:635`
  `e.a.a(this.f7928b, Q5.b.f11758x, "Cannot connect to " + yVar.H() + " (" + yVar.getName() + "): already connected", Q5.c.f11763B, 0L, yVar, null, null, null, null, 488, null);`
- `sources/J5/C1754d.java:765`
  `e.a.a(this.f7928b, Q5.b.f11757w, "Disconnecting from " + yVar.H() + " (" + yVar.getName() + ")", Q5.c.f11763B, 0L, yVar, null, null, null, null, 488, null);`
- `sources/J5/C1763m.java:59`
  `String name = this.f7987x.getName();`
- `sources/K5/c.java:62`
  `return this.f8335a.getDeviceName();`
- `sources/k6/AbstractC3661c.java:180`
  `AbstractC3661c.e(null, virtualDevice.getName(), AbstractC1838t.b(virtualDevice, this.f36097y), new C0744a(this.f36098z, virtualDevice), interfaceC1059m, 0, 1);`
- `sources/k6/C3619B.java:148`
  `d9.a.f31145a.i("Advertisement started for " + virtualDevice.getName(), new Object[0]);`
- `sources/k6/C3619B.java:220`
  `e.a.a(eVar, bVar, "Failed to start advertising virtual device: " + (virtualDevice != null ? virtualDevice.getName() : null) + ", error: " + i9 + " (" + str + ")", null, 0L, null, null, null, null, null, 508, null);`
- `sources/k6/C3619B.java:442`
  `String address = bluetoothDevice.getAddress();`
- `sources/k6/C3619B.java:444`
  `e.a.a(eVar, bVar, "Received characteristic " + uuid + " read request from device " + address + " on virtual device " + (virtualDevice != null ? virtualDevice.getName() : null), null, 0L, null, null, bluetoothGattCharacteristic, null, null, 444, null);`
- `sources/k6/C3619B.java:460`
  `String address = bluetoothDevice != null ? bluetoothDevice.getAddress() : null;`
- `sources/k6/C3619B.java:462`
  `e.a.a(eVar, bVar, "Received characteristic " + uuid + " write request of payload " + strI + " from device " + address + " on virtual device " + (virtualDevice != null ? virtualDevice.getName() : null), null, 0L, null, null, bluetoothGattCharacteristic, null, bArr, 188, null);`
- `sources/k6/C3619B.java:475`
  `d9.a.f31145a.i("Device disconnected from virtual device: " + bluetoothDevice.getAddress(), new Object[0]);`
- `sources/k6/C3619B.java:478`
  `String address = bluetoothDevice.getAddress();`
- `sources/k6/C3619B.java:480`
  `e.a.a(eVar, bVar, "Device " + address + " disconnected from virtual device " + (virtualDevice != null ? virtualDevice.getName() : null), null, 0L, null, null, null, null, null, 508, null);`
- `sources/k6/C3619B.java:487`
  `d9.a.f31145a.i("Device connected to virtual device: " + bluetoothDevice.getAddress(), new Object[0]);`
- `sources/k6/C3619B.java:490`
  `String address2 = bluetoothDevice.getAddress();`
- `sources/k6/C3619B.java:492`
  `e.a.a(eVar2, bVar2, "Device " + address2 + " connected to virtual device " + (virtualDevice2 != null ? virtualDevice2.getName() : null), null, 0L, null, null, null, null, null, 508, null);`
- `sources/k6/C3619B.java:529`
  `String address = bluetoothDevice != null ? bluetoothDevice.getAddress() : null;`
- `sources/k6/C3619B.java:531`
  `e.a.a(eVar, bVar, "Received descriptor " + uuid + " read request from device " + address + " on virtual device " + (virtualDevice != null ? virtualDevice.getName() : null), null, 0L, null, null, null, bluetoothGattDescriptor, null, 380, null);`
- `sources/k6/C3619B.java:583`
  `String address = bluetoothDevice != null ? bluetoothDevice.getAddress() : null;`
- `sources/k6/C3619B.java:585`
  `e.a.a(eVar, bVar, "Received descriptor " + uuid + " write request of payload " + strI + " from device " + address + " on virtual device " + (virtualDevice != null ? virtualDevice.getName() : null), null, 0L, null, null, null, bluetoothGattDescriptor, bArr, 124, null);`
- `sources/k6/C3619B.java:605`
  `String address2 = bluetoothDevice != null ? bluetoothDevice.getAddress() : null;`
- `sources/k6/C3619B.java:607`
  `e.a.a(eVar2, bVar2, "Enabled notifications/indications on characteristic " + uuid2 + " for connected device " + address2 + str + (virtualDevice2 != null ? virtualDevice2.getName() : null), null, 0L, null, null, null, bluetoothGattDescriptor, null, 380, null);`
- `sources/k6/C3619B.java:618`
  `String address3 = bluetoothDevice != null ? bluetoothDevice.getAddress() : null;`
- `sources/k6/C3619B.java:620`
  `e.a.a(eVar3, bVar3, "Disabled notifications/indications on characteristic " + uuid2 + " for connected device " + address3 + str + (virtualDevice3 != null ? virtualDevice3.getName() : null), null, 0L, null, null, null, bluetoothGattDescriptor, null, 380, null);`
- `sources/k6/C3619B.java:630`
  `String address = bluetoothDevice != null ? bluetoothDevice.getAddress() : null;`
- `sources/k6/C3619B.java:632`
  `e.a.a(eVar, bVar, "Successfully sent notification/indication to " + address + " from virtual device " + (virtualDevice != null ? virtualDevice.getName() : null), null, 0L, null, null, null, null, null, 508, null);`
- `sources/k6/C3619B.java:637`
  `String address2 = bluetoothDevice != null ? bluetoothDevice.getAddress() : null;`
- `sources/k6/C3619B.java:639`
  `e.a.a(eVar2, bVar2, "Failed to send notification/indication to " + address2 + " from virtual device " + (virtualDevice2 != null ? virtualDevice2.getName() : null), null, 0L, null, null, null, null, null, 508, null);`
- `sources/k6/C3619B.java:1311`
  `String name = bluetoothDevice.getName();`
- `sources/k6/C3619B.java:1313`
  `name = bluetoothDevice.getAddress();`
- `sources/k6/C3619B.java:1555`
  `e.a.a(eVar, bVar, "Stopping advertisement for virtual device " + (virtualDevice != null ? virtualDevice.getName() : null), null, 0L, null, null, null, null, null, 508, null);`
- `sources/k6/C3619B.java:1661`
  `String address = bluetoothDevice.getAddress();`
- `sources/k6/C3619B.java:1662`
  `String name = bluetoothDevice.getName();`
- `sources/k6/C3619B.java:1664`
  `e.a.a(eVar, bVar, "Notifying payload " + strI + " to device " + address + " (" + name + ") from virtual device " + (virtualDevice != null ? virtualDevice.getName() : null), null, 0L, null, bluetoothGattService, bluetoothGattCharacteristic, null, bArr, 156, null);`
- `sources/k6/C3619B.java:1844`
  `String address = bluetoothDevice.getAddress();`
- `sources/k6/C3619B.java:1845`
  `String name = bluetoothDevice.getName();`
- `sources/k6/C3619B.java:1847`
  `e.a.a(eVar, bVar, "Indicating payload " + strI + " to device " + address + " (" + name + ") from virtual device " + (virtualDevice != null ? virtualDevice.getName() : null), null, 0L, null, bluetoothGattService, bluetoothGattCharacteristic, null, bArr, 156, null);`

## BR066

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/work/impl/foreground/b.java:142`
  `this.f24961x.j(UUID.fromString(stringExtra));`
- `sources/C6/C2509a.java:124`
  `return "AdvertisementData(connectionStatus=" + this.f26084a + ", deviceName=" + this.f26085b + ", serviceUuids=" + this.f26086c + ", manufacturerSpecificData=" + this.f26087d + ", rawAdvertisementPacket=" + this.f26088e + ")";`
- `sources/C6/j.java:705`
  `AbstractC1838t.g(uuid, "characteristicUuid");`
- `sources/C6/j.java:706`
  `AbstractC1838t.g(uuid2, "serviceUUID");`
- `sources/C6/t.java:31`
  `AbstractC1838t.g(str2, "serviceUuid");`
- `sources/C6/t.java:32`
  `AbstractC1838t.g(str3, "characteristicUuid");`
- `sources/C6/t.java:85`
  `return "LaunchCharacteristicDetails(deviceName=" + this.f26263a + ", serviceUuid=" + this.f26264b + ", characteristicUuid=" + this.f26265c + ", readableName=" + this.f26266d + ", device=" + this.f26267e + ", service=" + this.f26268f + ")";`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:535`
  `intent.putExtra("com.punchthrough.lightblueexplorer.ui.devicedetails.DeviceDetailActivity.SelectedServiceUuid", String.valueOf(bluetoothGattService != null ? bluetoothGattService.getUuid() : null));`
- `sources/com/punchthrough/lightblueexplorer/ui/characteristicdetail/b.java:387`
  `AbstractC1838t.f(uuid, "$characteristicUUID");`
- `sources/com/punchthrough/lightblueexplorer/ui/characteristicdetail/CharacteristicDetailActivity.java:47`
  `@Metadata(d1 = {"\u0000T\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003...`
- `sources/com/punchthrough/lightblueexplorer/ui/characteristicdetail/CharacteristicDetailActivity.java:781`
  `public boolean K0(UUID characteristicUuid) {`
- `sources/com/punchthrough/lightblueexplorer/ui/characteristicdetail/CharacteristicDetailActivity.java:782`
  `AbstractC1838t.g(characteristicUuid, "characteristicUuid");`
- `sources/com/punchthrough/lightblueexplorer/ui/characteristicdetail/CharacteristicDetailActivity.java:783`
  `return AbstractC1838t.b(characteristicUuid, S0().M());`
- `sources/com/punchthrough/lightblueexplorer/ui/devicedetails/DeviceDetailActivity.java:1074`
  `intent.putExtra("com.punchthrough.lightblueexplorer.ui.devicedetails.DeviceDetailActivity.SelectedServiceUuid", launchData.f());`
- `sources/H5/b0.java:96`
  `return "PeripheralScanResult(txPower=" + this.f7173a + ", localName=" + this.f7174b + ", advertisingPacketRawBytes=" + this.f7175c + ", advertiseFlagsDescription=" + this.f7176d + ", serviceUuids=" + this.f7177e + ", manufacturerSpecificData=" + this.f7178f + ", serviceData=" + this.f7179g + ")";`
- `sources/J5/AbstractC1758h.java:83`
  `AbstractC1838t.g(uuid, "characteristicUuid");`
- `sources/J5/AbstractC1758h.java:84`
  `AbstractC1838t.g(uuid2, "serviceUuid");`
- `sources/J5/AbstractC1758h.java:125`
  `AbstractC1838t.g(uuid2, "characteristicUuid");`
- `sources/J5/AbstractC1758h.java:126`
  `AbstractC1838t.g(uuid3, "serviceUuid");`
- `sources/J5/B.java:22`
  `AbstractC1838t.g(uuid, "characteristicUuid");`
- `sources/J5/B.java:23`
  `AbstractC1838t.g(uuid2, "serviceUuid");`
- `sources/J5/B.java:58`
  `return "DisableNotifications(device=" + this.f7897a + ", characteristicUuid=" + this.f7898b + ", serviceUuid=" + this.f7899c + ")";`
- `sources/J5/C1753c.java:73`
  `AbstractC1838t.g(uuid2, "characteristicUuid");`
- `sources/J5/C1753c.java:74`
  `AbstractC1838t.g(uuid3, "serviceUuid");`
- `sources/J5/C1753c.java:98`
  `AbstractC1838t.g(uuid2, "serviceUuid");`
- `sources/J5/C1754d.java:363`
  `UUID uuidFromString = UUID.fromString("00002902-0000-1000-8000-00805F9B34FB");`
- `sources/J5/C1754d.java:399`
  `BluetoothGattDescriptor descriptor2 = bluetoothGattCharacteristicO4.getDescriptor(UUID.fromString("00002902-0000-1000-8000-00805F9B34FB"));`
- `sources/J5/D.java:22`
  `AbstractC1838t.g(uuid, "characteristicUuid");`
- `sources/J5/D.java:23`
  `AbstractC1838t.g(uuid2, "serviceUuid");`
- `sources/J5/D.java:58`
  `return "EnableNotifications(device=" + this.f7901a + ", characteristicUuid=" + this.f7902b + ", serviceUuid=" + this.f7903c + ")";`
- `sources/J5/F.java:40`
  `f7907c = AbstractC1190s.p(f9.d("1812"), f9.d("FFFD"), f9.d("1844"), f9.d("1845"), f9.d("1843"), f9.d("1850"), f9.d("184E"), f9.d("184F"), f9.d("1854"), f9.d("1846"), UUID.fromString("AB5E0001-5A21-4F05-BC7D-AF01F617B664"), f9.d("1800"), f9.d("1801"));`
- `sources/J5/r.java:22`
  `AbstractC1838t.g(uuid, "characteristicUuid");`
- `sources/J5/r.java:23`
  `AbstractC1838t.g(uuid2, "serviceUuid");`
- `sources/J5/r.java:58`
  `return "CharacteristicRead(device=" + this.f8007a + ", characteristicUuid=" + this.f8008b + ", serviceUuid=" + this.f8009c + ")";`
- `sources/J5/s.java:29`
  `AbstractC1838t.g(uuid, "characteristicUuid");`
- `sources/J5/s.java:30`
  `AbstractC1838t.g(uuid2, "serviceUuid");`
- `sources/J5/s.java:77`
  `return "CharacteristicWrite(device=" + this.f8010a + ", characteristicUuid=" + this.f8011b + ", serviceUuid=" + this.f8012c + ", writeType=" + this.f8013d + ", payload=" + Arrays.toString(this.f8014e) + ")";`
- `sources/J5/x.java:26`
  `AbstractC1838t.g(uuid2, "characteristicUuid");`
- `sources/J5/x.java:27`
  `AbstractC1838t.g(uuid3, "serviceUuid");`
- `sources/J5/x.java:67`
  `return "DescriptorRead(device=" + this.f8028a + ", descriptorUuid=" + this.f8029b + ", characteristicUuid=" + this.f8030c + ", serviceUuid=" + this.f8031d + ")";`

## BR069

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/J5/C1754d.java:1377`
  `BluetoothDevice device = bluetoothGatt.getDevice();`
- `sources/J5/C1754d.java:1482`
  `BluetoothDevice device = bluetoothGatt.getDevice();`

## BR070

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/J5/F.java:42`
  `f7909e = E6.N.k(D6.C.a(f9.d("1811"), "Alert Notification Service"), D6.C.a(f9.d("1843"), "Audio Input Control"), D6.C.a(f9.d("184E"), "Audio Stream Control"), D6.C.a(f9.d("183D"), "Authorization Control"), D6.C.a(f9.d("1815"), "Automation IO"), D6.C.a(f9.d("1851"), "Basic Audio Announcement"), D6.C....`
- `sources/J5/F.java:43`
  `f7910f = E6.N.k(D6.C.a(f9.d("2C06"), "Acceleration"), D6.C.a(f9.d("2B33"), "ACS Control Point"), D6.C.a(f9.d("2B30"), "ACS Data In"), D6.C.a(f9.d("2B32"), "ACS Data Out Indicate"), D6.C.a(f9.d("2B31"), "ACS Data Out Notify"), D6.C.a(f9.d("2B2F"), "ACS Status"), D6.C.a(f9.d("2BDC"), "Active Preset In...`

## BR073

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/androidx/compose/ui/platform/C2195j0.java:20`
  `byte[] bArrDecode = Base64.decode(str, 0);`
- `sources/androidx/compose/ui/platform/C2195j0.java:21`
  `parcelObtain.unmarshall(bArrDecode, 0, bArrDecode.length);`
- `sources/androidx/compose/ui/platform/r.java:2386`
  `public void onVirtualViewTranslationResponses(LongSparseArray longSparseArray) {`
- `sources/androidx/compose/ui/platform/r.java:2388`
  `bVar.v(bVar, longSparseArray);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:595`
  `int i11 = Integer.parseInt(strArrSplit[0]);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:596`
  `int i12 = Integer.parseInt(strArrSplit[1]);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:597`
  `int i13 = Integer.parseInt(strArrSplit[2]);`
- `sources/androidx/constraintlayout/widget/ConstraintLayout.java:606`
  `float f12 = i15 + ((int) ((Integer.parseInt(strArrSplit[3]) / 1920.0f) * height));`
- `sources/androidx/constraintlayout/widget/e.java:1581`
  `float f9 = Float.parseFloat(strTrim2);`
- `sources/androidx/core/graphics/drawable/a.java:30`
  `static void d(Drawable drawable, Resources resources, XmlPullParser xmlPullParser, AttributeSet attributeSet, Resources.Theme theme) throws XmlPullParserException, IOException {`
- `sources/androidx/core/graphics/drawable/a.java:31`
  `drawable.inflate(resources, xmlPullParser, attributeSet, theme);`
- `sources/androidx/datastore/preferences/protobuf/AbstractC2302w.java:116`
  `GET_PARSER`
- `sources/androidx/emoji2/text/n.java:4`
  `import android.util.SparseArray;`
- `sources/androidx/lifecycle/M.java:26`
  `private static final Class[] f23618g = {Boolean.TYPE, boolean[].class, Double.TYPE, double[].class, Integer.TYPE, int[].class, Long.TYPE, long[].class, String.class, String[].class, Binder.class, Bundle.class, Byte.TYPE, byte[].class, Character.TYPE, char[].class, CharSequence.class, CharSequence[]....`
- `sources/androidx/profileinstaller/h.java:75`
  `str = "RESULT_PARSE_EXCEPTION";`
- `sources/androidx/profileinstaller/m.java:473`
  `throw e.c("Read too much data during profile line parse");`
- `sources/androidx/vectordrawable/graphics/drawable/f.java:348`
  `ColorStateList colorStateListG = k.g(typedArray, xmlPullParser, theme, "tint", 1);`
- `sources/androidx/vectordrawable/graphics/drawable/f.java:352`
  `hVar.f24691e = k.e(typedArray, xmlPullParser, "autoMirrored", 5, hVar.f24691e);`
- `sources/androidx/vectordrawable/graphics/drawable/f.java:353`
  `gVar.f24681k = k.j(typedArray, xmlPullParser, "viewportWidth", 7, gVar.f24681k);`
- `sources/androidx/vectordrawable/graphics/drawable/f.java:354`
  `float fJ = k.j(typedArray, xmlPullParser, "viewportHeight", 8, gVar.f24682l);`
- `sources/androidx/vectordrawable/graphics/drawable/f.java:357`
  `throw new XmlPullParserException(typedArray.getPositionDescription() + "<vector> tag requires viewportWidth > 0");`
- `sources/androidx/vectordrawable/graphics/drawable/f.java:360`
  `throw new XmlPullParserException(typedArray.getPositionDescription() + "<vector> tag requires viewportHeight > 0");`
- `sources/androidx/vectordrawable/graphics/drawable/f.java:366`
  `throw new XmlPullParserException(typedArray.getPositionDescription() + "<vector> tag requires width > 0");`
- `sources/androidx/vectordrawable/graphics/drawable/f.java:369`
  `throw new XmlPullParserException(typedArray.getPositionDescription() + "<vector> tag requires height > 0");`
- `sources/androidx/vectordrawable/graphics/drawable/f.java:371`
  `gVar.setAlpha(k.j(typedArray, xmlPullParser, "alpha", 4, gVar.getAlpha()));`
- `sources/B1/AbstractC2395c.java:47`
  `throw new XmlPullParserException(typedArrayK.getPositionDescription() + "<VectorGraphic> tag requires viewportWidth > 0");`
- `sources/B1/AbstractC2395c.java:50`
  `throw new XmlPullParserException(typedArrayK.getPositionDescription() + "<VectorGraphic> tag requires viewportHeight > 0");`
- `sources/com/google/android/datatransport/runtime/scheduling/jobscheduling/AlarmManagerSchedulerBroadcastReceiver.java:26`
  `aVarD.c(Base64.decode(queryParameter2, 0));`
- `sources/com/google/android/datatransport/runtime/scheduling/jobscheduling/JobInfoSchedulerService.java:21`
  `aVarD.c(Base64.decode(string2, 0));`
- `sources/com/google/android/gms/internal/mlkit_vision_barcode_bundled/AbstractC2875y0.java:238`
  `throw new C2861v1("Failed to parse the message.");`
- `sources/com/google/android/gms/internal/mlkit_vision_barcode_bundled/AbstractC2875y0.java:394`
  `throw new C2861v1("Failed to parse the message.");`
- `sources/com/google/android/gms/measurement/internal/C2999q2.java:164`
  `h().E().c("Failed to parse URL. Not uploading MeasurementBatch. appId", C2978n2.t(str2), i52.b());`
- `sources/com/google/android/gms/measurement/internal/F2.java:48`
  `Bundle bundleA2 = e22.f28335a.J().A(Uri.parse("?" + string), z9);`
- `sources/com/google/android/gms/measurement/internal/H5.java:1223`
  `h().J().b("Failed to parse locally stored ad campaign info. appId", C2978n2.t(c2901c2.l()));`
- `sources/com/google/android/gms/measurement/internal/I2.java:262`
  `h().I().c("Parsed config. version, gmp_app_id", t12.Z() ? Long.valueOf(t12.I()) : null, t12.X() ? t12.P() : null);`
- `sources/com/google/android/gms/measurement/internal/S2.java:566`
  `h().E().b("Failed to parse the Deferred Deep Link response. exception", e9);`
- `sources/D8/a.java:29`
  `AbstractC1838t.g(eVar, "decoder");`
- `sources/F7/a.java:37`
  `objArr[1] = "decodeBytes";`
- `sources/F7/a.java:45`
  `objArr[1] = "decode7to8";`
- `sources/F7/a.java:66`
  `objArr[2] = "decodeBytes";`
- `sources/F7/a.java:75`
  `objArr[2] = "decode7to8";`
- `sources/F7/i.java:74`
  `AbstractC1838t.f(bArrE, "decodeBytes(data)");`
- `sources/F7/i.java:87`
  `AbstractC1838t.f(eVarD, "parseDelimitedFrom(this, EXTENSION_REGISTRY)");`
- `sources/F7/i.java:102`
  `AbstractC1838t.f(bArrE, "decodeBytes(data)");`
- `sources/G4/c.java:48`
  `this.f5659c.l("Failed to parse settings JSON from " + this.f5657a, e9);`
- `sources/I2/C3473h.java:19`
  `private static volatile X PARSER = null;`
- `sources/I3/M.java:574`
  `return Base64.decode(str, 0);`
- `sources/I8/C1734i.java:32`
  `AbstractC1838t.g(eVar, "decoder");`
- `sources/I8/m0.java:28`
  `AbstractC1838t.g(cVar, "decoder");`
- `sources/I8/n0.java:34`
  `AbstractC1838t.g(eVar, "decoder");`
- `sources/K5/c.java:76`
  `SparseArray sparseArrayH = h();`
- `sources/K5/c.java:77`
  `int size = sparseArrayH.size();`
- `sources/K5/c.java:79`
  `int iKeyAt = sparseArrayH.keyAt(i9);`
- `sources/K5/c.java:80`
  `byte[] bArr = (byte[]) sparseArrayH.valueAt(i9);`
- `sources/K5/c.java:117`
  `public SparseArray h() {`
- `sources/K5/c.java:118`
  `SparseArray<byte[]> manufacturerSpecificData = this.f8335a.getManufacturerSpecificData();`
- `sources/K5/c.java:119`
  `return manufacturerSpecificData == null ? new SparseArray() : manufacturerSpecificData;`
- `sources/K8/n.java:60`
  `AbstractC1770a.y(abstractC1770a, "Failed to parse type 'ULong' for input '" + strS + '\'', 0, null, 6, null);`
- `sources/K8/n.java:72`
  `AbstractC1770a.y(abstractC1770a, "Failed to parse type 'UByte' for input '" + strS + '\'', 0, null, 6, null);`
- `sources/K8/z.java:404`
  `AbstractC1770a.y(this.f8532c, "Failed to parse byte for input '" + jO + '\'', 0, null, 6, null);`
- `sources/N5/b.java:100`
  `String string = Integer.toString(Integer.parseInt(str, AbstractC3708a.a(2)), AbstractC3708a.a(8));`
- `sources/N5/m.java:68`
  `int iFloatToRawIntBits = Float.floatToRawIntBits(Float.parseFloat(str));`
- `sources/N5/m.java:74`
  `long jDoubleToRawLongBits = Double.doubleToRawLongBits(Double.parseDouble(str));`
- `sources/N5/m.java:88`
  `bArr[i10] = (byte) Integer.parseInt(new String(AbstractC1184l.r(charArray, i9, i11)), AbstractC3708a.a(16));`
- `sources/N5/m.java:124`
  `return new byte[]{Byte.parseByte(str)};`
- `sources/N5/m.java:127`
  `short s9 = Short.parseShort(str);`
- `sources/N5/m.java:131`
  `int i10 = Integer.parseInt(str);`
- `sources/N5/m.java:137`
  `long j9 = Long.parseLong(str);`
- `sources/P0/b.java:20`
  `import android.util.LongSparseArray;`
- `sources/P0/b.java:120`
  `private final void b(b bVar, LongSparseArray longSparseArray) {`
- `sources/P0/b.java:127`
  `L lA = V1.c.a(longSparseArray);`
- `sources/P0/b.java:130`
  `ViewTranslationResponse viewTranslationResponseA = h.a(longSparseArray.get(jB));`
- `sources/P0/b.java:137`
  `public static final void e(b bVar, LongSparseArray longSparseArray) {`
- `sources/P0/b.java:209`
  `public final void d(final b bVar, final LongSparseArray<ViewTranslationResponse> longSparseArray) {`
- `sources/P0/b.java:214`
  `b(bVar, longSparseArray);`
- `sources/P1/e.java:30`
  `private static final C2112d b(Resources.Theme theme, Resources resources, int i9, int i10, InterfaceC1059m interfaceC1059m, int i11) throws XmlPullParserException, IOException {`
- `sources/R4/g.java:12`
  `private static final byte f11877a = Byte.parseByte("01110000", 2);`
- `sources/R4/g.java:15`
  `private static final byte f11878b = Byte.parseByte("00001111", 2);`
- `sources/R5/a.java:150`
  `d9.a.f31145a.i("parseChunk " + i9 + " to " + i10, new Object[0]);`
- `sources/t/M0.java:576`
  `int i9 = Integer.parseInt(this.f40599i);`

## BR074

paper_id: B028
paper_title: A Study of the Feasibility of Co-located App Attacks against BLE and a Large-Scale Analysis of the Current Application-Layer Security Landscape

- `sources/A0/C2103u.java:198`
  `int iSave = canvasD.save();`
- `sources/A0/C2103u.java:201`
  `canvasD.restoreToCount(iSave);`
- `sources/androidx/appcompat/app/h.java:459`
  `return powerManager.isPowerSaveMode();`
- `sources/androidx/appcompat/widget/C2163w.java:22`
  `protected synchronized void onMeasure(int i9, int i10) {`
- `sources/androidx/appcompat/widget/C2166z.java:99`
  `int iSave = canvas.save();`
- `sources/androidx/appcompat/widget/C2166z.java:105`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/appcompat/widget/E.java:319`
  `synchronized (rectF) {`
- `sources/androidx/appcompat/widget/SwitchCompat.java:709`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/camera/core/d.java:54`
  `synchronized (this.f19069b) {`
- `sources/androidx/camera/core/d.java:63`
  `synchronized (this.f19069b) {`
- `sources/androidx/camera/core/r.java:48`
  `synchronized (this.f19165z) {`
- `sources/androidx/core/widget/NestedScrollView.java:1000`
  `int iSave = canvas.save();`
- `sources/androidx/core/widget/NestedScrollView.java:1019`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/core/widget/NestedScrollView.java:1024`
  `int iSave2 = canvas.save();`
- `sources/androidx/core/widget/NestedScrollView.java:1042`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/emoji2/text/k.java:136`
  `synchronized (this.f23100d) {`
- `sources/androidx/fragment/app/v.java:1882`
  `Log.v("FragmentManager", "saveAllState: no fragments!");`
- `sources/androidx/recyclerview/widget/RecyclerView.java:5016`
  `int iSave = canvas.save();`
- `sources/androidx/recyclerview/widget/RecyclerView.java:5022`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/recyclerview/widget/RecyclerView.java:5047`
  `int iSave4 = canvas.save();`
- `sources/androidx/vectordrawable/graphics/drawable/f.java:433`
  `int iSave = canvas.save();`
- `sources/androidx/work/impl/P.java:212`
  `synchronized (f24805n) {`
- `sources/androidx/work/impl/P.java:233`
  `synchronized (f24805n) {`
- `sources/B0/C1072t.java:1063`
  `synchronized (this.f1635z) {`
- `sources/C/AbstractActivityC2463j.java:436`
  `if (!AbstractC1838t.b(e9.getMessage(), "Can not perform this action after onSaveInstanceState")) {`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:188`
  `f26946h = c2680q3E.b("measurement.upload.debug_upload_interval", 1000L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:192`
  `f26949k = c2680q3E.b("measurement.upload.google_signal_max_queue_time", 605000L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:196`
  `f26953o = c2680q3E.b("measurement.upload.max_event_parameter_value_length", 500L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:200`
  `f26957s = c2680q3E.b("measurement.upload.max_item_scoped_custom_parameters", 27L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:205`
  `f26962x = c2680q3E.b("measurement.upload.minimum_delay", 500L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:209`
  `f26909B = c2680q3E.b("measurement.upload.realtime_upload_interval", 10000L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:210`
  `f26910C = c2680q3E.b("measurement.upload.refresh_blacklisted_config_interval", 604800000L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:215`
  `f26913F = c2680q3E.b("measurement.upload.stale_data_deletion_interval", 86400000L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:223`
  `f26921N = c2680q3E.b("measurement.upload.backoff_period", 43200000L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:224`
  `f26922O = c2680q3E.b("measurement.upload.initial_upload_delay_time", 15000L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:225`
  `f26923P = c2680q3E.b("measurement.upload.interval", 3600000L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:226`
  `f26924Q = c2680q3E.b("measurement.upload.max_bundle_size", 65536L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:227`
  `f26925R = c2680q3E.b("measurement.upload.max_bundles", 100L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:228`
  `f26926S = c2680q3E.b("measurement.upload.max_conversions_per_day", 500L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:229`
  `f26927T = c2680q3E.b("measurement.upload.max_error_events_per_day", 1000L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:230`
  `f26928U = c2680q3E.b("measurement.upload.max_events_per_bundle", 1000L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:231`
  `f26929V = c2680q3E.b("measurement.upload.max_events_per_day", 100000L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:232`
  `f26930W = c2680q3E.b("measurement.upload.max_public_events_per_day", 50000L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:233`
  `f26931X = c2680q3E.b("measurement.upload.max_queue_time", 518400000L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:234`
  `f26932Y = c2680q3E.b("measurement.upload.max_realtime_events_per_day", 10L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:235`
  `f26933Z = c2680q3E.b("measurement.upload.max_batch_size", 65536L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:236`
  `f26935a0 = c2680q3E.b("measurement.upload.retry_count", 6L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:237`
  `f26937b0 = c2680q3E.b("measurement.upload.retry_time", 1800000L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:238`
  `f26939c0 = c2680q3E.c("measurement.upload.url", "https://app-measurement.com/a");`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:239`
  `f26941d0 = c2680q3E.b("measurement.upload.window_interval", 3600000L);`
- `sources/com/google/android/gms/internal/measurement/C2719v3.java:125`
  `synchronized (this.f27328d) {`
- `sources/com/google/android/gms/internal/measurement/G1.java:29`
  `((P0) AbstractC4310p.l(C2573e1.this.f26989i)).onActivitySaveInstanceState(A3.b.e0(this.f26592A), this.f26593B, this.f26991x);`
- `sources/com/google/android/gms/internal/measurement/M2.java:47`
  `synchronized (this) {`
- `sources/com/google/android/gms/internal/measurement/M6.java:7`
  `private static final AbstractC2611i3 f26679a = new C2680q3(AbstractC2620j3.a("com.google.android.gms.measurement")).f().e().d("measurement.fix_origin_in_upload_utils.service", true);`
- `sources/com/google/android/gms/internal/measurement/Q0.java:57`
  `synchronized (this.f26703b) {`
- `sources/com/google/android/gms/internal/measurement/Q0.java:80`
  `synchronized (this.f26703b) {`
- `sources/com/google/android/gms/internal/measurement/R0.java:173`
  `public final void onActivitySaveInstanceState(A3.a aVar, U0 u02, long j9) {`
- `sources/com/google/android/gms/internal/measurement/S0.java:290`
  `onActivitySaveInstanceState(aVarD10, w07, j28);`
- `sources/com/google/android/gms/internal/measurement/s7.java:27`
  `f27284e = c2680q3E.d("measurement.sgtm.upload_queue", false);`
- `sources/com/google/android/gms/internal/mlkit_vision_barcode_bundled/i4.java:135`
  `PROVIDER_GOOGLE_GEO_DATA_UPLOAD(286732409),`
- `sources/com/google/android/gms/measurement/AppMeasurement.java:115`
  `synchronized (AppMeasurement.class) {`
- `sources/com/google/android/gms/measurement/internal/AbstractC3016t.java:33`
  `synchronized (AbstractC3016t.class) {`
- `sources/com/google/android/gms/measurement/internal/AppMeasurementDynamiteService.java:286`
  `public void onActivitySaveInstanceState(A3.a aVar, com.google.android.gms.internal.measurement.U0 u02, long j9) {`
- `sources/com/google/android/gms/measurement/internal/AppMeasurementDynamiteService.java:292`
  `activityLifecycleCallbacksN0.onActivitySaveInstanceState((Activity) A3.b.f(aVar), bundle);`
- `sources/com/google/android/gms/measurement/internal/AppMeasurementDynamiteService.java:331`
  `synchronized (this.f28276c) {`
- `sources/com/google/android/gms/measurement/internal/AppMeasurementDynamiteService.java:446`
  `synchronized (this.f28276c) {`
- `sources/com/google/android/gms/measurement/internal/C2953j5.java:53`
  `this.f29020h = new A2(c3061z2F4, "last_upload", 0L);`
- `sources/com/google/android/gms/measurement/internal/C2953j5.java:56`
  `this.f29021i = new A2(c3061z2F5, "last_upload_attempt", 0L);`
- `sources/com/google/android/gms/measurement/internal/C2954k.java:48`
  `private static final String[] f29033h = {"app_version", "ALTER TABLE apps ADD COLUMN app_version TEXT;", "app_store", "ALTER TABLE apps ADD COLUMN app_store TEXT;", "gmp_version", "ALTER TABLE apps ADD COLUMN gmp_version INTEGER;", "dev_cert_hash", "ALTER TABLE apps ADD COLUMN dev_cert_hash INTEGER;...`
- `sources/com/google/android/gms/measurement/internal/C2954k.java:883`
  `cursorQuery = z().query("apps", new String[]{"app_instance_id", "gmp_app_id", "resettable_device_id_hash", "last_bundle_index", "last_bundle_start_timestamp", "last_bundle_end_timestamp", "app_version", "app_store", "gmp_version", "dev_cert_hash", "measurement_enabled", "day", "daily_public_events_c...`
- `sources/com/google/android/gms/measurement/internal/C2954k.java:2285`
  `if (m0() && (iDelete = z().delete("upload_queue", x0(), new String[0])) > 0) {`
- `sources/com/google/android/gms/measurement/internal/C2954k.java:2286`
  `h().I().b("Deleted stale MeasurementBatch rows from upload_queue. rowsDeleted", Integer.valueOf(iDelete));`
- `sources/com/google/android/gms/measurement/internal/C2954k.java:2298`
  `contentValues.put("upload_uri", str2);`
- `sources/com/google/android/gms/measurement/internal/C2954k.java:2316`
  `if (z().insert("upload_queue", null, contentValues) != -1) {`
- `sources/com/google/android/gms/measurement/internal/C2954k.java:2319`
  `h().E().b("Failed to insert MeasurementBatch (got -1) to upload_queue. appId", str);`
- `sources/com/google/android/gms/measurement/internal/C2954k.java:2322`
  `h().E().c("Error storing MeasurementBatch to upload_queue. appId", str, e9);`
- `sources/com/google/android/gms/measurement/internal/C2964l2.java:45`
  `public final synchronized void b(int i9, int i10, long j9, long j10, int i11) {`
- `sources/com/google/android/gms/measurement/internal/C2967l5.java:38`
  `if ("com.google.android.gms.measurement.UPLOAD".equals(action)) {`
- `sources/com/google/android/gms/measurement/internal/C2967l5.java:68`
  `c2978n2.I().b("Local AppMeasurementService processed last upload request. StartId", Integer.valueOf(i9));`
- `sources/com/google/android/gms/measurement/internal/C2967l5.java:75`
  `c2978n2.I().a("AppMeasurementJobService processed last upload request.");`

## BR075

paper_id: B029
paper_title: Who?s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy

- `sources/androidx/appcompat/widget/D.java:82`
  `D.super.setAutoSizeTextTypeUniformWithPresetSizes(iArr, i9);`
- `sources/androidx/constraintlayout/widget/i.java:1179`
  `public static final int[] f22009n = {android.R.attr.textAppearance, R.attr.autoSizeMaxTextSize, R.attr.autoSizeMinTextSize, R.attr.autoSizePresetSizes, R.attr.autoSizeStepGranularity, R.attr.autoSizeTextType, R.attr.drawableBottomCompat, R.attr.drawableEndCompat, R.attr.drawableLeftCompat, R.attr.dr...`
- `sources/com/google/android/gms/internal/measurement/P0.java:70`
  `void resetAnalyticsData(long j9);`
- `sources/com/google/android/gms/internal/measurement/S0.java:149`
  `resetAnalyticsData(j16);`
- `sources/com/google/android/gms/measurement/internal/AppMeasurementDynamiteService.java:346`
  `public void resetAnalyticsData(long j9) {`
- `sources/com/google/android/gms/measurement/internal/C2954k.java:883`
  `cursorQuery = z().query("apps", new String[]{"app_instance_id", "gmp_app_id", "resettable_device_id_hash", "last_bundle_index", "last_bundle_start_timestamp", "last_bundle_end_timestamp", "app_version", "app_store", "gmp_version", "dev_cert_hash", "measurement_enabled", "day", "daily_public_events_c...`
- `sources/com/google/android/gms/measurement/internal/C3035v4.java:55`
  `h().D().b("Generating ScionPayload disabled. packageName", str);`
- `sources/com/google/android/gms/measurement/internal/C3035v4.java:59`
  `h().D().c("Generating a payload for this event is not available. package_name, event_name", str, e9.f28331w);`
- `sources/com/google/android/gms/measurement/internal/C3035v4.java:234`
  `h().D().b("Resettable device id encryption failed", e11.getMessage());`
- `sources/com/google/android/gms/measurement/internal/N4.java:24`
  `this.f28625x.h().E().a("Failed to reset data on the service: not connected to service");`
- `sources/com/google/android/gms/measurement/internal/r.java:60`
  `AbstractC3023u.c(this.f29165w.h(), sQLiteDatabase, "apps", "CREATE TABLE IF NOT EXISTS apps ( app_id TEXT NOT NULL, app_instance_id TEXT, gmp_app_id TEXT, resettable_device_id_hash TEXT, last_bundle_index INTEGER NOT NULL, last_bundle_end_timestamp INTEGER NOT NULL, PRIMARY KEY (app_id)) ;", "app_id...`
- `sources/com/google/android/gms/measurement/internal/Z5.java:749`
  `Y(sb, 1, "resettable_device_id", c2671p2.h0());`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:56`
  `@Metadata(d1 = {"\u0000Û\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u000b\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0004\n\u0002\u0010\u0012\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u000e\n\u0002\u0010 \n\u0002\u0018\...`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:593`
  `e.a.a(Q1(), Q5.b.f11757w, "Attempting to write ASCII payload of " + text, Q5.c.f11769x, 0L, O1(), null, null, null, null, 488, null);`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:646`
  `private final boolean G2(byte[] payload) {`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:648`
  `byte[] bArrH = aVar != null ? aVar.h(payload, (byte) 83) : null;`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:671`
  `private final boolean H2(byte[] payload) {`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:678`
  `N1().d(O1(), bluetoothGattCharacteristic, payload);`
- `sources/com/punchthrough/lightblueexplorer/R.java:168`
  `public static final int autoSizePresetSizes = 0x7f040049;`
- `sources/com/punchthrough/lightblueexplorer/R.java:4611`
  `public static final int invalid_hex_payload = 0x7f13016f;`
- `sources/com/punchthrough/lightblueexplorer/R.java:4894`
  `public static final int onboarding_reset_hard_explanation = 0x7f13028a;`
- `sources/com/punchthrough/lightblueexplorer/R.java:4895`
  `public static final int onboarding_reset_soft_explanation = 0x7f13028b;`
- `sources/com/punchthrough/lightblueexplorer/R.java:4903`
  `public static final int payload_exceeds_byte_limit = 0x7f130293;`
- `sources/com/punchthrough/lightblueexplorer/R.java:4955`
  `public static final int reset_banners = 0x7f1302c7;`
- `sources/com/punchthrough/lightblueexplorer/R.java:4956`
  `public static final int reset_onboarding = 0x7f1302c8;`
- `sources/com/punchthrough/lightblueexplorer/ui/characteristicdetail/b.java:1035`
  `bVar.o("Writing to characteristic %s, payload: %s", bluetoothGattCharacteristic3.getUuid(), N5.b.h(bArr, " ", ""));`
- `sources/G1/C3257I.java:9`
  `super("Pointer input was reset");`
- `sources/h/AbstractC3353j.java:646`
  `public static final int[] f34015g0 = {android.R.attr.textAppearance, R.attr.autoSizeMaxTextSize, R.attr.autoSizeMinTextSize, R.attr.autoSizePresetSizes, R.attr.autoSizeStepGranularity, R.attr.autoSizeTextType, R.attr.drawableBottomCompat, R.attr.drawableEndCompat, R.attr.drawableLeftCompat, R.attr.d...`
- `sources/H3/C3392r.java:98`
  `c3392r.f34433i.d(((Integer) r0.getValue()).intValue(), C3085c.b.INVALID_PAYLOD, (String) ((Map.Entry) it.next()).getKey());`
- `sources/H3/C3392r.java:218`
  `} else if (gVarE.c() == g.a.INVALID_PAYLOAD) {`
- `sources/I3/M.java:413`
  `contentValues.put("payload", z9 ? bArrA : new byte[0]);`
- `sources/I3/M.java:427`
  `sQLiteDatabase.insert("event_payloads", null, contentValues2);`
- `sources/I3/W.java:70`
  `sQLiteDatabase.execSQL("ALTER TABLE events ADD COLUMN payload_encoding TEXT");`
- `sources/I3/W.java:136`
  `sQLiteDatabase.execSQL("CREATE TABLE events (_id INTEGER PRIMARY KEY, context_id INTEGER NOT NULL, transport_name TEXT NOT NULL, timestamp_ms INTEGER NOT NULL, uptime_ms INTEGER NOT NULL, payload BLOB NOT NULL, code INTEGER, num_attempts INTEGER NOT NULL,FOREIGN KEY (context_id) REFERENCES transport...`
- `sources/I3/W.java:165`
  `sQLiteDatabase.execSQL("DROP TABLE IF EXISTS event_payloads");`
- `sources/I3/W.java:166`
  `sQLiteDatabase.execSQL("CREATE TABLE event_payloads (sequence_num INTEGER NOT NULL, event_id INTEGER NOT NULL, bytes BLOB NOT NULL,FOREIGN KEY (event_id) REFERENCES events(_id) ON DELETE CASCADE,PRIMARY KEY (sequence_num, event_id))");`
- `sources/I3/W.java:186`
  `sQLiteDatabase.execSQL("DROP TABLE IF EXISTS event_payloads");`
- `sources/J5/C1754d.java:598`
  `AbstractC1838t.g(bArr, "payload");`
- `sources/J5/F.java:43`
  `f7910f = E6.N.k(D6.C.a(f9.d("2C06"), "Acceleration"), D6.C.a(f9.d("2B33"), "ACS Control Point"), D6.C.a(f9.d("2B30"), "ACS Data In"), D6.C.a(f9.d("2B32"), "ACS Data Out Indicate"), D6.C.a(f9.d("2B31"), "ACS Data Out Notify"), D6.C.a(f9.d("2B2F"), "ACS Status"), D6.C.a(f9.d("2BDC"), "Active Preset In...`
- `sources/J5/K.java:2496`
  `map.put(D6.G.c(D6.G.g(3435)), "Crane Payment Innovations, Inc.");`
- `sources/J5/K.java:3417`
  `map.put(D6.G.c(D6.G.g(2513)), "ABLEPAY TECHNOLOGIES AS");`
- `sources/J5/s.java:77`
  `return "CharacteristicWrite(device=" + this.f8010a + ", characteristicUuid=" + this.f8011b + ", serviceUuid=" + this.f8012c + ", writeType=" + this.f8013d + ", payload=" + Arrays.toString(this.f8014e) + ")";`
- `sources/k6/C3619B.java:462`
  `e.a.a(eVar, bVar, "Received characteristic " + uuid + " write request of payload " + strI + " from device " + address + " on virtual device " + (virtualDevice != null ? virtualDevice.getName() : null), null, 0L, null, null, bluetoothGattCharacteristic, null, bArr, 188, null);`
- `sources/k6/C3619B.java:585`
  `e.a.a(eVar, bVar, "Received descriptor " + uuid + " write request of payload " + strI + " from device " + address + " on virtual device " + (virtualDevice != null ? virtualDevice.getName() : null), null, 0L, null, null, null, bluetoothGattDescriptor, bArr, 124, null);`
- `sources/k6/C3619B.java:1664`
  `e.a.a(eVar, bVar, "Notifying payload " + strI + " to device " + address + " (" + name + ") from virtual device " + (virtualDevice != null ? virtualDevice.getName() : null), null, 0L, null, bluetoothGattService, bluetoothGattCharacteristic, null, bArr, 156, null);`
- `sources/k6/C3619B.java:1847`
  `e.a.a(eVar, bVar, "Indicating payload " + strI + " to device " + address + " (" + name + ") from virtual device " + (virtualDevice != null ? virtualDevice.getName() : null), null, 0L, null, bluetoothGattService, bluetoothGattCharacteristic, null, bArr, 156, null);`
- `sources/O3/k.java:1032`
  `public static final int[] f11069r = {android.R.attr.textAppearance, R.attr.autoSizeMaxTextSize, R.attr.autoSizeMinTextSize, R.attr.autoSizePresetSizes, R.attr.autoSizeStepGranularity, R.attr.autoSizeTextType, R.attr.drawableBottomCompat, R.attr.drawableEndCompat, R.attr.drawableLeftCompat, R.attr.dr...`
- `sources/P8/L.java:155`
  `throw new UnsupportedOperationException("MutableStateFlow.resetReplayCache is not supported");`
- `sources/S8/f.java:897`
  `q0(new g("OkHttp %s Push Reset[%s]", new Object[]{this.f12428z, Integer.valueOf(i9)}, i9, bVar));`
- `sources/t/K.java:1534`
  `dVarD.a(c02, C0.g.SESSION_ERROR_SURFACE_NEEDS_RESET);`

## BR076

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:31`
  `<uses-feature android:name="android.hardware.camera"/>`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:32`
  `<uses-feature`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:35`
  `<uses-feature`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:38`
  `<uses-feature`
- `resources/com.punchthrough.lightblueexplorer.apk/AndroidManifest.xml:75`
  `android:name="com.punchthrough.lightblueexplorer.ui.launch.LaunchActivity"`
- `resources/res/values/strings.xml:60`
  `<string name="advertisement_data_tooltip">Before a connection is established, BLE devices broadcast advertisement packets. These packets are made up of various advertisement data structures that provide information about the device, such as the device’s connectivity status, signal strength, and name...`
- `resources/res/values/strings.xml:70`
  `<string name="apache_license">Apache License\n\n Version 2.0, January 2004\n\n http://www.apache.org/licenses/\n\n TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION\n\n 1. Definitions.\n\n \"License\" shall mean the terms and conditions for use, reproduction, and distribution as defined b...`
- `resources/res/values/strings.xml:92`
  `<string name="banner_manage_connections_message">When should you advertise? Request connections? Disconnect? See our Ultimate Guide to Managing your BLE Connection.</string>`
- `resources/res/values/strings.xml:146`
  `<string name="cannot_launch_app_settings">Unable to launch app settings, please navigate to app settings manually</string>`
- `resources/res/values/strings.xml:174`
  `<string name="cloud_connect_tooltip">This feature allows you to listen for BLE notifications or indications and send this stream of data to the supported cloud platform, Adafruit IO. You\'ll be prompted for your platform API credentials if you enable the feature.</string>`
- `resources/res/values/strings.xml:270`
  `<string name="endianness_tooltip">Determines the order of bytes in memory. In big-endian format, the most significant byte is stored first at the lowest memory address. In little-endian format, the least significant byte is stored first.</string>`
- `resources/res/values/strings.xml:281`
  `<string name="existing_characteristic_uuid">This field contains a duplicate characteristic UUID, which is not currently supported within the same service.</string>`
- `resources/res/values/strings.xml:282`
  `<string name="existing_service_uuid">This field contains a duplicate service UUID, which is not currently supported within the same device.</string>`
- `resources/res/values/strings.xml:296`
  `<string name="field_cannot_be_empty">The field cannot be empty</string>`
- `resources/res/values/strings.xml:304`
  `<string name="first_name">First Name</string>`
- `resources/res/values/strings.xml:372`
  `<string name="invalid_uuid">The field contains an invalid UUID.</string>`
- `resources/res/values/strings.xml:613`
  `<string name="mtu_updated_text">Request succeeded, current MTU is %d</string>`
- `resources/res/values/strings.xml:614`
  `<string name="multidisciplinary_services_description">Component integration is no small feat. Our multi-disciplinary team works seamlessly across the areas of expertise needed to take a project from concept to product launch.</string>`
- `resources/res/values/strings.xml:653`
  `<string name="onboarding_reset_hard_explanation">Onboarding will be shown again on next launch, and you will be seen as a new user.</string>`
- `resources/res/values/strings.xml:654`
  `<string name="onboarding_reset_soft_explanation">Onboarding will be shown again on next launch, and you will be seen as an existing user.</string>`
- `resources/res/values/strings.xml:678`
  `<string name="populated_field_with_payload">Populated field with selected payload</string>`
- `resources/res/values/strings.xml:700`
  `<string name="raw_advertisement_packet_tooltip">The full, unprocessed BLE advertisement data packet before any filtering or parsing by the app.</string>`
- `resources/res/values/strings.xml:709`
  `<string name="request_mtu_error_text">Request failed with error code %1$d, current MTU is %2$d</string>`
- `resources/res/values/strings.xml:711`
  `<string name="request_mtu_title">Request MTU…</string>`
- `resources/res/values/strings.xml:718`
  `<string name="restricted_uuid">The field contains a UUID that is restricted by Android.</string>`
- `resources/res/values/strings.xml:763`
  `<string name="services_list_tooltip">A service is a group of logically related characteristics that often represent a feature of a BLE device, such as a button or sensor. Characteristics are values within services that act as the primary means of data exchange and interaction with the peripheral</st...`
- `resources/res/values/strings.xml:764`
  `<string name="services_tooltip">A service is a group of logically related characteristics that often represent a feature of a BLE device, such as a button or sensor. Characteristics are values within services that act as the primary means of data exchange and interaction with the peripheral.</string...`
- `resources/res/values/strings.xml:855`
  `<string name="virtual_characteristic_uuid_tooltip">Characteristics are identified by their 128-bit UUID (Universally Unique Identifier). Some characteristic UUIDs are standardized and assigned human-readable names by the Bluetooth SIG (Special Interest Group), such as the Manufacturer Name String ch...`
- `resources/res/values/strings.xml:866`
  `<string name="virtual_read_tooltip">Adds the read property to the virtual characteristic when enabled. A read operation is a request from a client to read the current value of a characteristic on the server. This is typically used to retrieve static or infrequently updated data, such as a device\'s ...`
- `resources/res/values/strings.xml:867`
  `<string name="virtual_service_tooltip">The virtual service associated with the virtual characteristic. A service is a group of logically related characteristics that often represent a feature of a BLE device, such as a button or sensor.</string>`
- `resources/res/values/strings.xml:870`
  `<string name="virtual_write_tooltip">Adds the write property to the virtual characteristic when enabled. A write operation is a request from a client to write data to a characteristic on the server. The server then responds to confirm whether the write was successful.</string>`
- `resources/res/values/strings.xml:871`
  `<string name="virtual_write_without_response">Adds the write without response property to the virtual characteristic when enabled. A write without response operation is a request from a client to write data to a characteristic on the server without expecting a response. While faster than a normal wr...`
- `resources/res/values/strings.xml:874`
  `<string name="we_redesigned_app_user_friendly_enable_future_feature_dev">We’ve redesigned and rebuilt the app to be more user friendly. This will enable us to build future feature development.</string>`
- `resources/res/values/strings.xml:898`
  `<string name="written_value_tooltip">A value that was previously written to a characteristic using a write request or command, displayed in the selected format. Tap and hold the cell to copy the value to the clipboard, or tap to write the value to the characteristic again.</string>`
- `sources/A1/C2109a.java:84`
  `AbstractC3533a.b("drawCachedImage must be invoked first before attempting to draw the result into another destination");`
- `sources/a2/a.java:61`
  `throw new IllegalStateException("call to 'resume' before 'invoke' with coroutine");`
- `sources/a2/a.java:96`
  `throw new IllegalStateException("call to 'resume' before 'invoke' with coroutine");`
- `sources/a2/a.java:154`
  `throw new IllegalStateException("call to 'resume' before 'invoke' with coroutine");`
- `sources/a2/a.java:202`
  `throw new IllegalStateException("call to 'resume' before 'invoke' with coroutine");`
- `sources/a2/a.java:244`
  `throw new IllegalStateException("call to 'resume' before 'invoke' with coroutine");`
- `sources/a2/a.java:286`
  `throw new IllegalStateException("call to 'resume' before 'invoke' with coroutine");`
- `sources/a2/a.java:327`
  `AbstractC1838t.g(oVar, "request");`
- `sources/a2/a.java:332`
  `AbstractC1838t.g(pVar, "request");`
- `sources/androidx/appcompat/app/h.java:1197`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR id when requesting this feature.");`
- `sources/androidx/appcompat/app/h.java:1203`
  `Log.i("AppCompatDelegate", "You should now use the AppCompatDelegate.FEATURE_SUPPORT_ACTION_BAR_OVERLAY id when requesting this feature.");`
- `sources/androidx/appcompat/app/h.java:1313`
  `throw new AndroidRuntimeException("Window feature must be requested before adding content");`
- `sources/androidx/compose/foundation/lazy/layout/h.java:90`
  `throw new IllegalStateException("Should not execute nested prefetch on canceled request");`
- `sources/androidx/compose/foundation/lazy/layout/h.java:173`
  `throw new IllegalArgumentException("Callers should check whether the request is still valid before calling performComposition()");`
- `sources/androidx/compose/foundation/lazy/layout/h.java:176`
  `throw new IllegalArgumentException("Request was already composed!");`
- `sources/androidx/compose/foundation/lazy/layout/h.java:185`
  `throw new IllegalArgumentException("Callers should check whether the request is still valid before calling performMeasure()");`
- `sources/androidx/compose/foundation/lazy/layout/h.java:188`
  `throw new IllegalArgumentException("Request was already measured!");`
- `sources/androidx/compose/foundation/lazy/layout/h.java:193`
  `throw new IllegalArgumentException("performComposition() must be called before performMeasure()");`
- `sources/androidx/compose/foundation/lazy/layout/h.java:204`
  `throw new IllegalArgumentException("Should precompose before resolving nested prefetch states");`
- `sources/androidx/core/view/C2278y0.java:10`
  `import java.lang.reflect.Field;`
- `sources/androidx/core/view/C2278y0.java:28`
  `private static Field f22590a;`
- `sources/androidx/core/view/C2278y0.java:31`
  `private static Field f22591b;`
- `sources/androidx/core/view/C2278y0.java:34`
  `private static Field f22592c;`
- `sources/androidx/core/view/C2278y0.java:41`
  `Field declaredField = View.class.getDeclaredField("mAttachInfo");`
- `sources/androidx/core/view/C2278y0.java:45`
  `Field declaredField2 = cls.getDeclaredField("mStableInsets");`
- `sources/androidx/core/view/C2278y0.java:48`
  `Field declaredField3 = cls.getDeclaredField("mContentInsets");`
- `sources/androidx/core/view/C2278y0.java:389`
  `throw new IllegalArgumentException("type needs to be >= FIRST and <= LAST, type=" + i9);`
- `sources/androidx/core/view/C2278y0.java:602`
  `private static Field f22595e = null;`
- `sources/androidx/core/view/C2278y0.java:628`
  `Log.i("WindowInsetsCompat", "Could not retrieve WindowInsets.CONSUMED field", e9);`
- `sources/androidx/core/view/C2278y0.java:632`
  `Field field = f22595e;`
- `sources/androidx/core/view/C2278y0.java:633`
  `if (field != null) {`
- `sources/androidx/core/view/C2278y0.java:635`
  `WindowInsets windowInsets = (WindowInsets) field.get(null);`
- `sources/androidx/core/view/C2278y0.java:640`
  `Log.i("WindowInsetsCompat", "Could not get value from WindowInsets.CONSUMED field", e10);`
- `sources/androidx/core/view/C2278y0.java:805`
  `private static Field f22607k;`
- `sources/androidx/core/view/C2278y0.java:808`
  `private static Field f22608l;`
- `sources/androidx/fragment/app/C2310e.java:1249`
  `Log.v("FragmentManager", ">>> entering view names <<<");`
- `sources/androidx/fragment/app/C2310e.java:1253`
  `Log.v("FragmentManager", ">>> exiting view names <<<");`
- `sources/androidx/fragment/app/C2310e.java:1285`
  `Log.i("FragmentManager", "Ignoring shared elements transition " + objB + " between " + dVar + " and " + dVar2 + " as there are no matching elements in both the entering and exiting fragment. In order to run a SharedElementTransition, both fragments involved must have the element.");`
- `sources/androidx/recyclerview/widget/RecyclerView.java:2792`
  `throw new IllegalArgumentException("Tmp detached view should be removed from RecyclerView before it can be recycled: " + c10 + RecyclerView.this.P());`
- `sources/androidx/recyclerview/widget/RecyclerView.java:2795`
  `throw new IllegalArgumentException("Trying to recycle an ignored view holder. You should first call stopIgnoringView(view) before calling recycle." + RecyclerView.this.P());`
- `sources/androidx/recyclerview/widget/RecyclerView.java:4185`
  `Log.e("RecyclerView", "Problem while matching changed view holders with the newones. The pre-layout information for the change holder " + c11 + " cannot be found but it is necessary for " + c10 + P());`
- `sources/b7/y.java:25`
  `import java.lang.reflect.Field;`
- `sources/b7/y.java:250`
  `public final Field f() {`
- `sources/b7/y.java:368`
  `if (member instanceof Field) {`
- `sources/b7/y.java:369`
  `return ((Field) member).get(objY);`
- `sources/b7/y.java:372`
  `throw new AssertionError("delegate field/method " + member + " neither field nor method");`

## BR077

paper_id: B007
paper_title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

- `sources/M8/A.java:280`
  `private static SSLSocketFactory y(X509TrustManager x509TrustManager) {`
- `sources/M8/A.java:282`
  `SSLContext sSLContextM = T8.j.l().m();`

## BR078

paper_id: B010
paper_title: Client-Focused Security Assessment of mHealth Apps and Recommended Practices to Prevent or Mitigate Transport Security Issues

- `sources/M8/A.java:15`
  `import javax.net.ssl.HostnameVerifier;`

## BR079

paper_id: B030
paper_title: Why Eve and Mallory Love Android: An Analysis of Android SSL (In)Security

- `sources/L6/d.java:59`
  `webView.getSettings().setJavaScriptEnabled(true);`

## BR080

paper_id: B001
paper_title: Security Concerns in Android mHealth Apps

- `sources/androidx/fragment/app/t.java:92`
  `Log.v("FragmentManager", "Fragment " + nVarI0 + " has been inflated via the <fragment> tag: id=0x" + Integer.toHexString(resourceId));`
- `sources/androidx/fragment/app/t.java:105`
  `Log.v("FragmentManager", "Retained Fragment " + nVarI0 + " has been re-attached via the <fragment> tag: id=0x" + Integer.toHexString(resourceId));`
- `sources/androidx/profileinstaller/h.java:46`
  `Log.d("ProfileInstaller", i9 != 1 ? i9 != 2 ? i9 != 3 ? i9 != 4 ? i9 != 5 ? "" : "DIAGNOSTIC_PROFILE_IS_COMPRESSED" : "DIAGNOSTIC_REF_PROFILE_DOES_NOT_EXIST" : "DIAGNOSTIC_REF_PROFILE_EXISTS" : "DIAGNOSTIC_CURRENT_PROFILE_DOES_NOT_EXIST" : "DIAGNOSTIC_CURRENT_PROFILE_EXISTS");`
- `sources/androidx/profileinstaller/h.java:91`
  `Log.d("ProfileInstaller", str);`
- `sources/androidx/profileinstaller/h.java:185`
  `Log.d("ProfileInstaller", "Skipping profile installation for " + context.getPackageName());`
- `sources/androidx/profileinstaller/h.java:189`
  `Log.d("ProfileInstaller", "Installing profile for " + context.getPackageName());`
- `sources/O0/f.java:27`
  `Log.d("Autofill Status", i10 != 1 ? i10 != 2 ? i10 != 3 ? "Unknown status event." : "Autofill popup isn't shown because autofill is not available.\n\nDid you set up autofill?\n1. Go to Settings > System > Languages&input > Advanced > Autofill Service\n2. Pick a service\n\nDid you add an account?\n1....`
- `sources/Y4/B.java:242`
  `Log.d("SessionFirelogPublisher", "Successfully logged Session Start event: " + zVar.c().f());`
- `sources/Y4/C1981g.java:37`
  `Log.d("EventGDTLogger", "Session Event: " + strB);`

## BR082

paper_id: B002
paper_title: Unaddressed privacy risks in accredited health and wellness apps: a cross-sectional systematic assessment

- `sources/androidx/core/content/FileProvider.java:82`
  `@Override // androidx.core.content.FileProvider.b`
- `sources/androidx/core/content/FileProvider.java:104`
  `@Override // androidx.core.content.FileProvider.b`
- `sources/N5/f.java:14`
  `import androidx.core.content.FileProvider;`

## BR086

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/a3/C2119b.java:266`
  `return "EventInternal{transportName=" + this.f17513a + ", code=" + this.f17514b + ", encodedPayload=" + this.f17515c + ", eventMillis=" + this.f17516d + ", uptimeMillis=" + this.f17517e + ", autoMetadata=" + this.f17518f + ", productId=" + this.f17519g + ", pseudonymousId=" + this.f17520h + ", exper...`
- `sources/androidx/appcompat/widget/C2152k.java:10`
  `import android.graphics.Shader;`
- `sources/androidx/appcompat/widget/C2152k.java:126`
  `bitmapDrawable2.setTileModeX(Shader.TileMode.REPEAT);`
- `sources/androidx/appcompat/widget/C2161u.java:5`
  `import android.graphics.BitmapShader;`
- `sources/androidx/appcompat/widget/C2161u.java:6`
  `import android.graphics.Shader;`
- `sources/androidx/appcompat/widget/C2161u.java:12`
  `import android.graphics.drawable.ShapeDrawable;`
- `sources/androidx/appcompat/widget/C2161u.java:13`
  `import android.graphics.drawable.shapes.RoundRectShape;`
- `sources/androidx/appcompat/widget/C2161u.java:14`
  `import android.graphics.drawable.shapes.Shape;`
- `sources/androidx/appcompat/widget/C2161u.java:51`
  `private Shape a() {`
- `sources/androidx/appcompat/widget/C2161u.java:52`
  `return new RoundRectShape(new float[]{5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f}, null, null);`
- `sources/androidx/appcompat/widget/C2161u.java:120`
  `ShapeDrawable shapeDrawable = new ShapeDrawable(a());`
- `sources/androidx/appcompat/widget/C2161u.java:121`
  `shapeDrawable.getPaint().setShader(new BitmapShader(bitmap, Shader.TileMode.REPEAT, Shader.TileMode.CLAMP));`
- `sources/androidx/appcompat/widget/C2161u.java:122`
  `shapeDrawable.getPaint().setColorFilter(bitmapDrawable.getPaint().getColorFilter());`
- `sources/androidx/appcompat/widget/C2161u.java:123`
  `return z9 ? new ClipDrawable(shapeDrawable, 3, 1) : shapeDrawable;`
- `sources/androidx/browser/customtabs/b.java:46`
  `activityOptions.setShareIdentityEnabled(z9);`
- `sources/androidx/browser/customtabs/b.java:134`
  `this.f19010a.putExtra("androidx.browser.customtabs.extra.SHARE_STATE", this.f19017h);`
- `sources/androidx/compose/ui/platform/r.java:2308`
  `getAndroidViewsHandler$ui_release().layout(0, 0, i11 - i9, i12 - i10);`
- `sources/androidx/compose/ui/platform/r.java:2341`
  `getAndroidViewsHandler$ui_release().measure(View.MeasureSpec.makeMeasureSpec(getRoot().t0(), 1073741824), View.MeasureSpec.makeMeasureSpec(getRoot().O(), 1073741824));`
- `sources/androidx/compose/ui/platform/r.java:2419`
  `if (isHardwareAccelerated() && Build.VERSION.SDK_INT != 28) {`
- `sources/androidx/compose/ui/platform/r.java:2422`
  `if (isHardwareAccelerated() && this.f20907v0) {`
- `sources/androidx/constraintlayout/widget/i.java:1182`
  `public static final int[] f22018o = {android.R.attr.windowIsFloating, android.R.attr.windowAnimationStyle, R.attr.actionBarDivider, R.attr.actionBarItemBackground, R.attr.actionBarPopupTheme, R.attr.actionBarSize, R.attr.actionBarSplitStyle, R.attr.actionBarStyle, R.attr.actionBarTabBarStyle, R.attr...`
- `sources/androidx/constraintlayout/widget/i.java:1218`
  `public static final int[] f21873X4 = {R.attr.arrowHeadLength, R.attr.arrowShaftLength, R.attr.barLength, R.attr.color, R.attr.drawableSize, R.attr.gapBetweenBars, R.attr.spinBars, R.attr.thickness};`
- `sources/androidx/constraintlayout/widget/i.java:1239`
  `public static final int[] f21934e5 = {android.R.attr.alpha, android.R.attr.translationX, android.R.attr.translationY, android.R.attr.scaleX, android.R.attr.scaleY, android.R.attr.rotation, android.R.attr.rotationX, android.R.attr.rotationY, android.R.attr.translationZ, android.R.attr.elevation, R.at...`
- `sources/androidx/constraintlayout/widget/i.java:1344`
  `public static final int[] f22008m7 = {android.R.attr.textSize, android.R.attr.typeface, android.R.attr.textStyle, android.R.attr.textColor, android.R.attr.textColorHint, android.R.attr.textColorLink, android.R.attr.shadowColor, android.R.attr.shadowDx, android.R.attr.shadowDy, android.R.attr.shadowR...`
- `sources/androidx/constraintlayout/widget/i.java:1347`
  `public static final int[] f22017n7 = {android.R.attr.textSize, android.R.attr.typeface, android.R.attr.textStyle, android.R.attr.text, android.R.attr.shadowColor, android.R.attr.shadowDx, android.R.attr.shadowDy, android.R.attr.shadowRadius, android.R.attr.fontFamily, R.attr.borderRound, R.attr.bord...`
- `sources/androidx/constraintlayout/widget/i.java:1371`
  `public static final int[] f21786M7 = {android.R.attr.id, R.attr.SharedValue, R.attr.SharedValueId, R.attr.clearsTag, R.attr.duration, R.attr.ifTagNotSet, R.attr.ifTagSet, R.attr.motionInterpolator, R.attr.motionTarget, R.attr.onStateTransition, R.attr.pathMotionArc, R.attr.setsTag, R.attr.transition...`
- `sources/androidx/core/app/b.java:68`
  `activity.finishAffinity();`
- `sources/androidx/fragment/app/H.java:32`
  `@Override // java.io.Writer, java.io.Flushable`
- `sources/androidx/vectordrawable/graphics/drawable/f.java:19`
  `import android.graphics.Shader;`
- `sources/androidx/work/impl/utils/ForceStopRunnable.java:213`
  `String str = p.a(this.f25001w) ? "The file system on the device is in a bad state. WorkManager cannot access the app's internal data store." : "WorkManager can't be accessed from direct boot, because credential encrypted storage isn't accessible.\nDon't access or initialise WorkManager from directAw...`
- `sources/com/google/android/gms/internal/measurement/AbstractC2748z0.java:15`
  `if (sharedPreferencesC2708u0 != null) {`
- `sources/com/google/android/gms/internal/measurement/AbstractC2748z0.java:16`
  `return sharedPreferencesC2708u0;`
- `sources/com/google/android/gms/internal/measurement/AbstractC2748z0.java:22`
  `SharedPreferences sharedPreferences = context.getSharedPreferences(str, 0);`
- `sources/com/google/android/gms/internal/measurement/AbstractC2748z0.java:24`
  `return sharedPreferences;`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:208`
  `f26908A = c2680q3E.c("measurement.rb.attribution.app_allowlist", "com.labpixies.flood,com.sofascore.results,games.spearmint.triplecrush,com.block.juggle,io.supercent.linkedcubic,com.cdtg.gunsound,com.corestudios.storemanagementidle,com.cdgames.fidget3d,io.supercent.burgeridle,io.supercent.pizzaidle,...`
- `sources/com/google/android/gms/internal/measurement/C2719v3.java:20`
  `private final SharedPreferences f27325a;`
- `sources/com/google/android/gms/internal/measurement/C2719v3.java:26`
  `private final SharedPreferences.OnSharedPreferenceChangeListener f27327c;`
- `sources/com/google/android/gms/internal/measurement/C2719v3.java:37`
  `private C2719v3(SharedPreferences sharedPreferences, Runnable runnable) {`
- `sources/com/google/android/gms/internal/measurement/C2719v3.java:38`
  `SharedPreferences.OnSharedPreferenceChangeListener onSharedPreferenceChangeListener = new SharedPreferences.OnSharedPreferenceChangeListener() { // from class: com.google.android.gms.internal.measurement.u3`
- `sources/com/google/android/gms/internal/measurement/C2719v3.java:39`
  `@Override // android.content.SharedPreferences.OnSharedPreferenceChangeListener`
- `sources/com/google/android/gms/internal/measurement/C2719v3.java:40`
  `public final void onSharedPreferenceChanged(SharedPreferences sharedPreferences2, String str) {`
- `sources/com/google/android/gms/internal/measurement/C2719v3.java:41`
  `this.f27309a.d(sharedPreferences2, str);`
- `sources/com/google/android/gms/internal/measurement/C2719v3.java:44`
  `this.f27327c = onSharedPreferenceChangeListener;`
- `sources/com/google/android/gms/internal/measurement/C2719v3.java:47`
  `this.f27325a = sharedPreferences;`
- `sources/com/google/android/gms/internal/measurement/C2719v3.java:49`
  `sharedPreferences.registerOnSharedPreferenceChangeListener(onSharedPreferenceChangeListener);`
- `sources/com/google/android/gms/internal/measurement/C2719v3.java:52`
  `private static SharedPreferences a(Context context, String str) {`
- `sources/com/google/android/gms/internal/measurement/C2719v3.java:56`
  `SharedPreferences sharedPreferencesA = AbstractC2748z0.a(context, str, 0, AbstractC2716v0.f27317a);`
- `sources/com/google/android/gms/internal/measurement/C2719v3.java:58`
  `return sharedPreferencesA;`
- `sources/com/google/android/gms/internal/measurement/C2719v3.java:63`
  `SharedPreferences sharedPreferencesA2 = AbstractC2748z0.a(context, str.substring(12), 0, AbstractC2716v0.f27317a);`
- `sources/com/google/android/gms/internal/measurement/C2719v3.java:65`
  `return sharedPreferencesA2;`
- `sources/com/google/android/gms/internal/measurement/C2719v3.java:95`
  `c2719v3.f27325a.unregisterOnSharedPreferenceChangeListener(c2719v3.f27327c);`
- `sources/com/google/android/gms/internal/measurement/C2719v3.java:103`
  `final /* synthetic */ void d(SharedPreferences sharedPreferences, String str) {`
- `sources/com/google/android/gms/measurement/internal/B2.java:63`
  `this.f28291d.h().E().b("Cannot serialize bundle value to SharedPreferences. Type", obj.getClass());`
- `sources/com/google/android/gms/measurement/internal/B2.java:75`
  `this.f28291d.h().E().b("Cannot serialize bundle value to SharedPreferences. Type", obj.getClass());`
- `sources/com/google/android/gms/measurement/internal/B2.java:80`
  `this.f28291d.h().E().b("Cannot serialize bundle value to SharedPreferences", e9);`
- `sources/com/google/android/gms/measurement/internal/C3035v4.java:234`
  `h().D().b("Resettable device id encryption failed", e11.getMessage());`
- `sources/com/google/android/gms/measurement/internal/C3035v4.java:237`
  `h().D().b("app instance id encryption failed", e12.getMessage());`
- `sources/com/google/android/gms/measurement/internal/C3061z2.java:132`
  `if (sharedPreferences == null) {`
- `sources/com/google/android/gms/measurement/internal/C3061z2.java:135`
  `return sharedPreferences.contains("deferred_analytics_collection");`
- `sources/com/google/android/gms/measurement/internal/C3061z2.java:140`
  `SharedPreferences.Editor editorEdit = H().edit();`
- `sources/com/google/android/gms/measurement/internal/C3061z2.java:151`
  `SharedPreferences.Editor editorEdit = H().edit();`
- `sources/com/google/android/gms/measurement/internal/C3061z2.java:350`
  `SharedPreferences.Editor editorEdit = H().edit();`
- `sources/com/google/android/gms/measurement/internal/C3061z2.java:361`
  `SharedPreferences.Editor editorEdit = H().edit();`
- `sources/com/google/android/gms/measurement/internal/C3064z5.java:35`
  `public static C3064z5 c(SharedPreferences sharedPreferences) {`
- `sources/com/google/android/gms/measurement/internal/C3064z5.java:37`
  `String strF = f(sharedPreferences, "IABTCF_VendorConsents");`
- `sources/com/google/android/gms/measurement/internal/C3064z5.java:41`
  `int iA = a(sharedPreferences, "IABTCF_gdprApplies");`
- `sources/com/google/android/gms/measurement/internal/C3064z5.java:45`
  `int iA2 = a(sharedPreferences, "IABTCF_EnableAdvertiserConsentMode");`
- `sources/com/google/android/gms/measurement/internal/C3064z5.java:49`
  `int iA3 = a(sharedPreferences, "IABTCF_PolicyVersion");`
- `sources/com/google/android/gms/measurement/internal/C3064z5.java:53`
  `String strF2 = f(sharedPreferences, "IABTCF_PurposeConsents");`
- `sources/com/google/android/gms/measurement/internal/C3064z5.java:57`
  `int iA4 = a(sharedPreferences, "IABTCF_CmpSdkID");`
- `sources/com/google/android/gms/measurement/internal/d6.java:510`
  `return parcelObtain.marshall();`
- `sources/com/google/android/gms/measurement/internal/d6.java:1195`
  `SharedPreferences.Editor editorEdit = zza().getSharedPreferences("google.analytics.deferred.deeplink.prefs", 0).edit();`
- `sources/com/google/android/gms/measurement/internal/F3.java:561`
  `final /* synthetic */ void L(SharedPreferences sharedPreferences, String str) {`
- `sources/com/google/android/gms/measurement/internal/G.java:717`
  `f28434e0 = F("measurement.rb.attribution.app_allowlist", "com.labpixies.flood,com.sofascore.results,games.spearmint.triplecrush,com.block.juggle,io.supercent.linkedcubic,com.cdtg.gunsound,com.corestudios.storemanagementidle,com.cdgames.fidget3d,io.supercent.burgeridle,io.supercent.pizzaidle,jp.ne.ib...`
- `sources/com/google/android/gms/measurement/internal/Q2.java:51`
  `this.f28660z.h().G().b("Two tasks share the same index. index", Long.valueOf(this.f28657w));`
- `sources/com/google/android/gms/measurement/internal/Z5.java:475`
  `parcelObtain.unmarshall(bArr, 0, bArr.length);`
- `sources/com/google/android/material/button/MaterialButton.java:523`
  `Log.w("MaterialButton", "MaterialButton manages its own background to control elevation, shape, color and states. Consider using backgroundTint, shapeAppearance and other attributes where available. A custom background will ignore these attributes and you should consider handling interaction states ...`
- `sources/com/google/android/material/button/MaterialButtonToggleGroup.java:390`
  `C3323k shapeAppearanceModel = materialButton.getShapeAppearanceModel();`
- `sources/com/google/android/material/button/MaterialButtonToggleGroup.java:391`
  `this.f29508w.add(new c(shapeAppearanceModel.r(), shapeAppearanceModel.j(), shapeAppearanceModel.t(), shapeAppearanceModel.l()));`
- `sources/com/google/android/material/button/MaterialButtonToggleGroup.java:492`
  `C3323k.b bVarV = materialButtonH.getShapeAppearanceModel().v();`

## BR090

paper_id: B014
paper_title: Privacy Assessment in Mobile Health Apps: Scoping Review

- `audit_reports/evidence_chains.md:1`
  `# LightBlue Evidence Chains`
- `audit_reports/evidence_chains.md:30`
  `7. 系统 logcat 状态：'d9.a.C0570a' 会调用 'Log.println'。搜索到 'f5.a.e(boolean)' 在 boolean 为 true 时执行 'd9.a.f(new a.C0570a())'，并输出 'SDK initialized'。这条路径属于 Mailchimp SDK wrapper；是否在 release 初始化中传 true 未静态确认。因此不能把系统 logcat 泄漏写为 confirmed。`
- `audit_reports/evidence_chains.md:31`
  `8. 应用层安全判断：没有看到 AES/HMAC/signature wrapper、token exchange、attestation、payload provenance、白名单命令约束或 BLE peer proof。但通用 BLE Explorer 的目标就是把 GATT 操作暴露给用户，因此该项是“敏感外设场景下的 supported hypothesis”，不是对 App 本身产品功能的漏洞定性。`
- `audit_reports/evidence_chains.md:64`
  `当前结论：BR092 为 'supported_hypothesis'；BR076/BR077/BR093 为 'not_testable' 或 'not_supported'；BR040/BR041 因 Facebook 专项规则不能套用为 confirmed。`
- `audit_reports/evidence_chains.md:77`
  `当前结论：BR016 为 'confirmed'；BR092 为 'supported_hypothesis'；BR093 为 'not_testable'。`
- `audit_reports/evidence_chains.md:102`
  `4. Third-party TLS classes：'V8.d'、'V8.c'、OkHttp 相关类为库实现，不能直接按一方弱 TLS confirmed。`
- `audit_reports/lightblue_beginner_audit_report.md:6`
  `结论枚举严格限定为：'confirmed'、'supported_hypothesis'、'not_supported'、'not_testable'。`
- `audit_reports/lightblue_beginner_audit_report.md:49`
  `因此，本报告对动态类规则严格使用 'not_testable'，除非静态代码足以支持一个非 confirmed 的 hypothesis；没有动态流量的项目不会强行写成 confirmed。`
- `audit_reports/lightblue_beginner_audit_report.md:78`
  `- B008 'Your Signal, Their Data... Wireless-scanning SDKs in Android'：论文摘要指出 BLE/Wi-Fi 扫描结果、AAID、email、GPS 等可被无线扫描 SDK 收集并导致移动画像风险。该论文支持检查第三方 SDK 是否处理 BLE scan result。本 App 的 BLE scan result 处理在一方 'K5.b'，因此第三方扫描 SDK 规则不能 confirmed。`
- `audit_reports/lightblue_beginner_audit_report.md:79`
  `- B028 'A Study of the Feasibility of Co-located App Attacks against BLE...'：论文摘要指出 BLE 设备可能保存健康数据或关键控制，Android 上同机恶意 App 可滥用 host-device trusted relationship，且论文主张由 BLE device/app developers 实现 application-layer security。该论文支持把“只有 Android BLE/GATT 权限，没有应用层 token/signature”的 BLE 操作标为 supported hypot...`
- `audit_reports/lightblue_beginner_audit_report.md:90`
  `- 结论：'confirmed'`
- `audit_reports/lightblue_beginner_audit_report.md:94`
  `- 风险边界：该 key 不是用户密码，也不是证书私钥。confirmed 的范围只限于“APK 中存在可提取的第三方服务 key/SDK key”。是否可被滥用需要 Mailchimp 后端策略验证，当前证据不足以确认账号接管或远程写入滥用。`
- `audit_reports/lightblue_beginner_audit_report.md:102`
  `- 为什么不是 confirmed：没有运行 App 后的 DataStore 文件或设备抽取结果，不能证明某个真实用户 secret 已存在本地；而 BR026 的原始信号偏向 SharedPreferences，本 App 使用的是 DataStore，并有 SharedPreferences migration。静态证据足以支持 hypothesis：一旦用户配置 Adafruit，secret 会被 app-private DataStore 保存，且未见加密。`
- `audit_reports/lightblue_beginner_audit_report.md:111`
  `- 为什么不是 confirmed：没有抓包证明真实 payload 已上传，也没有真实 BLE 设备证明 payload 是健康测量或位置数据。App 的 'sample_virtual_devices.json' 包含 Heart Rate、Glucose、Health Thermometer、Blood Pressure、Location and Navigation 等 demo GATT 服务，但这些是本地示例数据，不能单独证明真实用户数据上传。`
- `audit_reports/lightblue_beginner_audit_report.md:120`
  `- 为什么不是 confirmed：没有抓包和首次启动运行记录，不能确认这些 SDK 在用户作出偏好选择前实际发包，也不能确认 Advertising ID 被读取或上传。单个权限、单个 SDK、单个事件名都不作为 confirmed。`
- `audit_reports/lightblue_beginner_audit_report.md:128`
  `- 为什么不是 confirmed：没有 logcat，不知道运行时日志级别、debug/release 条件、Timber tree 是否实际 planted，也不知道 payload 是否为敏感健康测量。confirmed 的范围不能扩大到“系统日志泄漏真实敏感数据”。`
- `audit_reports/lightblue_beginner_audit_report.md:136`
  `- 为什么不是 confirmed：LightBlue 是通用 BLE Explorer，设计目标就是允许用户探索任意 BLE GATT 表面；没有具体外设协议或设备，无法证明某个外设被越权读写。该结论是“如果用于敏感 BLE 外设，应由外设/协议层补应用层安全”的 supported hypothesis。`
- `audit_reports/lightblue_beginner_audit_report.md:142`
  `BR006、BR007、BR008、BR009、BR010、BR011、BR012、BR013、BR078、BR079、BR095：当前一方 Adafruit 路径使用 HTTPS base URL；未发现一方 'usesCleartextTraffic=true'、Network Security Config 放宽 CA、业务 HTTP endpoint、空 'TrustManager'、'HostnameVerifier' 总返回 true、SSL exception fallback 到 HTTP。OkHttp/Retrofit/Firebase/Mailchimp 第三方库中的 TL...`
- `audit_reports/lightblue_beginner_audit_report.md:150`
  `BR029、BR030、BR031、BR032、BR033、BR034、BR035、BR059、BR083、BR084：'LaunchActivity' 导出用于 launcher，带 'MAIN'、'VIEW' 与 'LAUNCHER'；未见 'BROWSABLE'、scheme、host、path 或 data URI。'MainActivity' 导出且有 SEARCH action，但未见外部 intent 参数进入账号、设备命令、报告或上传路径。WorkManager/ProfileInstaller 等导出组件为第三方/系统组件并带系统权限或框架用途。没有 adb 动态测试，不能 ...`
- `audit_reports/lightblue_beginner_audit_report.md:154`
  `BR018、BR019、BR020、BR073、BR096、BR097：资源 'sample_virtual_devices.json' 确实包含 Heart Rate、Glucose、Health Thermometer、Blood Pressure、Location and Navigation 等示例 BLE 服务和字节样例。这些是本地 demo/virtual device 数据，不能单独作为真实用户健康数据收集、上传或解析漏洞的 confirmed 证据。没有 medication/dose/prescription、mood/depression/anxiety/journal/s...`
- `audit_reports/lightblue_beginner_audit_report.md:158`
  `Manifest 权限包括 BLE/Location/Internet/Camera/AD_ID/AdServices/Vibrate/WakeLock/Boot/ForegroundService 等。BLE 与 Location 对 BLE 扫描和连接有功能解释；Camera 对 QR scanner/ML Kit 有解释；Internet 对 Adafruit/Firebase/Mailchimp 有解释。AD_ID/AdServices 与 Analytics SDK 有关联，但没有 Advertising ID 读取和上传抓包，不能 confirmed。权限类规则主要为 not_su...`
- `audit_reports/lightblue_beginner_audit_report.md:163`
  `2. 同意开关测试：关闭 'send_usage_data' 后重启 App，再抓包比较 Firebase Analytics/Crashlytics 行为。若仍发 analytics event，再考虑把 BR076/BR077 从 not_testable 升级为 confirmed 或 supported_hypothesis。`
- `audit_reports/lightblue_beginner_audit_report.md:171`
  `confirmed 仅有 1 类：APK 中硬编码 Mailchimp SDK/audience key（BR016）。`
- `audit_reports/mentor_review.md:9`
  `- 'confirmed'`
- `audit_reports/mentor_review.md:18`
  `### 2.1 单个权限不作为 confirmed`
- `audit_reports/mentor_review.md:20`
  `Manifest 中的 'AD_ID'、'ACCESS_ADSERVICES_AD_ID'、'ACCESS_FINE_LOCATION'、'BLUETOOTH_SCAN'、'CAMERA' 没有被单独用于 confirmed。BLE/location/camera 都有功能路径；AD_ID 只支持 telemetry hypothesis，未写成 confirmed。`
- `audit_reports/mentor_review.md:22`
  `### 2.2 单个 SDK 不作为 confirmed`
- `audit_reports/mentor_review.md:24`
  `Firebase、Crashlytics、Mailchimp、MLKit、WorkManager、OkHttp 的存在没有被单独写成漏洞。唯一 confirmed 的第三方相关项是 BR016，因为源码中有可从 APK 提取的 hardcoded Mailchimp key 常量；这个结论不依赖“存在 Mailchimp SDK”。`
- `audit_reports/mentor_review.md:26`
  `### 2.3 单个 URL 不作为 confirmed`
- `audit_reports/mentor_review.md:32`
  `'sample_virtual_devices.json' 中的 Heart Rate、Glucose、Blood Pressure、Location and Navigation 等样例没有被直接写成 confirmed health data collection。报告仅把它们作为“App 具备演示这些 GATT service 的语义背景”，真实健康数据上传仍为 supported_hypothesis 或 not_supported。`
- `audit_reports/mentor_review.md:44`
  `复核结果：保持 'confirmed'。`
- `audit_reports/mentor_review.md:51`
  `复核结果：保持 'supported_hypothesis'，不升级 confirmed。`
- `audit_reports/mentor_review.md:68`
  `修正边界：没有把 “AD_ID permission” 或 “Firebase SDK” 单独写成 confirmed。`
- `audit_reports/mentor_review.md:96`
  `修正边界：没有把 exported=true 单独作为 confirmed。`
- `audit_reports/mentor_review.md:102`
  `1. 把 Adafruit secret 本地存储从可能的 confirmed 降级为 'supported_hypothesis'。`
- `audit_reports/mentor_review.md:103`
  `2. 把 Firebase/Mailchimp 首启或同意前发包从 supported/confirmed 降级为动态规则 'not_testable'，只在 cloud/third-party recipient 层保留 static hypothesis。`
- `audit_reports/mentor_review.md:105`
  `4. 把 BLE app-layer security 写成“敏感外设场景下的 supported hypothesis”，不是产品功能漏洞。`
- `audit_reports/mentor_review.md:106`
  `5. 把 sample virtual device 健康服务排除出真实用户数据 confirmed 证据。`
- `audit_reports/rule_by_rule_mapping.md:3`
  `本附录逐条覆盖 'rule_catalog.tsv' 中的 83 条规则。每条规则只使用四个允许结论之一：'confirmed'、'supported_hypothesis'、'not_supported'、'not_testable'。`
- `audit_reports/rule_by_rule_mapping.md:22`
  `- BR016 | B006 'Analyzing security issues of android mobile health and medical applications' | 'confirmed' | 'O5.a' 硬编码 Mailchimp key 'THE KEY'。`
- `audit_reports/rule_by_rule_mapping.md:32`
  `- BR026 | B002 'Unaddressed privacy risks in accredited health and wellness apps' | 'supported_hypothesis' | 'ADAFRUIT_IO_USERNAME' 与 'ADAFRUIT_IO_SECRET_KEY' 写入 DataStore；无设备抽取，不能 confirmed。`
- `audit_reports/rule_by_rule_mapping.md:34`
  `- BR028 | B014 'Privacy Assessment in Mobile Health Apps' | 'not_supported' | Manifest 'allowBackup=false'；本地 secret 风险不等于 backup 风险 confirmed。`
- `audit_reports/rule_by_rule_mapping.md:51`
  `- BR055 | B014 'Privacy Assessment in Mobile Health Apps' | 'confirmed' | 本审计提供 file/class/function/rule 证据；该条是报告质量 meta-rule。`
- `audit_reports/rule_by_rule_mapping.md:52`
  `- BR058 | B022 'Android Application Security' | 'confirmed' | 本审计明确区分一方与 Firebase/Mailchimp/AndroidX/MLKit/OkHttp；该条是报告质量 meta-rule。`
- `audit_reports/rule_by_rule_mapping.md:64`
  `- BR067 | B029 'Who’s Accessing My Data? Application-Level Access Control for Bluetooth Low Energy' | 'supported_hypothesis' | BLE 操作前未见 app-specific token/key/attestation；无具体外设，不能 confirmed。`

## BR092

paper_id: B005
paper_title: Mobile health and privacy: cross sectional study

- `sources/androidx/appcompat/app/h.java:459`
  `return powerManager.isPowerSaveMode();`
- `sources/androidx/appcompat/widget/C2163w.java:22`
  `protected synchronized void onMeasure(int i9, int i10) {`
- `sources/androidx/appcompat/widget/C2166z.java:99`
  `int iSave = canvas.save();`
- `sources/androidx/appcompat/widget/C2166z.java:105`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/appcompat/widget/E.java:319`
  `synchronized (rectF) {`
- `sources/androidx/appcompat/widget/SwitchCompat.java:709`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/camera/core/d.java:54`
  `synchronized (this.f19069b) {`
- `sources/androidx/camera/core/r.java:48`
  `synchronized (this.f19165z) {`
- `sources/androidx/core/widget/NestedScrollView.java:1000`
  `int iSave = canvas.save();`
- `sources/androidx/core/widget/NestedScrollView.java:1019`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/core/widget/NestedScrollView.java:1024`
  `int iSave2 = canvas.save();`
- `sources/androidx/core/widget/NestedScrollView.java:1042`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/recyclerview/widget/RecyclerView.java:5016`
  `int iSave = canvas.save();`
- `sources/androidx/recyclerview/widget/RecyclerView.java:5022`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/recyclerview/widget/RecyclerView.java:5047`
  `int iSave4 = canvas.save();`
- `sources/androidx/vectordrawable/graphics/drawable/f.java:433`
  `int iSave = canvas.save();`
- `sources/B0/C1072t.java:1063`
  `synchronized (this.f1635z) {`
- `sources/C/AbstractActivityC2463j.java:436`
  `if (!AbstractC1838t.b(e9.getMessage(), "Can not perform this action after onSaveInstanceState")) {`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:205`
  `f26962x = c2680q3E.b("measurement.upload.minimum_delay", 500L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:209`
  `f26909B = c2680q3E.b("measurement.upload.realtime_upload_interval", 10000L);`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:210`
  `f26910C = c2680q3E.b("measurement.upload.refresh_blacklisted_config_interval", 604800000L);`
- `sources/com/google/android/gms/measurement/internal/C2953j5.java:53`
  `this.f29020h = new A2(c3061z2F4, "last_upload", 0L);`
- `sources/com/google/android/gms/measurement/internal/C2953j5.java:56`
  `this.f29021i = new A2(c3061z2F5, "last_upload_attempt", 0L);`
- `sources/com/google/android/gms/measurement/internal/ServiceConnectionC2911d5.java:37`
  `synchronized (this) {`
- `sources/com/google/android/gms/measurement/internal/ServiceConnectionC2911d5.java:62`
  `synchronized (this) {`
- `sources/com/google/android/material/internal/a.java:859`
  `int iSave = canvas.save();`
- `sources/com/punchthrough/lightblueexplorer/MicrochipActivity.java:56`
  `@Metadata(d1 = {"\u0000Û\u0001\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u000b\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0004\n\u0002\u0010\u0012\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u000e\n\u0002\u0010 \n\u0002\u0018\...`
- `sources/com/punchthrough/lightblueexplorer/R.java:214`
  `public static final int behavior_saveFlags = 0x7f040077;`
- `sources/D2/C1152c.java:189`
  `synchronized (this.f3391d) {`
- `sources/D2/o.java:697`
  `synchronized (this.f3471o) {`
- `sources/f4/b.java:50`
  `return new b(new e(iVarG.a("FIREBASE_CRASHLYTICS_REPORT", F.class, bVarB, gVar), jVar.b(), c4871n), gVar);`
- `sources/f4/C3192a.java:91`
  `canvas.save();`
- `sources/f4/e.java:135`
  `g.f().b("Sending report through Google DataTransport: " + abstractC4858A.d());`
- `sources/G4/m.java:28`
  `return new d(d(interfaceC4860C, iOptInt2, jSONObject), jSONObject.has("session") ? c(jSONObject.getJSONObject("session")) : c(new JSONObject()), b(jSONObject.getJSONObject("features")), iOptInt, iOptInt2, jSONObject.optDouble("on_demand_upload_rate_per_minute", 10.0d), jSONObject.optDouble("on_deman...`
- `sources/H3/C3378d.java:78`
  `AbstractC3119a.b("JobInfoScheduler", "Scheduling upload for context %s with jobId=%d in %dms(Backend next call timestamp %d). Attempt %d", pVar, Integer.valueOf(iC), Long.valueOf(this.f34391c.g(pVar.d(), J9, i9)), Long.valueOf(J9), Integer.valueOf(i9));`
- `sources/I3/W.java:153`
  `sQLiteDatabase.execSQL("CREATE TABLE global_log_event_state (last_metrics_upload_ms BIGINT PRIMARY KEY)");`
- `sources/J5/F.java:43`
  `f7910f = E6.N.k(D6.C.a(f9.d("2C06"), "Acceleration"), D6.C.a(f9.d("2B33"), "ACS Control Point"), D6.C.a(f9.d("2B30"), "ACS Data In"), D6.C.a(f9.d("2B32"), "ACS Data Out Indicate"), D6.C.a(f9.d("2B31"), "ACS Data Out Notify"), D6.C.a(f9.d("2B2F"), "ACS Status"), D6.C.a(f9.d("2BDC"), "Active Preset In...`
- `sources/J5/F.java:44`
  `f7911g = E6.N.k(D6.C.a(f9.d("2905"), "Characteristic Aggregate Format"), D6.C.a(f9.d("2900"), "Characteristic Extended Properties"), D6.C.a(f9.d("2904"), "Characteristic Presentation Format"), D6.C.a(f9.d("2901"), "Characteristic User Description"), D6.C.a(f9.d("2902"), "Client Characteristic Config...`
- `sources/O3/k.java:1050`
  `public static final int[] f10899Y = {android.R.attr.maxWidth, android.R.attr.maxHeight, android.R.attr.elevation, R.attr.backgroundTint, R.attr.behavior_draggable, R.attr.behavior_expandedOffset, R.attr.behavior_fitToContents, R.attr.behavior_halfExpandedRatio, R.attr.behavior_hideable, R.attr.behav...`
- `sources/P4/k.java:25`
  `private synchronized void a() {`

## BR093

paper_id: B004
paper_title: Assessment of the Data Sharing and Privacy Practices of Smartphone Apps for Depression and Smoking Cessation

- `sources/androidx/work/c.java:158`
  `cVarT.q(new IllegalStateException("Expedited WorkRequests require a ListenableWorker to provide an implementation for 'getForegroundInfoAsync()'"));`
- `sources/b4/C1087b.java:323`
  `return "CrashlyticsReport{sdkVersion=" + this.f1903b + ", gmpAppId=" + this.f1904c + ", platform=" + this.f1905d + ", installationUuid=" + this.f1906e + ", firebaseInstallationId=" + this.f1907f + ", firebaseAuthenticationToken=" + this.f1908g + ", appQualitySessionId=" + this.f1909h + ", buildVersi...`
- `sources/com/google/android/gms/measurement/internal/C2954k.java:48`
  `private static final String[] f29033h = {"app_version", "ALTER TABLE apps ADD COLUMN app_version TEXT;", "app_store", "ALTER TABLE apps ADD COLUMN app_store TEXT;", "gmp_version", "ALTER TABLE apps ADD COLUMN gmp_version INTEGER;", "dev_cert_hash", "ALTER TABLE apps ADD COLUMN dev_cert_hash INTEGER;...`
- `sources/com/google/android/gms/measurement/internal/C2954k.java:883`
  `cursorQuery = z().query("apps", new String[]{"app_instance_id", "gmp_app_id", "resettable_device_id_hash", "last_bundle_index", "last_bundle_start_timestamp", "last_bundle_end_timestamp", "app_version", "app_store", "gmp_version", "dev_cert_hash", "measurement_enabled", "day", "daily_public_events_c...`
- `sources/com/punchthrough/lightblueexplorer/ui/characteristicdetail/CharacteristicDetailActivity.java:47`
  `@Metadata(d1 = {"\u0000T\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003...`
- `sources/com/punchthrough/lightblueexplorer/ui/characteristicdetail/CharacteristicDetailActivity.java:787`
  `protected void onCreate(Bundle savedInstanceState) {`
- `sources/com/punchthrough/lightblueexplorer/ui/characteristicdetail/CharacteristicDetailActivity.java:788`
  `super.onCreate(savedInstanceState);`
- `sources/J5/F.java:43`
  `f7910f = E6.N.k(D6.C.a(f9.d("2C06"), "Acceleration"), D6.C.a(f9.d("2B33"), "ACS Control Point"), D6.C.a(f9.d("2B30"), "ACS Data In"), D6.C.a(f9.d("2B32"), "ACS Data Out Indicate"), D6.C.a(f9.d("2B31"), "ACS Data Out Notify"), D6.C.a(f9.d("2B2F"), "ACS Status"), D6.C.a(f9.d("2BDC"), "Active Preset In...`
- `sources/J5/F.java:44`
  `f7911g = E6.N.k(D6.C.a(f9.d("2905"), "Characteristic Aggregate Format"), D6.C.a(f9.d("2900"), "Characteristic Extended Properties"), D6.C.a(f9.d("2904"), "Characteristic Presentation Format"), D6.C.a(f9.d("2901"), "Characteristic User Description"), D6.C.a(f9.d("2902"), "Client Characteristic Config...`
- `sources/k6/O.java:128`
  `byte[] bArrC = AbstractC1935e.c(((k6.Q) O.this.f35897B.getValue()).g().g().h(), characteristicFormatViewStateE.getSavedFormat(), characteristicFormatViewStateE.getSavedByteLimit(), characteristicFormatViewStateE.getSavedEndianness());`
- `sources/k6/O.java:354`
  `if (AbstractC1935e.a(str, characteristicFormatViewState.getSavedFormat()) && str.length() == 32) {`
- `sources/k6/O.java:1948`
  `EnumC1934d savedFormat = this.f36019F.getSavedFormat();`
- `sources/k6/O.java:1949`
  `EnumC1932b savedByteLimit = this.f36019F.getSavedByteLimit();`
- `sources/k6/O.java:1950`
  `W5.z savedEndianness = this.f36019F.getSavedEndianness();`
- `sources/k6/O.java:1952`
  `if (e9.l(uuid, instanceId, instanceId2, savedFormat, savedByteLimit, savedEndianness, this) == objF) {`
- `sources/k6/O.java:2135`
  `if (AbstractC1935e.a(str, characteristicFormatViewState.getSavedFormat()) && str.length() == 32) {`
- `sources/k6/VirtualCharacteristic.java:380`
  `this.displayValue = (i9 & 512) == 0 ? AbstractC1935e.d(this.byteArray, this.dataFormatViewState.getSavedFormat(), this.dataFormatViewState.getSavedByteLimit(), this.dataFormatViewState.getSavedEndianness()) : str4;`
- `sources/k6/VirtualCharacteristic.java:524`
  `this.displayValue = AbstractC1935e.d(bArrQ0, dVar.getSavedFormat(), dVar.getSavedByteLimit(), dVar.getSavedEndianness());`
- `sources/o5/C4033m.java:28`
  `public synchronized String a() {`
- `sources/Y4/C4866I.java:56`
  `private synchronized String b(String str, SharedPreferences sharedPreferences) {`

## BR094

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `sources/A0/C2067J.java:157`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:17:0x0038 -> B:11:0x0021). Please report as a decompilation issue!!! */`
- `sources/A0/C2067J.java:158`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:19:0x0042 -> B:21:0x0045). Please report as a decompilation issue!!! */`
- `sources/A0/C2083a.java:110`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:16:0x0066 -> B:18:0x0069). Please report as a decompilation issue!!! */`
- `sources/A0/C2097o.java:44`
  `int iSave = canvas.save();`
- `sources/A0/C2097o.java:48`
  `canvas.restoreToCount(iSave);`
- `sources/A0/C2103u.java:198`
  `int iSave = canvasD.save();`
- `sources/A0/C2103u.java:201`
  `canvasD.restoreToCount(iSave);`
- `sources/androidx/appcompat/widget/C2166z.java:99`
  `int iSave = canvas.save();`
- `sources/androidx/appcompat/widget/C2166z.java:105`
  `canvas.restoreToCount(iSave);`
- `sources/androidx/appcompat/widget/S.java:154`
  `r0.postDelayed(r6, r3)`
- `sources/androidx/appcompat/widget/S.java:164`
  `r0.postDelayed(r6, r3)`
- `sources/androidx/appcompat/widget/SwitchCompat.java:709`
  `canvas.restoreToCount(iSave2);`
- `sources/androidx/appcompat/widget/X.java:90`
  `private synchronized boolean a(Context context, long j9, Drawable drawable) {`
- `sources/androidx/appcompat/widget/X.java:176`
  `private synchronized Drawable h(Context context, long j9) {`
- `sources/androidx/camera/core/d.java:88`
  `synchronized (this.f19069b) {`
- `sources/androidx/camera/core/p.java:146`
  `synchronized (this.f19140a) {`
- `sources/androidx/camera/core/p.java:166`
  `synchronized (this.f19140a) {`
- `sources/androidx/compose/foundation/gestures/d.java:527`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:20:0x0049 -> B:25:0x005b). Please report as a decompilation issue!!! */`
- `sources/androidx/compose/foundation/gestures/d.java:528`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:22:0x0055 -> B:24:0x0058). Please report as a decompilation issue!!! */`
- `sources/androidx/compose/foundation/gestures/d.java:633`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:30:0x008e -> B:19:0x005e). Please report as a decompilation issue!!! */`
- `sources/androidx/compose/foundation/gestures/d.java:634`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:41:0x00d5 -> B:19:0x005e). Please report as a decompilation issue!!! */`
- `sources/androidx/compose/foundation/gestures/d.java:635`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:45:0x00dc -> B:19:0x005e). Please report as a decompilation issue!!! */`
- `sources/androidx/compose/foundation/gestures/d.java:636`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:47:0x00eb -> B:19:0x005e). Please report as a decompilation issue!!! */`
- `sources/androidx/compose/foundation/gestures/d.java:637`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:50:0x00fb -> B:11:0x0027). Please report as a decompilation issue!!! */`
- `sources/androidx/compose/foundation/relocation/a.java:49`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:18:0x0064 -> B:20:0x0067). Please report as a decompilation issue!!! */`
- `sources/androidx/compose/ui/platform/AndroidCompositionLocals_androidKt.java:19`
  `@Metadata(d1 = {"\u0000\\\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\u0001\n\u0002\b\u000...`
- `sources/androidx/compose/ui/platform/C2180e0.java:32`
  `this.f20697a.postTranslate(iArr2[0] - i9, iArr2[1] - i10);`
- `sources/androidx/compose/ui/platform/C2213r0.java:54`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:15:0x0035 -> B:17:0x0038). Please report as a decompilation issue!!! */`
- `sources/androidx/compose/ui/platform/C2224x.java:1627`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:94:0x0194 -> B:95:0x0195). Please report as a decompilation issue!!! */`
- `sources/androidx/compose/ui/platform/C2224x.java:1726`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:32:0x0086 -> B:42:0x00d2). Please report as a decompilation issue!!! */`
- `sources/androidx/compose/ui/platform/C2224x.java:1727`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:40:0x00cf -> B:42:0x00d2). Please report as a decompilation issue!!! */`
- `sources/androidx/compose/ui/platform/I1.java:387`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:25:0x007f -> B:8:0x0019). Please report as a decompilation issue!!! */`
- `sources/androidx/compose/ui/platform/Q.java:219`
  `synchronized (this.f20630A) {`
- `sources/androidx/compose/ui/platform/r.java:915`
  `handler2.post(new Runnable() { // from class: androidx.compose.ui.platform.s`
- `sources/androidx/compose/ui/window/b.java:221`
  `/* JADX WARN: Unsupported multi-entry loop pattern (BACK_EDGE: B:12:0x0033 -> B:14:0x0036). Please report as a decompilation issue!!! */`
- `sources/androidx/constraintlayout/widget/d.java:130`
  `/* JADX WARN: Failed to restore switch over string. Please report as a decompilation issue */`
- `sources/androidx/constraintlayout/widget/e.java:2661`
  `/* JADX WARN: Failed to restore switch over string. Please report as a decompilation issue */`
- `sources/androidx/constraintlayout/widget/i.java:1257`
  `public static final int[] f21988k5 = {R.attr.framePosition, R.attr.motionTarget, R.attr.motion_postLayoutCollision, R.attr.motion_triggerOnCollision, R.attr.onCross, R.attr.onNegativeCross, R.attr.onPositiveCross, R.attr.triggerId, R.attr.triggerReceiver, R.attr.triggerSlack, R.attr.viewTransitionOn...`
- `sources/androidx/core/app/g.java:37`
  `/* JADX WARN: Failed to restore switch over string. Please report as a decompilation issue */`
- `sources/androidx/core/os/d.java:57`
  `synchronized (this) {`

## BR095

paper_id: B025
paper_title: Why Eve and Mallory Still Love Android: Revisiting TLS (In)Security in Android Applications

- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$avd_hide_password__0.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$avd_hide_password__1.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$avd_hide_password__2.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$avd_show_password__0.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$avd_show_password__1.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$avd_show_password__2.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$m3_avd_hide_password__0.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$m3_avd_hide_password__1.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$m3_avd_show_password__0.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$m3_avd_show_password__1.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_ab_back_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_arrow_drop_right_black_24dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_clear_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_go_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_menu_copy_mtrl_am_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_menu_cut_mtrl_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_menu_overflow_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_menu_paste_mtrl_am_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_menu_selectall_mtrl_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_menu_share_mtrl_alpha.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_ic_voice_search_api_material.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_seekbar_tick_mark_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_star_black_48dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_star_half_black_48dp.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_text_cursor_material.xml:2`
  `<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/abc_vector_test.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/arrow_down.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/arrow_down_to_line.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/arrow_up.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/arrow_up_to_line.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/avd_hide_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_hide_password__0_res_0x7f080000">`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/avd_show_password.xml:2`
  `<animated-vector xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt" android:drawable="@drawable/_avd_show_password__0_res_0x7f080003">`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/btn_checkbox_checked_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/btn_checkbox_unchecked_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/btn_radio_off_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/btn_radio_on_mtrl.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/design_ic_visibility.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/design_ic_visibility_off.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_bell.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_bluetooth.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_bullet_list.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_caret_down.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_caret_left.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_caret_right.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_caret_up.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_check.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_check_circle.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_circle.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_clear.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_edit.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_filter.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_filter_funnel.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_gear.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_horizontal_link.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_info.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_lightbulb.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_menu_item.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_minus.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_plus.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_refresh.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_search.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_share.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_signal_stength_0.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_signal_stength_1.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_signal_stength_2.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_signal_stength_3.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_signal_stength_4.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_signal_stength_5.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_sort.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_vertical_ellipsis.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_virtual_devices.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_warning_circle.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/icon_x.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/ic_arrow_back_black_24.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/ic_arrow_forward.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/ic_backspace.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/ic_bluetooth_disabled.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/ic_bonded.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/ic_check.xml:2`
  `<vector xmlns:android="http://schemas.android.com/apk/res/android"`

## BR096

paper_id: B011
paper_title: Locking it down: The privacy and security of mobile medication apps

- `resources/com.punchthrough.lightblueexplorer.apk/res/color/design_box_stroke_color.xml:2`
  `<selector xmlns:android="http://schemas.android.com/apk/res/android">`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$mtrl_switch_thumb_checked_unchecked__1.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$mtrl_switch_thumb_unchecked_checked__0.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/drawable/$mtrl_switch_thumb_unchecked_checked__1.xml:2`
  `<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android" xmlns:aapt="http://schemas.android.com/aapt"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/layout/design_text_input_end_icon.xml:2`
  `<com.google.android.material.internal.CheckableImageButton xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/layout/design_text_input_start_icon.xml:2`
  `<com.google.android.material.internal.CheckableImageButton xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/layout/material_chip_input_combo.xml:2`
  `<com.google.android.material.timepicker.ChipTextInputComboView xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/layout/material_time_input.xml:2`
  `<com.google.android.material.textfield.TextInputLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/layout/mtrl_picker_text_input_date.xml:2`
  `<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"`
- `resources/com.punchthrough.lightblueexplorer.apk/res/raw/firebase_common_keep.xml:2`
  `<resources xmlns:tools="http://schemas.android.com/tools"`
- `resources/res/values/strings.xml:70`
  `<string name="apache_license">Apache License\n\n Version 2.0, January 2004\n\n http://www.apache.org/licenses/\n\n TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION\n\n 1. Definitions.\n\n \"License\" shall mean the terms and conditions for use, reproduction, and distribution as defined b...`
- `resources/res/values/strings.xml:303`
  `<string name="firebase_database_url">https://lightblue-explorer.firebaseio.com</string>`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:193`
  `f26950l = c2680q3E.c("measurement.sgtm.google_signal.url", "https://app-measurement.com/s/d");`
- `sources/com/google/android/gms/internal/measurement/C2560c6.java:238`
  `f26939c0 = c2680q3E.c("measurement.upload.url", "https://app-measurement.com/a");`
- `sources/com/google/android/gms/measurement/internal/C2980n4.java:30`
  `bundleA = d6VarG.A(Uri.parse("https://google.com/search?" + str2), z10);`
- `sources/com/google/android/gms/measurement/internal/G.java:491`
  `f28468r = F("measurement.upload.url", "https://app-measurement.com/a", new Z1() { // from class: com.google.android.gms.measurement.internal.v0`
- `sources/com/google/firebase/installations/c.java:332`
  `AbstractC4310p.g(n(), "Please set your Application ID. A valid Firebase App ID is required to communicate with Firebase server APIs: It identifies your application with Firebase.Please refer to https://firebase.google.com/support/privacy/init-options.");`
- `sources/com/google/firebase/installations/c.java:333`
  `AbstractC4310p.g(u(), "Please set your Project ID. A valid Firebase Project ID is required to communicate with Firebase server APIs: It identifies your application with Firebase.Please refer to https://firebase.google.com/support/privacy/init-options.");`
- `sources/com/google/firebase/installations/c.java:334`
  `AbstractC4310p.g(m(), "Please set a valid API key. A Firebase API key is required to communicate with Firebase server APIs: It authenticates your project with Google.Please refer to https://firebase.google.com/support/privacy/init-options.");`
- `sources/com/google/firebase/installations/c.java:335`
  `AbstractC4310p.b(i.h(n()), "Please set your Application ID. A valid Firebase App ID is required to communicate with Firebase server APIs: It identifies your application with Firebase.Please refer to https://firebase.google.com/support/privacy/init-options.");`
- `sources/com/google/firebase/installations/c.java:336`
  `AbstractC4310p.b(i.g(m()), "Please set a valid API key. A Firebase API key is required to communicate with Firebase server APIs: It authenticates your project with Google.Please refer to https://firebase.google.com/support/privacy/init-options.");`
- `sources/o5/a.java:72`
  `Object objB = new y.b().c("https://io.adafruit.com/api/v2/").a(b9.a.f(rVar)).d().b(P5.a.class);`
- `sources/X/g.java:23`
  `Q.d("FlashAvailability", String.format("Exception thrown while checking for flash availability on device not known to throw exceptions during this check. Please file an issue at https://issuetracker.google.com/issues/new?component=618491&template=1257717 with this error message [Manufacturer: %s, Mo...`

## BR098

paper_id: B008
paper_title: Your Signal, Their Data: An Empirical Privacy Analysis of Wireless-scanning SDKs in Android

- `sources/X5/C4736b.java:37`
  `AbstractC1838t.c(yVarD, "Retrofit.Builder()\n     …ent)\n            .build()");`
