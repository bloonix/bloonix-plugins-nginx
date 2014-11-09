Summary: Bloonix plugins for nginx.
Name: bloonix-plugins-nginx
Version: 0.8
Release: 1%{dist}
License: Commercial
Group: Utilities/System
Distribution: RHEL and CentOS

Packager: Jonny Schulz <js@bloonix.de>
Vendor: Bloonix

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Source0: http://download.bloonix.de/sources/%{name}-%{version}.tar.gz
Requires: bloonix-core
Requires: curl
AutoReqProv: no

%description
bloonix-plugins-nginx provides plugins to check the nginx webserver.

%define blxdir /usr/lib/bloonix
%define docdir %{_docdir}/%{name}-%{version}

%prep
%setup -q -n %{name}-%{version}

%build
%{__perl} Configure.PL --prefix /usr
%{__make}

%install
rm -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
mkdir -p ${RPM_BUILD_ROOT}%{docdir}
install -c -m 0444 LICENSE ${RPM_BUILD_ROOT}%{docdir}/
install -c -m 0444 ChangeLog ${RPM_BUILD_ROOT}%{docdir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%dir %{blxdir}
%dir %{blxdir}/plugins
%{blxdir}/plugins/check-*
%{blxdir}/etc/plugins/plugin-*

%dir %attr(0755, root, root) %{docdir}
%doc %attr(0444, root, root) %{docdir}/ChangeLog
%doc %attr(0444, root, root) %{docdir}/LICENSE

%changelog
* Mon Nov 03 2014 Jonny Schulz <js@bloonix.de> - 0.8-1
- Updated the license information.
* Tue Aug 26 2014 Jonny Schulz <js@bloonix.de> - 0.7-1
- Licence added and old releases deleted.
* Sat Mar 23 2014 Jonny Schulz <js@bloonix.de> - 0.6-1
- Complete rewrite of all plugins.
* Sun Sep 16 2012 Jonny Schulz <js@bloonix.de> - 0.4-1
- Improved the yaml file handling.
- Updated the plugin-* files.
* Fri Jul 01 2011 Jonny Schulz <js@bloonix.de> - 0.2-1
- Renamed environment variable YAML_FILE_BASEDIR to
  PLUGIN_LIBDIR.
- Fixed wrong environment variable CHECK_SERVICE_NAME
  and renamed it to CHECK_COMMAND_NAME.
- Kicked unused option o_stat.
- Changed the default error status from WARNING to
  CRITICAL.
* Tue Jun 21 2011 Jonny Schulz <js@bloonix.de> - 0.1-1
- Initial release.
