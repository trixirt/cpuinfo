%global commit0 eb4a6674bfe9cf91b63b9817412ae5f6862c8432
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary:        A library to detect information about host CPU
Name:           cpuinfo
License:        BSD
# The project has no version, this is the last git commit date YY.M.D
Version:        23.2.14
%define patch_level 2
Release:        %{patch_level}.git%{?shortcommit0}%{?dist}

URL:            https://github.com/pytorch/%{name}
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
# so version YY.M.D
Patch0:         0001-cpuinfo-fedora-cmake-changes.patch

Group:          Development/Libraries
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

%description
cpuinfo is a library to detect essential for performance
optimization information about host CPU.

Features
* Cross-platform availability:
  * Linux, Windows, macOS, Android, and iOS operating systems
  * x86, x86-64, ARM, and ARM64 architectures
* Modern C/C++ interface
  * Thread-safe
  * No memory allocation after initialization
  * No exceptions thrown
* Detection of supported instruction sets, up to AVX512 (x86)
  and ARMv8.3 extensions
* Detection of SoC and core information:
  * Processor (SoC) name
  * Vendor and microarchitecture for each CPU core
  * ID (MIDR on ARM, CPUID leaf 1 EAX value on x86) for each CPU core
* Detection of cache information:
  * Cache type (instruction/data/unified), size and line size
  * Cache associativity
  * Cores and logical processors (hyper-threads) sharing the cache
* Detection of topology information (relative between logical
  processors, cores, and processor packages)
* Well-tested production-quality code:
  * 60+ mock tests based on data from real devices
  * Includes work-arounds for common bugs in hardware and OS kernels
  * Supports systems with heterogenous cores, such as big.LITTLE and Max.Med.Min
* Permissive open-source license (Simplified BSD)

%package devel
Summary:        Headers and libraries for cpuinfo
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the developement libraries and headers
for cpuinfo.

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build
%cmake \
    -DCPUINFO_BUILD_UNIT_TESTS=OFF \
    -DCPUINFO_BUILD_MOCK_TESTS=OFF \
    -DCPUINFO_BUILD_BENCHMARKS=OFF

%cmake_build

%install
%cmake_install
%files
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%license LICENSE
%doc README.md
%dir %{_datadir}/%{name}
%{_includedir}/*.h
%{_datadir}/%{name}/*.cmake
%{_libdir}/*.so
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
* Wed Mar 29 2023 Tom Rix <trix@redhat.com> - 23.2.14-2.giteb4a667
- Simplify devel description
- Use dir tag for cpuinfo datadir

* Sun Mar 12 2023 Tom Rix <trix@redhat.com> - 23.2.14-1.giteb4a667
- Initial package

