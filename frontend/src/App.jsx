import React, { useState, useEffect } from 'react';
import { Activity, TrendingUp, Zap, Target, BarChart2 } from 'lucide-react';
import GlassCard from './components/GlassCard';

const API_BASE_URL = 'http://localhost:8000/api/v1';

function App() {
  const [recommendations, setRecommendations] = useState([]);
  const [quotaStats, setQuotaStats] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Fetch Recommendations
        const recResponse = await fetch(`${API_BASE_URL}/recommendations/channel_123`);
        const recData = await recResponse.json();
        setRecommendations(recData);

        // Fetch Quota Stats
        const quotaResponse = await fetch(`${API_BASE_URL}/optimization/quota-stats`);
        const quotaData = await quotaResponse.json();
        setQuotaStats(quotaData);

        setLoading(false);
      } catch (error) {
        console.error("Error fetching data:", error);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-charcoal to-grey-olive text-linen p-8">
      <header className="mb-12 flex justify-between items-center">
        <div>
          <h1 className="text-4xl font-bold font-zen bg-clip-text text-transparent bg-gradient-to-r from-lemon-lime to-celadon pb-1 drop-shadow-sm">
            TubeSage Intelligence
          </h1>
          <p className="text-linen/70 mt-2 font-light">AI-Driven Content Strategy Dashboard</p>
        </div>
        <div className="flex items-center gap-2">
          <div className={`w-3 h-3 rounded-full ${quotaStats?.status === 'Healthy' ? 'bg-lemon-lime shadow-[0_0_10px_var(--color-lemon-lime)]' : 'bg-red-400'} animate-pulse`} />
          <span className="text-sm font-medium text-linen/80">System Status: {quotaStats?.status || 'Unknown'}</span>
        </div>
      </header>

      {loading ? (
        <div className="flex justify-center items-center h-64">
          <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-lemon-lime"></div>
        </div>
      ) : (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">

          {/* Main Feed: Recommendations */}
          <div className="lg:col-span-2 space-y-6">
            <h2 className="text-2xl font-semibold mb-4 flex items-center gap-2 text-linen">
              <Zap className="text-lemon-lime" />
              Strategic Recommendations
            </h2>

            {recommendations.map((rec, index) => (
              <GlassCard key={index} delay={index * 0.1} className="hover:bg-linen/10 transition-colors border-linen/20">
                <div className="flex justify-between items-start">
                  <div>
                    <span className="inline-block px-3 py-1 rounded-full text-xs font-semibold bg-celadon/20 text-celadon mb-2 border border-celadon/30">
                      {rec.category}
                    </span>
                    <h3 className="text-xl font-bold mb-2 text-linen">{rec.suggestion}</h3>
                    <p className="text-linen/80">{rec.rationale}</p>
                  </div>
                  <div className="flex flex-col items-center ml-4">
                    <div className="text-3xl font-bold text-lemon-lime drop-shadow-sm">{rec.impact_score}</div>
                    <span className="text-xs text-linen/50 uppercase tracking-widest mt-1">Impact</span>
                  </div>
                </div>
              </GlassCard>
            ))}
          </div>

          {/* Sidebar: Stats & Metrics */}
          <div className="space-y-8">
            {/* Quota Optimization Card */}
            <GlassCard delay={0.3} className="border-linen/20">
              <h3 className="text-lg font-semibold mb-4 flex items-center gap-2 text-linen">
                <Activity className="text-celadon" />
                API Efficiency
              </h3>
              <div className="space-y-4">
                <div className="flex justify-between items-center text-sm">
                  <span className="text-linen/70">Daily Quota Used</span>
                  <span className="font-mono font-bold text-linen">{quotaStats?.current_daily_usage} / {quotaStats?.limit}</span>
                </div>
                <div className="w-full bg-charcoal/50 rounded-full h-2.5 border border-white/5">
                  <div
                    className="bg-gradient-to-r from-celadon to-lemon-lime h-2.5 rounded-full shadow-[0_0_10px_rgba(207,209,26,0.3)]"
                    style={{ width: `${(quotaStats?.current_daily_usage / quotaStats?.limit) * 100}%` }}
                  ></div>
                </div>

                <div className="pt-4 border-t border-linen/10">
                  <div className="flex justify-between items-center mb-1">
                    <span className="text-linen/70">Requests Saved (Cache)</span>
                    <span className="font-bold text-lemon-lime">+{quotaStats?.estimated_requests_saved}</span>
                  </div>
                  <p className="text-xs text-linen/50">
                    Smart Cache prevented {quotaStats?.estimated_requests_saved} unnecessary API calls today.
                  </p>
                </div>
              </div>
            </GlassCard>

            {/* Quick Actions */}
            <GlassCard delay={0.4} className="border-linen/20">
              <h3 className="text-lg font-semibold mb-4 flex items-center gap-2 text-linen">
                <Target className="text-lemon-lime" />
                Quick Actions
              </h3>
              <div className="space-y-3">
                <button className="w-full py-3 px-4 bg-linen/5 hover:bg-linen/10 border border-linen/10 rounded-lg text-left text-sm transition-all hover:border-lemon-lime/50 flex justify-between group">
                  <span>Run Competitor Analysis</span>
                  <span className="text-lemon-lime opacity-0 group-hover:opacity-100 transition-opacity">→</span>
                </button>
                <button className="w-full py-3 px-4 bg-linen/5 hover:bg-linen/10 border border-linen/10 rounded-lg text-left text-sm transition-all hover:border-lemon-lime/50 flex justify-between group">
                  <span>Simulate Growth Strategy</span>
                  <span className="text-lemon-lime opacity-0 group-hover:opacity-100 transition-opacity">→</span>
                </button>
              </div>
            </GlassCard>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
