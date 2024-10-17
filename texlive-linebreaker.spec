Name:		texlive-linebreaker
Version:	66639
Release:	1
Summary:	Prevent overflow boxes with LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/linebreaker
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linebreaker.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linebreaker.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package tries to prevent overflow lines in paragraphs or
boxes. It changes LuaTeX's \linebreak callback and re-typesets
the paragraph with increased values of \tolerance and
\emergencystretch until the overflow no longer happens. If that
doesn't help, it chooses the solution with the lowest badness.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/linebreaker
%doc %{_texmfdistdir}/doc/lualatex/linebreaker

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
