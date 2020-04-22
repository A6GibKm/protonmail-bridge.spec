%global commit 409abba995e7add59ab8e0391dbe1f4132695fc0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}

Name:           protonmail-bridge
Version:        1.2.6
Release:        1%{?dist}
Summary:        Integrate ProtonMail paid account with any program that supports IMAP and SMTP

License:        GPLv3+
URL:            https://protonmail.com/bridge/
Source0:        https://github.com/ProtonMail/proton-bridge/archive/%{commit}/%{shortcommit}.tar.gz

Source1:        %{name}.appdata.xml
Source2:        %{name}.desktop

BuildRequires: make
BuildRequires: go
BuildRequires: g++
BuildRequires: libglvnd-devel
BuildRequires: libsecret-devel
BuildRequires: which

%description
ProtonMail Bridge (protonmail-bridge) Integrate ProtonMail paid
account with any program that supports IMAP and SMTP.

%prep
%setup -q -n proton-bridge-%{commit}
%build
export PATH=~/go/bin:$PATH
%make_build build VERSION=%{version}

%install
install -Dpm 744 cmd/Desktop-Bridge/deploy/linux/proton-bridge-%{commit} %{buildroot}%{_bindir}/%{name}
install -Dpm 644 cmd/Desktop-Bridge/deploy/linux/logo.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -Dpm 644 %{SOURCE1} %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
install -Dpm 644 %{SOURCE2} %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%license LICENSE

%changelog
* Wed Apr 22 2020 Maximiliano Sandoval <msandova@protonmail.com> - 1.2.6-1
- Initial spec
