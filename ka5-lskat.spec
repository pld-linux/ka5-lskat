%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		lskat
Summary:	lskat
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	17f73416721000ed6fccf8f727f9a898
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kconfig-devel >= 5.30.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.30.0
BuildRequires:	kf5-kcrash-devel >= 5.30.0
BuildRequires:	kf5-kdoctools-devel >= 5.30.0
BuildRequires:	kf5-kguiaddons-devel >= 5.30.0
BuildRequires:	kf5-ki18n-devel >= 5.30.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.30.0
BuildRequires:	kf5-kxmlgui-devel >= 5.30.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lieutnant Skat (from German "Offiziersskat") is a fun and engaging
card game for two players, where the second player is either live
opponent, or a built in artificial intelligence.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/lskat.categories
%attr(755,root,root) %{_bindir}/lskat
%{_desktopdir}/org.kde.lskat.desktop
%{_iconsdir}/hicolor/128x128/apps/lskat.png
%{_iconsdir}/hicolor/16x16/apps/lskat.png
%{_iconsdir}/hicolor/22x22/apps/lskat.png
%{_iconsdir}/hicolor/32x32/apps/lskat.png
%{_iconsdir}/hicolor/48x48/apps/lskat.png
%{_iconsdir}/hicolor/64x64/apps/lskat.png
%{_datadir}/kxmlgui5/lskat
%{_datadir}/lskat
%{_datadir}/metainfo/org.kde.lskat.appdata.xml
