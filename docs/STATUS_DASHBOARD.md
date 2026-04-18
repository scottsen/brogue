# Veinborn Status Dashboard 🎯

**Last Updated:** 2026-04-17 (validated against code & tests; see `PROJECT_REVIEW_2026-04-17.md`)
**Quick View:** One-page status overview

---

## 🚦 Current Status

| Category | Status | Details |
|----------|--------|---------|
| **Single-Player core** | 🟢 Mostly healthy | ~800/802 unit tests pass; 2 test-drift failures in `test_action_factory.py` (new 8th action not added to expectations) |
| **Multiplayer** | 🔴 Experimental / broken | 7+ server test failures; reconnection/websocket_server tests hang. `GameSession` runs against raw `GameState` (should be `GameContext`); missing `WaitAction` module. |
| **Test Health** | 🟡 Partial | 1063 collected. SP ~800 pass / 2 fail. MP ~95 pass / 7 fail plus hangs in reconnection & websocket_server. Not 100%. |
| **Current Phase** | 🛠️ Restore trust | Fix stale docs, repair MP correctness, then resume feature work |
| **Playability** | ✅ SP playable / ❌ MP not recommended | |

See `docs/PROJECT_REVIEW_2026-04-17.md` for full evidence.

**Codebase Stats:**
- **114+ Python files**
- **~17,400 lines of code**
- **11 new multiplayer files** (~2,400 lines)

---

## 🎯 Top 3 Priorities (What to Work On NOW)

### 1️⃣ **Extended Multiplayer Testing** 🔴 CRITICAL
- Test 30+ minutes of 2-player co-op
- Validate combat balance with multiple players
- Document edge cases and bugs
- **Why:** Phase 2 just completed, needs validation

### 2️⃣ **Single-Player Balance Tuning** 🟡 HIGH
- Playtest extensively (30-60 min sessions)
- Tune monster difficulty progression
- Balance ore spawn rates and crafting formulas
- **Why:** Core gameplay needs refinement

### 3️⃣ **Tutorial System** 🟢 MEDIUM
- First-run tutorial for new players
- Help screen (H key)
- Keybind reference
- **Why:** Usability and onboarding

---

## ✅ What's Working (Complete Systems)

### Single-Player (100% Complete)
- ✅ Mining system (survey ore, mine over turns)
- ✅ Crafting system (recipes, stat calculation)
- ✅ Equipment system (weapons, armor, bonuses)
- ✅ Save/Load system (game state persistence)
- ✅ Character classes (4 classes with different stats)
- ✅ Floor progression (stairs, difficulty scaling)
- ✅ Legacy Vault (meta-progression)
- ✅ Combat system (turn-based tactical)
- ✅ Monster AI (pathfinding, aggression)
- ✅ Lua Event System (Phase 3 complete)

### Multiplayer (Phase 2 Complete - 2025-11-14)
- ✅ WebSocket server infrastructure
- ✅ 2+ player co-op working
- ✅ Shared dungeon generation
- ✅ Distributed player spawning
- ✅ Turn system ("4 actions per round")
- ✅ Monster AI integration
- ✅ Nearest-player targeting

---

## 🚧 What's In Progress

### Track A: Single-Player Polish
- [ ] Balance tuning
- [ ] Tutorial system
- [ ] Special room types (treasure, shrine, trap)
- [ ] Polish & UX improvements

### Track B: Multiplayer Phase 3
- [ ] Extended co-op testing (30+ min)
- [ ] Combat balance for multiplayer
- [ ] Delta compression (performance)
- [ ] Reconnection handling
- [ ] Class selection on join
- [ ] Personal loot system

---

## 📅 Recent Milestones (November 2025)

| Date | Milestone | Impact |
|------|-----------|--------|
| **Nov 14** | 🎉 Multiplayer Phase 2 Complete | +2,400 lines, 11 new files |
| **Nov 13** | Monster AI targeting (nearest player) | Smart co-op AI |
| **Nov 12** | Distributed player spawning | Players start in different rooms |
| **Nov 11** | Multiplayer game functionality | Turn system working |
| **Nov 10** | Multiplayer design finalized | Clear roadmap |
| **Nov 5** | Documentation cleanup | Truth alignment |

---

## 🗺️ Phase Roadmap

| Phase | Status | Description |
|-------|--------|-------------|
| **Phase 0** | ✅ Complete | Foundation (movement, combat, map gen) |
| **Phase 1** | ✅ Complete | MVP Core (mining, crafting, classes) |
| **Phase 2** | ✅ Complete | Multiplayer infrastructure (co-op working!) |
| **Phase 3** | 🔨 Current | Testing + Polish (both tracks) |
| **Phase 4** | 📅 Future | Advanced features (persistence, bosses) |

---

## 🎮 How to Play

### Single-Player
```bash
./veinborn              # Normal mode
./veinborn --debug      # Debug logging
./veinborn --safe       # Terminal reset on crash
```

### Multiplayer (NEW!)
```bash
# Terminal 1: Start server
python3 src/server/run_server.py

# Terminal 2: Connect player 1
python3 src/server/test_client.py

# Terminal 3: Connect player 2
python3 src/server/test_client.py
```

**Then:** Create game → Join → Ready → Start → Play together!

---

## 📚 Key Documentation

| Doc | Purpose | Time to Read |
|-----|---------|--------------|
| **This file** | At-a-glance status | 2 min |
| [PROJECT_STATUS.md](PROJECT_STATUS.md) | Comprehensive status | 10 min |
| [MVP_CURRENT_FOCUS.md](MVP_CURRENT_FOCUS.md) | Current priorities | 5 min |
| [design/MULTIPLAYER_DESIGN_2025.md](design/MULTIPLAYER_DESIGN_2025.md) | Multiplayer design | 30 min |
| [README.md](../README.md) | Project overview | 5 min |
| [START_HERE.md](START_HERE.md) | Developer onboarding | 15 min |

---

## 🔥 Quick Stats

**Development Velocity:**
- **5 PRs merged** in November 2025
- **Phase 2 completed** ahead of schedule (was projected 8-12 weeks!)
- **Dual-track development** now active

**Quality Metrics:**
- **100% test pass rate**
- **5/5 architectural improvements complete**
- **5/5 Lua integration readiness**
- **4.8/5 architecture quality**

**Content:**
- **19 monster types** (exceeds 15-20 goal!)
- **23 recipes** (6 legendary)
- **4 character classes**
- **4 ore types**

---

## 🚨 Known Issues

| Issue | Severity | Status |
|-------|----------|--------|
| 2 skipped Lua timeout tests | 🟡 Low | C-level execution limitation (acceptable) |
| Balance needs tuning | 🟡 Medium | Requires playtesting |
| No tutorial for new players | 🟢 Low | Planned for Phase 3 |

**Critical issues:** None! 🎉

---

## 💡 For New Contributors

**Want to help? Start here:**

1. **Read this dashboard** (you're doing it!)
2. **Play the game** - `./veinborn`
3. **Pick a priority** from "Top 3 Priorities" above
4. **Read the relevant doc** from "Key Documentation"
5. **Start coding!**

**Easy first tasks:**
- Playtest and document balance issues
- Add new monster types to `data/entities/monsters.yaml`
- Add new recipes to `data/balance/recipes.yaml`
- Test multiplayer co-op and report bugs

---

## 📞 Need More Info?

- **Comprehensive status:** [PROJECT_STATUS.md](PROJECT_STATUS.md)
- **Current work:** [MVP_CURRENT_FOCUS.md](MVP_CURRENT_FOCUS.md)
- **Game design:** [VEINBORN_CONSOLIDATED_DESIGN.md](VEINBORN_CONSOLIDATED_DESIGN.md)
- **Architecture:** [architecture/00_ARCHITECTURE_OVERVIEW.md](architecture/00_ARCHITECTURE_OVERVIEW.md)
- **Full doc map:** [INDEX.md](INDEX.md)

---

**🎯 TL;DR (2026-04-17):** Single-player core is healthy and playable (2 minor test-drift failures). Multiplayer Phase 2 is NOT complete — `GameSession` is misaligned with the action contract, `WaitAction` module is missing, and multiple async server tests fail or hang. Focus is on restoring doc accuracy and MP correctness before continuing feature work.

---

**Last Updated:** 2025-11-14
**Next Update:** After extended multiplayer testing session
