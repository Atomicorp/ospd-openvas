Summary: OSPd-openvas
Name: OSPd-openvas
Version: 1.0.0
Release: RELEASE-AUTO%{?dist}.art
License: GPLv2
Group: Networking/Mail
URL: http://www.openvas.org
Source0: https://github.com/greenbone/ospd-openvas/archive/v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch

%if 0%{?fedora}
BuildRequires: python3-devel >= 2.2.1
BuildRequires: python3-setuptools
#Requires: %{python_libdir}
Requires: python3-dateutil
Requires: python3-paramiko
%endif

# Because the excludes keep breaking it
BuildRequires: /usr/bin/python3-config
BuildRequires: /usr/bin/easy_install-3.6

# Not all python36 dependencies are available
# It is not currently supportable
%if 0%{?rhel} == 7
BuildRequires:       python36-devel
BuildRequires:       python36-setuptools
#Requires: python3-lxml python3-configparser python3-dialog python3-paramiko
Requires: python36-paramiko
Requires: epel-release
Requires: python36-setuptools
Requires: python36-defusedxml

%endif







%description
OSPd

%prep
%setup -q -n ospd-openvas-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
#%license COPYING
#%doc CHANGELOG.md INSTALL README.md
/usr/lib/python3.6/site-packages/ospd_openvas*
/usr/bin/ospd-openvas

%changelog
* Thu Sep 14 2017 Scott R. Shinn <scott@atomicorp.com> - 1.2.0
- Initialize

