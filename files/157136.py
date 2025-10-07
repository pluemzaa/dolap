<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Compound Interesttan"/>
        <attribute name="authors" value="Lenovo"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 06:15:04 PM"/>
        <attribute name="created" value="TGVub3ZvO0xBUFRPUC01U1Q1MjVRTzsyNTY4LTA3LTE2OzA1OjQxOjI5IFBNOzI5NzI="/>
        <attribute name="edited" value="TGVub3ZvO0xBUFRPUC01U1Q1MjVRTzsyNTY4LTA3LTE2OzA2OjE1OjA0IFBNOzM7MzA3Nw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="m, in, m1, i" type="Real" array="False" size=""/>
            <declare name="y" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="m"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="in"/>
            <assign variable="in" expression="in * 0.01"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="i"/>
            <assign variable="y" expression="0"/>
            <while expression="i &gt; 0">
                <assign variable="y" expression="y + 1"/>
                <assign variable="m1" expression="m * in"/>
                <assign variable="m" expression="m + m1"/>
                <output expression="&quot;Year&quot;&amp;y&amp;&quot;:&quot;&amp;m" newline="True"/>
                <assign variable="i" expression="i - 1"/>
            </while>
        </body>
    </function>
</flowgorithm>