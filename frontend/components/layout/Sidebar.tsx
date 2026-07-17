// @/components/layout/Sidebar.tsx
"use client";
import React from 'react';

interface SidebarItemProps {
    label: string;
    href: string;
    icon: React.ReactNode;
    active?: boolean;
}

const SidebarItem: React.FC<SidebarItemProps> = ({ label, href, icon, active }) => {
    return (
        <a
            href={href}
            className={`flex flex-col md:flex-row items-center gap-1 md:gap-3 px-2 py-1.5 sm:px-3 sm:py-2 md:px-4 md:py-3 rounded-lg font-medium transition-all duration-200 flex-shrink-0 whitespace-nowrap ${active
                ? 'bg-red-700 text-white shadow-sm'
                : 'text-red-100 hover:bg-red-800 hover:text-white'
                }`}
        >
            <span className="flex-shrink-0 w-4 h-4 sm:w-5 sm:h-5">{icon}</span>
            <span className="text-[10px] sm:text-[11px] md:text-sm font-semibold md:font-medium">{label}</span>
        </a>
    );
};

interface SidebarProps {
    isOpen?: boolean;
}

const Sidebar: React.FC<SidebarProps> = () => {
    return (
        <aside
            /* 
              FIX: Adjusted visibility architecture variables.
              - Mobile: 'w-full relative' retains default flex-flow structure.
              - Desktop: 'md:fixed md:w-64 md:h-[calc(100vh-56px)]' locks sidebar viewport scroll.
              (Note: Swap out '56px' with your exact custom header navbar height calculation if needed)
            */
            className="w-full md:w-64 md:fixed md:left-0 md:top-[56px] md:h-[calc(100vh-56px)] bg-red-600 text-white flex flex-row md:flex-col border-b md:border-b-0 md:border-r border-red-700 shadow-lg md:shadow-xl z-40 overflow-hidden"
        >
            {/* Inner Content Scrolling Architecture */}
            <div className="flex flex-row md:flex-col flex-1 overflow-x-auto md:overflow-y-auto scrollbar-none [scrollbar-width:none] [-ms-overflow-style:none] [&::-webkit-scrollbar]:hidden touch-pan-x md:p-4">

                {/* Brand / Title Header (Desktop Only) */}
                <div className="hidden md:flex items-center gap-2 px-2 pb-6 border-b border-red-500/30 mb-6">
                    <svg className="w-8 h-8 flex-shrink-0 fill-current" viewBox="0 0 24 24">
                        <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" />
                    </svg>
                    <span className="text-xl font-bold tracking-wider">
                        RED<span className="text-red-200">PORTAL</span>
                    </span>
                </div>

                {/* Navigation Links Grid Block */}
                <nav className="flex flex-row md:flex-col gap-1 sm:gap-2 flex-1 px-3 py-2 md:px-0 md:py-0 justify-center sm:justify-around md:justify-start min-w-max md:min-w-0">
                    <SidebarItem
                        label="POS"
                        href="/pos"
                        icon={
                            <svg className="stroke-current fill-none stroke-2" viewBox="0 0 24 24">
                                <rect x="2" y="3" width="20" height="14" rx="2" ry="2" />
                                <line x1="8" y1="21" x2="16" y2="21" />
                                <line x1="12" y1="17" x2="12" y2="21" />
                            </svg>
                        }
                    />
                    <SidebarItem
                        label="Sales"
                        href="/sales"
                        active={true}
                        icon={
                            <svg className="stroke-current fill-none stroke-2" viewBox="0 0 24 24">
                                <line x1="18" y1="20" x2="18" y2="10" />
                                <line x1="12" y1="20" x2="12" y2="4" />
                                <line x1="6" y1="20" x2="6" y2="14" />
                            </svg>
                        }
                    />
                    <SidebarItem
                        label="Products"
                        href="/products"
                        icon={
                            <svg className="stroke-current fill-none stroke-2" viewBox="0 0 24 24">
                                <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z" />
                                <polyline points="3.27 6.96 12 12.01 20.73 6.96" />
                                <line x1="12" y1="22.08" x2="12" y2="12" />
                            </svg>
                        }
                    />
                    <SidebarItem
                        label="Finance"
                        href="/finance"
                        icon={
                            <svg className="stroke-current fill-none stroke-2" viewBox="0 0 24 24">
                                <line x1="12" y1="1" x2="12" y2="23" />
                                <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" />
                            </svg>
                        }
                    />
                    <SidebarItem
                        label="Users"
                        href="/users"
                        icon={
                            <svg className="stroke-current fill-none stroke-2" viewBox="0 0 24 24">
                                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
                                <circle cx="9" cy="7" r="4" />
                                <path d="M23 21v-2a4 4 0 0 0-3-3.87" />
                                <path d="M16 3.13a4 4 0 0 1 0 7.75" />
                            </svg>
                        }
                    />
                    <SidebarItem
                        label="Purchases"
                        href="/purchases"
                        icon={
                            <svg className="stroke-current fill-none stroke-2" viewBox="0 0 24 24">
                                <circle cx="9" cy="21" r="1" />
                                <circle cx="20" cy="21" r="1" />
                                <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6" />
                            </svg>
                        }
                    />
                </nav>
            </div>

            {/* Bottom Section: Logout Component (Desktop Only) */}
            <div className="hidden md:block p-4 border-t border-red-500/30 bg-red-600">
                <button
                    onClick={() => console.log('Logging out...')}
                    className="w-full flex items-center gap-3 px-4 py-3 rounded-lg font-medium text-red-200 hover:bg-red-800 hover:text-white transition-all duration-200"
                >
                    <svg className="w-5 h-5 flex-shrink-0 stroke-current fill-none stroke-2" viewBox="0 0 24 24">
                        <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4" />
                        <polyline points="16 17 21 12 16 7" />
                        <line x1="21" y1="12" x2="9" y2="12" />
                    </svg>
                    <span className="truncate">Logout</span>
                </button>
            </div>
        </aside>
    );
};

export default Sidebar;