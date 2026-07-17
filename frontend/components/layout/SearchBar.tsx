// @/components/layout/SearchBar.tsx
"use client";
import React, { useEffect, useRef } from 'react';
import SearchIcon from '@/components/icons/SearchIcon';

interface SearchBarProps {
    isVisible: boolean;
    onClose: () => void;
}

const SearchBar: React.FC<SearchBarProps> = ({ isVisible, onClose }) => {
    const searchBarRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        const handleClickOutside = (event: MouseEvent) => {
            if (
                searchBarRef.current &&
                !searchBarRef.current.contains(event.target as Node)
            ) {
                onClose();
            }
        };

        if (isVisible) {
            document.addEventListener('mousedown', handleClickOutside);
        }

        return () => {
            document.removeEventListener('mousedown', handleClickOutside);
        };
    }, [isVisible, onClose]);

    if (!isVisible) return null;

    return (
        <div
            ref={searchBarRef}
            /* 
              Changed right-14 to right-20 on mobile (right-20 md:right-0).
              This shifts the input box further to the left, completely exposing 
              the search and cart buttons on the right.
            */
            className="absolute md:relative right-20 md:right-0 z-50 flex items-center w-40 sm:w-48 md:w-56 animate-in fade-in zoom-in-95 duration-150"
        >
            <div className="absolute left-3 text-red-600 pointer-events-none">
                <SearchIcon size={14} />
            </div>
            <input
                type="text"
                placeholder="Search SKU, client..."
                autoFocus
                className="w-full bg-white text-gray-800 placeholder-gray-400 pl-9 pr-3 py-1.5 rounded-lg text-xs md:text-sm border border-transparent focus:outline-none focus:ring-2 focus:ring-red-400 shadow-md md:shadow-inner"
            />
        </div>
    );
};

export default SearchBar;