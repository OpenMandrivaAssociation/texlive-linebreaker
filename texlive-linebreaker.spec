%global tl_name linebreaker
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1c
Release:	%{tl_revision}.1
Summary:	Prevent overflow boxes with LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/linebreaker
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/linebreaker.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/linebreaker.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package tries to prevent overflow lines in paragraphs or boxes. It
changes LuaTeX's \linebreak callback and re-typesets the paragraph with
increased values of \tolerance and \emergencystretch until the overflow
no longer happens. If that doesn't help, it chooses the solution with
the lowest badness.

