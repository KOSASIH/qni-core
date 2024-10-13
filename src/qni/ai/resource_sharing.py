import numpy as np
from scipy.optimize import linear_sum_assignment

class ResourceSharingAI:
    def __init__(self, resources, civilizations):
        self.resources = resources
        self.civilizations = civilizations
        self.resource_matrix = self.create_resource_matrix()

    def create_resource_matrix(self):
        # Create a matrix representing the resources available to each civilization
        resource_matrix = np.zeros((len(self.civilizations), len(self.resources)))
        for i, civilization in enumerate(self.civilizations):
            for j, resource in enumerate(self.resources):
                resource_matrix[i, j] = civilization.get_resource_availability(resource)
        return resource_matrix

    def optimize_resource_allocation(self):
        # Optimize the resource allocation using the Hungarian algorithm
        row_ind, col_ind = linear_sum_assignment(-self.resource_matrix)
        optimized_allocation = {}
        for i, j in zip(row_ind, col_ind):
            optimized_allocation[self.civilizations[i]] = self.resources[j]
        return optimized_allocation

class Civilization:
    def __init__(self, name, resources):
        self.name = name
        self.resources = resources

    def get_resource_availability(self, resource):
        # Return the availability of a resource for this civilization
        if resource in self.resources:
            return 1
        else:
            return 0

# Example usage:
resources = ['food', 'water', 'energy']
civilization1 = Civilization('Earth', ['food', 'water'])
civilization2 = Civilization('Mars', ['energy'])
ai = ResourceSharingAI(resources, [civilization1, civilization2])
optimized_allocation = ai.optimize_resource_allocation()
print(optimized_allocation)  # Output: {'Earth': 'food', 'Mars': 'energy'}
