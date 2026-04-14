# Connecting "Stitch UI" to EatSmart Backend

To connect your frontend (built with Google Stitch or any other framework) to this backend, follow these steps:

## 1. CORS is Enabled
I have already enabled **CORS** in `main.py`. This allows your UI (which might be hosted at a different URL) to make requests to the backend without being blocked by the browser.

## 2. API Endpoint
- **Local Development**: `http://localhost:8000/analyze-food`
- **GCP Deployment**: Once deployed, it will be `https://<your-cloud-run-url>/analyze-food`

## 3. Sample Connection Code (JavaScript/React)
You can use the following code in your UI to call the backend:

```javascript
const analyzeFood = async (foodName, goal) => {
  const BACKEND_URL = "http://localhost:8000"; // Update this after GCP deployment

  try {
    const response = await fetch(`${BACKEND_URL}/analyze-food`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        food_name: foodName,
        user_goal: goal, // "weight loss" or "muscle gain"
      }),
    });

    if (!response.ok) {
      throw new Error("Failed to analyze food");
    }

    const data = await response.json();
    console.log("EatSmart Analysis:", data);
    return data;
  } catch (error) {
    console.error("Error connecting to backend:", error);
  }
};
```

## 4. Managed GCP Deployment (Cloud Run)
Instead of manual scripts, we are using the **"Deploy from repository"** feature.

### Setup Instructions:
1. **Push your code to GitHub**: Ensure your `EatSmart` repo is up to date on GitHub.
2. **Open Cloud Run Console**: Go to [Cloud Run](https://console.cloud.google.com/run).
3. **Set up Continuous Deployment**:
   - Choose **"Continuously deploy from a repository"**.
   - Authenticate with GitHub and select your repo.
   - For **Build Type**, select **Dockerfile** (the one I've provided in the root).
   - Ensure **"Allow unauthenticated invocations"** is checked for public access.
4. **Deploy**: Cloud Run will now rebuild your app every time you push to GitHub!
