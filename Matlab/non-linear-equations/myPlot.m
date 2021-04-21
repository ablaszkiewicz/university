function myPlot(name, xlabel_name, ylabel_name, x, y)
    plot(x, y);
    title(name);
    xlabel(xlabel_name);
    ylabel(ylabel_name);
    saveas(gcf, strcat(name));
end