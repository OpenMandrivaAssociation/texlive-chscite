# revision 24037
# category Package
# catalog-ctan /macros/latex/contrib/chscite
# catalog-date 2011-09-20 14:34:15 +0200
# catalog-license lppl1.2
# catalog-version 2.99
Name:		texlive-chscite
Version:	2.99
Release:	1
Summary:	Bibliography style for Chalmers University of Technology
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chscite
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chscite.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chscite.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chscite.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package, heavily based on the harvard package for Harvard-
style citations, provides a citation suite for students at
Chalmers University of Technology that follows given
recommendations.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
