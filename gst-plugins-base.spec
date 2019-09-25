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
%define libgl %mklibname %{sname}gl %{api} %{major}
%define devname %mklibname %{name} %{api} -d


Summary:	GStreamer Streaming-media framework plug-ins
Name:		gst-plugins-base
Version:	1.16.1
Release:	1
License:	LGPLv2+
Group:		Sound
Url:		http://gstreamer.freedesktop.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gst-plugins-base/%(echo %{version}|cut -d. -f1-2)/%{name}-%{version}.tar.xz
Patch0:		align.patch
BuildRequires:	cdda-devel
BuildRequires:	meson
BuildRequires:	iso-codes-devel
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(graphene-1.0)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(orc-0.4)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(xv)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(sdl2)
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
Group:          System/Libraries
Summary:        GStreamer plugin libraries
Obsoletes:      %{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

%description -n %{liballocators}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{girallocators}
Summary:        GObject Introspection interface libraries for %{liballocators}
Group:          System/Libraries
Obsoletes:      %{_lib}gstreamer-plugins-base1.0_0 < 1.0.5-1

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


%package -n %{libaudiomixer}
Group:<><------>System/Libraries
Summary:<------>GStreamer plugin libraries

%description -n %{libaudiomixer}
This package contain the basic audiomixer library.


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
This package contain the basic audio and video playback 
library and
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

%package -n %{libgl}
Summary:	Gstreamer plugin libraries for %{libgl}
Group:		System/Libraries

%description -n %{libgl}
This package contain the gst opengl library.


%package -n %{devname}
Summary:	GStreamer Plugin Library Headers
Group:		Development/C
Requires:       %{liballocators} = %{version}-%{release}
Requires:       %{girallocators} = %{version}-%{release}
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

%prep
%autosetup -p1

%build
#export CC=gcc
#export CXX=g++
export CXXFLAGS+="%{optflags} -std=gnu++14"
%meson -Dtremor=disabled -Dexamples=disabled -Dgtk_doc=disabled
%meson_build

%if %{enable_check}
%check
cd tests/check
%make check
%endif

%install
%meson_install
%find_lang %{name}-%{api}

%files -n %{oname}-plugins-base -f %{name}-%{api}.lang
%doc AUTHORS COPYING README NEWS
%{_bindir}/gst-device-monitor-%{api}
%{_bindir}/gst-discoverer-%{api}
%{_bindir}/gst-play-%{api}
%dir %{_datadir}/gst-plugins-base
%dir %{_datadir}/gst-plugins-base/%{api}
%{_datadir}/gst-plugins-base/%{api}/license-translations.dict
%{_mandir}/man1/gst-device-monitor-%{api}.1*
%{_mandir}/man1/gst-play-%{api}.1*
%{_mandir}/man1/gst-discoverer-%{api}.1*
# non-core plugins without external dependencies
%{_libdir}/gstreamer-%{api}/libgstalsa.so
%{_libdir}/gstreamer-%{api}/libgstadder.so
%{_libdir}/gstreamer-%{api}/libgstapp.so
%{_libdir}/gstreamer-%{api}/libgstaudioconvert.so
%{_libdir}/gstreamer-%{api}/libgstaudiorate.so
%{_libdir}/gstreamer-%{api}/libgstaudioresample.so
%{_libdir}/gstreamer-%{api}/libgstaudiotestsrc.so
%{_libdir}/gstreamer-%{api}/libgstaudiomixer.so
%{_libdir}/gstreamer-%{api}/libgstgio.so
%{_libdir}/gstreamer-%{api}/libgstogg.so
%{_libdir}/gstreamer-%{api}/libgstopus.so
%{_libdir}/gstreamer-%{api}/libgstpango.so
%{_libdir}/gstreamer-%{api}/libgstplayback.so
%{_libdir}/gstreamer-%{api}/libgstsubparse.so
%{_libdir}/gstreamer-%{api}/libgsttcp.so
%{_libdir}/gstreamer-%{api}/libgsttheora.so
%{_libdir}/gstreamer-%{api}/libgsttypefindfunctions.so
%{_libdir}/gstreamer-%{api}/libgstvideoconvert.so
%{_libdir}/gstreamer-%{api}/libgstvideotestsrc.so
%{_libdir}/gstreamer-%{api}/libgstvideorate.so
%{_libdir}/gstreamer-%{api}/libgstvideoscale.so
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

%files -n %{girapp}
%{_libdir}/girepository-1.0/GstApp-%{api}.typelib

%files -n %{giraudio}
%{_libdir}/girepository-1.0/GstAudio-%{api}.typelib

%files -n %{girpbutils}
%{_libdir}/girepository-1.0/GstPbutils-%{api}.typelib

%files -n %{girrtp}
%{_libdir}/girepository-1.0/GstRtp-%{api}.typelib

%files -n %{girrtsp}
%{_libdir}/girepository-1.0/GstRtsp-%{api}.typelib

%files -n %{girsdp}
%{_libdir}/girepository-1.0/GstSdp-%{api}.typelib

%files -n %{girtag}
%{_libdir}/girepository-1.0/GstTag-%{api}.typelib

%files -n %{girvideo}
%{_libdir}/girepository-1.0/GstVideo-%{api}.typelib

%files -n %{girgl}
%{_libdir}/girepository-1.0/GstGL-%{api}.typelib

%files -n %{devname}
%doc docs/libs/html docs/plugins/html
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
%{_libdir}/pkgconfig/gstreamer-gl-1.0.pc
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

#% {_datadir}/gtk-doc/html/*
%{_datadir}/gir-1.0/GstAllocators-%{api}.gir
%{_datadir}/gir-1.0/GstApp-%{api}.gir
%{_datadir}/gir-1.0/GstAudio-%{api}.gir
%{_datadir}/gir-1.0/GstPbutils-%{api}.gir
%{_datadir}/gir-1.0/GstRtp-%{api}.gir
%{_datadir}/gir-1.0/GstRtsp-%{api}.gir
%{_datadir}/gir-1.0/GstSdp-%{api}.gir
%{_datadir}/gir-1.0/GstTag-%{api}.gir
%{_datadir}/gir-1.0/GstVideo-%{api}.gir
%{_datadir}/gir-1.0/GstGL-%{api}.gir

%files -n %{oname}-cdparanoia
%{_libdir}/gstreamer-%{api}/libgstcdparanoia.so

%if %{build_libvisual}
%files -n %{oname}-libvisual
%{_libdir}/gstreamer-%{api}/libgstlibvisual.so
%endif

