# gst-plugins-base is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define build_libvisual 1
%define build_docs 0
%define build_qtexamples 0
%define enable_check 0

%define sname gst
%define oname gstreamer%{api}

%define major 0
%define api 1.0
%define liballocators %mklibname %{sname}allocators %{api} %{major}
%define girallocators %mklibname %{sname}allocators-gir %{api}
%define libapp %mklibname %{sname}app %{api} %{major}
%define girapp %mklibname %{sname}app-gir %{api}
%define libaudio %mklibname %{sname}audio %{api} %{major}
%define giraudio %mklibname %{sname}audio-gir %{api}
%define libfft %mklibname %{sname}fft %{api} %{major}
%define libpbutils %mklibname %{sname}pbutils %{api} %{major}
%define girpbutils %mklibname %{sname}pbutils-gir %{api}
%define libriff %mklibname %{sname}riff %{api} %{major}
%define librtp %mklibname %{sname}rtp %{api} %{major}
%define girrtp %mklibname %{sname}rtp-gir %{api}
%define librtsp %mklibname %{sname}rtsp %{api} %{major}
%define girrtsp %mklibname %{sname}rtsp-gir %{api}
%define libsdp %mklibname %{sname}sdp %{api} %{major}
%define girsdp %mklibname %{sname}sdp-gir %{api}
%define libtag %mklibname %{sname}tag %{api} %{major}
%define girtag %mklibname %{sname}tag-gir %{api}
%define libvideo %mklibname %{sname}video %{api} %{major}
%define girvideo %mklibname %{sname}video-gir %{api}
%define girgl %mklibname %{sname}gl-gir %{api}
%define girglegl %mklibname %{sname}glegl-gir %{api}
%define girglwayland %mklibname %{sname}glwayland-gir %{api}
%define girglx11 %mklibname %{sname}glx11-gir %{api}
%define libgl %mklibname %{sname}gl %{api} %{major}
%define devname %mklibname %{name} %{api} -d

%define lib32allocators %mklib32name %{sname}allocators %{api} %{major}
%define lib32app %mklib32name %{sname}app %{api} %{major}
%define lib32audio %mklib32name %{sname}audio %{api} %{major}
%define lib32fft %mklib32name %{sname}fft %{api} %{major}
%define lib32pbutils %mklib32name %{sname}pbutils %{api} %{major}
%define lib32riff %mklib32name %{sname}riff %{api} %{major}
%define lib32rtp %mklib32name %{sname}rtp %{api} %{major}
%define lib32rtsp %mklib32name %{sname}rtsp %{api} %{major}
%define lib32sdp %mklib32name %{sname}sdp %{api} %{major}
%define lib32tag %mklib32name %{sname}tag %{api} %{major}
%define lib32video %mklib32name %{sname}video %{api} %{major}
%define lib32gl %mklib32name %{sname}gl %{api} %{major}
%define dev32name %mklib32name %{name} %{api} -d

Summary:	GStreamer Streaming-media framework plug-ins
Name:		gst-plugins-base
Version:	1.26.6
Release:	1
License:	LGPLv2+
Group:		Sound
Url:		https://gstreamer.freedesktop.org/
Source0:	https://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-%{version}.tar.xz
Patch0:		align.patch
BuildRequires:	cdda-devel
BuildRequires:	meson
BuildRequires:	gettext
BuildRequires:	iso-codes-devel
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(graphene-1.0)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gstreamer-1.0) >= 1.20.0
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(orc-0.4)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xv)
BuildRequires:	pkgconfig(inputproto)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	kernel-headers
BuildRequires:	git-core
%if %{build_libvisual}
BuildRequires:	pkgconfig(libvisual-0.4) >= 0.4
%endif
%ifarch %ix86
BuildRequires:	nasm => 0.90
%endif
%ifnarch %armx %mips %{riscv}
BuildRequires:	valgrind
BuildRequires:	pkgconfig(valgrind)
%endif
%if %{build_qtexamples}
BuildRequires:	qt5-devel
%endif
%if %{build_docs}
BuildRequires:	gtk-doc
%endif
%if %{enable_check}
#gw we need some fonts for the tests
BuildRequires:	fonts-ttf-dejavu
%endif
%if %{with compat32}
BuildRequires:	devel(libjpeg)
BuildRequires:	devel(libvorbis)
BuildRequires:	devel(libogg)
BuildRequires:	devel(libasound)
BuildRequires:	devel(libglib-2.0)
BuildRequires:	devel(libSDL2-2.0)
BuildRequires:	devel(libdrm)
BuildRequires:	devel(libgbm)
BuildRequires:	devel(libwayland-egl)
BuildRequires:	devel(libOpenGL)
BuildRequires:	devel(libGL)
BuildRequires:	devel(libGLU)
BuildRequires:	devel(libXv)
BuildRequires:	devel(libpango-1.0)
BuildRequires:	devel(libpangocairo-1.0)
BuildRequires:	devel(libpangoft2-1.0)
BuildRequires:	devel(libcairo)
BuildRequires:	devel(libXfixes)
BuildRequires:	devel(libXi)
BuildRequires:	devel(libX11)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmcp)
BuildRequires:	devel(libz)
BuildRequires:	devel(liblzma)
BuildRequires:	devel(libffi)
BuildRequires:	devel(libgio-2.0)
BuildRequires:	devel(libmount)
BuildRequires:	devel(libblkid)
BuildRequires:	devel(libgstreamer-1.0)
BuildRequires:	libunwind-nongnu-devel
BuildRequires:	devel(libdw)
BuildRequires:	devel(libgmodule-2.0)
BuildRequires:	devel(libpcre)
BuildRequires:	devel(libgobject-2.0)
BuildRequires:	devel(libgstbase-1.0)
BuildRequires:	devel(liborc-0.4)
BuildRequires:	devel(libpng16)
BuildRequires:	devel(libopus)
BuildRequires:	devel(libpangoft2-1.0)
BuildRequires:	devel(libfribidi)
BuildRequires:	devel(libharfbuzz)
BuildRequires:	devel(libfontconfig)
BuildRequires:	devel(libfreetype)
BuildRequires:	devel(libXrender)
BuildRequires:	devel(libXft)
BuildRequires:	devel(libbz2)
BuildRequires:	devel(libXext)
BuildRequires:	devel(libpixman-1)
BuildRequires:	devel(libexpat)
%endif

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

%package -n %{oname}-plugins-base
Group:		Sound
Summary:	GStreamer plugin libraries
Suggests:	gst-install-plugins-helper
Conflicts:	gstreamer1.0-plugins-bad <= 1.10.2-1

%description -n %{oname}-plugins-base
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of reference plugins, base classes for other
plugins, and helper libraries:
 * device plugins: x(v)imagesink, alsa, v4lsrc, cdparanoia
 * containers: ogg
 * codecs: vorbis, theora
 * text: textoverlay, subparse
 * sources: audiotestsrc, videotestsrc
 * network: tcp
 * typefind
 * audio processing: audioconvert, adder, audiorate, audioscale, volume
 * visualisation: libvisual
 * video processing: ffmpegcolorspace
 * aggregate elements: decodebin, playbin

%package -n %{liballocators}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

%description -n %{liballocators}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{girallocators}
Summary:	GObject Introspection interface libraries for %{liballocators}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

%description -n %{girallocators}
GObject Introspection interface libraries for %{liballocators}.

%package -n %{libapp}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

%description -n %{libapp}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{girapp}
Summary:	GObject Introspection interface libraries for %{libapp}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

%description -n %{girapp}
GObject Introspection interface libraries for %{libapp}.

%package -n %{libaudio}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

%description -n %{libaudio}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{giraudio}
Summary:	GObject Introspection interface libraries for %{libaudio}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

%description -n %{giraudio}
GObject Introspection interface libraries for %{libaudio}.

%package -n %{libfft}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

%description -n %{libfft}
This package contain the basic audio and video playback library and
the interfaces library.

#%package -n %{girfft}
#Summary:	GObject Introspection interface libraries for %{libfft}
#Group:		System/Libraries
#Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

#%description -n %{girfft}
#GObject Introspection interface libraries for %{libfft}.

%package -n %{libpbutils}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

%description -n %{libpbutils}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{girpbutils}
Summary:	GObject Introspection interface libraries for %{libpbutils}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

%description -n %{girpbutils}
GObject Introspection interface libraries for %{libpbutils}.

%package -n %{libriff}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

%description -n %{libriff}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{librtp}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

%description -n %{librtp}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{girrtp}
Summary:	GObject Introspection interface libraries for %{librtp}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

%description -n %{girrtp}
GObject Introspection interface libraries for %{librtp}.

%package -n %{librtsp}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

%description -n %{librtsp}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{girrtsp}
Summary:	GObject Introspection interface libraries for %{librtsp}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

%description -n %{girrtsp}
GObject Introspection interface libraries for %{librtsp}.

%package -n %{libsdp}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

%description -n %{libsdp}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{girsdp}
Summary:	GObject Introspection interface libraries for %{libsdp}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

%description -n %{girsdp}
GObject Introspection interface libraries for %{libsdp}.

%package -n %{libtag}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

%description -n %{libtag}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{girtag}
Summary:	GObject Introspection interface libraries for %{libtag}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

%description -n %{girtag}
GObject Introspection interface libraries for %{libtag}.

%package -n %{libvideo}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

%description -n %{libvideo}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{girvideo}
Summary:	GObject Introspection interface libraries for %{libvideo}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1
Obsoletes:	%{_lib}gstvideo-gir < 1.0.5-6

%description -n %{girvideo}
GObject Introspection interface libraries for %{libvideo}.


%package -n %{girgl}
Summary:	GObject Introspection interface libraries for %{girgl}
Group:		System/Libraries

%description -n %{girgl}
GObject Introspection interface libraries for %{girgl}

%package -n %{girglegl}
Summary:	GObject Introspection interface libraries for %{girglegl}
Group:		System/Libraries

%description -n %{girglegl}
GObject Introspection interface libraries for %{girglegl}

%package -n %{girglx11}
Summary:	GObject Introspection interface libraries for %{girglx11}
Group:		System/Libraries

%description -n %{girglx11}
GObject Introspection interface libraries for %{girglx11}

%package -n %{girglwayland}
Summary:	GObject Introspection interface libraries for %{girglwayland}
Group:		System/Libraries

%description -n %{girglwayland}
GObject Introspection interface libraries for %{girglwayland}

%package -n %{libgl}
Summary:	Gstreamer plugin libraries for %{libgl}
Group:		System/Libraries

%description -n %{libgl}
This package contain the gst opengl library.

%package -n %{devname}
Summary:	GStreamer Plugin Library Headers
Group:		Development/C
Requires:	%{liballocators} = %{version}-%{release}
Requires:	%{girallocators} = %{version}-%{release}
Requires:	%{libapp} = %{version}-%{release}
Requires:	%{girapp} = %{version}-%{release}
Requires:	%{libaudio} = %{version}-%{release}
Requires:	%{giraudio} = %{version}-%{release}
Requires:	%{libfft} = %{version}-%{release}
#Requires:	%{girfft} = %{version}-%{release}
Requires:	%{libpbutils} = %{version}-%{release}
Requires:	%{girpbutils} = %{version}-%{release}
Requires:	%{libriff} = %{version}-%{release}
Requires:	%{librtp} = %{version}-%{release}
Requires:	%{girrtp} = %{version}-%{release}
Requires:	%{librtsp} = %{version}-%{release}
Requires:	%{girrtsp} = %{version}-%{release}
Requires:	%{libsdp} = %{version}-%{release}
Requires:	%{girsdp} = %{version}-%{release}
Requires:	%{libtag} = %{version}-%{release}
Requires:	%{girtag} = %{version}-%{release}
Requires:	%{girvideo} = %{version}-%{release}
Requires:	%{libvideo} = %{version}-%{release}
Requires:	%{libgl} = %{version}-%{release}
Provides:	gstreamer-plugins-base-devel = %{version}-%{release}

%description -n %{devname}
GStreamer support libraries header files.

%package -n	%{oname}-cdparanoia
Summary:	Gstreamer plugin for CD audio input using CDParanoia IV
Group:		Sound
Requires:	%{oname}-plugins-base = %{version}-%{release}

%description -n	%{oname}-cdparanoia
Plugin for ripping audio tracks using cdparanoia under GStreamer

%if %{build_libvisual}
%package -n	%{oname}-libvisual
Summary:	GStreamer visualisations plug-in based on libvisual
Group:		Video
Requires:	%{oname}-plugins-base = %{version}-%{release}

%description -n	%{oname}-libvisual
This plugin makes visualisations based on libvisual available for
GStreamer applications.
%endif

%if %{with compat32}
%package -n %{lib32allocators}
Group:		System/Libraries
Summary:	GStreamer plugin libraries (32-bit)

%description -n %{lib32allocators}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{lib32app}
Group:		System/Libraries
Summary:	GStreamer plugin libraries (32-bit)

%description -n %{lib32app}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{lib32audio}
Summary:	GStreamer plugin libraries (32-bit)
Group:		System/Libraries

%description -n %{lib32audio}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{lib32fft}
Summary:	GStreamer plugin libraries (32-bit)
Group:		System/Libraries

%description -n %{lib32fft}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{lib32pbutils}
Summary:	GStreamer plugin libraries (32-bit)
Group:		System/Libraries

%description -n %{lib32pbutils}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{lib32riff}
Summary:	GStreamer plugin libraries (32-bit)
Group:		System/Libraries

%description -n %{lib32riff}
This package contain the basic audio and video playback
library and the interfaces library.

%package -n %{lib32rtp}
Summary:	GStreamer plugin libraries (32-bit)
Group:		System/Libraries

%description -n %{lib32rtp}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{lib32rtsp}
Summary:	GStreamer plugin libraries (32-bit)
Group:		System/Libraries

%description -n %{lib32rtsp}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{lib32sdp}
Summary:	GStreamer plugin libraries (32-bit)
Group:		System/Libraries

%description -n %{lib32sdp}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{lib32tag}
Summary:	GStreamer plugin libraries (32-bit)
Group:		System/Libraries

%description -n %{lib32tag}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{lib32video}
Summary:	GStreamer plugin libraries (32-bit)
Group:		System/Libraries

%description -n %{lib32video}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{lib32gl}
Summary:	Gstreamer plugin libraries for %{libgl} (32-bit)
Group:		System/Libraries

%description -n %{lib32gl}
This package contain the gst opengl library.

%package -n %{dev32name}
Summary:	GStreamer Plugin Library Headers (32-bit)
Group:		Development/C
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32allocators} = %{version}-%{release}
Requires:	%{lib32app} = %{version}-%{release}
Requires:	%{lib32audio} = %{version}-%{release}
Requires:	%{lib32fft} = %{version}-%{release}
Requires:	%{lib32pbutils} = %{version}-%{release}
Requires:	%{lib32riff} = %{version}-%{release}
Requires:	%{lib32rtp} = %{version}-%{release}
Requires:	%{lib32rtsp} = %{version}-%{release}
Requires:	%{lib32sdp} = %{version}-%{release}
Requires:	%{lib32tag} = %{version}-%{release}
Requires:	%{lib32video} = %{version}-%{release}
Requires:	%{lib32gl} = %{version}-%{release}

%description -n %{dev32name}
GStreamer support libraries header files.
%endif

%prep
%autosetup -p1
%if %{with compat32}
# FIXME we need to determine if any of the things
# we're disabling here to avoid dependency bloat
# could actually benefit wine
%meson32 --debug \
	-Dtremor=disabled \
	-Dexamples=disabled \
	-Dintrospection=disabled \
	-Dgl-graphene=disabled \
	-Dlibvisual=disabled \
	-Dtheora=disabled \
	-Dcdparanoia=disabled \
	-Dtests=disabled \
	-Ddoc=disabled
%endif

export CXXFLAGS+="%{optflags} -std=gnu++14"
%meson \
	-Dtremor=disabled \
	-Dexamples=disabled \
	-Dtests=disabled \
	-Ddoc=disabled

%build
%if %{with compat32}
%ninja_build -C build32
%endif
%meson_build

%if %{enable_check}
%check
cd tests/check
%make check
%endif

%install
%if %{with compat32}
%ninja_install -C build32
%endif
%meson_install
%find_lang %{name}-%{api}

%files -n %{oname}-plugins-base -f %{name}-%{api}.lang
%doc AUTHORS COPYING README* NEWS
%{_bindir}/gst-device-monitor-%{api}
%{_bindir}/gst-discoverer-%{api}
%{_bindir}/gst-play-%{api}
%dir %{_datadir}/gst-plugins-base
%dir %{_datadir}/gst-plugins-base/%{api}
%{_datadir}/gst-plugins-base/%{api}/license-translations.dict
%doc %{_mandir}/man1/gst-device-monitor-%{api}.1*
%doc %{_mandir}/man1/gst-play-%{api}.1*
%doc %{_mandir}/man1/gst-discoverer-%{api}.1*
# non-core plugins without external dependencies
%{_libdir}/gstreamer-%{api}/libgstalsa.so
%{_libdir}/gstreamer-%{api}/libgstadder.so
%{_libdir}/gstreamer-%{api}/libgstapp.so
%{_libdir}/gstreamer-%{api}/libgstaudioconvert.so
%{_libdir}/gstreamer-%{api}/libgstaudiorate.so
%{_libdir}/gstreamer-%{api}/libgstaudioresample.so
%{_libdir}/gstreamer-%{api}/libgstaudiotestsrc.so
%{_libdir}/gstreamer-%{api}/libgstaudiomixer.so
%{_libdir}/gstreamer-%{api}/libgstbasedebug.so
%{_libdir}/gstreamer-%{api}/libgstdsd.so
%{_libdir}/gstreamer-%{api}/libgstgio.so
%{_libdir}/gstreamer-%{api}/libgstogg.so
%{_libdir}/gstreamer-%{api}/libgstopus.so
%{_libdir}/gstreamer-%{api}/libgstpango.so
%{_libdir}/gstreamer-%{api}/libgstplayback.so
%{_libdir}/gstreamer-%{api}/libgstsubparse.so
%{_libdir}/gstreamer-%{api}/libgsttcp.so
%{_libdir}/gstreamer-%{api}/libgsttheora.so
%{_libdir}/gstreamer-%{api}/libgsttypefindfunctions.so
%{_libdir}/gstreamer-%{api}/libgstvideoconvertscale.so
%{_libdir}/gstreamer-%{api}/libgstvideotestsrc.so
%{_libdir}/gstreamer-%{api}/libgstvideorate.so
%{_libdir}/gstreamer-%{api}/libgstopengl.so
%{_libdir}/gstreamer-%{api}/libgstvolume.so
%{_libdir}/gstreamer-%{api}/libgstvorbis.so
%{_libdir}/gstreamer-%{api}/libgstximagesink.so
%{_libdir}/gstreamer-%{api}/libgstxvimagesink.so
%{_libdir}/gstreamer-%{api}/libgstencoding.so
%{_libdir}/gstreamer-%{api}/libgstpbtypes.so
%{_libdir}/gstreamer-%{api}/libgstrawparse.so

%files -n %{liballocators}
%{_libdir}/libgstallocators-%{api}.so.%{major}*

%files -n %{libapp}
%{_libdir}/libgstapp-%{api}.so.%{major}*

%files -n %{libaudio}
%{_libdir}/libgstaudio-%{api}.so.%{major}*

%files -n %{libfft}
%{_libdir}/libgstfft-%{api}.so.%{major}*

%files -n %{libpbutils}
%{_libdir}/libgstpbutils-%{api}.so.%{major}*

%files -n %{libriff}
%{_libdir}/libgstriff-%{api}.so.%{major}*

%files -n %{librtp}
%{_libdir}/libgstrtp-%{api}.so.%{major}*

%files -n %{librtsp}
%{_libdir}/libgstrtsp-%{api}.so.%{major}*

%files -n %{libsdp}
%{_libdir}/libgstsdp-%{api}.so.%{major}*

%files -n %{libtag}
%{_libdir}/libgsttag-%{api}.so.%{major}*

%files -n %{libvideo}
%{_libdir}/libgstvideo-%{api}.so.%{major}*

%files -n %{libgl}
%{_libdir}/libgstgl-%{api}.so.%{major}*

%files -n %{girallocators}
%{_libdir}/girepository-1.0/GstAllocators-%{api}.typelib
%{_datadir}/gir-1.0/GstAllocators-%{api}.gir

%files -n %{girapp}
%{_libdir}/girepository-1.0/GstApp-%{api}.typelib
%{_datadir}/gir-1.0/GstApp-%{api}.gir

%files -n %{giraudio}
%{_libdir}/girepository-1.0/GstAudio-%{api}.typelib
%{_datadir}/gir-1.0/GstAudio-%{api}.gir

%files -n %{girpbutils}
%{_libdir}/girepository-1.0/GstPbutils-%{api}.typelib
%{_datadir}/gir-1.0/GstPbutils-%{api}.gir

%files -n %{girrtp}
%{_libdir}/girepository-1.0/GstRtp-%{api}.typelib
%{_datadir}/gir-1.0/GstRtp-%{api}.gir

%files -n %{girrtsp}
%{_libdir}/girepository-1.0/GstRtsp-%{api}.typelib
%{_datadir}/gir-1.0/GstRtsp-%{api}.gir

%files -n %{girsdp}
%{_libdir}/girepository-1.0/GstSdp-%{api}.typelib
%{_datadir}/gir-1.0/GstSdp-%{api}.gir

%files -n %{girtag}
%{_libdir}/girepository-1.0/GstTag-%{api}.typelib
%{_datadir}/gir-1.0/GstTag-%{api}.gir

%files -n %{girvideo}
%{_libdir}/girepository-1.0/GstVideo-%{api}.typelib
%{_datadir}/gir-1.0/GstVideo-%{api}.gir

%files -n %{girgl}
%{_libdir}/girepository-1.0/GstGL-%{api}.typelib
%{_datadir}/gir-1.0/GstGL-%{api}.gir

%files -n %{girglegl}
%{_libdir}/girepository-1.0/GstGLEGL-%{api}.typelib
%{_datadir}/gir-1.0/GstGLEGL-%{api}.gir

%files -n %{girglwayland}
%{_libdir}/girepository-1.0/GstGLWayland-1.0.typelib
%{_datadir}/gir-1.0/GstGLWayland-%{api}.gir

%files -n %{girglx11}
%{_libdir}/girepository-1.0/GstGLX11-1.0.typelib
%{_datadir}/gir-1.0/GstGLX11-%{api}.gir

%files -n %{devname}
%{_includedir}/gstreamer-%{api}/gst/allocators
%{_includedir}/gstreamer-%{api}/gst/app/
%{_includedir}/gstreamer-%{api}/gst/audio
%{_includedir}/gstreamer-%{api}/gst/fft
%{_includedir}/gstreamer-%{api}/gst/pbutils
%{_includedir}/gstreamer-%{api}/gst/riff
%{_includedir}/gstreamer-%{api}/gst/rtsp
%{_includedir}/gstreamer-%{api}/gst/sdp
%{_includedir}/gstreamer-%{api}/gst/tag/
%{_includedir}/gstreamer-%{api}/gst/video/
%{_includedir}/gstreamer-%{api}/gst/rtp
%{_includedir}/gstreamer-%{api}/gst/gl
%{_libdir}/gstreamer-%{api}/include/gst/gl/gstglconfig.h
%{_libdir}/pkgconfig/gstreamer-allocators-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-app-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-audio-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-fft-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-pbutils-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-plugins-base-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-riff-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-rtp-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-rtsp-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-sdp-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-tag-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-video-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-gl-egl-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-gl-prototypes-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-gl-wayland-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-gl-x11-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-gl-%{api}.pc
%{_libdir}/libgstallocators-%{api}.so
%{_libdir}/libgstaudio-%{api}.so
%{_libdir}/libgstapp-%{api}.so
%{_libdir}/libgstfft-%{api}.so
%{_libdir}/libgstpbutils-%{api}.so
%{_libdir}/libgstriff-%{api}.so
%{_libdir}/libgstrtp-%{api}.so
%{_libdir}/libgstrtsp-%{api}.so
%{_libdir}/libgsttag-%{api}.so
%{_libdir}/libgstsdp-%{api}.so
%{_libdir}/libgstvideo-%{api}.so
%{_libdir}/libgstgl-%{api}.so
%{_libdir}/gstreamer-%{api}/libgstcompositor.so
%{_libdir}/gstreamer-%{api}/libgstoverlaycomposition.so

%files -n %{oname}-cdparanoia
%{_libdir}/gstreamer-%{api}/libgstcdparanoia.so

%if %{build_libvisual}
%files -n %{oname}-libvisual
%{_libdir}/gstreamer-%{api}/libgstlibvisual.so
%endif

%if %{with compat32}
%files -n %{lib32allocators}
%{_prefix}/lib/libgstallocators-%{api}.so.%{major}*

%files -n %{lib32app}
%{_prefix}/lib/libgstapp-%{api}.so.%{major}*
%{_datadir}/gir-1.0/GstApp-%{api}.gir

%files -n %{lib32audio}
%{_prefix}/lib/libgstaudio-%{api}.so.%{major}*
%{_prefix}/lib/gstreamer-%{api}/libgstalsa.so
%{_prefix}/lib/gstreamer-%{api}/libgstadder.so
%{_prefix}/lib/gstreamer-%{api}/libgstapp.so
%{_prefix}/lib/gstreamer-%{api}/libgstaudioconvert.so
%{_prefix}/lib/gstreamer-%{api}/libgstaudiorate.so
%{_prefix}/lib/gstreamer-%{api}/libgstaudioresample.so
%{_prefix}/lib/gstreamer-%{api}/libgstaudiotestsrc.so
%{_prefix}/lib/gstreamer-%{api}/libgstaudiomixer.so
%{_prefix}/lib/gstreamer-%{api}/libgstbasedebug.so
%{_prefix}/lib/gstreamer-%{api}/libgstdsd.so
%{_prefix}/lib/gstreamer-%{api}/libgstencoding.so
%{_prefix}/lib/gstreamer-%{api}/libgstogg.so
%{_prefix}/lib/gstreamer-%{api}/libgstopus.so
%{_prefix}/lib/gstreamer-%{api}/libgstgio.so
%{_prefix}/lib/gstreamer-%{api}/libgsttypefindfunctions.so
%{_prefix}/lib/gstreamer-%{api}/libgstpbtypes.so
%{_prefix}/lib/gstreamer-%{api}/libgstvolume.so
%{_prefix}/lib/gstreamer-%{api}/libgstvorbis.so

%files -n %{lib32fft}
%{_prefix}/lib/libgstfft-%{api}.so.%{major}*

%files -n %{lib32pbutils}
%{_prefix}/lib/libgstpbutils-%{api}.so.%{major}*

%files -n %{lib32riff}
%{_prefix}/lib/libgstriff-%{api}.so.%{major}*

%files -n %{lib32rtp}
%{_prefix}/lib/libgstrtp-%{api}.so.%{major}*

%files -n %{lib32rtsp}
%{_prefix}/lib/libgstrtsp-%{api}.so.%{major}*

%files -n %{lib32sdp}
%{_prefix}/lib/libgstsdp-%{api}.so.%{major}*

%files -n %{lib32tag}
%{_prefix}/lib/libgsttag-%{api}.so.%{major}*

%files -n %{lib32video}
%{_prefix}/lib/libgstvideo-%{api}.so.%{major}*
%{_prefix}/lib/gstreamer-%{api}/libgstpango.so
%{_prefix}/lib/gstreamer-%{api}/libgstplayback.so
%{_prefix}/lib/gstreamer-%{api}/libgstsubparse.so
%{_prefix}/lib/gstreamer-%{api}/libgsttcp.so
%{_prefix}/lib/gstreamer-%{api}/libgstvideoconvertscale.so
%{_prefix}/lib/gstreamer-%{api}/libgstvideotestsrc.so
%{_prefix}/lib/gstreamer-%{api}/libgstvideorate.so
%{_prefix}/lib/gstreamer-%{api}/libgstopengl.so
%{_prefix}/lib/gstreamer-%{api}/libgstximagesink.so
%{_prefix}/lib/gstreamer-%{api}/libgstxvimagesink.so
%{_prefix}/lib/gstreamer-%{api}/libgstrawparse.so

%files -n %{lib32gl}
%{_prefix}/lib/libgstgl-%{api}.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/gstreamer-%{api}/include/gst/gl/gstglconfig.h
%{_prefix}/lib/pkgconfig/gstreamer-allocators-%{api}.pc
%{_prefix}/lib/pkgconfig/gstreamer-app-%{api}.pc
%{_prefix}/lib/pkgconfig/gstreamer-audio-%{api}.pc
%{_prefix}/lib/pkgconfig/gstreamer-fft-%{api}.pc
%{_prefix}/lib/pkgconfig/gstreamer-pbutils-%{api}.pc
%{_prefix}/lib/pkgconfig/gstreamer-plugins-base-%{api}.pc
%{_prefix}/lib/pkgconfig/gstreamer-riff-%{api}.pc
%{_prefix}/lib/pkgconfig/gstreamer-rtp-%{api}.pc
%{_prefix}/lib/pkgconfig/gstreamer-rtsp-%{api}.pc
%{_prefix}/lib/pkgconfig/gstreamer-sdp-%{api}.pc
%{_prefix}/lib/pkgconfig/gstreamer-tag-%{api}.pc
%{_prefix}/lib/pkgconfig/gstreamer-video-%{api}.pc
%{_prefix}/lib/pkgconfig/gstreamer-gl-%{api}.pc
%{_prefix}/lib/pkgconfig/gstreamer-gl-egl-%{api}.pc
%{_prefix}/lib/pkgconfig/gstreamer-gl-prototypes-%{api}.pc
%{_prefix}/lib/pkgconfig/gstreamer-gl-wayland-%{api}.pc
%{_prefix}/lib/pkgconfig/gstreamer-gl-x11-%{api}.pc

%{_prefix}/lib/libgstallocators-%{api}.so
%{_prefix}/lib/libgstaudio-%{api}.so
%{_prefix}/lib/libgstapp-%{api}.so
%{_prefix}/lib/libgstfft-%{api}.so
%{_prefix}/lib/libgstpbutils-%{api}.so
%{_prefix}/lib/libgstriff-%{api}.so
%{_prefix}/lib/libgstrtp-%{api}.so
%{_prefix}/lib/libgstrtsp-%{api}.so
%{_prefix}/lib/libgsttag-%{api}.so
%{_prefix}/lib/libgstsdp-%{api}.so
%{_prefix}/lib/libgstvideo-%{api}.so
%{_prefix}/lib/libgstgl-%{api}.so
%{_prefix}/lib/gstreamer-%{api}/libgstcompositor.so
%{_prefix}/lib/gstreamer-%{api}/libgstoverlaycomposition.so
%endif
