// Exact component body extracted from the verified registered catalog.
// The full unchanged catalog is preserved in baseline/.
import {splitTypographyProps,usePageTypography,type PageTypographyProps} from "../baseline/src/shaders/landing-pages/pageTypography";
import {LandingPageFrame,type LandingPageProps} from "../baseline/src/shaders/landing-pages/LandingPageFrame";
import {MENG_TO_SKETCHBOOK_TYPOGRAPHY} from "../baseline/src/shaders/landing-pages/pageRecipes";

export function MengToSketchbookLandingPage(props: LandingPageProps & PageTypographyProps) {
  const [type, frame] = splitTypographyProps(props);
  const customization = usePageTypography(MENG_TO_SKETCHBOOK_TYPOGRAPHY, type);
  return <LandingPageFrame {...frame} customization={customization} title="Meng To — Singapore Sketchbook" sourceUrl="/landing-pages/meng-to-sketchbook.html" />;
}
