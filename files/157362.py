<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab.3"/>
        <attribute name="authors" value="Admin"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 08:25:15 PM"/>
        <attribute name="created" value="QWRtaW47REVTS1RPUC1GRVNPSFVUOzI1NjgtMDctMTc7MDg6MTY6NTUgUE07MjkxOQ=="/>
        <attribute name="edited" value="QWRtaW47REVTS1RPUC1GRVNPSFVUOzI1NjgtMDctMTc7MDg6MjU6MTUgUE07MTszMDIz"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="nn, n, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="n"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="nn"/>
            <output expression="n" newline="True"/>
            <while expression="n &lt; nn">
                <output expression="(n+1)" newline="True"/>
                <assign variable="n" expression="n+1"/>
            </while>
        </body>
    </function>
</flowgorithm>