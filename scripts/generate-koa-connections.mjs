/** Generate public navigation-only exports from the locally versioned kOA Connections registry.
 * This script reads local JSON only, and deliberately never downloads or certifies audit data.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const source = JSON.parse(fs.readFileSync(path.join(root, "data/koa-connections.registry.json"), "utf8"));
const repositories = source.entities.repositories;
const chains = source.entities.chains;
const paths = source.entities.focus_paths;
const crosswalks = source.relations.editorial_crosswalk_proposals;
const aliases = source.aliases_proposed;
if (repositories.length !== 53 || chains.length !== 24 || paths.length !== 4) {
  throw new Error("Unexpected source counts; review changes before release");
}
const chainIds = new Set(chains.map(c => c.id));
const pathIds = new Set(paths.map(p => p.id));
const repoIds = new Set(repositories.map(r => r.id));
const seenPaths = new Set();
const allowedHosts = new Set(source.publishing_policy.alias_targets_allowlist);
for (const c of crosswalks) {
  if (!chainIds.has(c.from) || !pathIds.has(c.to) || !c.status.startsWith("proposed_")) throw new Error(`Invalid proposed crosswalk ${c.id}`);
}
for (const a of aliases) {
  if (seenPaths.has(a.path) || (!/^\/go\/[a-z0-9_.\/-]+$/.test(a.path) || a.path.includes(".."))) throw new Error(`Invalid/duplicate alias ${a.path}`);
  seenPaths.add(a.path);
  if (a.entity_id && !repoIds.has(a.entity_id)) throw new Error(`Unknown repo in alias ${a.path}`);
  if (a.target.startsWith("/")) {
    if (a.target.startsWith("//")) throw new Error(`Invalid internal alias: ${a.path}`);
  } else {
    const target = new URL(a.target);
    if (target.protocol !== "https:" || !allowedHosts.has(target.hostname)) throw new Error(`Disallowed redirect: ${a.path}`);
  }
}
const pick = (obj, keys) => Object.fromEntries(keys.map(key => [key, obj[key] ?? null]));
const publicRegistry = {
  schema: "koa.connections.public-navigation.v1",
  language: "en", brand_color: "#1E6864", release_mode: "local_package_only",
  qualification_notice: "Navigation equivalences are not integration evidence. Target design, public audit records and proposed editorial crosswalks remain distinct.",
  source_snapshots: source.source_snapshots,
  repositories: repositories.map(r => pick(r, ["id","repository","name","admission","in_target_design","in_audit_reference_inventory","target_family","target_role","audit_slug","audit_app_url"])),
  chains: chains.map(c => pick(c, ["id","title_en","outcome","status_raw","href"])),
  paths: paths.map(p => pick(p, ["id","title_en","summary_en","audit_url","spine_repositories"])),
  crosswalks: crosswalks.map(c => pick(c, ["id","from","to","relation","status","editorial_note"])),
  aliases: aliases.map(a => pick(a, ["path","target","kind","entity_id"])),
  relation_counts: Object.fromEntries(Object.entries(source.relations).map(([key,list]) => [key,list.length])),
};
const output = JSON.stringify(publicRegistry, null, 2) + "\n";
const destinations = fs.existsSync(path.join(root, "app"))
  ? ["lib/koa-connections-public.json", "public/data/koa-connections.json"]
  : ["docs/data/koa-connections.json"];
for (const rel of destinations) {
  const dest = path.join(root, rel);
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  fs.writeFileSync(dest, output);
  console.log("Generated", rel);
}
