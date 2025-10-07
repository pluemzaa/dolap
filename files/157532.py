<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="2-683380471-6"/>
        <attribute name="authors" value="HP"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 04:11:55 PM"/>
        <attribute name="created" value="SFA7V0lOMTE7MjU2OC0wNy0yMDswODo0NToyMiBQTTsxNzgz"/>
        <attribute name="edited" value="SFA7V0lOMTE7MjU2OC0wNy0yMjswNDoxMTo1NSBQTTs3OzE4OTQ="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, years, i" type="Real" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <for variable="i" start="1" end="years" direction="inc" step="1">
                <assign variable="money" expression="money * (1 + interest / 100)"/>
                <output expression="&quot;Year &quot; &amp; i &amp; &quot;: &quot; &amp; money" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>