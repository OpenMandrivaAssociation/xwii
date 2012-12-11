
Name:		xwii
License:	GPL
Group:		System/Kernel and hardware
URL:		http://pingus.seul.org/~grumbel/xwii/
Version:	2.9.4
Release:	4
Summary:	Nintendo Wiimote Driver
Source:		http://pingus.seul.org/~grumbel/xwii/%{name}_%{version}_src.tar.gz
Patch0:		xwii_2.9.4-linkage.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(xi)
BuildRequires:	wiiuse
BuildRequires:	wiiuse-devel

%description
Userspace Nintendo Wiimote Driver for Linux

%prep
%setup -q -n %{name}_%{version}_src
%patch0 -p0 -b .link
rm -fr wiiuse_v0.12

%build
ln -s %{_libdir}/libwiiuse.so ./
%make PREFIX=%{_prefix}

%install
install -d %{buildroot}%{_docdir}/%{name}/
install -d %{buildroot}%{_datadir}/%{name}/

install -Dp xwii %{buildroot}%{_bindir}/%{name}
install -Dp Documentation/* %{buildroot}%{_docdir}/%{name}/
install -Dp profiles/* %{buildroot}%{_datadir}/%{name}/

%clean

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_docdir}/%{name}
%{_datadir}/%{name}



%changelog
* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 2.9.4-3mdv2011.0
+ Revision: 640479
- rebuild to obsolete old packages

* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 2.9.4-2
+ Revision: 635132
- bump rel
- fix link and build

* Fri Jan 28 2011 Zombie Ryushu <ryushu@mandriva.org> 2.9.4-1
+ Revision: 633640
- Fix wiiuse dependency
- imported package xwii


* Thu Dec 11 2008 - uli@suse.de
- fixed bugs found by rpmlint
