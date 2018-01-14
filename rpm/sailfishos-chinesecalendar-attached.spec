# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       jolla-settings-gost-button-status

# >> macros
BuildArch: noarch
# << macros

Summary:    Status bar icon for gost
Version:    0.1.0
Release:    1
Group:      Qt/Qt
License:    TODO
Source0:    %{name}-%{version}.tar.bz2
# Requires:   patchmanager
Requires:   jolla-settings-gost-button >= 0.1.4-3
%description
Status bar icon for gost


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/share/patchmanager/patches/jolla-settings-gost-button-status
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/jolla-settings-gost-button-status
mkdir -p %{buildroot}/usr/share/lipstick-jolla-home-qt5/statusarea
cp patch/GostStatusIndicator.qml %{buildroot}/usr/share/lipstick-jolla-home-qt5/statusarea
# << install pre

# >> install post
# << install post

%pre
# >> pre
if [ -f /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u jolla-settings-gost-button-status || true
fi
# << pre

%preun
# >> preun
if [ -f /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u jolla-settings-gost-button-status || true
fi
# << preun

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/jolla-settings-gost-button-status
%{_datadir}/lipstick-jolla-home-qt5/statusarea
# >> files
# << files
