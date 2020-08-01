Summary: OSPd-openvas
Name: OSPd-openvas
Version: 1.0.1
Release: RELEASE-AUTO%{?dist}.art
License: GPLv2
Group: Networking/Mail
URL: http://www.openvas.org
Source0: https://github.com/greenbone/ospd-openvas/archive/v%{version}.tar.gz
Source1: ospd-openvas.service
Source2: tmpfile.ospd-openvas.conf
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
#AutoReq: no

%if 0%{?fedora}
BuildRequires: python3-devel >= 2.2.1
BuildRequires: python3-setuptools
#Requires: %{python_libdir}
Requires: python3-dateutil
Requires: python3-paramiko
%endif

# Because the excludes keep breaking it
BuildRequires: /usr/bin/python3-config

%if 0%{?rhel} >= 7
BuildRequires: /usr/bin/easy_install-3.6
%else
BuildRequires: /usr/bin/easy_install
%endif


# Not all python36 dependencies are available
# It is not currently supportable
#%if 0%{?rhel} == 7
#BuildRequires:       python36-devel
#BuildRequires:       python36-setuptools
##Requires: python3-lxml python3-configparser python3-dialog python3-paramiko
#Requires: python36-paramiko
#Requires: epel-release
#Requires: python36-setuptools
#Requires: python36-defusedxml
#%endif

# el8
Requires: python3-psutil
Requires: python3-redis
Requires: python3-lxml
Requires: python3-defusedxml
Requires: python3-paramiko


# cant find packaging thing on el8, wtf
#python36-devel-3.6.8-2.module_el8.1.0+245+c39af44f.x86_64 : Libraries and header files needed for Python development
#no
#/usr/bin/easy_install-3.6 no
# Original was to use platform-python-3.6.8-23.el8.x86_64


%description
OSPd

%prep
%setup -q -n ospd-openvas-%{version}


%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot}
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p $RPM_BUILD_ROOT/var/run/ospd/
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/ospd-openvas.service
%{__install} -d -m 0755 %{buildroot}%_tmpfilesdir/
%{__install} -Dp -m0755 %{SOURCE2} %{buildroot}%_tmpfilesdir/ospd-openvas.conf

%post
%systemd_post %{name}.service
/bin/systemd-tmpfiles --create %_tmpfilesdir/ospd-openvas.conf >/dev/null 2>&1 || :



%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
#%license COPYING
#%doc CHANGELOG.md INSTALL README.md
%attr(770,gvm,gvm) %dir /var/run/ospd/
/usr/lib/python*/site-packages/ospd_openvas*
/usr/bin/ospd-openvas
/usr/lib/systemd/system/ospd-openvas.service
%_tmpfilesdir/ospd-openvas.conf



%changelog
* Sun Jun 7 2020 Scott R. Shinn <scott@atomicorp.com> - 1.0.1
- Initialize

