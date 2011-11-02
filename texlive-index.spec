Name:		texlive-index
Version:	4.1beta
Release:	1
Summary:	Extended index for LaTeX including multiple indexes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/index
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/index.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/index.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/index.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This is a reimplementation of LaTeX's indexing macros to
provide better support for indexing. For example, it supports
multiple indexes in a single document and provides a more
robust \index command. It supplies short hand notations for the
\index command (^{word}) and a * variation of \index
(abbreviated _{word}) that prints the word being indexed, as
well as creating an index entry for it.

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
%{_texmfdistdir}/bibtex/bst/index/xagsm.bst
%{_texmfdistdir}/bibtex/bst/index/xplain.bst
%{_texmfdistdir}/makeindex/index/bibref.ist
%{_texmfdistdir}/tex/latex/index/autind.sty
%{_texmfdistdir}/tex/latex/index/bibref.sty
%{_texmfdistdir}/tex/latex/index/index.sty
%doc %{_texmfdistdir}/doc/latex/index/README
%doc %{_texmfdistdir}/doc/latex/index/TODO
%doc %{_texmfdistdir}/doc/latex/index/agsmtst.tex
%doc %{_texmfdistdir}/doc/latex/index/autind.tex
%doc %{_texmfdistdir}/doc/latex/index/index.pdf
%doc %{_texmfdistdir}/doc/latex/index/plaintst.tex
%doc %{_texmfdistdir}/doc/latex/index/sample.tex
%doc %{_texmfdistdir}/doc/latex/index/test.bib
#- source
%doc %{_texmfdistdir}/source/latex/index/index.dtx
%doc %{_texmfdistdir}/source/latex/index/index.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex makeindex tex doc source %{buildroot}%{_texmfdistdir}
