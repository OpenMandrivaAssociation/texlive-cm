# revision 32865
# category Package
# catalog-ctan /fonts/cm
# catalog-date 2012-06-26 21:09:43 +0200
# catalog-license knuth
# catalog-version undef
Name:		texlive-cm
Version:	20120626
Release:	9
Summary:	Computer Modern fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/cm
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cm.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cm.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Knuth's final iteration of his re-interpretation of a c.19
Modern-style font from Monotype. The family is comprehensive,
offering both sans and roman styles, and a monospaced font,
together with mathematics fonts closely integrated with the
mathematical facilities of TeX itself. The base fonts are
distributed as Metafont source, but autotraced PostScript Type
1 versions are available (one version in the AMS fonts
distribution, and also the BaKoMa distribution). The Computer
Modern fonts have inspired many later families, notably the
European Computer Modern and the Latin Modern families.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/cm/cmtext-bsr-interpolated.map
%{_texmfdistdir}/fonts/pk/ljfour/public/cm/dpi600/cmbx10.pk
%{_texmfdistdir}/fonts/pk/ljfour/public/cm/dpi600/cmex10.pk
%{_texmfdistdir}/fonts/pk/ljfour/public/cm/dpi600/cmmi10.pk
%{_texmfdistdir}/fonts/pk/ljfour/public/cm/dpi600/cmmi7.pk
%{_texmfdistdir}/fonts/pk/ljfour/public/cm/dpi600/cmr10.pk
%{_texmfdistdir}/fonts/pk/ljfour/public/cm/dpi600/cmr12.pk
%{_texmfdistdir}/fonts/pk/ljfour/public/cm/dpi600/cmr17.pk
%{_texmfdistdir}/fonts/pk/ljfour/public/cm/dpi600/cmr6.pk
%{_texmfdistdir}/fonts/pk/ljfour/public/cm/dpi600/cmr7.pk
%{_texmfdistdir}/fonts/pk/ljfour/public/cm/dpi600/cmr8.pk
%{_texmfdistdir}/fonts/pk/ljfour/public/cm/dpi600/cmsl10.pk
%{_texmfdistdir}/fonts/pk/ljfour/public/cm/dpi600/cmsy10.pk
%{_texmfdistdir}/fonts/pk/ljfour/public/cm/dpi600/cmsy7.pk
%{_texmfdistdir}/fonts/pk/ljfour/public/cm/dpi600/cmti10.pk
%{_texmfdistdir}/fonts/source/public/cm/accent.mf
%{_texmfdistdir}/fonts/source/public/cm/bigacc.mf
%{_texmfdistdir}/fonts/source/public/cm/bigdel.mf
%{_texmfdistdir}/fonts/source/public/cm/bigop.mf
%{_texmfdistdir}/fonts/source/public/cm/calu.mf
%{_texmfdistdir}/fonts/source/public/cm/cmb10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmbase.mf
%{_texmfdistdir}/fonts/source/public/cm/cmbcsc10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmbsy10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmbtex10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmbtt10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmbtt8.mf
%{_texmfdistdir}/fonts/source/public/cm/cmbtt9.mf
%{_texmfdistdir}/fonts/source/public/cm/cmbx10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmbx12.mf
%{_texmfdistdir}/fonts/source/public/cm/cmbx5.mf
%{_texmfdistdir}/fonts/source/public/cm/cmbx6.mf
%{_texmfdistdir}/fonts/source/public/cm/cmbx7.mf
%{_texmfdistdir}/fonts/source/public/cm/cmbx8.mf
%{_texmfdistdir}/fonts/source/public/cm/cmbx9.mf
%{_texmfdistdir}/fonts/source/public/cm/cmbxsl10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmbxti10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmcsc10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmdunh10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmex10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmexb10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmff10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmfi10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmfib8.mf
%{_texmfdistdir}/fonts/source/public/cm/cminch.mf
%{_texmfdistdir}/fonts/source/public/cm/cmitt10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmmi10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmmi12.mf
%{_texmfdistdir}/fonts/source/public/cm/cmmi5.mf
%{_texmfdistdir}/fonts/source/public/cm/cmmi6.mf
%{_texmfdistdir}/fonts/source/public/cm/cmmi7.mf
%{_texmfdistdir}/fonts/source/public/cm/cmmi8.mf
%{_texmfdistdir}/fonts/source/public/cm/cmmi9.mf
%{_texmfdistdir}/fonts/source/public/cm/cmmib10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmplain.mf
%{_texmfdistdir}/fonts/source/public/cm/cmr10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmr12.mf
%{_texmfdistdir}/fonts/source/public/cm/cmr17.mf
%{_texmfdistdir}/fonts/source/public/cm/cmr5.mf
%{_texmfdistdir}/fonts/source/public/cm/cmr6.mf
%{_texmfdistdir}/fonts/source/public/cm/cmr7.mf
%{_texmfdistdir}/fonts/source/public/cm/cmr8.mf
%{_texmfdistdir}/fonts/source/public/cm/cmr9.mf
%{_texmfdistdir}/fonts/source/public/cm/cmsl10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmsl12.mf
%{_texmfdistdir}/fonts/source/public/cm/cmsl8.mf
%{_texmfdistdir}/fonts/source/public/cm/cmsl9.mf
%{_texmfdistdir}/fonts/source/public/cm/cmsltt10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmss10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmss12.mf
%{_texmfdistdir}/fonts/source/public/cm/cmss17.mf
%{_texmfdistdir}/fonts/source/public/cm/cmss8.mf
%{_texmfdistdir}/fonts/source/public/cm/cmss9.mf
%{_texmfdistdir}/fonts/source/public/cm/cmssbx10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmssdc10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmssi10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmssi12.mf
%{_texmfdistdir}/fonts/source/public/cm/cmssi17.mf
%{_texmfdistdir}/fonts/source/public/cm/cmssi8.mf
%{_texmfdistdir}/fonts/source/public/cm/cmssi9.mf
%{_texmfdistdir}/fonts/source/public/cm/cmssq8.mf
%{_texmfdistdir}/fonts/source/public/cm/cmssqi8.mf
%{_texmfdistdir}/fonts/source/public/cm/cmsy10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmsy5.mf
%{_texmfdistdir}/fonts/source/public/cm/cmsy6.mf
%{_texmfdistdir}/fonts/source/public/cm/cmsy7.mf
%{_texmfdistdir}/fonts/source/public/cm/cmsy8.mf
%{_texmfdistdir}/fonts/source/public/cm/cmsy9.mf
%{_texmfdistdir}/fonts/source/public/cm/cmtcsc10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmtex10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmtex8.mf
%{_texmfdistdir}/fonts/source/public/cm/cmtex9.mf
%{_texmfdistdir}/fonts/source/public/cm/cmti10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmti12.mf
%{_texmfdistdir}/fonts/source/public/cm/cmti7.mf
%{_texmfdistdir}/fonts/source/public/cm/cmti8.mf
%{_texmfdistdir}/fonts/source/public/cm/cmti9.mf
%{_texmfdistdir}/fonts/source/public/cm/cmtt10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmtt12.mf
%{_texmfdistdir}/fonts/source/public/cm/cmtt8.mf
%{_texmfdistdir}/fonts/source/public/cm/cmtt9.mf
%{_texmfdistdir}/fonts/source/public/cm/cmttb10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmu10.mf
%{_texmfdistdir}/fonts/source/public/cm/cmvtt10.mf
%{_texmfdistdir}/fonts/source/public/cm/comlig.mf
%{_texmfdistdir}/fonts/source/public/cm/csc.mf
%{_texmfdistdir}/fonts/source/public/cm/cscspu.mf
%{_texmfdistdir}/fonts/source/public/cm/greekl.mf
%{_texmfdistdir}/fonts/source/public/cm/greeku.mf
%{_texmfdistdir}/fonts/source/public/cm/itald.mf
%{_texmfdistdir}/fonts/source/public/cm/italig.mf
%{_texmfdistdir}/fonts/source/public/cm/itall.mf
%{_texmfdistdir}/fonts/source/public/cm/italms.mf
%{_texmfdistdir}/fonts/source/public/cm/italp.mf
%{_texmfdistdir}/fonts/source/public/cm/italsp.mf
%{_texmfdistdir}/fonts/source/public/cm/mathex.mf
%{_texmfdistdir}/fonts/source/public/cm/mathit.mf
%{_texmfdistdir}/fonts/source/public/cm/mathsy.mf
%{_texmfdistdir}/fonts/source/public/cm/olddig.mf
%{_texmfdistdir}/fonts/source/public/cm/punct.mf
%{_texmfdistdir}/fonts/source/public/cm/roman.mf
%{_texmfdistdir}/fonts/source/public/cm/romand.mf
%{_texmfdistdir}/fonts/source/public/cm/romanl.mf
%{_texmfdistdir}/fonts/source/public/cm/romanp.mf
%{_texmfdistdir}/fonts/source/public/cm/romanu.mf
%{_texmfdistdir}/fonts/source/public/cm/romlig.mf
%{_texmfdistdir}/fonts/source/public/cm/romms.mf
%{_texmfdistdir}/fonts/source/public/cm/romspl.mf
%{_texmfdistdir}/fonts/source/public/cm/romspu.mf
%{_texmfdistdir}/fonts/source/public/cm/romsub.mf
%{_texmfdistdir}/fonts/source/public/cm/sym.mf
%{_texmfdistdir}/fonts/source/public/cm/symbol.mf
%{_texmfdistdir}/fonts/source/public/cm/texset.mf
%{_texmfdistdir}/fonts/source/public/cm/textit.mf
%{_texmfdistdir}/fonts/source/public/cm/title.mf
%{_texmfdistdir}/fonts/source/public/cm/tset.mf
%{_texmfdistdir}/fonts/source/public/cm/tsetsl.mf
%{_texmfdistdir}/fonts/source/public/cm/white_setup.mf
%{_texmfdistdir}/fonts/tfm/public/cm/cmb10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmbcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmbsy10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmbx5.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmbxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmbxti10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmdunh10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmex10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmff10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmfi10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmfib8.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cminch.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmitt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmmi10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmmi12.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmmi6.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmmi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmmi9.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmmib10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmr10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmr12.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmr17.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmr5.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmr6.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmr7.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmr8.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmr9.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmsltt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmss10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmss12.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmss17.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmss8.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmss9.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmssbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmssdc10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmssi10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmssi12.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmssi17.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmssi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmssi9.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmssq8.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmssqi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmsy10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmsy5.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmsy6.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmsy7.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmsy8.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmsy9.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmtcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmtex10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmtex8.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmtex9.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmti10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmti12.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmti7.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmti8.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmti9.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmtt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmtt12.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmtt8.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmtt9.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmu10.tfm
%{_texmfdistdir}/fonts/tfm/public/cm/cmvtt10.tfm
%doc %{_texmfdistdir}/doc/fonts/cm/README
%doc %{_texmfdistdir}/doc/fonts/cm/README-cmps.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
