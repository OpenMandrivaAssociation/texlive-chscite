%global tl_name chscite
%global tl_revision 28552

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.9999
Release:	%{tl_revision}.1
Summary:	Bibliography style for Chalmers University of Technology
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chscite
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chscite.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chscite.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chscite.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package, heavily based on the harvard package for Harvard-style
citations, provides a citation suite for students at Chalmers University
of Technology that follows given recommendations.

