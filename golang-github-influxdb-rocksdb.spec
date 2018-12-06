# http://github.com/influxdb/rocksdb
%global provider_prefix github.com/influxdb/rocksdb
%global gobaseipath     %{provider_prefix}
%global commit          7adff3eb33001c471c48cdcadf1b55462920b123
%global commitdate      20141010

%gocraftmeta -i

Name:           %{goname}
Version:        0
Release:        0.12.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Go wrapper for RocksDB
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{gobaseipath} prefix.

%prep
%gosetup

%install
%goinstall

%check
# Missing rocksdb/c.h
#%%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.20141010git7adff3e
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git7adff3e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git7adff3e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git7adff3e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git7adff3e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git7adff3e
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git7adff3e
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git7adff3e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git7adff3e
- Update to spec-2.1
  related: #1250486

* Thu Aug 06 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.3.git7adff3e
- Update spec file to spec-2.0
  resolves: #1250486

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git7adff3e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 27 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git7adff3e
- First package for Fedora
  resolves: #1186345

