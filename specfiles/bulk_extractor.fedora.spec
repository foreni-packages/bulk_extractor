#
# spec file for package bulk_extractor
#

#

Name:           bulk_extractor
Version:        1.5.5
Release:        1
License:        Public-Domain
Summary:        Forensics tool for extracting email addresses and URLs from bulk data.
Url:            http://afflib.org/downloads/bulk_extractor-1.5.5.tar.gz
Group:          Productivity/File utilities
AutoReqProv:    on
Source:         bulk_extractor-1.5.5.tar.gz
BuildRequires:  zlib-devel
BuildRequires:  libewf-devel

BuildRequires:  exiv2-devel
BuildRequires:  librx-devel
BuildRequires:  gcc-c++
BuildRequires:  flex

%description
bulk_extractor is a C++ program that scans a disk image, a file, or a
directory of files and extracts useful information without parsing the
file system or file system structures. Useful information currently
includes email addresses, URLs, credit card numbers, EXIF data
structures, KML files, AES encryption keys (from RAM), IP packets, and
other kinds of forensicly important information. Results are stored in
text files (called feature files) 
that can be easily inspected, parsed, or processed with automated
tools. The program is multi-threaded and will use all available
cores. bulk_extractor also created a histograms of features that it finds,
as features that are more common tend to be more important.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc ChangeLog README COPYING
%doc %{_mandir}/man1/bulk_extractor.1.gz
%{_bindir}/bulk_extractor

%changelog

