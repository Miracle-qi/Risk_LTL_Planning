# author: Shuhao Qi
# Email: s.qi@tue.nl
# Date: August 6nd, 2023

import matplotlib.pyplot as plt
import numpy as np

from sim.visualizer import Visualizer
import sim.simulator as sim
from risk_LP.risk_LP import RiskLP
import risk_field.risk_field as rf
from risk_LP.prod_auto import Product
from specification.specification import LTL_Spec
from risk_LP.abstraction import Abstraction
from controller import MPC


def main():

    # ---------- Environment Setting ---------------------
    params = {"dt": 0.1, "WB": 1.5}
    car_state = np.array([2, 2, np.pi/2])
    prod_state = (0, 1,  1)
    region_size = (25, 25)
    label_func = {(15, 20, 15, 20): "t",
                  (10, 15, 10, 15): "o"}
    cost_func = {"co_safe": 0, "safe": 10}
    region_res = (5, 5)

    # ---------- Specification Define --------------------
    safe_frag = LTL_Spec("G(!o)")
    scltl_frag = LTL_Spec("F(t)")

    # ---------- Realtime States ---------------------
    fig = plt.figure()
    grid = plt.GridSpec(2, 2)
    ax_1 = fig.add_subplot(grid[0:, 0])
    plt.axis('off')
    plt.axis('equal')
    ax_2 = fig.add_subplot(grid[0, 1], projection='3d')
    ax_3 = fig.add_subplot(grid[1, 1])
    ax_3.axis('off')

    vis = Visualizer(ax_1)
    LP_prob = RiskLP()
    mpc_con = MPC(params, horizon_steps=5)
    car_pos = car_state[:2]
    abs_state = [-1, -1]
    target_abs_state = None

    # ----------- Abstraction -----------------------------
    abs_model = Abstraction(region_size, region_res, car_pos, label_func)
    MDP = abs_model.MDP
    prod_auto = Product(MDP, scltl_frag.dfa, safe_frag.dfa)
    P_matrix = prod_auto.prod_transitions
    cost_map = prod_auto.gen_cost_map(cost_func)
    while True:
        ax_1.cla()
        ax_2.cla()
        ax_1.set_aspect(1)
        car_pos = car_state[:2]

        abs_model.update_abs_state(car_pos)
        if abs_state != abs_model.init_abs_state:
            abs_state_index, abs_state = abs_model.get_abs_state(car_pos)
            prod_state_index, prod_state  = prod_auto.update_prod_state(abs_state_index, prod_state)
            occ_measure = LP_prob.solve_2(P_matrix, cost_map, prod_state_index, prod_auto.accepting_states, prod_auto.trap_states)
            optimal_policy, Z = LP_prob.extract(occ_measure)
            decision_index = optimal_policy[prod_state_index]
            decision = abs_model.action_set[int(decision_index)]
            target_abs_state = abs_state + decision

        target_point = target_abs_state * 5 + np.array([2.5, 2.5])
        control_input = mpc_con.solve(car_state, target_point)
        print("control_input:", control_input)
        print("decision:", decision)
        print("target_point", target_point)
        for i in range(2):
            car_state = sim.car_dyn(car_state, control_input, params['dt'])

        plt.gca().set_aspect(1)
        vis.plot_grid(region_size, region_res, label_func)
        vis.plot_car(car_pos[0], car_pos[1], car_state[2], 0)
        plt.pause(0.001)


if __name__ == '__main__':
    main()