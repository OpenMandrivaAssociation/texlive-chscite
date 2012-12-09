# revision 26383
# category Package
# catalog-ctan /macros/latex/contrib/chscite
# catalog-date 2012-05-14 12:19:39 +0200
# catalog-license lppl1.2
# catalog-version 2.999
Name:		texlive-chscite
Version:	2.999
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.999-1
+ Revision: 812116
- Update to latest release.

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.99-2
+ Revision: 750228
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.99-1
+ Revision: 718059
- texlive-chscite
- texlive-chscite
- texlive-chscite

