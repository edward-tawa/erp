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

            {/* 2. Page Content Wrapper 
                Mobile: flex-col (Sidebar is stacked under navbar, above the content)
                Desktop: flex-row (Sidebar is on the left, content is on the right)
            */}
            <div className="flex flex-col md:flex-row flex-grow">

              {/* Sidebar sits under the navbar on mobile, or to the left on desktop */}
              <Sidebar />

              {/* Main Content Area */}
              <main className="flex-grow p-4 md:p-6">
                {children}
              </main>

            </div>

            {/* 3. Optional Footer */}
            {/* <Footer /> */}

          </div>
        </ReduxProvider>
      </body>
    </html>
  );
}