Summary:	An xrandr clone for wlroots compositors
Name:		wlr-randr
Version:	0.2.0
Release:	2
License:	MIT
Group:		Applications
Source0:	https://git.sr.ht/~emersion/wlr-randr/refs/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fc62932c1724ec3640376b6a156b375d
URL:		https://sr.ht/~emersion/wlr-randr/
BuildRequires:	meson >= 0.47.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	wayland-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to manage outputs of a Wayland compositor.

%prep
%setup -q

%build
%meson build
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/%{name}
