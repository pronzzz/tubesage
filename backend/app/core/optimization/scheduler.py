from typing import List, Callable, Any

class BatchScheduler:
    def __init__(self, batch_size: int = 50):
        self.batch_size = batch_size

    async def execute_batch(self, items: List[str], fetch_func: Callable[[List[str]], Any]) -> List[Any]:
        """
        Splits items into chunks and executes fetch_func for each chunk.
        fetch_func must accept a list of IDs and return results.
        """
        results = []
        
        for i in range(0, len(items), self.batch_size):
            chunk = items[i : i + self.batch_size]
            if not chunk:
                continue
                
            # Execute batch request
            # In a real async loop we might gather these concurrenty
            batch_result = await fetch_func(chunk)
            if isinstance(batch_result, list):
                results.extend(batch_result)
            else:
                results.append(batch_result)
                
        return results

batch_scheduler = BatchScheduler()
