import matplotlib.pyplot as plt
import numpy as np
import math

PI = np.pi


def arrow(ax, x, y, theta, L, c):
    angle = np.deg2rad(30)
    d = 0.3 * L
    w = 2

    x_start = x
    y_start = y
    x_end = x + L * np.cos(theta)
    y_end = y + L * np.sin(theta)

    theta_hat_L = theta + PI - angle
    theta_hat_R = theta + PI + angle

    x_hat_start = x_end
    x_hat_end_L = x_hat_start + d * np.cos(theta_hat_L)
    x_hat_end_R = x_hat_start + d * np.cos(theta_hat_R)

    y_hat_start = y_end
    y_hat_end_L = y_hat_start + d * np.sin(theta_hat_L)
    y_hat_end_R = y_hat_start + d * np.sin(theta_hat_R)

    ax.plot([x_start, x_end], [y_start, y_end], color=c, linewidth=w)
    ax.plot([x_hat_start, x_hat_end_L],
             [y_hat_start, y_hat_end_L], color=c, linewidth=w)
    ax.plot([x_hat_start, x_hat_end_R],
             [y_hat_start, y_hat_end_R], color=c, linewidth=w)


def draw_car(ax, x, y, yaw, steer, C, color='black'):
    car = np.array([[-C.RB, -C.RB, C.RF, C.RF, -C.RB],
                    [C.W / 2, -C.W / 2, -C.W / 2, C.W / 2, C.W / 2]])

    wheel = np.array([[-C.TR, -C.TR, C.TR, C.TR, -C.TR],
                      [C.TW / 4, -C.TW / 4, -C.TW / 4, C.TW / 4, C.TW / 4]])

    rlWheel = wheel.copy()
    rrWheel = wheel.copy()
    frWheel = wheel.copy()
    flWheel = wheel.copy()

    Rot1 = np.array([[math.cos(yaw), -math.sin(yaw)],
                     [math.sin(yaw), math.cos(yaw)]])

    Rot2 = np.array([[math.cos(steer), math.sin(steer)],
                     [-math.sin(steer), math.cos(steer)]])

    frWheel = np.dot(Rot2, frWheel)
    flWheel = np.dot(Rot2, flWheel)

    frWheel += np.array([[C.WB], [-C.WD / 2]])
    flWheel += np.array([[C.WB], [C.WD / 2]])
    rrWheel[1, :] -= C.WD / 2
    rlWheel[1, :] += C.WD / 2

    frWheel = np.dot(Rot1, frWheel)
    flWheel = np.dot(Rot1, flWheel)

    rrWheel = np.dot(Rot1, rrWheel)
    rlWheel = np.dot(Rot1, rlWheel)
    car = np.dot(Rot1, car)

    frWheel += np.array([[x], [y]])
    flWheel += np.array([[x], [y]])
    rrWheel += np.array([[x], [y]])
    rlWheel += np.array([[x], [y]])
    car += np.array([[x], [y]])

    ax.plot(car[0, :], car[1, :], color)
    ax.plot(frWheel[0, :], frWheel[1, :], color)
    ax.plot(rrWheel[0, :], rrWheel[1, :], color)
    ax.plot(flWheel[0, :], flWheel[1, :], color)
    ax.plot(rlWheel[0, :], rlWheel[1, :], color)
    arrow(ax, x, y, yaw, C.WB * 0.8, color)


def display_traj(ax, traj_profile):
    # ax.set_ylim(0, 120)
    ax.plot(np.array(traj_profile)[:,3])

