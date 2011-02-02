
Name:		xwii
License:	GPL
Group:		System/Kernel and hardware
URL:		http://pingus.seul.org/~grumbel/xwii/
Autoreqprov:	on
Version:	2.9.4
Release:	%mkrel 1
Summary:	Nintendo Wiimote Driver
Source:		http://pingus.seul.org/~grumbel/xwii/%{name}_%{version}_src.tar.gz
Patch0:		xwii_2.9.4-linkage.patch
BuildRequires:	libx11-devel
BuildRequires:	libxtst-devel
BuildRequires:	wiiuse
BuildRequires:	wiiuse-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

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
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xwii
# %{_docdir}/*
%{_datadir}/*

