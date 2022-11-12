Name:		texlive-chscite
Version:	28552
Release:	1
Summary:	Bibliography style for Chalmers University of Technology
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chscite
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chscite.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chscite.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chscite.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package, heavily based on the harvard package for Harvard-
style citations, provides a citation suite for students at
Chalmers University of Technology that follows given
recommendations.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/chscite/chscite.bst
%{_texmfdistdir}/tex/latex/chscite/chscite.sty
%doc %{_texmfdistdir}/doc/latex/chscite/README
%doc %{_texmfdistdir}/doc/latex/chscite/chscite.pdf
#- source
%doc %{_texmfdistdir}/source/latex/chscite/chscite.dtx
%doc %{_texmfdistdir}/source/latex/chscite/chscite.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
