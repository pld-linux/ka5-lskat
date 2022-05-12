#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.04.1
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		lskat
Summary:	lskat
Name:		ka5-%{kaname}
Version:	22.04.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	861d34aa65b03d879f7db3cf4de005f7
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
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kguiaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
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

%description -l pl.UTF-8
Lieutnant Skat (z niemieckiego "Offiziersskat") jest zabawną
i wciągającą grą karcianą dla dwóch graczy, gdzie drugi gracz może
być albo żywym rywalem, albo opartym na sztucznej inteligencji.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lskat
%{_desktopdir}/org.kde.lskat.desktop
%{_iconsdir}/hicolor/128x128/apps/lskat.png
%{_iconsdir}/hicolor/16x16/apps/lskat.png
%{_iconsdir}/hicolor/22x22/apps/lskat.png
%{_iconsdir}/hicolor/32x32/apps/lskat.png
%{_iconsdir}/hicolor/48x48/apps/lskat.png
%{_iconsdir}/hicolor/64x64/apps/lskat.png
%{_datadir}/lskat
%{_datadir}/metainfo/org.kde.lskat.appdata.xml
%{_datadir}/qlogging-categories5/lskat.categories
