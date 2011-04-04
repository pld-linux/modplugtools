Summary:	Audio player for libmodplug
Summary(pl.UTF-8):	Odtwarzacz muzyki dla libmodplug
Name:		modplugtools
Version:	0.5.3
Release:	1
License:	GPL v3
Group:		Applications/Sound
Source0:	http://downloads.sourceforge.net/modplug-xmms/%{name}-%{version}.tar.gz
# Source0-md5:	502b9a11e41219ceb7f2322d7521e2b3
URL:		http://modplug-xmms.sourceforge.net/
BuildRequires:	libao-devel >= 0.8.0
BuildRequires:	libmodplug-devel >= 0.8.8
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
Requires:	libao >= 0.8.0
Requires:	libmodplug >= 0.8.8
Conflicts:	xmms-input-modplug < 2.05-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audio playing tools for libmodplug (for the command line):
- modplugplay is written for the OSS audio output (/dev/dsp)
- modplug123 uses libAO for better cross platform audio support.

%description -l pl.UTF-8
Odtwarzacze muzyki dla libmodplug (uruchamiane z linii poleceń):
- modplugplay korzysta z wyjścia dźwięku OSS (/dev/dsp)
- modplug123 używa libAO, dzięki czemu jest bardziej przenośny.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/modplug123
%attr(755,root,root) %{_bindir}/modplugplay
