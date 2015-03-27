# no matter what, ignores -lssl -lcrypto dependency of -lcurl
%define		_disable_ld_as_needed		1

%define		debug_package			%{nil}

Name:		megaglest
Version:	3.11.1
Release:	1
Summary:	Open Source 3d real time strategy game
License:	GPLv3+
Group:		Games/Strategy
Url:		http://megaglest.org/
Source0:	https://github.com/MegaGlest/megaglest-source/releases/download/3.11.1/megaglest-source-%{version}.tar.xz
# Correct usage of xvfb-run when generating manpages
Patch0:		%{name}-help2man.patch
# Do not fail with cryptic message if there are missing translations
# just use english text
Patch1:		%{name}-translation-missing.patch
# Use proper path to g3dviewer.ico in sources
Patch2:         %{name}-icon-path.patch
# Mandriva patch
Patch3:		%{name}-underlink.patch

BuildRequires:	cmake
BuildRequires:	help2man
BuildRequires:	subversion
BuildRequires:	x11-server-xvfb
BuildRequires:	icu-devel
BuildRequires:	jpeg-devel
BuildRequires:	libircclient-static-devel
BuildRequires:	miniupnpc-devel
BuildRequires:	wxgtku-devel
BuildRequires:	xerces-c-devel
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(ftgl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_net)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(zlib)
Requires:	glxinfo
Requires:	megaglest-data = %{version}
Requires:	p7zip

%description
MegaGlest is an open source 3D-real-time strategy game, where you control
the armies of one of seven different factions: Tech, Magic, Egyptians,
Indians, Norsemen, Persian or Romans. The game is setup in one of 16
naturally looking settings, which -like the unit models- are crafted with
great appreciation for detail. Additional game data can be downloaded from
within the game at no cost.

#-----------------------------------------------------------------------
%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

#-----------------------------------------------------------------------
%build
sed -i -e 's/-O3//g' `find . -name CMakeLists.txt`
%cmake									\
	-DCMAKE_INSTALL_PREFIX=/					\
	-DMEGAGLEST_BIN_INSTALL_PATH=%{_gamesbindir}			\
	-DMEGAGLEST_ICON_INSTALL_PATH=%{_iconsdir}			\
	-DMEGAGLEST_DATA_INSTALL_PATH=%{_gamesdatadir}/megaglest
%make

#-----------------------------------------------------------------------
%install
%makeinstall_std -C build
mv %{buildroot}/share/* %{buildroot}%{_datadir}
rmdir %{buildroot}/share
install -d %{buildroot}%{_gamesdatadir}/megaglest
for image in `ls %{buildroot}%{_iconsdir}`; do
    [ -e %{buildroot}%{_gamesdatadir}/$image ] ||
	ln -sf %{_iconsdir}/$image %{buildroot}%{_gamesdatadir}/megaglest
done
# installed by megaglest-data
rm %{buildroot}%{_gamesdatadir}/megaglest/megaglest.bmp
for file in megaglest megaglest_editor megaglest_g3dviewer; do
    desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/$file.desktop
done

#-----------------------------------------------------------------------
%files
%doc docs/AUTHORS.source_code.txt
%doc docs/CHANGELOG.txt
%doc docs/COPYRIGHT.source_code.txt
%doc docs/gnu_gpl_3.0.txt
%doc docs/README.txt
%{_datadir}/applications/%{name}*.desktop
%{_iconsdir}/*
%{_mandir}/man6/*.6*
%{_gamesbindir}/*
%{_gamesdatadir}/megaglest/*
