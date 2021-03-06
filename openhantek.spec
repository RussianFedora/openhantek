%global gitcommit_full 9935f0a6defa78a77824d389472d9b3a7172a1aa
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
%global date 20180710

Name:           openhantek
Version:        0
Release:        1.%{date}git%{gitcommit}%{?dist}
Summary:        Hantek and compatible USB digital signal oscilloscope

#Contain nonfree firmware
License:        GPLv3+ and GPLv2+ and ASL 2.0 and nonfree
URL:            http://openhantek.org
Source0:        https://github.com/OpenHantek/openhantek/tarball/%{gitcommit_full}
Source1:        %{name}.desktop

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(Qt5)
BuildRequires:  fftw-devel
BuildRequires:  libusbx-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qttranslations
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  binutils-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  pkgconfig(udev)

Requires:       hicolor-icon-theme
Requires:       systemd-udev

%description
OpenHantek is a free software for Hantek and compatible
(Voltcraft/Darkwire/Protek/Acetech) USB digital signal oscilloscopes.
Supported devices: DSO2xxx Series, DSO52xx Series, 6022BE/BL.

%prep
%autosetup -n OpenHantek-%{name}-%{gitcommit}


%build
mkdir build
pushd build
    %cmake ..
    %make_build
popd

%install
pushd build
    %make_install
popd
mkdir -p %{buildroot}%{_udevrulesdir}
mv %{buildroot}/lib/udev/rules.d/60-hantek.rules %{buildroot}%{_udevrulesdir}
desktop-file-install --dir="%{buildroot}%{_datadir}/applications" %{SOURCE1}
install -p -D -m 644 %{name}/res/images/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%files
%license COPYING
%doc readme.md
%{_bindir}/OpenHantek
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_udevrulesdir}/60-hantek.*



%changelog
* Wed Jul 11 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 0-1.20180710git9935f0a
- Update to latest git

* Thu Mar 15 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 0-1.20180320git0eff8d4
- Initial package for Fedora
