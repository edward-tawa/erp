"use client";
import React, { useState } from 'react';
import CartIcon from '@/components/icons/CartIcon';
import SearchIcon from '@/components/icons/SearchIcon';
import SearchBar from '@/components/layout/SearchBar';

const Navbar = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [isSearchOpen, setIsSearchOpen] = useState(false);

    const toggleSearch = (e: React.MouseEvent) => {
        e.stopPropagation();
        setIsSearchOpen(!isSearchOpen);
    };

    return (
        <nav className="bg-red-600 text-white shadow-md relative">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex items-center justify-between h-16">

                    {/* Left side: Menu trigger and logo */}
                    {/* On mobile, if search is open, we hide the brand logo to save real estate */}
                    <div className="flex items-center gap-3">
                        <button
                            onClick={() => setIsOpen(!isOpen)}
                            type="button"
                            className="md:hidden text-white hover:text-red-200 focus:outline-none"
                            aria-label="Toggle menu"
                        >
                            <svg className="h-6 w-6 fill-current" viewBox="0 0 24 24">
                                {isOpen ? (
                                    <path fillRule="evenodd" clipRule="evenodd" d="M18.278 16.864a1 1 0 0 1-1.414 1.414l-4.829-4.83-4.828 4.83a1 1 0 0 1-1.414-1.414l4.829-4.83-4.829-4.83a1 1 0 0 1 1.414-1.414l4.828 4.83 4.829-4.83a1 1 0 1 1 1.414 1.414l-4.83 4.83 4.83 4.83z" />
                                ) : (
                                    <path fillRule="evenodd" d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z" />
                                )}
                            </svg>
                        </button>

                        <div className={`flex-shrink-0 ${isSearchOpen ? 'hidden sm:block' : 'block'}`}>
                            <a href="/dashboard" className="text-lg md:text-xl font-bold tracking-wider hover:text-red-100 transition-colors">
                                RED<span className="text-red-200">PORTAL</span>
                            </a>
                        </div>
                    </div>

                    {/* Desktop Navigation Links */}
                    <div className="hidden md:flex space-x-6 lg:space-x-8 font-medium">
                        <a href="/dashboard" className="hover:text-red-200 transition-colors py-2 text-sm lg:text-base">Dashboard</a>
                        <a href="/reports" className="hover:text-red-200 transition-colors py-2 text-sm lg:text-base">Reports</a>
                        <a href="/inventory" className="hover:text-red-200 transition-colors py-2 text-sm lg:text-base">Inventory</a>
                        <a href="/support" className="hover:text-red-200 transition-colors py-2 text-sm lg:text-base">Support</a>
                    </div>

                    {/* Right side layout */}
                    <div className="flex items-center gap-1 md:gap-4 relative">

                        {/* Search Icon Trigger */}
                        <button
                            onClick={toggleSearch}
                            className="p-2 rounded-full hover:bg-red-700 text-red-100 hover:text-white transition-all focus:outline-none"
                            aria-label="Search ERP"
                        >
                            <SearchIcon size={20} />
                        </button>

                        {/* Search Bar component */}
                        <SearchBar
                            isVisible={isSearchOpen}
                            onClose={() => setIsSearchOpen(false)}
                        />

                        {/* Cart Link */}
                        <a
                            href="/cart"
                            className="p-2 rounded-full hover:bg-red-700 text-red-100 hover:text-white transition-all"
                            aria-label="View Cart"
                        >
                            <CartIcon size={20} />
                        </a>

                        {/* Invoice Button */}
                        <div className="hidden md:block">
                            <button className="bg-white text-red-600 hover:bg-red-50 px-3 py-1.5 rounded-lg font-semibold shadow-sm text-sm transition-all duration-200 flex items-center gap-1.5">
                                <svg className="w-4 h-4 stroke-current fill-none stroke-2" viewBox="0 0 24 24">
                                    <line x1="12" y1="5" x2="12" y2="19" />
                                    <line x1="5" y1="12" x2="19" y2="12" />
                                </svg>
                                New Invoice
                            </button>
                        </div>
                    </div>

                </div>
            </div>

            {/* Mobile Menu dropdown */}
            <div className={`${isOpen ? 'block' : 'hidden'} md:hidden bg-red-700 transition-all duration-300`}>
                <div className="px-2 pt-2 pb-4 space-y-1 sm:px-3">
                    <a href="/dashboard" className="block px-3 py-2 rounded-md text-base font-medium hover:bg-red-800 transition-colors">Dashboard</a>
                    <a href="/reports" className="block px-3 py-2 rounded-md text-base font-medium hover:bg-red-800 transition-colors">Reports</a>
                    <a href="/inventory" className="block px-3 py-2 rounded-md text-base font-medium hover:bg-red-800 transition-colors">Inventory</a>
                    <a href="/support" className="block px-3 py-2 rounded-md text-base font-medium hover:bg-red-800 transition-colors">Support</a>

                    <div className="pt-4 border-t border-red-500">
                        <button className="w-full bg-white text-red-600 hover:bg-red-50 px-4 py-2 rounded-lg font-semibold transition-colors flex items-center justify-center gap-2">
                            <svg className="w-4 h-4 stroke-current fill-none stroke-2" viewBox="0 0 24 24">
                                <line x1="12" y1="5" x2="12" y2="19" />
                                <line x1="5" y1="12" x2="19" y2="12" />
                            </svg>
                            New Invoice
                        </button>
                    </div>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;