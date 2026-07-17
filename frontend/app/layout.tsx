// @/app/layout.tsx
import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import ReduxProvider from "@/store/provider";
import Navbar from "@/components/layout/Navbar";
import Sidebar from "@/components/layout/Sidebar";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Storefront",
  description: "Dynamic shopping experience",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
    >
      <body className="h-full bg-gray-50">
        <ReduxProvider>
          <div className="flex flex-col min-h-screen">

            {/* 1. Header / Navbar */}
            <header className="sticky top-0 z-50">
              <Navbar />
            </header>

            {/* 2. Page Content Wrapper */}
            <div className="flex flex-col md:flex-row flex-grow relative">

              {/* Sidebar Component */}
              <Sidebar />

              {/* 
                Main Content Area 
                FIX: added 'md:pl-64' so the layout doesn't slide under your fixed desktop sidebar!
              */}
              <main className="flex-grow p-4 md:p-6 md:pl-64 transition-all duration-200">
                {children}
              </main>

            </div>
          </div>
        </ReduxProvider>
      </body>
    </html>
  );
}